# SNMP MIB module (MPLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MPLS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:21 2024
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

(jnxMibs,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

mpls = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2)
)
mpls.setRevisions(
        ("2009-02-23 14:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MplsLspTraps_ObjectIdentity = ObjectIdentity
mplsLspTraps = _MplsLspTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 0)
)
_MplsInfo_ObjectIdentity = ObjectIdentity
mplsInfo = _MplsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 1)
)
_MplsVersion_Type = Integer32
_MplsVersion_Object = MibScalar
mplsVersion = _MplsVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 1, 1),
    _MplsVersion_Type()
)
mplsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsVersion.setStatus("current")


class _MplsSignalingProto_Type(Integer32):
    """Custom type mplsSignalingProto based on Integer32"""
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
        *(("ldp", 4),
          ("none", 1),
          ("other", 2),
          ("rsvp", 3))
    )


_MplsSignalingProto_Type.__name__ = "Integer32"
_MplsSignalingProto_Object = MibScalar
mplsSignalingProto = _MplsSignalingProto_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 1, 2),
    _MplsSignalingProto_Type()
)
mplsSignalingProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsSignalingProto.setStatus("current")
_MplsConfiguredLsps_Type = Integer32
_MplsConfiguredLsps_Object = MibScalar
mplsConfiguredLsps = _MplsConfiguredLsps_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 1, 3),
    _MplsConfiguredLsps_Type()
)
mplsConfiguredLsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsConfiguredLsps.setStatus("current")
_MplsActiveLsps_Type = Integer32
_MplsActiveLsps_Object = MibScalar
mplsActiveLsps = _MplsActiveLsps_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 1, 4),
    _MplsActiveLsps_Type()
)
mplsActiveLsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsActiveLsps.setStatus("current")
_MplsTEInfo_ObjectIdentity = ObjectIdentity
mplsTEInfo = _MplsTEInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 2)
)


class _MplsTEDistProtocol_Type(Integer32):
    """Custom type mplsTEDistProtocol based on Integer32"""
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
        *(("isis", 2),
          ("isis-ospf", 4),
          ("none", 1),
          ("ospf", 3))
    )


_MplsTEDistProtocol_Type.__name__ = "Integer32"
_MplsTEDistProtocol_Object = MibScalar
mplsTEDistProtocol = _MplsTEDistProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 2, 1),
    _MplsTEDistProtocol_Type()
)
mplsTEDistProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTEDistProtocol.setStatus("current")
_MplsAdminGroupList_Object = MibTable
mplsAdminGroupList = _MplsAdminGroupList_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    mplsAdminGroupList.setStatus("current")
_MplsAdminGroup_Object = MibTableRow
mplsAdminGroup = _MplsAdminGroup_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 2, 2, 1)
)
mplsAdminGroup.setIndexNames(
    (0, "MPLS-MIB", "mplsAdminGroupNumber"),
)
if mibBuilder.loadTexts:
    mplsAdminGroup.setStatus("current")


class _MplsAdminGroupNumber_Type(Integer32):
    """Custom type mplsAdminGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_MplsAdminGroupNumber_Type.__name__ = "Integer32"
_MplsAdminGroupNumber_Object = MibTableColumn
mplsAdminGroupNumber = _MplsAdminGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 2, 2, 1, 1),
    _MplsAdminGroupNumber_Type()
)
mplsAdminGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsAdminGroupNumber.setStatus("current")


class _MplsAdminGroupName_Type(DisplayString):
    """Custom type mplsAdminGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MplsAdminGroupName_Type.__name__ = "DisplayString"
_MplsAdminGroupName_Object = MibTableColumn
mplsAdminGroupName = _MplsAdminGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 2, 2, 1, 2),
    _MplsAdminGroupName_Type()
)
mplsAdminGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsAdminGroupName.setStatus("current")
_MplsLspList_Object = MibTable
mplsLspList = _MplsLspList_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3)
)
if mibBuilder.loadTexts:
    mplsLspList.setStatus("deprecated")
_MplsLspEntry_Object = MibTableRow
mplsLspEntry = _MplsLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1)
)
mplsLspEntry.setIndexNames(
    (0, "MPLS-MIB", "mplsLspName"),
)
if mibBuilder.loadTexts:
    mplsLspEntry.setStatus("deprecated")


