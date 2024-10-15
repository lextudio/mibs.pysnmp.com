# SNMP MIB module (CISCO-IPMCAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IPMCAST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:49 2024
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

(igmpInterfaceEntry,) = mibBuilder.importSymbols(
    "IGMP-MIB",
    "igmpInterfaceEntry")

(OwnerString,) = mibBuilder.importSymbols(
    "RFC1271-MIB",
    "OwnerString")

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
 enterprises,
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
    "enterprises",
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

ciscoMcastMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoMcastMIBObjects_ObjectIdentity = ObjectIdentity
ciscoMcastMIBObjects = _CiscoMcastMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1)
)
_McastAccess_ObjectIdentity = ObjectIdentity
mcastAccess = _McastAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 1)
)
_PimRpAccessListTable_Object = MibTable
pimRpAccessListTable = _PimRpAccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pimRpAccessListTable.setStatus("current")
_PimRpAccessListEntry_Object = MibTableRow
pimRpAccessListEntry = _PimRpAccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 1, 1, 1)
)
pimRpAccessListEntry.setIndexNames(
    (0, "CISCO-IPMCAST-MIB", "pimRpAccessListRP"),
)
if mibBuilder.loadTexts:
    pimRpAccessListEntry.setStatus("current")
_PimRpAccessListRP_Type = IpAddress
_PimRpAccessListRP_Object = MibTableColumn
pimRpAccessListRP = _PimRpAccessListRP_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 1, 1, 1, 1),
    _PimRpAccessListRP_Type()
)
pimRpAccessListRP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimRpAccessListRP.setStatus("current")


class _PimRpAccessListNumber_Type(Integer32):
    """Custom type pimRpAccessListNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PimRpAccessListNumber_Type.__name__ = "Integer32"
_PimRpAccessListNumber_Object = MibTableColumn
pimRpAccessListNumber = _PimRpAccessListNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 1, 1, 1, 2),
    _PimRpAccessListNumber_Type()
)
pimRpAccessListNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimRpAccessListNumber.setStatus("current")
_PimRpAccessListStatus_Type = RowStatus
_PimRpAccessListStatus_Object = MibTableColumn
pimRpAccessListStatus = _PimRpAccessListStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 1, 1, 1, 3),
    _PimRpAccessListStatus_Type()
)
pimRpAccessListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimRpAccessListStatus.setStatus("current")
_IgmpAccessListTable_Object = MibTable
igmpAccessListTable = _IgmpAccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    igmpAccessListTable.setStatus("current")
_IgmpAccessListEntry_Object = MibTableRow
igmpAccessListEntry = _IgmpAccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    igmpAccessListEntry.setStatus("current")


class _IgmpAccessListNumber_Type(Integer32):
    """Custom type igmpAccessListNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IgmpAccessListNumber_Type.__name__ = "Integer32"
_IgmpAccessListNumber_Object = MibTableColumn
igmpAccessListNumber = _IgmpAccessListNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 1, 2, 1, 1),
    _IgmpAccessListNumber_Type()
)
igmpAccessListNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpAccessListNumber.setStatus("current")
_McastTrace_ObjectIdentity = ObjectIdentity
mcastTrace = _McastTrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2)
)
_McastTraceRequest_ObjectIdentity = ObjectIdentity
mcastTraceRequest = _McastTraceRequest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 1)
)


