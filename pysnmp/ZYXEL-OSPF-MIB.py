# SNMP MIB module (ZYXEL-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-OSPF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:29 2024
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

(ospfAddressLessIf,
 ospfAreaId,
 ospfIfIpAddress,
 ospfLsdbAreaId,
 ospfLsdbLsid,
 ospfLsdbRouterId,
 ospfLsdbType,
 ospfNbrAddressLessIndex,
 ospfNbrIpAddr,
 ospfVirtIfAreaId,
 ospfVirtIfNeighbor) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "ospfAddressLessIf",
    "ospfAreaId",
    "ospfIfIpAddress",
    "ospfLsdbAreaId",
    "ospfLsdbLsid",
    "ospfLsdbRouterId",
    "ospfLsdbType",
    "ospfNbrAddressLessIndex",
    "ospfNbrIpAddr",
    "ospfVirtIfAreaId",
    "ospfVirtIfNeighbor")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelOspf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelOspfSetup_ObjectIdentity = ObjectIdentity
zyxelOspfSetup = _ZyxelOspfSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1)
)
_ZyxelOspfIfTable_Object = MibTable
zyxelOspfIfTable = _ZyxelOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 1)
)
if mibBuilder.loadTexts:
    zyxelOspfIfTable.setStatus("current")
_ZyxelOspfIfEntry_Object = MibTableRow
zyxelOspfIfEntry = _ZyxelOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 1, 1)
)
zyxelOspfIfEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfIfIpAddress"),
    (0, "OSPF-MIB", "ospfAddressLessIf"),
)
if mibBuilder.loadTexts:
    zyxelOspfIfEntry.setStatus("current")
_ZyOspfIfKeyId_Type = Integer32
_ZyOspfIfKeyId_Object = MibTableColumn
zyOspfIfKeyId = _ZyOspfIfKeyId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 1, 1, 1),
    _ZyOspfIfKeyId_Type()
)
zyOspfIfKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyOspfIfKeyId.setStatus("current")
_ZyxelOspfAreaTable_Object = MibTable
zyxelOspfAreaTable = _ZyxelOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelOspfAreaTable.setStatus("current")
_ZyxelOspfAreaEntry_Object = MibTableRow
zyxelOspfAreaEntry = _ZyxelOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 2, 1)
)
zyxelOspfAreaEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfAreaId"),
)
if mibBuilder.loadTexts:
    zyxelOspfAreaEntry.setStatus("current")
_ZyOspfAreaName_Type = DisplayString
_ZyOspfAreaName_Object = MibTableColumn
zyOspfAreaName = _ZyOspfAreaName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 2, 1, 1),
    _ZyOspfAreaName_Type()
)
zyOspfAreaName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyOspfAreaName.setStatus("current")
_ZyxelOspfRedistributeRouteTable_Object = MibTable
zyxelOspfRedistributeRouteTable = _ZyxelOspfRedistributeRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 3)
)
if mibBuilder.loadTexts:
    zyxelOspfRedistributeRouteTable.setStatus("current")
_ZyxelOspfRedistributeRouteEntry_Object = MibTableRow
zyxelOspfRedistributeRouteEntry = _ZyxelOspfRedistributeRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 3, 1)
)
zyxelOspfRedistributeRouteEntry.setIndexNames(
    (0, "ZYXEL-OSPF-MIB", "zyOspfRedistributeRouteProtocol"),
)
if mibBuilder.loadTexts:
    zyxelOspfRedistributeRouteEntry.setStatus("current")


