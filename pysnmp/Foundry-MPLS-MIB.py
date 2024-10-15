# SNMP MIB module (FOUNDRY-MPLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FOUNDRY-MPLS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:47 2024
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

(ClassOfService,) = mibBuilder.importSymbols(
    "FDRY-MPLS-L2VPN-MIB",
    "ClassOfService")

(AreaID,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-OSPF-GROUP-MIB",
    "AreaID")

(snMpls,
 snTraps) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "snMpls",
    "snTraps")

(MplsTunnelAffinity,) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsTunnelAffinity")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mpls = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1)
)
mpls.setRevisions(
        ("2013-05-29 00:00",
         "2010-06-02 00:00",
         "2008-02-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MplsLspNotifications_ObjectIdentity = ObjectIdentity
mplsLspNotifications = _MplsLspNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 0)
)
_MplsInfo_ObjectIdentity = ObjectIdentity
mplsInfo = _MplsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 1)
)
_MplsVersion_Type = Unsigned32
_MplsVersion_Object = MibScalar
mplsVersion = _MplsVersion_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 1, 1),
    _MplsVersion_Type()
)
mplsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVersion.setStatus("current")
_BrcdMplsAdminGroupTable_Object = MibTable
brcdMplsAdminGroupTable = _BrcdMplsAdminGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 1, 2)
)
if mibBuilder.loadTexts:
    brcdMplsAdminGroupTable.setStatus("current")
_BrcdMplsAdminGroupEntry_Object = MibTableRow
brcdMplsAdminGroupEntry = _BrcdMplsAdminGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 1, 2, 1)
)
brcdMplsAdminGroupEntry.setIndexNames(
    (0, "FOUNDRY-MPLS-MIB", "brcdMplsAdminGroupId"),
)
if mibBuilder.loadTexts:
    brcdMplsAdminGroupEntry.setStatus("current")


class _BrcdMplsAdminGroupId_Type(Unsigned32):
    """Custom type brcdMplsAdminGroupId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_BrcdMplsAdminGroupId_Type.__name__ = "Unsigned32"
_BrcdMplsAdminGroupId_Object = MibTableColumn
brcdMplsAdminGroupId = _BrcdMplsAdminGroupId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 1, 2, 1, 1),
    _BrcdMplsAdminGroupId_Type()
)
brcdMplsAdminGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdMplsAdminGroupId.setStatus("current")


class _BrcdMplsAdminGroupName_Type(DisplayString):
    """Custom type brcdMplsAdminGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BrcdMplsAdminGroupName_Type.__name__ = "DisplayString"
_BrcdMplsAdminGroupName_Object = MibTableColumn
brcdMplsAdminGroupName = _BrcdMplsAdminGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 1, 2, 1, 2),
    _BrcdMplsAdminGroupName_Type()
)
brcdMplsAdminGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdMplsAdminGroupName.setStatus("current")
_BrcdMplsAdminGroupRowStatus_Type = RowStatus
_BrcdMplsAdminGroupRowStatus_Object = MibTableColumn
brcdMplsAdminGroupRowStatus = _BrcdMplsAdminGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 1, 2, 1, 3),
    _BrcdMplsAdminGroupRowStatus_Type()
)
brcdMplsAdminGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdMplsAdminGroupRowStatus.setStatus("current")
_BrcdMplsInterfaceTable_Object = MibTable
brcdMplsInterfaceTable = _BrcdMplsInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 1, 3)
)
if mibBuilder.loadTexts:
    brcdMplsInterfaceTable.setStatus("current")
_BrcdMplsInterfaceEntry_Object = MibTableRow
brcdMplsInterfaceEntry = _BrcdMplsInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 1, 3, 1)
)
brcdMplsInterfaceEntry.setIndexNames(
    (0, "FOUNDRY-MPLS-MIB", "brcdMplsInterfaceIndex"),
)
if mibBuilder.loadTexts:
    brcdMplsInterfaceEntry.setStatus("current")
