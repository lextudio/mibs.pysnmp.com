# SNMP MIB module (CADANT-CMTS-LAYER2CMTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-CMTS-LAYER2CMTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:25 2024
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

(BridgeId,
 Timeout) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "Timeout")

(cadLayer2,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadLayer2")

(AdminState,
 CadBridgeGroupId,
 CadBridgePortType,
 CardId,
 CerCardSubType,
 CerCardType,
 DuplexStatus,
 MacPortId,
 MacPortIdWithInvalid,
 PortId,
 PortType,
 PrimaryState,
 SecondaryState) = mibBuilder.importSymbols(
    "CADANT-TC",
    "AdminState",
    "CadBridgeGroupId",
    "CadBridgePortType",
    "CardId",
    "CerCardSubType",
    "CerCardType",
    "DuplexStatus",
    "MacPortId",
    "MacPortIdWithInvalid",
    "PortId",
    "PortType",
    "PrimaryState",
    "SecondaryState")

(AttributeMask,
 IfDirection) = mibBuilder.importSymbols(
    "DOCS-IF3-MIB",
    "AttributeMask",
    "IfDirection")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetVersion,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetVersion")

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
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

cadLayer2Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1)
)
cadLayer2Mib.setRevisions(
        ("2015-08-25 00:00",
         "2015-06-17 00:00",
         "2015-04-15 00:00",
         "2015-04-01 00:00",
         "2015-01-21 00:00",
         "2015-01-20 00:00",
         "2014-12-09 00:00",
         "2014-12-08 00:00",
         "2014-12-03 00:00",
         "2014-11-18 00:00",
         "2014-10-15 00:00",
         "2014-10-14 00:00",
         "2014-09-19 00:00",
         "2014-08-01 00:00",
         "2014-07-03 00:00",
         "2014-06-24 00:00",
         "2014-03-10 00:00",
         "2014-01-15 00:00",
         "2013-10-30 00:00",
         "2013-08-08 00:00",
         "2013-05-30 00:00",
         "2013-05-17 00:00",
         "2013-05-08 00:00",
         "2013-04-29 00:00",
         "2013-03-25 00:00",
         "2013-01-03 00:00",
         "2012-11-20 00:00",
         "2011-10-05 00:00",
         "2011-08-17 00:00",
         "2011-03-03 00:00",
         "2010-08-10 00:00",
         "2010-06-23 00:00",
         "2010-03-01 00:00",
         "2009-10-22 00:00",
         "2009-10-12 00:00",
         "2009-09-02 00:00",
         "2009-07-17 00:00",
         "2009-01-12 00:00",
         "2009-01-07 00:00",
         "2009-01-05 00:00",
         "2008-11-11 00:00",
         "2008-09-30 00:00",
         "2008-02-08 00:00",
         "2008-02-06 00:00",
         "2008-01-22 00:00",
         "2008-01-03 00:00",
         "2007-12-14 00:00",
         "2007-08-28 00:00",
         "2007-08-13 00:00",
         "2007-05-31 00:00",
         "2007-05-14 00:00",
         "2007-05-08 00:00",
         "2007-03-01 00:00",
         "2007-02-07 00:00",
         "2007-02-05 00:00",
         "2006-11-27 00:00",
         "2006-11-01 00:00",
         "2006-10-13 00:00",
         "2006-09-12 00:00",
         "2006-09-01 00:00",
         "2006-08-02 00:00",
         "2006-01-31 00:00",
         "2006-01-27 00:00",
         "2006-01-04 00:00",
         "2005-10-24 00:00",
         "2003-09-26 00:00",
         "2002-10-21 00:00",
         "2001-10-18 00:00",
         "2001-09-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CadTftpEnforceType(Integer32, TextualConvention):
    status = "current"
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
        *(("block", 4),
          ("disabled", 0),
          ("enabled", 1),
          ("lock", 3),
          ("mark-only", 2))
    )



class CadDynamicSecretType(Integer32, TextualConvention):
    status = "current"
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
        *(("block", 4),
          ("disabled", 0),
          ("lock", 3),
          ("mark", 2),
          ("reject", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CadBridgeGroup_ObjectIdentity = ObjectIdentity
cadBridgeGroup = _CadBridgeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1)
)
_CadBridgeGroupGeneral_ObjectIdentity = ObjectIdentity
cadBridgeGroupGeneral = _CadBridgeGroupGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 1)
)
_CadBridgeGroupMaxNum_Type = Integer32
_CadBridgeGroupMaxNum_Object = MibScalar
cadBridgeGroupMaxNum = _CadBridgeGroupMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 1, 1),
    _CadBridgeGroupMaxNum_Type()
)
cadBridgeGroupMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadBridgeGroupMaxNum.setStatus("current")
_CadBridgeGroupTable_Object = MibTable
cadBridgeGroupTable = _CadBridgeGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cadBridgeGroupTable.setStatus("current")
_CadBridgeGroupEntry_Object = MibTableRow
cadBridgeGroupEntry = _CadBridgeGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 2, 1)
)
cadBridgeGroupEntry.setIndexNames(
    (0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadBgIndex"),
)
if mibBuilder.loadTexts:
    cadBridgeGroupEntry.setStatus("current")
_CadBgIndex_Type = CadBridgeGroupId
_CadBgIndex_Object = MibTableColumn
cadBgIndex = _CadBgIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 2, 1, 1),
    _CadBgIndex_Type()
)
cadBgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadBgIndex.setStatus("current")


class _CadBgName_Type(DisplayString):
    """Custom type cadBgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CadBgName_Type.__name__ = "DisplayString"
_CadBgName_Object = MibTableColumn
cadBgName = _CadBgName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 2, 1, 2),
    _CadBgName_Type()
)
cadBgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadBgName.setStatus("current")
_CadBgRowStatus_Type = RowStatus
_CadBgRowStatus_Object = MibTableColumn
cadBgRowStatus = _CadBgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 2, 1, 11),
    _CadBgRowStatus_Type()
)
cadBgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadBgRowStatus.setStatus("current")
_CadBridgeGroupStatsTable_Object = MibTable
cadBridgeGroupStatsTable = _CadBridgeGroupStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 10)
)
if mibBuilder.loadTexts:
    cadBridgeGroupStatsTable.setStatus("current")
_CadBridgeGroupStatsEntry_Object = MibTableRow
cadBridgeGroupStatsEntry = _CadBridgeGroupStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    cadBridgeGroupStatsEntry.setStatus("current")
_CadBgLeaderBgpId_Type = InterfaceIndexOrZero
_CadBgLeaderBgpId_Object = MibTableColumn
cadBgLeaderBgpId = _CadBgLeaderBgpId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 10, 1, 1),
    _CadBgLeaderBgpId_Type()
)
cadBgLeaderBgpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadBgLeaderBgpId.setStatus("current")
_CadBgMacAddress_Type = MacAddress
_CadBgMacAddress_Object = MibTableColumn
cadBgMacAddress = _CadBgMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 10, 1, 2),
    _CadBgMacAddress_Type()
)
cadBgMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadBgMacAddress.setStatus("current")
_CadBridgePortTable_Object = MibTable
cadBridgePortTable = _CadBridgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 11)
)
if mibBuilder.loadTexts:
    cadBridgePortTable.setStatus("current")
_CadBridgePortEntry_Object = MibTableRow
cadBridgePortEntry = _CadBridgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 11, 1)
)
cadBridgePortEntry.setIndexNames(
    (0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadBgpId"),
    (0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadBgpType"),
)
if mibBuilder.loadTexts:
    cadBridgePortEntry.setStatus("current")
_CadBgpGroupId_Type = CadBridgeGroupId
_CadBgpGroupId_Object = MibTableColumn
cadBgpGroupId = _CadBgpGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 11, 1, 1),
    _CadBgpGroupId_Type()
)
cadBgpGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadBgpGroupId.setStatus("current")
_CadBgpId_Type = InterfaceIndex
_CadBgpId_Object = MibTableColumn
cadBgpId = _CadBgpId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 11, 1, 2),
    _CadBgpId_Type()
)
cadBgpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadBgpId.setStatus("current")
_CadBgpCardId_Type = CardId
_CadBgpCardId_Object = MibTableColumn
cadBgpCardId = _CadBgpCardId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 11, 1, 3),
    _CadBgpCardId_Type()
)
cadBgpCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadBgpCardId.setStatus("current")
_CadBgpCardType_Type = CerCardType
_CadBgpCardType_Object = MibTableColumn
cadBgpCardType = _CadBgpCardType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 11, 1, 4),
    _CadBgpCardType_Type()
)
cadBgpCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadBgpCardType.setStatus("current")
_CadBgpPortId_Type = PortId
_CadBgpPortId_Object = MibTableColumn
cadBgpPortId = _CadBgpPortId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 11, 1, 5),
    _CadBgpPortId_Type()
)
cadBgpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadBgpPortId.setStatus("current")
_CadBgpType_Type = CadBridgePortType
_CadBgpType_Object = MibTableColumn
cadBgpType = _CadBgpType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 11, 1, 6),
    _CadBgpType_Type()
)
cadBgpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadBgpType.setStatus("current")


class _CadBgpBundleGroupId_Type(InterfaceIndexOrZero):
    """Custom type cadBgpBundleGroupId based on InterfaceIndexOrZero"""
    defaultValue = 0


_CadBgpBundleGroupId_Object = MibTableColumn
cadBgpBundleGroupId = _CadBgpBundleGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 11, 1, 10),
    _CadBgpBundleGroupId_Type()
)
cadBgpBundleGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadBgpBundleGroupId.setStatus("current")
_CadBgpMacAddress_Type = MacAddress
_CadBgpMacAddress_Object = MibTableColumn
cadBgpMacAddress = _CadBgpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 11, 1, 11),
    _CadBgpMacAddress_Type()
)
cadBgpMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadBgpMacAddress.setStatus("current")
_CadBridgeGroupPortStatusTable_Object = MibTable
cadBridgeGroupPortStatusTable = _CadBridgeGroupPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 12)
)
if mibBuilder.loadTexts:
    cadBridgeGroupPortStatusTable.setStatus("current")
_CadBridgeGroupPortStatusEntry_Object = MibTableRow
cadBridgeGroupPortStatusEntry = _CadBridgeGroupPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 12, 1)
)
cadBridgeGroupPortStatusEntry.setIndexNames(
    (0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadBgpStatGroupId"),
    (0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadBgpStatMacIfIndex"),
    (0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadBgpStatPhyIfIndex"),
)
if mibBuilder.loadTexts:
    cadBridgeGroupPortStatusEntry.setStatus("current")
_CadBgpStatGroupId_Type = CadBridgeGroupId
_CadBgpStatGroupId_Object = MibTableColumn
cadBgpStatGroupId = _CadBgpStatGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 12, 1, 1),
    _CadBgpStatGroupId_Type()
)
cadBgpStatGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadBgpStatGroupId.setStatus("current")
_CadBgpStatMacIfIndex_Type = InterfaceIndex
_CadBgpStatMacIfIndex_Object = MibTableColumn
cadBgpStatMacIfIndex = _CadBgpStatMacIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 12, 1, 2),
    _CadBgpStatMacIfIndex_Type()
)
cadBgpStatMacIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadBgpStatMacIfIndex.setStatus("current")
_CadBgpStatPhyIfIndex_Type = InterfaceIndex
_CadBgpStatPhyIfIndex_Object = MibTableColumn
cadBgpStatPhyIfIndex = _CadBgpStatPhyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 12, 1, 3),
    _CadBgpStatPhyIfIndex_Type()
)
cadBgpStatPhyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadBgpStatPhyIfIndex.setStatus("current")
_CadBgpStatPhyCardId_Type = CardId
_CadBgpStatPhyCardId_Object = MibTableColumn
cadBgpStatPhyCardId = _CadBgpStatPhyCardId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 12, 1, 4),
    _CadBgpStatPhyCardId_Type()
)
cadBgpStatPhyCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadBgpStatPhyCardId.setStatus("current")
_CadBgpStatPhyPortId_Type = PortId
_CadBgpStatPhyPortId_Object = MibTableColumn
cadBgpStatPhyPortId = _CadBgpStatPhyPortId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 12, 1, 5),
    _CadBgpStatPhyPortId_Type()
)
cadBgpStatPhyPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadBgpStatPhyPortId.setStatus("current")
_CadDot3adAggTable_Object = MibTable
cadDot3adAggTable = _CadDot3adAggTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 13)
)
if mibBuilder.loadTexts:
    cadDot3adAggTable.setStatus("current")
_CadDot3adAggEntry_Object = MibTableRow
cadDot3adAggEntry = _CadDot3adAggEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 13, 1)
)
cadDot3adAggEntry.setIndexNames(
    (0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadDot3adAggId"),
)
if mibBuilder.loadTexts:
    cadDot3adAggEntry.setStatus("current")


class _CadDot3adAggId_Type(Integer32):
    """Custom type cadDot3adAggId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CadDot3adAggId_Type.__name__ = "Integer32"
