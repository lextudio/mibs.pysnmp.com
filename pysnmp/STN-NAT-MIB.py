# SNMP MIB module (STN-NAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STN-NAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:10 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(stnNotification,) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-SMI",
    "stnNotification")

(stnRouterNAT,) = mibBuilder.importSymbols(
    "STN-ROUTER-MIB",
    "stnRouterNAT")


# MODULE-IDENTITY

stnNat = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NatTransMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pat", 3),
          ("pooled", 1),
          ("static", 2))
    )



# MIB Managed Objects in the order of their OIDs

_StnNatObjects_ObjectIdentity = ObjectIdentity
stnNatObjects = _StnNatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1)
)
_StnNatL2Table_Object = MibTable
stnNatL2Table = _StnNatL2Table_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    stnNatL2Table.setStatus("current")
_StnNatL2Entry_Object = MibTableRow
stnNatL2Entry = _StnNatL2Entry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 1, 1)
)
stnNatL2Entry.setIndexNames(
    (0, "STN-NAT-MIB", "stnNatL2IfIndex"),
)
if mibBuilder.loadTexts:
    stnNatL2Entry.setStatus("current")
_StnNatL2IfIndex_Type = InterfaceIndex
_StnNatL2IfIndex_Object = MibTableColumn
stnNatL2IfIndex = _StnNatL2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 1, 1, 1),
    _StnNatL2IfIndex_Type()
)
stnNatL2IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatL2IfIndex.setStatus("current")
_StnNatL2InsidePktMisses_Type = Integer32
_StnNatL2InsidePktMisses_Object = MibTableColumn
stnNatL2InsidePktMisses = _StnNatL2InsidePktMisses_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 1, 1, 2),
    _StnNatL2InsidePktMisses_Type()
)
stnNatL2InsidePktMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatL2InsidePktMisses.setStatus("current")
_StnNatL2InsidePktHits_Type = Integer32
_StnNatL2InsidePktHits_Object = MibTableColumn
stnNatL2InsidePktHits = _StnNatL2InsidePktHits_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 1, 1, 3),
    _StnNatL2InsidePktHits_Type()
)
stnNatL2InsidePktHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatL2InsidePktHits.setStatus("current")
_StnNatL2OutsidePktMisses_Type = Integer32
_StnNatL2OutsidePktMisses_Object = MibTableColumn
stnNatL2OutsidePktMisses = _StnNatL2OutsidePktMisses_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 1, 1, 4),
    _StnNatL2OutsidePktMisses_Type()
)
stnNatL2OutsidePktMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatL2OutsidePktMisses.setStatus("current")
_StnNatL2OutsidePktHits_Type = Integer32
_StnNatL2OutsidePktHits_Object = MibTableColumn
stnNatL2OutsidePktHits = _StnNatL2OutsidePktHits_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 1, 1, 5),
    _StnNatL2OutsidePktHits_Type()
)
stnNatL2OutsidePktHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatL2OutsidePktHits.setStatus("current")
_StnNatL2UntransInsidePkts_Type = Integer32
_StnNatL2UntransInsidePkts_Object = MibTableColumn
stnNatL2UntransInsidePkts = _StnNatL2UntransInsidePkts_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 1, 1, 6),
    _StnNatL2UntransInsidePkts_Type()
)
stnNatL2UntransInsidePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatL2UntransInsidePkts.setStatus("current")
_StnNatL2UntransOutsidePkts_Type = Integer32
_StnNatL2UntransOutsidePkts_Object = MibTableColumn
stnNatL2UntransOutsidePkts = _StnNatL2UntransOutsidePkts_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 1, 1, 7),
    _StnNatL2UntransOutsidePkts_Type()
)
stnNatL2UntransOutsidePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatL2UntransOutsidePkts.setStatus("current")
_StnNatL2InsideAlgPkts_Type = Integer32
_StnNatL2InsideAlgPkts_Object = MibTableColumn
stnNatL2InsideAlgPkts = _StnNatL2InsideAlgPkts_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 1, 1, 8),
    _StnNatL2InsideAlgPkts_Type()
)
stnNatL2InsideAlgPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatL2InsideAlgPkts.setStatus("current")
_StnNatL2OutsideAlgPkts_Type = Integer32
_StnNatL2OutsideAlgPkts_Object = MibTableColumn
stnNatL2OutsideAlgPkts = _StnNatL2OutsideAlgPkts_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 1, 1, 9),
    _StnNatL2OutsideAlgPkts_Type()
)
stnNatL2OutsideAlgPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatL2OutsideAlgPkts.setStatus("current")
_StnNatL2FlowId_Type = Integer32
_StnNatL2FlowId_Object = MibTableColumn
stnNatL2FlowId = _StnNatL2FlowId_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 1, 1, 10),
    _StnNatL2FlowId_Type()
)
stnNatL2FlowId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatL2FlowId.setStatus("current")
_StnNatGroupTable_Object = MibTable
stnNatGroupTable = _StnNatGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    stnNatGroupTable.setStatus("current")
_StnNatGroupEntry_Object = MibTableRow
stnNatGroupEntry = _StnNatGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1)
)
stnNatGroupEntry.setIndexNames(
    (0, "STN-NAT-MIB", "stnNatGroupSubnetIfInstance"),
    (0, "STN-NAT-MIB", "stnNatGroupOutsideBaseAddress"),
)
if mibBuilder.loadTexts:
    stnNatGroupEntry.setStatus("current")