_BrcdMplsInterfaceIndex_Type = Unsigned32
_BrcdMplsInterfaceIndex_Object = MibTableColumn
brcdMplsInterfaceIndex = _BrcdMplsInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 1, 3, 1, 1),
    _BrcdMplsInterfaceIndex_Type()
)
brcdMplsInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdMplsInterfaceIndex.setStatus("current")
_BrcdMplsInterfaceAdminGroup_Type = MplsTunnelAffinity
_BrcdMplsInterfaceAdminGroup_Object = MibTableColumn
brcdMplsInterfaceAdminGroup = _BrcdMplsInterfaceAdminGroup_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 1, 3, 1, 2),
    _BrcdMplsInterfaceAdminGroup_Type()
)
brcdMplsInterfaceAdminGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdMplsInterfaceAdminGroup.setStatus("current")
_BrcdMplsInterfaceRowStatus_Type = RowStatus
_BrcdMplsInterfaceRowStatus_Object = MibTableColumn
brcdMplsInterfaceRowStatus = _BrcdMplsInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 1, 3, 1, 3),
    _BrcdMplsInterfaceRowStatus_Type()
)
brcdMplsInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdMplsInterfaceRowStatus.setStatus("current")
_MplsLspInfo_ObjectIdentity = ObjectIdentity
mplsLspInfo = _MplsLspInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2)
)
_MplsConfiguredLsps_Type = Unsigned32
_MplsConfiguredLsps_Object = MibScalar
mplsConfiguredLsps = _MplsConfiguredLsps_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 1),
    _MplsConfiguredLsps_Type()
)
mplsConfiguredLsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsConfiguredLsps.setStatus("deprecated")
_MplsActiveLsps_Type = Unsigned32
_MplsActiveLsps_Object = MibScalar
mplsActiveLsps = _MplsActiveLsps_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 2),
    _MplsActiveLsps_Type()
)
mplsActiveLsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsActiveLsps.setStatus("deprecated")
_MplsLspTable_Object = MibTable
mplsLspTable = _MplsLspTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mplsLspTable.setStatus("current")
_MplsLspEntry_Object = MibTableRow
mplsLspEntry = _MplsLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1)
)
mplsLspEntry.setIndexNames(
    (0, "FOUNDRY-MPLS-MIB", "mplsLspSignalingProto"),
    (0, "FOUNDRY-MPLS-MIB", "mplsLspIndex"),
)
if mibBuilder.loadTexts:
    mplsLspEntry.setStatus("current")


class _MplsLspSignalingProto_Type(Integer32):
    """Custom type mplsLspSignalingProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ldp", 1),
          ("rsvp", 2))
    )


_MplsLspSignalingProto_Type.__name__ = "Integer32"
_MplsLspSignalingProto_Object = MibTableColumn
mplsLspSignalingProto = _MplsLspSignalingProto_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 1),
    _MplsLspSignalingProto_Type()
)
mplsLspSignalingProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLspSignalingProto.setStatus("current")
_MplsLspIndex_Type = Unsigned32
_MplsLspIndex_Object = MibTableColumn
mplsLspIndex = _MplsLspIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 2),
    _MplsLspIndex_Type()
)
mplsLspIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLspIndex.setStatus("current")


class _MplsLspName_Type(DisplayString):
    """Custom type mplsLspName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MplsLspName_Type.__name__ = "DisplayString"
_MplsLspName_Object = MibTableColumn
mplsLspName = _MplsLspName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 3),
    _MplsLspName_Type()
)
mplsLspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspName.setStatus("current")