class _MplsLspName_Type(DisplayString):
    """Custom type mplsLspName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_MplsLspName_Type.__name__ = "DisplayString"
_MplsLspName_Object = MibTableColumn
mplsLspName = _MplsLspName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 1),
    _MplsLspName_Type()
)
mplsLspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspName.setStatus("deprecated")


class _MplsLspState_Type(Integer32):
    """Custom type mplsLspState based on Integer32"""
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
        *(("backupActive", 5),
          ("down", 3),
          ("notInService", 4),
          ("unknown", 1),
          ("up", 2))
    )


_MplsLspState_Type.__name__ = "Integer32"
_MplsLspState_Object = MibTableColumn
mplsLspState = _MplsLspState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 2),
    _MplsLspState_Type()
)
mplsLspState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspState.setStatus("deprecated")
_MplsLspOctets_Type = Counter64
_MplsLspOctets_Object = MibTableColumn
mplsLspOctets = _MplsLspOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 3),
    _MplsLspOctets_Type()
)
mplsLspOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspOctets.setStatus("deprecated")
_MplsLspPackets_Type = Counter64
_MplsLspPackets_Object = MibTableColumn
mplsLspPackets = _MplsLspPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 4),
    _MplsLspPackets_Type()
)
mplsLspPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspPackets.setStatus("deprecated")
_MplsLspAge_Type = TimeStamp
_MplsLspAge_Object = MibTableColumn
mplsLspAge = _MplsLspAge_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 5),
    _MplsLspAge_Type()
)
mplsLspAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspAge.setStatus("deprecated")
_MplsLspTimeUp_Type = TimeStamp
_MplsLspTimeUp_Object = MibTableColumn
mplsLspTimeUp = _MplsLspTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 6),
    _MplsLspTimeUp_Type()
)
mplsLspTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspTimeUp.setStatus("deprecated")
_MplsLspPrimaryTimeUp_Type = TimeStamp
_MplsLspPrimaryTimeUp_Object = MibTableColumn
mplsLspPrimaryTimeUp = _MplsLspPrimaryTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 7),
    _MplsLspPrimaryTimeUp_Type()
)
mplsLspPrimaryTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspPrimaryTimeUp.setStatus("deprecated")
_MplsLspTransitions_Type = Counter32
_MplsLspTransitions_Object = MibTableColumn
mplsLspTransitions = _MplsLspTransitions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 8),
    _MplsLspTransitions_Type()
)
mplsLspTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspTransitions.setStatus("deprecated")
_MplsLspLastTransition_Type = TimeStamp
_MplsLspLastTransition_Object = MibTableColumn
mplsLspLastTransition = _MplsLspLastTransition_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 9),
    _MplsLspLastTransition_Type()
)
mplsLspLastTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspLastTransition.setStatus("deprecated")
_MplsLspPathChanges_Type = Counter32
_MplsLspPathChanges_Object = MibTableColumn
mplsLspPathChanges = _MplsLspPathChanges_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 10),
    _MplsLspPathChanges_Type()
)
mplsLspPathChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspPathChanges.setStatus("deprecated")
_MplsLspLastPathChange_Type = TimeStamp
_MplsLspLastPathChange_Object = MibTableColumn
mplsLspLastPathChange = _MplsLspLastPathChange_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 11),
    _MplsLspLastPathChange_Type()
)
mplsLspLastPathChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspLastPathChange.setStatus("deprecated")
_MplsLspConfiguredPaths_Type = Integer32
_MplsLspConfiguredPaths_Object = MibTableColumn
mplsLspConfiguredPaths = _MplsLspConfiguredPaths_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 12),
    _MplsLspConfiguredPaths_Type()
)
mplsLspConfiguredPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspConfiguredPaths.setStatus("deprecated")
_MplsLspStandbyPaths_Type = Integer32
_MplsLspStandbyPaths_Object = MibTableColumn
mplsLspStandbyPaths = _MplsLspStandbyPaths_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 13),
    _MplsLspStandbyPaths_Type()
)
mplsLspStandbyPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspStandbyPaths.setStatus("deprecated")
_MplsLspOperationalPaths_Type = Integer32
_MplsLspOperationalPaths_Object = MibTableColumn
mplsLspOperationalPaths = _MplsLspOperationalPaths_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 14),
    _MplsLspOperationalPaths_Type()
)
mplsLspOperationalPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspOperationalPaths.setStatus("deprecated")
_MplsLspFrom_Type = IpAddress
_MplsLspFrom_Object = MibTableColumn
mplsLspFrom = _MplsLspFrom_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 15),
    _MplsLspFrom_Type()
)
mplsLspFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspFrom.setStatus("deprecated")
_MplsLspTo_Type = IpAddress
_MplsLspTo_Object = MibTableColumn
mplsLspTo = _MplsLspTo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 16),
    _MplsLspTo_Type()
)
mplsLspTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspTo.setStatus("deprecated")


class _MplsPathName_Type(DisplayString):
    """Custom type mplsPathName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MplsPathName_Type.__name__ = "DisplayString"