_CadDot3adAggId_Object = MibTableColumn
cadDot3adAggId = _CadDot3adAggId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 13, 1, 1),
    _CadDot3adAggId_Type()
)
cadDot3adAggId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadDot3adAggId.setStatus("current")
_CadDot3adAggIndex_Type = InterfaceIndex
_CadDot3adAggIndex_Object = MibTableColumn
cadDot3adAggIndex = _CadDot3adAggIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 13, 1, 2),
    _CadDot3adAggIndex_Type()
)
cadDot3adAggIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDot3adAggIndex.setStatus("current")
_CadDot3adAggMacAddress_Type = MacAddress
_CadDot3adAggMacAddress_Object = MibTableColumn
cadDot3adAggMacAddress = _CadDot3adAggMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 13, 1, 3),
    _CadDot3adAggMacAddress_Type()
)
cadDot3adAggMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDot3adAggMacAddress.setStatus("current")


class _CadDot3adAggLacpEnable_Type(TruthValue):
    """Custom type cadDot3adAggLacpEnable based on TruthValue"""


_CadDot3adAggLacpEnable_Object = MibTableColumn
cadDot3adAggLacpEnable = _CadDot3adAggLacpEnable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 13, 1, 4),
    _CadDot3adAggLacpEnable_Type()
)
cadDot3adAggLacpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDot3adAggLacpEnable.setStatus("current")


class _CadDot3adAggLacpMode_Type(Integer32):
    """Custom type cadDot3adAggLacpMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_CadDot3adAggLacpMode_Type.__name__ = "Integer32"
_CadDot3adAggLacpMode_Object = MibTableColumn
cadDot3adAggLacpMode = _CadDot3adAggLacpMode_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 13, 1, 5),
    _CadDot3adAggLacpMode_Type()
)
cadDot3adAggLacpMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDot3adAggLacpMode.setStatus("current")


class _CadDot3adAggLacpRate_Type(Integer32):
    """Custom type cadDot3adAggLacpRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fast", 2),
          ("slow", 1))
    )


_CadDot3adAggLacpRate_Type.__name__ = "Integer32"
_CadDot3adAggLacpRate_Object = MibTableColumn
cadDot3adAggLacpRate = _CadDot3adAggLacpRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 13, 1, 6),
    _CadDot3adAggLacpRate_Type()
)
cadDot3adAggLacpRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDot3adAggLacpRate.setStatus("current")


class _CadDot3adAggMinLinks_Type(Integer32):
    """Custom type cadDot3adAggMinLinks based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CadDot3adAggMinLinks_Type.__name__ = "Integer32"
_CadDot3adAggMinLinks_Object = MibTableColumn
cadDot3adAggMinLinks = _CadDot3adAggMinLinks_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 13, 1, 7),
    _CadDot3adAggMinLinks_Type()
)
cadDot3adAggMinLinks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDot3adAggMinLinks.setStatus("current")


class _CadDot3adAggDescription_Type(DisplayString):
    """Custom type cadDot3adAggDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CadDot3adAggDescription_Type.__name__ = "DisplayString"
_CadDot3adAggDescription_Object = MibTableColumn
cadDot3adAggDescription = _CadDot3adAggDescription_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 13, 1, 8),
    _CadDot3adAggDescription_Type()
)
cadDot3adAggDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDot3adAggDescription.setStatus("current")


class _CadDot3adAggTrapInh_Type(Bits):
    """Custom type cadDot3adAggTrapInh based on Bits"""
    defaultHexValue = "e0"

    namedValues = NamedValues(
        *(("duplex", 2),
          ("linkUpLinkDown", 3),
          ("primary", 0),
          ("secondary", 1))
    )

_CadDot3adAggTrapInh_Type.__name__ = "Bits"
_CadDot3adAggTrapInh_Object = MibTableColumn
cadDot3adAggTrapInh = _CadDot3adAggTrapInh_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 13, 1, 9),
    _CadDot3adAggTrapInh_Type()
)
cadDot3adAggTrapInh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDot3adAggTrapInh.setStatus("current")


class _CadDot3adAggAdminState_Type(AdminState):
    """Custom type cadDot3adAggAdminState based on AdminState"""


_CadDot3adAggAdminState_Object = MibTableColumn
cadDot3adAggAdminState = _CadDot3adAggAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 13, 1, 10),
    _CadDot3adAggAdminState_Type()
)
cadDot3adAggAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDot3adAggAdminState.setStatus("current")


class _CadDot3adAggPrState_Type(PrimaryState):
    """Custom type cadDot3adAggPrState based on PrimaryState"""


_CadDot3adAggPrState_Object = MibTableColumn
cadDot3adAggPrState = _CadDot3adAggPrState_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 13, 1, 11),
    _CadDot3adAggPrState_Type()
)
cadDot3adAggPrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDot3adAggPrState.setStatus("current")


class _CadDot3adAggSecState_Type(SecondaryState):
    """Custom type cadDot3adAggSecState based on SecondaryState"""


_CadDot3adAggSecState_Object = MibTableColumn
cadDot3adAggSecState = _CadDot3adAggSecState_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 13, 1, 12),
    _CadDot3adAggSecState_Type()
)
cadDot3adAggSecState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDot3adAggSecState.setStatus("current")
_CadDot3adAggRowStatus_Type = RowStatus
_CadDot3adAggRowStatus_Object = MibTableColumn
cadDot3adAggRowStatus = _CadDot3adAggRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 13, 1, 13),
    _CadDot3adAggRowStatus_Type()
)
cadDot3adAggRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDot3adAggRowStatus.setStatus("current")
_CadDot3adAggSystemID_Type = MacAddress
_CadDot3adAggSystemID_Object = MibTableColumn
cadDot3adAggSystemID = _CadDot3adAggSystemID_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 13, 1, 14),
    _CadDot3adAggSystemID_Type()
)
cadDot3adAggSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDot3adAggSystemID.setStatus("current")
_CadDot3adParams_ObjectIdentity = ObjectIdentity
cadDot3adParams = _CadDot3adParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 14)
)


class _CadDot3adSystemPriority_Type(Integer32):
    """Custom type cadDot3adSystemPriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadDot3adSystemPriority_Type.__name__ = "Integer32"
_CadDot3adSystemPriority_Object = MibScalar
cadDot3adSystemPriority = _CadDot3adSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 1, 14, 1),
    _CadDot3adSystemPriority_Type()
)
cadDot3adSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDot3adSystemPriority.setStatus("current")
_CadAging_ObjectIdentity = ObjectIdentity
cadAging = _CadAging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 2)
)


class _CadAgingCPEAgingInterval_Type(TimeInterval):
    """Custom type cadAgingCPEAgingInterval based on TimeInterval"""
    defaultValue = 10

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
    )


_CadAgingCPEAgingInterval_Type.__name__ = "TimeInterval"
_CadAgingCPEAgingInterval_Object = MibScalar
cadAgingCPEAgingInterval = _CadAgingCPEAgingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 2, 1),
    _CadAgingCPEAgingInterval_Type()
)
cadAgingCPEAgingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAgingCPEAgingInterval.setStatus("current")


class _CadAgingSFAgingInterval_Type(TimeInterval):
    """Custom type cadAgingSFAgingInterval based on TimeInterval"""
    defaultValue = 1

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CadAgingSFAgingInterval_Type.__name__ = "TimeInterval"
_CadAgingSFAgingInterval_Object = MibScalar
cadAgingSFAgingInterval = _CadAgingSFAgingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 2, 2),
    _CadAgingSFAgingInterval_Type()
)
cadAgingSFAgingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAgingSFAgingInterval.setStatus("current")


class _CadAgingStaleMACAgingInterval_Type(Integer32):
    """Custom type cadAgingStaleMACAgingInterval based on Integer32"""
    defaultValue = 604800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000000),
    )


_CadAgingStaleMACAgingInterval_Type.__name__ = "Integer32"
_CadAgingStaleMACAgingInterval_Object = MibScalar
cadAgingStaleMACAgingInterval = _CadAgingStaleMACAgingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 2, 3),
    _CadAgingStaleMACAgingInterval_Type()
)
cadAgingStaleMACAgingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAgingStaleMACAgingInterval.setStatus("current")


class _CadAgingArpCacheAgingInterval_Type(Integer32):
    """Custom type cadAgingArpCacheAgingInterval based on Integer32"""
    defaultValue = 1200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(600, 360000),
    )


_CadAgingArpCacheAgingInterval_Type.__name__ = "Integer32"
_CadAgingArpCacheAgingInterval_Object = MibScalar
cadAgingArpCacheAgingInterval = _CadAgingArpCacheAgingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 2, 4),
    _CadAgingArpCacheAgingInterval_Type()
)
cadAgingArpCacheAgingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAgingArpCacheAgingInterval.setStatus("current")
if mibBuilder.loadTexts:
    cadAgingArpCacheAgingInterval.setUnits("seconds")


class _CadAgingIdleMACAgingInterval_Type(Integer32):
    """Custom type cadAgingIdleMACAgingInterval based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_CadAgingIdleMACAgingInterval_Type.__name__ = "Integer32"
_CadAgingIdleMACAgingInterval_Object = MibScalar
cadAgingIdleMACAgingInterval = _CadAgingIdleMACAgingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 2, 5),
    _CadAgingIdleMACAgingInterval_Type()
)
cadAgingIdleMACAgingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAgingIdleMACAgingInterval.setStatus("current")


class _CadAgingArpCacheSearchingRateLimit_Type(Integer32):
    """Custom type cadAgingArpCacheSearchingRateLimit based on Integer32"""
    defaultValue = 333

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 86400000),
    )


_CadAgingArpCacheSearchingRateLimit_Type.__name__ = "Integer32"
_CadAgingArpCacheSearchingRateLimit_Object = MibScalar
cadAgingArpCacheSearchingRateLimit = _CadAgingArpCacheSearchingRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 2, 6),
    _CadAgingArpCacheSearchingRateLimit_Type()
)
cadAgingArpCacheSearchingRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAgingArpCacheSearchingRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    cadAgingArpCacheSearchingRateLimit.setUnits("milliseconds")


class _CadAgingArpCacheSearchingMaxNumber_Type(Integer32):
    """Custom type cadAgingArpCacheSearchingMaxNumber based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadAgingArpCacheSearchingMaxNumber_Type.__name__ = "Integer32"
_CadAgingArpCacheSearchingMaxNumber_Object = MibScalar
cadAgingArpCacheSearchingMaxNumber = _CadAgingArpCacheSearchingMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 2, 7),
    _CadAgingArpCacheSearchingMaxNumber_Type()
)
cadAgingArpCacheSearchingMaxNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAgingArpCacheSearchingMaxNumber.setStatus("current")


class _CadAgingArpCacheNotPresentRateLimit_Type(Integer32):
    """Custom type cadAgingArpCacheNotPresentRateLimit based on Integer32"""
    defaultValue = 333

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 86400000),
    )


_CadAgingArpCacheNotPresentRateLimit_Type.__name__ = "Integer32"
_CadAgingArpCacheNotPresentRateLimit_Object = MibScalar
cadAgingArpCacheNotPresentRateLimit = _CadAgingArpCacheNotPresentRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 2, 8),
    _CadAgingArpCacheNotPresentRateLimit_Type()
)
cadAgingArpCacheNotPresentRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAgingArpCacheNotPresentRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    cadAgingArpCacheNotPresentRateLimit.setUnits("milliseconds")


class _CadAgingArpCacheNotPresentMaxNumber_Type(Integer32):
    """Custom type cadAgingArpCacheNotPresentMaxNumber based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadAgingArpCacheNotPresentMaxNumber_Type.__name__ = "Integer32"