class _MplsLspState_Type(Integer32):
    """Custom type mplsLspState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("unknown", 1),
          ("up", 2))
    )


_MplsLspState_Type.__name__ = "Integer32"
_MplsLspState_Object = MibTableColumn
mplsLspState = _MplsLspState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 4),
    _MplsLspState_Type()
)
mplsLspState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspState.setStatus("current")
_MplsLspPackets_Type = Counter64
_MplsLspPackets_Object = MibTableColumn
mplsLspPackets = _MplsLspPackets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 5),
    _MplsLspPackets_Type()
)
mplsLspPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspPackets.setStatus("current")
_MplsLspAge_Type = TimeStamp
_MplsLspAge_Object = MibTableColumn
mplsLspAge = _MplsLspAge_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 6),
    _MplsLspAge_Type()
)
mplsLspAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspAge.setStatus("current")
_MplsLspTimeUp_Type = TimeStamp
_MplsLspTimeUp_Object = MibTableColumn
mplsLspTimeUp = _MplsLspTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 7),
    _MplsLspTimeUp_Type()
)
mplsLspTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspTimeUp.setStatus("current")
_MplsLspPrimaryTimeUp_Type = TimeStamp
_MplsLspPrimaryTimeUp_Object = MibTableColumn
mplsLspPrimaryTimeUp = _MplsLspPrimaryTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 8),
    _MplsLspPrimaryTimeUp_Type()
)
mplsLspPrimaryTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspPrimaryTimeUp.setStatus("current")
_MplsLspTransitions_Type = Counter32
_MplsLspTransitions_Object = MibTableColumn
mplsLspTransitions = _MplsLspTransitions_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 9),
    _MplsLspTransitions_Type()
)
mplsLspTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspTransitions.setStatus("current")
_MplsLspLastTransition_Type = TimeStamp
_MplsLspLastTransition_Object = MibTableColumn
mplsLspLastTransition = _MplsLspLastTransition_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 10),
    _MplsLspLastTransition_Type()
)
mplsLspLastTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspLastTransition.setStatus("current")
_MplsLspFrom_Type = IpAddress
_MplsLspFrom_Object = MibTableColumn
mplsLspFrom = _MplsLspFrom_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 11),
    _MplsLspFrom_Type()
)
mplsLspFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspFrom.setStatus("current")
_MplsLspTo_Type = IpAddress
_MplsLspTo_Object = MibTableColumn
mplsLspTo = _MplsLspTo_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 12),
    _MplsLspTo_Type()
)
mplsLspTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspTo.setStatus("current")


class _MplsLspPathName_Type(DisplayString):
    """Custom type mplsLspPathName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MplsLspPathName_Type.__name__ = "DisplayString"
_MplsLspPathName_Object = MibTableColumn
mplsLspPathName = _MplsLspPathName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 13),
    _MplsLspPathName_Type()
)
mplsLspPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspPathName.setStatus("current")


class _MplsLspPathType_Type(Integer32):
    """Custom type mplsLspPathType based on Integer32"""
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
        *(("other", 1),
          ("primary", 2),
          ("secondary", 4),
          ("standby", 3))
    )


_MplsLspPathType_Type.__name__ = "Integer32"
_MplsLspPathType_Object = MibTableColumn
mplsLspPathType = _MplsLspPathType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 14),
    _MplsLspPathType_Type()
)
mplsLspPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspPathType.setStatus("current")
_MplsLspAdaptive_Type = TruthValue
_MplsLspAdaptive_Object = MibTableColumn
mplsLspAdaptive = _MplsLspAdaptive_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 15),
    _MplsLspAdaptive_Type()
)
mplsLspAdaptive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspAdaptive.setStatus("current")
_MplsLspBfdSessionId_Type = Unsigned32
_MplsLspBfdSessionId_Object = MibTableColumn
mplsLspBfdSessionId = _MplsLspBfdSessionId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 16),
    _MplsLspBfdSessionId_Type()
)
mplsLspBfdSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspBfdSessionId.setStatus("current")


