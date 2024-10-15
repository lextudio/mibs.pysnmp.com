# SNMP MIB module (ZHONE-COM-BRIDGE-REC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-COM-BRIDGE-REC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:09 2024
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
 ifAlias,
 ifIndex,
 ifPhysAddress) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifAlias",
    "ifIndex",
    "ifPhysAddress")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(zhone,
 zhoneBridge,
 zhoneModules) = mibBuilder.importSymbols(
    "Zhone",
    "zhone",
    "zhoneBridge",
    "zhoneModules")

(ZhoneAdminString,
 ZhoneRowStatus) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneAdminString",
    "ZhoneRowStatus")


# MODULE-IDENTITY

bridgeRecord = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 77)
)
bridgeRecord.setRevisions(
        ("2014-11-11 07:01",
         "2014-09-06 05:32",
         "2014-05-16 05:58",
         "2014-04-07 10:38",
         "2013-11-12 08:56",
         "2013-10-10 11:21",
         "2013-08-14 03:51",
         "2013-06-18 11:03",
         "2013-06-14 12:08",
         "2013-06-06 21:02",
         "2013-05-10 03:59",
         "2013-02-20 13:34",
         "2012-10-22 15:59",
         "2012-06-12 12:40",
         "2012-04-11 14:44",
         "2012-03-15 07:04",
         "2012-03-06 09:05",
         "2012-01-26 17:35",
         "2011-11-15 17:59",
         "2011-09-20 02:49",
         "2011-07-06 17:07",
         "2011-06-21 11:46",
         "2011-06-16 21:07",
         "2011-05-15 10:35",
         "2011-02-15 17:16",
         "2011-01-31 21:16",
         "2010-08-31 17:26",
         "2010-08-16 12:47",
         "2010-07-30 12:07",
         "2010-03-17 10:32",
         "2010-02-08 15:08",
         "2010-02-08 15:07",
         "2010-02-08 15:05",
         "2010-02-08 14:55",
         "2009-09-16 16:35",
         "2009-09-10 16:49",
         "2009-07-06 16:21",
         "2009-06-26 10:42",
         "2009-05-01 15:21",
         "2009-03-23 16:23",
         "2009-02-13 16:50",
         "2009-01-14 13:24",
         "2008-11-04 09:54",
         "2008-04-18 14:29",
         "2008-01-10 16:28",
         "2007-11-21 07:23",
         "2007-11-12 14:21",
         "2007-11-08 13:08",
         "2007-10-10 15:28",
         "2007-09-25 09:31",
         "2007-07-18 16:04",
         "2007-04-16 17:36",
         "2007-04-11 12:22",
         "2006-11-27 09:25",
         "2006-09-10 10:02",
         "2006-04-26 15:51",
         "2006-02-01 14:19",
         "2006-01-20 15:00",
         "2005-11-11 16:46",
         "2005-08-01 12:13",
         "2005-07-20 17:13",
         "2004-12-17 15:06",
         "2004-06-02 16:09",
         "2004-04-15 13:26",
         "2004-02-01 13:21",
         "2003-10-07 14:22",
         "2003-09-22 09:32",
         "2003-07-29 19:21",
         "2001-09-18 11:00")
)


# Types definitions



class NetworkAddress(OctetString):
    """Custom type NetworkAddress based on OctetString"""



# TEXTUAL-CONVENTIONS



class PacketRuleGroupIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class EapsState(Integer32, TextualConvention):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("complete", 1),
          ("failed", 2),
          ("idle", 0),
          ("init", 6),
          ("link-down", 4),
          ("links-up", 3),
          ("preForwarding", 5))
    )



class BridgeState(Integer32, TextualConvention):
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("adminDown", 6),
          ("adminStateNone", 8),
          ("adminStateTest", 7),
          ("blocked", 12),
          ("blockedFlapping", 17),
          ("blockedFlappingPersistent", 19),
          ("blockedPersistent", 18),
          ("disabled", 14),
          ("discovering", 10),
          ("down", 2),
          ("forwarding", 16),
          ("initializing", 5),
          ("learning", 15),
          ("notAvailable", 4),
          ("pending", 13),
          ("ready", 9),
          ("trouble", 3),
          ("unknown", 11),
          ("up", 1))
    )



# MIB Managed Objects in the order of their OIDs

_BridgeInterfaceTable_Object = MibTable
bridgeInterfaceTable = _BridgeInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2)
)
if mibBuilder.loadTexts:
    bridgeInterfaceTable.setStatus("current")
_BridgeInterfaceEntry_Object = MibTableRow
bridgeInterfaceEntry = _BridgeInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1)
)
bridgeInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    bridgeInterfaceEntry.setStatus("current")


class _BridgeIfVpi_Type(AtmVpIdentifier):
    """Custom type bridgeIfVpi based on AtmVpIdentifier"""
    defaultValue = 0


_BridgeIfVpi_Object = MibTableColumn
bridgeIfVpi = _BridgeIfVpi_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 1),
    _BridgeIfVpi_Type()
)
bridgeIfVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfVpi.setStatus("current")
_BridgeIfVci_Type = AtmVcIdentifier
_BridgeIfVci_Object = MibTableColumn
bridgeIfVci = _BridgeIfVci_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 2),
    _BridgeIfVci_Type()
)
bridgeIfVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfVci.setStatus("current")


class _BridgeIfVlanId_Type(Integer32):
    """Custom type bridgeIfVlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BridgeIfVlanId_Type.__name__ = "Integer32"
_BridgeIfVlanId_Object = MibTableColumn
bridgeIfVlanId = _BridgeIfVlanId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 3),
    _BridgeIfVlanId_Type()
)
bridgeIfVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfVlanId.setStatus("current")


class _BridgeIfStripAndInsert_Type(TruthValue):
    """Custom type bridgeIfStripAndInsert based on TruthValue"""


_BridgeIfStripAndInsert_Object = MibTableColumn
bridgeIfStripAndInsert = _BridgeIfStripAndInsert_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 4),
    _BridgeIfStripAndInsert_Type()
)
bridgeIfStripAndInsert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfStripAndInsert.setStatus("current")


class _BridgeIfCustomARP_Type(TruthValue):
    """Custom type bridgeIfCustomARP based on TruthValue"""


_BridgeIfCustomARP_Object = MibTableColumn
bridgeIfCustomARP = _BridgeIfCustomARP_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 5),
    _BridgeIfCustomARP_Type()
)
bridgeIfCustomARP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfCustomARP.setStatus("current")


class _BridgeIfFilterBroadcast_Type(TruthValue):
    """Custom type bridgeIfFilterBroadcast based on TruthValue"""


_BridgeIfFilterBroadcast_Object = MibTableColumn
bridgeIfFilterBroadcast = _BridgeIfFilterBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 6),
    _BridgeIfFilterBroadcast_Type()
)
bridgeIfFilterBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfFilterBroadcast.setStatus("current")


class _BridgeIfLearnIp_Type(TruthValue):
    """Custom type bridgeIfLearnIp based on TruthValue"""


_BridgeIfLearnIp_Object = MibTableColumn
bridgeIfLearnIp = _BridgeIfLearnIp_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 7),
    _BridgeIfLearnIp_Type()
)
bridgeIfLearnIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfLearnIp.setStatus("current")


class _BridgeIfLearnUnicast_Type(TruthValue):
    """Custom type bridgeIfLearnUnicast based on TruthValue"""


_BridgeIfLearnUnicast_Object = MibTableColumn
bridgeIfLearnUnicast = _BridgeIfLearnUnicast_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 8),
    _BridgeIfLearnUnicast_Type()
)
bridgeIfLearnUnicast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfLearnUnicast.setStatus("current")


class _BridgeIfMaxUnicast_Type(Integer32):
    """Custom type bridgeIfMaxUnicast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BridgeIfMaxUnicast_Type.__name__ = "Integer32"
_BridgeIfMaxUnicast_Object = MibTableColumn
bridgeIfMaxUnicast = _BridgeIfMaxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 9),
    _BridgeIfMaxUnicast_Type()
)
bridgeIfMaxUnicast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfMaxUnicast.setStatus("current")


class _BridgeIfLearnMulticast_Type(TruthValue):
    """Custom type bridgeIfLearnMulticast based on TruthValue"""


_BridgeIfLearnMulticast_Object = MibTableColumn
bridgeIfLearnMulticast = _BridgeIfLearnMulticast_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 10),
    _BridgeIfLearnMulticast_Type()
)
bridgeIfLearnMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfLearnMulticast.setStatus("current")


class _BridgeIfForwardToUnicast_Type(TruthValue):
    """Custom type bridgeIfForwardToUnicast based on TruthValue"""


_BridgeIfForwardToUnicast_Object = MibTableColumn
bridgeIfForwardToUnicast = _BridgeIfForwardToUnicast_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 11),
    _BridgeIfForwardToUnicast_Type()
)
bridgeIfForwardToUnicast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfForwardToUnicast.setStatus("current")


class _BridgeIfForwardToMulticast_Type(TruthValue):
    """Custom type bridgeIfForwardToMulticast based on TruthValue"""


_BridgeIfForwardToMulticast_Object = MibTableColumn
bridgeIfForwardToMulticast = _BridgeIfForwardToMulticast_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 12),
    _BridgeIfForwardToMulticast_Type()
)
bridgeIfForwardToMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfForwardToMulticast.setStatus("current")


class _BridgeIfForwardToDefault_Type(TruthValue):
    """Custom type bridgeIfForwardToDefault based on TruthValue"""


_BridgeIfForwardToDefault_Object = MibTableColumn
bridgeIfForwardToDefault = _BridgeIfForwardToDefault_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 13),
    _BridgeIfForwardToDefault_Type()
)
bridgeIfForwardToDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfForwardToDefault.setStatus("current")
_BridgeLowerIfIndex_Type = InterfaceIndex
_BridgeLowerIfIndex_Object = MibTableColumn
bridgeLowerIfIndex = _BridgeLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 14),
    _BridgeLowerIfIndex_Type()
)
bridgeLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeLowerIfIndex.setStatus("current")


class _BridgeIfRowStatus_Type(ZhoneRowStatus):
    """Custom type bridgeIfRowStatus based on ZhoneRowStatus"""


_BridgeIfRowStatus_Object = MibTableColumn
bridgeIfRowStatus = _BridgeIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 15),
    _BridgeIfRowStatus_Type()
)
bridgeIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfRowStatus.setStatus("current")


class _BridgeIfCustomDHCP_Type(TruthValue):
    """Custom type bridgeIfCustomDHCP based on TruthValue"""


_BridgeIfCustomDHCP_Object = MibTableColumn
bridgeIfCustomDHCP = _BridgeIfCustomDHCP_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 16),
    _BridgeIfCustomDHCP_Type()
)
bridgeIfCustomDHCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfCustomDHCP.setStatus("current")
_BridgeIfIngressPacketRuleGroupIndex_Type = PacketRuleGroupIndex
_BridgeIfIngressPacketRuleGroupIndex_Object = MibTableColumn
bridgeIfIngressPacketRuleGroupIndex = _BridgeIfIngressPacketRuleGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 17),
    _BridgeIfIngressPacketRuleGroupIndex_Type()
)
bridgeIfIngressPacketRuleGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfIngressPacketRuleGroupIndex.setStatus("current")


class _BridgeIfVlanIdCOS_Type(Integer32):
    """Custom type bridgeIfVlanIdCOS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BridgeIfVlanIdCOS_Type.__name__ = "Integer32"
_BridgeIfVlanIdCOS_Object = MibTableColumn
bridgeIfVlanIdCOS = _BridgeIfVlanIdCOS_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 18),
    _BridgeIfVlanIdCOS_Type()
)
bridgeIfVlanIdCOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfVlanIdCOS.setStatus("current")


class _BridgeIfOutgoingCOSOption_Type(Integer32):
    """Custom type bridgeIfOutgoingCOSOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("outgoingCOSOptionAll", 2),
          ("outgoingCOSOptionDisable", 1))
    )


_BridgeIfOutgoingCOSOption_Type.__name__ = "Integer32"
_BridgeIfOutgoingCOSOption_Object = MibTableColumn
bridgeIfOutgoingCOSOption = _BridgeIfOutgoingCOSOption_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 19),
    _BridgeIfOutgoingCOSOption_Type()
)
bridgeIfOutgoingCOSOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfOutgoingCOSOption.setStatus("current")


class _BridgeIfOutgoingCOSValue_Type(Integer32):
    """Custom type bridgeIfOutgoingCOSValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BridgeIfOutgoingCOSValue_Type.__name__ = "Integer32"
_BridgeIfOutgoingCOSValue_Object = MibTableColumn
bridgeIfOutgoingCOSValue = _BridgeIfOutgoingCOSValue_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 20),
    _BridgeIfOutgoingCOSValue_Type()
)
bridgeIfOutgoingCOSValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfOutgoingCOSValue.setStatus("current")


class _BridgeIfStagTPID_Type(Integer32):
    """Custom type bridgeIfStagTPID based on Integer32"""
    defaultHexValue = 33024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(33024, 33024),
        ValueRangeConstraint(34984, 34984),
        ValueRangeConstraint(37120, 37120),
        ValueRangeConstraint(37376, 37376),
    )


_BridgeIfStagTPID_Type.__name__ = "Integer32"
_BridgeIfStagTPID_Object = MibTableColumn
bridgeIfStagTPID = _BridgeIfStagTPID_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 21),
    _BridgeIfStagTPID_Type()
)
bridgeIfStagTPID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfStagTPID.setStatus("current")


class _BridgeIfStagId_Type(Integer32):
    """Custom type bridgeIfStagId based on Integer32"""
    defaultHexValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_BridgeIfStagId_Type.__name__ = "Integer32"
_BridgeIfStagId_Object = MibTableColumn
bridgeIfStagId = _BridgeIfStagId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 22),
    _BridgeIfStagId_Type()
)
bridgeIfStagId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfStagId.setStatus("current")


class _BridgeIfStagStripAndInsert_Type(TruthValue):
    """Custom type bridgeIfStagStripAndInsert based on TruthValue"""


_BridgeIfStagStripAndInsert_Object = MibTableColumn
bridgeIfStagStripAndInsert = _BridgeIfStagStripAndInsert_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 23),
    _BridgeIfStagStripAndInsert_Type()
)
bridgeIfStagStripAndInsert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfStagStripAndInsert.setStatus("current")


class _BridgeIfStagOutgoingCOSOption_Type(Integer32):
    """Custom type bridgeIfStagOutgoingCOSOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sTagCOSAll", 2),
          ("sTagCOSDisable", 1))
    )


_BridgeIfStagOutgoingCOSOption_Type.__name__ = "Integer32"
_BridgeIfStagOutgoingCOSOption_Object = MibTableColumn
bridgeIfStagOutgoingCOSOption = _BridgeIfStagOutgoingCOSOption_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 24),
    _BridgeIfStagOutgoingCOSOption_Type()
)
bridgeIfStagOutgoingCOSOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfStagOutgoingCOSOption.setStatus("current")


class _BridgeIfStagCOS_Type(Integer32):
    """Custom type bridgeIfStagCOS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BridgeIfStagCOS_Type.__name__ = "Integer32"
_BridgeIfStagCOS_Object = MibTableColumn
bridgeIfStagCOS = _BridgeIfStagCOS_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 25),
    _BridgeIfStagCOS_Type()
)
bridgeIfStagCOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfStagCOS.setStatus("current")


class _BridgeIfStagOutgoingCOSValue_Type(Integer32):
    """Custom type bridgeIfStagOutgoingCOSValue based on Integer32"""
    defaultHexValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BridgeIfStagOutgoingCOSValue_Type.__name__ = "Integer32"
_BridgeIfStagOutgoingCOSValue_Object = MibTableColumn
bridgeIfStagOutgoingCOSValue = _BridgeIfStagOutgoingCOSValue_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 26),
    _BridgeIfStagOutgoingCOSValue_Type()
)
bridgeIfStagOutgoingCOSValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfStagOutgoingCOSValue.setStatus("current")
_BridgeIfMcastControlList_Type = SnmpAdminString
_BridgeIfMcastControlList_Object = MibTableColumn
bridgeIfMcastControlList = _BridgeIfMcastControlList_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 27),
    _BridgeIfMcastControlList_Type()
)
bridgeIfMcastControlList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfMcastControlList.setStatus("current")


class _BridgeIfMaxVideoStreams_Type(Unsigned32):
    """Custom type bridgeIfMaxVideoStreams based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_BridgeIfMaxVideoStreams_Type.__name__ = "Unsigned32"
