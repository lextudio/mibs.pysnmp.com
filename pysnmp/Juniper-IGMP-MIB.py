# SNMP MIB module (Juniper-IGMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-IGMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:26 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniInterfaceLocationType,
 JuniInterfaceLocationValue) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniInterfaceLocationType",
    "JuniInterfaceLocationValue")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

juniIgmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40)
)
juniIgmpMIB.setRevisions(
        ("2006-08-25 05:40",
         "2003-09-29 18:39",
         "2002-10-28 14:55",
         "2000-09-26 18:50")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniIgmpProxyGroupState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("juniIgmpProxyGroupDelayingMember", 2),
          ("juniIgmpProxyGroupIdleMember", 1),
          ("juniIgmpProxyGroupUnknown", 0))
    )



class JuniIgmpProxyInterfaceState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("juniIgmpProxyInterfaceStateNonV1RouterPresent", 2),
          ("juniIgmpProxyInterfaceStateV1RouterPresent", 1),
          ("juniIgmpProxyInterfaceUnknown", 0))
    )



# MIB Managed Objects in the order of their OIDs

_JuniIgmpMIBObject_ObjectIdentity = ObjectIdentity
juniIgmpMIBObject = _JuniIgmpMIBObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1)
)
_JuniIgmpProtocol_ObjectIdentity = ObjectIdentity
juniIgmpProtocol = _JuniIgmpProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 1)
)
_JuniIgmpInterfaceTable_Object = MibTable
juniIgmpInterfaceTable = _JuniIgmpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 1, 1)
)
if mibBuilder.loadTexts:
    juniIgmpInterfaceTable.setStatus("current")
_JuniIgmpInterfaceEntry_Object = MibTableRow
juniIgmpInterfaceEntry = _JuniIgmpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 1, 1, 1)
)
juniIgmpInterfaceEntry.setIndexNames(
    (0, "Juniper-IGMP-MIB", "juniIgmpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    juniIgmpInterfaceEntry.setStatus("current")
_JuniIgmpInterfaceIfIndex_Type = InterfaceIndex
_JuniIgmpInterfaceIfIndex_Object = MibTableColumn
juniIgmpInterfaceIfIndex = _JuniIgmpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 1, 1, 1, 1),
    _JuniIgmpInterfaceIfIndex_Type()
)
juniIgmpInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIgmpInterfaceIfIndex.setStatus("current")


class _JuniIgmpInterfaceQuerierTimeout_Type(Integer32):
    """Custom type juniIgmpInterfaceQuerierTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 399),
    )


_JuniIgmpInterfaceQuerierTimeout_Type.__name__ = "Integer32"
_JuniIgmpInterfaceQuerierTimeout_Object = MibTableColumn
juniIgmpInterfaceQuerierTimeout = _JuniIgmpInterfaceQuerierTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 1, 1, 1, 2),
    _JuniIgmpInterfaceQuerierTimeout_Type()
)
juniIgmpInterfaceQuerierTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIgmpInterfaceQuerierTimeout.setStatus("current")
if mibBuilder.loadTexts:
    juniIgmpInterfaceQuerierTimeout.setUnits("seconds")
_JuniIgmpInterfaceImmediateLeave_Type = TruthValue
_JuniIgmpInterfaceImmediateLeave_Object = MibTableColumn
juniIgmpInterfaceImmediateLeave = _JuniIgmpInterfaceImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 1, 1, 1, 3),
    _JuniIgmpInterfaceImmediateLeave_Type()
)
juniIgmpInterfaceImmediateLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIgmpInterfaceImmediateLeave.setStatus("current")
_JuniIgmpInterfaceAccessGroup_Type = DisplayString
_JuniIgmpInterfaceAccessGroup_Object = MibTableColumn
juniIgmpInterfaceAccessGroup = _JuniIgmpInterfaceAccessGroup_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 1, 1, 1, 4),
    _JuniIgmpInterfaceAccessGroup_Type()
)
juniIgmpInterfaceAccessGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIgmpInterfaceAccessGroup.setStatus("current")
_JuniIgmpInterfacePromiscuous_Type = TruthValue
_JuniIgmpInterfacePromiscuous_Object = MibTableColumn
juniIgmpInterfacePromiscuous = _JuniIgmpInterfacePromiscuous_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 1, 1, 1, 5),
    _JuniIgmpInterfacePromiscuous_Type()
)
juniIgmpInterfacePromiscuous.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIgmpInterfacePromiscuous.setStatus("current")


class _JuniIgmpInterfaceMaxGroups_Type(Integer32):
    """Custom type juniIgmpInterfaceMaxGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_JuniIgmpInterfaceMaxGroups_Type.__name__ = "Integer32"