class _MplsLspReoptimizeTimer_Type(Unsigned32):
    """Custom type mplsLspReoptimizeTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(300, 65535),
    )


_MplsLspReoptimizeTimer_Type.__name__ = "Unsigned32"
_MplsLspReoptimizeTimer_Object = MibTableColumn
mplsLspReoptimizeTimer = _MplsLspReoptimizeTimer_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 17),
    _MplsLspReoptimizeTimer_Type()
)
mplsLspReoptimizeTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspReoptimizeTimer.setStatus("current")
_MplsLspCoS_Type = ClassOfService
_MplsLspCoS_Object = MibTableColumn
mplsLspCoS = _MplsLspCoS_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 18),
    _MplsLspCoS_Type()
)
mplsLspCoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspCoS.setStatus("current")


class _MplsLspHopLimit_Type(Unsigned32):
    """Custom type mplsLspHopLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MplsLspHopLimit_Type.__name__ = "Unsigned32"
_MplsLspHopLimit_Object = MibTableColumn
mplsLspHopLimit = _MplsLspHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 19),
    _MplsLspHopLimit_Type()
)
mplsLspHopLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspHopLimit.setStatus("current")


class _MplsLspCspf_Type(Integer32):
    """Custom type mplsLspCspf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MplsLspCspf_Type.__name__ = "Integer32"
_MplsLspCspf_Object = MibTableColumn
mplsLspCspf = _MplsLspCspf_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 20),
    _MplsLspCspf_Type()
)
mplsLspCspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspCspf.setStatus("current")


class _MplsLspCspfTieBreaker_Type(Integer32):
    """Custom type mplsLspCspfTieBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("leastFill", 2),
          ("mostFill", 3),
          ("random", 1))
    )


_MplsLspCspfTieBreaker_Type.__name__ = "Integer32"
_MplsLspCspfTieBreaker_Object = MibTableColumn
mplsLspCspfTieBreaker = _MplsLspCspfTieBreaker_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 21),
    _MplsLspCspfTieBreaker_Type()
)
mplsLspCspfTieBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspCspfTieBreaker.setStatus("current")


class _MplsLspFrrMode_Type(Integer32):
    """Custom type mplsLspFrrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("detour", 2),
          ("facility", 3),
          ("none", 1))
    )


_MplsLspFrrMode_Type.__name__ = "Integer32"
_MplsLspFrrMode_Object = MibTableColumn
mplsLspFrrMode = _MplsLspFrrMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 22),
    _MplsLspFrrMode_Type()
)
mplsLspFrrMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspFrrMode.setStatus("current")


class _MplsLspFrrSetupPriority_Type(Unsigned32):
    """Custom type mplsLspFrrSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MplsLspFrrSetupPriority_Type.__name__ = "Unsigned32"
_MplsLspFrrSetupPriority_Object = MibTableColumn
mplsLspFrrSetupPriority = _MplsLspFrrSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 23),
    _MplsLspFrrSetupPriority_Type()
)
mplsLspFrrSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspFrrSetupPriority.setStatus("current")


class _MplsLspFrrHoldingPriority_Type(Unsigned32):
    """Custom type mplsLspFrrHoldingPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MplsLspFrrHoldingPriority_Type.__name__ = "Unsigned32"
_MplsLspFrrHoldingPriority_Object = MibTableColumn
mplsLspFrrHoldingPriority = _MplsLspFrrHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 24),
    _MplsLspFrrHoldingPriority_Type()
)
mplsLspFrrHoldingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspFrrHoldingPriority.setStatus("current")


class _MplsLspFrrHopLimit_Type(Unsigned32):
    """Custom type mplsLspFrrHopLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MplsLspFrrHopLimit_Type.__name__ = "Unsigned32"
_MplsLspFrrHopLimit_Object = MibTableColumn
mplsLspFrrHopLimit = _MplsLspFrrHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 25),
    _MplsLspFrrHopLimit_Type()
)
mplsLspFrrHopLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspFrrHopLimit.setStatus("current")