_BridgeIfMaxVideoStreams_Object = MibTableColumn
bridgeIfMaxVideoStreams = _BridgeIfMaxVideoStreams_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 28),
    _BridgeIfMaxVideoStreams_Type()
)
bridgeIfMaxVideoStreams.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfMaxVideoStreams.setStatus("current")


class _BridgeIfIsPPPoA_Type(TruthValue):
    """Custom type bridgeIfIsPPPoA based on TruthValue"""


_BridgeIfIsPPPoA_Object = MibTableColumn
bridgeIfIsPPPoA = _BridgeIfIsPPPoA_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 29),
    _BridgeIfIsPPPoA_Type()
)
bridgeIfIsPPPoA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfIsPPPoA.setStatus("current")


class _BridgeIfFloodUnknown_Type(TruthValue):
    """Custom type bridgeIfFloodUnknown based on TruthValue"""


_BridgeIfFloodUnknown_Object = MibTableColumn
bridgeIfFloodUnknown = _BridgeIfFloodUnknown_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 30),
    _BridgeIfFloodUnknown_Type()
)
bridgeIfFloodUnknown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfFloodUnknown.setStatus("current")


class _BridgeIfFloodMulticast_Type(TruthValue):
    """Custom type bridgeIfFloodMulticast based on TruthValue"""


_BridgeIfFloodMulticast_Object = MibTableColumn
bridgeIfFloodMulticast = _BridgeIfFloodMulticast_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 31),
    _BridgeIfFloodMulticast_Type()
)
bridgeIfFloodMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfFloodMulticast.setStatus("current")
_BridgeIfEgressPacketRuleGroupIndex_Type = PacketRuleGroupIndex
_BridgeIfEgressPacketRuleGroupIndex_Object = MibTableColumn
bridgeIfEgressPacketRuleGroupIndex = _BridgeIfEgressPacketRuleGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 32),
    _BridgeIfEgressPacketRuleGroupIndex_Type()
)
bridgeIfEgressPacketRuleGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfEgressPacketRuleGroupIndex.setStatus("current")


class _BridgeIfTableBasedFilter_Type(Bits):
    """Custom type bridgeIfTableBasedFilter based on Bits"""
    namedValues = NamedValues(
        *(("ip", 1),
          ("mac", 0))
    )

_BridgeIfTableBasedFilter_Type.__name__ = "Bits"
_BridgeIfTableBasedFilter_Object = MibTableColumn
bridgeIfTableBasedFilter = _BridgeIfTableBasedFilter_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 33),
    _BridgeIfTableBasedFilter_Type()
)
bridgeIfTableBasedFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfTableBasedFilter.setStatus("current")


class _BridgeIfDhcpLearn_Type(Bits):
    """Custom type bridgeIfDhcpLearn based on Bits"""
    namedValues = NamedValues(
        *(("ip", 1),
          ("mac", 0))
    )

_BridgeIfDhcpLearn_Type.__name__ = "Bits"
_BridgeIfDhcpLearn_Object = MibTableColumn
bridgeIfDhcpLearn = _BridgeIfDhcpLearn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 34),
    _BridgeIfDhcpLearn_Type()
)
bridgeIfDhcpLearn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfDhcpLearn.setStatus("current")


class _BridgeIfOnDemandStatsEnabled_Type(Integer32):
    """Custom type bridgeIfOnDemandStatsEnabled based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bytes", 3),
          ("false", 2),
          ("true", 1))
    )


_BridgeIfOnDemandStatsEnabled_Type.__name__ = "Integer32"
_BridgeIfOnDemandStatsEnabled_Object = MibTableColumn
bridgeIfOnDemandStatsEnabled = _BridgeIfOnDemandStatsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 35),
    _BridgeIfOnDemandStatsEnabled_Type()
)
bridgeIfOnDemandStatsEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfOnDemandStatsEnabled.setStatus("current")


class _BridgeIfMvrVlan_Type(Integer32):
    """Custom type bridgeIfMvrVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_BridgeIfMvrVlan_Type.__name__ = "Integer32"
_BridgeIfMvrVlan_Object = MibTableColumn
bridgeIfMvrVlan = _BridgeIfMvrVlan_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 36),
    _BridgeIfMvrVlan_Type()
)
bridgeIfMvrVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfMvrVlan.setStatus("current")


class _BridgeIfVlanXlateFrom_Type(Integer32):
    """Custom type bridgeIfVlanXlateFrom based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_BridgeIfVlanXlateFrom_Type.__name__ = "Integer32"
_BridgeIfVlanXlateFrom_Object = MibTableColumn
bridgeIfVlanXlateFrom = _BridgeIfVlanXlateFrom_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 37),
    _BridgeIfVlanXlateFrom_Type()
)
bridgeIfVlanXlateFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfVlanXlateFrom.setStatus("current")


class _BridgeIfSlanXlateFrom_Type(Integer32):
    """Custom type bridgeIfSlanXlateFrom based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_BridgeIfSlanXlateFrom_Type.__name__ = "Integer32"
_BridgeIfSlanXlateFrom_Object = MibTableColumn
bridgeIfSlanXlateFrom = _BridgeIfSlanXlateFrom_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 38),
    _BridgeIfSlanXlateFrom_Type()
)
bridgeIfSlanXlateFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfSlanXlateFrom.setStatus("current")
_BridgeIfBridgeState_Type = BridgeState
_BridgeIfBridgeState_Object = MibTableColumn
bridgeIfBridgeState = _BridgeIfBridgeState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 39),
    _BridgeIfBridgeState_Type()
)
bridgeIfBridgeState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeIfBridgeState.setStatus("current")
_BridgeIfUnblock_Type = TruthValue
_BridgeIfUnblock_Object = MibTableColumn
bridgeIfUnblock = _BridgeIfUnblock_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 40),
    _BridgeIfUnblock_Type()
)
bridgeIfUnblock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeIfUnblock.setStatus("current")


class _BridgeType_Type(Integer32):
    """Custom type bridgeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("downlink", 2),
          ("downlinkData", 14),
          ("downlinkP2P", 16),
          ("downlinkPPPoE", 15),
          ("downlinkUpstreamMcast", 18),
          ("downlinkVideo", 13),
          ("downlinkVoice", 17),
          ("intralink", 4),
          ("ipobDownlink", 21),
          ("ipobTls", 19),
          ("ipobUplink", 20),
          ("mvr", 11),
          ("pppoa", 9),
          ("rlink", 8),
          ("tls", 6),
          ("uplink", 1),
          ("user", 12),
          ("wire", 10))
    )


_BridgeType_Type.__name__ = "Integer32"
_BridgeType_Object = MibTableColumn
bridgeType = _BridgeType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 41),
    _BridgeType_Type()
)
bridgeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeType.setStatus("current")


class _BridgeIfGponGemPortId_Type(Unsigned32):
    """Custom type bridgeIfGponGemPortId based on Unsigned32"""
    defaultValue = 0


_BridgeIfGponGemPortId_Object = MibTableColumn
bridgeIfGponGemPortId = _BridgeIfGponGemPortId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 42),
    _BridgeIfGponGemPortId_Type()
)
bridgeIfGponGemPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeIfGponGemPortId.setStatus("current")


class _BridgeIfGponTrafficProfile_Type(Unsigned32):
    """Custom type bridgeIfGponTrafficProfile based on Unsigned32"""
    defaultValue = 0


_BridgeIfGponTrafficProfile_Object = MibTableColumn
bridgeIfGponTrafficProfile = _BridgeIfGponTrafficProfile_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 43),
    _BridgeIfGponTrafficProfile_Type()
)
bridgeIfGponTrafficProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeIfGponTrafficProfile.setStatus("current")


class _BridgeIfIncomingCOSOption_Type(Integer32):
    """Custom type bridgeIfIncomingCOSOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incomingCOSOptionAll", 2),
          ("incomingCOSOptionDisable", 1))
    )


_BridgeIfIncomingCOSOption_Type.__name__ = "Integer32"
_BridgeIfIncomingCOSOption_Object = MibTableColumn
bridgeIfIncomingCOSOption = _BridgeIfIncomingCOSOption_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 44),
    _BridgeIfIncomingCOSOption_Type()
)
bridgeIfIncomingCOSOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeIfIncomingCOSOption.setStatus("current")


class _BridgeIfStagIncomingCOSOption_Type(Integer32):
    """Custom type bridgeIfStagIncomingCOSOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stagIncomingCOSOptionAll", 2),
          ("stagIncomingCOSOptionDisable", 1))
    )


_BridgeIfStagIncomingCOSOption_Type.__name__ = "Integer32"
_BridgeIfStagIncomingCOSOption_Object = MibTableColumn
bridgeIfStagIncomingCOSOption = _BridgeIfStagIncomingCOSOption_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 2, 1, 45),
    _BridgeIfStagIncomingCOSOption_Type()
)
bridgeIfStagIncomingCOSOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeIfStagIncomingCOSOption.setStatus("current")
_StaticBridgeTable_Object = MibTable
staticBridgeTable = _StaticBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 3)
)
if mibBuilder.loadTexts:
    staticBridgeTable.setStatus("current")
_StaticBridgeEntry_Object = MibTableRow
staticBridgeEntry = _StaticBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 3, 1)
)
staticBridgeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "staticBridgeAddressType"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfVlanId"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "staticBridgeMacOrIpAddress"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfStagId"),
)
if mibBuilder.loadTexts:
    staticBridgeEntry.setStatus("current")


class _StaticBridgeMacOrIpAddress_Type(PhysAddress):
    """Custom type staticBridgeMacOrIpAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_StaticBridgeMacOrIpAddress_Type.__name__ = "PhysAddress"
_StaticBridgeMacOrIpAddress_Object = MibTableColumn
staticBridgeMacOrIpAddress = _StaticBridgeMacOrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 3, 1, 1),
    _StaticBridgeMacOrIpAddress_Type()
)
staticBridgeMacOrIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staticBridgeMacOrIpAddress.setStatus("current")


class _StaticBridgeAddressType_Type(Integer32):
    """Custom type staticBridgeAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7,
              8,
              9,
              10,
              13,
              14,
              15,
              720901)
        )
    )
    namedValues = NamedValues(
        *(("dhcpAllowOui", 720901),
          ("dhcpIpAddr", 9),
          ("dhcpMacAddr", 10),
          ("globalAddr", 4),
          ("globalIntralinkAddr", 8),
          ("intralinkAddr", 7),
          ("ipAddr", 2),
          ("macAddr", 1),
          ("mvrAddr", 13),
          ("secMvrAddr", 15),
          ("vlanIdAddr", 3),
          ("vlanParms", 14))
    )


_StaticBridgeAddressType_Type.__name__ = "Integer32"
_StaticBridgeAddressType_Object = MibTableColumn
staticBridgeAddressType = _StaticBridgeAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 3, 1, 2),
    _StaticBridgeAddressType_Type()
)
staticBridgeAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staticBridgeAddressType.setStatus("current")


class _StaticBridgeMulticastAging_Type(Integer32):
    """Custom type staticBridgeMulticastAging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StaticBridgeMulticastAging_Type.__name__ = "Integer32"
_StaticBridgeMulticastAging_Object = MibTableColumn
staticBridgeMulticastAging = _StaticBridgeMulticastAging_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 3, 1, 3),
    _StaticBridgeMulticastAging_Type()
)
staticBridgeMulticastAging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticBridgeMulticastAging.setStatus("current")


class _StaticBridgeRowStatus_Type(ZhoneRowStatus):
    """Custom type staticBridgeRowStatus based on ZhoneRowStatus"""


_StaticBridgeRowStatus_Object = MibTableColumn
staticBridgeRowStatus = _StaticBridgeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 3, 1, 4),
    _StaticBridgeRowStatus_Type()
)
staticBridgeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticBridgeRowStatus.setStatus("current")


class _StaticBridgeFlapControl_Type(Integer32):
    """Custom type staticBridgeFlapControl based on Integer32"""
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
        *(("default", 1),
          ("disable", 2),
          ("enable", 3),
          ("fast", 4))
    )


_StaticBridgeFlapControl_Type.__name__ = "Integer32"
_StaticBridgeFlapControl_Object = MibTableColumn
staticBridgeFlapControl = _StaticBridgeFlapControl_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 3, 1, 5),
    _StaticBridgeFlapControl_Type()
)
staticBridgeFlapControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticBridgeFlapControl.setStatus("current")


class _StaticBridgeUnicastAging_Type(Integer32):
    """Custom type staticBridgeUnicastAging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 2147483647),
    )


_StaticBridgeUnicastAging_Type.__name__ = "Integer32"
_StaticBridgeUnicastAging_Object = MibTableColumn
staticBridgeUnicastAging = _StaticBridgeUnicastAging_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 3, 1, 6),
    _StaticBridgeUnicastAging_Type()
)
staticBridgeUnicastAging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticBridgeUnicastAging.setStatus("current")


class _StaticBridgeIgmpQueryInterval_Type(Integer32):
    """Custom type staticBridgeIgmpQueryInterval based on Integer32"""
    defaultValue = 0


_StaticBridgeIgmpQueryInterval_Object = MibTableColumn
staticBridgeIgmpQueryInterval = _StaticBridgeIgmpQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 3, 1, 7),
    _StaticBridgeIgmpQueryInterval_Type()
)
staticBridgeIgmpQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticBridgeIgmpQueryInterval.setStatus("current")


class _StaticBridgeFlags_Type(Bits):
    """Custom type staticBridgeFlags based on Bits"""
    namedValues = NamedValues(
        *(("forceIGMPv2Down", 3),
          ("forceIGMPv2Up", 4),
          ("igmpProcessJoinAndLeave", 0),
          ("igmpRespondToQuery", 1),
          ("igmpUseBridgeIpAddress", 2))
    )

_StaticBridgeFlags_Type.__name__ = "Bits"
_StaticBridgeFlags_Object = MibTableColumn
staticBridgeFlags = _StaticBridgeFlags_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 3, 1, 8),
    _StaticBridgeFlags_Type()
)
staticBridgeFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticBridgeFlags.setStatus("current")
_StaticBridgeIgmpCustomIpAddress_Type = IpAddress
_StaticBridgeIgmpCustomIpAddress_Object = MibTableColumn
staticBridgeIgmpCustomIpAddress = _StaticBridgeIgmpCustomIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 3, 1, 9),
    _StaticBridgeIgmpCustomIpAddress_Type()
)
staticBridgeIgmpCustomIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticBridgeIgmpCustomIpAddress.setStatus("current")


class _StaticBridgeLoopPrevention_Type(Integer32):
    """Custom type staticBridgeLoopPrevention based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("blockAll", 2),
          ("blockAllAuto", 4),
          ("blockAsym", 1),
          ("blockAsymAuto", 3),
          ("none", 0))
    )


_StaticBridgeLoopPrevention_Type.__name__ = "Integer32"
_StaticBridgeLoopPrevention_Object = MibTableColumn
staticBridgeLoopPrevention = _StaticBridgeLoopPrevention_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 3, 1, 10),
    _StaticBridgeLoopPrevention_Type()
)
staticBridgeLoopPrevention.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticBridgeLoopPrevention.setStatus("current")