_StnNatGroupSubnetIfInstance_Type = Integer32
_StnNatGroupSubnetIfInstance_Object = MibTableColumn
stnNatGroupSubnetIfInstance = _StnNatGroupSubnetIfInstance_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 1),
    _StnNatGroupSubnetIfInstance_Type()
)
stnNatGroupSubnetIfInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupSubnetIfInstance.setStatus("current")
_StnNatGroupOutsideBaseAddress_Type = IpAddress
_StnNatGroupOutsideBaseAddress_Object = MibTableColumn
stnNatGroupOutsideBaseAddress = _StnNatGroupOutsideBaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 2),
    _StnNatGroupOutsideBaseAddress_Type()
)
stnNatGroupOutsideBaseAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupOutsideBaseAddress.setStatus("current")
_StnNatGroupOutsideEndAddress_Type = IpAddress
_StnNatGroupOutsideEndAddress_Object = MibTableColumn
stnNatGroupOutsideEndAddress = _StnNatGroupOutsideEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 3),
    _StnNatGroupOutsideEndAddress_Type()
)
stnNatGroupOutsideEndAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupOutsideEndAddress.setStatus("current")
_StnNatGroupInsideBaseAddress_Type = IpAddress
_StnNatGroupInsideBaseAddress_Object = MibTableColumn
stnNatGroupInsideBaseAddress = _StnNatGroupInsideBaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 4),
    _StnNatGroupInsideBaseAddress_Type()
)
stnNatGroupInsideBaseAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupInsideBaseAddress.setStatus("current")
_StnNatGroupInsideEndAddress_Type = IpAddress
_StnNatGroupInsideEndAddress_Object = MibTableColumn
stnNatGroupInsideEndAddress = _StnNatGroupInsideEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 5),
    _StnNatGroupInsideEndAddress_Type()
)
stnNatGroupInsideEndAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupInsideEndAddress.setStatus("current")
_StnNatGroupTransMode_Type = NatTransMode
_StnNatGroupTransMode_Object = MibTableColumn
stnNatGroupTransMode = _StnNatGroupTransMode_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 6),
    _StnNatGroupTransMode_Type()
)
stnNatGroupTransMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupTransMode.setStatus("current")
_StnNatGroupAddrIdleTime_Type = Integer32
_StnNatGroupAddrIdleTime_Object = MibTableColumn
stnNatGroupAddrIdleTime = _StnNatGroupAddrIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 7),
    _StnNatGroupAddrIdleTime_Type()
)
stnNatGroupAddrIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupAddrIdleTime.setStatus("current")
_StnNatGroupAddrTransAvailable_Type = Integer32
_StnNatGroupAddrTransAvailable_Object = MibTableColumn
stnNatGroupAddrTransAvailable = _StnNatGroupAddrTransAvailable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 8),
    _StnNatGroupAddrTransAvailable_Type()
)
stnNatGroupAddrTransAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupAddrTransAvailable.setStatus("current")
_StnNatGroupMaxFtpSessions_Type = Integer32
_StnNatGroupMaxFtpSessions_Object = MibTableColumn
stnNatGroupMaxFtpSessions = _StnNatGroupMaxFtpSessions_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 9),
    _StnNatGroupMaxFtpSessions_Type()
)
stnNatGroupMaxFtpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupMaxFtpSessions.setStatus("current")
_StnNatGroupMaxFtpSessionsPerInsideAddr_Type = Integer32
_StnNatGroupMaxFtpSessionsPerInsideAddr_Object = MibTableColumn
stnNatGroupMaxFtpSessionsPerInsideAddr = _StnNatGroupMaxFtpSessionsPerInsideAddr_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 10),
    _StnNatGroupMaxFtpSessionsPerInsideAddr_Type()
)
stnNatGroupMaxFtpSessionsPerInsideAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupMaxFtpSessionsPerInsideAddr.setStatus("current")
_StnNatGroupFtpControlSessionIdleTime_Type = Integer32
_StnNatGroupFtpControlSessionIdleTime_Object = MibTableColumn
stnNatGroupFtpControlSessionIdleTime = _StnNatGroupFtpControlSessionIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 11),
    _StnNatGroupFtpControlSessionIdleTime_Type()
)
stnNatGroupFtpControlSessionIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupFtpControlSessionIdleTime.setStatus("current")
_StnNatGroupCurrentFtpSessions_Type = Integer32
_StnNatGroupCurrentFtpSessions_Object = MibTableColumn
stnNatGroupCurrentFtpSessions = _StnNatGroupCurrentFtpSessions_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 12),
    _StnNatGroupCurrentFtpSessions_Type()
)
stnNatGroupCurrentFtpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupCurrentFtpSessions.setStatus("current")
_StnNatGroupTotalFtpSessions_Type = Integer32
_StnNatGroupTotalFtpSessions_Object = MibTableColumn
stnNatGroupTotalFtpSessions = _StnNatGroupTotalFtpSessions_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 13),
    _StnNatGroupTotalFtpSessions_Type()
)
stnNatGroupTotalFtpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupTotalFtpSessions.setStatus("current")
_StnNatGroupMissedFtpSessionLookups_Type = Integer32
_StnNatGroupMissedFtpSessionLookups_Object = MibTableColumn
stnNatGroupMissedFtpSessionLookups = _StnNatGroupMissedFtpSessionLookups_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 14),
    _StnNatGroupMissedFtpSessionLookups_Type()
)
stnNatGroupMissedFtpSessionLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupMissedFtpSessionLookups.setStatus("current")
_StnNatGroupNoIdleFtpSessions_Type = Integer32
_StnNatGroupNoIdleFtpSessions_Object = MibTableColumn
stnNatGroupNoIdleFtpSessions = _StnNatGroupNoIdleFtpSessions_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 15),
    _StnNatGroupNoIdleFtpSessions_Type()
)
stnNatGroupNoIdleFtpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupNoIdleFtpSessions.setStatus("current")
_StnNatGroupNoIdleOutsideAddrs_Type = Integer32
_StnNatGroupNoIdleOutsideAddrs_Object = MibTableColumn
stnNatGroupNoIdleOutsideAddrs = _StnNatGroupNoIdleOutsideAddrs_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 16),
    _StnNatGroupNoIdleOutsideAddrs_Type()
)
stnNatGroupNoIdleOutsideAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupNoIdleOutsideAddrs.setStatus("current")
_StnNatGroupFoundIdleOutsideAddrs_Type = Integer32
_StnNatGroupFoundIdleOutsideAddrs_Object = MibTableColumn
stnNatGroupFoundIdleOutsideAddrs = _StnNatGroupFoundIdleOutsideAddrs_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 17),
    _StnNatGroupFoundIdleOutsideAddrs_Type()
)
stnNatGroupFoundIdleOutsideAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupFoundIdleOutsideAddrs.setStatus("current")
_StnNatGroupInsidePktMisses_Type = Integer32
_StnNatGroupInsidePktMisses_Object = MibTableColumn
stnNatGroupInsidePktMisses = _StnNatGroupInsidePktMisses_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 18),
    _StnNatGroupInsidePktMisses_Type()
)
stnNatGroupInsidePktMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupInsidePktMisses.setStatus("current")
_StnNatGroupInsidePktHits_Type = Integer32
_StnNatGroupInsidePktHits_Object = MibTableColumn
stnNatGroupInsidePktHits = _StnNatGroupInsidePktHits_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 19),
    _StnNatGroupInsidePktHits_Type()
)
stnNatGroupInsidePktHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupInsidePktHits.setStatus("current")
_StnNatGroupOutsidePktMisses_Type = Integer32
_StnNatGroupOutsidePktMisses_Object = MibTableColumn
stnNatGroupOutsidePktMisses = _StnNatGroupOutsidePktMisses_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 20),
    _StnNatGroupOutsidePktMisses_Type()
)
stnNatGroupOutsidePktMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupOutsidePktMisses.setStatus("current")
_StnNatGroupOutsidePktHits_Type = Integer32
_StnNatGroupOutsidePktHits_Object = MibTableColumn
stnNatGroupOutsidePktHits = _StnNatGroupOutsidePktHits_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 21),
    _StnNatGroupOutsidePktHits_Type()
)
stnNatGroupOutsidePktHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupOutsidePktHits.setStatus("current")
_StnNatGroupInvalidOutsidePktMisses_Type = Integer32
_StnNatGroupInvalidOutsidePktMisses_Object = MibTableColumn
stnNatGroupInvalidOutsidePktMisses = _StnNatGroupInvalidOutsidePktMisses_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 22),
    _StnNatGroupInvalidOutsidePktMisses_Type()
)
stnNatGroupInvalidOutsidePktMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupInvalidOutsidePktMisses.setStatus("current")