_MplsPathName_Object = MibTableColumn
mplsPathName = _MplsPathName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 17),
    _MplsPathName_Type()
)
mplsPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsPathName.setStatus("deprecated")


class _MplsPathType_Type(Integer32):
    """Custom type mplsPathType based on Integer32"""
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
        *(("bypass", 5),
          ("other", 1),
          ("primary", 2),
          ("secondary", 4),
          ("standby", 3))
    )


_MplsPathType_Type.__name__ = "Integer32"
_MplsPathType_Object = MibTableColumn
mplsPathType = _MplsPathType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 18),
    _MplsPathType_Type()
)
mplsPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsPathType.setStatus("deprecated")


class _MplsPathExplicitRoute_Type(OctetString):
    """Custom type mplsPathExplicitRoute based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_MplsPathExplicitRoute_Type.__name__ = "OctetString"
_MplsPathExplicitRoute_Object = MibTableColumn
mplsPathExplicitRoute = _MplsPathExplicitRoute_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 19),
    _MplsPathExplicitRoute_Type()
)
mplsPathExplicitRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsPathExplicitRoute.setStatus("deprecated")


class _MplsPathRecordRoute_Type(OctetString):
    """Custom type mplsPathRecordRoute based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_MplsPathRecordRoute_Type.__name__ = "OctetString"
_MplsPathRecordRoute_Object = MibTableColumn
mplsPathRecordRoute = _MplsPathRecordRoute_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 20),
    _MplsPathRecordRoute_Type()
)
mplsPathRecordRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsPathRecordRoute.setStatus("deprecated")
_MplsPathBandwidth_Type = Integer32
_MplsPathBandwidth_Object = MibTableColumn
mplsPathBandwidth = _MplsPathBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 21),
    _MplsPathBandwidth_Type()
)
mplsPathBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsPathBandwidth.setStatus("deprecated")


class _MplsPathCOS_Type(Integer32):
    """Custom type mplsPathCOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_MplsPathCOS_Type.__name__ = "Integer32"
_MplsPathCOS_Object = MibTableColumn
mplsPathCOS = _MplsPathCOS_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 22),
    _MplsPathCOS_Type()
)
mplsPathCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsPathCOS.setStatus("deprecated")
_MplsPathInclude_Type = Integer32
_MplsPathInclude_Object = MibTableColumn
mplsPathInclude = _MplsPathInclude_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 23),
    _MplsPathInclude_Type()
)
mplsPathInclude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsPathInclude.setStatus("deprecated")
_MplsPathExclude_Type = Integer32
_MplsPathExclude_Object = MibTableColumn
mplsPathExclude = _MplsPathExclude_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 24),
    _MplsPathExclude_Type()
)
mplsPathExclude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsPathExclude.setStatus("deprecated")


class _MplsPathSetupPriority_Type(Integer32):
    """Custom type mplsPathSetupPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MplsPathSetupPriority_Type.__name__ = "Integer32"
_MplsPathSetupPriority_Object = MibTableColumn
mplsPathSetupPriority = _MplsPathSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 25),
    _MplsPathSetupPriority_Type()
)
mplsPathSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsPathSetupPriority.setStatus("deprecated")


class _MplsPathHoldPriority_Type(Integer32):
    """Custom type mplsPathHoldPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MplsPathHoldPriority_Type.__name__ = "Integer32"
_MplsPathHoldPriority_Object = MibTableColumn
mplsPathHoldPriority = _MplsPathHoldPriority_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 26),
    _MplsPathHoldPriority_Type()
)
mplsPathHoldPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsPathHoldPriority.setStatus("deprecated")


class _MplsPathProperties_Type(Integer32):
    """Custom type mplsPathProperties based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 2),
          ("cspf", 4),
          ("fast-reroute", 64),
          ("mergeable", 8),
          ("preemptable", 16),
          ("preemptive", 32),
          ("record-route", 1))
    )