_CadAgingArpCacheNotPresentMaxNumber_Object = MibScalar
cadAgingArpCacheNotPresentMaxNumber = _CadAgingArpCacheNotPresentMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 2, 9),
    _CadAgingArpCacheNotPresentMaxNumber_Type()
)
cadAgingArpCacheNotPresentMaxNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAgingArpCacheNotPresentMaxNumber.setStatus("current")


class _CadAgingArpCacheNotPresentMaxTime_Type(Integer32):
    """Custom type cadAgingArpCacheNotPresentMaxTime based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_CadAgingArpCacheNotPresentMaxTime_Type.__name__ = "Integer32"
_CadAgingArpCacheNotPresentMaxTime_Object = MibScalar
cadAgingArpCacheNotPresentMaxTime = _CadAgingArpCacheNotPresentMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 2, 10),
    _CadAgingArpCacheNotPresentMaxTime_Type()
)
cadAgingArpCacheNotPresentMaxTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAgingArpCacheNotPresentMaxTime.setStatus("current")
if mibBuilder.loadTexts:
    cadAgingArpCacheNotPresentMaxTime.setUnits("seconds")


class _CadAgingArpCacheNotPresentMinTime_Type(Integer32):
    """Custom type cadAgingArpCacheNotPresentMinTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_CadAgingArpCacheNotPresentMinTime_Type.__name__ = "Integer32"
_CadAgingArpCacheNotPresentMinTime_Object = MibScalar
cadAgingArpCacheNotPresentMinTime = _CadAgingArpCacheNotPresentMinTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 2, 11),
    _CadAgingArpCacheNotPresentMinTime_Type()
)
cadAgingArpCacheNotPresentMinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAgingArpCacheNotPresentMinTime.setStatus("current")
if mibBuilder.loadTexts:
    cadAgingArpCacheNotPresentMinTime.setUnits("seconds")


class _CadAgingArpCacheSearchingGlobalMaxRate_Type(Integer32):
    """Custom type cadAgingArpCacheSearchingGlobalMaxRate based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadAgingArpCacheSearchingGlobalMaxRate_Type.__name__ = "Integer32"
_CadAgingArpCacheSearchingGlobalMaxRate_Object = MibScalar
cadAgingArpCacheSearchingGlobalMaxRate = _CadAgingArpCacheSearchingGlobalMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 2, 12),
    _CadAgingArpCacheSearchingGlobalMaxRate_Type()
)
cadAgingArpCacheSearchingGlobalMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAgingArpCacheSearchingGlobalMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    cadAgingArpCacheSearchingGlobalMaxRate.setUnits("packets/second")


class _CadAgingArpCacheNotPresentGlobalMaxRate_Type(Integer32):
    """Custom type cadAgingArpCacheNotPresentGlobalMaxRate based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadAgingArpCacheNotPresentGlobalMaxRate_Type.__name__ = "Integer32"
_CadAgingArpCacheNotPresentGlobalMaxRate_Object = MibScalar
cadAgingArpCacheNotPresentGlobalMaxRate = _CadAgingArpCacheNotPresentGlobalMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 2, 13),
    _CadAgingArpCacheNotPresentGlobalMaxRate_Type()
)
cadAgingArpCacheNotPresentGlobalMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAgingArpCacheNotPresentGlobalMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    cadAgingArpCacheNotPresentGlobalMaxRate.setUnits("packets/second")


class _CadAgingNDCacheAgingInterval_Type(Integer32):
    """Custom type cadAgingNDCacheAgingInterval based on Integer32"""
    defaultValue = 1200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(180, 360000),
    )


_CadAgingNDCacheAgingInterval_Type.__name__ = "Integer32"
_CadAgingNDCacheAgingInterval_Object = MibScalar
cadAgingNDCacheAgingInterval = _CadAgingNDCacheAgingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 2, 14),
    _CadAgingNDCacheAgingInterval_Type()
)
cadAgingNDCacheAgingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAgingNDCacheAgingInterval.setStatus("current")
if mibBuilder.loadTexts:
    cadAgingNDCacheAgingInterval.setUnits("seconds")


class _CadAgingNDCacheSearchingRateLimit_Type(Integer32):
    """Custom type cadAgingNDCacheSearchingRateLimit based on Integer32"""
    defaultValue = 333

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 86400000),
    )


_CadAgingNDCacheSearchingRateLimit_Type.__name__ = "Integer32"
_CadAgingNDCacheSearchingRateLimit_Object = MibScalar
cadAgingNDCacheSearchingRateLimit = _CadAgingNDCacheSearchingRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 2, 15),
    _CadAgingNDCacheSearchingRateLimit_Type()
)
cadAgingNDCacheSearchingRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAgingNDCacheSearchingRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    cadAgingNDCacheSearchingRateLimit.setUnits("milliseconds")


class _CadAgingNDCacheSearchingMaxNumber_Type(Integer32):
    """Custom type cadAgingNDCacheSearchingMaxNumber based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadAgingNDCacheSearchingMaxNumber_Type.__name__ = "Integer32"
_CadAgingNDCacheSearchingMaxNumber_Object = MibScalar
cadAgingNDCacheSearchingMaxNumber = _CadAgingNDCacheSearchingMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 2, 16),
    _CadAgingNDCacheSearchingMaxNumber_Type()
)
cadAgingNDCacheSearchingMaxNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAgingNDCacheSearchingMaxNumber.setStatus("current")


class _CadAgingNDCacheNotPresentRateLimit_Type(Integer32):
    """Custom type cadAgingNDCacheNotPresentRateLimit based on Integer32"""
    defaultValue = 333

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 86400000),
    )


_CadAgingNDCacheNotPresentRateLimit_Type.__name__ = "Integer32"
_CadAgingNDCacheNotPresentRateLimit_Object = MibScalar
cadAgingNDCacheNotPresentRateLimit = _CadAgingNDCacheNotPresentRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 2, 17),
    _CadAgingNDCacheNotPresentRateLimit_Type()
)
cadAgingNDCacheNotPresentRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAgingNDCacheNotPresentRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    cadAgingNDCacheNotPresentRateLimit.setUnits("milliseconds")


class _CadAgingNDCacheNotPresentMaxNumber_Type(Integer32):
    """Custom type cadAgingNDCacheNotPresentMaxNumber based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadAgingNDCacheNotPresentMaxNumber_Type.__name__ = "Integer32"
_CadAgingNDCacheNotPresentMaxNumber_Object = MibScalar
cadAgingNDCacheNotPresentMaxNumber = _CadAgingNDCacheNotPresentMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 2, 18),
    _CadAgingNDCacheNotPresentMaxNumber_Type()
)
cadAgingNDCacheNotPresentMaxNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAgingNDCacheNotPresentMaxNumber.setStatus("current")


class _CadAgingNDCacheNotPresentMaxTime_Type(Integer32):
    """Custom type cadAgingNDCacheNotPresentMaxTime based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_CadAgingNDCacheNotPresentMaxTime_Type.__name__ = "Integer32"
_CadAgingNDCacheNotPresentMaxTime_Object = MibScalar
cadAgingNDCacheNotPresentMaxTime = _CadAgingNDCacheNotPresentMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 2, 19),
    _CadAgingNDCacheNotPresentMaxTime_Type()
)
cadAgingNDCacheNotPresentMaxTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAgingNDCacheNotPresentMaxTime.setStatus("current")
if mibBuilder.loadTexts:
    cadAgingNDCacheNotPresentMaxTime.setUnits("seconds")


class _CadAgingNDCacheNotPresentMinTime_Type(Integer32):
    """Custom type cadAgingNDCacheNotPresentMinTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_CadAgingNDCacheNotPresentMinTime_Type.__name__ = "Integer32"
_CadAgingNDCacheNotPresentMinTime_Object = MibScalar
cadAgingNDCacheNotPresentMinTime = _CadAgingNDCacheNotPresentMinTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 2, 20),
    _CadAgingNDCacheNotPresentMinTime_Type()
)
cadAgingNDCacheNotPresentMinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAgingNDCacheNotPresentMinTime.setStatus("current")
if mibBuilder.loadTexts:
    cadAgingNDCacheNotPresentMinTime.setUnits("seconds")


class _CadAgingNDCacheSearchingGlobalMaxRate_Type(Integer32):
    """Custom type cadAgingNDCacheSearchingGlobalMaxRate based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadAgingNDCacheSearchingGlobalMaxRate_Type.__name__ = "Integer32"
_CadAgingNDCacheSearchingGlobalMaxRate_Object = MibScalar
cadAgingNDCacheSearchingGlobalMaxRate = _CadAgingNDCacheSearchingGlobalMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 2, 21),
    _CadAgingNDCacheSearchingGlobalMaxRate_Type()
)
cadAgingNDCacheSearchingGlobalMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAgingNDCacheSearchingGlobalMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    cadAgingNDCacheSearchingGlobalMaxRate.setUnits("packets/second")


class _CadAgingNDCacheNotPresentGlobalMaxRate_Type(Integer32):
    """Custom type cadAgingNDCacheNotPresentGlobalMaxRate based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadAgingNDCacheNotPresentGlobalMaxRate_Type.__name__ = "Integer32"
_CadAgingNDCacheNotPresentGlobalMaxRate_Object = MibScalar
cadAgingNDCacheNotPresentGlobalMaxRate = _CadAgingNDCacheNotPresentGlobalMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 2, 22),
    _CadAgingNDCacheNotPresentGlobalMaxRate_Type()
)
cadAgingNDCacheNotPresentGlobalMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAgingNDCacheNotPresentGlobalMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    cadAgingNDCacheNotPresentGlobalMaxRate.setUnits("packets/second")


class _CadAgingArpCacheSearchingCableUnicast_Type(Integer32):
    """Custom type cadAgingArpCacheSearchingCableUnicast based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadAgingArpCacheSearchingCableUnicast_Type.__name__ = "Integer32"
_CadAgingArpCacheSearchingCableUnicast_Object = MibScalar
cadAgingArpCacheSearchingCableUnicast = _CadAgingArpCacheSearchingCableUnicast_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 2, 23),
    _CadAgingArpCacheSearchingCableUnicast_Type()
)
cadAgingArpCacheSearchingCableUnicast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAgingArpCacheSearchingCableUnicast.setStatus("current")


class _CadAgingArpCacheSearchingCableBroadcast_Type(TruthValue):
    """Custom type cadAgingArpCacheSearchingCableBroadcast based on TruthValue"""


_CadAgingArpCacheSearchingCableBroadcast_Object = MibScalar
cadAgingArpCacheSearchingCableBroadcast = _CadAgingArpCacheSearchingCableBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 2, 24),
    _CadAgingArpCacheSearchingCableBroadcast_Type()
)
cadAgingArpCacheSearchingCableBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAgingArpCacheSearchingCableBroadcast.setStatus("current")


class _CadAgingNDCacheSearchingCableUnicast_Type(Integer32):
    """Custom type cadAgingNDCacheSearchingCableUnicast based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CadAgingNDCacheSearchingCableUnicast_Type.__name__ = "Integer32"
_CadAgingNDCacheSearchingCableUnicast_Object = MibScalar
cadAgingNDCacheSearchingCableUnicast = _CadAgingNDCacheSearchingCableUnicast_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 2, 25),
    _CadAgingNDCacheSearchingCableUnicast_Type()
)
cadAgingNDCacheSearchingCableUnicast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAgingNDCacheSearchingCableUnicast.setStatus("current")


class _CadAgingNDCacheSearchingCableMulticast_Type(TruthValue):
    """Custom type cadAgingNDCacheSearchingCableMulticast based on TruthValue"""


_CadAgingNDCacheSearchingCableMulticast_Object = MibScalar
cadAgingNDCacheSearchingCableMulticast = _CadAgingNDCacheSearchingCableMulticast_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 2, 26),
    _CadAgingNDCacheSearchingCableMulticast_Type()
)
cadAgingNDCacheSearchingCableMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadAgingNDCacheSearchingCableMulticast.setStatus("current")
_CadLayer2MibGroup_ObjectIdentity = ObjectIdentity
cadLayer2MibGroup = _CadLayer2MibGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 3)
)
_CadMacPortMIBObjects_ObjectIdentity = ObjectIdentity
cadMacPortMIBObjects = _CadMacPortMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4)
)
_CadMacPortTable_Object = MibTable
cadMacPortTable = _CadMacPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cadMacPortTable.setStatus("current")
_CadMacPortEntry_Object = MibTableRow
cadMacPortEntry = _CadMacPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 1, 1)
)
cadMacPortEntry.setIndexNames(
    (0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadMacPortId"),
)
if mibBuilder.loadTexts:
    cadMacPortEntry.setStatus("current")
_CadMacPortId_Type = MacPortId
_CadMacPortId_Object = MibTableColumn
cadMacPortId = _CadMacPortId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 1, 1, 1),
    _CadMacPortId_Type()
)
cadMacPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadMacPortId.setStatus("current")