_JuniIgmpInterfaceMaxGroups_Object = MibTableColumn
juniIgmpInterfaceMaxGroups = _JuniIgmpInterfaceMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 1, 1, 1, 6),
    _JuniIgmpInterfaceMaxGroups_Type()
)
juniIgmpInterfaceMaxGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIgmpInterfaceMaxGroups.setStatus("current")
_JuniIgmpInterfaceIoaPacketReplIfIndex_Type = InterfaceIndex
_JuniIgmpInterfaceIoaPacketReplIfIndex_Object = MibTableColumn
juniIgmpInterfaceIoaPacketReplIfIndex = _JuniIgmpInterfaceIoaPacketReplIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 1, 1, 1, 7),
    _JuniIgmpInterfaceIoaPacketReplIfIndex_Type()
)
juniIgmpInterfaceIoaPacketReplIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIgmpInterfaceIoaPacketReplIfIndex.setStatus("current")
_JuniIgmpRouterPromiscuous_Type = TruthValue
_JuniIgmpRouterPromiscuous_Object = MibScalar
juniIgmpRouterPromiscuous = _JuniIgmpRouterPromiscuous_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 1, 2),
    _JuniIgmpRouterPromiscuous_Type()
)
juniIgmpRouterPromiscuous.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIgmpRouterPromiscuous.setStatus("current")


class _JuniIgmpAdminState_Type(Integer32):
    """Custom type juniIgmpAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_JuniIgmpAdminState_Type.__name__ = "Integer32"
_JuniIgmpAdminState_Object = MibScalar
juniIgmpAdminState = _JuniIgmpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 1, 3),
    _JuniIgmpAdminState_Type()
)
juniIgmpAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIgmpAdminState.setStatus("current")
_JuniIgmpProxy_ObjectIdentity = ObjectIdentity
juniIgmpProxy = _JuniIgmpProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2)
)
_JuniIgmpProxyInterfaceTable_Object = MibTable
juniIgmpProxyInterfaceTable = _JuniIgmpProxyInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1)
)
if mibBuilder.loadTexts:
    juniIgmpProxyInterfaceTable.setStatus("current")
_JuniIgmpProxyInterfaceEntry_Object = MibTableRow
juniIgmpProxyInterfaceEntry = _JuniIgmpProxyInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1)
)
juniIgmpProxyInterfaceEntry.setIndexNames(
    (0, "Juniper-IGMP-MIB", "juniIgmpProxyInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    juniIgmpProxyInterfaceEntry.setStatus("current")
_JuniIgmpProxyInterfaceIfIndex_Type = InterfaceIndex
_JuniIgmpProxyInterfaceIfIndex_Object = MibTableColumn
juniIgmpProxyInterfaceIfIndex = _JuniIgmpProxyInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 1),
    _JuniIgmpProxyInterfaceIfIndex_Type()
)
juniIgmpProxyInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIgmpProxyInterfaceIfIndex.setStatus("current")
_JuniIgmpProxyInterfaceAddress_Type = IpAddress
_JuniIgmpProxyInterfaceAddress_Object = MibTableColumn
juniIgmpProxyInterfaceAddress = _JuniIgmpProxyInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 2),
    _JuniIgmpProxyInterfaceAddress_Type()
)
juniIgmpProxyInterfaceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIgmpProxyInterfaceAddress.setStatus("current")
_JuniIgmpProxyInterfaceMask_Type = IpAddress
_JuniIgmpProxyInterfaceMask_Object = MibTableColumn
juniIgmpProxyInterfaceMask = _JuniIgmpProxyInterfaceMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 3),
    _JuniIgmpProxyInterfaceMask_Type()
)
juniIgmpProxyInterfaceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIgmpProxyInterfaceMask.setStatus("current")
_JuniIgmpProxyInterfaceState_Type = JuniIgmpProxyInterfaceState
_JuniIgmpProxyInterfaceState_Object = MibTableColumn
juniIgmpProxyInterfaceState = _JuniIgmpProxyInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 4),
    _JuniIgmpProxyInterfaceState_Type()
)
juniIgmpProxyInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIgmpProxyInterfaceState.setStatus("current")
_JuniIgmpProxyInterfaceStatus_Type = RowStatus
_JuniIgmpProxyInterfaceStatus_Object = MibTableColumn
juniIgmpProxyInterfaceStatus = _JuniIgmpProxyInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 5),
    _JuniIgmpProxyInterfaceStatus_Type()
)
juniIgmpProxyInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIgmpProxyInterfaceStatus.setStatus("current")
_JuniIgmpProxyInterfaceVersion_Type = Integer32
_JuniIgmpProxyInterfaceVersion_Object = MibTableColumn
juniIgmpProxyInterfaceVersion = _JuniIgmpProxyInterfaceVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 6),
    _JuniIgmpProxyInterfaceVersion_Type()
)
juniIgmpProxyInterfaceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIgmpProxyInterfaceVersion.setStatus("current")


class _JuniIgmpProxyInterfaceV1RoutePresentTimeout_Type(Integer32):
    """Custom type juniIgmpProxyInterfaceV1RoutePresentTimeout based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_JuniIgmpProxyInterfaceV1RoutePresentTimeout_Type.__name__ = "Integer32"