class _StnNatGroupInsideFlowOrigin_Type(Integer32):
    """Custom type stnNatGroupInsideFlowOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egress", 2),
          ("ingress", 1))
    )


_StnNatGroupInsideFlowOrigin_Type.__name__ = "Integer32"
_StnNatGroupInsideFlowOrigin_Object = MibTableColumn
stnNatGroupInsideFlowOrigin = _StnNatGroupInsideFlowOrigin_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 23),
    _StnNatGroupInsideFlowOrigin_Type()
)
stnNatGroupInsideFlowOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupInsideFlowOrigin.setStatus("current")
_StnNatGroupPortBaseNumber_Type = Integer32
_StnNatGroupPortBaseNumber_Object = MibTableColumn
stnNatGroupPortBaseNumber = _StnNatGroupPortBaseNumber_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 24),
    _StnNatGroupPortBaseNumber_Type()
)
stnNatGroupPortBaseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupPortBaseNumber.setStatus("current")
_StnNatGroupPortEndNumber_Type = Integer32
_StnNatGroupPortEndNumber_Object = MibTableColumn
stnNatGroupPortEndNumber = _StnNatGroupPortEndNumber_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 25),
    _StnNatGroupPortEndNumber_Type()
)
stnNatGroupPortEndNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupPortEndNumber.setStatus("current")
_StnNatGroupMaxInsideAddrs_Type = Integer32
_StnNatGroupMaxInsideAddrs_Object = MibTableColumn
stnNatGroupMaxInsideAddrs = _StnNatGroupMaxInsideAddrs_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 26),
    _StnNatGroupMaxInsideAddrs_Type()
)
stnNatGroupMaxInsideAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupMaxInsideAddrs.setStatus("current")
_StnNatGroupMaxPortsPerInsideAddr_Type = Integer32
_StnNatGroupMaxPortsPerInsideAddr_Object = MibTableColumn
stnNatGroupMaxPortsPerInsideAddr = _StnNatGroupMaxPortsPerInsideAddr_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 27),
    _StnNatGroupMaxPortsPerInsideAddr_Type()
)
stnNatGroupMaxPortsPerInsideAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupMaxPortsPerInsideAddr.setStatus("current")
_StnNatGroupPortLimitReached_Type = Integer32
_StnNatGroupPortLimitReached_Object = MibTableColumn
stnNatGroupPortLimitReached = _StnNatGroupPortLimitReached_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 28),
    _StnNatGroupPortLimitReached_Type()
)
stnNatGroupPortLimitReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupPortLimitReached.setStatus("current")
_StnNatGroupInsideAddrLimitReached_Type = Integer32
_StnNatGroupInsideAddrLimitReached_Object = MibTableColumn
stnNatGroupInsideAddrLimitReached = _StnNatGroupInsideAddrLimitReached_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 2, 1, 29),
    _StnNatGroupInsideAddrLimitReached_Type()
)
stnNatGroupInsideAddrLimitReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatGroupInsideAddrLimitReached.setStatus("current")
_StnNatOutTransTable_Object = MibTable
stnNatOutTransTable = _StnNatOutTransTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 3)
)
if mibBuilder.loadTexts:
    stnNatOutTransTable.setStatus("current")
_StnNatOutTransEntry_Object = MibTableRow
stnNatOutTransEntry = _StnNatOutTransEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 3, 1)
)
stnNatOutTransEntry.setIndexNames(
    (0, "STN-NAT-MIB", "stnNatOutTransSubnetIfInstance"),
    (0, "STN-NAT-MIB", "stnNatOutTransOutsideBaseAddress"),
    (0, "STN-NAT-MIB", "stnNatOutTransOutsideAddress"),
    (0, "STN-NAT-MIB", "stnNatOutTransOutsidePortNumber"),
)
if mibBuilder.loadTexts:
    stnNatOutTransEntry.setStatus("current")
_StnNatOutTransSubnetIfInstance_Type = Integer32
_StnNatOutTransSubnetIfInstance_Object = MibTableColumn
stnNatOutTransSubnetIfInstance = _StnNatOutTransSubnetIfInstance_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 3, 1, 1),
    _StnNatOutTransSubnetIfInstance_Type()
)
stnNatOutTransSubnetIfInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatOutTransSubnetIfInstance.setStatus("current")
_StnNatOutTransOutsideBaseAddress_Type = IpAddress
_StnNatOutTransOutsideBaseAddress_Object = MibTableColumn
stnNatOutTransOutsideBaseAddress = _StnNatOutTransOutsideBaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 3, 1, 2),
    _StnNatOutTransOutsideBaseAddress_Type()
)
stnNatOutTransOutsideBaseAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatOutTransOutsideBaseAddress.setStatus("current")
_StnNatOutTransOutsideAddress_Type = IpAddress
_StnNatOutTransOutsideAddress_Object = MibTableColumn
stnNatOutTransOutsideAddress = _StnNatOutTransOutsideAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 3, 1, 3),
    _StnNatOutTransOutsideAddress_Type()
)
stnNatOutTransOutsideAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatOutTransOutsideAddress.setStatus("current")
_StnNatOutTransInsideAddress_Type = IpAddress
_StnNatOutTransInsideAddress_Object = MibTableColumn
stnNatOutTransInsideAddress = _StnNatOutTransInsideAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 3, 1, 4),
    _StnNatOutTransInsideAddress_Type()
)
stnNatOutTransInsideAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatOutTransInsideAddress.setStatus("current")
_StnNatOutTransMode_Type = NatTransMode
_StnNatOutTransMode_Object = MibTableColumn
stnNatOutTransMode = _StnNatOutTransMode_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 3, 1, 5),
    _StnNatOutTransMode_Type()
)
stnNatOutTransMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatOutTransMode.setStatus("current")


class _StnNatOutTransState_Type(Integer32):
    """Custom type stnNatOutTransState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("expired", 2),
          ("leased", 1))
    )