class _ZyOspfRedistributeRouteProtocol_Type(Integer32):
    """Custom type zyOspfRedistributeRouteProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rip", 1),
          ("static", 2))
    )


_ZyOspfRedistributeRouteProtocol_Type.__name__ = "Integer32"
_ZyOspfRedistributeRouteProtocol_Object = MibTableColumn
zyOspfRedistributeRouteProtocol = _ZyOspfRedistributeRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 3, 1, 1),
    _ZyOspfRedistributeRouteProtocol_Type()
)
zyOspfRedistributeRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyOspfRedistributeRouteProtocol.setStatus("current")
_ZyOspfRedistributeRouteState_Type = EnabledStatus
_ZyOspfRedistributeRouteState_Object = MibTableColumn
zyOspfRedistributeRouteState = _ZyOspfRedistributeRouteState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 3, 1, 2),
    _ZyOspfRedistributeRouteState_Type()
)
zyOspfRedistributeRouteState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyOspfRedistributeRouteState.setStatus("current")
_ZyOspfRedistributeRouteType_Type = Integer32
_ZyOspfRedistributeRouteType_Object = MibTableColumn
zyOspfRedistributeRouteType = _ZyOspfRedistributeRouteType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 3, 1, 3),
    _ZyOspfRedistributeRouteType_Type()
)
zyOspfRedistributeRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyOspfRedistributeRouteType.setStatus("current")
_ZyOspfRedistributeRouteMetric_Type = Integer32
_ZyOspfRedistributeRouteMetric_Object = MibTableColumn
zyOspfRedistributeRouteMetric = _ZyOspfRedistributeRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 3, 1, 4),
    _ZyOspfRedistributeRouteMetric_Type()
)
zyOspfRedistributeRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyOspfRedistributeRouteMetric.setStatus("current")
_ZyxelOspfVirtualLinkTable_Object = MibTable
zyxelOspfVirtualLinkTable = _ZyxelOspfVirtualLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 4)
)
if mibBuilder.loadTexts:
    zyxelOspfVirtualLinkTable.setStatus("current")
_ZyxelOspfVirtualLinkEntry_Object = MibTableRow
zyxelOspfVirtualLinkEntry = _ZyxelOspfVirtualLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 4, 1)
)
zyxelOspfVirtualLinkEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfVirtIfAreaId"),
    (0, "OSPF-MIB", "ospfVirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    zyxelOspfVirtualLinkEntry.setStatus("current")
_ZyOspfVirtualLinkName_Type = DisplayString
_ZyOspfVirtualLinkName_Object = MibTableColumn
zyOspfVirtualLinkName = _ZyOspfVirtualLinkName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 4, 1, 1),
    _ZyOspfVirtualLinkName_Type()
)
zyOspfVirtualLinkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyOspfVirtualLinkName.setStatus("current")
_ZyOspfVirtualLinkKeyId_Type = Integer32
_ZyOspfVirtualLinkKeyId_Object = MibTableColumn
zyOspfVirtualLinkKeyId = _ZyOspfVirtualLinkKeyId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 4, 1, 2),
    _ZyOspfVirtualLinkKeyId_Type()
)
zyOspfVirtualLinkKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyOspfVirtualLinkKeyId.setStatus("current")
_ZyOspfMaxNumberOfSummaryAddress_Type = Integer32
_ZyOspfMaxNumberOfSummaryAddress_Object = MibScalar
zyOspfMaxNumberOfSummaryAddress = _ZyOspfMaxNumberOfSummaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 5),
    _ZyOspfMaxNumberOfSummaryAddress_Type()
)
zyOspfMaxNumberOfSummaryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyOspfMaxNumberOfSummaryAddress.setStatus("current")
_ZyxelOspfSummaryAddressTable_Object = MibTable
zyxelOspfSummaryAddressTable = _ZyxelOspfSummaryAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 6)
)
if mibBuilder.loadTexts:
    zyxelOspfSummaryAddressTable.setStatus("current")
_ZyxelOspfSummaryAddressEntry_Object = MibTableRow
zyxelOspfSummaryAddressEntry = _ZyxelOspfSummaryAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 6, 1)
)
zyxelOspfSummaryAddressEntry.setIndexNames(
    (0, "ZYXEL-OSPF-MIB", "zyOspfSummaryAddressIpAddress"),
    (0, "ZYXEL-OSPF-MIB", "zyOspfSummaryAddressMaskBits"),
)
if mibBuilder.loadTexts:
    zyxelOspfSummaryAddressEntry.setStatus("current")
_ZyOspfSummaryAddressIpAddress_Type = IpAddress
_ZyOspfSummaryAddressIpAddress_Object = MibTableColumn
zyOspfSummaryAddressIpAddress = _ZyOspfSummaryAddressIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 6, 1, 1),
    _ZyOspfSummaryAddressIpAddress_Type()
)
zyOspfSummaryAddressIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyOspfSummaryAddressIpAddress.setStatus("current")
_ZyOspfSummaryAddressMaskBits_Type = Integer32
_ZyOspfSummaryAddressMaskBits_Object = MibTableColumn
zyOspfSummaryAddressMaskBits = _ZyOspfSummaryAddressMaskBits_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 6, 1, 2),
    _ZyOspfSummaryAddressMaskBits_Type()
)
zyOspfSummaryAddressMaskBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyOspfSummaryAddressMaskBits.setStatus("current")
_ZyOspfSummaryAddressRowStatus_Type = RowStatus
_ZyOspfSummaryAddressRowStatus_Object = MibTableColumn
zyOspfSummaryAddressRowStatus = _ZyOspfSummaryAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 6, 1, 3),
    _ZyOspfSummaryAddressRowStatus_Type()
)
zyOspfSummaryAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyOspfSummaryAddressRowStatus.setStatus("current")
_ZyxelOspfGeneralGroup_ObjectIdentity = ObjectIdentity
zyxelOspfGeneralGroup = _ZyxelOspfGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 7)
)
_ZyOspfDistance_Type = Integer32
_ZyOspfDistance_Object = MibScalar
zyOspfDistance = _ZyOspfDistance_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 1, 7, 1),
    _ZyOspfDistance_Type()
)
zyOspfDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyOspfDistance.setStatus("current")
_ZyxelOspfStatus_ObjectIdentity = ObjectIdentity
zyxelOspfStatus = _ZyxelOspfStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2)
)
_ZyxelOspfIfInfoTable_Object = MibTable
zyxelOspfIfInfoTable = _ZyxelOspfIfInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 1)
)
if mibBuilder.loadTexts:
    zyxelOspfIfInfoTable.setStatus("current")
_ZyxelOspfIfInfoEntry_Object = MibTableRow
zyxelOspfIfInfoEntry = _ZyxelOspfIfInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 1, 1)
)
zyxelOspfIfInfoEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfIfIpAddress"),
    (0, "OSPF-MIB", "ospfAddressLessIf"),
)
if mibBuilder.loadTexts:
    zyxelOspfIfInfoEntry.setStatus("current")
_ZyOspfIfInfoMaskbits_Type = Integer32
_ZyOspfIfInfoMaskbits_Object = MibTableColumn
zyOspfIfInfoMaskbits = _ZyOspfIfInfoMaskbits_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 1, 1, 1),
    _ZyOspfIfInfoMaskbits_Type()
)
zyOspfIfInfoMaskbits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyOspfIfInfoMaskbits.setStatus("current")
_ZyOspfIfInfoDesignatedRouterID_Type = IpAddress
_ZyOspfIfInfoDesignatedRouterID_Object = MibTableColumn
zyOspfIfInfoDesignatedRouterID = _ZyOspfIfInfoDesignatedRouterID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 1, 1, 2),
    _ZyOspfIfInfoDesignatedRouterID_Type()
)
zyOspfIfInfoDesignatedRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyOspfIfInfoDesignatedRouterID.setStatus("current")
_ZyOspfIfInfoBackupDesignatedRouterID_Type = IpAddress
_ZyOspfIfInfoBackupDesignatedRouterID_Object = MibTableColumn
zyOspfIfInfoBackupDesignatedRouterID = _ZyOspfIfInfoBackupDesignatedRouterID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 1, 1, 3),
    _ZyOspfIfInfoBackupDesignatedRouterID_Type()
)
zyOspfIfInfoBackupDesignatedRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyOspfIfInfoBackupDesignatedRouterID.setStatus("current")
_ZyOspfIfInfoNbrCount_Type = Integer32
_ZyOspfIfInfoNbrCount_Object = MibTableColumn
zyOspfIfInfoNbrCount = _ZyOspfIfInfoNbrCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 1, 1, 4),
    _ZyOspfIfInfoNbrCount_Type()
)
zyOspfIfInfoNbrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyOspfIfInfoNbrCount.setStatus("current")
_ZyOspfIfInfoAdjacentNbrCount_Type = Integer32
_ZyOspfIfInfoAdjacentNbrCount_Object = MibTableColumn
zyOspfIfInfoAdjacentNbrCount = _ZyOspfIfInfoAdjacentNbrCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 1, 1, 5),
    _ZyOspfIfInfoAdjacentNbrCount_Type()
)
zyOspfIfInfoAdjacentNbrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyOspfIfInfoAdjacentNbrCount.setStatus("current")
_ZyOspfIfInfoHelloDueTime_Type = DisplayString
_ZyOspfIfInfoHelloDueTime_Object = MibTableColumn
zyOspfIfInfoHelloDueTime = _ZyOspfIfInfoHelloDueTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 1, 1, 6),
    _ZyOspfIfInfoHelloDueTime_Type()
)
zyOspfIfInfoHelloDueTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyOspfIfInfoHelloDueTime.setStatus("current")
_ZyxelOspfNbrTable_Object = MibTable
zyxelOspfNbrTable = _ZyxelOspfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 2)
)
if mibBuilder.loadTexts:
    zyxelOspfNbrTable.setStatus("current")
_ZyxelOspfNbrEntry_Object = MibTableRow
zyxelOspfNbrEntry = _ZyxelOspfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 2, 1)
)
zyxelOspfNbrEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfNbrIpAddr"),
    (0, "OSPF-MIB", "ospfNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    zyxelOspfNbrEntry.setStatus("current")


class _ZyOspfNbrRole_Type(Integer32):
    """Custom type zyOspfNbrRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("dr", 1),
          ("drOther", 3))
    )