class _MrbranchState_Type(Integer32):
    """Custom type mrbranchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_MrbranchState_Type.__name__ = "Integer32"
_MrbranchState_Object = MibScalar
mrbranchState = _MrbranchState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 1, 1),
    _MrbranchState_Type()
)
mrbranchState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrbranchState.setStatus("current")
_MrbranchGroup_Type = IpAddress
_MrbranchGroup_Object = MibScalar
mrbranchGroup = _MrbranchGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 1, 2),
    _MrbranchGroup_Type()
)
mrbranchGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrbranchGroup.setStatus("current")
_MrbranchBranch_Type = IpAddress
_MrbranchBranch_Object = MibScalar
mrbranchBranch = _MrbranchBranch_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 1, 3),
    _MrbranchBranch_Type()
)
mrbranchBranch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrbranchBranch.setStatus("current")
_MrbranchTimeout_Type = Integer32
_MrbranchTimeout_Object = MibScalar
mrbranchTimeout = _MrbranchTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 1, 4),
    _MrbranchTimeout_Type()
)
mrbranchTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrbranchTimeout.setStatus("current")
if mibBuilder.loadTexts:
    mrbranchTimeout.setUnits("seconds")
_MrbranchRequestor_Type = OwnerString
_MrbranchRequestor_Object = MibScalar
mrbranchRequestor = _MrbranchRequestor_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 1, 5),
    _MrbranchRequestor_Type()
)
mrbranchRequestor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrbranchRequestor.setStatus("current")
if mibBuilder.loadTexts:
    mrbranchRequestor.setUnits("seconds")
_McastTraceResponse_ObjectIdentity = ObjectIdentity
mcastTraceResponse = _McastTraceResponse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 2)
)
_MrbranchResponseTable_Object = MibTable
mrbranchResponseTable = _MrbranchResponseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mrbranchResponseTable.setStatus("current")
_MrbranchResponseEntry_Object = MibTableRow
mrbranchResponseEntry = _MrbranchResponseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 2, 1, 1)
)
mrbranchResponseEntry.setIndexNames(
    (0, "CISCO-IPMCAST-MIB", "mrbranchResponseResponder"),
)
if mibBuilder.loadTexts:
    mrbranchResponseEntry.setStatus("current")
_MrbranchResponseResponder_Type = IpAddress
_MrbranchResponseResponder_Object = MibTableColumn
mrbranchResponseResponder = _MrbranchResponseResponder_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 2, 1, 1, 1),
    _MrbranchResponseResponder_Type()
)
mrbranchResponseResponder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mrbranchResponseResponder.setStatus("current")
_MrbranchResponseRtt_Type = Integer32
_MrbranchResponseRtt_Object = MibTableColumn
mrbranchResponseRtt = _MrbranchResponseRtt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 2, 1, 1, 2),
    _MrbranchResponseRtt_Type()
)
mrbranchResponseRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrbranchResponseRtt.setStatus("current")
_MrbranchResponseRPF_Type = IpAddress
_MrbranchResponseRPF_Object = MibTableColumn
mrbranchResponseRPF = _MrbranchResponseRPF_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 2, 1, 1, 3),
    _MrbranchResponseRPF_Type()
)
mrbranchResponseRPF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrbranchResponseRPF.setStatus("current")
_MrbranchInterfaceListTable_Object = MibTable
mrbranchInterfaceListTable = _MrbranchInterfaceListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    mrbranchInterfaceListTable.setStatus("current")
_MrbranchInterfaceListEntry_Object = MibTableRow
mrbranchInterfaceListEntry = _MrbranchInterfaceListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 2, 2, 1)
)
mrbranchInterfaceListEntry.setIndexNames(
    (0, "CISCO-IPMCAST-MIB", "mrbranchResponseResponder"),
    (0, "CISCO-IPMCAST-MIB", "mrbranchInterfaceListAddress"),
)
if mibBuilder.loadTexts:
    mrbranchInterfaceListEntry.setStatus("current")
_MrbranchInterfaceListAddress_Type = IpAddress
_MrbranchInterfaceListAddress_Object = MibTableColumn
mrbranchInterfaceListAddress = _MrbranchInterfaceListAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 2, 2, 1, 1),
    _MrbranchInterfaceListAddress_Type()
)
mrbranchInterfaceListAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrbranchInterfaceListAddress.setStatus("current")
_MrbranchInterfaceListNetMask_Type = IpAddress
_MrbranchInterfaceListNetMask_Object = MibTableColumn
mrbranchInterfaceListNetMask = _MrbranchInterfaceListNetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 2, 2, 2, 1, 2),
    _MrbranchInterfaceListNetMask_Type()
)
mrbranchInterfaceListNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrbranchInterfaceListNetMask.setStatus("current")
_McastFilter_ObjectIdentity = ObjectIdentity
mcastFilter = _McastFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3)
)
_IgmpConditionalFilteringEnable_Type = TruthValue
_IgmpConditionalFilteringEnable_Object = MibScalar
igmpConditionalFilteringEnable = _IgmpConditionalFilteringEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3, 1),
    _IgmpConditionalFilteringEnable_Type()
)
igmpConditionalFilteringEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpConditionalFilteringEnable.setStatus("current")
_IgmpMemberReportTimeout_Type = Integer32
_IgmpMemberReportTimeout_Object = MibScalar
igmpMemberReportTimeout = _IgmpMemberReportTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3, 2),
    _IgmpMemberReportTimeout_Type()
)
igmpMemberReportTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpMemberReportTimeout.setStatus("current")
if mibBuilder.loadTexts:
    igmpMemberReportTimeout.setUnits("seconds")
_IgmpCondFilterIfTable_Object = MibTable
igmpCondFilterIfTable = _IgmpCondFilterIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3, 3)
)
if mibBuilder.loadTexts:
    igmpCondFilterIfTable.setStatus("current")
_IgmpCondFilterIfEntry_Object = MibTableRow
igmpCondFilterIfEntry = _IgmpCondFilterIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3, 3, 1)
)
igmpCondFilterIfEntry.setIndexNames(
    (0, "CISCO-IPMCAST-MIB", "igmpCondFilterIfIndex"),
)
if mibBuilder.loadTexts:
    igmpCondFilterIfEntry.setStatus("current")
_IgmpCondFilterIfIndex_Type = Integer32
_IgmpCondFilterIfIndex_Object = MibTableColumn
igmpCondFilterIfIndex = _IgmpCondFilterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3, 3, 1, 1),
    _IgmpCondFilterIfIndex_Type()
)
igmpCondFilterIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpCondFilterIfIndex.setStatus("current")


class _IgmpCondFilterIfStatus_Type(Integer32):
    """Custom type igmpCondFilterIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 3),
          ("noRouter", 2),
          ("routerPresent", 1))
    )