class _StaticBridgeIgmpDscp_Type(OctetString):
    """Custom type staticBridgeIgmpDscp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_StaticBridgeIgmpDscp_Type.__name__ = "OctetString"
_StaticBridgeIgmpDscp_Object = MibTableColumn
staticBridgeIgmpDscp = _StaticBridgeIgmpDscp_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 3, 1, 11),
    _StaticBridgeIgmpDscp_Type()
)
staticBridgeIgmpDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticBridgeIgmpDscp.setStatus("current")
_BridgeIfLookupTable_Object = MibTable
bridgeIfLookupTable = _BridgeIfLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 4)
)
if mibBuilder.loadTexts:
    bridgeIfLookupTable.setStatus("current")
_BridgeIfLookupEntry_Object = MibTableRow
bridgeIfLookupEntry = _BridgeIfLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 4, 1)
)
bridgeIfLookupEntry.setIndexNames(
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfAddressType"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfMacOrIpAddress"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfVlanId"),
    (0, "IF-MIB", "ifIndex"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfStagId"),
)
if mibBuilder.loadTexts:
    bridgeIfLookupEntry.setStatus("current")


class _BridgeIfAddressType_Type(Integer32):
    """Custom type bridgeIfAddressType based on Integer32"""
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
        *(("dhcpIp", 5),
          ("dhcpMac", 4),
          ("dhcpV6Ip", 8),
          ("dhcpV6Mac", 7),
          ("ipAddress", 3),
          ("ipV6Address", 6),
          ("multicastMac", 2),
          ("unicastMac", 1))
    )


_BridgeIfAddressType_Type.__name__ = "Integer32"
_BridgeIfAddressType_Object = MibTableColumn
bridgeIfAddressType = _BridgeIfAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 4, 1, 1),
    _BridgeIfAddressType_Type()
)
bridgeIfAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bridgeIfAddressType.setStatus("current")
_BridgeIfMacOrIpAddress_Type = PhysAddress
_BridgeIfMacOrIpAddress_Object = MibTableColumn
bridgeIfMacOrIpAddress = _BridgeIfMacOrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 4, 1, 2),
    _BridgeIfMacOrIpAddress_Type()
)
bridgeIfMacOrIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bridgeIfMacOrIpAddress.setStatus("current")


class _BridgeIfLookupStaticOrDynamic_Type(Integer32):
    """Custom type bridgeIfLookupStaticOrDynamic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamicEntry", 2),
          ("staticEntry", 1))
    )


_BridgeIfLookupStaticOrDynamic_Type.__name__ = "Integer32"
_BridgeIfLookupStaticOrDynamic_Object = MibTableColumn
bridgeIfLookupStaticOrDynamic = _BridgeIfLookupStaticOrDynamic_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 4, 1, 3),
    _BridgeIfLookupStaticOrDynamic_Type()
)
bridgeIfLookupStaticOrDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeIfLookupStaticOrDynamic.setStatus("current")


class _BridgeIfLookupFlush_Type(TruthValue):
    """Custom type bridgeIfLookupFlush based on TruthValue"""


_BridgeIfLookupFlush_Object = MibTableColumn
bridgeIfLookupFlush = _BridgeIfLookupFlush_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 4, 1, 4),
    _BridgeIfLookupFlush_Type()
)
bridgeIfLookupFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeIfLookupFlush.setStatus("current")
_BridgeAddressLookupTable_Object = MibTable
bridgeAddressLookupTable = _BridgeAddressLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 5)
)
if mibBuilder.loadTexts:
    bridgeAddressLookupTable.setStatus("current")
_BridgeAddressLookupEntry_Object = MibTableRow
bridgeAddressLookupEntry = _BridgeAddressLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 5, 1)
)
bridgeAddressLookupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfAddressType"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfMacOrIpAddress"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfVlanId"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfStagId"),
)
if mibBuilder.loadTexts:
    bridgeAddressLookupEntry.setStatus("current")


class _BridgeAddressLookupStaticOrDynamic_Type(Integer32):
    """Custom type bridgeAddressLookupStaticOrDynamic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamicEntry", 2),
          ("staticEntry", 1))
    )


_BridgeAddressLookupStaticOrDynamic_Type.__name__ = "Integer32"
_BridgeAddressLookupStaticOrDynamic_Object = MibTableColumn
bridgeAddressLookupStaticOrDynamic = _BridgeAddressLookupStaticOrDynamic_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 5, 1, 1),
    _BridgeAddressLookupStaticOrDynamic_Type()
)
bridgeAddressLookupStaticOrDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeAddressLookupStaticOrDynamic.setStatus("current")


class _BridgeAddressLookupFlush_Type(TruthValue):
    """Custom type bridgeAddressLookupFlush based on TruthValue"""


_BridgeAddressLookupFlush_Object = MibTableColumn
bridgeAddressLookupFlush = _BridgeAddressLookupFlush_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 5, 1, 2),
    _BridgeAddressLookupFlush_Type()
)
bridgeAddressLookupFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeAddressLookupFlush.setStatus("current")
_PacketRuleGroup_ObjectIdentity = ObjectIdentity
packetRuleGroup = _PacketRuleGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 6)
)
_PacketRuleGroupIndexNext_Type = PacketRuleGroupIndex
_PacketRuleGroupIndexNext_Object = MibScalar
packetRuleGroupIndexNext = _PacketRuleGroupIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 6, 1),
    _PacketRuleGroupIndexNext_Type()
)
packetRuleGroupIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetRuleGroupIndexNext.setStatus("current")
_PacketRuleGroupNextIndexTable_Object = MibTable
packetRuleGroupNextIndexTable = _PacketRuleGroupNextIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 6, 2)
)
if mibBuilder.loadTexts:
    packetRuleGroupNextIndexTable.setStatus("current")
_PacketRuleGroupNextIndexEntry_Object = MibTableRow
packetRuleGroupNextIndexEntry = _PacketRuleGroupNextIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 6, 2, 1)
)
packetRuleGroupNextIndexEntry.setIndexNames(
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "packetRuleGroupIndex"),
)
if mibBuilder.loadTexts:
    packetRuleGroupNextIndexEntry.setStatus("current")
_PacketRuleGroupMemberNextIndex_Type = PacketRuleGroupIndex
_PacketRuleGroupMemberNextIndex_Object = MibTableColumn
packetRuleGroupMemberNextIndex = _PacketRuleGroupMemberNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 6, 2, 1, 1),
    _PacketRuleGroupMemberNextIndex_Type()
)
packetRuleGroupMemberNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetRuleGroupMemberNextIndex.setStatus("current")
_PacketRuleTable_Object = MibTable
packetRuleTable = _PacketRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 6, 3)
)
if mibBuilder.loadTexts:
    packetRuleTable.setStatus("current")
_PacketRuleEntry_Object = MibTableRow
packetRuleEntry = _PacketRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 6, 3, 1)
)
packetRuleEntry.setIndexNames(
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "packetRuleGroupIndex"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "packetRuleGroupMemberIndex"),
)
if mibBuilder.loadTexts:
    packetRuleEntry.setStatus("current")


class _PacketRuleGroupMemberIndex_Type(Integer32):
    """Custom type packetRuleGroupMemberIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PacketRuleGroupMemberIndex_Type.__name__ = "Integer32"
_PacketRuleGroupMemberIndex_Object = MibTableColumn
packetRuleGroupMemberIndex = _PacketRuleGroupMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 6, 3, 1, 1),
    _PacketRuleGroupMemberIndex_Type()
)
packetRuleGroupMemberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    packetRuleGroupMemberIndex.setStatus("current")


class _PacketRuleType_Type(Integer32):
    """Custom type packetRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(37,
              38,
              41,
              42,
              43,
              44,
              45,
              46,
              97,
              98,
              99,
              100,
              103,
              104,
              114,
              120)
        )
    )
    namedValues = NamedValues(
        *(("aclAllow", 104),
          ("aclDeny", 120),
          ("bridgeForbidOui", 114),
          ("bridgeInsertOption82", 97),
          ("bridgeInsertPPPoEVendorTag", 99),
          ("bridgeStormDetect", 46),
          ("colorAwareRateLimitDiscard", 103),
          ("dhcpRelay", 98),
          ("dscpToCos", 41),
          ("dstMacSwapDynamic", 38),
          ("dstMacSwapStatic", 37),
          ("filterFirstEncapsulationVlan", 43),
          ("filterSecondEncapsulationVlan", 45),
          ("promoteFirstEncapsulationVlan", 42),
          ("promoteSecondEncapsulationVlan", 44),
          ("rateLimitDiscard", 100))
    )


_PacketRuleType_Type.__name__ = "Integer32"
_PacketRuleType_Object = MibTableColumn
packetRuleType = _PacketRuleType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 6, 3, 1, 2),
    _PacketRuleType_Type()
)
packetRuleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    packetRuleType.setStatus("current")
_PacketRuleValue_Type = SnmpAdminString
_PacketRuleValue_Object = MibTableColumn
packetRuleValue = _PacketRuleValue_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 6, 3, 1, 3),
    _PacketRuleValue_Type()
)
packetRuleValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    packetRuleValue.setStatus("current")


class _PacketRuleRowStatus_Type(ZhoneRowStatus):
    """Custom type packetRuleRowStatus based on ZhoneRowStatus"""


_PacketRuleRowStatus_Object = MibTableColumn
packetRuleRowStatus = _PacketRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 6, 3, 1, 4),
    _PacketRuleRowStatus_Type()
)
packetRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    packetRuleRowStatus.setStatus("current")
_PacketRuleValue2_Type = SnmpAdminString
_PacketRuleValue2_Object = MibTableColumn
packetRuleValue2 = _PacketRuleValue2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 6, 3, 1, 5),
    _PacketRuleValue2_Type()
)
packetRuleValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    packetRuleValue2.setStatus("current")
_PacketRuleValue3_Type = SnmpAdminString
_PacketRuleValue3_Object = MibTableColumn
packetRuleValue3 = _PacketRuleValue3_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 6, 3, 1, 6),
    _PacketRuleValue3_Type()
)
packetRuleValue3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    packetRuleValue3.setStatus("current")
_PacketRuleValue4_Type = SnmpAdminString
_PacketRuleValue4_Object = MibTableColumn
packetRuleValue4 = _PacketRuleValue4_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 6, 3, 1, 7),
    _PacketRuleValue4_Type()
)
packetRuleValue4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    packetRuleValue4.setStatus("current")
_PacketRuleValue5_Type = SnmpAdminString
_PacketRuleValue5_Object = MibTableColumn
packetRuleValue5 = _PacketRuleValue5_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 6, 3, 1, 8),
    _PacketRuleValue5_Type()
)
packetRuleValue5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    packetRuleValue5.setStatus("current")


class _PacketRuleGroupIndex_Type(PacketRuleGroupIndex):
    """Custom type packetRuleGroupIndex based on PacketRuleGroupIndex"""
    subtypeSpec = PacketRuleGroupIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PacketRuleGroupIndex_Type.__name__ = "PacketRuleGroupIndex"
_PacketRuleGroupIndex_Object = MibTableColumn
packetRuleGroupIndex = _PacketRuleGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 6, 3, 1, 9),
    _PacketRuleGroupIndex_Type()
)
packetRuleGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    packetRuleGroupIndex.setStatus("current")
_PacketRuleValue6_Type = SnmpAdminString
_PacketRuleValue6_Object = MibTableColumn
packetRuleValue6 = _PacketRuleValue6_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 6, 3, 1, 10),
    _PacketRuleValue6_Type()
)
packetRuleValue6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    packetRuleValue6.setStatus("current")
_PacketRuleValue7_Type = SnmpAdminString
_PacketRuleValue7_Object = MibTableColumn
packetRuleValue7 = _PacketRuleValue7_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 6, 3, 1, 11),
    _PacketRuleValue7_Type()
)
packetRuleValue7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    packetRuleValue7.setStatus("current")
_BridgePPPoETable_Object = MibTable
bridgePPPoETable = _BridgePPPoETable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 7)
)
if mibBuilder.loadTexts:
    bridgePPPoETable.setStatus("current")
_BridgePPPoEEntry_Object = MibTableRow
bridgePPPoEEntry = _BridgePPPoEEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 7, 1)
)
bridgePPPoEEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    bridgePPPoEEntry.setStatus("current")


class _BridgePPPoEBrasMac_Type(OctetString):
    """Custom type bridgePPPoEBrasMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_BridgePPPoEBrasMac_Type.__name__ = "OctetString"
_BridgePPPoEBrasMac_Object = MibTableColumn
bridgePPPoEBrasMac = _BridgePPPoEBrasMac_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 7, 1, 1),
    _BridgePPPoEBrasMac_Type()
)
bridgePPPoEBrasMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgePPPoEBrasMac.setStatus("current")


class _BridgePPPoELocalHostMac_Type(OctetString):
    """Custom type bridgePPPoELocalHostMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_BridgePPPoELocalHostMac_Type.__name__ = "OctetString"
_BridgePPPoELocalHostMac_Object = MibTableColumn
bridgePPPoELocalHostMac = _BridgePPPoELocalHostMac_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 7, 1, 2),
    _BridgePPPoELocalHostMac_Type()
)
bridgePPPoELocalHostMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgePPPoELocalHostMac.setStatus("current")
_BridgePPPoEEIfIndex_Type = InterfaceIndex
_BridgePPPoEEIfIndex_Object = MibTableColumn
bridgePPPoEEIfIndex = _BridgePPPoEEIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 7, 1, 3),
    _BridgePPPoEEIfIndex_Type()
)
bridgePPPoEEIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgePPPoEEIfIndex.setStatus("current")


class _BridgePPPoESessionID_Type(Integer32):
    """Custom type bridgePPPoESessionID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BridgePPPoESessionID_Type.__name__ = "Integer32"
_BridgePPPoESessionID_Object = MibTableColumn
bridgePPPoESessionID = _BridgePPPoESessionID_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 7, 1, 4),
    _BridgePPPoESessionID_Type()
)
bridgePPPoESessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgePPPoESessionID.setStatus("current")


class _BridgePPPoESlanId_Type(Integer32):
    """Custom type bridgePPPoESlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_BridgePPPoESlanId_Type.__name__ = "Integer32"
_BridgePPPoESlanId_Object = MibTableColumn
bridgePPPoESlanId = _BridgePPPoESlanId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 7, 1, 5),
    _BridgePPPoESlanId_Type()
)
bridgePPPoESlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgePPPoESlanId.setStatus("current")


class _BridgePPPoEVlanId_Type(Integer32):
    """Custom type bridgePPPoEVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_BridgePPPoEVlanId_Type.__name__ = "Integer32"
_BridgePPPoEVlanId_Object = MibTableColumn
bridgePPPoEVlanId = _BridgePPPoEVlanId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 7, 1, 6),
    _BridgePPPoEVlanId_Type()
)
bridgePPPoEVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgePPPoEVlanId.setStatus("current")


class _BridgePPPoEEncapLLC_Type(Integer32):
    """Custom type bridgePPPoEEncapLLC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llc", 2),
          ("vcmux", 1))
    )


_BridgePPPoEEncapLLC_Type.__name__ = "Integer32"
_BridgePPPoEEncapLLC_Object = MibTableColumn
bridgePPPoEEncapLLC = _BridgePPPoEEncapLLC_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 7, 1, 7),
    _BridgePPPoEEncapLLC_Type()
)
bridgePPPoEEncapLLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgePPPoEEncapLLC.setStatus("current")
_StpParam_ObjectIdentity = ObjectIdentity
stpParam = _StpParam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 8)
)
_StpParamName_Type = ZhoneAdminString
_StpParamName_Object = MibScalar
stpParamName = _StpParamName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 8, 1),
    _StpParamName_Type()
)
stpParamName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpParamName.setStatus("current")


class _StpParamRevision_Type(Unsigned32):
    """Custom type stpParamRevision based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_StpParamRevision_Type.__name__ = "Unsigned32"
_StpParamRevision_Object = MibScalar
stpParamRevision = _StpParamRevision_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 8, 2),
    _StpParamRevision_Type()
)
stpParamRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpParamRevision.setStatus("current")


class _StpParamBridgePriority_Type(Unsigned32):
    """Custom type stpParamBridgePriority based on Unsigned32"""
    defaultValue = 36864

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4096, 61440),
    )


_StpParamBridgePriority_Type.__name__ = "Unsigned32"
_StpParamBridgePriority_Object = MibScalar
stpParamBridgePriority = _StpParamBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 8, 3),
    _StpParamBridgePriority_Type()
)
stpParamBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpParamBridgePriority.setStatus("current")


class _StpParamForceVersion_Type(Unsigned32):
    """Custom type stpParamForceVersion based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_StpParamForceVersion_Type.__name__ = "Unsigned32"
_StpParamForceVersion_Object = MibScalar
stpParamForceVersion = _StpParamForceVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 8, 4),
    _StpParamForceVersion_Type()
)
stpParamForceVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpParamForceVersion.setStatus("current")


class _StpParamFwdDelay_Type(Unsigned32):
    """Custom type stpParamFwdDelay based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 20),
    )