_MplsPathProperties_Type.__name__ = "Integer32"
_MplsPathProperties_Object = MibTableColumn
mplsPathProperties = _MplsPathProperties_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 3, 1, 27),
    _MplsPathProperties_Type()
)
mplsPathProperties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsPathProperties.setStatus("deprecated")
_MplsTraps_ObjectIdentity = ObjectIdentity
mplsTraps = _MplsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 4)
)
_MplsLspInfoList_Object = MibTable
mplsLspInfoList = _MplsLspInfoList_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5)
)
if mibBuilder.loadTexts:
    mplsLspInfoList.setStatus("current")
_MplsLspInfoEntry_Object = MibTableRow
mplsLspInfoEntry = _MplsLspInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1)
)
mplsLspInfoEntry.setIndexNames(
    (1, "MPLS-MIB", "mplsLspInfoName"),
)
if mibBuilder.loadTexts:
    mplsLspInfoEntry.setStatus("current")


class _MplsLspInfoName_Type(DisplayString):
    """Custom type mplsLspInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_MplsLspInfoName_Type.__name__ = "DisplayString"
_MplsLspInfoName_Object = MibTableColumn
mplsLspInfoName = _MplsLspInfoName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 1),
    _MplsLspInfoName_Type()
)
mplsLspInfoName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mplsLspInfoName.setStatus("current")


class _MplsLspInfoState_Type(Integer32):
    """Custom type mplsLspInfoState based on Integer32"""
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
        *(("backupActive", 5),
          ("down", 3),
          ("notInService", 4),
          ("unknown", 1),
          ("up", 2))
    )


_MplsLspInfoState_Type.__name__ = "Integer32"
_MplsLspInfoState_Object = MibTableColumn
mplsLspInfoState = _MplsLspInfoState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 2),
    _MplsLspInfoState_Type()
)
mplsLspInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspInfoState.setStatus("current")
_MplsLspInfoOctets_Type = Counter64
_MplsLspInfoOctets_Object = MibTableColumn
mplsLspInfoOctets = _MplsLspInfoOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 3),
    _MplsLspInfoOctets_Type()
)
mplsLspInfoOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspInfoOctets.setStatus("current")
_MplsLspInfoPackets_Type = Counter64
_MplsLspInfoPackets_Object = MibTableColumn
mplsLspInfoPackets = _MplsLspInfoPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 4),
    _MplsLspInfoPackets_Type()
)
mplsLspInfoPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspInfoPackets.setStatus("current")
_MplsLspInfoAge_Type = TimeStamp
_MplsLspInfoAge_Object = MibTableColumn
mplsLspInfoAge = _MplsLspInfoAge_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 5),
    _MplsLspInfoAge_Type()
)
mplsLspInfoAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspInfoAge.setStatus("current")
_MplsLspInfoTimeUp_Type = TimeStamp
_MplsLspInfoTimeUp_Object = MibTableColumn
mplsLspInfoTimeUp = _MplsLspInfoTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 6),
    _MplsLspInfoTimeUp_Type()
)
mplsLspInfoTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspInfoTimeUp.setStatus("current")
_MplsLspInfoPrimaryTimeUp_Type = TimeStamp
_MplsLspInfoPrimaryTimeUp_Object = MibTableColumn
mplsLspInfoPrimaryTimeUp = _MplsLspInfoPrimaryTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 7),
    _MplsLspInfoPrimaryTimeUp_Type()
)
mplsLspInfoPrimaryTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspInfoPrimaryTimeUp.setStatus("current")
_MplsLspInfoTransitions_Type = Counter32
_MplsLspInfoTransitions_Object = MibTableColumn
mplsLspInfoTransitions = _MplsLspInfoTransitions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 8),
    _MplsLspInfoTransitions_Type()
)
mplsLspInfoTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspInfoTransitions.setStatus("current")
_MplsLspInfoLastTransition_Type = TimeStamp
_MplsLspInfoLastTransition_Object = MibTableColumn
mplsLspInfoLastTransition = _MplsLspInfoLastTransition_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 9),
    _MplsLspInfoLastTransition_Type()
)
mplsLspInfoLastTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspInfoLastTransition.setStatus("current")
_MplsLspInfoPathChanges_Type = Counter32
_MplsLspInfoPathChanges_Object = MibTableColumn
mplsLspInfoPathChanges = _MplsLspInfoPathChanges_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 10),
    _MplsLspInfoPathChanges_Type()
)
mplsLspInfoPathChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspInfoPathChanges.setStatus("current")
_MplsLspInfoLastPathChange_Type = TimeStamp
_MplsLspInfoLastPathChange_Object = MibTableColumn
mplsLspInfoLastPathChange = _MplsLspInfoLastPathChange_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 11),
    _MplsLspInfoLastPathChange_Type()
)
mplsLspInfoLastPathChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspInfoLastPathChange.setStatus("current")
_MplsLspInfoConfiguredPaths_Type = Integer32
_MplsLspInfoConfiguredPaths_Object = MibTableColumn
mplsLspInfoConfiguredPaths = _MplsLspInfoConfiguredPaths_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 12),
    _MplsLspInfoConfiguredPaths_Type()
)
mplsLspInfoConfiguredPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspInfoConfiguredPaths.setStatus("current")
_MplsLspInfoStandbyPaths_Type = Integer32
_MplsLspInfoStandbyPaths_Object = MibTableColumn
mplsLspInfoStandbyPaths = _MplsLspInfoStandbyPaths_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 13),
    _MplsLspInfoStandbyPaths_Type()
)
mplsLspInfoStandbyPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspInfoStandbyPaths.setStatus("current")
_MplsLspInfoOperationalPaths_Type = Integer32
_MplsLspInfoOperationalPaths_Object = MibTableColumn
mplsLspInfoOperationalPaths = _MplsLspInfoOperationalPaths_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 14),
    _MplsLspInfoOperationalPaths_Type()
)
mplsLspInfoOperationalPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspInfoOperationalPaths.setStatus("current")
_MplsLspInfoFrom_Type = IpAddress
_MplsLspInfoFrom_Object = MibTableColumn
mplsLspInfoFrom = _MplsLspInfoFrom_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 15),
    _MplsLspInfoFrom_Type()
)
mplsLspInfoFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspInfoFrom.setStatus("current")
_MplsLspInfoTo_Type = IpAddress
_MplsLspInfoTo_Object = MibTableColumn
mplsLspInfoTo = _MplsLspInfoTo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 16),
    _MplsLspInfoTo_Type()
)
mplsLspInfoTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspInfoTo.setStatus("current")


class _MplsPathInfoName_Type(DisplayString):
    """Custom type mplsPathInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MplsPathInfoName_Type.__name__ = "DisplayString"