_StnNatOutTransState_Type.__name__ = "Integer32"
_StnNatOutTransState_Object = MibTableColumn
stnNatOutTransState = _StnNatOutTransState_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 3, 1, 6),
    _StnNatOutTransState_Type()
)
stnNatOutTransState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatOutTransState.setStatus("current")
_StnNatOutTransUpTimeSec_Type = Integer32
_StnNatOutTransUpTimeSec_Object = MibTableColumn
stnNatOutTransUpTimeSec = _StnNatOutTransUpTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 3, 1, 7),
    _StnNatOutTransUpTimeSec_Type()
)
stnNatOutTransUpTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatOutTransUpTimeSec.setStatus("current")
_StnNatOutTransSecsSinceLastHit_Type = Integer32
_StnNatOutTransSecsSinceLastHit_Object = MibTableColumn
stnNatOutTransSecsSinceLastHit = _StnNatOutTransSecsSinceLastHit_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 3, 1, 8),
    _StnNatOutTransSecsSinceLastHit_Type()
)
stnNatOutTransSecsSinceLastHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatOutTransSecsSinceLastHit.setStatus("current")
_StnNatOutTransCurrentFtpSessions_Type = Integer32
_StnNatOutTransCurrentFtpSessions_Object = MibTableColumn
stnNatOutTransCurrentFtpSessions = _StnNatOutTransCurrentFtpSessions_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 3, 1, 9),
    _StnNatOutTransCurrentFtpSessions_Type()
)
stnNatOutTransCurrentFtpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatOutTransCurrentFtpSessions.setStatus("current")
_StnNatOutTransTotalFtpSessions_Type = Integer32
_StnNatOutTransTotalFtpSessions_Object = MibTableColumn
stnNatOutTransTotalFtpSessions = _StnNatOutTransTotalFtpSessions_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 3, 1, 10),
    _StnNatOutTransTotalFtpSessions_Type()
)
stnNatOutTransTotalFtpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatOutTransTotalFtpSessions.setStatus("current")
_StnNatOutTransInsidePktHits_Type = Integer32
_StnNatOutTransInsidePktHits_Object = MibTableColumn
stnNatOutTransInsidePktHits = _StnNatOutTransInsidePktHits_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 3, 1, 11),
    _StnNatOutTransInsidePktHits_Type()
)
stnNatOutTransInsidePktHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatOutTransInsidePktHits.setStatus("current")
_StnNatOutTransOutsidePktHits_Type = Integer32
_StnNatOutTransOutsidePktHits_Object = MibTableColumn
stnNatOutTransOutsidePktHits = _StnNatOutTransOutsidePktHits_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 3, 1, 12),
    _StnNatOutTransOutsidePktHits_Type()
)
stnNatOutTransOutsidePktHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatOutTransOutsidePktHits.setStatus("current")
_StnNatOutTransOutsidePortNumber_Type = Integer32
_StnNatOutTransOutsidePortNumber_Object = MibTableColumn
stnNatOutTransOutsidePortNumber = _StnNatOutTransOutsidePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 3, 1, 13),
    _StnNatOutTransOutsidePortNumber_Type()
)
stnNatOutTransOutsidePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatOutTransOutsidePortNumber.setStatus("current")
_StnNatOutTransInsidePortNumber_Type = Integer32
_StnNatOutTransInsidePortNumber_Object = MibTableColumn
stnNatOutTransInsidePortNumber = _StnNatOutTransInsidePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 3, 1, 14),
    _StnNatOutTransInsidePortNumber_Type()
)
stnNatOutTransInsidePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatOutTransInsidePortNumber.setStatus("current")
_StnNatOutTransOutsidePortsInuse_Type = Integer32
_StnNatOutTransOutsidePortsInuse_Object = MibTableColumn
stnNatOutTransOutsidePortsInuse = _StnNatOutTransOutsidePortsInuse_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 3, 1, 15),
    _StnNatOutTransOutsidePortsInuse_Type()
)
stnNatOutTransOutsidePortsInuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatOutTransOutsidePortsInuse.setStatus("current")
_StnNatOutTransInsidePortsInuse_Type = Integer32
_StnNatOutTransInsidePortsInuse_Object = MibTableColumn
stnNatOutTransInsidePortsInuse = _StnNatOutTransInsidePortsInuse_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 3, 1, 16),
    _StnNatOutTransInsidePortsInuse_Type()
)
stnNatOutTransInsidePortsInuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatOutTransInsidePortsInuse.setStatus("current")
_StnNatOutTransInsidePortLimitReached_Type = Integer32
_StnNatOutTransInsidePortLimitReached_Object = MibTableColumn
stnNatOutTransInsidePortLimitReached = _StnNatOutTransInsidePortLimitReached_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 3, 1, 17),
    _StnNatOutTransInsidePortLimitReached_Type()
)
stnNatOutTransInsidePortLimitReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatOutTransInsidePortLimitReached.setStatus("current")
_StnNatInTransTable_Object = MibTable
stnNatInTransTable = _StnNatInTransTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 4)
)
if mibBuilder.loadTexts:
    stnNatInTransTable.setStatus("current")