_StpParamFwdDelay_Type.__name__ = "Unsigned32"
_StpParamFwdDelay_Object = MibScalar
stpParamFwdDelay = _StpParamFwdDelay_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 8, 5),
    _StpParamFwdDelay_Type()
)
stpParamFwdDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpParamFwdDelay.setStatus("current")


class _StpParamHelloTime_Type(Unsigned32):
    """Custom type stpParamHelloTime based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_StpParamHelloTime_Type.__name__ = "Unsigned32"
_StpParamHelloTime_Object = MibScalar
stpParamHelloTime = _StpParamHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 8, 6),
    _StpParamHelloTime_Type()
)
stpParamHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpParamHelloTime.setStatus("current")


class _StpParamMigrateTime_Type(Unsigned32):
    """Custom type stpParamMigrateTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3),
    )


_StpParamMigrateTime_Type.__name__ = "Unsigned32"
_StpParamMigrateTime_Object = MibScalar
stpParamMigrateTime = _StpParamMigrateTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 8, 7),
    _StpParamMigrateTime_Type()
)
stpParamMigrateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpParamMigrateTime.setStatus("current")


class _StpParamTxHoldCount_Type(Unsigned32):
    """Custom type stpParamTxHoldCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_StpParamTxHoldCount_Type.__name__ = "Unsigned32"
_StpParamTxHoldCount_Object = MibScalar
stpParamTxHoldCount = _StpParamTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 8, 8),
    _StpParamTxHoldCount_Type()
)
stpParamTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpParamTxHoldCount.setStatus("current")


class _StpParamMaxAge_Type(Unsigned32):
    """Custom type stpParamMaxAge based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 20),
    )


_StpParamMaxAge_Type.__name__ = "Unsigned32"
_StpParamMaxAge_Object = MibScalar
stpParamMaxAge = _StpParamMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 8, 9),
    _StpParamMaxAge_Type()
)
stpParamMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpParamMaxAge.setStatus("current")
_StpBindTable_Object = MibTable
stpBindTable = _StpBindTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 9)
)
if mibBuilder.loadTexts:
    stpBindTable.setStatus("current")
_StpBindEntry_Object = MibTableRow
stpBindEntry = _StpBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 9, 1)
)
stpBindEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "stpBindInstanceID"),
)
if mibBuilder.loadTexts:
    stpBindEntry.setStatus("current")
_StpBindInstanceID_Type = Unsigned32
_StpBindInstanceID_Object = MibTableColumn
stpBindInstanceID = _StpBindInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 9, 1, 1),
    _StpBindInstanceID_Type()
)
stpBindInstanceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpBindInstanceID.setStatus("current")
_StpBindRowStatus_Type = ZhoneRowStatus
_StpBindRowStatus_Object = MibTableColumn
stpBindRowStatus = _StpBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 9, 1, 2),
    _StpBindRowStatus_Type()
)
stpBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stpBindRowStatus.setStatus("current")


class _StpBindPortPriority_Type(Unsigned32):
    """Custom type stpBindPortPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StpBindPortPriority_Type.__name__ = "Unsigned32"
_StpBindPortPriority_Object = MibTableColumn
stpBindPortPriority = _StpBindPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 9, 1, 3),
    _StpBindPortPriority_Type()
)
stpBindPortPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stpBindPortPriority.setStatus("current")
_MstpInstanceTable_Object = MibTable
mstpInstanceTable = _MstpInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 10)
)
if mibBuilder.loadTexts:
    mstpInstanceTable.setStatus("current")
_MstpInstanceEntry_Object = MibTableRow
mstpInstanceEntry = _MstpInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 10, 1)
)
mstpInstanceEntry.setIndexNames(
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "stpBindInstanceID"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfVlanId"),
)
if mibBuilder.loadTexts:
    mstpInstanceEntry.setStatus("current")
_MstpInstanceRowStatus_Type = ZhoneRowStatus
_MstpInstanceRowStatus_Object = MibTableColumn
mstpInstanceRowStatus = _MstpInstanceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 10, 1, 1),
    _MstpInstanceRowStatus_Type()
)
mstpInstanceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstpInstanceRowStatus.setStatus("current")
_MstpInstanceName_Type = ZhoneAdminString
_MstpInstanceName_Object = MibTableColumn
mstpInstanceName = _MstpInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 10, 1, 2),
    _MstpInstanceName_Type()
)
mstpInstanceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstpInstanceName.setStatus("current")
_BridgeStatsTable_Object = MibTable
bridgeStatsTable = _BridgeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 11)
)
if mibBuilder.loadTexts:
    bridgeStatsTable.setStatus("current")
_BridgeStatsEntry_Object = MibTableRow
bridgeStatsEntry = _BridgeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 11, 1)
)
bridgeStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    bridgeStatsEntry.setStatus("current")
_BridgeStatsUcastRcvd_Type = Unsigned32
_BridgeStatsUcastRcvd_Object = MibTableColumn
bridgeStatsUcastRcvd = _BridgeStatsUcastRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 11, 1, 1),
    _BridgeStatsUcastRcvd_Type()
)
bridgeStatsUcastRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatsUcastRcvd.setStatus("current")
_BridgeStatsMcastRcvd_Type = Unsigned32
_BridgeStatsMcastRcvd_Object = MibTableColumn
bridgeStatsMcastRcvd = _BridgeStatsMcastRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 11, 1, 2),
    _BridgeStatsMcastRcvd_Type()
)
bridgeStatsMcastRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatsMcastRcvd.setStatus("current")
_BridgeStatsBcastRcvd_Type = Unsigned32
_BridgeStatsBcastRcvd_Object = MibTableColumn
bridgeStatsBcastRcvd = _BridgeStatsBcastRcvd_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 11, 1, 3),
    _BridgeStatsBcastRcvd_Type()
)
bridgeStatsBcastRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatsBcastRcvd.setStatus("current")
_BridgeStatsUcastSent_Type = Unsigned32
_BridgeStatsUcastSent_Object = MibTableColumn
bridgeStatsUcastSent = _BridgeStatsUcastSent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 11, 1, 4),
    _BridgeStatsUcastSent_Type()
)
bridgeStatsUcastSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatsUcastSent.setStatus("current")
_BridgeStatsMcastSent_Type = Unsigned32
_BridgeStatsMcastSent_Object = MibTableColumn
bridgeStatsMcastSent = _BridgeStatsMcastSent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 11, 1, 5),
    _BridgeStatsMcastSent_Type()
)
bridgeStatsMcastSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatsMcastSent.setStatus("current")
_BridgeStatsBcastSent_Type = Unsigned32
_BridgeStatsBcastSent_Object = MibTableColumn
bridgeStatsBcastSent = _BridgeStatsBcastSent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 11, 1, 6),
    _BridgeStatsBcastSent_Type()
)
bridgeStatsBcastSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatsBcastSent.setStatus("current")
_BridgeStatsErrorSent_Type = Unsigned32
_BridgeStatsErrorSent_Object = MibTableColumn
bridgeStatsErrorSent = _BridgeStatsErrorSent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 11, 1, 7),
    _BridgeStatsErrorSent_Type()
)
bridgeStatsErrorSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatsErrorSent.setStatus("current")
_BridgeOnDemandStatsRulesSupported_Type = Unsigned32
_BridgeOnDemandStatsRulesSupported_Object = MibTableColumn
bridgeOnDemandStatsRulesSupported = _BridgeOnDemandStatsRulesSupported_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 11, 1, 8),
    _BridgeOnDemandStatsRulesSupported_Type()
)
bridgeOnDemandStatsRulesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeOnDemandStatsRulesSupported.setStatus("current")
_BridgeOnDemandStatsRulesRemaining_Type = Unsigned32
_BridgeOnDemandStatsRulesRemaining_Object = MibTableColumn
bridgeOnDemandStatsRulesRemaining = _BridgeOnDemandStatsRulesRemaining_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 11, 1, 9),
    _BridgeOnDemandStatsRulesRemaining_Type()
)
bridgeOnDemandStatsRulesRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeOnDemandStatsRulesRemaining.setStatus("current")
_BridgeStatsBSDUcastBlocked_Type = Unsigned32
_BridgeStatsBSDUcastBlocked_Object = MibTableColumn
bridgeStatsBSDUcastBlocked = _BridgeStatsBSDUcastBlocked_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 11, 1, 10),
    _BridgeStatsBSDUcastBlocked_Type()
)
bridgeStatsBSDUcastBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatsBSDUcastBlocked.setStatus("current")
_BridgeStatsBSDMcastBlocked_Type = Unsigned32
_BridgeStatsBSDMcastBlocked_Object = MibTableColumn
bridgeStatsBSDMcastBlocked = _BridgeStatsBSDMcastBlocked_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 11, 1, 11),
    _BridgeStatsBSDMcastBlocked_Type()
)
bridgeStatsBSDMcastBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatsBSDMcastBlocked.setStatus("current")
_BridgeStatsBSDBcastBlocked_Type = Unsigned32
_BridgeStatsBSDBcastBlocked_Object = MibTableColumn
bridgeStatsBSDBcastBlocked = _BridgeStatsBSDBcastBlocked_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 11, 1, 12),
    _BridgeStatsBSDBcastBlocked_Type()
)
bridgeStatsBSDBcastBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatsBSDBcastBlocked.setStatus("current")
_BridgeStatsBSDAlarmCount_Type = Unsigned32
_BridgeStatsBSDAlarmCount_Object = MibTableColumn
bridgeStatsBSDAlarmCount = _BridgeStatsBSDAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 11, 1, 13),
    _BridgeStatsBSDAlarmCount_Type()
)
bridgeStatsBSDAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatsBSDAlarmCount.setStatus("current")
_BridgeStatsBytesRcvdCount_Type = Counter64
_BridgeStatsBytesRcvdCount_Object = MibTableColumn
bridgeStatsBytesRcvdCount = _BridgeStatsBytesRcvdCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 11, 1, 14),
    _BridgeStatsBytesRcvdCount_Type()
)
bridgeStatsBytesRcvdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatsBytesRcvdCount.setStatus("current")
_BridgeStatsBytesSentCount_Type = Counter64
_BridgeStatsBytesSentCount_Object = MibTableColumn
bridgeStatsBytesSentCount = _BridgeStatsBytesSentCount_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 11, 1, 15),
    _BridgeStatsBytesSentCount_Type()
)
bridgeStatsBytesSentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatsBytesSentCount.setStatus("current")
_BridgeStatsTicksLastCleared_Type = Counter64
_BridgeStatsTicksLastCleared_Object = MibTableColumn
bridgeStatsTicksLastCleared = _BridgeStatsTicksLastCleared_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 11, 1, 16),
    _BridgeStatsTicksLastCleared_Type()
)
bridgeStatsTicksLastCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatsTicksLastCleared.setStatus("current")
_BridgeStatsTicksNow_Type = Counter64
_BridgeStatsTicksNow_Object = MibTableColumn
bridgeStatsTicksNow = _BridgeStatsTicksNow_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 11, 1, 17),
    _BridgeStatsTicksNow_Type()
)
bridgeStatsTicksNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatsTicksNow.setStatus("current")
_BridgeStatsTicksPerSecond_Type = Counter64
_BridgeStatsTicksPerSecond_Object = MibTableColumn
bridgeStatsTicksPerSecond = _BridgeStatsTicksPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 11, 1, 18),
    _BridgeStatsTicksPerSecond_Type()
)
bridgeStatsTicksPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatsTicksPerSecond.setStatus("current")
_BridgeCmd_ObjectIdentity = ObjectIdentity
bridgeCmd = _BridgeCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 12)
)


class _BridgeCmdOperation_Type(Integer32):
    """Custom type bridgeCmdOperation based on Integer32"""
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
        *(("clrIgmpStats", 2),
          ("clrStats", 1),
          ("flush", 4),
          ("unblock", 3))
    )


_BridgeCmdOperation_Type.__name__ = "Integer32"
_BridgeCmdOperation_Object = MibScalar
bridgeCmdOperation = _BridgeCmdOperation_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 12, 1),
    _BridgeCmdOperation_Type()
)
bridgeCmdOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeCmdOperation.setStatus("current")


class _BridgeCmdFilterMask_Type(Bits):
    """Custom type bridgeCmdFilterMask based on Bits"""
    namedValues = NamedValues(
        *(("filterIfIndex", 0),
          ("filterIpAddress", 5),
          ("filterMacAddress", 6),
          ("filterPort", 4),
          ("filterSecure", 7),
          ("filterSlan", 2),
          ("filterSlot", 3),
          ("filterVlan", 1))
    )

_BridgeCmdFilterMask_Type.__name__ = "Bits"
_BridgeCmdFilterMask_Object = MibScalar
bridgeCmdFilterMask = _BridgeCmdFilterMask_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 12, 2),
    _BridgeCmdFilterMask_Type()
)
bridgeCmdFilterMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeCmdFilterMask.setStatus("current")
_BridgeCmdIfIndex_Type = InterfaceIndex
_BridgeCmdIfIndex_Object = MibScalar
bridgeCmdIfIndex = _BridgeCmdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 12, 3),
    _BridgeCmdIfIndex_Type()
)
bridgeCmdIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeCmdIfIndex.setStatus("current")


class _BridgeCmdVlanId_Type(Integer32):
    """Custom type bridgeCmdVlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4090),
    )


_BridgeCmdVlanId_Type.__name__ = "Integer32"
_BridgeCmdVlanId_Object = MibScalar
bridgeCmdVlanId = _BridgeCmdVlanId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 12, 5),
    _BridgeCmdVlanId_Type()
)
bridgeCmdVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeCmdVlanId.setStatus("current")


class _BridgeCmdSlanId_Type(Integer32):
    """Custom type bridgeCmdSlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4090),
    )


_BridgeCmdSlanId_Type.__name__ = "Integer32"
_BridgeCmdSlanId_Object = MibScalar
bridgeCmdSlanId = _BridgeCmdSlanId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 12, 6),
    _BridgeCmdSlanId_Type()
)
bridgeCmdSlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeCmdSlanId.setStatus("current")


class _BridgeCmdSlot_Type(Integer32):
    """Custom type bridgeCmdSlot based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_BridgeCmdSlot_Type.__name__ = "Integer32"
_BridgeCmdSlot_Object = MibScalar
bridgeCmdSlot = _BridgeCmdSlot_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 12, 7),
    _BridgeCmdSlot_Type()
)
bridgeCmdSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeCmdSlot.setStatus("current")


class _BridgeCmdPort_Type(Integer32):
    """Custom type bridgeCmdPort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BridgeCmdPort_Type.__name__ = "Integer32"
_BridgeCmdPort_Object = MibScalar
bridgeCmdPort = _BridgeCmdPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 12, 8),
    _BridgeCmdPort_Type()
)
bridgeCmdPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeCmdPort.setStatus("current")
_BridgeCmdIpAddress_Type = IpAddress
_BridgeCmdIpAddress_Object = MibScalar
bridgeCmdIpAddress = _BridgeCmdIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 12, 9),
    _BridgeCmdIpAddress_Type()
)
bridgeCmdIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeCmdIpAddress.setStatus("current")
_BridgeCmdMacAddress_Type = MacAddress
_BridgeCmdMacAddress_Object = MibScalar
bridgeCmdMacAddress = _BridgeCmdMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 12, 10),
    _BridgeCmdMacAddress_Type()
)
bridgeCmdMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeCmdMacAddress.setStatus("current")
_EapsGroup_ObjectIdentity = ObjectIdentity
eapsGroup = _EapsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13)
)
_EapsConfigTable_Object = MibTable
eapsConfigTable = _EapsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 1)
)
if mibBuilder.loadTexts:
    eapsConfigTable.setStatus("current")
_EapsConfigEntry_Object = MibTableRow
eapsConfigEntry = _EapsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 1, 1)
)
eapsConfigEntry.setIndexNames(
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigPrimaryPortLineGroup"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigSecondaryPortLineGroup"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigControlVlan"),
)
if mibBuilder.loadTexts:
    eapsConfigEntry.setStatus("current")
_EapsConfigPrimaryPortLineGroup_Type = InterfaceIndex
_EapsConfigPrimaryPortLineGroup_Object = MibTableColumn
eapsConfigPrimaryPortLineGroup = _EapsConfigPrimaryPortLineGroup_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 1, 1, 1),
    _EapsConfigPrimaryPortLineGroup_Type()
)
eapsConfigPrimaryPortLineGroup.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eapsConfigPrimaryPortLineGroup.setStatus("current")
_EapsConfigSecondaryPortLineGroup_Type = InterfaceIndex
_EapsConfigSecondaryPortLineGroup_Object = MibTableColumn
eapsConfigSecondaryPortLineGroup = _EapsConfigSecondaryPortLineGroup_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 1, 1, 2),
    _EapsConfigSecondaryPortLineGroup_Type()
)
eapsConfigSecondaryPortLineGroup.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eapsConfigSecondaryPortLineGroup.setStatus("current")


class _EapsConfigControlVlan_Type(Integer32):
    """Custom type eapsConfigControlVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4090),
    )