class _CadMacPortAdminState_Type(AdminState):
    """Custom type cadMacPortAdminState based on AdminState"""


_CadMacPortAdminState_Object = MibTableColumn
cadMacPortAdminState = _CadMacPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 1, 1, 4),
    _CadMacPortAdminState_Type()
)
cadMacPortAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadMacPortAdminState.setStatus("current")


class _CadMacPortPrState_Type(PrimaryState):
    """Custom type cadMacPortPrState based on PrimaryState"""


_CadMacPortPrState_Object = MibTableColumn
cadMacPortPrState = _CadMacPortPrState_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 1, 1, 5),
    _CadMacPortPrState_Type()
)
cadMacPortPrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMacPortPrState.setStatus("current")


class _CadMacPortSecState_Type(SecondaryState):
    """Custom type cadMacPortSecState based on SecondaryState"""


_CadMacPortSecState_Object = MibTableColumn
cadMacPortSecState = _CadMacPortSecState_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 1, 1, 6),
    _CadMacPortSecState_Type()
)
cadMacPortSecState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMacPortSecState.setStatus("current")
_CadMacPortDplxStatus_Type = DuplexStatus
_CadMacPortDplxStatus_Object = MibTableColumn
cadMacPortDplxStatus = _CadMacPortDplxStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 1, 1, 7),
    _CadMacPortDplxStatus_Type()
)
cadMacPortDplxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMacPortDplxStatus.setStatus("current")
_CadMacPortMacAddress_Type = MacAddress
_CadMacPortMacAddress_Object = MibTableColumn
cadMacPortMacAddress = _CadMacPortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 1, 1, 8),
    _CadMacPortMacAddress_Type()
)
cadMacPortMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMacPortMacAddress.setStatus("current")
_CadMacPortIfIndex_Type = InterfaceIndex
_CadMacPortIfIndex_Object = MibTableColumn
cadMacPortIfIndex = _CadMacPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 1, 1, 9),
    _CadMacPortIfIndex_Type()
)
cadMacPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMacPortIfIndex.setStatus("current")


class _CadMacPortDescription_Type(DisplayString):
    """Custom type cadMacPortDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CadMacPortDescription_Type.__name__ = "DisplayString"
_CadMacPortDescription_Object = MibTableColumn
cadMacPortDescription = _CadMacPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 1, 1, 10),
    _CadMacPortDescription_Type()
)
cadMacPortDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadMacPortDescription.setStatus("current")


class _CadMacPortTrapInh_Type(Bits):
    """Custom type cadMacPortTrapInh based on Bits"""
    defaultHexValue = "e0"

    namedValues = NamedValues(
        *(("duplex", 2),
          ("linkUpLinkDown", 3),
          ("primary", 0),
          ("secondary", 1))
    )

_CadMacPortTrapInh_Type.__name__ = "Bits"
_CadMacPortTrapInh_Object = MibTableColumn
cadMacPortTrapInh = _CadMacPortTrapInh_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 1, 1, 11),
    _CadMacPortTrapInh_Type()
)
cadMacPortTrapInh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadMacPortTrapInh.setStatus("current")
_CadMacPortRowStatus_Type = RowStatus
_CadMacPortRowStatus_Object = MibTableColumn
cadMacPortRowStatus = _CadMacPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 1, 1, 12),
    _CadMacPortRowStatus_Type()
)
cadMacPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadMacPortRowStatus.setStatus("current")


class _CadMacPortOfdm_Type(TruthValue):
    """Custom type cadMacPortOfdm based on TruthValue"""


_CadMacPortOfdm_Object = MibTableColumn
cadMacPortOfdm = _CadMacPortOfdm_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 1, 1, 13),
    _CadMacPortOfdm_Type()
)
cadMacPortOfdm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadMacPortOfdm.setStatus("current")
_CadIfMacDomainTable_Object = MibTable
cadIfMacDomainTable = _CadIfMacDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cadIfMacDomainTable.setStatus("current")
_CadIfMacDomainEntry_Object = MibTableRow
cadIfMacDomainEntry = _CadIfMacDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1)
)
cadIfMacDomainEntry.setIndexNames(
    (0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadIfMacDomainIfIndex"),
)
if mibBuilder.loadTexts:
    cadIfMacDomainEntry.setStatus("current")
_CadIfMacDomainIfIndex_Type = InterfaceIndex
_CadIfMacDomainIfIndex_Object = MibTableColumn
cadIfMacDomainIfIndex = _CadIfMacDomainIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 1),
    _CadIfMacDomainIfIndex_Type()
)
cadIfMacDomainIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIfMacDomainIfIndex.setStatus("current")


class _CadIfMacDomainCapabilities_Type(Bits):
    """Custom type cadIfMacDomainCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("atmCells", 0),
          ("concatentation", 1))
    )

_CadIfMacDomainCapabilities_Type.__name__ = "Bits"
_CadIfMacDomainCapabilities_Object = MibTableColumn
cadIfMacDomainCapabilities = _CadIfMacDomainCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 2),
    _CadIfMacDomainCapabilities_Type()
)
cadIfMacDomainCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfMacDomainCapabilities.setStatus("current")


class _CadIfMacDomainSyncInterval_Type(Integer32):
    """Custom type cadIfMacDomainSyncInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_CadIfMacDomainSyncInterval_Type.__name__ = "Integer32"
_CadIfMacDomainSyncInterval_Object = MibTableColumn
cadIfMacDomainSyncInterval = _CadIfMacDomainSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 3),
    _CadIfMacDomainSyncInterval_Type()
)
cadIfMacDomainSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainSyncInterval.setStatus("current")
if mibBuilder.loadTexts:
    cadIfMacDomainSyncInterval.setUnits("Milliseconds")


class _CadIfMacDomainUcdInterval_Type(Integer32):
    """Custom type cadIfMacDomainUcdInterval based on Integer32"""
    defaultValue = 1600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_CadIfMacDomainUcdInterval_Type.__name__ = "Integer32"
_CadIfMacDomainUcdInterval_Object = MibTableColumn
cadIfMacDomainUcdInterval = _CadIfMacDomainUcdInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 4),
    _CadIfMacDomainUcdInterval_Type()
)
cadIfMacDomainUcdInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainUcdInterval.setStatus("current")
if mibBuilder.loadTexts:
    cadIfMacDomainUcdInterval.setUnits("Milliseconds")


class _CadIfMacDomainMaxServiceIds_Type(Integer32):
    """Custom type cadIfMacDomainMaxServiceIds based on Integer32"""
    defaultValue = 8191

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_CadIfMacDomainMaxServiceIds_Type.__name__ = "Integer32"
_CadIfMacDomainMaxServiceIds_Object = MibTableColumn
cadIfMacDomainMaxServiceIds = _CadIfMacDomainMaxServiceIds_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 5),
    _CadIfMacDomainMaxServiceIds_Type()
)
cadIfMacDomainMaxServiceIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfMacDomainMaxServiceIds.setStatus("current")


class _CadIfMacDomainInvitedRangingAttempts_Type(Integer32):
    """Custom type cadIfMacDomainInvitedRangingAttempts based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_CadIfMacDomainInvitedRangingAttempts_Type.__name__ = "Integer32"
_CadIfMacDomainInvitedRangingAttempts_Object = MibTableColumn
cadIfMacDomainInvitedRangingAttempts = _CadIfMacDomainInvitedRangingAttempts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 6),
    _CadIfMacDomainInvitedRangingAttempts_Type()
)
cadIfMacDomainInvitedRangingAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainInvitedRangingAttempts.setStatus("current")


class _CadIfMacDomainInsertInterval_Type(Integer32):
    """Custom type cadIfMacDomainInsertInterval based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_CadIfMacDomainInsertInterval_Type.__name__ = "Integer32"
_CadIfMacDomainInsertInterval_Object = MibTableColumn
cadIfMacDomainInsertInterval = _CadIfMacDomainInsertInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 7),
    _CadIfMacDomainInsertInterval_Type()
)
cadIfMacDomainInsertInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainInsertInterval.setStatus("current")
if mibBuilder.loadTexts:
    cadIfMacDomainInsertInterval.setUnits("Centiseconds")


class _CadIfMacDomainRangingInterval_Type(TimeInterval):
    """Custom type cadIfMacDomainRangingInterval based on TimeInterval"""
    defaultValue = 2400

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 3500),
    )


_CadIfMacDomainRangingInterval_Type.__name__ = "TimeInterval"
_CadIfMacDomainRangingInterval_Object = MibTableColumn
cadIfMacDomainRangingInterval = _CadIfMacDomainRangingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 8),
    _CadIfMacDomainRangingInterval_Type()
)
cadIfMacDomainRangingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainRangingInterval.setStatus("current")
if mibBuilder.loadTexts:
    cadIfMacDomainRangingInterval.setUnits("Centiseconds")


class _CadIfMacDomainRangeOpportunityCycle_Type(TimeInterval):
    """Custom type cadIfMacDomainRangeOpportunityCycle based on TimeInterval"""
    defaultValue = 120

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 500),
    )


_CadIfMacDomainRangeOpportunityCycle_Type.__name__ = "TimeInterval"
_CadIfMacDomainRangeOpportunityCycle_Object = MibTableColumn
cadIfMacDomainRangeOpportunityCycle = _CadIfMacDomainRangeOpportunityCycle_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 9),
    _CadIfMacDomainRangeOpportunityCycle_Type()
)
cadIfMacDomainRangeOpportunityCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainRangeOpportunityCycle.setStatus("current")
if mibBuilder.loadTexts:
    cadIfMacDomainRangeOpportunityCycle.setUnits("Centiseconds")


class _CadIfMacDomainTftpEnforce_Type(CadTftpEnforceType):
    """Custom type cadIfMacDomainTftpEnforce based on CadTftpEnforceType"""


_CadIfMacDomainTftpEnforce_Object = MibTableColumn
cadIfMacDomainTftpEnforce = _CadIfMacDomainTftpEnforce_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 10),
    _CadIfMacDomainTftpEnforce_Type()
)
cadIfMacDomainTftpEnforce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainTftpEnforce.setStatus("current")


class _CadIfMacDomainDynamicSecret_Type(CadDynamicSecretType):
    """Custom type cadIfMacDomainDynamicSecret based on CadDynamicSecretType"""


_CadIfMacDomainDynamicSecret_Object = MibTableColumn
cadIfMacDomainDynamicSecret = _CadIfMacDomainDynamicSecret_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 11),
    _CadIfMacDomainDynamicSecret_Type()
)
cadIfMacDomainDynamicSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainDynamicSecret.setStatus("current")


class _CadIfMacDomainAnnex_Type(Integer32):
    """Custom type cadIfMacDomainAnnex based on Integer32"""
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
        *(("annexA", 3),
          ("annexB", 4),
          ("annexC", 5),
          ("other", 2),
          ("unknown", 1))
    )


_CadIfMacDomainAnnex_Type.__name__ = "Integer32"
_CadIfMacDomainAnnex_Object = MibTableColumn
cadIfMacDomainAnnex = _CadIfMacDomainAnnex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 13),
    _CadIfMacDomainAnnex_Type()
)
cadIfMacDomainAnnex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainAnnex.setStatus("current")


class _CadIfMacDomainMddInterval_Type(Unsigned32):
    """Custom type cadIfMacDomainMddInterval based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_CadIfMacDomainMddInterval_Type.__name__ = "Unsigned32"
_CadIfMacDomainMddInterval_Object = MibTableColumn
cadIfMacDomainMddInterval = _CadIfMacDomainMddInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 14),
    _CadIfMacDomainMddInterval_Type()
)
cadIfMacDomainMddInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainMddInterval.setStatus("current")
if mibBuilder.loadTexts:
    cadIfMacDomainMddInterval.setUnits("milliseconds")