_StnNatInTransEntry_Object = MibTableRow
stnNatInTransEntry = _StnNatInTransEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 4, 1)
)
stnNatInTransEntry.setIndexNames(
    (0, "STN-NAT-MIB", "stnNatInTransSubnetIfInstance"),
    (0, "STN-NAT-MIB", "stnNatInTransOutsideBaseAddress"),
    (0, "STN-NAT-MIB", "stnNatInTransInsideAddress"),
    (0, "STN-NAT-MIB", "stnNatInTransInsidePortNumber"),
)
if mibBuilder.loadTexts:
    stnNatInTransEntry.setStatus("current")
_StnNatInTransSubnetIfInstance_Type = Integer32
_StnNatInTransSubnetIfInstance_Object = MibTableColumn
stnNatInTransSubnetIfInstance = _StnNatInTransSubnetIfInstance_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 4, 1, 1),
    _StnNatInTransSubnetIfInstance_Type()
)
stnNatInTransSubnetIfInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatInTransSubnetIfInstance.setStatus("current")
_StnNatInTransOutsideBaseAddress_Type = IpAddress
_StnNatInTransOutsideBaseAddress_Object = MibTableColumn
stnNatInTransOutsideBaseAddress = _StnNatInTransOutsideBaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 4, 1, 2),
    _StnNatInTransOutsideBaseAddress_Type()
)
stnNatInTransOutsideBaseAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatInTransOutsideBaseAddress.setStatus("current")
_StnNatInTransOutsideAddress_Type = IpAddress
_StnNatInTransOutsideAddress_Object = MibTableColumn
stnNatInTransOutsideAddress = _StnNatInTransOutsideAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 4, 1, 3),
    _StnNatInTransOutsideAddress_Type()
)
stnNatInTransOutsideAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatInTransOutsideAddress.setStatus("current")
_StnNatInTransInsideAddress_Type = IpAddress
_StnNatInTransInsideAddress_Object = MibTableColumn
stnNatInTransInsideAddress = _StnNatInTransInsideAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 4, 1, 4),
    _StnNatInTransInsideAddress_Type()
)
stnNatInTransInsideAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatInTransInsideAddress.setStatus("current")
_StnNatInTransMode_Type = NatTransMode
_StnNatInTransMode_Object = MibTableColumn
stnNatInTransMode = _StnNatInTransMode_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 4, 1, 5),
    _StnNatInTransMode_Type()
)
stnNatInTransMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatInTransMode.setStatus("current")