_ZyOspfNbrRole_Type.__name__ = "Integer32"
_ZyOspfNbrRole_Object = MibTableColumn
zyOspfNbrRole = _ZyOspfNbrRole_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 2, 1, 1),
    _ZyOspfNbrRole_Type()
)
zyOspfNbrRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyOspfNbrRole.setStatus("current")
_ZyOspfNbrDeadtime_Type = DisplayString
_ZyOspfNbrDeadtime_Object = MibTableColumn
zyOspfNbrDeadtime = _ZyOspfNbrDeadtime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 2, 1, 2),
    _ZyOspfNbrDeadtime_Type()
)
zyOspfNbrDeadtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyOspfNbrDeadtime.setStatus("current")
_ZyOspfNbrInterface_Type = IpAddress
_ZyOspfNbrInterface_Object = MibTableColumn
zyOspfNbrInterface = _ZyOspfNbrInterface_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 2, 1, 3),
    _ZyOspfNbrInterface_Type()
)
zyOspfNbrInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyOspfNbrInterface.setStatus("current")
_ZyOspfNbrRetransmitLSA_Type = Integer32
_ZyOspfNbrRetransmitLSA_Object = MibTableColumn
zyOspfNbrRetransmitLSA = _ZyOspfNbrRetransmitLSA_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 2, 1, 4),
    _ZyOspfNbrRetransmitLSA_Type()
)
zyOspfNbrRetransmitLSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyOspfNbrRetransmitLSA.setStatus("current")
_ZyOspfNbrRequestLSA_Type = Integer32
_ZyOspfNbrRequestLSA_Object = MibTableColumn
zyOspfNbrRequestLSA = _ZyOspfNbrRequestLSA_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 2, 1, 5),
    _ZyOspfNbrRequestLSA_Type()
)
zyOspfNbrRequestLSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyOspfNbrRequestLSA.setStatus("current")
_ZyOspfNbrDatabaseSummaryLSA_Type = Integer32
_ZyOspfNbrDatabaseSummaryLSA_Object = MibTableColumn
zyOspfNbrDatabaseSummaryLSA = _ZyOspfNbrDatabaseSummaryLSA_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 2, 1, 6),
    _ZyOspfNbrDatabaseSummaryLSA_Type()
)
zyOspfNbrDatabaseSummaryLSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyOspfNbrDatabaseSummaryLSA.setStatus("current")
_ZyxelOspfLsdbTable_Object = MibTable
zyxelOspfLsdbTable = _ZyxelOspfLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 3)
)
if mibBuilder.loadTexts:
    zyxelOspfLsdbTable.setStatus("current")