_JuniIgmpProxyInterfaceV1RoutePresentTimeout_Object = MibTableColumn
juniIgmpProxyInterfaceV1RoutePresentTimeout = _JuniIgmpProxyInterfaceV1RoutePresentTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 7),
    _JuniIgmpProxyInterfaceV1RoutePresentTimeout_Type()
)
juniIgmpProxyInterfaceV1RoutePresentTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIgmpProxyInterfaceV1RoutePresentTimeout.setStatus("current")
if mibBuilder.loadTexts:
    juniIgmpProxyInterfaceV1RoutePresentTimeout.setUnits("seconds")


class _JuniIgmpProxyInterfaceUnsolicitedReportInterval_Type(Integer32):
    """Custom type juniIgmpProxyInterfaceUnsolicitedReportInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_JuniIgmpProxyInterfaceUnsolicitedReportInterval_Type.__name__ = "Integer32"
_JuniIgmpProxyInterfaceUnsolicitedReportInterval_Object = MibTableColumn
juniIgmpProxyInterfaceUnsolicitedReportInterval = _JuniIgmpProxyInterfaceUnsolicitedReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 8),
    _JuniIgmpProxyInterfaceUnsolicitedReportInterval_Type()
)
juniIgmpProxyInterfaceUnsolicitedReportInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIgmpProxyInterfaceUnsolicitedReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniIgmpProxyInterfaceUnsolicitedReportInterval.setUnits("seconds")
_JuniIgmpProxyInterfaceTotalGroupCount_Type = Counter32
_JuniIgmpProxyInterfaceTotalGroupCount_Object = MibTableColumn
juniIgmpProxyInterfaceTotalGroupCount = _JuniIgmpProxyInterfaceTotalGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 9),
    _JuniIgmpProxyInterfaceTotalGroupCount_Type()
)
juniIgmpProxyInterfaceTotalGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIgmpProxyInterfaceTotalGroupCount.setStatus("current")
_JuniIgmpProxyInterfaceWrongVersionCount_Type = Counter32
_JuniIgmpProxyInterfaceWrongVersionCount_Object = MibTableColumn
juniIgmpProxyInterfaceWrongVersionCount = _JuniIgmpProxyInterfaceWrongVersionCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 10),
    _JuniIgmpProxyInterfaceWrongVersionCount_Type()
)
juniIgmpProxyInterfaceWrongVersionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIgmpProxyInterfaceWrongVersionCount.setStatus("current")
_JuniIgmpProxyInterfaceV1QueryReceiveCount_Type = Counter32
_JuniIgmpProxyInterfaceV1QueryReceiveCount_Object = MibTableColumn
juniIgmpProxyInterfaceV1QueryReceiveCount = _JuniIgmpProxyInterfaceV1QueryReceiveCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 11),
    _JuniIgmpProxyInterfaceV1QueryReceiveCount_Type()
)
juniIgmpProxyInterfaceV1QueryReceiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIgmpProxyInterfaceV1QueryReceiveCount.setStatus("current")
_JuniIgmpProxyInterfaceV2QueryReceiveCount_Type = Counter32
_JuniIgmpProxyInterfaceV2QueryReceiveCount_Object = MibTableColumn
juniIgmpProxyInterfaceV2QueryReceiveCount = _JuniIgmpProxyInterfaceV2QueryReceiveCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 12),
    _JuniIgmpProxyInterfaceV2QueryReceiveCount_Type()
)
juniIgmpProxyInterfaceV2QueryReceiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIgmpProxyInterfaceV2QueryReceiveCount.setStatus("current")
_JuniIgmpProxyInterfaceV1ReportReceiveCount_Type = Counter32
_JuniIgmpProxyInterfaceV1ReportReceiveCount_Object = MibTableColumn
juniIgmpProxyInterfaceV1ReportReceiveCount = _JuniIgmpProxyInterfaceV1ReportReceiveCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 13),
    _JuniIgmpProxyInterfaceV1ReportReceiveCount_Type()
)
juniIgmpProxyInterfaceV1ReportReceiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIgmpProxyInterfaceV1ReportReceiveCount.setStatus("current")
_JuniIgmpProxyInterfaceV2ReportReceiveCount_Type = Counter32
_JuniIgmpProxyInterfaceV2ReportReceiveCount_Object = MibTableColumn
juniIgmpProxyInterfaceV2ReportReceiveCount = _JuniIgmpProxyInterfaceV2ReportReceiveCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 14),
    _JuniIgmpProxyInterfaceV2ReportReceiveCount_Type()
)
juniIgmpProxyInterfaceV2ReportReceiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIgmpProxyInterfaceV2ReportReceiveCount.setStatus("current")
_JuniIgmpProxyInterfaceV1JoinReportCount_Type = Counter32
_JuniIgmpProxyInterfaceV1JoinReportCount_Object = MibTableColumn
juniIgmpProxyInterfaceV1JoinReportCount = _JuniIgmpProxyInterfaceV1JoinReportCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 15),
    _JuniIgmpProxyInterfaceV1JoinReportCount_Type()
)
juniIgmpProxyInterfaceV1JoinReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIgmpProxyInterfaceV1JoinReportCount.setStatus("current")
_JuniIgmpProxyInterfaceV2JoinReportCount_Type = Counter32
_JuniIgmpProxyInterfaceV2JoinReportCount_Object = MibTableColumn
juniIgmpProxyInterfaceV2JoinReportCount = _JuniIgmpProxyInterfaceV2JoinReportCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 16),
    _JuniIgmpProxyInterfaceV2JoinReportCount_Type()
)
juniIgmpProxyInterfaceV2JoinReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIgmpProxyInterfaceV2JoinReportCount.setStatus("current")
_JuniIgmpProxyInterfaceLeaveReportCount_Type = Counter32
_JuniIgmpProxyInterfaceLeaveReportCount_Object = MibTableColumn
juniIgmpProxyInterfaceLeaveReportCount = _JuniIgmpProxyInterfaceLeaveReportCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 1, 1, 17),
    _JuniIgmpProxyInterfaceLeaveReportCount_Type()
)
juniIgmpProxyInterfaceLeaveReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIgmpProxyInterfaceLeaveReportCount.setStatus("current")
_JuniIgmpProxyCacheTable_Object = MibTable
juniIgmpProxyCacheTable = _JuniIgmpProxyCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 2)
)
if mibBuilder.loadTexts:
    juniIgmpProxyCacheTable.setStatus("current")
_JuniIgmpProxyCacheEntry_Object = MibTableRow
juniIgmpProxyCacheEntry = _JuniIgmpProxyCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 2, 1)
)
juniIgmpProxyCacheEntry.setIndexNames(
    (0, "Juniper-IGMP-MIB", "juniIgmpProxyIfIndex"),
    (0, "Juniper-IGMP-MIB", "juniIgmpProxyAddress"),
)
if mibBuilder.loadTexts:
    juniIgmpProxyCacheEntry.setStatus("current")
_JuniIgmpProxyIfIndex_Type = InterfaceIndex
_JuniIgmpProxyIfIndex_Object = MibTableColumn
juniIgmpProxyIfIndex = _JuniIgmpProxyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 2, 1, 1),
    _JuniIgmpProxyIfIndex_Type()
)
juniIgmpProxyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIgmpProxyIfIndex.setStatus("current")
_JuniIgmpProxyAddress_Type = IpAddress
_JuniIgmpProxyAddress_Object = MibTableColumn
juniIgmpProxyAddress = _JuniIgmpProxyAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 2, 1, 2),
    _JuniIgmpProxyAddress_Type()
)
juniIgmpProxyAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIgmpProxyAddress.setStatus("current")
_JuniIgmpProxyStatus_Type = JuniIgmpProxyGroupState
_JuniIgmpProxyStatus_Object = MibTableColumn
juniIgmpProxyStatus = _JuniIgmpProxyStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 2, 2, 1, 3),
    _JuniIgmpProxyStatus_Type()
)
juniIgmpProxyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIgmpProxyStatus.setStatus("current")
_JuniIgmpGlobal_ObjectIdentity = ObjectIdentity
juniIgmpGlobal = _JuniIgmpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 3)
)
_JuniIgmpGroupsTable_Object = MibTable
juniIgmpGroupsTable = _JuniIgmpGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 3, 1)
)
if mibBuilder.loadTexts:
    juniIgmpGroupsTable.setStatus("deprecated")
_JuniIgmpGroupsEntry_Object = MibTableRow
juniIgmpGroupsEntry = _JuniIgmpGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 3, 1, 1)
)
juniIgmpGroupsEntry.setIndexNames(
    (0, "Juniper-IGMP-MIB", "juniIgmpGroupsSlot"),
    (0, "Juniper-IGMP-MIB", "juniIgmpGroupsPort"),
)
if mibBuilder.loadTexts:
    juniIgmpGroupsEntry.setStatus("deprecated")


class _JuniIgmpGroupsSlot_Type(Integer32):
    """Custom type juniIgmpGroupsSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniIgmpGroupsSlot_Type.__name__ = "Integer32"