class _MplsLspFrrBandwidth_Type(Unsigned32):
    """Custom type mplsLspFrrBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsLspFrrBandwidth_Type.__name__ = "Unsigned32"
_MplsLspFrrBandwidth_Object = MibTableColumn
mplsLspFrrBandwidth = _MplsLspFrrBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 26),
    _MplsLspFrrBandwidth_Type()
)
mplsLspFrrBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspFrrBandwidth.setStatus("current")
_MplsLspFrrAdmGrpIncludeAny_Type = MplsTunnelAffinity
_MplsLspFrrAdmGrpIncludeAny_Object = MibTableColumn
mplsLspFrrAdmGrpIncludeAny = _MplsLspFrrAdmGrpIncludeAny_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 27),
    _MplsLspFrrAdmGrpIncludeAny_Type()
)
mplsLspFrrAdmGrpIncludeAny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspFrrAdmGrpIncludeAny.setStatus("current")
_MplsLspFrrAdmGrpIncludeAll_Type = MplsTunnelAffinity
_MplsLspFrrAdmGrpIncludeAll_Object = MibTableColumn
mplsLspFrrAdmGrpIncludeAll = _MplsLspFrrAdmGrpIncludeAll_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 28),
    _MplsLspFrrAdmGrpIncludeAll_Type()
)
mplsLspFrrAdmGrpIncludeAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspFrrAdmGrpIncludeAll.setStatus("current")
_MplsLspFrrAdmGrpExcludeAny_Type = MplsTunnelAffinity
_MplsLspFrrAdmGrpExcludeAny_Object = MibTableColumn
mplsLspFrrAdmGrpExcludeAny = _MplsLspFrrAdmGrpExcludeAny_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 29),
    _MplsLspFrrAdmGrpExcludeAny_Type()
)
mplsLspFrrAdmGrpExcludeAny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspFrrAdmGrpExcludeAny.setStatus("current")


class _MplsLspPathSelectMode_Type(Integer32):
    """Custom type mplsLspPathSelectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2),
          ("unconditional", 3))
    )


_MplsLspPathSelectMode_Type.__name__ = "Integer32"
_MplsLspPathSelectMode_Object = MibTableColumn
mplsLspPathSelectMode = _MplsLspPathSelectMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 30),
    _MplsLspPathSelectMode_Type()
)
mplsLspPathSelectMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspPathSelectMode.setStatus("current")


class _MplsLspPathSelectPathname_Type(DisplayString):
    """Custom type mplsLspPathSelectPathname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MplsLspPathSelectPathname_Type.__name__ = "DisplayString"
_MplsLspPathSelectPathname_Object = MibTableColumn
mplsLspPathSelectPathname = _MplsLspPathSelectPathname_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 31),
    _MplsLspPathSelectPathname_Type()
)
mplsLspPathSelectPathname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspPathSelectPathname.setStatus("current")


class _MplsLspPathSelectRevertTimer_Type(Unsigned32):
    """Custom type mplsLspPathSelectRevertTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MplsLspPathSelectRevertTimer_Type.__name__ = "Unsigned32"
_MplsLspPathSelectRevertTimer_Object = MibTableColumn
mplsLspPathSelectRevertTimer = _MplsLspPathSelectRevertTimer_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 32),
    _MplsLspPathSelectRevertTimer_Type()
)
mplsLspPathSelectRevertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspPathSelectRevertTimer.setStatus("current")
_MplsLspShortcutOspfAllowed_Type = TruthValue
_MplsLspShortcutOspfAllowed_Object = MibTableColumn
mplsLspShortcutOspfAllowed = _MplsLspShortcutOspfAllowed_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 33),
    _MplsLspShortcutOspfAllowed_Type()
)
mplsLspShortcutOspfAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspShortcutOspfAllowed.setStatus("current")
_MplsLspShortcutIsisAllowed_Type = TruthValue
_MplsLspShortcutIsisAllowed_Object = MibTableColumn
mplsLspShortcutIsisAllowed = _MplsLspShortcutIsisAllowed_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 34),
    _MplsLspShortcutIsisAllowed_Type()
)
mplsLspShortcutIsisAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspShortcutIsisAllowed.setStatus("current")