_EapsConfigControlVlan_Type.__name__ = "Integer32"
_EapsConfigControlVlan_Object = MibTableColumn
eapsConfigControlVlan = _EapsConfigControlVlan_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 1, 1, 3),
    _EapsConfigControlVlan_Type()
)
eapsConfigControlVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eapsConfigControlVlan.setStatus("current")


class _EapsConfigIsMasterNode_Type(TruthValue):
    """Custom type eapsConfigIsMasterNode based on TruthValue"""


_EapsConfigIsMasterNode_Object = MibTableColumn
eapsConfigIsMasterNode = _EapsConfigIsMasterNode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 1, 1, 4),
    _EapsConfigIsMasterNode_Type()
)
eapsConfigIsMasterNode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eapsConfigIsMasterNode.setStatus("current")


class _EapsConfigControlVlanPriority_Type(Integer32):
    """Custom type eapsConfigControlVlanPriority based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_EapsConfigControlVlanPriority_Type.__name__ = "Integer32"
_EapsConfigControlVlanPriority_Object = MibTableColumn
eapsConfigControlVlanPriority = _EapsConfigControlVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 1, 1, 5),
    _EapsConfigControlVlanPriority_Type()
)
eapsConfigControlVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eapsConfigControlVlanPriority.setStatus("current")
_EapsConfigDomainName_Type = ZhoneAdminString
_EapsConfigDomainName_Object = MibTableColumn
eapsConfigDomainName = _EapsConfigDomainName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 1, 1, 6),
    _EapsConfigDomainName_Type()
)
eapsConfigDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eapsConfigDomainName.setStatus("current")


class _EapsConfigMsgTxInterval_Type(Integer32):
    """Custom type eapsConfigMsgTxInterval based on Integer32"""
    defaultValue = 1


_EapsConfigMsgTxInterval_Object = MibTableColumn
eapsConfigMsgTxInterval = _EapsConfigMsgTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 1, 1, 7),
    _EapsConfigMsgTxInterval_Type()
)
eapsConfigMsgTxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eapsConfigMsgTxInterval.setStatus("current")
if mibBuilder.loadTexts:
    eapsConfigMsgTxInterval.setUnits("seconds")


class _EapsConfigTimeout_Type(Integer32):
    """Custom type eapsConfigTimeout based on Integer32"""
    defaultValue = 3


_EapsConfigTimeout_Object = MibTableColumn
eapsConfigTimeout = _EapsConfigTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 1, 1, 8),
    _EapsConfigTimeout_Type()
)
eapsConfigTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eapsConfigTimeout.setStatus("current")
if mibBuilder.loadTexts:
    eapsConfigTimeout.setUnits("seconds")


class _EapsConfigMaxDroppedMessages_Type(Integer32):
    """Custom type eapsConfigMaxDroppedMessages based on Integer32"""
    defaultValue = 2


_EapsConfigMaxDroppedMessages_Object = MibTableColumn
eapsConfigMaxDroppedMessages = _EapsConfigMaxDroppedMessages_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 1, 1, 9),
    _EapsConfigMaxDroppedMessages_Type()
)
eapsConfigMaxDroppedMessages.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eapsConfigMaxDroppedMessages.setStatus("current")


class _EapsConfigSnmpTrap_Type(TruthValue):
    """Custom type eapsConfigSnmpTrap based on TruthValue"""


_EapsConfigSnmpTrap_Object = MibTableColumn
eapsConfigSnmpTrap = _EapsConfigSnmpTrap_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 1, 1, 10),
    _EapsConfigSnmpTrap_Type()
)
eapsConfigSnmpTrap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eapsConfigSnmpTrap.setStatus("current")


class _EapsConfigDomainEnable_Type(TruthValue):
    """Custom type eapsConfigDomainEnable based on TruthValue"""


_EapsConfigDomainEnable_Object = MibTableColumn
eapsConfigDomainEnable = _EapsConfigDomainEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 1, 1, 11),
    _EapsConfigDomainEnable_Type()
)
eapsConfigDomainEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eapsConfigDomainEnable.setStatus("current")


class _EapsConfigRowStatus_Type(ZhoneRowStatus):
    """Custom type eapsConfigRowStatus based on ZhoneRowStatus"""


_EapsConfigRowStatus_Object = MibTableColumn
eapsConfigRowStatus = _EapsConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 1, 1, 12),
    _EapsConfigRowStatus_Type()
)
eapsConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eapsConfigRowStatus.setStatus("current")
_EapsProtectedVlanTable_Object = MibTable
eapsProtectedVlanTable = _EapsProtectedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 2)
)
if mibBuilder.loadTexts:
    eapsProtectedVlanTable.setStatus("current")
_EapsProtectedVlanEntry_Object = MibTableRow
eapsProtectedVlanEntry = _EapsProtectedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 2, 1)
)
eapsProtectedVlanEntry.setIndexNames(
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigPrimaryPortLineGroup"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigSecondaryPortLineGroup"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigControlVlan"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "eapsProtectedVlanEntryIndex"),
)
if mibBuilder.loadTexts:
    eapsProtectedVlanEntry.setStatus("current")


class _EapsProtectedVlanEntryIndex_Type(Integer32):
    """Custom type eapsProtectedVlanEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_EapsProtectedVlanEntryIndex_Type.__name__ = "Integer32"
_EapsProtectedVlanEntryIndex_Object = MibTableColumn
eapsProtectedVlanEntryIndex = _EapsProtectedVlanEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 2, 1, 1),
    _EapsProtectedVlanEntryIndex_Type()
)
eapsProtectedVlanEntryIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eapsProtectedVlanEntryIndex.setStatus("current")


class _EapsProtectedVlanLowerRange_Type(Integer32):
    """Custom type eapsProtectedVlanLowerRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4090),
    )


_EapsProtectedVlanLowerRange_Type.__name__ = "Integer32"
_EapsProtectedVlanLowerRange_Object = MibTableColumn
eapsProtectedVlanLowerRange = _EapsProtectedVlanLowerRange_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 2, 1, 2),
    _EapsProtectedVlanLowerRange_Type()
)
eapsProtectedVlanLowerRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eapsProtectedVlanLowerRange.setStatus("current")


class _EapsProtectedVlanUpperRange_Type(Integer32):
    """Custom type eapsProtectedVlanUpperRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4090),
    )


_EapsProtectedVlanUpperRange_Type.__name__ = "Integer32"
_EapsProtectedVlanUpperRange_Object = MibTableColumn
eapsProtectedVlanUpperRange = _EapsProtectedVlanUpperRange_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 2, 1, 3),
    _EapsProtectedVlanUpperRange_Type()
)
eapsProtectedVlanUpperRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eapsProtectedVlanUpperRange.setStatus("current")


class _EapsProtectedVlanRowStatus_Type(ZhoneRowStatus):
    """Custom type eapsProtectedVlanRowStatus based on ZhoneRowStatus"""


_EapsProtectedVlanRowStatus_Object = MibTableColumn
eapsProtectedVlanRowStatus = _EapsProtectedVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 2, 1, 4),
    _EapsProtectedVlanRowStatus_Type()
)
eapsProtectedVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eapsProtectedVlanRowStatus.setStatus("current")
_EapsProtectedVlanDomainName_Type = ZhoneAdminString
_EapsProtectedVlanDomainName_Object = MibTableColumn
eapsProtectedVlanDomainName = _EapsProtectedVlanDomainName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 2, 1, 5),
    _EapsProtectedVlanDomainName_Type()
)
eapsProtectedVlanDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eapsProtectedVlanDomainName.setStatus("current")
_EapsStatusTable_Object = MibTable
eapsStatusTable = _EapsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 3)
)
if mibBuilder.loadTexts:
    eapsStatusTable.setStatus("current")
_EapsStatusEntry_Object = MibTableRow
eapsStatusEntry = _EapsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 3, 1)
)
eapsStatusEntry.setIndexNames(
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigPrimaryPortLineGroup"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigSecondaryPortLineGroup"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigControlVlan"),
)
if mibBuilder.loadTexts:
    eapsStatusEntry.setStatus("current")
_EapsPrevState_Type = EapsState
_EapsPrevState_Object = MibTableColumn
eapsPrevState = _EapsPrevState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 3, 1, 1),
    _EapsPrevState_Type()
)
eapsPrevState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eapsPrevState.setStatus("current")
_EapsState_Type = EapsState
_EapsState_Object = MibTableColumn
eapsState = _EapsState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 3, 1, 2),
    _EapsState_Type()
)
eapsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eapsState.setStatus("current")
_EapsStatsTable_Object = MibTable
eapsStatsTable = _EapsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 4)
)
if mibBuilder.loadTexts:
    eapsStatsTable.setStatus("current")
_EapsStatsEntry_Object = MibTableRow
eapsStatsEntry = _EapsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 4, 1)
)
eapsStatsEntry.setIndexNames(
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigPrimaryPortLineGroup"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigSecondaryPortLineGroup"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigControlVlan"),
)
if mibBuilder.loadTexts:
    eapsStatsEntry.setStatus("current")
_EapsStatsTotCtrlMsgSent_Type = Integer32
_EapsStatsTotCtrlMsgSent_Object = MibTableColumn
eapsStatsTotCtrlMsgSent = _EapsStatsTotCtrlMsgSent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 4, 1, 1),
    _EapsStatsTotCtrlMsgSent_Type()
)
eapsStatsTotCtrlMsgSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eapsStatsTotCtrlMsgSent.setStatus("current")
_EapsStatsTotCtrlMsgRecvd_Type = Integer32
_EapsStatsTotCtrlMsgRecvd_Object = MibTableColumn
eapsStatsTotCtrlMsgRecvd = _EapsStatsTotCtrlMsgRecvd_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 4, 1, 2),
    _EapsStatsTotCtrlMsgRecvd_Type()
)
eapsStatsTotCtrlMsgRecvd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eapsStatsTotCtrlMsgRecvd.setStatus("current")
_EapsTrapPrefix_ObjectIdentity = ObjectIdentity
eapsTrapPrefix = _EapsTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 5)
)
if mibBuilder.loadTexts:
    eapsTrapPrefix.setStatus("current")
_EapsTraps_ObjectIdentity = ObjectIdentity
eapsTraps = _EapsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 5, 0)
)
if mibBuilder.loadTexts:
    eapsTraps.setStatus("current")
_EapsTopologyTable_Object = MibTable
eapsTopologyTable = _EapsTopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 6)
)
if mibBuilder.loadTexts:
    eapsTopologyTable.setStatus("current")
_EapsTopologyEntry_Object = MibTableRow
eapsTopologyEntry = _EapsTopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 6, 1)
)
eapsTopologyEntry.setIndexNames(
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigPrimaryPortLineGroup"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigSecondaryPortLineGroup"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "eapsTopologyRing"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "eapsTopologyRowNumber"),
)
if mibBuilder.loadTexts:
    eapsTopologyEntry.setStatus("current")


class _EapsTopologyRing_Type(Integer32):
    """Custom type eapsTopologyRing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("primary", 0),
          ("secondary", 1))
    )


_EapsTopologyRing_Type.__name__ = "Integer32"
_EapsTopologyRing_Object = MibTableColumn
eapsTopologyRing = _EapsTopologyRing_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 6, 1, 1),
    _EapsTopologyRing_Type()
)
eapsTopologyRing.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eapsTopologyRing.setStatus("current")


class _EapsTopologyRowNumber_Type(Integer32):
    """Custom type eapsTopologyRowNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 47),
    )


_EapsTopologyRowNumber_Type.__name__ = "Integer32"
_EapsTopologyRowNumber_Object = MibTableColumn
eapsTopologyRowNumber = _EapsTopologyRowNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 6, 1, 2),
    _EapsTopologyRowNumber_Type()
)
eapsTopologyRowNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eapsTopologyRowNumber.setStatus("current")
_EapsTopologyDomainName_Type = ZhoneAdminString
_EapsTopologyDomainName_Object = MibTableColumn
eapsTopologyDomainName = _EapsTopologyDomainName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 6, 1, 3),
    _EapsTopologyDomainName_Type()
)
eapsTopologyDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eapsTopologyDomainName.setStatus("current")
_EapsTopologyMacAddr_Type = MacAddress
_EapsTopologyMacAddr_Object = MibTableColumn
eapsTopologyMacAddr = _EapsTopologyMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 6, 1, 4),
    _EapsTopologyMacAddr_Type()
)
eapsTopologyMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eapsTopologyMacAddr.setStatus("current")
_EapsTopologyIpAddr_Type = IpAddress
_EapsTopologyIpAddr_Object = MibTableColumn
eapsTopologyIpAddr = _EapsTopologyIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 6, 1, 5),
    _EapsTopologyIpAddr_Type()
)
eapsTopologyIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eapsTopologyIpAddr.setStatus("current")