_MplsPathInfoName_Object = MibTableColumn
mplsPathInfoName = _MplsPathInfoName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 17),
    _MplsPathInfoName_Type()
)
mplsPathInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsPathInfoName.setStatus("current")


class _MplsPathInfoType_Type(Integer32):
    """Custom type mplsPathInfoType based on Integer32"""
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
        *(("bypass", 5),
          ("other", 1),
          ("primary", 2),
          ("secondary", 4),
          ("standby", 3))
    )


_MplsPathInfoType_Type.__name__ = "Integer32"
_MplsPathInfoType_Object = MibTableColumn
mplsPathInfoType = _MplsPathInfoType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 18),
    _MplsPathInfoType_Type()
)
mplsPathInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsPathInfoType.setStatus("current")


class _MplsPathInfoExplicitRoute_Type(OctetString):
    """Custom type mplsPathInfoExplicitRoute based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_MplsPathInfoExplicitRoute_Type.__name__ = "OctetString"
_MplsPathInfoExplicitRoute_Object = MibTableColumn
mplsPathInfoExplicitRoute = _MplsPathInfoExplicitRoute_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 19),
    _MplsPathInfoExplicitRoute_Type()
)
mplsPathInfoExplicitRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsPathInfoExplicitRoute.setStatus("current")


class _MplsPathInfoRecordRoute_Type(OctetString):
    """Custom type mplsPathInfoRecordRoute based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_MplsPathInfoRecordRoute_Type.__name__ = "OctetString"