_IgmpCondFilterIfStatus_Type.__name__ = "Integer32"
_IgmpCondFilterIfStatus_Object = MibTableColumn
igmpCondFilterIfStatus = _IgmpCondFilterIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3, 3, 1, 2),
    _IgmpCondFilterIfStatus_Type()
)
igmpCondFilterIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpCondFilterIfStatus.setStatus("current")
_IgmpCondFilterIfRouter_Type = TruthValue
_IgmpCondFilterIfRouter_Object = MibTableColumn
igmpCondFilterIfRouter = _IgmpCondFilterIfRouter_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3, 3, 1, 3),
    _IgmpCondFilterIfRouter_Type()
)
igmpCondFilterIfRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCondFilterIfRouter.setStatus("current")
_IgmpCondFilterMcastTable_Object = MibTable
igmpCondFilterMcastTable = _IgmpCondFilterMcastTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3, 4)
)
if mibBuilder.loadTexts:
    igmpCondFilterMcastTable.setStatus("current")
_IgmpCondFilterMcastEntry_Object = MibTableRow
igmpCondFilterMcastEntry = _IgmpCondFilterMcastEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3, 4, 1)
)
igmpCondFilterMcastEntry.setIndexNames(
    (0, "CISCO-IPMCAST-MIB", "igmpCondFilterMcastIfIndex"),
    (0, "CISCO-IPMCAST-MIB", "igmpCondFilterMcastAddress"),
)
if mibBuilder.loadTexts:
    igmpCondFilterMcastEntry.setStatus("current")