class _EapsTopologyType_Type(Integer32):
    """Custom type eapsTopologyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("transit", 1))
    )


_EapsTopologyType_Type.__name__ = "Integer32"
_EapsTopologyType_Object = MibTableColumn
eapsTopologyType = _EapsTopologyType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 6, 1, 6),
    _EapsTopologyType_Type()
)
eapsTopologyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eapsTopologyType.setStatus("current")
_EapsTopologyPrimaryLinkName_Type = ZhoneAdminString
_EapsTopologyPrimaryLinkName_Object = MibTableColumn
eapsTopologyPrimaryLinkName = _EapsTopologyPrimaryLinkName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 6, 1, 7),
    _EapsTopologyPrimaryLinkName_Type()
)
eapsTopologyPrimaryLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eapsTopologyPrimaryLinkName.setStatus("current")
_EapsTopologyPrimaryLinkState_Type = EapsState
_EapsTopologyPrimaryLinkState_Object = MibTableColumn
eapsTopologyPrimaryLinkState = _EapsTopologyPrimaryLinkState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 6, 1, 8),
    _EapsTopologyPrimaryLinkState_Type()
)
eapsTopologyPrimaryLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eapsTopologyPrimaryLinkState.setStatus("current")
_EapsTopologySecondaryLinkName_Type = ZhoneAdminString
_EapsTopologySecondaryLinkName_Object = MibTableColumn
eapsTopologySecondaryLinkName = _EapsTopologySecondaryLinkName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 6, 1, 9),
    _EapsTopologySecondaryLinkName_Type()
)
eapsTopologySecondaryLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eapsTopologySecondaryLinkName.setStatus("current")
_EapsTopologySecondaryLinkState_Type = EapsState
_EapsTopologySecondaryLinkState_Object = MibTableColumn
eapsTopologySecondaryLinkState = _EapsTopologySecondaryLinkState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 6, 1, 10),
    _EapsTopologySecondaryLinkState_Type()
)
eapsTopologySecondaryLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eapsTopologySecondaryLinkState.setStatus("current")
_BridgeIgmpStatsTable_Object = MibTable
bridgeIgmpStatsTable = _BridgeIgmpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 14)
)
if mibBuilder.loadTexts:
    bridgeIgmpStatsTable.setStatus("current")
_BridgeIgmpStatsEntry_Object = MibTableRow
bridgeIgmpStatsEntry = _BridgeIgmpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 14, 1)
)
bridgeIgmpStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    bridgeIgmpStatsEntry.setStatus("current")
_GenQueryRx_Type = Unsigned32
_GenQueryRx_Object = MibTableColumn
genQueryRx = _GenQueryRx_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 14, 1, 1),
    _GenQueryRx_Type()
)
genQueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genQueryRx.setStatus("current")
_GenQueryTx_Type = Unsigned32
_GenQueryTx_Object = MibTableColumn
genQueryTx = _GenQueryTx_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 14, 1, 2),
    _GenQueryTx_Type()
)
genQueryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genQueryTx.setStatus("current")
_SpecQueryRx_Type = Unsigned32
_SpecQueryRx_Object = MibTableColumn
specQueryRx = _SpecQueryRx_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 14, 1, 3),
    _SpecQueryRx_Type()
)
specQueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specQueryRx.setStatus("current")
_SpecQueryTx_Type = Unsigned32
_SpecQueryTx_Object = MibTableColumn
specQueryTx = _SpecQueryTx_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 14, 1, 4),
    _SpecQueryTx_Type()
)
specQueryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specQueryTx.setStatus("current")
_V2ReportsRx_Type = Unsigned32
_V2ReportsRx_Object = MibTableColumn
v2ReportsRx = _V2ReportsRx_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 14, 1, 5),
    _V2ReportsRx_Type()
)
v2ReportsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2ReportsRx.setStatus("current")
_V2ReportsTx_Type = Unsigned32
_V2ReportsTx_Object = MibTableColumn
v2ReportsTx = _V2ReportsTx_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 14, 1, 6),
    _V2ReportsTx_Type()
)
v2ReportsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2ReportsTx.setStatus("current")
_LeavesRx_Type = Unsigned32
_LeavesRx_Object = MibTableColumn
leavesRx = _LeavesRx_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 14, 1, 7),
    _LeavesRx_Type()
)
leavesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leavesRx.setStatus("current")
_LeavesTx_Type = Unsigned32
_LeavesTx_Object = MibTableColumn
leavesTx = _LeavesTx_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 14, 1, 8),
    _LeavesTx_Type()
)
leavesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leavesTx.setStatus("current")
_UnknownRx_Type = Unsigned32
_UnknownRx_Object = MibTableColumn
unknownRx = _UnknownRx_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 14, 1, 9),
    _UnknownRx_Type()
)
unknownRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unknownRx.setStatus("current")
_ErrorRx_Type = Unsigned32
_ErrorRx_Object = MibTableColumn
errorRx = _ErrorRx_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 14, 1, 10),
    _ErrorRx_Type()
)
errorRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorRx.setStatus("current")
_ActChans_Type = Unsigned32
_ActChans_Object = MibTableColumn
actChans = _ActChans_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 14, 1, 11),
    _ActChans_Type()
)
actChans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actChans.setStatus("current")
_ActHosts_Type = Unsigned32
_ActHosts_Object = MibTableColumn
actHosts = _ActHosts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 14, 1, 12),
    _ActHosts_Type()
)
actHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actHosts.setStatus("current")
_V3GenQueryRx_Type = Unsigned32
_V3GenQueryRx_Object = MibTableColumn
v3GenQueryRx = _V3GenQueryRx_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 14, 1, 13),
    _V3GenQueryRx_Type()
)
v3GenQueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3GenQueryRx.setStatus("current")
_V3GenQueryTx_Type = Unsigned32
_V3GenQueryTx_Object = MibTableColumn
v3GenQueryTx = _V3GenQueryTx_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 14, 1, 14),
    _V3GenQueryTx_Type()
)
v3GenQueryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3GenQueryTx.setStatus("current")
_V3SpecQueryRx_Type = Unsigned32
_V3SpecQueryRx_Object = MibTableColumn
v3SpecQueryRx = _V3SpecQueryRx_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 14, 1, 15),
    _V3SpecQueryRx_Type()
)
v3SpecQueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3SpecQueryRx.setStatus("current")
_V3SpecQueryTx_Type = Unsigned32
_V3SpecQueryTx_Object = MibTableColumn
v3SpecQueryTx = _V3SpecQueryTx_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 14, 1, 16),
    _V3SpecQueryTx_Type()
)
v3SpecQueryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3SpecQueryTx.setStatus("current")
_V3ReportsRx_Type = Unsigned32
_V3ReportsRx_Object = MibTableColumn
v3ReportsRx = _V3ReportsRx_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 14, 1, 17),
    _V3ReportsRx_Type()
)
v3ReportsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3ReportsRx.setStatus("current")
_V3ReportsTx_Type = Unsigned32
_V3ReportsTx_Object = MibTableColumn
v3ReportsTx = _V3ReportsTx_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 14, 1, 18),
    _V3ReportsTx_Type()
)
v3ReportsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v3ReportsTx.setStatus("current")
_BridgeGroup_ObjectIdentity = ObjectIdentity
bridgeGroup = _BridgeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 15)
)
_BridgeTrapPrefix_ObjectIdentity = ObjectIdentity
bridgeTrapPrefix = _BridgeTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 15, 1)
)
if mibBuilder.loadTexts:
    bridgeTrapPrefix.setStatus("current")
_BridgeTraps_ObjectIdentity = ObjectIdentity
bridgeTraps = _BridgeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 15, 1, 0)
)
if mibBuilder.loadTexts:
    bridgeTraps.setStatus("current")
_BridgeTrapObjects_ObjectIdentity = ObjectIdentity
bridgeTrapObjects = _BridgeTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 16)
)
_BridgeMacAddrString_Type = OctetString
_BridgeMacAddrString_Object = MibScalar
bridgeMacAddrString = _BridgeMacAddrString_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 16, 1),
    _BridgeMacAddrString_Type()
)
bridgeMacAddrString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bridgeMacAddrString.setStatus("current")
_BridgeIgmpTable_Object = MibTable
bridgeIgmpTable = _BridgeIgmpTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 17)
)
if mibBuilder.loadTexts:
    bridgeIgmpTable.setStatus("current")
_BridgeIgmpEntry_Object = MibTableRow
bridgeIgmpEntry = _BridgeIgmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 17, 1)
)
bridgeIgmpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "hostMac"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "mcastMac"),
)
if mibBuilder.loadTexts:
    bridgeIgmpEntry.setStatus("current")


class _SlanId_Type(Integer32):
    """Custom type slanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4090),
    )


_SlanId_Type.__name__ = "Integer32"
_SlanId_Object = MibTableColumn
slanId = _SlanId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 17, 1, 1),
    _SlanId_Type()
)
slanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slanId.setStatus("current")


class _VlanId_Type(Integer32):
    """Custom type vlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4090),
    )


_VlanId_Type.__name__ = "Integer32"
_VlanId_Object = MibTableColumn
vlanId = _VlanId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 17, 1, 2),
    _VlanId_Type()
)
vlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanId.setStatus("current")


class _McastMac_Type(OctetString):
    """Custom type mcastMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_McastMac_Type.__name__ = "OctetString"
_McastMac_Object = MibTableColumn
mcastMac = _McastMac_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 17, 1, 3),
    _McastMac_Type()
)
mcastMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcastMac.setStatus("current")
_McastIP_Type = IpAddress
_McastIP_Object = MibTableColumn
mcastIP = _McastIP_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 17, 1, 4),
    _McastIP_Type()
)
mcastIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcastIP.setStatus("current")


class _HostMac_Type(OctetString):
    """Custom type hostMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_HostMac_Type.__name__ = "OctetString"
_HostMac_Object = MibTableColumn
hostMac = _HostMac_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 17, 1, 5),
    _HostMac_Type()
)
hostMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostMac.setStatus("current")
_LastJoinTimer_Type = Integer32
_LastJoinTimer_Object = MibTableColumn
lastJoinTimer = _LastJoinTimer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 17, 1, 6),
    _LastJoinTimer_Type()
)
lastJoinTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastJoinTimer.setStatus("current")
_StaticBridgePathTable_Object = MibTable
staticBridgePathTable = _StaticBridgePathTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 18)
)
if mibBuilder.loadTexts:
    staticBridgePathTable.setStatus("current")
_StaticBridgePathEntry_Object = MibTableRow
staticBridgePathEntry = _StaticBridgePathEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 18, 1)
)
staticBridgePathEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "staticBridgePathAddressType"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfVlanId"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "staticBridgePathMacOrIpAddress"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfStagId"),
)
if mibBuilder.loadTexts:
    staticBridgePathEntry.setStatus("current")
_StaticBridgePathMacOrIpAddress_Type = IpAddress
_StaticBridgePathMacOrIpAddress_Object = MibTableColumn
staticBridgePathMacOrIpAddress = _StaticBridgePathMacOrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 18, 1, 1),
    _StaticBridgePathMacOrIpAddress_Type()
)
staticBridgePathMacOrIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staticBridgePathMacOrIpAddress.setStatus("current")


class _StaticBridgePathAddressType_Type(Integer32):
    """Custom type staticBridgePathAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7,
              8,
              9,
              10,
              13,
              14,
              15,
              16,
              17,
              720901)
        )
    )
    namedValues = NamedValues(
        *(("dhcpAllowOui", 720901),
          ("dhcpIpAddr", 9),
          ("dhcpIpAddrV6", 17),
          ("dhcpMacAddr", 10),
          ("globalAddr", 4),
          ("globalIntralinkAddr", 8),
          ("intralinkAddr", 7),
          ("ipAddr", 2),
          ("ipAddrV6", 16),
          ("macAddr", 1),
          ("mvrAddr", 13),
          ("secMvrAddr", 15),
          ("vlanIdAddr", 3),
          ("vlanParms", 14))
    )


_StaticBridgePathAddressType_Type.__name__ = "Integer32"
_StaticBridgePathAddressType_Object = MibTableColumn
staticBridgePathAddressType = _StaticBridgePathAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 18, 1, 2),
    _StaticBridgePathAddressType_Type()
)
staticBridgePathAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staticBridgePathAddressType.setStatus("current")


class _StaticBridgePathMulticastAging_Type(Integer32):
    """Custom type staticBridgePathMulticastAging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_StaticBridgePathMulticastAging_Type.__name__ = "Integer32"
_StaticBridgePathMulticastAging_Object = MibTableColumn
staticBridgePathMulticastAging = _StaticBridgePathMulticastAging_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 18, 1, 3),
    _StaticBridgePathMulticastAging_Type()
)
staticBridgePathMulticastAging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticBridgePathMulticastAging.setStatus("current")


class _StaticBridgePathRowStatus_Type(ZhoneRowStatus):
    """Custom type staticBridgePathRowStatus based on ZhoneRowStatus"""


_StaticBridgePathRowStatus_Object = MibTableColumn
staticBridgePathRowStatus = _StaticBridgePathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 18, 1, 4),
    _StaticBridgePathRowStatus_Type()
)
staticBridgePathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticBridgePathRowStatus.setStatus("current")


class _StaticBridgePathFlapControl_Type(Integer32):
    """Custom type staticBridgePathFlapControl based on Integer32"""
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
        *(("default", 1),
          ("disable", 2),
          ("enable", 3),
          ("fast", 4))
    )


_StaticBridgePathFlapControl_Type.__name__ = "Integer32"
_StaticBridgePathFlapControl_Object = MibTableColumn
staticBridgePathFlapControl = _StaticBridgePathFlapControl_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 18, 1, 5),
    _StaticBridgePathFlapControl_Type()
)
staticBridgePathFlapControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticBridgePathFlapControl.setStatus("current")


class _StaticBridgePathUnicastAging_Type(Integer32):
    """Custom type staticBridgePathUnicastAging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 2147483647),
    )


_StaticBridgePathUnicastAging_Type.__name__ = "Integer32"
_StaticBridgePathUnicastAging_Object = MibTableColumn
staticBridgePathUnicastAging = _StaticBridgePathUnicastAging_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 18, 1, 6),
    _StaticBridgePathUnicastAging_Type()
)
staticBridgePathUnicastAging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticBridgePathUnicastAging.setStatus("current")


class _StaticBridgePathIgmpQueryInterval_Type(Integer32):
    """Custom type staticBridgePathIgmpQueryInterval based on Integer32"""
    defaultValue = 0


_StaticBridgePathIgmpQueryInterval_Object = MibTableColumn
staticBridgePathIgmpQueryInterval = _StaticBridgePathIgmpQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 18, 1, 7),
    _StaticBridgePathIgmpQueryInterval_Type()
)
staticBridgePathIgmpQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticBridgePathIgmpQueryInterval.setStatus("current")


class _StaticBridgePathFlags_Type(Bits):
    """Custom type staticBridgePathFlags based on Bits"""
    namedValues = NamedValues(
        *(("igmpProcessJoinAndLeave", 0),
          ("igmpRespondToQuery", 1),
          ("igmpUseBridgeIpAddress", 2))
    )

_StaticBridgePathFlags_Type.__name__ = "Bits"
_StaticBridgePathFlags_Object = MibTableColumn
staticBridgePathFlags = _StaticBridgePathFlags_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 18, 1, 8),
    _StaticBridgePathFlags_Type()
)
staticBridgePathFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticBridgePathFlags.setStatus("current")
_StaticBridgePathIgmpCustomIpAddress_Type = IpAddress
_StaticBridgePathIgmpCustomIpAddress_Object = MibTableColumn
staticBridgePathIgmpCustomIpAddress = _StaticBridgePathIgmpCustomIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 18, 1, 9),
    _StaticBridgePathIgmpCustomIpAddress_Type()
)
staticBridgePathIgmpCustomIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticBridgePathIgmpCustomIpAddress.setStatus("current")


class _StaticBridgePathLoopPrevention_Type(Integer32):
    """Custom type staticBridgePathLoopPrevention based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("blockAll", 2),
          ("blockAllAuto", 4),
          ("blockAsym", 1),
          ("blockAsymAuto", 3),
          ("none", 0))
    )


_StaticBridgePathLoopPrevention_Type.__name__ = "Integer32"
_StaticBridgePathLoopPrevention_Object = MibTableColumn
staticBridgePathLoopPrevention = _StaticBridgePathLoopPrevention_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 18, 1, 10),
    _StaticBridgePathLoopPrevention_Type()
)
staticBridgePathLoopPrevention.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticBridgePathLoopPrevention.setStatus("current")


class _StaticBridgePathIgmpDscp_Type(OctetString):
    """Custom type staticBridgePathIgmpDscp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_StaticBridgePathIgmpDscp_Type.__name__ = "OctetString"
_StaticBridgePathIgmpDscp_Object = MibTableColumn
staticBridgePathIgmpDscp = _StaticBridgePathIgmpDscp_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 18, 1, 11),
    _StaticBridgePathIgmpDscp_Type()
)
staticBridgePathIgmpDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticBridgePathIgmpDscp.setStatus("current")
_BridgePathIfLookupTable_Object = MibTable
bridgePathIfLookupTable = _BridgePathIfLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 19)
)
if mibBuilder.loadTexts:
    bridgePathIfLookupTable.setStatus("current")
_BridgePathIfLookupEntry_Object = MibTableRow
bridgePathIfLookupEntry = _BridgePathIfLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 19, 1)
)
bridgePathIfLookupEntry.setIndexNames(
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "bridgePathIfAddressType"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "bridgePathIfMacOrIpAddress"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfVlanId"),
    (0, "IF-MIB", "ifIndex"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfStagId"),
)
if mibBuilder.loadTexts:
    bridgePathIfLookupEntry.setStatus("current")


class _BridgePathIfAddressType_Type(Integer32):
    """Custom type bridgePathIfAddressType based on Integer32"""
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
        *(("dhcpIp", 5),
          ("dhcpMac", 4),
          ("ipAddress", 3),
          ("multicastMac", 2),
          ("unicastMac", 1))
    )


_BridgePathIfAddressType_Type.__name__ = "Integer32"
_BridgePathIfAddressType_Object = MibTableColumn
bridgePathIfAddressType = _BridgePathIfAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 19, 1, 1),
    _BridgePathIfAddressType_Type()
)
bridgePathIfAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bridgePathIfAddressType.setStatus("current")
_BridgePathIfMacOrIpAddress_Type = IpAddress
_BridgePathIfMacOrIpAddress_Object = MibTableColumn
bridgePathIfMacOrIpAddress = _BridgePathIfMacOrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 19, 1, 2),
    _BridgePathIfMacOrIpAddress_Type()
)
bridgePathIfMacOrIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bridgePathIfMacOrIpAddress.setStatus("current")