class _MplsLspShortcutIsisLevel_Type(Integer32):
    """Custom type mplsLspShortcutIsisLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level1and2", 3),
          ("level2", 2))
    )


_MplsLspShortcutIsisLevel_Type.__name__ = "Integer32"
_MplsLspShortcutIsisLevel_Object = MibTableColumn
mplsLspShortcutIsisLevel = _MplsLspShortcutIsisLevel_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 35),
    _MplsLspShortcutIsisLevel_Type()
)
mplsLspShortcutIsisLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspShortcutIsisLevel.setStatus("current")
_MplsLspShortcutIsisAnnounce_Type = TruthValue
_MplsLspShortcutIsisAnnounce_Object = MibTableColumn
mplsLspShortcutIsisAnnounce = _MplsLspShortcutIsisAnnounce_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 36),
    _MplsLspShortcutIsisAnnounce_Type()
)
mplsLspShortcutIsisAnnounce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspShortcutIsisAnnounce.setStatus("current")


class _MplsLspShortcutIsisAnnounceMetric_Type(Integer32):
    """Custom type mplsLspShortcutIsisAnnounceMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_MplsLspShortcutIsisAnnounceMetric_Type.__name__ = "Integer32"
_MplsLspShortcutIsisAnnounceMetric_Object = MibTableColumn
mplsLspShortcutIsisAnnounceMetric = _MplsLspShortcutIsisAnnounceMetric_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 37),
    _MplsLspShortcutIsisAnnounceMetric_Type()
)
mplsLspShortcutIsisAnnounceMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspShortcutIsisAnnounceMetric.setStatus("current")


