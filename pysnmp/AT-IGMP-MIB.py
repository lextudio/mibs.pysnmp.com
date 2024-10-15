# SNMP MIB module (AT-IGMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-IGMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:17 2024
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

(modules,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "modules")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

igmp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139)
)
igmp.setRevisions(
        ("2007-08-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IgmpIntInfo_ObjectIdentity = ObjectIdentity
igmpIntInfo = _IgmpIntInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1)
)
_IgmpInterfaceTable_Object = MibTable
igmpInterfaceTable = _IgmpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 1)
)
if mibBuilder.loadTexts:
    igmpInterfaceTable.setStatus("current")
_IgmpInterfaceEntry_Object = MibTableRow
igmpInterfaceEntry = _IgmpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 1, 1)
)
igmpInterfaceEntry.setIndexNames(
    (0, "AT-IGMP-MIB", "igmpInterface"),
)
if mibBuilder.loadTexts:
    igmpInterfaceEntry.setStatus("current")
_IgmpInterface_Type = Integer32
_IgmpInterface_Object = MibTableColumn
igmpInterface = _IgmpInterface_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 1, 1, 1),
    _IgmpInterface_Type()
)
igmpInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInterface.setStatus("current")
_IgmpInterfaceName_Type = DisplayString
_IgmpInterfaceName_Object = MibTableColumn
igmpInterfaceName = _IgmpInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 1, 1, 2),
    _IgmpInterfaceName_Type()
)
igmpInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInterfaceName.setStatus("current")


class _IgmpQueryTimeout_Type(Unsigned32):
    """Custom type igmpQueryTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IgmpQueryTimeout_Type.__name__ = "Unsigned32"
_IgmpQueryTimeout_Object = MibTableColumn
igmpQueryTimeout = _IgmpQueryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 1, 1, 3),
    _IgmpQueryTimeout_Type()
)
igmpQueryTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpQueryTimeout.setStatus("current")


class _IgmpProxy_Type(Integer32):
    """Custom type igmpProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 2),
          ("off", 0),
          ("upstream", 1))
    )


_IgmpProxy_Type.__name__ = "Integer32"
_IgmpProxy_Object = MibTableColumn
igmpProxy = _IgmpProxy_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 1, 1, 4),
    _IgmpProxy_Type()
)
igmpProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpProxy.setStatus("current")
_IgmpIntStatsTable_Object = MibTable
igmpIntStatsTable = _IgmpIntStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 2)
)
if mibBuilder.loadTexts:
    igmpIntStatsTable.setStatus("current")
_IgmpIntStatsEntry_Object = MibTableRow
igmpIntStatsEntry = _IgmpIntStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 2, 1)
)
igmpIntStatsEntry.setIndexNames(
    (0, "AT-IGMP-MIB", "igmpInterface"),
)
if mibBuilder.loadTexts:
    igmpIntStatsEntry.setStatus("current")