_MplsPathInfoRecordRoute_Object = MibTableColumn
mplsPathInfoRecordRoute = _MplsPathInfoRecordRoute_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 20),
    _MplsPathInfoRecordRoute_Type()
)
mplsPathInfoRecordRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsPathInfoRecordRoute.setStatus("current")
_MplsPathInfoBandwidth_Type = Integer32
_MplsPathInfoBandwidth_Object = MibTableColumn
mplsPathInfoBandwidth = _MplsPathInfoBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 21),
    _MplsPathInfoBandwidth_Type()
)
mplsPathInfoBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsPathInfoBandwidth.setStatus("current")


class _MplsPathInfoCOS_Type(Integer32):
    """Custom type mplsPathInfoCOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_MplsPathInfoCOS_Type.__name__ = "Integer32"
_MplsPathInfoCOS_Object = MibTableColumn
mplsPathInfoCOS = _MplsPathInfoCOS_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 22),
    _MplsPathInfoCOS_Type()
)
mplsPathInfoCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsPathInfoCOS.setStatus("current")
_MplsPathInfoInclude_Type = Integer32
_MplsPathInfoInclude_Object = MibTableColumn
mplsPathInfoInclude = _MplsPathInfoInclude_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 23),
    _MplsPathInfoInclude_Type()
)
mplsPathInfoInclude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsPathInfoInclude.setStatus("current")
_MplsPathInfoExclude_Type = Integer32
_MplsPathInfoExclude_Object = MibTableColumn
mplsPathInfoExclude = _MplsPathInfoExclude_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 24),
    _MplsPathInfoExclude_Type()
)
mplsPathInfoExclude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsPathInfoExclude.setStatus("current")


class _MplsPathInfoSetupPriority_Type(Integer32):
    """Custom type mplsPathInfoSetupPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MplsPathInfoSetupPriority_Type.__name__ = "Integer32"
_MplsPathInfoSetupPriority_Object = MibTableColumn
mplsPathInfoSetupPriority = _MplsPathInfoSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 25),
    _MplsPathInfoSetupPriority_Type()
)
mplsPathInfoSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsPathInfoSetupPriority.setStatus("current")


class _MplsPathInfoHoldPriority_Type(Integer32):
    """Custom type mplsPathInfoHoldPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MplsPathInfoHoldPriority_Type.__name__ = "Integer32"
_MplsPathInfoHoldPriority_Object = MibTableColumn
mplsPathInfoHoldPriority = _MplsPathInfoHoldPriority_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 26),
    _MplsPathInfoHoldPriority_Type()
)
mplsPathInfoHoldPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsPathInfoHoldPriority.setStatus("current")


class _MplsPathInfoProperties_Type(Integer32):
    """Custom type mplsPathInfoProperties based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 2),
          ("cspf", 4),
          ("fast-reroute", 64),
          ("mergeable", 8),
          ("preemptable", 16),
          ("preemptive", 32),
          ("record-route", 1))
    )


_MplsPathInfoProperties_Type.__name__ = "Integer32"
_MplsPathInfoProperties_Object = MibTableColumn
mplsPathInfoProperties = _MplsPathInfoProperties_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 27),
    _MplsPathInfoProperties_Type()
)
mplsPathInfoProperties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsPathInfoProperties.setStatus("current")
_MplsLspInfoAggrOctets_Type = Counter64
_MplsLspInfoAggrOctets_Object = MibTableColumn
mplsLspInfoAggrOctets = _MplsLspInfoAggrOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 28),
    _MplsLspInfoAggrOctets_Type()
)
mplsLspInfoAggrOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspInfoAggrOctets.setStatus("current")
_MplsLspInfoAggrPackets_Type = Counter64
_MplsLspInfoAggrPackets_Object = MibTableColumn
mplsLspInfoAggrPackets = _MplsLspInfoAggrPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 29),
    _MplsLspInfoAggrPackets_Type()
)
mplsLspInfoAggrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLspInfoAggrPackets.setStatus("current")