class _MplsLspShortcutIsisRelativeMetric_Type(Integer32):
    """Custom type mplsLspShortcutIsisRelativeMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-16777215, 16777215),
    )


_MplsLspShortcutIsisRelativeMetric_Type.__name__ = "Integer32"
_MplsLspShortcutIsisRelativeMetric_Object = MibTableColumn
mplsLspShortcutIsisRelativeMetric = _MplsLspShortcutIsisRelativeMetric_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 2, 3, 1, 38),
    _MplsLspShortcutIsisRelativeMetric_Type()
)
mplsLspShortcutIsisRelativeMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspShortcutIsisRelativeMetric.setStatus("current")
_MplsVllInfo_ObjectIdentity = ObjectIdentity
mplsVllInfo = _MplsVllInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 3)
)
_MplsVplsInfo_ObjectIdentity = ObjectIdentity
mplsVplsInfo = _MplsVplsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 15, 1, 4)
)

# Managed Objects groups


# Notification objects

snMplsLspUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1010)
)
snMplsLspUp.setObjects(
      *(("FOUNDRY-MPLS-MIB", "mplsLspName"),
        ("FOUNDRY-MPLS-MIB", "mplsLspPathName"))
)
if mibBuilder.loadTexts:
    snMplsLspUp.setStatus(
        "current"
    )

snMplsLspDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1011)
)
snMplsLspDown.setObjects(
      *(("FOUNDRY-MPLS-MIB", "mplsLspName"),
        ("FOUNDRY-MPLS-MIB", "mplsLspPathName"))
)
if mibBuilder.loadTexts:
    snMplsLspDown.setStatus(
        "current"
    )

snMplsLspChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1012)
)
snMplsLspChange.setObjects(
      *(("FOUNDRY-MPLS-MIB", "mplsLspName"),
        ("FOUNDRY-MPLS-MIB", "mplsLspPathName"))
)
if mibBuilder.loadTexts:
    snMplsLspChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-MPLS-MIB",
    **{"snMplsLspUp": snMplsLspUp,
       "snMplsLspDown": snMplsLspDown,
       "snMplsLspChange": snMplsLspChange,
       "mpls": mpls,
       "mplsLspNotifications": mplsLspNotifications,
       "mplsInfo": mplsInfo,
       "mplsVersion": mplsVersion,
       "brcdMplsAdminGroupTable": brcdMplsAdminGroupTable,
       "brcdMplsAdminGroupEntry": brcdMplsAdminGroupEntry,
       "brcdMplsAdminGroupId": brcdMplsAdminGroupId,
       "brcdMplsAdminGroupName": brcdMplsAdminGroupName,
       "brcdMplsAdminGroupRowStatus": brcdMplsAdminGroupRowStatus,
       "brcdMplsInterfaceTable": brcdMplsInterfaceTable,
       "brcdMplsInterfaceEntry": brcdMplsInterfaceEntry,
       "brcdMplsInterfaceIndex": brcdMplsInterfaceIndex,
       "brcdMplsInterfaceAdminGroup": brcdMplsInterfaceAdminGroup,
       "brcdMplsInterfaceRowStatus": brcdMplsInterfaceRowStatus,
       "mplsLspInfo": mplsLspInfo,
       "mplsConfiguredLsps": mplsConfiguredLsps,
       "mplsActiveLsps": mplsActiveLsps,
       "mplsLspTable": mplsLspTable,
       "mplsLspEntry": mplsLspEntry,
       "mplsLspSignalingProto": mplsLspSignalingProto,
       "mplsLspIndex": mplsLspIndex,
       "mplsLspName": mplsLspName,
       "mplsLspState": mplsLspState,
       "mplsLspPackets": mplsLspPackets,
       "mplsLspAge": mplsLspAge,
       "mplsLspTimeUp": mplsLspTimeUp,
       "mplsLspPrimaryTimeUp": mplsLspPrimaryTimeUp,
       "mplsLspTransitions": mplsLspTransitions,
       "mplsLspLastTransition": mplsLspLastTransition,
       "mplsLspFrom": mplsLspFrom,
       "mplsLspTo": mplsLspTo,
       "mplsLspPathName": mplsLspPathName,
       "mplsLspPathType": mplsLspPathType,
       "mplsLspAdaptive": mplsLspAdaptive,
       "mplsLspBfdSessionId": mplsLspBfdSessionId,
       "mplsLspReoptimizeTimer": mplsLspReoptimizeTimer,
       "mplsLspCoS": mplsLspCoS,
       "mplsLspHopLimit": mplsLspHopLimit,
       "mplsLspCspf": mplsLspCspf,
       "mplsLspCspfTieBreaker": mplsLspCspfTieBreaker,
       "mplsLspFrrMode": mplsLspFrrMode,
       "mplsLspFrrSetupPriority": mplsLspFrrSetupPriority,
       "mplsLspFrrHoldingPriority": mplsLspFrrHoldingPriority,
       "mplsLspFrrHopLimit": mplsLspFrrHopLimit,
       "mplsLspFrrBandwidth": mplsLspFrrBandwidth,
       "mplsLspFrrAdmGrpIncludeAny": mplsLspFrrAdmGrpIncludeAny,
       "mplsLspFrrAdmGrpIncludeAll": mplsLspFrrAdmGrpIncludeAll,
       "mplsLspFrrAdmGrpExcludeAny": mplsLspFrrAdmGrpExcludeAny,
       "mplsLspPathSelectMode": mplsLspPathSelectMode,
       "mplsLspPathSelectPathname": mplsLspPathSelectPathname,
       "mplsLspPathSelectRevertTimer": mplsLspPathSelectRevertTimer,
       "mplsLspShortcutOspfAllowed": mplsLspShortcutOspfAllowed,
       "mplsLspShortcutIsisAllowed": mplsLspShortcutIsisAllowed,
       "mplsLspShortcutIsisLevel": mplsLspShortcutIsisLevel,
       "mplsLspShortcutIsisAnnounce": mplsLspShortcutIsisAnnounce,
       "mplsLspShortcutIsisAnnounceMetric": mplsLspShortcutIsisAnnounceMetric,
       "mplsLspShortcutIsisRelativeMetric": mplsLspShortcutIsisRelativeMetric,
       "mplsVllInfo": mplsVllInfo,
       "mplsVplsInfo": mplsVplsInfo}
)