_IgmpInQuery_Type = Unsigned32
_IgmpInQuery_Object = MibTableColumn
igmpInQuery = _IgmpInQuery_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 2, 1, 1),
    _IgmpInQuery_Type()
)
igmpInQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInQuery.setStatus("current")
_IgmpInReportV1_Type = Unsigned32
_IgmpInReportV1_Object = MibTableColumn
igmpInReportV1 = _IgmpInReportV1_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 2, 1, 2),
    _IgmpInReportV1_Type()
)
igmpInReportV1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInReportV1.setStatus("current")
_IgmpInReportV2_Type = Unsigned32
_IgmpInReportV2_Object = MibTableColumn
igmpInReportV2 = _IgmpInReportV2_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 2, 1, 3),
    _IgmpInReportV2_Type()
)
igmpInReportV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInReportV2.setStatus("current")
_IgmpInLeave_Type = Unsigned32
_IgmpInLeave_Object = MibTableColumn
igmpInLeave = _IgmpInLeave_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 2, 1, 4),
    _IgmpInLeave_Type()
)
igmpInLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInLeave.setStatus("current")
_IgmpInTotal_Type = Unsigned32
_IgmpInTotal_Object = MibTableColumn
igmpInTotal = _IgmpInTotal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 2, 1, 5),
    _IgmpInTotal_Type()
)
igmpInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInTotal.setStatus("current")
_IgmpOutQuery_Type = Unsigned32
_IgmpOutQuery_Object = MibTableColumn
igmpOutQuery = _IgmpOutQuery_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 2, 1, 6),
    _IgmpOutQuery_Type()
)
igmpOutQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpOutQuery.setStatus("current")
_IgmpOutTotal_Type = Unsigned32
_IgmpOutTotal_Object = MibTableColumn
igmpOutTotal = _IgmpOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 2, 1, 7),
    _IgmpOutTotal_Type()
)
igmpOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpOutTotal.setStatus("current")
_IgmpBadQuery_Type = Unsigned32
_IgmpBadQuery_Object = MibTableColumn
igmpBadQuery = _IgmpBadQuery_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 2, 1, 8),
    _IgmpBadQuery_Type()
)
igmpBadQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpBadQuery.setStatus("current")
_IgmpBadReportV1_Type = Unsigned32
_IgmpBadReportV1_Object = MibTableColumn
igmpBadReportV1 = _IgmpBadReportV1_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 2, 1, 9),
    _IgmpBadReportV1_Type()
)
igmpBadReportV1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpBadReportV1.setStatus("current")
_IgmpBadReportV2_Type = Unsigned32
_IgmpBadReportV2_Object = MibTableColumn
igmpBadReportV2 = _IgmpBadReportV2_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 2, 1, 10),
    _IgmpBadReportV2_Type()
)
igmpBadReportV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpBadReportV2.setStatus("current")
_IgmpBadLeave_Type = Unsigned32
_IgmpBadLeave_Object = MibTableColumn
igmpBadLeave = _IgmpBadLeave_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 2, 1, 11),
    _IgmpBadLeave_Type()
)
igmpBadLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpBadLeave.setStatus("current")
_IgmpBadTotal_Type = Unsigned32
_IgmpBadTotal_Object = MibTableColumn
igmpBadTotal = _IgmpBadTotal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 1, 2, 1, 12),
    _IgmpBadTotal_Type()
)
igmpBadTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpBadTotal.setStatus("current")
_IgmpIntMember_ObjectIdentity = ObjectIdentity
igmpIntMember = _IgmpIntMember_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 9)
)
_IgmpIntGroupTable_Object = MibTable
igmpIntGroupTable = _IgmpIntGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 9, 1)
)
if mibBuilder.loadTexts:
    igmpIntGroupTable.setStatus("current")
_IgmpIntGroupEntry_Object = MibTableRow
igmpIntGroupEntry = _IgmpIntGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 9, 1, 1)
)
igmpIntGroupEntry.setIndexNames(
    (0, "AT-IGMP-MIB", "igmpInterface"),
)
if mibBuilder.loadTexts:
    igmpIntGroupEntry.setStatus("current")