_JuniIgmpGroupsSlot_Object = MibTableColumn
juniIgmpGroupsSlot = _JuniIgmpGroupsSlot_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 3, 1, 1, 1),
    _JuniIgmpGroupsSlot_Type()
)
juniIgmpGroupsSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIgmpGroupsSlot.setStatus("deprecated")


class _JuniIgmpGroupsPort_Type(Integer32):
    """Custom type juniIgmpGroupsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniIgmpGroupsPort_Type.__name__ = "Integer32"
_JuniIgmpGroupsPort_Object = MibTableColumn
juniIgmpGroupsPort = _JuniIgmpGroupsPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 3, 1, 1, 2),
    _JuniIgmpGroupsPort_Type()
)
juniIgmpGroupsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIgmpGroupsPort.setStatus("deprecated")


class _JuniIgmpGroupsMaxGroups_Type(Integer32):
    """Custom type juniIgmpGroupsMaxGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_JuniIgmpGroupsMaxGroups_Type.__name__ = "Integer32"
_JuniIgmpGroupsMaxGroups_Object = MibTableColumn
juniIgmpGroupsMaxGroups = _JuniIgmpGroupsMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 3, 1, 1, 3),
    _JuniIgmpGroupsMaxGroups_Type()
)
juniIgmpGroupsMaxGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIgmpGroupsMaxGroups.setStatus("deprecated")
_JuniIgmpIfLocationType_Type = JuniInterfaceLocationType
_JuniIgmpIfLocationType_Object = MibScalar
juniIgmpIfLocationType = _JuniIgmpIfLocationType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 3, 2),
    _JuniIgmpIfLocationType_Type()
)
juniIgmpIfLocationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIgmpIfLocationType.setStatus("current")
_JuniIgmpGroupsTable2_Object = MibTable
juniIgmpGroupsTable2 = _JuniIgmpGroupsTable2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 3, 3)
)
if mibBuilder.loadTexts:
    juniIgmpGroupsTable2.setStatus("current")