_IgmpCondFilterMcastIfIndex_Type = Integer32
_IgmpCondFilterMcastIfIndex_Object = MibTableColumn
igmpCondFilterMcastIfIndex = _IgmpCondFilterMcastIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3, 4, 1, 1),
    _IgmpCondFilterMcastIfIndex_Type()
)
igmpCondFilterMcastIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpCondFilterMcastIfIndex.setStatus("current")
_IgmpCondFilterMcastAddress_Type = IpAddress
_IgmpCondFilterMcastAddress_Object = MibTableColumn
igmpCondFilterMcastAddress = _IgmpCondFilterMcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3, 4, 1, 2),
    _IgmpCondFilterMcastAddress_Type()
)
igmpCondFilterMcastAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpCondFilterMcastAddress.setStatus("current")
_IgmpCondFilterMcastMember_Type = TruthValue
_IgmpCondFilterMcastMember_Object = MibTableColumn
igmpCondFilterMcastMember = _IgmpCondFilterMcastMember_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3, 4, 1, 3),
    _IgmpCondFilterMcastMember_Type()
)
igmpCondFilterMcastMember.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpCondFilterMcastMember.setStatus("current")
_IgmpCondFilterMcastInPkts_Type = Counter32
_IgmpCondFilterMcastInPkts_Object = MibTableColumn
igmpCondFilterMcastInPkts = _IgmpCondFilterMcastInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3, 4, 1, 4),
    _IgmpCondFilterMcastInPkts_Type()
)
igmpCondFilterMcastInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCondFilterMcastInPkts.setStatus("current")
_IgmpCondFilterMcastOutPkts_Type = Counter32
_IgmpCondFilterMcastOutPkts_Object = MibTableColumn
igmpCondFilterMcastOutPkts = _IgmpCondFilterMcastOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3, 4, 1, 5),
    _IgmpCondFilterMcastOutPkts_Type()
)
igmpCondFilterMcastOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCondFilterMcastOutPkts.setStatus("current")
_IgmpCondFilterMcastStatus_Type = RowStatus
_IgmpCondFilterMcastStatus_Object = MibTableColumn
igmpCondFilterMcastStatus = _IgmpCondFilterMcastStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 1, 3, 4, 1, 6),
    _IgmpCondFilterMcastStatus_Type()
)
igmpCondFilterMcastStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpCondFilterMcastStatus.setStatus("current")
_CiscoMcastMIBConformance_ObjectIdentity = ObjectIdentity
ciscoMcastMIBConformance = _CiscoMcastMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 2)
)
_CiscoMcastMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoMcastMIBCompliances = _CiscoMcastMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 2, 1)
)
_CiscoMcastMIBGroups_ObjectIdentity = ObjectIdentity
ciscoMcastMIBGroups = _CiscoMcastMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 2, 2)
)
igmpInterfaceEntry.registerAugmentions(
    ("CISCO-IPMCAST-MIB",
     "igmpAccessListEntry")
)
igmpAccessListEntry.setIndexNames(*igmpInterfaceEntry.getIndexNames())

# Managed Objects groups

ciscoMcastAccessMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 2, 2, 1)
)
ciscoMcastAccessMIBGroup.setObjects(
      *(("CISCO-IPMCAST-MIB", "pimRpAccessListNumber"),
        ("CISCO-IPMCAST-MIB", "pimRpAccessListStatus"),
        ("CISCO-IPMCAST-MIB", "igmpAccessListNumber"))
)
if mibBuilder.loadTexts:
    ciscoMcastAccessMIBGroup.setStatus("current")

ciscoMrbranchMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 2, 2, 2)
)
ciscoMrbranchMIBGroup.setObjects(
      *(("CISCO-IPMCAST-MIB", "mrbranchState"),
        ("CISCO-IPMCAST-MIB", "mrbranchGroup"),
        ("CISCO-IPMCAST-MIB", "mrbranchBranch"),
        ("CISCO-IPMCAST-MIB", "mrbranchTimeout"),
        ("CISCO-IPMCAST-MIB", "mrbranchRequestor"),
        ("CISCO-IPMCAST-MIB", "mrbranchResponseRtt"),
        ("CISCO-IPMCAST-MIB", "mrbranchResponseRPF"),
        ("CISCO-IPMCAST-MIB", "mrbranchInterfaceListNetMask"))
)
if mibBuilder.loadTexts:
    ciscoMrbranchMIBGroup.setStatus("current")

ciscoMcastFilterMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 2, 2, 3)
)
ciscoMcastFilterMIBGroup.setObjects(
      *(("CISCO-IPMCAST-MIB", "igmpConditionalFilteringEnable"),
        ("CISCO-IPMCAST-MIB", "igmpMemberReportTimeout"),
        ("CISCO-IPMCAST-MIB", "igmpCondFilterIfStatus"),
        ("CISCO-IPMCAST-MIB", "igmpCondFilterIfRouter"),
        ("CISCO-IPMCAST-MIB", "igmpCondFilterMcastMember"),
        ("CISCO-IPMCAST-MIB", "igmpCondFilterMcastInPkts"),
        ("CISCO-IPMCAST-MIB", "igmpCondFilterMcastOutPkts"),
        ("CISCO-IPMCAST-MIB", "igmpCondFilterMcastStatus"))
)
if mibBuilder.loadTexts:
    ciscoMcastFilterMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoMcastMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoMcastMIBCompliance.setStatus(
        "current"
    )

ciscoMcastCondFilterMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 4, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoMcastCondFilterMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IPMCAST-MIB",
    **{"ciscoMcastMIB": ciscoMcastMIB,
       "ciscoMcastMIBObjects": ciscoMcastMIBObjects,
       "mcastAccess": mcastAccess,
       "pimRpAccessListTable": pimRpAccessListTable,
       "pimRpAccessListEntry": pimRpAccessListEntry,
       "pimRpAccessListRP": pimRpAccessListRP,
       "pimRpAccessListNumber": pimRpAccessListNumber,
       "pimRpAccessListStatus": pimRpAccessListStatus,
       "igmpAccessListTable": igmpAccessListTable,
       "igmpAccessListEntry": igmpAccessListEntry,
       "igmpAccessListNumber": igmpAccessListNumber,
       "mcastTrace": mcastTrace,
       "mcastTraceRequest": mcastTraceRequest,
       "mrbranchState": mrbranchState,
       "mrbranchGroup": mrbranchGroup,
       "mrbranchBranch": mrbranchBranch,
       "mrbranchTimeout": mrbranchTimeout,
       "mrbranchRequestor": mrbranchRequestor,
       "mcastTraceResponse": mcastTraceResponse,
       "mrbranchResponseTable": mrbranchResponseTable,
       "mrbranchResponseEntry": mrbranchResponseEntry,
       "mrbranchResponseResponder": mrbranchResponseResponder,
       "mrbranchResponseRtt": mrbranchResponseRtt,
       "mrbranchResponseRPF": mrbranchResponseRPF,
       "mrbranchInterfaceListTable": mrbranchInterfaceListTable,
       "mrbranchInterfaceListEntry": mrbranchInterfaceListEntry,
       "mrbranchInterfaceListAddress": mrbranchInterfaceListAddress,
       "mrbranchInterfaceListNetMask": mrbranchInterfaceListNetMask,
       "mcastFilter": mcastFilter,
       "igmpConditionalFilteringEnable": igmpConditionalFilteringEnable,
       "igmpMemberReportTimeout": igmpMemberReportTimeout,
       "igmpCondFilterIfTable": igmpCondFilterIfTable,
       "igmpCondFilterIfEntry": igmpCondFilterIfEntry,
       "igmpCondFilterIfIndex": igmpCondFilterIfIndex,
       "igmpCondFilterIfStatus": igmpCondFilterIfStatus,
       "igmpCondFilterIfRouter": igmpCondFilterIfRouter,
       "igmpCondFilterMcastTable": igmpCondFilterMcastTable,
       "igmpCondFilterMcastEntry": igmpCondFilterMcastEntry,
       "igmpCondFilterMcastIfIndex": igmpCondFilterMcastIfIndex,
       "igmpCondFilterMcastAddress": igmpCondFilterMcastAddress,
       "igmpCondFilterMcastMember": igmpCondFilterMcastMember,
       "igmpCondFilterMcastInPkts": igmpCondFilterMcastInPkts,
       "igmpCondFilterMcastOutPkts": igmpCondFilterMcastOutPkts,
       "igmpCondFilterMcastStatus": igmpCondFilterMcastStatus,
       "ciscoMcastMIBConformance": ciscoMcastMIBConformance,
       "ciscoMcastMIBCompliances": ciscoMcastMIBCompliances,
       "ciscoMcastMIBCompliance": ciscoMcastMIBCompliance,
       "ciscoMcastCondFilterMIBCompliance": ciscoMcastCondFilterMIBCompliance,
       "ciscoMcastMIBGroups": ciscoMcastMIBGroups,
       "ciscoMcastAccessMIBGroup": ciscoMcastAccessMIBGroup,
       "ciscoMrbranchMIBGroup": ciscoMrbranchMIBGroup,
       "ciscoMcastFilterMIBGroup": ciscoMcastFilterMIBGroup}
)