_IgmpIntGroupAddress_Type = IpAddress
_IgmpIntGroupAddress_Object = MibTableColumn
igmpIntGroupAddress = _IgmpIntGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 9, 1, 1, 1),
    _IgmpIntGroupAddress_Type()
)
igmpIntGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpIntGroupAddress.setStatus("current")
_IgmpLastHost_Type = IpAddress
_IgmpLastHost_Object = MibTableColumn
igmpLastHost = _IgmpLastHost_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 9, 1, 1, 2),
    _IgmpLastHost_Type()
)
igmpLastHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpLastHost.setStatus("current")
_IgmpRefreshTime_Type = Unsigned32
_IgmpRefreshTime_Object = MibTableColumn
igmpRefreshTime = _IgmpRefreshTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 9, 1, 1, 3),
    _IgmpRefreshTime_Type()
)
igmpRefreshTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpRefreshTime.setStatus("current")
_IgmpSnooping_ObjectIdentity = ObjectIdentity
igmpSnooping = _IgmpSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10)
)
_IgmpSnoopAdminInfo_ObjectIdentity = ObjectIdentity
igmpSnoopAdminInfo = _IgmpSnoopAdminInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 1)
)
_IgmpSnoopAdminEnabled_Type = TruthValue
_IgmpSnoopAdminEnabled_Object = MibScalar
igmpSnoopAdminEnabled = _IgmpSnoopAdminEnabled_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 1, 1),
    _IgmpSnoopAdminEnabled_Type()
)
igmpSnoopAdminEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopAdminEnabled.setStatus("current")
_IgmpSnoopVlanTable_Object = MibTable
igmpSnoopVlanTable = _IgmpSnoopVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 2)
)
if mibBuilder.loadTexts:
    igmpSnoopVlanTable.setStatus("current")
_IgmpSnoopVlanEntry_Object = MibTableRow
igmpSnoopVlanEntry = _IgmpSnoopVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 2, 1)
)
igmpSnoopVlanEntry.setIndexNames(
    (0, "AT-IGMP-MIB", "igmpSnoopVID"),
)
if mibBuilder.loadTexts:
    igmpSnoopVlanEntry.setStatus("current")
_IgmpSnoopVID_Type = Integer32
_IgmpSnoopVID_Object = MibTableColumn
igmpSnoopVID = _IgmpSnoopVID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 2, 1, 1),
    _IgmpSnoopVID_Type()
)
igmpSnoopVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopVID.setStatus("current")
_IgmpSnoopVlanName_Type = DisplayString
_IgmpSnoopVlanName_Object = MibTableColumn
igmpSnoopVlanName = _IgmpSnoopVlanName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 2, 1, 2),
    _IgmpSnoopVlanName_Type()
)
igmpSnoopVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopVlanName.setStatus("current")