class _CadIfMacDomainIpProvMode_Type(Integer32):
    """Custom type cadIfMacDomainIpProvMode based on Integer32"""
    defaultValue = 1

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
        *(("alternate", 2),
          ("dualStack", 3),
          ("ipv4Only", 0),
          ("ipv6Only", 1))
    )


_CadIfMacDomainIpProvMode_Type.__name__ = "Integer32"
_CadIfMacDomainIpProvMode_Object = MibTableColumn
cadIfMacDomainIpProvMode = _CadIfMacDomainIpProvMode_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 16),
    _CadIfMacDomainIpProvMode_Type()
)
cadIfMacDomainIpProvMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainIpProvMode.setStatus("current")


class _CadIfMacDomainCmStatusEvCtlEnabled_Type(TruthValue):
    """Custom type cadIfMacDomainCmStatusEvCtlEnabled based on TruthValue"""


_CadIfMacDomainCmStatusEvCtlEnabled_Object = MibTableColumn
cadIfMacDomainCmStatusEvCtlEnabled = _CadIfMacDomainCmStatusEvCtlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 18),
    _CadIfMacDomainCmStatusEvCtlEnabled_Type()
)
cadIfMacDomainCmStatusEvCtlEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainCmStatusEvCtlEnabled.setStatus("current")


class _CadIfMacDomainUsFreqRange_Type(Integer32):
    """Custom type cadIfMacDomainUsFreqRange based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("extended", 1),
          ("standard", 0))
    )


_CadIfMacDomainUsFreqRange_Type.__name__ = "Integer32"
_CadIfMacDomainUsFreqRange_Object = MibTableColumn
cadIfMacDomainUsFreqRange = _CadIfMacDomainUsFreqRange_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 19),
    _CadIfMacDomainUsFreqRange_Type()
)
cadIfMacDomainUsFreqRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainUsFreqRange.setStatus("current")


class _CadIfMacDomainMcastDsidFwdEnabled_Type(TruthValue):
    """Custom type cadIfMacDomainMcastDsidFwdEnabled based on TruthValue"""


_CadIfMacDomainMcastDsidFwdEnabled_Object = MibTableColumn
cadIfMacDomainMcastDsidFwdEnabled = _CadIfMacDomainMcastDsidFwdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 20),
    _CadIfMacDomainMcastDsidFwdEnabled_Type()
)
cadIfMacDomainMcastDsidFwdEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainMcastDsidFwdEnabled.setStatus("current")


class _CadIfMacDomainDsBondingEnabled_Type(TruthValue):
    """Custom type cadIfMacDomainDsBondingEnabled based on TruthValue"""


_CadIfMacDomainDsBondingEnabled_Object = MibTableColumn
cadIfMacDomainDsBondingEnabled = _CadIfMacDomainDsBondingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 21),
    _CadIfMacDomainDsBondingEnabled_Type()
)
cadIfMacDomainDsBondingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainDsBondingEnabled.setStatus("current")


class _CadIfMacDomainMultTxChModeEnabled_Type(TruthValue):
    """Custom type cadIfMacDomainMultTxChModeEnabled based on TruthValue"""


_CadIfMacDomainMultTxChModeEnabled_Object = MibTableColumn
cadIfMacDomainMultTxChModeEnabled = _CadIfMacDomainMultTxChModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 22),
    _CadIfMacDomainMultTxChModeEnabled_Type()
)
cadIfMacDomainMultTxChModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainMultTxChModeEnabled.setStatus("current")


class _CadIfMacDomainEarlyAuthEncrCtrl_Type(Integer32):
    """Custom type cadIfMacDomainEarlyAuthEncrCtrl based on Integer32"""
    defaultValue = 2

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
        *(("disableEae", 1),
          ("enableEaeCapabilityBasedEnforcement", 3),
          ("enableEaeRangingBasedEnforcement", 2),
          ("enableEaeTotalEnforcement", 4))
    )


_CadIfMacDomainEarlyAuthEncrCtrl_Type.__name__ = "Integer32"
_CadIfMacDomainEarlyAuthEncrCtrl_Object = MibTableColumn
cadIfMacDomainEarlyAuthEncrCtrl = _CadIfMacDomainEarlyAuthEncrCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 23),
    _CadIfMacDomainEarlyAuthEncrCtrl_Type()
)
cadIfMacDomainEarlyAuthEncrCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainEarlyAuthEncrCtrl.setStatus("current")


class _CadIfMacDomainTftpProxyEnabled_Type(TruthValue):
    """Custom type cadIfMacDomainTftpProxyEnabled based on TruthValue"""


_CadIfMacDomainTftpProxyEnabled_Object = MibTableColumn
cadIfMacDomainTftpProxyEnabled = _CadIfMacDomainTftpProxyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 24),
    _CadIfMacDomainTftpProxyEnabled_Type()
)
cadIfMacDomainTftpProxyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainTftpProxyEnabled.setStatus("current")


class _CadIfMacDomainSrcAddrVerifEnabled_Type(TruthValue):
    """Custom type cadIfMacDomainSrcAddrVerifEnabled based on TruthValue"""


_CadIfMacDomainSrcAddrVerifEnabled_Object = MibTableColumn
cadIfMacDomainSrcAddrVerifEnabled = _CadIfMacDomainSrcAddrVerifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 25),
    _CadIfMacDomainSrcAddrVerifEnabled_Type()
)
cadIfMacDomainSrcAddrVerifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainSrcAddrVerifEnabled.setStatus("current")


class _CadIfMacDomainMulticastEncryption_Type(TruthValue):
    """Custom type cadIfMacDomainMulticastEncryption based on TruthValue"""


_CadIfMacDomainMulticastEncryption_Object = MibTableColumn
cadIfMacDomainMulticastEncryption = _CadIfMacDomainMulticastEncryption_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 26),
    _CadIfMacDomainMulticastEncryption_Type()
)
cadIfMacDomainMulticastEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfMacDomainMulticastEncryption.setStatus("current")


class _CadIfMacDomainRcpReportMode_Type(Integer32):
    """Custom type cadIfMacDomainRcpReportMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nonVerbose", 0),
          ("verbose", 1))
    )


_CadIfMacDomainRcpReportMode_Type.__name__ = "Integer32"
_CadIfMacDomainRcpReportMode_Object = MibTableColumn
cadIfMacDomainRcpReportMode = _CadIfMacDomainRcpReportMode_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 27),
    _CadIfMacDomainRcpReportMode_Type()
)
cadIfMacDomainRcpReportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainRcpReportMode.setStatus("current")


class _CadIfMacDomainRegRspToOverride_Type(Unsigned32):
    """Custom type cadIfMacDomainRegRspToOverride based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CadIfMacDomainRegRspToOverride_Type.__name__ = "Unsigned32"
_CadIfMacDomainRegRspToOverride_Object = MibTableColumn
cadIfMacDomainRegRspToOverride = _CadIfMacDomainRegRspToOverride_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 28),
    _CadIfMacDomainRegRspToOverride_Type()
)
cadIfMacDomainRegRspToOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainRegRspToOverride.setStatus("current")
if mibBuilder.loadTexts:
    cadIfMacDomainRegRspToOverride.setUnits("seconds")


class _CadIfMacDomainMultRxChModeEnabled_Type(TruthValue):
    """Custom type cadIfMacDomainMultRxChModeEnabled based on TruthValue"""


_CadIfMacDomainMultRxChModeEnabled_Object = MibTableColumn
cadIfMacDomainMultRxChModeEnabled = _CadIfMacDomainMultRxChModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 29),
    _CadIfMacDomainMultRxChModeEnabled_Type()
)
cadIfMacDomainMultRxChModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainMultRxChModeEnabled.setStatus("current")


class _CadIfMacDomainCmUdcEnabled_Type(TruthValue):
    """Custom type cadIfMacDomainCmUdcEnabled based on TruthValue"""


_CadIfMacDomainCmUdcEnabled_Object = MibTableColumn
cadIfMacDomainCmUdcEnabled = _CadIfMacDomainCmUdcEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 30),
    _CadIfMacDomainCmUdcEnabled_Type()
)
cadIfMacDomainCmUdcEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainCmUdcEnabled.setStatus("current")


class _CadIfMacDomainSendUdcRulesEnabled_Type(TruthValue):
    """Custom type cadIfMacDomainSendUdcRulesEnabled based on TruthValue"""


_CadIfMacDomainSendUdcRulesEnabled_Object = MibTableColumn
cadIfMacDomainSendUdcRulesEnabled = _CadIfMacDomainSendUdcRulesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 31),
    _CadIfMacDomainSendUdcRulesEnabled_Type()
)
cadIfMacDomainSendUdcRulesEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainSendUdcRulesEnabled.setStatus("current")


class _CadIfMacDomainRccDynEnable_Type(TruthValue):
    """Custom type cadIfMacDomainRccDynEnable based on TruthValue"""


_CadIfMacDomainRccDynEnable_Object = MibTableColumn
cadIfMacDomainRccDynEnable = _CadIfMacDomainRccDynEnable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 32),
    _CadIfMacDomainRccDynEnable_Type()
)
cadIfMacDomainRccDynEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainRccDynEnable.setStatus("current")


class _CadIfMacDomainDsbgDynEnable_Type(TruthValue):
    """Custom type cadIfMacDomainDsbgDynEnable based on TruthValue"""


_CadIfMacDomainDsbgDynEnable_Object = MibTableColumn
cadIfMacDomainDsbgDynEnable = _CadIfMacDomainDsbgDynEnable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 33),
    _CadIfMacDomainDsbgDynEnable_Type()
)
cadIfMacDomainDsbgDynEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainDsbgDynEnable.setStatus("current")


class _CadIfMacDomainDsbgReseqWaitTime_Type(Unsigned32):
    """Custom type cadIfMacDomainDsbgReseqWaitTime based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
        ValueRangeConstraint(255, 255),
    )


_CadIfMacDomainDsbgReseqWaitTime_Type.__name__ = "Unsigned32"
_CadIfMacDomainDsbgReseqWaitTime_Object = MibTableColumn
cadIfMacDomainDsbgReseqWaitTime = _CadIfMacDomainDsbgReseqWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 34),
    _CadIfMacDomainDsbgReseqWaitTime_Type()
)
cadIfMacDomainDsbgReseqWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainDsbgReseqWaitTime.setStatus("current")
if mibBuilder.loadTexts:
    cadIfMacDomainDsbgReseqWaitTime.setUnits("hundredMicroseconds")


class _CadIfMacDomainDsbgReseqWarnThrshld_Type(Unsigned32):
    """Custom type cadIfMacDomainDsbgReseqWarnThrshld based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 179),
        ValueRangeConstraint(255, 255),
    )


_CadIfMacDomainDsbgReseqWarnThrshld_Type.__name__ = "Unsigned32"
_CadIfMacDomainDsbgReseqWarnThrshld_Object = MibTableColumn
cadIfMacDomainDsbgReseqWarnThrshld = _CadIfMacDomainDsbgReseqWarnThrshld_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 35),
    _CadIfMacDomainDsbgReseqWarnThrshld_Type()
)
cadIfMacDomainDsbgReseqWarnThrshld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainDsbgReseqWarnThrshld.setStatus("current")
if mibBuilder.loadTexts:
    cadIfMacDomainDsbgReseqWarnThrshld.setUnits("hundredMicroseconds")


class _CadIfMacDomainDpId_Type(Integer32):
    """Custom type cadIfMacDomainDpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(255, 255),
    )


_CadIfMacDomainDpId_Type.__name__ = "Integer32"
_CadIfMacDomainDpId_Object = MibTableColumn
cadIfMacDomainDpId = _CadIfMacDomainDpId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 36),
    _CadIfMacDomainDpId_Type()
)
cadIfMacDomainDpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfMacDomainDpId.setStatus("current")


class _CadIfMacDomainUsbgDynEnable_Type(TruthValue):
    """Custom type cadIfMacDomainUsbgDynEnable based on TruthValue"""


_CadIfMacDomainUsbgDynEnable_Object = MibTableColumn
cadIfMacDomainUsbgDynEnable = _CadIfMacDomainUsbgDynEnable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 37),
    _CadIfMacDomainUsbgDynEnable_Type()
)
cadIfMacDomainUsbgDynEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainUsbgDynEnable.setStatus("current")


class _CadIfMacDomainDownChannelMaxFrequency_Type(Integer32):
    """Custom type cadIfMacDomainDownChannelMaxFrequency based on Integer32"""
    defaultValue = 867000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(858000000, 858000000),
        ValueRangeConstraint(867000000, 867000000),
        ValueRangeConstraint(999000000, 999000000),
    )