class _MplsPathInfoRecordRouteWithLabels_Type(OctetString):
    """Custom type mplsPathInfoRecordRouteWithLabels based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_MplsPathInfoRecordRouteWithLabels_Type.__name__ = "OctetString"
_MplsPathInfoRecordRouteWithLabels_Object = MibTableColumn
mplsPathInfoRecordRouteWithLabels = _MplsPathInfoRecordRouteWithLabels_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 5, 1, 30),
    _MplsPathInfoRecordRouteWithLabels_Type()
)
mplsPathInfoRecordRouteWithLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsPathInfoRecordRouteWithLabels.setStatus("current")

# Managed Objects groups


# Notification objects

mplsLspInfoUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 0, 1)
)
mplsLspInfoUp.setObjects(
      *(("MPLS-MIB", "mplsLspInfoName"),
        ("MPLS-MIB", "mplsPathInfoName"))
)
if mibBuilder.loadTexts:
    mplsLspInfoUp.setStatus(
        "current"
    )

mplsLspInfoDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 0, 2)
)
mplsLspInfoDown.setObjects(
      *(("MPLS-MIB", "mplsLspInfoName"),
        ("MPLS-MIB", "mplsPathInfoName"))
)
if mibBuilder.loadTexts:
    mplsLspInfoDown.setStatus(
        "current"
    )

mplsLspInfoChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 0, 3)
)
mplsLspInfoChange.setObjects(
      *(("MPLS-MIB", "mplsLspInfoName"),
        ("MPLS-MIB", "mplsPathInfoName"))
)
if mibBuilder.loadTexts:
    mplsLspInfoChange.setStatus(
        "current"
    )

mplsLspInfoPathDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 0, 4)
)
mplsLspInfoPathDown.setObjects(
      *(("MPLS-MIB", "mplsLspInfoName"),
        ("MPLS-MIB", "mplsPathInfoName"))
)
if mibBuilder.loadTexts:
    mplsLspInfoPathDown.setStatus(
        "current"
    )

mplsLspInfoPathUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 0, 5)
)
mplsLspInfoPathUp.setObjects(
      *(("MPLS-MIB", "mplsLspInfoName"),
        ("MPLS-MIB", "mplsPathInfoName"))
)
if mibBuilder.loadTexts:
    mplsLspInfoPathUp.setStatus(
        "current"
    )

mplsLspUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 4, 1)
)
mplsLspUp.setObjects(
      *(("MPLS-MIB", "mplsLspName"),
        ("MPLS-MIB", "mplsPathName"))
)
if mibBuilder.loadTexts:
    mplsLspUp.setStatus(
        "deprecated"
    )

mplsLspDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 4, 2)
)
mplsLspDown.setObjects(
      *(("MPLS-MIB", "mplsLspName"),
        ("MPLS-MIB", "mplsPathName"))
)
if mibBuilder.loadTexts:
    mplsLspDown.setStatus(
        "deprecated"
    )

mplsLspChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 4, 3)
)
mplsLspChange.setObjects(
      *(("MPLS-MIB", "mplsLspName"),
        ("MPLS-MIB", "mplsPathName"))
)
if mibBuilder.loadTexts:
    mplsLspChange.setStatus(
        "deprecated"
    )

mplsLspPathDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 4, 4)
)
mplsLspPathDown.setObjects(
      *(("MPLS-MIB", "mplsLspName"),
        ("MPLS-MIB", "mplsPathName"))
)
if mibBuilder.loadTexts:
    mplsLspPathDown.setStatus(
        "deprecated"
    )

mplsLspPathUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 2, 4, 5)
)
mplsLspPathUp.setObjects(
      *(("MPLS-MIB", "mplsLspName"),
        ("MPLS-MIB", "mplsPathName"))
)
if mibBuilder.loadTexts:
    mplsLspPathUp.setStatus(
        "deprecated"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPLS-MIB",
    **{"mpls": mpls,
       "mplsLspTraps": mplsLspTraps,
       "mplsLspInfoUp": mplsLspInfoUp,
       "mplsLspInfoDown": mplsLspInfoDown,
       "mplsLspInfoChange": mplsLspInfoChange,
       "mplsLspInfoPathDown": mplsLspInfoPathDown,
       "mplsLspInfoPathUp": mplsLspInfoPathUp,
       "mplsInfo": mplsInfo,
       "mplsVersion": mplsVersion,
       "mplsSignalingProto": mplsSignalingProto,
       "mplsConfiguredLsps": mplsConfiguredLsps,
       "mplsActiveLsps": mplsActiveLsps,
       "mplsTEInfo": mplsTEInfo,
       "mplsTEDistProtocol": mplsTEDistProtocol,
       "mplsAdminGroupList": mplsAdminGroupList,
       "mplsAdminGroup": mplsAdminGroup,
       "mplsAdminGroupNumber": mplsAdminGroupNumber,
       "mplsAdminGroupName": mplsAdminGroupName,
       "mplsLspList": mplsLspList,
       "mplsLspEntry": mplsLspEntry,
       "mplsLspName": mplsLspName,
       "mplsLspState": mplsLspState,
       "mplsLspOctets": mplsLspOctets,
       "mplsLspPackets": mplsLspPackets,
       "mplsLspAge": mplsLspAge,
       "mplsLspTimeUp": mplsLspTimeUp,
       "mplsLspPrimaryTimeUp": mplsLspPrimaryTimeUp,
       "mplsLspTransitions": mplsLspTransitions,
       "mplsLspLastTransition": mplsLspLastTransition,
       "mplsLspPathChanges": mplsLspPathChanges,
       "mplsLspLastPathChange": mplsLspLastPathChange,
       "mplsLspConfiguredPaths": mplsLspConfiguredPaths,
       "mplsLspStandbyPaths": mplsLspStandbyPaths,
       "mplsLspOperationalPaths": mplsLspOperationalPaths,
       "mplsLspFrom": mplsLspFrom,
       "mplsLspTo": mplsLspTo,
       "mplsPathName": mplsPathName,
       "mplsPathType": mplsPathType,
       "mplsPathExplicitRoute": mplsPathExplicitRoute,
       "mplsPathRecordRoute": mplsPathRecordRoute,
       "mplsPathBandwidth": mplsPathBandwidth,
       "mplsPathCOS": mplsPathCOS,
       "mplsPathInclude": mplsPathInclude,
       "mplsPathExclude": mplsPathExclude,
       "mplsPathSetupPriority": mplsPathSetupPriority,
       "mplsPathHoldPriority": mplsPathHoldPriority,
       "mplsPathProperties": mplsPathProperties,
       "mplsTraps": mplsTraps,
       "mplsLspUp": mplsLspUp,
       "mplsLspDown": mplsLspDown,
       "mplsLspChange": mplsLspChange,
       "mplsLspPathDown": mplsLspPathDown,
       "mplsLspPathUp": mplsLspPathUp,
       "mplsLspInfoList": mplsLspInfoList,
       "mplsLspInfoEntry": mplsLspInfoEntry,
       "mplsLspInfoName": mplsLspInfoName,
       "mplsLspInfoState": mplsLspInfoState,
       "mplsLspInfoOctets": mplsLspInfoOctets,
       "mplsLspInfoPackets": mplsLspInfoPackets,
       "mplsLspInfoAge": mplsLspInfoAge,
       "mplsLspInfoTimeUp": mplsLspInfoTimeUp,
       "mplsLspInfoPrimaryTimeUp": mplsLspInfoPrimaryTimeUp,
       "mplsLspInfoTransitions": mplsLspInfoTransitions,
       "mplsLspInfoLastTransition": mplsLspInfoLastTransition,
       "mplsLspInfoPathChanges": mplsLspInfoPathChanges,
       "mplsLspInfoLastPathChange": mplsLspInfoLastPathChange,
       "mplsLspInfoConfiguredPaths": mplsLspInfoConfiguredPaths,
       "mplsLspInfoStandbyPaths": mplsLspInfoStandbyPaths,
       "mplsLspInfoOperationalPaths": mplsLspInfoOperationalPaths,
       "mplsLspInfoFrom": mplsLspInfoFrom,
       "mplsLspInfoTo": mplsLspInfoTo,
       "mplsPathInfoName": mplsPathInfoName,
       "mplsPathInfoType": mplsPathInfoType,
       "mplsPathInfoExplicitRoute": mplsPathInfoExplicitRoute,
       "mplsPathInfoRecordRoute": mplsPathInfoRecordRoute,
       "mplsPathInfoBandwidth": mplsPathInfoBandwidth,
       "mplsPathInfoCOS": mplsPathInfoCOS,
       "mplsPathInfoInclude": mplsPathInfoInclude,
       "mplsPathInfoExclude": mplsPathInfoExclude,
       "mplsPathInfoSetupPriority": mplsPathInfoSetupPriority,
       "mplsPathInfoHoldPriority": mplsPathInfoHoldPriority,
       "mplsPathInfoProperties": mplsPathInfoProperties,
       "mplsLspInfoAggrOctets": mplsLspInfoAggrOctets,
       "mplsLspInfoAggrPackets": mplsLspInfoAggrPackets,
       "mplsPathInfoRecordRouteWithLabels": mplsPathInfoRecordRouteWithLabels}
)