class _IgmpSnoopFastLeave_Type(Integer32):
    """Custom type igmpSnoopFastLeave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multi", 2),
          ("off", 0),
          ("single", 1))
    )


_IgmpSnoopFastLeave_Type.__name__ = "Integer32"
_IgmpSnoopFastLeave_Object = MibTableColumn
igmpSnoopFastLeave = _IgmpSnoopFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 2, 1, 3),
    _IgmpSnoopFastLeave_Type()
)
igmpSnoopFastLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopFastLeave.setStatus("current")
_IgmpSnoopQuerySolicit_Type = TruthValue
_IgmpSnoopQuerySolicit_Object = MibTableColumn
igmpSnoopQuerySolicit = _IgmpSnoopQuerySolicit_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 2, 1, 4),
    _IgmpSnoopQuerySolicit_Type()
)
igmpSnoopQuerySolicit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopQuerySolicit.setStatus("current")
_IgmpSnoopStaticRouterPorts_Type = DisplayString
_IgmpSnoopStaticRouterPorts_Object = MibTableColumn
igmpSnoopStaticRouterPorts = _IgmpSnoopStaticRouterPorts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 2, 1, 5),
    _IgmpSnoopStaticRouterPorts_Type()
)
igmpSnoopStaticRouterPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopStaticRouterPorts.setStatus("current")
_IgmpSnoopGroupTable_Object = MibTable
igmpSnoopGroupTable = _IgmpSnoopGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 3)
)
if mibBuilder.loadTexts:
    igmpSnoopGroupTable.setStatus("current")
_IgmpSnoopGroupEntry_Object = MibTableRow
igmpSnoopGroupEntry = _IgmpSnoopGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 3, 1)
)
igmpSnoopGroupEntry.setIndexNames(
    (0, "AT-IGMP-MIB", "igmpSnoopVID"),
    (0, "AT-IGMP-MIB", "igmpSnoopGroupAddress"),
)
if mibBuilder.loadTexts:
    igmpSnoopGroupEntry.setStatus("current")
_IgmpSnoopGroupAddress_Type = IpAddress
_IgmpSnoopGroupAddress_Object = MibTableColumn
igmpSnoopGroupAddress = _IgmpSnoopGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 3, 1, 1),
    _IgmpSnoopGroupAddress_Type()
)
igmpSnoopGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopGroupAddress.setStatus("current")
_IgmpSnoopGroupTimer_Type = Unsigned32
_IgmpSnoopGroupTimer_Object = MibTableColumn
igmpSnoopGroupTimer = _IgmpSnoopGroupTimer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 3, 1, 2),
    _IgmpSnoopGroupTimer_Type()
)
igmpSnoopGroupTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopGroupTimer.setStatus("current")
_IgmpSnoopPortTable_Object = MibTable
igmpSnoopPortTable = _IgmpSnoopPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 4)
)
if mibBuilder.loadTexts:
    igmpSnoopPortTable.setStatus("current")
_IgmpSnoopPortEntry_Object = MibTableRow
igmpSnoopPortEntry = _IgmpSnoopPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 4, 1)
)
igmpSnoopPortEntry.setIndexNames(
    (0, "AT-IGMP-MIB", "igmpSnoopVID"),
    (0, "AT-IGMP-MIB", "igmpSnoopGroupAddress"),
    (0, "AT-IGMP-MIB", "igmpSnoopPortNumber"),
)
if mibBuilder.loadTexts:
    igmpSnoopPortEntry.setStatus("current")
_IgmpSnoopPortNumber_Type = Integer32
_IgmpSnoopPortNumber_Object = MibTableColumn
igmpSnoopPortNumber = _IgmpSnoopPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 4, 1, 1),
    _IgmpSnoopPortNumber_Type()
)
igmpSnoopPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopPortNumber.setStatus("current")
_IgmpSnoopPortIsStatic_Type = TruthValue
_IgmpSnoopPortIsStatic_Object = MibTableColumn
igmpSnoopPortIsStatic = _IgmpSnoopPortIsStatic_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 4, 1, 2),
    _IgmpSnoopPortIsStatic_Type()
)
igmpSnoopPortIsStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopPortIsStatic.setStatus("current")
_IgmpSnoopPortTimer_Type = Unsigned32
_IgmpSnoopPortTimer_Object = MibTableColumn
igmpSnoopPortTimer = _IgmpSnoopPortTimer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 4, 1, 3),
    _IgmpSnoopPortTimer_Type()
)
igmpSnoopPortTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopPortTimer.setStatus("current")
_IgmpSnoopHostTable_Object = MibTable
igmpSnoopHostTable = _IgmpSnoopHostTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 5)
)
if mibBuilder.loadTexts:
    igmpSnoopHostTable.setStatus("current")
_IgmpSnoopHostEntry_Object = MibTableRow
igmpSnoopHostEntry = _IgmpSnoopHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 5, 1)
)
igmpSnoopHostEntry.setIndexNames(
    (0, "AT-IGMP-MIB", "igmpSnoopVID"),
    (0, "AT-IGMP-MIB", "igmpSnoopGroupAddress"),
    (0, "AT-IGMP-MIB", "igmpSnoopPortNumber"),
    (0, "AT-IGMP-MIB", "igmpSnoopHostMAC"),
)
if mibBuilder.loadTexts:
    igmpSnoopHostEntry.setStatus("current")
_IgmpSnoopHostMAC_Type = MacAddress
_IgmpSnoopHostMAC_Object = MibTableColumn
igmpSnoopHostMAC = _IgmpSnoopHostMAC_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 5, 1, 1),
    _IgmpSnoopHostMAC_Type()
)
igmpSnoopHostMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopHostMAC.setStatus("current")
_IgmpSnoopHostIpAddress_Type = IpAddress
_IgmpSnoopHostIpAddress_Object = MibTableColumn
igmpSnoopHostIpAddress = _IgmpSnoopHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 5, 1, 2),
    _IgmpSnoopHostIpAddress_Type()
)
igmpSnoopHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopHostIpAddress.setStatus("current")
_IgmpSnoopHostTimer_Type = Unsigned32
_IgmpSnoopHostTimer_Object = MibTableColumn
igmpSnoopHostTimer = _IgmpSnoopHostTimer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 139, 10, 5, 1, 3),
    _IgmpSnoopHostTimer_Type()
)
igmpSnoopHostTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopHostTimer.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-IGMP-MIB",
    **{"igmp": igmp,
       "igmpIntInfo": igmpIntInfo,
       "igmpInterfaceTable": igmpInterfaceTable,
       "igmpInterfaceEntry": igmpInterfaceEntry,
       "igmpInterface": igmpInterface,
       "igmpInterfaceName": igmpInterfaceName,
       "igmpQueryTimeout": igmpQueryTimeout,
       "igmpProxy": igmpProxy,
       "igmpIntStatsTable": igmpIntStatsTable,
       "igmpIntStatsEntry": igmpIntStatsEntry,
       "igmpInQuery": igmpInQuery,
       "igmpInReportV1": igmpInReportV1,
       "igmpInReportV2": igmpInReportV2,
       "igmpInLeave": igmpInLeave,
       "igmpInTotal": igmpInTotal,
       "igmpOutQuery": igmpOutQuery,
       "igmpOutTotal": igmpOutTotal,
       "igmpBadQuery": igmpBadQuery,
       "igmpBadReportV1": igmpBadReportV1,
       "igmpBadReportV2": igmpBadReportV2,
       "igmpBadLeave": igmpBadLeave,
       "igmpBadTotal": igmpBadTotal,
       "igmpIntMember": igmpIntMember,
       "igmpIntGroupTable": igmpIntGroupTable,
       "igmpIntGroupEntry": igmpIntGroupEntry,
       "igmpIntGroupAddress": igmpIntGroupAddress,
       "igmpLastHost": igmpLastHost,
       "igmpRefreshTime": igmpRefreshTime,
       "igmpSnooping": igmpSnooping,
       "igmpSnoopAdminInfo": igmpSnoopAdminInfo,
       "igmpSnoopAdminEnabled": igmpSnoopAdminEnabled,
       "igmpSnoopVlanTable": igmpSnoopVlanTable,
       "igmpSnoopVlanEntry": igmpSnoopVlanEntry,
       "igmpSnoopVID": igmpSnoopVID,
       "igmpSnoopVlanName": igmpSnoopVlanName,
       "igmpSnoopFastLeave": igmpSnoopFastLeave,
       "igmpSnoopQuerySolicit": igmpSnoopQuerySolicit,
       "igmpSnoopStaticRouterPorts": igmpSnoopStaticRouterPorts,
       "igmpSnoopGroupTable": igmpSnoopGroupTable,
       "igmpSnoopGroupEntry": igmpSnoopGroupEntry,
       "igmpSnoopGroupAddress": igmpSnoopGroupAddress,
       "igmpSnoopGroupTimer": igmpSnoopGroupTimer,
       "igmpSnoopPortTable": igmpSnoopPortTable,
       "igmpSnoopPortEntry": igmpSnoopPortEntry,
       "igmpSnoopPortNumber": igmpSnoopPortNumber,
       "igmpSnoopPortIsStatic": igmpSnoopPortIsStatic,
       "igmpSnoopPortTimer": igmpSnoopPortTimer,
       "igmpSnoopHostTable": igmpSnoopHostTable,
       "igmpSnoopHostEntry": igmpSnoopHostEntry,
       "igmpSnoopHostMAC": igmpSnoopHostMAC,
       "igmpSnoopHostIpAddress": igmpSnoopHostIpAddress,
       "igmpSnoopHostTimer": igmpSnoopHostTimer}
)