class _StnNatInTransState_Type(Integer32):
    """Custom type stnNatInTransState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("expired", 2),
          ("leased", 1))
    )


_StnNatInTransState_Type.__name__ = "Integer32"
_StnNatInTransState_Object = MibTableColumn
stnNatInTransState = _StnNatInTransState_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 4, 1, 6),
    _StnNatInTransState_Type()
)
stnNatInTransState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatInTransState.setStatus("current")
_StnNatInTransUpTimeSec_Type = Integer32
_StnNatInTransUpTimeSec_Object = MibTableColumn
stnNatInTransUpTimeSec = _StnNatInTransUpTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 4, 1, 7),
    _StnNatInTransUpTimeSec_Type()
)
stnNatInTransUpTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatInTransUpTimeSec.setStatus("current")
_StnNatInTransSecsSinceLastHit_Type = Integer32
_StnNatInTransSecsSinceLastHit_Object = MibTableColumn
stnNatInTransSecsSinceLastHit = _StnNatInTransSecsSinceLastHit_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 4, 1, 8),
    _StnNatInTransSecsSinceLastHit_Type()
)
stnNatInTransSecsSinceLastHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatInTransSecsSinceLastHit.setStatus("current")
_StnNatInTransCurrentFtpSessions_Type = Integer32
_StnNatInTransCurrentFtpSessions_Object = MibTableColumn
stnNatInTransCurrentFtpSessions = _StnNatInTransCurrentFtpSessions_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 4, 1, 9),
    _StnNatInTransCurrentFtpSessions_Type()
)
stnNatInTransCurrentFtpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatInTransCurrentFtpSessions.setStatus("current")
_StnNatInTransTotalFtpSessions_Type = Integer32
_StnNatInTransTotalFtpSessions_Object = MibTableColumn
stnNatInTransTotalFtpSessions = _StnNatInTransTotalFtpSessions_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 4, 1, 10),
    _StnNatInTransTotalFtpSessions_Type()
)
stnNatInTransTotalFtpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatInTransTotalFtpSessions.setStatus("current")
_StnNatInTransInsidePktHits_Type = Integer32
_StnNatInTransInsidePktHits_Object = MibTableColumn
stnNatInTransInsidePktHits = _StnNatInTransInsidePktHits_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 4, 1, 11),
    _StnNatInTransInsidePktHits_Type()
)
stnNatInTransInsidePktHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatInTransInsidePktHits.setStatus("current")
_StnNatInTransOutsidePktHits_Type = Integer32
_StnNatInTransOutsidePktHits_Object = MibTableColumn
stnNatInTransOutsidePktHits = _StnNatInTransOutsidePktHits_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 4, 1, 12),
    _StnNatInTransOutsidePktHits_Type()
)
stnNatInTransOutsidePktHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatInTransOutsidePktHits.setStatus("current")
_StnNatInTransOutsidePortNumber_Type = Integer32
_StnNatInTransOutsidePortNumber_Object = MibTableColumn
stnNatInTransOutsidePortNumber = _StnNatInTransOutsidePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 4, 1, 13),
    _StnNatInTransOutsidePortNumber_Type()
)
stnNatInTransOutsidePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatInTransOutsidePortNumber.setStatus("current")
_StnNatInTransInsidePortNumber_Type = Integer32
_StnNatInTransInsidePortNumber_Object = MibTableColumn
stnNatInTransInsidePortNumber = _StnNatInTransInsidePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 4, 1, 14),
    _StnNatInTransInsidePortNumber_Type()
)
stnNatInTransInsidePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatInTransInsidePortNumber.setStatus("current")
_StnNatInTransOutsidePortsInuse_Type = Integer32
_StnNatInTransOutsidePortsInuse_Object = MibTableColumn
stnNatInTransOutsidePortsInuse = _StnNatInTransOutsidePortsInuse_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 4, 1, 15),
    _StnNatInTransOutsidePortsInuse_Type()
)
stnNatInTransOutsidePortsInuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatInTransOutsidePortsInuse.setStatus("current")
_StnNatInTransInsidePortsInuse_Type = Integer32
_StnNatInTransInsidePortsInuse_Object = MibTableColumn
stnNatInTransInsidePortsInuse = _StnNatInTransInsidePortsInuse_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 4, 1, 16),
    _StnNatInTransInsidePortsInuse_Type()
)
stnNatInTransInsidePortsInuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatInTransInsidePortsInuse.setStatus("current")
_StnNatInTransInsidePortLimitReached_Type = Integer32
_StnNatInTransInsidePortLimitReached_Object = MibTableColumn
stnNatInTransInsidePortLimitReached = _StnNatInTransInsidePortLimitReached_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 1, 4, 1, 17),
    _StnNatInTransInsidePortLimitReached_Type()
)
stnNatInTransInsidePortLimitReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNatInTransInsidePortLimitReached.setStatus("current")
_StnNatMibConformance_ObjectIdentity = ObjectIdentity
stnNatMibConformance = _StnNatMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 2)
)
_StnNatMibTraps_ObjectIdentity = ObjectIdentity
stnNatMibTraps = _StnNatMibTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 7, 1, 5, 1, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STN-NAT-MIB",
    **{"NatTransMode": NatTransMode,
       "stnNat": stnNat,
       "stnNatObjects": stnNatObjects,
       "stnNatL2Table": stnNatL2Table,
       "stnNatL2Entry": stnNatL2Entry,
       "stnNatL2IfIndex": stnNatL2IfIndex,
       "stnNatL2InsidePktMisses": stnNatL2InsidePktMisses,
       "stnNatL2InsidePktHits": stnNatL2InsidePktHits,
       "stnNatL2OutsidePktMisses": stnNatL2OutsidePktMisses,
       "stnNatL2OutsidePktHits": stnNatL2OutsidePktHits,
       "stnNatL2UntransInsidePkts": stnNatL2UntransInsidePkts,
       "stnNatL2UntransOutsidePkts": stnNatL2UntransOutsidePkts,
       "stnNatL2InsideAlgPkts": stnNatL2InsideAlgPkts,
       "stnNatL2OutsideAlgPkts": stnNatL2OutsideAlgPkts,
       "stnNatL2FlowId": stnNatL2FlowId,
       "stnNatGroupTable": stnNatGroupTable,
       "stnNatGroupEntry": stnNatGroupEntry,
       "stnNatGroupSubnetIfInstance": stnNatGroupSubnetIfInstance,
       "stnNatGroupOutsideBaseAddress": stnNatGroupOutsideBaseAddress,
       "stnNatGroupOutsideEndAddress": stnNatGroupOutsideEndAddress,
       "stnNatGroupInsideBaseAddress": stnNatGroupInsideBaseAddress,
       "stnNatGroupInsideEndAddress": stnNatGroupInsideEndAddress,
       "stnNatGroupTransMode": stnNatGroupTransMode,
       "stnNatGroupAddrIdleTime": stnNatGroupAddrIdleTime,
       "stnNatGroupAddrTransAvailable": stnNatGroupAddrTransAvailable,
       "stnNatGroupMaxFtpSessions": stnNatGroupMaxFtpSessions,
       "stnNatGroupMaxFtpSessionsPerInsideAddr": stnNatGroupMaxFtpSessionsPerInsideAddr,
       "stnNatGroupFtpControlSessionIdleTime": stnNatGroupFtpControlSessionIdleTime,
       "stnNatGroupCurrentFtpSessions": stnNatGroupCurrentFtpSessions,
       "stnNatGroupTotalFtpSessions": stnNatGroupTotalFtpSessions,
       "stnNatGroupMissedFtpSessionLookups": stnNatGroupMissedFtpSessionLookups,
       "stnNatGroupNoIdleFtpSessions": stnNatGroupNoIdleFtpSessions,
       "stnNatGroupNoIdleOutsideAddrs": stnNatGroupNoIdleOutsideAddrs,
       "stnNatGroupFoundIdleOutsideAddrs": stnNatGroupFoundIdleOutsideAddrs,
       "stnNatGroupInsidePktMisses": stnNatGroupInsidePktMisses,
       "stnNatGroupInsidePktHits": stnNatGroupInsidePktHits,
       "stnNatGroupOutsidePktMisses": stnNatGroupOutsidePktMisses,
       "stnNatGroupOutsidePktHits": stnNatGroupOutsidePktHits,
       "stnNatGroupInvalidOutsidePktMisses": stnNatGroupInvalidOutsidePktMisses,
       "stnNatGroupInsideFlowOrigin": stnNatGroupInsideFlowOrigin,
       "stnNatGroupPortBaseNumber": stnNatGroupPortBaseNumber,
       "stnNatGroupPortEndNumber": stnNatGroupPortEndNumber,
       "stnNatGroupMaxInsideAddrs": stnNatGroupMaxInsideAddrs,
       "stnNatGroupMaxPortsPerInsideAddr": stnNatGroupMaxPortsPerInsideAddr,
       "stnNatGroupPortLimitReached": stnNatGroupPortLimitReached,
       "stnNatGroupInsideAddrLimitReached": stnNatGroupInsideAddrLimitReached,
       "stnNatOutTransTable": stnNatOutTransTable,
       "stnNatOutTransEntry": stnNatOutTransEntry,
       "stnNatOutTransSubnetIfInstance": stnNatOutTransSubnetIfInstance,
       "stnNatOutTransOutsideBaseAddress": stnNatOutTransOutsideBaseAddress,
       "stnNatOutTransOutsideAddress": stnNatOutTransOutsideAddress,
       "stnNatOutTransInsideAddress": stnNatOutTransInsideAddress,
       "stnNatOutTransMode": stnNatOutTransMode,
       "stnNatOutTransState": stnNatOutTransState,
       "stnNatOutTransUpTimeSec": stnNatOutTransUpTimeSec,
       "stnNatOutTransSecsSinceLastHit": stnNatOutTransSecsSinceLastHit,
       "stnNatOutTransCurrentFtpSessions": stnNatOutTransCurrentFtpSessions,
       "stnNatOutTransTotalFtpSessions": stnNatOutTransTotalFtpSessions,
       "stnNatOutTransInsidePktHits": stnNatOutTransInsidePktHits,
       "stnNatOutTransOutsidePktHits": stnNatOutTransOutsidePktHits,
       "stnNatOutTransOutsidePortNumber": stnNatOutTransOutsidePortNumber,
       "stnNatOutTransInsidePortNumber": stnNatOutTransInsidePortNumber,
       "stnNatOutTransOutsidePortsInuse": stnNatOutTransOutsidePortsInuse,
       "stnNatOutTransInsidePortsInuse": stnNatOutTransInsidePortsInuse,
       "stnNatOutTransInsidePortLimitReached": stnNatOutTransInsidePortLimitReached,
       "stnNatInTransTable": stnNatInTransTable,
       "stnNatInTransEntry": stnNatInTransEntry,
       "stnNatInTransSubnetIfInstance": stnNatInTransSubnetIfInstance,
       "stnNatInTransOutsideBaseAddress": stnNatInTransOutsideBaseAddress,
       "stnNatInTransOutsideAddress": stnNatInTransOutsideAddress,
       "stnNatInTransInsideAddress": stnNatInTransInsideAddress,
       "stnNatInTransMode": stnNatInTransMode,
       "stnNatInTransState": stnNatInTransState,
       "stnNatInTransUpTimeSec": stnNatInTransUpTimeSec,
       "stnNatInTransSecsSinceLastHit": stnNatInTransSecsSinceLastHit,
       "stnNatInTransCurrentFtpSessions": stnNatInTransCurrentFtpSessions,
       "stnNatInTransTotalFtpSessions": stnNatInTransTotalFtpSessions,
       "stnNatInTransInsidePktHits": stnNatInTransInsidePktHits,
       "stnNatInTransOutsidePktHits": stnNatInTransOutsidePktHits,
       "stnNatInTransOutsidePortNumber": stnNatInTransOutsidePortNumber,
       "stnNatInTransInsidePortNumber": stnNatInTransInsidePortNumber,
       "stnNatInTransOutsidePortsInuse": stnNatInTransOutsidePortsInuse,
       "stnNatInTransInsidePortsInuse": stnNatInTransInsidePortsInuse,
       "stnNatInTransInsidePortLimitReached": stnNatInTransInsidePortLimitReached,
       "stnNatMibConformance": stnNatMibConformance,
       "stnNatMibTraps": stnNatMibTraps}
)