_CadIfMacDomainDownChannelMaxFrequency_Type.__name__ = "Integer32"
_CadIfMacDomainDownChannelMaxFrequency_Object = MibTableColumn
cadIfMacDomainDownChannelMaxFrequency = _CadIfMacDomainDownChannelMaxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 38),
    _CadIfMacDomainDownChannelMaxFrequency_Type()
)
cadIfMacDomainDownChannelMaxFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainDownChannelMaxFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cadIfMacDomainDownChannelMaxFrequency.setUnits("hertz")


class _CadIfMacDomainDownChannelMinFrequency_Type(Integer32):
    """Custom type cadIfMacDomainDownChannelMinFrequency based on Integer32"""
    defaultValue = 91000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(57000000, 57000000),
        ValueRangeConstraint(85000000, 85000000),
        ValueRangeConstraint(91000000, 91000000),
        ValueRangeConstraint(112000000, 112000000),
    )


_CadIfMacDomainDownChannelMinFrequency_Type.__name__ = "Integer32"
_CadIfMacDomainDownChannelMinFrequency_Object = MibTableColumn
cadIfMacDomainDownChannelMinFrequency = _CadIfMacDomainDownChannelMinFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 39),
    _CadIfMacDomainDownChannelMinFrequency_Type()
)
cadIfMacDomainDownChannelMinFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainDownChannelMinFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cadIfMacDomainDownChannelMinFrequency.setUnits("hertz")


class _CadIfMacDomainUpChannelMaxFrequency_Type(Integer32):
    """Custom type cadIfMacDomainUpChannelMaxFrequency based on Integer32"""
    defaultValue = 42000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(42000000, 42000000),
        ValueRangeConstraint(55000000, 55000000),
        ValueRangeConstraint(65000000, 65000000),
        ValueRangeConstraint(85000000, 85000000),
    )


_CadIfMacDomainUpChannelMaxFrequency_Type.__name__ = "Integer32"
_CadIfMacDomainUpChannelMaxFrequency_Object = MibTableColumn
cadIfMacDomainUpChannelMaxFrequency = _CadIfMacDomainUpChannelMaxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 40),
    _CadIfMacDomainUpChannelMaxFrequency_Type()
)
cadIfMacDomainUpChannelMaxFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainUpChannelMaxFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cadIfMacDomainUpChannelMaxFrequency.setUnits("hertz")


class _CadIfMacDomainBpi2Mandatory_Type(Integer32):
    """Custom type cadIfMacDomainBpi2Mandatory based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bpi", 1),
          ("bpiPlus", 2),
          ("none", 0))
    )


_CadIfMacDomainBpi2Mandatory_Type.__name__ = "Integer32"
_CadIfMacDomainBpi2Mandatory_Object = MibTableColumn
cadIfMacDomainBpi2Mandatory = _CadIfMacDomainBpi2Mandatory_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 41),
    _CadIfMacDomainBpi2Mandatory_Type()
)
cadIfMacDomainBpi2Mandatory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainBpi2Mandatory.setStatus("current")


class _CadIfMacDomainDSG30Enabled_Type(TruthValue):
    """Custom type cadIfMacDomainDSG30Enabled based on TruthValue"""


_CadIfMacDomainDSG30Enabled_Object = MibTableColumn
cadIfMacDomainDSG30Enabled = _CadIfMacDomainDSG30Enabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 43),
    _CadIfMacDomainDSG30Enabled_Type()
)
cadIfMacDomainDSG30Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainDSG30Enabled.setStatus("current")


class _CadIfMacDomainEnforceRulesEnabled_Type(TruthValue):
    """Custom type cadIfMacDomainEnforceRulesEnabled based on TruthValue"""


_CadIfMacDomainEnforceRulesEnabled_Object = MibTableColumn
cadIfMacDomainEnforceRulesEnabled = _CadIfMacDomainEnforceRulesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 44),
    _CadIfMacDomainEnforceRulesEnabled_Type()
)
cadIfMacDomainEnforceRulesEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainEnforceRulesEnabled.setStatus("current")


class _CadIfMacDomainCmTxPwrExtentionPreRegistrationEnabled_Type(TruthValue):
    """Custom type cadIfMacDomainCmTxPwrExtentionPreRegistrationEnabled based on TruthValue"""


_CadIfMacDomainCmTxPwrExtentionPreRegistrationEnabled_Object = MibTableColumn
cadIfMacDomainCmTxPwrExtentionPreRegistrationEnabled = _CadIfMacDomainCmTxPwrExtentionPreRegistrationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 45),
    _CadIfMacDomainCmTxPwrExtentionPreRegistrationEnabled_Type()
)
cadIfMacDomainCmTxPwrExtentionPreRegistrationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainCmTxPwrExtentionPreRegistrationEnabled.setStatus("current")


class _CadIfMacDomainCmTxPwrExtentionPostRegistrationEnabled_Type(TruthValue):
    """Custom type cadIfMacDomainCmTxPwrExtentionPostRegistrationEnabled based on TruthValue"""


_CadIfMacDomainCmTxPwrExtentionPostRegistrationEnabled_Object = MibTableColumn
cadIfMacDomainCmTxPwrExtentionPostRegistrationEnabled = _CadIfMacDomainCmTxPwrExtentionPostRegistrationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 46),
    _CadIfMacDomainCmTxPwrExtentionPostRegistrationEnabled_Type()
)
cadIfMacDomainCmTxPwrExtentionPostRegistrationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainCmTxPwrExtentionPostRegistrationEnabled.setStatus("current")


class _CadIfMacDomainT4TimeoutMultiplierEnabled_Type(TruthValue):
    """Custom type cadIfMacDomainT4TimeoutMultiplierEnabled based on TruthValue"""


_CadIfMacDomainT4TimeoutMultiplierEnabled_Object = MibTableColumn
cadIfMacDomainT4TimeoutMultiplierEnabled = _CadIfMacDomainT4TimeoutMultiplierEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 47),
    _CadIfMacDomainT4TimeoutMultiplierEnabled_Type()
)
cadIfMacDomainT4TimeoutMultiplierEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainT4TimeoutMultiplierEnabled.setStatus("current")


class _CadIfMacDomainDynamicRccMultiTunerEnabled_Type(TruthValue):
    """Custom type cadIfMacDomainDynamicRccMultiTunerEnabled based on TruthValue"""


_CadIfMacDomainDynamicRccMultiTunerEnabled_Object = MibTableColumn
cadIfMacDomainDynamicRccMultiTunerEnabled = _CadIfMacDomainDynamicRccMultiTunerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 48),
    _CadIfMacDomainDynamicRccMultiTunerEnabled_Type()
)
cadIfMacDomainDynamicRccMultiTunerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainDynamicRccMultiTunerEnabled.setStatus("current")


class _CadIfMacDomainTcsSizeLimit_Type(Integer32):
    """Custom type cadIfMacDomainTcsSizeLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_CadIfMacDomainTcsSizeLimit_Type.__name__ = "Integer32"
_CadIfMacDomainTcsSizeLimit_Object = MibTableColumn
cadIfMacDomainTcsSizeLimit = _CadIfMacDomainTcsSizeLimit_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 49),
    _CadIfMacDomainTcsSizeLimit_Type()
)
cadIfMacDomainTcsSizeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainTcsSizeLimit.setStatus("current")


class _CadIfMacDomainDocsis31Enabled_Type(TruthValue):
    """Custom type cadIfMacDomainDocsis31Enabled based on TruthValue"""


_CadIfMacDomainDocsis31Enabled_Object = MibTableColumn
cadIfMacDomainDocsis31Enabled = _CadIfMacDomainDocsis31Enabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 50),
    _CadIfMacDomainDocsis31Enabled_Type()
)
cadIfMacDomainDocsis31Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainDocsis31Enabled.setStatus("current")


class _CadIfMacDomainEnergyMgt1x1Enabled_Type(TruthValue):
    """Custom type cadIfMacDomainEnergyMgt1x1Enabled based on TruthValue"""


_CadIfMacDomainEnergyMgt1x1Enabled_Object = MibTableColumn
cadIfMacDomainEnergyMgt1x1Enabled = _CadIfMacDomainEnergyMgt1x1Enabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 51),
    _CadIfMacDomainEnergyMgt1x1Enabled_Type()
)
cadIfMacDomainEnergyMgt1x1Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainEnergyMgt1x1Enabled.setStatus("current")


class _CadIfMacDomainDsOfdmProfileRecoveryGuardTime_Type(Integer32):
    """Custom type cadIfMacDomainDsOfdmProfileRecoveryGuardTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_CadIfMacDomainDsOfdmProfileRecoveryGuardTime_Type.__name__ = "Integer32"
_CadIfMacDomainDsOfdmProfileRecoveryGuardTime_Object = MibTableColumn
cadIfMacDomainDsOfdmProfileRecoveryGuardTime = _CadIfMacDomainDsOfdmProfileRecoveryGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 52),
    _CadIfMacDomainDsOfdmProfileRecoveryGuardTime_Type()
)
cadIfMacDomainDsOfdmProfileRecoveryGuardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainDsOfdmProfileRecoveryGuardTime.setStatus("current")
if mibBuilder.loadTexts:
    cadIfMacDomainDsOfdmProfileRecoveryGuardTime.setUnits("seconds")


class _CadIfMacDomainGracefulTcsReductionEnabled_Type(TruthValue):
    """Custom type cadIfMacDomainGracefulTcsReductionEnabled based on TruthValue"""


_CadIfMacDomainGracefulTcsReductionEnabled_Object = MibTableColumn
cadIfMacDomainGracefulTcsReductionEnabled = _CadIfMacDomainGracefulTcsReductionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 2, 1, 53),
    _CadIfMacDomainGracefulTcsReductionEnabled_Type()
)
cadIfMacDomainGracefulTcsReductionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfMacDomainGracefulTcsReductionEnabled.setStatus("current")
_CadMacChlTable_Object = MibTable
cadMacChlTable = _CadMacChlTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cadMacChlTable.setStatus("current")
_CadMacChlEntry_Object = MibTableRow
cadMacChlEntry = _CadMacChlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 3, 1)
)
cadMacChlEntry.setIndexNames(
    (0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadMacChlMacDomainIfIndex"),
    (0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadMacChlChannelIfIndex"),
)
if mibBuilder.loadTexts:
    cadMacChlEntry.setStatus("current")
_CadMacChlMacDomainIfIndex_Type = InterfaceIndex
_CadMacChlMacDomainIfIndex_Object = MibTableColumn
cadMacChlMacDomainIfIndex = _CadMacChlMacDomainIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 3, 1, 1),
    _CadMacChlMacDomainIfIndex_Type()
)
cadMacChlMacDomainIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadMacChlMacDomainIfIndex.setStatus("current")
_CadMacChlChannelIfIndex_Type = InterfaceIndex
_CadMacChlChannelIfIndex_Object = MibTableColumn
cadMacChlChannelIfIndex = _CadMacChlChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 3, 1, 2),
    _CadMacChlChannelIfIndex_Type()
)
cadMacChlChannelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadMacChlChannelIfIndex.setStatus("current")
_CadMacChlCardNumber_Type = CardId
_CadMacChlCardNumber_Object = MibTableColumn
cadMacChlCardNumber = _CadMacChlCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 3, 1, 3),
    _CadMacChlCardNumber_Type()
)
cadMacChlCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMacChlCardNumber.setStatus("current")
_CadMacChlPortId_Type = PortId
_CadMacChlPortId_Object = MibTableColumn
cadMacChlPortId = _CadMacChlPortId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 3, 1, 4),
    _CadMacChlPortId_Type()
)
cadMacChlPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMacChlPortId.setStatus("current")
_CadMacChlPortType_Type = PortType
_CadMacChlPortType_Object = MibTableColumn
cadMacChlPortType = _CadMacChlPortType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 3, 1, 5),
    _CadMacChlPortType_Type()
)
cadMacChlPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMacChlPortType.setStatus("current")
_CadMacChlCardSubType_Type = CerCardSubType
_CadMacChlCardSubType_Object = MibTableColumn
cadMacChlCardSubType = _CadMacChlCardSubType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 3, 1, 6),
    _CadMacChlCardSubType_Type()
)
cadMacChlCardSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMacChlCardSubType.setStatus("current")


class _CadMacChlChannelId_Type(Integer32):
    """Custom type cadMacChlChannelId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CadMacChlChannelId_Type.__name__ = "Integer32"