_ZyxelOspfLsdbEntry_Object = MibTableRow
zyxelOspfLsdbEntry = _ZyxelOspfLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 3, 1)
)
zyxelOspfLsdbEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfLsdbAreaId"),
    (0, "OSPF-MIB", "ospfLsdbType"),
    (0, "OSPF-MIB", "ospfLsdbLsid"),
    (0, "OSPF-MIB", "ospfLsdbRouterId"),
)
if mibBuilder.loadTexts:
    zyxelOspfLsdbEntry.setStatus("current")
_ZyOspfLsdbLinkCount_Type = Integer32
_ZyOspfLsdbLinkCount_Object = MibTableColumn
zyOspfLsdbLinkCount = _ZyOspfLsdbLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 3, 1, 1),
    _ZyOspfLsdbLinkCount_Type()
)
zyOspfLsdbLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyOspfLsdbLinkCount.setStatus("current")
_ZyOspfLsdbRouteIpAddress_Type = IpAddress
_ZyOspfLsdbRouteIpAddress_Object = MibTableColumn
zyOspfLsdbRouteIpAddress = _ZyOspfLsdbRouteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 3, 1, 2),
    _ZyOspfLsdbRouteIpAddress_Type()
)
zyOspfLsdbRouteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyOspfLsdbRouteIpAddress.setStatus("current")
_ZyOspfLsdbRouteMaskBits_Type = Integer32
_ZyOspfLsdbRouteMaskBits_Object = MibTableColumn
zyOspfLsdbRouteMaskBits = _ZyOspfLsdbRouteMaskBits_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 57, 2, 3, 1, 3),
    _ZyOspfLsdbRouteMaskBits_Type()
)
zyOspfLsdbRouteMaskBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyOspfLsdbRouteMaskBits.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-OSPF-MIB",
    **{"zyxelOspf": zyxelOspf,
       "zyxelOspfSetup": zyxelOspfSetup,
       "zyxelOspfIfTable": zyxelOspfIfTable,
       "zyxelOspfIfEntry": zyxelOspfIfEntry,
       "zyOspfIfKeyId": zyOspfIfKeyId,
       "zyxelOspfAreaTable": zyxelOspfAreaTable,
       "zyxelOspfAreaEntry": zyxelOspfAreaEntry,
       "zyOspfAreaName": zyOspfAreaName,
       "zyxelOspfRedistributeRouteTable": zyxelOspfRedistributeRouteTable,
       "zyxelOspfRedistributeRouteEntry": zyxelOspfRedistributeRouteEntry,
       "zyOspfRedistributeRouteProtocol": zyOspfRedistributeRouteProtocol,
       "zyOspfRedistributeRouteState": zyOspfRedistributeRouteState,
       "zyOspfRedistributeRouteType": zyOspfRedistributeRouteType,
       "zyOspfRedistributeRouteMetric": zyOspfRedistributeRouteMetric,
       "zyxelOspfVirtualLinkTable": zyxelOspfVirtualLinkTable,
       "zyxelOspfVirtualLinkEntry": zyxelOspfVirtualLinkEntry,
       "zyOspfVirtualLinkName": zyOspfVirtualLinkName,
       "zyOspfVirtualLinkKeyId": zyOspfVirtualLinkKeyId,
       "zyOspfMaxNumberOfSummaryAddress": zyOspfMaxNumberOfSummaryAddress,
       "zyxelOspfSummaryAddressTable": zyxelOspfSummaryAddressTable,
       "zyxelOspfSummaryAddressEntry": zyxelOspfSummaryAddressEntry,
       "zyOspfSummaryAddressIpAddress": zyOspfSummaryAddressIpAddress,
       "zyOspfSummaryAddressMaskBits": zyOspfSummaryAddressMaskBits,
       "zyOspfSummaryAddressRowStatus": zyOspfSummaryAddressRowStatus,
       "zyxelOspfGeneralGroup": zyxelOspfGeneralGroup,
       "zyOspfDistance": zyOspfDistance,
       "zyxelOspfStatus": zyxelOspfStatus,
       "zyxelOspfIfInfoTable": zyxelOspfIfInfoTable,
       "zyxelOspfIfInfoEntry": zyxelOspfIfInfoEntry,
       "zyOspfIfInfoMaskbits": zyOspfIfInfoMaskbits,
       "zyOspfIfInfoDesignatedRouterID": zyOspfIfInfoDesignatedRouterID,
       "zyOspfIfInfoBackupDesignatedRouterID": zyOspfIfInfoBackupDesignatedRouterID,
       "zyOspfIfInfoNbrCount": zyOspfIfInfoNbrCount,
       "zyOspfIfInfoAdjacentNbrCount": zyOspfIfInfoAdjacentNbrCount,
       "zyOspfIfInfoHelloDueTime": zyOspfIfInfoHelloDueTime,
       "zyxelOspfNbrTable": zyxelOspfNbrTable,
       "zyxelOspfNbrEntry": zyxelOspfNbrEntry,
       "zyOspfNbrRole": zyOspfNbrRole,
       "zyOspfNbrDeadtime": zyOspfNbrDeadtime,
       "zyOspfNbrInterface": zyOspfNbrInterface,
       "zyOspfNbrRetransmitLSA": zyOspfNbrRetransmitLSA,
       "zyOspfNbrRequestLSA": zyOspfNbrRequestLSA,
       "zyOspfNbrDatabaseSummaryLSA": zyOspfNbrDatabaseSummaryLSA,
       "zyxelOspfLsdbTable": zyxelOspfLsdbTable,
       "zyxelOspfLsdbEntry": zyxelOspfLsdbEntry,
       "zyOspfLsdbLinkCount": zyOspfLsdbLinkCount,
       "zyOspfLsdbRouteIpAddress": zyOspfLsdbRouteIpAddress,
       "zyOspfLsdbRouteMaskBits": zyOspfLsdbRouteMaskBits}
)