class _BridgePathIfLookupStaticOrDynamic_Type(Integer32):
    """Custom type bridgePathIfLookupStaticOrDynamic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamicEntry", 2),
          ("staticEntry", 1))
    )


_BridgePathIfLookupStaticOrDynamic_Type.__name__ = "Integer32"
_BridgePathIfLookupStaticOrDynamic_Object = MibTableColumn
bridgePathIfLookupStaticOrDynamic = _BridgePathIfLookupStaticOrDynamic_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 19, 1, 3),
    _BridgePathIfLookupStaticOrDynamic_Type()
)
bridgePathIfLookupStaticOrDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgePathIfLookupStaticOrDynamic.setStatus("current")


class _BridgePathIfLookupFlush_Type(TruthValue):
    """Custom type bridgePathIfLookupFlush based on TruthValue"""


_BridgePathIfLookupFlush_Object = MibTableColumn
bridgePathIfLookupFlush = _BridgePathIfLookupFlush_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 19, 1, 4),
    _BridgePathIfLookupFlush_Type()
)
bridgePathIfLookupFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgePathIfLookupFlush.setStatus("current")
_BridgePathAddressLookupTable_Object = MibTable
bridgePathAddressLookupTable = _BridgePathAddressLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 20)
)
if mibBuilder.loadTexts:
    bridgePathAddressLookupTable.setStatus("current")
_BridgePathAddressLookupEntry_Object = MibTableRow
bridgePathAddressLookupEntry = _BridgePathAddressLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 20, 1)
)
bridgePathAddressLookupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfAddressType"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "bridgePathIfLookupStaticOrDynamic"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfVlanId"),
    (0, "ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfStagId"),
)
if mibBuilder.loadTexts:
    bridgePathAddressLookupEntry.setStatus("current")


class _BridgePathAddressLookupStaticOrDynamic_Type(Integer32):
    """Custom type bridgePathAddressLookupStaticOrDynamic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamicEntry", 2),
          ("staticEntry", 1))
    )


_BridgePathAddressLookupStaticOrDynamic_Type.__name__ = "Integer32"
_BridgePathAddressLookupStaticOrDynamic_Object = MibTableColumn
bridgePathAddressLookupStaticOrDynamic = _BridgePathAddressLookupStaticOrDynamic_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 20, 1, 1),
    _BridgePathAddressLookupStaticOrDynamic_Type()
)
bridgePathAddressLookupStaticOrDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgePathAddressLookupStaticOrDynamic.setStatus("current")


class _BridgePathAddressLookupFlush_Type(TruthValue):
    """Custom type bridgePathAddressLookupFlush based on TruthValue"""


_BridgePathAddressLookupFlush_Object = MibTableColumn
bridgePathAddressLookupFlush = _BridgePathAddressLookupFlush_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 20, 1, 2),
    _BridgePathAddressLookupFlush_Type()
)
bridgePathAddressLookupFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgePathAddressLookupFlush.setStatus("current")
_BridgeStatusTable_Object = MibTable
bridgeStatusTable = _BridgeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 21)
)
if mibBuilder.loadTexts:
    bridgeStatusTable.setStatus("current")
_BridgeStatusEntry_Object = MibTableRow
bridgeStatusEntry = _BridgeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 21, 1)
)
bridgeStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    bridgeStatusEntry.setStatus("current")
_BridgeStatusState_Type = BridgeState
_BridgeStatusState_Object = MibTableColumn
bridgeStatusState = _BridgeStatusState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 21, 1, 1),
    _BridgeStatusState_Type()
)
bridgeStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStatusState.setStatus("current")
_ZhoneCompliances_ObjectIdentity = ObjectIdentity
zhoneCompliances = _ZhoneCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 9)
)
_ZhoneGroups_ObjectIdentity = ObjectIdentity
zhoneGroups = _ZhoneGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1)
)

# Managed Objects groups

bridgeInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 1)
)
bridgeInterfaceGroup.setObjects(
      *(("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfVci"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfVpi"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfVlanId"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfStripAndInsert"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfCustomARP"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfFilterBroadcast"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfLearnIp"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfLearnUnicast"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfMaxUnicast"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfLearnMulticast"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfForwardToUnicast"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfForwardToMulticast"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfForwardToDefault"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeLowerIfIndex"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeAddressLookupStaticOrDynamic"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfLookupStaticOrDynamic"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfCustomDHCP"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "staticBridgeMulticastAging"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfRowStatus"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "staticBridgeRowStatus"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfLookupFlush"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfOutgoingCOSValue"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfOutgoingCOSOption"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfVlanIdCOS"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeAddressLookupFlush"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "staticBridgeFlapControl"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfStagOutgoingCOSValue"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfStagCOS"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfStagOutgoingCOSOption"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfStagStripAndInsert"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfStagId"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfStagTPID"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "packetRuleValue"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "packetRuleRowStatus"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "packetRuleGroupMemberNextIndex"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfEgressPacketRuleGroupIndex"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfIngressPacketRuleGroupIndex"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "packetRuleGroupIndexNext"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "packetRuleValue5"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "packetRuleValue4"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "packetRuleValue3"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigControlVlan"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigPrimaryPortLineGroup"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigSecondaryPortLineGroup"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigIsMasterNode"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigControlVlanPriority"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigDomainName"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigMsgTxInterval"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigTimeout"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigMaxDroppedMessages"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigSnmpTrap"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsProtectedVlanLowerRange"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsProtectedVlanUpperRange"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigDomainEnable"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsProtectedVlanEntryIndex"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "genQueryRx"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "genQueryTx"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "specQueryRx"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "specQueryTx"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "v2ReportsRx"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "v2ReportsTx"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "leavesRx"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "leavesTx"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "unknownRx"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "errorRx"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "actChans"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "actHosts"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "staticBridgeLoopPrevention"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "v3ReportsTx"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "v3ReportsRx"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "v3SpecQueryTx"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "v3SpecQueryRx"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "v3GenQueryTx"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "v3GenQueryRx"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "packetRuleValue2"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "packetRuleType"))
)
if mibBuilder.loadTexts:
    bridgeInterfaceGroup.setStatus("current")

zhoneBridgeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 23)
)
zhoneBridgeGroup.setObjects(
      *(("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfMcastControlList"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfMaxVideoStreams"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfIsPPPoA"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfFloodUnknown"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfFloodMulticast"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfTableBasedFilter"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfDhcpLearn"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "staticBridgeUnicastAging"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "staticBridgeIgmpQueryInterval"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgePPPoEBrasMac"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgePPPoELocalHostMac"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgePPPoEEIfIndex"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgePPPoESessionID"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgePPPoESlanId"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgePPPoEVlanId"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgePPPoEEncapLLC"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "stpParamName"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "stpParamRevision"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "stpParamBridgePriority"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "stpParamForceVersion"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "stpParamFwdDelay"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "stpParamHelloTime"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "stpParamMigrateTime"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "stpParamTxHoldCount"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "stpParamMaxAge"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "stpBindRowStatus"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "stpBindPortPriority"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "mstpInstanceRowStatus"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeCmdOperation"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeCmdFilterMask"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "mstpInstanceName"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "staticBridgeFlags"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "staticBridgeIgmpCustomIpAddress"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfMvrVlan"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfVlanXlateFrom"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfSlanXlateFrom"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeMacAddrString"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfGponTrafficProfile"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfGponGemPortId"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeType"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "staticBridgePathMulticastAging"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "staticBridgePathRowStatus"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "staticBridgePathFlapControl"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "staticBridgePathUnicastAging"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "staticBridgePathIgmpQueryInterval"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "staticBridgePathFlags"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "staticBridgePathIgmpCustomIpAddress"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "staticBridgePathLoopPrevention"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "staticBridgePathIgmpDscp"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgePathIfLookupStaticOrDynamic"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgePathIfLookupFlush"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfStagIncomingCOSOption"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfIncomingCOSOption"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfUnblock"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfOnDemandStatsEnabled"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeIfBridgeState"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "staticBridgeIgmpDscp"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "packetRuleValue6"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "packetRuleValue7"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgePathAddressLookupFlush"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgePathAddressLookupStaticOrDynamic"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeStatusState"))
)
if mibBuilder.loadTexts:
    zhoneBridgeGroup.setStatus("current")

zhoneBridgeCmdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 76)
)
zhoneBridgeCmdGroup.setObjects(
      *(("ZHONE-COM-BRIDGE-REC-MIB", "bridgeCmdOperation"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeCmdFilterMask"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeCmdIfIndex"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeCmdVlanId"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeCmdSlanId"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeCmdSlot"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeCmdPort"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeCmdIpAddress"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeCmdMacAddress"))
)
if mibBuilder.loadTexts:
    zhoneBridgeCmdGroup.setStatus("current")

zhoneBridgeEapsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 77)
)
zhoneBridgeEapsGroup.setObjects(
      *(("ZHONE-COM-BRIDGE-REC-MIB", "eapsProtectedVlanEntryIndex"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsProtectedVlanLowerRange"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsProtectedVlanUpperRange"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsProtectedVlanRowStatus"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsProtectedVlanDomainName"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsPrevState"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsState"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsStatsTotCtrlMsgSent"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsStatsTotCtrlMsgRecvd"))
)
if mibBuilder.loadTexts:
    zhoneBridgeEapsGroup.setStatus("current")

zhoneBridgeEapsConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 78)
)
zhoneBridgeEapsConfigGroup.setObjects(
      *(("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigPrimaryPortLineGroup"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigSecondaryPortLineGroup"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigControlVlan"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigIsMasterNode"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigControlVlanPriority"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigDomainName"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigMsgTxInterval"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigTimeout"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigMaxDroppedMessages"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigSnmpTrap"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigDomainEnable"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigRowStatus"))
)
if mibBuilder.loadTexts:
    zhoneBridgeEapsConfigGroup.setStatus("current")

zhoneBridgeEapsTopologyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 79)
)
zhoneBridgeEapsTopologyGroup.setObjects(
      *(("ZHONE-COM-BRIDGE-REC-MIB", "eapsTopologyDomainName"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsTopologyMacAddr"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsTopologyIpAddr"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsTopologyType"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsTopologyPrimaryLinkName"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsTopologyPrimaryLinkState"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsTopologySecondaryLinkName"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsTopologySecondaryLinkState"))
)
if mibBuilder.loadTexts:
    zhoneBridgeEapsTopologyGroup.setStatus("current")

zhoneBridgeIgmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 81)
)
zhoneBridgeIgmpGroup.setObjects(
      *(("ZHONE-COM-BRIDGE-REC-MIB", "slanId"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "vlanId"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "mcastMac"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "mcastIP"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "hostMac"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "lastJoinTimer"))
)
if mibBuilder.loadTexts:
    zhoneBridgeIgmpGroup.setStatus("current")

zhoneBridgeStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 82)
)
zhoneBridgeStatsGroup.setObjects(
      *(("ZHONE-COM-BRIDGE-REC-MIB", "bridgeStatsUcastRcvd"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeStatsMcastRcvd"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeStatsBcastRcvd"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeStatsUcastSent"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeStatsMcastSent"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeStatsBcastSent"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeStatsErrorSent"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeOnDemandStatsRulesSupported"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeOnDemandStatsRulesRemaining"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeStatsBSDUcastBlocked"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeStatsBSDMcastBlocked"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeStatsBSDBcastBlocked"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeStatsBSDAlarmCount"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeStatsBytesRcvdCount"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeStatsBytesSentCount"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeStatsTicksLastCleared"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeStatsTicksNow"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeStatsTicksPerSecond"))
)
if mibBuilder.loadTexts:
    zhoneBridgeStatsGroup.setStatus("current")


# Notification objects

eapsStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 5, 0, 1)
)
eapsStateChange.setObjects(
      *(("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigPrimaryPortLineGroup"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigSecondaryPortLineGroup"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigControlVlan"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigDomainName"))
)
if mibBuilder.loadTexts:
    eapsStateChange.setStatus(
        "current"
    )

eapsFailTimerExpFlagSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 5, 0, 2)
)
eapsFailTimerExpFlagSet.setObjects(
      *(("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigPrimaryPortLineGroup"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigSecondaryPortLineGroup"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigControlVlan"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigDomainName"))
)
if mibBuilder.loadTexts:
    eapsFailTimerExpFlagSet.setStatus(
        "current"
    )

eapsFailTimerExpFlagClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 5, 0, 3)
)
eapsFailTimerExpFlagClear.setObjects(
      *(("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigPrimaryPortLineGroup"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigSecondaryPortLineGroup"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigControlVlan"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigDomainName"))
)
if mibBuilder.loadTexts:
    eapsFailTimerExpFlagClear.setStatus(
        "current"
    )

eapsLinkDownRingComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 13, 5, 0, 4)
)
eapsLinkDownRingComplete.setObjects(
      *(("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigPrimaryPortLineGroup"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigSecondaryPortLineGroup"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigControlVlan"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsConfigDomainName"))
)
if mibBuilder.loadTexts:
    eapsLinkDownRingComplete.setStatus(
        "current"
    )

bridgeLoopDetection = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 15, 1, 0, 1)
)
bridgeLoopDetection.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAlias"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeMacAddrString"))
)
if mibBuilder.loadTexts:
    bridgeLoopDetection.setStatus(
        "current"
    )

bridgeStormDetection = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 4, 7, 15, 1, 0, 2)
)
bridgeStormDetection.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAlias"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeMacAddrString"))
)
if mibBuilder.loadTexts:
    bridgeStormDetection.setStatus(
        "current"
    )


# Notifications groups

zhoneBridgeNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 80)
)
zhoneBridgeNotificationGroup.setObjects(
      *(("ZHONE-COM-BRIDGE-REC-MIB", "eapsStateChange"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsFailTimerExpFlagSet"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsFailTimerExpFlagClear"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "eapsLinkDownRingComplete"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeLoopDetection"),
        ("ZHONE-COM-BRIDGE-REC-MIB", "bridgeStormDetection"))
)
if mibBuilder.loadTexts:
    zhoneBridgeNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-COM-BRIDGE-REC-MIB",
    **{"PacketRuleGroupIndex": PacketRuleGroupIndex,
       "EapsState": EapsState,
       "BridgeState": BridgeState,
       "NetworkAddress": NetworkAddress,
       "bridgeInterfaceGroup": bridgeInterfaceGroup,
       "bridgeInterfaceTable": bridgeInterfaceTable,
       "bridgeInterfaceEntry": bridgeInterfaceEntry,
       "bridgeIfVpi": bridgeIfVpi,
       "bridgeIfVci": bridgeIfVci,
       "bridgeIfVlanId": bridgeIfVlanId,
       "bridgeIfStripAndInsert": bridgeIfStripAndInsert,
       "bridgeIfCustomARP": bridgeIfCustomARP,
       "bridgeIfFilterBroadcast": bridgeIfFilterBroadcast,
       "bridgeIfLearnIp": bridgeIfLearnIp,
       "bridgeIfLearnUnicast": bridgeIfLearnUnicast,
       "bridgeIfMaxUnicast": bridgeIfMaxUnicast,
       "bridgeIfLearnMulticast": bridgeIfLearnMulticast,
       "bridgeIfForwardToUnicast": bridgeIfForwardToUnicast,
       "bridgeIfForwardToMulticast": bridgeIfForwardToMulticast,
       "bridgeIfForwardToDefault": bridgeIfForwardToDefault,
       "bridgeLowerIfIndex": bridgeLowerIfIndex,
       "bridgeIfRowStatus": bridgeIfRowStatus,
       "bridgeIfCustomDHCP": bridgeIfCustomDHCP,
       "bridgeIfIngressPacketRuleGroupIndex": bridgeIfIngressPacketRuleGroupIndex,
       "bridgeIfVlanIdCOS": bridgeIfVlanIdCOS,
       "bridgeIfOutgoingCOSOption": bridgeIfOutgoingCOSOption,
       "bridgeIfOutgoingCOSValue": bridgeIfOutgoingCOSValue,
       "bridgeIfStagTPID": bridgeIfStagTPID,
       "bridgeIfStagId": bridgeIfStagId,
       "bridgeIfStagStripAndInsert": bridgeIfStagStripAndInsert,
       "bridgeIfStagOutgoingCOSOption": bridgeIfStagOutgoingCOSOption,
       "bridgeIfStagCOS": bridgeIfStagCOS,
       "bridgeIfStagOutgoingCOSValue": bridgeIfStagOutgoingCOSValue,
       "bridgeIfMcastControlList": bridgeIfMcastControlList,
       "bridgeIfMaxVideoStreams": bridgeIfMaxVideoStreams,
       "bridgeIfIsPPPoA": bridgeIfIsPPPoA,
       "bridgeIfFloodUnknown": bridgeIfFloodUnknown,
       "bridgeIfFloodMulticast": bridgeIfFloodMulticast,
       "bridgeIfEgressPacketRuleGroupIndex": bridgeIfEgressPacketRuleGroupIndex,
       "bridgeIfTableBasedFilter": bridgeIfTableBasedFilter,
       "bridgeIfDhcpLearn": bridgeIfDhcpLearn,
       "bridgeIfOnDemandStatsEnabled": bridgeIfOnDemandStatsEnabled,
       "bridgeIfMvrVlan": bridgeIfMvrVlan,
       "bridgeIfVlanXlateFrom": bridgeIfVlanXlateFrom,
       "bridgeIfSlanXlateFrom": bridgeIfSlanXlateFrom,
       "bridgeIfBridgeState": bridgeIfBridgeState,
       "bridgeIfUnblock": bridgeIfUnblock,
       "bridgeType": bridgeType,
       "bridgeIfGponGemPortId": bridgeIfGponGemPortId,
       "bridgeIfGponTrafficProfile": bridgeIfGponTrafficProfile,
       "bridgeIfIncomingCOSOption": bridgeIfIncomingCOSOption,
       "bridgeIfStagIncomingCOSOption": bridgeIfStagIncomingCOSOption,
       "staticBridgeTable": staticBridgeTable,
       "staticBridgeEntry": staticBridgeEntry,
       "staticBridgeMacOrIpAddress": staticBridgeMacOrIpAddress,
       "staticBridgeAddressType": staticBridgeAddressType,
       "staticBridgeMulticastAging": staticBridgeMulticastAging,
       "staticBridgeRowStatus": staticBridgeRowStatus,
       "staticBridgeFlapControl": staticBridgeFlapControl,
       "staticBridgeUnicastAging": staticBridgeUnicastAging,
       "staticBridgeIgmpQueryInterval": staticBridgeIgmpQueryInterval,
       "staticBridgeFlags": staticBridgeFlags,
       "staticBridgeIgmpCustomIpAddress": staticBridgeIgmpCustomIpAddress,
       "staticBridgeLoopPrevention": staticBridgeLoopPrevention,
       "staticBridgeIgmpDscp": staticBridgeIgmpDscp,
       "bridgeIfLookupTable": bridgeIfLookupTable,
       "bridgeIfLookupEntry": bridgeIfLookupEntry,
       "bridgeIfAddressType": bridgeIfAddressType,
       "bridgeIfMacOrIpAddress": bridgeIfMacOrIpAddress,
       "bridgeIfLookupStaticOrDynamic": bridgeIfLookupStaticOrDynamic,
       "bridgeIfLookupFlush": bridgeIfLookupFlush,
       "bridgeAddressLookupTable": bridgeAddressLookupTable,
       "bridgeAddressLookupEntry": bridgeAddressLookupEntry,
       "bridgeAddressLookupStaticOrDynamic": bridgeAddressLookupStaticOrDynamic,
       "bridgeAddressLookupFlush": bridgeAddressLookupFlush,
       "packetRuleGroup": packetRuleGroup,
       "packetRuleGroupIndexNext": packetRuleGroupIndexNext,
       "packetRuleGroupNextIndexTable": packetRuleGroupNextIndexTable,
       "packetRuleGroupNextIndexEntry": packetRuleGroupNextIndexEntry,
       "packetRuleGroupMemberNextIndex": packetRuleGroupMemberNextIndex,
       "packetRuleTable": packetRuleTable,
       "packetRuleEntry": packetRuleEntry,
       "packetRuleGroupMemberIndex": packetRuleGroupMemberIndex,
       "packetRuleType": packetRuleType,
       "packetRuleValue": packetRuleValue,
       "packetRuleRowStatus": packetRuleRowStatus,
       "packetRuleValue2": packetRuleValue2,
       "packetRuleValue3": packetRuleValue3,
       "packetRuleValue4": packetRuleValue4,
       "packetRuleValue5": packetRuleValue5,
       "packetRuleGroupIndex": packetRuleGroupIndex,
       "packetRuleValue6": packetRuleValue6,
       "packetRuleValue7": packetRuleValue7,
       "bridgePPPoETable": bridgePPPoETable,
       "bridgePPPoEEntry": bridgePPPoEEntry,
       "bridgePPPoEBrasMac": bridgePPPoEBrasMac,
       "bridgePPPoELocalHostMac": bridgePPPoELocalHostMac,
       "bridgePPPoEEIfIndex": bridgePPPoEEIfIndex,
       "bridgePPPoESessionID": bridgePPPoESessionID,
       "bridgePPPoESlanId": bridgePPPoESlanId,
       "bridgePPPoEVlanId": bridgePPPoEVlanId,
       "bridgePPPoEEncapLLC": bridgePPPoEEncapLLC,
       "stpParam": stpParam,
       "stpParamName": stpParamName,
       "stpParamRevision": stpParamRevision,
       "stpParamBridgePriority": stpParamBridgePriority,
       "stpParamForceVersion": stpParamForceVersion,
       "stpParamFwdDelay": stpParamFwdDelay,
       "stpParamHelloTime": stpParamHelloTime,
       "stpParamMigrateTime": stpParamMigrateTime,
       "stpParamTxHoldCount": stpParamTxHoldCount,
       "stpParamMaxAge": stpParamMaxAge,
       "stpBindTable": stpBindTable,
       "stpBindEntry": stpBindEntry,
       "stpBindInstanceID": stpBindInstanceID,
       "stpBindRowStatus": stpBindRowStatus,
       "stpBindPortPriority": stpBindPortPriority,
       "mstpInstanceTable": mstpInstanceTable,
       "mstpInstanceEntry": mstpInstanceEntry,
       "mstpInstanceRowStatus": mstpInstanceRowStatus,
       "mstpInstanceName": mstpInstanceName,
       "bridgeStatsTable": bridgeStatsTable,
       "bridgeStatsEntry": bridgeStatsEntry,
       "bridgeStatsUcastRcvd": bridgeStatsUcastRcvd,
       "bridgeStatsMcastRcvd": bridgeStatsMcastRcvd,
       "bridgeStatsBcastRcvd": bridgeStatsBcastRcvd,
       "bridgeStatsUcastSent": bridgeStatsUcastSent,
       "bridgeStatsMcastSent": bridgeStatsMcastSent,
       "bridgeStatsBcastSent": bridgeStatsBcastSent,
       "bridgeStatsErrorSent": bridgeStatsErrorSent,
       "bridgeOnDemandStatsRulesSupported": bridgeOnDemandStatsRulesSupported,
       "bridgeOnDemandStatsRulesRemaining": bridgeOnDemandStatsRulesRemaining,
       "bridgeStatsBSDUcastBlocked": bridgeStatsBSDUcastBlocked,
       "bridgeStatsBSDMcastBlocked": bridgeStatsBSDMcastBlocked,
       "bridgeStatsBSDBcastBlocked": bridgeStatsBSDBcastBlocked,
       "bridgeStatsBSDAlarmCount": bridgeStatsBSDAlarmCount,
       "bridgeStatsBytesRcvdCount": bridgeStatsBytesRcvdCount,
       "bridgeStatsBytesSentCount": bridgeStatsBytesSentCount,
       "bridgeStatsTicksLastCleared": bridgeStatsTicksLastCleared,
       "bridgeStatsTicksNow": bridgeStatsTicksNow,
       "bridgeStatsTicksPerSecond": bridgeStatsTicksPerSecond,
       "bridgeCmd": bridgeCmd,
       "bridgeCmdOperation": bridgeCmdOperation,
       "bridgeCmdFilterMask": bridgeCmdFilterMask,
       "bridgeCmdIfIndex": bridgeCmdIfIndex,
       "bridgeCmdVlanId": bridgeCmdVlanId,
       "bridgeCmdSlanId": bridgeCmdSlanId,
       "bridgeCmdSlot": bridgeCmdSlot,
       "bridgeCmdPort": bridgeCmdPort,
       "bridgeCmdIpAddress": bridgeCmdIpAddress,
       "bridgeCmdMacAddress": bridgeCmdMacAddress,
       "eapsGroup": eapsGroup,
       "eapsConfigTable": eapsConfigTable,
       "eapsConfigEntry": eapsConfigEntry,
       "eapsConfigPrimaryPortLineGroup": eapsConfigPrimaryPortLineGroup,
       "eapsConfigSecondaryPortLineGroup": eapsConfigSecondaryPortLineGroup,
       "eapsConfigControlVlan": eapsConfigControlVlan,
       "eapsConfigIsMasterNode": eapsConfigIsMasterNode,
       "eapsConfigControlVlanPriority": eapsConfigControlVlanPriority,
       "eapsConfigDomainName": eapsConfigDomainName,
       "eapsConfigMsgTxInterval": eapsConfigMsgTxInterval,
       "eapsConfigTimeout": eapsConfigTimeout,
       "eapsConfigMaxDroppedMessages": eapsConfigMaxDroppedMessages,
       "eapsConfigSnmpTrap": eapsConfigSnmpTrap,
       "eapsConfigDomainEnable": eapsConfigDomainEnable,
       "eapsConfigRowStatus": eapsConfigRowStatus,
       "eapsProtectedVlanTable": eapsProtectedVlanTable,
       "eapsProtectedVlanEntry": eapsProtectedVlanEntry,
       "eapsProtectedVlanEntryIndex": eapsProtectedVlanEntryIndex,
       "eapsProtectedVlanLowerRange": eapsProtectedVlanLowerRange,
       "eapsProtectedVlanUpperRange": eapsProtectedVlanUpperRange,
       "eapsProtectedVlanRowStatus": eapsProtectedVlanRowStatus,
       "eapsProtectedVlanDomainName": eapsProtectedVlanDomainName,
       "eapsStatusTable": eapsStatusTable,
       "eapsStatusEntry": eapsStatusEntry,
       "eapsPrevState": eapsPrevState,
       "eapsState": eapsState,
       "eapsStatsTable": eapsStatsTable,
       "eapsStatsEntry": eapsStatsEntry,
       "eapsStatsTotCtrlMsgSent": eapsStatsTotCtrlMsgSent,
       "eapsStatsTotCtrlMsgRecvd": eapsStatsTotCtrlMsgRecvd,
       "eapsTrapPrefix": eapsTrapPrefix,
       "eapsTraps": eapsTraps,
       "eapsStateChange": eapsStateChange,
       "eapsFailTimerExpFlagSet": eapsFailTimerExpFlagSet,
       "eapsFailTimerExpFlagClear": eapsFailTimerExpFlagClear,
       "eapsLinkDownRingComplete": eapsLinkDownRingComplete,
       "eapsTopologyTable": eapsTopologyTable,
       "eapsTopologyEntry": eapsTopologyEntry,
       "eapsTopologyRing": eapsTopologyRing,
       "eapsTopologyRowNumber": eapsTopologyRowNumber,
       "eapsTopologyDomainName": eapsTopologyDomainName,
       "eapsTopologyMacAddr": eapsTopologyMacAddr,
       "eapsTopologyIpAddr": eapsTopologyIpAddr,
       "eapsTopologyType": eapsTopologyType,
       "eapsTopologyPrimaryLinkName": eapsTopologyPrimaryLinkName,
       "eapsTopologyPrimaryLinkState": eapsTopologyPrimaryLinkState,
       "eapsTopologySecondaryLinkName": eapsTopologySecondaryLinkName,
       "eapsTopologySecondaryLinkState": eapsTopologySecondaryLinkState,
       "bridgeIgmpStatsTable": bridgeIgmpStatsTable,
       "bridgeIgmpStatsEntry": bridgeIgmpStatsEntry,
       "genQueryRx": genQueryRx,
       "genQueryTx": genQueryTx,
       "specQueryRx": specQueryRx,
       "specQueryTx": specQueryTx,
       "v2ReportsRx": v2ReportsRx,
       "v2ReportsTx": v2ReportsTx,
       "leavesRx": leavesRx,
       "leavesTx": leavesTx,
       "unknownRx": unknownRx,
       "errorRx": errorRx,
       "actChans": actChans,
       "actHosts": actHosts,
       "v3GenQueryRx": v3GenQueryRx,
       "v3GenQueryTx": v3GenQueryTx,
       "v3SpecQueryRx": v3SpecQueryRx,
       "v3SpecQueryTx": v3SpecQueryTx,
       "v3ReportsRx": v3ReportsRx,
       "v3ReportsTx": v3ReportsTx,
       "bridgeGroup": bridgeGroup,
       "bridgeTrapPrefix": bridgeTrapPrefix,
       "bridgeTraps": bridgeTraps,
       "bridgeLoopDetection": bridgeLoopDetection,
       "bridgeStormDetection": bridgeStormDetection,
       "bridgeTrapObjects": bridgeTrapObjects,
       "bridgeMacAddrString": bridgeMacAddrString,
       "bridgeIgmpTable": bridgeIgmpTable,
       "bridgeIgmpEntry": bridgeIgmpEntry,
       "slanId": slanId,
       "vlanId": vlanId,
       "mcastMac": mcastMac,
       "mcastIP": mcastIP,
       "hostMac": hostMac,
       "lastJoinTimer": lastJoinTimer,
       "staticBridgePathTable": staticBridgePathTable,
       "staticBridgePathEntry": staticBridgePathEntry,
       "staticBridgePathMacOrIpAddress": staticBridgePathMacOrIpAddress,
       "staticBridgePathAddressType": staticBridgePathAddressType,
       "staticBridgePathMulticastAging": staticBridgePathMulticastAging,
       "staticBridgePathRowStatus": staticBridgePathRowStatus,
       "staticBridgePathFlapControl": staticBridgePathFlapControl,
       "staticBridgePathUnicastAging": staticBridgePathUnicastAging,
       "staticBridgePathIgmpQueryInterval": staticBridgePathIgmpQueryInterval,
       "staticBridgePathFlags": staticBridgePathFlags,
       "staticBridgePathIgmpCustomIpAddress": staticBridgePathIgmpCustomIpAddress,
       "staticBridgePathLoopPrevention": staticBridgePathLoopPrevention,
       "staticBridgePathIgmpDscp": staticBridgePathIgmpDscp,
       "bridgePathIfLookupTable": bridgePathIfLookupTable,
       "bridgePathIfLookupEntry": bridgePathIfLookupEntry,
       "bridgePathIfAddressType": bridgePathIfAddressType,
       "bridgePathIfMacOrIpAddress": bridgePathIfMacOrIpAddress,
       "bridgePathIfLookupStaticOrDynamic": bridgePathIfLookupStaticOrDynamic,
       "bridgePathIfLookupFlush": bridgePathIfLookupFlush,
       "bridgePathAddressLookupTable": bridgePathAddressLookupTable,
       "bridgePathAddressLookupEntry": bridgePathAddressLookupEntry,
       "bridgePathAddressLookupStaticOrDynamic": bridgePathAddressLookupStaticOrDynamic,
       "bridgePathAddressLookupFlush": bridgePathAddressLookupFlush,
       "bridgeStatusTable": bridgeStatusTable,
       "bridgeStatusEntry": bridgeStatusEntry,
       "bridgeStatusState": bridgeStatusState,
       "bridgeRecord": bridgeRecord,
       "zhoneCompliances": zhoneCompliances,
       "zhoneGroups": zhoneGroups,
       "zhoneBridgeGroup": zhoneBridgeGroup,
       "zhoneBridgeCmdGroup": zhoneBridgeCmdGroup,
       "zhoneBridgeEapsGroup": zhoneBridgeEapsGroup,
       "zhoneBridgeEapsConfigGroup": zhoneBridgeEapsConfigGroup,
       "zhoneBridgeEapsTopologyGroup": zhoneBridgeEapsTopologyGroup,
       "zhoneBridgeNotificationGroup": zhoneBridgeNotificationGroup,
       "zhoneBridgeIgmpGroup": zhoneBridgeIgmpGroup,
       "zhoneBridgeStatsGroup": zhoneBridgeStatsGroup}
)