_CadMacChlChannelId_Object = MibTableColumn
cadMacChlChannelId = _CadMacChlChannelId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 3, 1, 7),
    _CadMacChlChannelId_Type()
)
cadMacChlChannelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadMacChlChannelId.setStatus("current")
_CadMacChlRowStatus_Type = RowStatus
_CadMacChlRowStatus_Object = MibTableColumn
cadMacChlRowStatus = _CadMacChlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 3, 1, 8),
    _CadMacChlRowStatus_Type()
)
cadMacChlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadMacChlRowStatus.setStatus("current")


class _CadMacChlIsPriCapableDs_Type(TruthValue):
    """Custom type cadMacChlIsPriCapableDs based on TruthValue"""


_CadMacChlIsPriCapableDs_Object = MibTableColumn
cadMacChlIsPriCapableDs = _CadMacChlIsPriCapableDs_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 3, 1, 9),
    _CadMacChlIsPriCapableDs_Type()
)
cadMacChlIsPriCapableDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadMacChlIsPriCapableDs.setStatus("current")


class _CadMacChlSfProvAttrMask_Type(AttributeMask):
    """Custom type cadMacChlSfProvAttrMask based on AttributeMask"""
    defaultHexValue = "00000000"


_CadMacChlSfProvAttrMask_Object = MibTableColumn
cadMacChlSfProvAttrMask = _CadMacChlSfProvAttrMask_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 3, 1, 10),
    _CadMacChlSfProvAttrMask_Type()
)
cadMacChlSfProvAttrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadMacChlSfProvAttrMask.setStatus("current")
_CadMacChlDirection_Type = IfDirection
_CadMacChlDirection_Object = MibTableColumn
cadMacChlDirection = _CadMacChlDirection_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 3, 1, 11),
    _CadMacChlDirection_Type()
)
cadMacChlDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadMacChlDirection.setStatus("current")
_CadUpSupervisionCfgTable_Object = MibTable
cadUpSupervisionCfgTable = _CadUpSupervisionCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 4)
)
if mibBuilder.loadTexts:
    cadUpSupervisionCfgTable.setStatus("current")
_CadUpSupervisionCfgEntry_Object = MibTableRow
cadUpSupervisionCfgEntry = _CadUpSupervisionCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 4, 1)
)
cadUpSupervisionCfgEntry.setIndexNames(
    (0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadMacChlMacDomainIfIndex"),
    (0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadUpSupervisionCfgUpChannelIfIndex"),
    (0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadUpSupervisionCfgDownChannelIfIndex"),
)
if mibBuilder.loadTexts:
    cadUpSupervisionCfgEntry.setStatus("current")
_CadUpSupervisionCfgUpChannelIfIndex_Type = InterfaceIndex
_CadUpSupervisionCfgUpChannelIfIndex_Object = MibTableColumn
cadUpSupervisionCfgUpChannelIfIndex = _CadUpSupervisionCfgUpChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 4, 1, 1),
    _CadUpSupervisionCfgUpChannelIfIndex_Type()
)
cadUpSupervisionCfgUpChannelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadUpSupervisionCfgUpChannelIfIndex.setStatus("current")
_CadUpSupervisionCfgDownChannelIfIndex_Type = InterfaceIndex
_CadUpSupervisionCfgDownChannelIfIndex_Object = MibTableColumn
cadUpSupervisionCfgDownChannelIfIndex = _CadUpSupervisionCfgDownChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 4, 1, 2),
    _CadUpSupervisionCfgDownChannelIfIndex_Type()
)
cadUpSupervisionCfgDownChannelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadUpSupervisionCfgDownChannelIfIndex.setStatus("current")


class _CadUpSupervisionCfgAssign_Type(TruthValue):
    """Custom type cadUpSupervisionCfgAssign based on TruthValue"""


_CadUpSupervisionCfgAssign_Object = MibTableColumn
cadUpSupervisionCfgAssign = _CadUpSupervisionCfgAssign_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 4, 1, 3),
    _CadUpSupervisionCfgAssign_Type()
)
cadUpSupervisionCfgAssign.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadUpSupervisionCfgAssign.setStatus("current")
_CadUpSupervisionCfgRowStatus_Type = RowStatus
_CadUpSupervisionCfgRowStatus_Object = MibTableColumn
cadUpSupervisionCfgRowStatus = _CadUpSupervisionCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 4, 1, 4),
    _CadUpSupervisionCfgRowStatus_Type()
)
cadUpSupervisionCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadUpSupervisionCfgRowStatus.setStatus("current")
_CadUpSupervisionStatusTable_Object = MibTable
cadUpSupervisionStatusTable = _CadUpSupervisionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 5)
)
if mibBuilder.loadTexts:
    cadUpSupervisionStatusTable.setStatus("current")
_CadUpSupervisionStatusEntry_Object = MibTableRow
cadUpSupervisionStatusEntry = _CadUpSupervisionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 5, 1)
)
cadUpSupervisionStatusEntry.setIndexNames(
    (0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadMacChlMacDomainIfIndex"),
    (0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadUpSupervisionStatusUpChannelIfIndex"),
    (0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadUpSupervisionStatusDownChannelIfIndex"),
)
if mibBuilder.loadTexts:
    cadUpSupervisionStatusEntry.setStatus("current")
_CadUpSupervisionStatusUpChannelIfIndex_Type = InterfaceIndex
_CadUpSupervisionStatusUpChannelIfIndex_Object = MibTableColumn
cadUpSupervisionStatusUpChannelIfIndex = _CadUpSupervisionStatusUpChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 5, 1, 1),
    _CadUpSupervisionStatusUpChannelIfIndex_Type()
)
cadUpSupervisionStatusUpChannelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadUpSupervisionStatusUpChannelIfIndex.setStatus("current")
_CadUpSupervisionStatusDownChannelIfIndex_Type = InterfaceIndex
_CadUpSupervisionStatusDownChannelIfIndex_Object = MibTableColumn
cadUpSupervisionStatusDownChannelIfIndex = _CadUpSupervisionStatusDownChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 5, 1, 2),
    _CadUpSupervisionStatusDownChannelIfIndex_Type()
)
cadUpSupervisionStatusDownChannelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadUpSupervisionStatusDownChannelIfIndex.setStatus("current")