_JuniIgmpGroupsEntry2_Object = MibTableRow
juniIgmpGroupsEntry2 = _JuniIgmpGroupsEntry2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 3, 3, 1)
)
juniIgmpGroupsEntry2.setIndexNames(
    (0, "Juniper-IGMP-MIB", "juniIgmpIfLocationIndex"),
)
if mibBuilder.loadTexts:
    juniIgmpGroupsEntry2.setStatus("current")
_JuniIgmpIfLocationIndex_Type = JuniInterfaceLocationValue
_JuniIgmpIfLocationIndex_Object = MibTableColumn
juniIgmpIfLocationIndex = _JuniIgmpIfLocationIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 3, 3, 1, 1),
    _JuniIgmpIfLocationIndex_Type()
)
juniIgmpIfLocationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIgmpIfLocationIndex.setStatus("current")


class _JuniIgmpGroupsMaxGroups2_Type(Integer32):
    """Custom type juniIgmpGroupsMaxGroups2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_JuniIgmpGroupsMaxGroups2_Type.__name__ = "Integer32"
_JuniIgmpGroupsMaxGroups2_Object = MibTableColumn
juniIgmpGroupsMaxGroups2 = _JuniIgmpGroupsMaxGroups2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 1, 3, 3, 1, 2),
    _JuniIgmpGroupsMaxGroups2_Type()
)
juniIgmpGroupsMaxGroups2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniIgmpGroupsMaxGroups2.setStatus("current")
_JuniIgmpConformance_ObjectIdentity = ObjectIdentity
juniIgmpConformance = _JuniIgmpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4)
)
_JuniIgmpCompliances_ObjectIdentity = ObjectIdentity
juniIgmpCompliances = _JuniIgmpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 1)
)
_JuniIgmpGroups_ObjectIdentity = ObjectIdentity
juniIgmpGroups = _JuniIgmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 2)
)

# Managed Objects groups

juniIgmpProxyInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 2, 1)
)
juniIgmpProxyInterfaceGroup.setObjects(
      *(("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceAddress"),
        ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceMask"),
        ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceState"),
        ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceStatus"),
        ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceVersion"),
        ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceV1RoutePresentTimeout"),
        ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceUnsolicitedReportInterval"),
        ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceTotalGroupCount"),
        ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceWrongVersionCount"),
        ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceV1QueryReceiveCount"),
        ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceV2QueryReceiveCount"),
        ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceV1ReportReceiveCount"),
        ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceV2ReportReceiveCount"),
        ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceV1JoinReportCount"),
        ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceV2JoinReportCount"),
        ("Juniper-IGMP-MIB", "juniIgmpProxyInterfaceLeaveReportCount"))
)
if mibBuilder.loadTexts:
    juniIgmpProxyInterfaceGroup.setStatus("current")

juniIgmpProxyCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 2, 2)
)
juniIgmpProxyCacheGroup.setObjects(
    ("Juniper-IGMP-MIB", "juniIgmpProxyStatus")
)
if mibBuilder.loadTexts:
    juniIgmpProxyCacheGroup.setStatus("current")

juniIgmpInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 2, 3)
)
juniIgmpInterfaceGroup.setObjects(
      *(("Juniper-IGMP-MIB", "juniIgmpInterfaceQuerierTimeout"),
        ("Juniper-IGMP-MIB", "juniIgmpInterfaceImmediateLeave"),
        ("Juniper-IGMP-MIB", "juniIgmpInterfaceAccessGroup"),
        ("Juniper-IGMP-MIB", "juniIgmpInterfacePromiscuous"),
        ("Juniper-IGMP-MIB", "juniIgmpInterfaceMaxGroups"),
        ("Juniper-IGMP-MIB", "juniIgmpRouterPromiscuous"))
)
if mibBuilder.loadTexts:
    juniIgmpInterfaceGroup.setStatus("obsolete")

juniIgmpGroupsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 2, 4)
)
juniIgmpGroupsGroup.setObjects(
    ("Juniper-IGMP-MIB", "juniIgmpGroupsMaxGroups")
)
if mibBuilder.loadTexts:
    juniIgmpGroupsGroup.setStatus("deprecated")

juniIgmpInterfaceGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 2, 5)
)
juniIgmpInterfaceGroup2.setObjects(
      *(("Juniper-IGMP-MIB", "juniIgmpInterfaceQuerierTimeout"),
        ("Juniper-IGMP-MIB", "juniIgmpInterfaceImmediateLeave"),
        ("Juniper-IGMP-MIB", "juniIgmpInterfaceAccessGroup"),
        ("Juniper-IGMP-MIB", "juniIgmpInterfacePromiscuous"),
        ("Juniper-IGMP-MIB", "juniIgmpInterfaceMaxGroups"),
        ("Juniper-IGMP-MIB", "juniIgmpRouterPromiscuous"),
        ("Juniper-IGMP-MIB", "juniIgmpAdminState"))
)
if mibBuilder.loadTexts:
    juniIgmpInterfaceGroup2.setStatus("current")

juniIgmpGroupsGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 2, 6)
)
juniIgmpGroupsGroup2.setObjects(
      *(("Juniper-IGMP-MIB", "juniIgmpIfLocationType"),
        ("Juniper-IGMP-MIB", "juniIgmpGroupsMaxGroups2"))
)
if mibBuilder.loadTexts:
    juniIgmpGroupsGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniIgmpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniIgmpCompliance.setStatus(
        "obsolete"
    )

juniIgmpCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniIgmpCompliance2.setStatus(
        "obsolete"
    )

juniIgmpCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 1, 3)
)
if mibBuilder.loadTexts:
    juniIgmpCompliance3.setStatus(
        "deprecated"
    )

juniIgmpCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40, 4, 1, 4)
)
if mibBuilder.loadTexts:
    juniIgmpCompliance4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-IGMP-MIB",
    **{"JuniIgmpProxyGroupState": JuniIgmpProxyGroupState,
       "JuniIgmpProxyInterfaceState": JuniIgmpProxyInterfaceState,
       "juniIgmpMIB": juniIgmpMIB,
       "juniIgmpMIBObject": juniIgmpMIBObject,
       "juniIgmpProtocol": juniIgmpProtocol,
       "juniIgmpInterfaceTable": juniIgmpInterfaceTable,
       "juniIgmpInterfaceEntry": juniIgmpInterfaceEntry,
       "juniIgmpInterfaceIfIndex": juniIgmpInterfaceIfIndex,
       "juniIgmpInterfaceQuerierTimeout": juniIgmpInterfaceQuerierTimeout,
       "juniIgmpInterfaceImmediateLeave": juniIgmpInterfaceImmediateLeave,
       "juniIgmpInterfaceAccessGroup": juniIgmpInterfaceAccessGroup,
       "juniIgmpInterfacePromiscuous": juniIgmpInterfacePromiscuous,
       "juniIgmpInterfaceMaxGroups": juniIgmpInterfaceMaxGroups,
       "juniIgmpInterfaceIoaPacketReplIfIndex": juniIgmpInterfaceIoaPacketReplIfIndex,
       "juniIgmpRouterPromiscuous": juniIgmpRouterPromiscuous,
       "juniIgmpAdminState": juniIgmpAdminState,
       "juniIgmpProxy": juniIgmpProxy,
       "juniIgmpProxyInterfaceTable": juniIgmpProxyInterfaceTable,
       "juniIgmpProxyInterfaceEntry": juniIgmpProxyInterfaceEntry,
       "juniIgmpProxyInterfaceIfIndex": juniIgmpProxyInterfaceIfIndex,
       "juniIgmpProxyInterfaceAddress": juniIgmpProxyInterfaceAddress,
       "juniIgmpProxyInterfaceMask": juniIgmpProxyInterfaceMask,
       "juniIgmpProxyInterfaceState": juniIgmpProxyInterfaceState,
       "juniIgmpProxyInterfaceStatus": juniIgmpProxyInterfaceStatus,
       "juniIgmpProxyInterfaceVersion": juniIgmpProxyInterfaceVersion,
       "juniIgmpProxyInterfaceV1RoutePresentTimeout": juniIgmpProxyInterfaceV1RoutePresentTimeout,
       "juniIgmpProxyInterfaceUnsolicitedReportInterval": juniIgmpProxyInterfaceUnsolicitedReportInterval,
       "juniIgmpProxyInterfaceTotalGroupCount": juniIgmpProxyInterfaceTotalGroupCount,
       "juniIgmpProxyInterfaceWrongVersionCount": juniIgmpProxyInterfaceWrongVersionCount,
       "juniIgmpProxyInterfaceV1QueryReceiveCount": juniIgmpProxyInterfaceV1QueryReceiveCount,
       "juniIgmpProxyInterfaceV2QueryReceiveCount": juniIgmpProxyInterfaceV2QueryReceiveCount,
       "juniIgmpProxyInterfaceV1ReportReceiveCount": juniIgmpProxyInterfaceV1ReportReceiveCount,
       "juniIgmpProxyInterfaceV2ReportReceiveCount": juniIgmpProxyInterfaceV2ReportReceiveCount,
       "juniIgmpProxyInterfaceV1JoinReportCount": juniIgmpProxyInterfaceV1JoinReportCount,
       "juniIgmpProxyInterfaceV2JoinReportCount": juniIgmpProxyInterfaceV2JoinReportCount,
       "juniIgmpProxyInterfaceLeaveReportCount": juniIgmpProxyInterfaceLeaveReportCount,
       "juniIgmpProxyCacheTable": juniIgmpProxyCacheTable,
       "juniIgmpProxyCacheEntry": juniIgmpProxyCacheEntry,
       "juniIgmpProxyIfIndex": juniIgmpProxyIfIndex,
       "juniIgmpProxyAddress": juniIgmpProxyAddress,
       "juniIgmpProxyStatus": juniIgmpProxyStatus,
       "juniIgmpGlobal": juniIgmpGlobal,
       "juniIgmpGroupsTable": juniIgmpGroupsTable,
       "juniIgmpGroupsEntry": juniIgmpGroupsEntry,
       "juniIgmpGroupsSlot": juniIgmpGroupsSlot,
       "juniIgmpGroupsPort": juniIgmpGroupsPort,
       "juniIgmpGroupsMaxGroups": juniIgmpGroupsMaxGroups,
       "juniIgmpIfLocationType": juniIgmpIfLocationType,
       "juniIgmpGroupsTable2": juniIgmpGroupsTable2,
       "juniIgmpGroupsEntry2": juniIgmpGroupsEntry2,
       "juniIgmpIfLocationIndex": juniIgmpIfLocationIndex,
       "juniIgmpGroupsMaxGroups2": juniIgmpGroupsMaxGroups2,
       "juniIgmpConformance": juniIgmpConformance,
       "juniIgmpCompliances": juniIgmpCompliances,
       "juniIgmpCompliance": juniIgmpCompliance,
       "juniIgmpCompliance2": juniIgmpCompliance2,
       "juniIgmpCompliance3": juniIgmpCompliance3,
       "juniIgmpCompliance4": juniIgmpCompliance4,
       "juniIgmpGroups": juniIgmpGroups,
       "juniIgmpProxyInterfaceGroup": juniIgmpProxyInterfaceGroup,
       "juniIgmpProxyCacheGroup": juniIgmpProxyCacheGroup,
       "juniIgmpInterfaceGroup": juniIgmpInterfaceGroup,
       "juniIgmpGroupsGroup": juniIgmpGroupsGroup,
       "juniIgmpInterfaceGroup2": juniIgmpInterfaceGroup2,
       "juniIgmpGroupsGroup2": juniIgmpGroupsGroup2}
)