class _CadUpSupervisionStatusAssignmentMethod_Type(Integer32):
    """Custom type cadUpSupervisionStatusAssignmentMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("provisioned", 2))
    )


_CadUpSupervisionStatusAssignmentMethod_Type.__name__ = "Integer32"
_CadUpSupervisionStatusAssignmentMethod_Object = MibTableColumn
cadUpSupervisionStatusAssignmentMethod = _CadUpSupervisionStatusAssignmentMethod_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 4, 5, 1, 3),
    _CadUpSupervisionStatusAssignmentMethod_Type()
)
cadUpSupervisionStatusAssignmentMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadUpSupervisionStatusAssignmentMethod.setStatus("current")
_ArrisCerIpGroup_ObjectIdentity = ObjectIdentity
arrisCerIpGroup = _ArrisCerIpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 5)
)


class _CerIpGratuitousArpPeriod_Type(Unsigned32):
    """Custom type cerIpGratuitousArpPeriod based on Unsigned32"""
    defaultValue = 60


_CerIpGratuitousArpPeriod_Object = MibScalar
cerIpGratuitousArpPeriod = _CerIpGratuitousArpPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 5, 1),
    _CerIpGratuitousArpPeriod_Type()
)
cerIpGratuitousArpPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerIpGratuitousArpPeriod.setStatus("current")
cadBridgeGroupEntry.registerAugmentions(
    ("CADANT-CMTS-LAYER2CMTS-MIB",
     "cadBridgeGroupStatsEntry")
)
cadBridgeGroupStatsEntry.setIndexNames(*cadBridgeGroupEntry.getIndexNames())

# Managed Objects groups

cadAgingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 3, 1)
)
cadAgingGroup.setObjects(
      *(("CADANT-CMTS-LAYER2CMTS-MIB", "cadAgingCPEAgingInterval"),
        ("CADANT-CMTS-LAYER2CMTS-MIB", "cadAgingSFAgingInterval"),
        ("CADANT-CMTS-LAYER2CMTS-MIB", "cadAgingStaleMACAgingInterval"),
        ("CADANT-CMTS-LAYER2CMTS-MIB", "cadAgingArpCacheAgingInterval"),
        ("CADANT-CMTS-LAYER2CMTS-MIB", "cadAgingNDCacheAgingInterval"),
        ("CADANT-CMTS-LAYER2CMTS-MIB", "cadAgingNDCacheSearchingRateLimit"),
        ("CADANT-CMTS-LAYER2CMTS-MIB", "cadAgingNDCacheSearchingMaxNumber"),
        ("CADANT-CMTS-LAYER2CMTS-MIB", "cadAgingNDCacheNotPresentRateLimit"),
        ("CADANT-CMTS-LAYER2CMTS-MIB", "cadAgingNDCacheNotPresentMaxNumber"),
        ("CADANT-CMTS-LAYER2CMTS-MIB", "cadAgingNDCacheNotPresentMaxTime"),
        ("CADANT-CMTS-LAYER2CMTS-MIB", "cadAgingNDCacheNotPresentMinTime"),
        ("CADANT-CMTS-LAYER2CMTS-MIB", "cadAgingNDCacheSearchingGlobalMaxRate"),
        ("CADANT-CMTS-LAYER2CMTS-MIB", "cadAgingNDCacheNotPresentGlobalMaxRate"))
)
if mibBuilder.loadTexts:
    cadAgingGroup.setStatus("current")

cerIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 20, 1, 3, 2)
)
cerIpGroup.setObjects(
    ("CADANT-CMTS-LAYER2CMTS-MIB", "cerIpGratuitousArpPeriod")
)
if mibBuilder.loadTexts:
    cerIpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-CMTS-LAYER2CMTS-MIB",
    **{"CadTftpEnforceType": CadTftpEnforceType,
       "CadDynamicSecretType": CadDynamicSecretType,
       "cadLayer2Mib": cadLayer2Mib,
       "cadBridgeGroup": cadBridgeGroup,
       "cadBridgeGroupGeneral": cadBridgeGroupGeneral,
       "cadBridgeGroupMaxNum": cadBridgeGroupMaxNum,
       "cadBridgeGroupTable": cadBridgeGroupTable,
       "cadBridgeGroupEntry": cadBridgeGroupEntry,
       "cadBgIndex": cadBgIndex,
       "cadBgName": cadBgName,
       "cadBgRowStatus": cadBgRowStatus,
       "cadBridgeGroupStatsTable": cadBridgeGroupStatsTable,
       "cadBridgeGroupStatsEntry": cadBridgeGroupStatsEntry,
       "cadBgLeaderBgpId": cadBgLeaderBgpId,
       "cadBgMacAddress": cadBgMacAddress,
       "cadBridgePortTable": cadBridgePortTable,
       "cadBridgePortEntry": cadBridgePortEntry,
       "cadBgpGroupId": cadBgpGroupId,
       "cadBgpId": cadBgpId,
       "cadBgpCardId": cadBgpCardId,
       "cadBgpCardType": cadBgpCardType,
       "cadBgpPortId": cadBgpPortId,
       "cadBgpType": cadBgpType,
       "cadBgpBundleGroupId": cadBgpBundleGroupId,
       "cadBgpMacAddress": cadBgpMacAddress,
       "cadBridgeGroupPortStatusTable": cadBridgeGroupPortStatusTable,
       "cadBridgeGroupPortStatusEntry": cadBridgeGroupPortStatusEntry,
       "cadBgpStatGroupId": cadBgpStatGroupId,
       "cadBgpStatMacIfIndex": cadBgpStatMacIfIndex,
       "cadBgpStatPhyIfIndex": cadBgpStatPhyIfIndex,
       "cadBgpStatPhyCardId": cadBgpStatPhyCardId,
       "cadBgpStatPhyPortId": cadBgpStatPhyPortId,
       "cadDot3adAggTable": cadDot3adAggTable,
       "cadDot3adAggEntry": cadDot3adAggEntry,
       "cadDot3adAggId": cadDot3adAggId,
       "cadDot3adAggIndex": cadDot3adAggIndex,
       "cadDot3adAggMacAddress": cadDot3adAggMacAddress,
       "cadDot3adAggLacpEnable": cadDot3adAggLacpEnable,
       "cadDot3adAggLacpMode": cadDot3adAggLacpMode,
       "cadDot3adAggLacpRate": cadDot3adAggLacpRate,
       "cadDot3adAggMinLinks": cadDot3adAggMinLinks,
       "cadDot3adAggDescription": cadDot3adAggDescription,
       "cadDot3adAggTrapInh": cadDot3adAggTrapInh,
       "cadDot3adAggAdminState": cadDot3adAggAdminState,
       "cadDot3adAggPrState": cadDot3adAggPrState,
       "cadDot3adAggSecState": cadDot3adAggSecState,
       "cadDot3adAggRowStatus": cadDot3adAggRowStatus,
       "cadDot3adAggSystemID": cadDot3adAggSystemID,
       "cadDot3adParams": cadDot3adParams,
       "cadDot3adSystemPriority": cadDot3adSystemPriority,
       "cadAging": cadAging,
       "cadAgingCPEAgingInterval": cadAgingCPEAgingInterval,
       "cadAgingSFAgingInterval": cadAgingSFAgingInterval,
       "cadAgingStaleMACAgingInterval": cadAgingStaleMACAgingInterval,
       "cadAgingArpCacheAgingInterval": cadAgingArpCacheAgingInterval,
       "cadAgingIdleMACAgingInterval": cadAgingIdleMACAgingInterval,
       "cadAgingArpCacheSearchingRateLimit": cadAgingArpCacheSearchingRateLimit,
       "cadAgingArpCacheSearchingMaxNumber": cadAgingArpCacheSearchingMaxNumber,
       "cadAgingArpCacheNotPresentRateLimit": cadAgingArpCacheNotPresentRateLimit,
       "cadAgingArpCacheNotPresentMaxNumber": cadAgingArpCacheNotPresentMaxNumber,
       "cadAgingArpCacheNotPresentMaxTime": cadAgingArpCacheNotPresentMaxTime,
       "cadAgingArpCacheNotPresentMinTime": cadAgingArpCacheNotPresentMinTime,
       "cadAgingArpCacheSearchingGlobalMaxRate": cadAgingArpCacheSearchingGlobalMaxRate,
       "cadAgingArpCacheNotPresentGlobalMaxRate": cadAgingArpCacheNotPresentGlobalMaxRate,
       "cadAgingNDCacheAgingInterval": cadAgingNDCacheAgingInterval,
       "cadAgingNDCacheSearchingRateLimit": cadAgingNDCacheSearchingRateLimit,
       "cadAgingNDCacheSearchingMaxNumber": cadAgingNDCacheSearchingMaxNumber,
       "cadAgingNDCacheNotPresentRateLimit": cadAgingNDCacheNotPresentRateLimit,
       "cadAgingNDCacheNotPresentMaxNumber": cadAgingNDCacheNotPresentMaxNumber,
       "cadAgingNDCacheNotPresentMaxTime": cadAgingNDCacheNotPresentMaxTime,
       "cadAgingNDCacheNotPresentMinTime": cadAgingNDCacheNotPresentMinTime,
       "cadAgingNDCacheSearchingGlobalMaxRate": cadAgingNDCacheSearchingGlobalMaxRate,
       "cadAgingNDCacheNotPresentGlobalMaxRate": cadAgingNDCacheNotPresentGlobalMaxRate,
       "cadAgingArpCacheSearchingCableUnicast": cadAgingArpCacheSearchingCableUnicast,
       "cadAgingArpCacheSearchingCableBroadcast": cadAgingArpCacheSearchingCableBroadcast,
       "cadAgingNDCacheSearchingCableUnicast": cadAgingNDCacheSearchingCableUnicast,
       "cadAgingNDCacheSearchingCableMulticast": cadAgingNDCacheSearchingCableMulticast,
       "cadLayer2MibGroup": cadLayer2MibGroup,
       "cadAgingGroup": cadAgingGroup,
       "cerIpGroup": cerIpGroup,
       "cadMacPortMIBObjects": cadMacPortMIBObjects,
       "cadMacPortTable": cadMacPortTable,
       "cadMacPortEntry": cadMacPortEntry,
       "cadMacPortId": cadMacPortId,
       "cadMacPortAdminState": cadMacPortAdminState,
       "cadMacPortPrState": cadMacPortPrState,
       "cadMacPortSecState": cadMacPortSecState,
       "cadMacPortDplxStatus": cadMacPortDplxStatus,
       "cadMacPortMacAddress": cadMacPortMacAddress,
       "cadMacPortIfIndex": cadMacPortIfIndex,
       "cadMacPortDescription": cadMacPortDescription,
       "cadMacPortTrapInh": cadMacPortTrapInh,
       "cadMacPortRowStatus": cadMacPortRowStatus,
       "cadMacPortOfdm": cadMacPortOfdm,
       "cadIfMacDomainTable": cadIfMacDomainTable,
       "cadIfMacDomainEntry": cadIfMacDomainEntry,
       "cadIfMacDomainIfIndex": cadIfMacDomainIfIndex,
       "cadIfMacDomainCapabilities": cadIfMacDomainCapabilities,
       "cadIfMacDomainSyncInterval": cadIfMacDomainSyncInterval,
       "cadIfMacDomainUcdInterval": cadIfMacDomainUcdInterval,
       "cadIfMacDomainMaxServiceIds": cadIfMacDomainMaxServiceIds,
       "cadIfMacDomainInvitedRangingAttempts": cadIfMacDomainInvitedRangingAttempts,
       "cadIfMacDomainInsertInterval": cadIfMacDomainInsertInterval,
       "cadIfMacDomainRangingInterval": cadIfMacDomainRangingInterval,
       "cadIfMacDomainRangeOpportunityCycle": cadIfMacDomainRangeOpportunityCycle,
       "cadIfMacDomainTftpEnforce": cadIfMacDomainTftpEnforce,
       "cadIfMacDomainDynamicSecret": cadIfMacDomainDynamicSecret,
       "cadIfMacDomainAnnex": cadIfMacDomainAnnex,
       "cadIfMacDomainMddInterval": cadIfMacDomainMddInterval,
       "cadIfMacDomainIpProvMode": cadIfMacDomainIpProvMode,
       "cadIfMacDomainCmStatusEvCtlEnabled": cadIfMacDomainCmStatusEvCtlEnabled,
       "cadIfMacDomainUsFreqRange": cadIfMacDomainUsFreqRange,
       "cadIfMacDomainMcastDsidFwdEnabled": cadIfMacDomainMcastDsidFwdEnabled,
       "cadIfMacDomainDsBondingEnabled": cadIfMacDomainDsBondingEnabled,
       "cadIfMacDomainMultTxChModeEnabled": cadIfMacDomainMultTxChModeEnabled,
       "cadIfMacDomainEarlyAuthEncrCtrl": cadIfMacDomainEarlyAuthEncrCtrl,
       "cadIfMacDomainTftpProxyEnabled": cadIfMacDomainTftpProxyEnabled,
       "cadIfMacDomainSrcAddrVerifEnabled": cadIfMacDomainSrcAddrVerifEnabled,
       "cadIfMacDomainMulticastEncryption": cadIfMacDomainMulticastEncryption,
       "cadIfMacDomainRcpReportMode": cadIfMacDomainRcpReportMode,
       "cadIfMacDomainRegRspToOverride": cadIfMacDomainRegRspToOverride,
       "cadIfMacDomainMultRxChModeEnabled": cadIfMacDomainMultRxChModeEnabled,
       "cadIfMacDomainCmUdcEnabled": cadIfMacDomainCmUdcEnabled,
       "cadIfMacDomainSendUdcRulesEnabled": cadIfMacDomainSendUdcRulesEnabled,
       "cadIfMacDomainRccDynEnable": cadIfMacDomainRccDynEnable,
       "cadIfMacDomainDsbgDynEnable": cadIfMacDomainDsbgDynEnable,
       "cadIfMacDomainDsbgReseqWaitTime": cadIfMacDomainDsbgReseqWaitTime,
       "cadIfMacDomainDsbgReseqWarnThrshld": cadIfMacDomainDsbgReseqWarnThrshld,
       "cadIfMacDomainDpId": cadIfMacDomainDpId,
       "cadIfMacDomainUsbgDynEnable": cadIfMacDomainUsbgDynEnable,
       "cadIfMacDomainDownChannelMaxFrequency": cadIfMacDomainDownChannelMaxFrequency,
       "cadIfMacDomainDownChannelMinFrequency": cadIfMacDomainDownChannelMinFrequency,
       "cadIfMacDomainUpChannelMaxFrequency": cadIfMacDomainUpChannelMaxFrequency,
       "cadIfMacDomainBpi2Mandatory": cadIfMacDomainBpi2Mandatory,
       "cadIfMacDomainDSG30Enabled": cadIfMacDomainDSG30Enabled,
       "cadIfMacDomainEnforceRulesEnabled": cadIfMacDomainEnforceRulesEnabled,
       "cadIfMacDomainCmTxPwrExtentionPreRegistrationEnabled": cadIfMacDomainCmTxPwrExtentionPreRegistrationEnabled,
       "cadIfMacDomainCmTxPwrExtentionPostRegistrationEnabled": cadIfMacDomainCmTxPwrExtentionPostRegistrationEnabled,
       "cadIfMacDomainT4TimeoutMultiplierEnabled": cadIfMacDomainT4TimeoutMultiplierEnabled,
       "cadIfMacDomainDynamicRccMultiTunerEnabled": cadIfMacDomainDynamicRccMultiTunerEnabled,
       "cadIfMacDomainTcsSizeLimit": cadIfMacDomainTcsSizeLimit,
       "cadIfMacDomainDocsis31Enabled": cadIfMacDomainDocsis31Enabled,
       "cadIfMacDomainEnergyMgt1x1Enabled": cadIfMacDomainEnergyMgt1x1Enabled,
       "cadIfMacDomainDsOfdmProfileRecoveryGuardTime": cadIfMacDomainDsOfdmProfileRecoveryGuardTime,
       "cadIfMacDomainGracefulTcsReductionEnabled": cadIfMacDomainGracefulTcsReductionEnabled,
       "cadMacChlTable": cadMacChlTable,
       "cadMacChlEntry": cadMacChlEntry,
       "cadMacChlMacDomainIfIndex": cadMacChlMacDomainIfIndex,
       "cadMacChlChannelIfIndex": cadMacChlChannelIfIndex,
       "cadMacChlCardNumber": cadMacChlCardNumber,
       "cadMacChlPortId": cadMacChlPortId,
       "cadMacChlPortType": cadMacChlPortType,
       "cadMacChlCardSubType": cadMacChlCardSubType,
       "cadMacChlChannelId": cadMacChlChannelId,
       "cadMacChlRowStatus": cadMacChlRowStatus,
       "cadMacChlIsPriCapableDs": cadMacChlIsPriCapableDs,
       "cadMacChlSfProvAttrMask": cadMacChlSfProvAttrMask,
       "cadMacChlDirection": cadMacChlDirection,
       "cadUpSupervisionCfgTable": cadUpSupervisionCfgTable,
       "cadUpSupervisionCfgEntry": cadUpSupervisionCfgEntry,
       "cadUpSupervisionCfgUpChannelIfIndex": cadUpSupervisionCfgUpChannelIfIndex,
       "cadUpSupervisionCfgDownChannelIfIndex": cadUpSupervisionCfgDownChannelIfIndex,
       "cadUpSupervisionCfgAssign": cadUpSupervisionCfgAssign,
       "cadUpSupervisionCfgRowStatus": cadUpSupervisionCfgRowStatus,
       "cadUpSupervisionStatusTable": cadUpSupervisionStatusTable,
       "cadUpSupervisionStatusEntry": cadUpSupervisionStatusEntry,
       "cadUpSupervisionStatusUpChannelIfIndex": cadUpSupervisionStatusUpChannelIfIndex,
       "cadUpSupervisionStatusDownChannelIfIndex": cadUpSupervisionStatusDownChannelIfIndex,
       "cadUpSupervisionStatusAssignmentMethod": cadUpSupervisionStatusAssignmentMethod,
       "arrisCerIpGroup": arrisCerIpGroup,
       "cerIpGratuitousArpPeriod": cerIpGratuitousArpPeriod}
)
