# SNMP MIB module (SONUS-ISUP-SERVICE-GROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-ISUP-SERVICE-GROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:01 2024
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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(sonusEventClass,
 sonusEventDescription,
 sonusEventLevel) = mibBuilder.importSymbols(
    "SONUS-COMMON-MIB",
    "sonusEventClass",
    "sonusEventDescription",
    "sonusEventLevel")

(sonusSignallingMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusSignallingMIBs")

(PointCode,
 SonusAdminState,
 SonusName,
 SonusNameReference,
 SonusPointCode,
 SonusSupportFlag) = mibBuilder.importSymbols(
    "SONUS-TC",
    "PointCode",
    "SonusAdminState",
    "SonusName",
    "SonusNameReference",
    "SonusPointCode",
    "SonusSupportFlag")


# MODULE-IDENTITY

sonusIsupServiceGroupMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusIsupServiceGroupMIBObjects_ObjectIdentity = ObjectIdentity
sonusIsupServiceGroupMIBObjects = _SonusIsupServiceGroupMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1)
)
_SonusIsupsgServiceGroup_ObjectIdentity = ObjectIdentity
sonusIsupsgServiceGroup = _SonusIsupsgServiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1)
)
_SonusIsupsgServiceGroupNextIndex_Type = Integer32
_SonusIsupsgServiceGroupNextIndex_Object = MibScalar
sonusIsupsgServiceGroupNextIndex = _SonusIsupsgServiceGroupNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 1),
    _SonusIsupsgServiceGroupNextIndex_Type()
)
sonusIsupsgServiceGroupNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupNextIndex.setStatus("current")
_SonusIsupsgServiceGroupTable_Object = MibTable
sonusIsupsgServiceGroupTable = _SonusIsupsgServiceGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupTable.setStatus("current")
_SonusIsupsgServiceGroupEntry_Object = MibTableRow
sonusIsupsgServiceGroupEntry = _SonusIsupsgServiceGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1)
)
sonusIsupsgServiceGroupEntry.setIndexNames(
    (0, "SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupsgServiceGroupListIndex"),
)
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupEntry.setStatus("current")


class _SonusIsupsgServiceGroupListIndex_Type(Integer32):
    """Custom type sonusIsupsgServiceGroupListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SonusIsupsgServiceGroupListIndex_Type.__name__ = "Integer32"
_SonusIsupsgServiceGroupListIndex_Object = MibTableColumn
sonusIsupsgServiceGroupListIndex = _SonusIsupsgServiceGroupListIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 1),
    _SonusIsupsgServiceGroupListIndex_Type()
)
sonusIsupsgServiceGroupListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupListIndex.setStatus("current")
_SonusIsupsgServiceGroupName_Type = SonusName
_SonusIsupsgServiceGroupName_Object = MibTableColumn
sonusIsupsgServiceGroupName = _SonusIsupsgServiceGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 2),
    _SonusIsupsgServiceGroupName_Type()
)
sonusIsupsgServiceGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupName.setStatus("current")
_SonusIsupsgServiceGroupRemotePointCode_Type = PointCode
_SonusIsupsgServiceGroupRemotePointCode_Object = MibTableColumn
sonusIsupsgServiceGroupRemotePointCode = _SonusIsupsgServiceGroupRemotePointCode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 3),
    _SonusIsupsgServiceGroupRemotePointCode_Type()
)
sonusIsupsgServiceGroupRemotePointCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupRemotePointCode.setStatus("current")
_SonusIsupsgServiceGroupTG_Type = SonusNameReference
_SonusIsupsgServiceGroupTG_Object = MibTableColumn
sonusIsupsgServiceGroupTG = _SonusIsupsgServiceGroupTG_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 4),
    _SonusIsupsgServiceGroupTG_Type()
)
sonusIsupsgServiceGroupTG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupTG.setStatus("current")


class _SonusIsupsgServiceGroupSwitchType_Type(Integer32):
    """Custom type sonusIsupsgServiceGroupSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dms100", 4),
          ("dms200", 3),
          ("dms250", 2),
          ("dms500", 1),
          ("lucent4ESS", 6),
          ("lucent5ESS", 5))
    )


_SonusIsupsgServiceGroupSwitchType_Type.__name__ = "Integer32"
_SonusIsupsgServiceGroupSwitchType_Object = MibTableColumn
sonusIsupsgServiceGroupSwitchType = _SonusIsupsgServiceGroupSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 5),
    _SonusIsupsgServiceGroupSwitchType_Type()
)
sonusIsupsgServiceGroupSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupSwitchType.setStatus("current")


class _SonusIsupsgServiceGroupRevision_Type(Integer32):
    """Custom type sonusIsupsgServiceGroupRevision based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ansi1992", 1),
          ("ansi1995", 2),
          ("belgacom", 9),
          ("etsi2", 4),
          ("itu1988", 7),
          ("itu1993", 3),
          ("itu1997", 6),
          ("ituq767", 8),
          ("nttfcc", 5))
    )


_SonusIsupsgServiceGroupRevision_Type.__name__ = "Integer32"
_SonusIsupsgServiceGroupRevision_Object = MibTableColumn
sonusIsupsgServiceGroupRevision = _SonusIsupsgServiceGroupRevision_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 6),
    _SonusIsupsgServiceGroupRevision_Type()
)
sonusIsupsgServiceGroupRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupRevision.setStatus("current")


class _SonusIsupsgServiceGroupHuntAlgorithm_Type(Integer32):
    """Custom type sonusIsupsgServiceGroupHuntAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("bottom2top", 1),
          ("circuithi2lo", 3),
          ("circuitlo2hi", 4),
          ("circularbottom2top", 6),
          ("circulartop2bottom", 7),
          ("mostnleastidle", 5),
          ("top2bottom", 2))
    )


_SonusIsupsgServiceGroupHuntAlgorithm_Type.__name__ = "Integer32"
_SonusIsupsgServiceGroupHuntAlgorithm_Object = MibTableColumn
sonusIsupsgServiceGroupHuntAlgorithm = _SonusIsupsgServiceGroupHuntAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 7),
    _SonusIsupsgServiceGroupHuntAlgorithm_Type()
)
sonusIsupsgServiceGroupHuntAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupHuntAlgorithm.setStatus("current")


class _SonusIsupsgServiceGroupCost_Type(Integer32):
    """Custom type sonusIsupsgServiceGroupCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SonusIsupsgServiceGroupCost_Type.__name__ = "Integer32"
_SonusIsupsgServiceGroupCost_Object = MibTableColumn
sonusIsupsgServiceGroupCost = _SonusIsupsgServiceGroupCost_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 8),
    _SonusIsupsgServiceGroupCost_Type()
)
sonusIsupsgServiceGroupCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupCost.setStatus("current")


class _SonusIsupsgServiceGroupCicControl_Type(Integer32):
    """Custom type sonusIsupsgServiceGroupCicControl based on Integer32"""
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
        *(("allCics", 4),
          ("evenCics", 3),
          ("noCics", 1),
          ("oddCics", 2))
    )


_SonusIsupsgServiceGroupCicControl_Type.__name__ = "Integer32"
_SonusIsupsgServiceGroupCicControl_Object = MibTableColumn
sonusIsupsgServiceGroupCicControl = _SonusIsupsgServiceGroupCicControl_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 9),
    _SonusIsupsgServiceGroupCicControl_Type()
)
sonusIsupsgServiceGroupCicControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupCicControl.setStatus("current")


class _SonusIsupsgServiceGroupContTestFreq_Type(Integer32):
    """Custom type sonusIsupsgServiceGroupContTestFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SonusIsupsgServiceGroupContTestFreq_Type.__name__ = "Integer32"
_SonusIsupsgServiceGroupContTestFreq_Object = MibTableColumn
sonusIsupsgServiceGroupContTestFreq = _SonusIsupsgServiceGroupContTestFreq_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 10),
    _SonusIsupsgServiceGroupContTestFreq_Type()
)
sonusIsupsgServiceGroupContTestFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupContTestFreq.setStatus("current")


class _SonusIsupsgServiceGroupOperation_Type(Integer32):
    """Custom type sonusIsupsgServiceGroupOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("reset", 3),
          ("unblock", 2))
    )


_SonusIsupsgServiceGroupOperation_Type.__name__ = "Integer32"
_SonusIsupsgServiceGroupOperation_Object = MibTableColumn
sonusIsupsgServiceGroupOperation = _SonusIsupsgServiceGroupOperation_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 11),
    _SonusIsupsgServiceGroupOperation_Type()
)
sonusIsupsgServiceGroupOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupOperation.setStatus("current")


class _SonusIsupsgServiceGroupMode_Type(Integer32):
    """Custom type sonusIsupsgServiceGroupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 2),
          ("outOfService", 1))
    )


_SonusIsupsgServiceGroupMode_Type.__name__ = "Integer32"
_SonusIsupsgServiceGroupMode_Object = MibTableColumn
sonusIsupsgServiceGroupMode = _SonusIsupsgServiceGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 12),
    _SonusIsupsgServiceGroupMode_Type()
)
sonusIsupsgServiceGroupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupMode.setStatus("current")


class _SonusIsupsgServiceGroupAction_Type(Integer32):
    """Custom type sonusIsupsgServiceGroupAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dryUp", 1),
          ("force", 2))
    )


_SonusIsupsgServiceGroupAction_Type.__name__ = "Integer32"
_SonusIsupsgServiceGroupAction_Object = MibTableColumn
sonusIsupsgServiceGroupAction = _SonusIsupsgServiceGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 13),
    _SonusIsupsgServiceGroupAction_Type()
)
sonusIsupsgServiceGroupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupAction.setStatus("current")


class _SonusIsupsgServiceGroupTimeout_Type(Integer32):
    """Custom type sonusIsupsgServiceGroupTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_SonusIsupsgServiceGroupTimeout_Type.__name__ = "Integer32"
_SonusIsupsgServiceGroupTimeout_Object = MibTableColumn
sonusIsupsgServiceGroupTimeout = _SonusIsupsgServiceGroupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 14),
    _SonusIsupsgServiceGroupTimeout_Type()
)
sonusIsupsgServiceGroupTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupTimeout.setStatus("current")
_SonusIsupsgServiceGroupAdminState_Type = SonusAdminState
_SonusIsupsgServiceGroupAdminState_Object = MibTableColumn
sonusIsupsgServiceGroupAdminState = _SonusIsupsgServiceGroupAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 15),
    _SonusIsupsgServiceGroupAdminState_Type()
)
sonusIsupsgServiceGroupAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupAdminState.setStatus("current")


class _SonusIsupsgServiceGroupProfileName_Type(DisplayString):
    """Custom type sonusIsupsgServiceGroupProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusIsupsgServiceGroupProfileName_Type.__name__ = "DisplayString"
_SonusIsupsgServiceGroupProfileName_Object = MibTableColumn
sonusIsupsgServiceGroupProfileName = _SonusIsupsgServiceGroupProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 16),
    _SonusIsupsgServiceGroupProfileName_Type()
)
sonusIsupsgServiceGroupProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupProfileName.setStatus("current")
_SonusIsupsgServiceGroupRowStatus_Type = RowStatus
_SonusIsupsgServiceGroupRowStatus_Object = MibTableColumn
sonusIsupsgServiceGroupRowStatus = _SonusIsupsgServiceGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 17),
    _SonusIsupsgServiceGroupRowStatus_Type()
)
sonusIsupsgServiceGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupRowStatus.setStatus("current")
_SonusIsupsgServiceGroupHopCounterState_Type = SonusAdminState
_SonusIsupsgServiceGroupHopCounterState_Object = MibTableColumn
sonusIsupsgServiceGroupHopCounterState = _SonusIsupsgServiceGroupHopCounterState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 18),
    _SonusIsupsgServiceGroupHopCounterState_Type()
)
sonusIsupsgServiceGroupHopCounterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupHopCounterState.setStatus("current")


class _SonusIsupsgServiceGroupHopCounterValue_Type(Integer32):
    """Custom type sonusIsupsgServiceGroupHopCounterValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 32),
    )


_SonusIsupsgServiceGroupHopCounterValue_Type.__name__ = "Integer32"
_SonusIsupsgServiceGroupHopCounterValue_Object = MibTableColumn
sonusIsupsgServiceGroupHopCounterValue = _SonusIsupsgServiceGroupHopCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 19),
    _SonusIsupsgServiceGroupHopCounterValue_Type()
)
sonusIsupsgServiceGroupHopCounterValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupHopCounterValue.setStatus("current")
_SonusIsupsgServiceGroupDiscTreatmentProfileName_Type = SonusNameReference
_SonusIsupsgServiceGroupDiscTreatmentProfileName_Object = MibTableColumn
sonusIsupsgServiceGroupDiscTreatmentProfileName = _SonusIsupsgServiceGroupDiscTreatmentProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 20),
    _SonusIsupsgServiceGroupDiscTreatmentProfileName_Type()
)
sonusIsupsgServiceGroupDiscTreatmentProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupDiscTreatmentProfileName.setStatus("current")
_SonusIsupsgServiceGroupTonePackageName_Type = SonusNameReference
_SonusIsupsgServiceGroupTonePackageName_Object = MibTableColumn
sonusIsupsgServiceGroupTonePackageName = _SonusIsupsgServiceGroupTonePackageName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 21),
    _SonusIsupsgServiceGroupTonePackageName_Type()
)
sonusIsupsgServiceGroupTonePackageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupTonePackageName.setStatus("current")


class _SonusIsupsgServiceGroupGrsStartup_Type(Integer32):
    """Custom type sonusIsupsgServiceGroupGrsStartup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusIsupsgServiceGroupGrsStartup_Type.__name__ = "Integer32"
_SonusIsupsgServiceGroupGrsStartup_Object = MibTableColumn
sonusIsupsgServiceGroupGrsStartup = _SonusIsupsgServiceGroupGrsStartup_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 22),
    _SonusIsupsgServiceGroupGrsStartup_Type()
)
sonusIsupsgServiceGroupGrsStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupGrsStartup.setStatus("current")


class _SonusIsupsgServiceGroupOlipCheck_Type(Integer32):
    """Custom type sonusIsupsgServiceGroupOlipCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SonusIsupsgServiceGroupOlipCheck_Type.__name__ = "Integer32"
_SonusIsupsgServiceGroupOlipCheck_Object = MibTableColumn
sonusIsupsgServiceGroupOlipCheck = _SonusIsupsgServiceGroupOlipCheck_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 23),
    _SonusIsupsgServiceGroupOlipCheck_Type()
)
sonusIsupsgServiceGroupOlipCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupOlipCheck.setStatus("current")
_SonusIsupsgServiceGroupRemPc_Type = SonusPointCode
_SonusIsupsgServiceGroupRemPc_Object = MibTableColumn
sonusIsupsgServiceGroupRemPc = _SonusIsupsgServiceGroupRemPc_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 24),
    _SonusIsupsgServiceGroupRemPc_Type()
)
sonusIsupsgServiceGroupRemPc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupRemPc.setStatus("current")


class _SonusIsupsgServiceGroupExchangeType_Type(Integer32):
    """Custom type sonusIsupsgServiceGroupExchangeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("typeA", 2),
          ("typeB", 3))
    )


_SonusIsupsgServiceGroupExchangeType_Type.__name__ = "Integer32"
_SonusIsupsgServiceGroupExchangeType_Object = MibTableColumn
sonusIsupsgServiceGroupExchangeType = _SonusIsupsgServiceGroupExchangeType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 25),
    _SonusIsupsgServiceGroupExchangeType_Type()
)
sonusIsupsgServiceGroupExchangeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupExchangeType.setStatus("current")
_SonusIsupsgServiceGroupInspectionTime_Type = DateAndTime
_SonusIsupsgServiceGroupInspectionTime_Object = MibTableColumn
sonusIsupsgServiceGroupInspectionTime = _SonusIsupsgServiceGroupInspectionTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 26),
    _SonusIsupsgServiceGroupInspectionTime_Type()
)
sonusIsupsgServiceGroupInspectionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupInspectionTime.setStatus("current")


class _SonusIsupsgServiceGroupInspectionFreq_Type(Integer32):
    """Custom type sonusIsupsgServiceGroupInspectionFreq based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("oneday", 5),
          ("onehour", 1),
          ("sixhours", 3),
          ("threehours", 2),
          ("twelvehours", 4),
          ("twodays", 6))
    )


_SonusIsupsgServiceGroupInspectionFreq_Type.__name__ = "Integer32"
_SonusIsupsgServiceGroupInspectionFreq_Object = MibTableColumn
sonusIsupsgServiceGroupInspectionFreq = _SonusIsupsgServiceGroupInspectionFreq_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 27),
    _SonusIsupsgServiceGroupInspectionFreq_Type()
)
sonusIsupsgServiceGroupInspectionFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupInspectionFreq.setStatus("current")


class _SonusIsupsgServiceGroupInspectionState_Type(SonusAdminState):
    """Custom type sonusIsupsgServiceGroupInspectionState based on SonusAdminState"""


_SonusIsupsgServiceGroupInspectionState_Object = MibTableColumn
sonusIsupsgServiceGroupInspectionState = _SonusIsupsgServiceGroupInspectionState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 28),
    _SonusIsupsgServiceGroupInspectionState_Type()
)
sonusIsupsgServiceGroupInspectionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupInspectionState.setStatus("current")
_SonusIsupsgServiceGroupSignalingProfileName_Type = SonusNameReference
_SonusIsupsgServiceGroupSignalingProfileName_Object = MibTableColumn
sonusIsupsgServiceGroupSignalingProfileName = _SonusIsupsgServiceGroupSignalingProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 29),
    _SonusIsupsgServiceGroupSignalingProfileName_Type()
)
sonusIsupsgServiceGroupSignalingProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupSignalingProfileName.setStatus("current")


class _SonusIsupsgServiceGroupAccRespProcess_Type(Integer32):
    """Custom type sonusIsupsgServiceGroupAccRespProcess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusIsupsgServiceGroupAccRespProcess_Type.__name__ = "Integer32"
_SonusIsupsgServiceGroupAccRespProcess_Object = MibTableColumn
sonusIsupsgServiceGroupAccRespProcess = _SonusIsupsgServiceGroupAccRespProcess_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 30),
    _SonusIsupsgServiceGroupAccRespProcess_Type()
)
sonusIsupsgServiceGroupAccRespProcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupAccRespProcess.setStatus("current")


class _SonusIsupsgServiceGroupAccL1ARCancelpercentage_Type(Integer32):
    """Custom type sonusIsupsgServiceGroupAccL1ARCancelpercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SonusIsupsgServiceGroupAccL1ARCancelpercentage_Type.__name__ = "Integer32"
_SonusIsupsgServiceGroupAccL1ARCancelpercentage_Object = MibTableColumn
sonusIsupsgServiceGroupAccL1ARCancelpercentage = _SonusIsupsgServiceGroupAccL1ARCancelpercentage_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 31),
    _SonusIsupsgServiceGroupAccL1ARCancelpercentage_Type()
)
sonusIsupsgServiceGroupAccL1ARCancelpercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupAccL1ARCancelpercentage.setStatus("current")


class _SonusIsupsgServiceGroupAccL1DRCancelpercentage_Type(Integer32):
    """Custom type sonusIsupsgServiceGroupAccL1DRCancelpercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SonusIsupsgServiceGroupAccL1DRCancelpercentage_Type.__name__ = "Integer32"
_SonusIsupsgServiceGroupAccL1DRCancelpercentage_Object = MibTableColumn
sonusIsupsgServiceGroupAccL1DRCancelpercentage = _SonusIsupsgServiceGroupAccL1DRCancelpercentage_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 32),
    _SonusIsupsgServiceGroupAccL1DRCancelpercentage_Type()
)
sonusIsupsgServiceGroupAccL1DRCancelpercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupAccL1DRCancelpercentage.setStatus("current")


class _SonusIsupsgServiceGroupAccL2ARCancelpercentage_Type(Integer32):
    """Custom type sonusIsupsgServiceGroupAccL2ARCancelpercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SonusIsupsgServiceGroupAccL2ARCancelpercentage_Type.__name__ = "Integer32"
_SonusIsupsgServiceGroupAccL2ARCancelpercentage_Object = MibTableColumn
sonusIsupsgServiceGroupAccL2ARCancelpercentage = _SonusIsupsgServiceGroupAccL2ARCancelpercentage_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 33),
    _SonusIsupsgServiceGroupAccL2ARCancelpercentage_Type()
)
sonusIsupsgServiceGroupAccL2ARCancelpercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupAccL2ARCancelpercentage.setStatus("current")


class _SonusIsupsgServiceGroupAccL2DRCancelpercentage_Type(Integer32):
    """Custom type sonusIsupsgServiceGroupAccL2DRCancelpercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SonusIsupsgServiceGroupAccL2DRCancelpercentage_Type.__name__ = "Integer32"
_SonusIsupsgServiceGroupAccL2DRCancelpercentage_Object = MibTableColumn
sonusIsupsgServiceGroupAccL2DRCancelpercentage = _SonusIsupsgServiceGroupAccL2DRCancelpercentage_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 34),
    _SonusIsupsgServiceGroupAccL2DRCancelpercentage_Type()
)
sonusIsupsgServiceGroupAccL2DRCancelpercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupAccL2DRCancelpercentage.setStatus("current")


class _SonusIsupsgServiceGroupAccL3ARCancelpercentage_Type(Integer32):
    """Custom type sonusIsupsgServiceGroupAccL3ARCancelpercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SonusIsupsgServiceGroupAccL3ARCancelpercentage_Type.__name__ = "Integer32"
_SonusIsupsgServiceGroupAccL3ARCancelpercentage_Object = MibTableColumn
sonusIsupsgServiceGroupAccL3ARCancelpercentage = _SonusIsupsgServiceGroupAccL3ARCancelpercentage_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 35),
    _SonusIsupsgServiceGroupAccL3ARCancelpercentage_Type()
)
sonusIsupsgServiceGroupAccL3ARCancelpercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupAccL3ARCancelpercentage.setStatus("current")


class _SonusIsupsgServiceGroupAccL3DRCancelpercentage_Type(Integer32):
    """Custom type sonusIsupsgServiceGroupAccL3DRCancelpercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SonusIsupsgServiceGroupAccL3DRCancelpercentage_Type.__name__ = "Integer32"
_SonusIsupsgServiceGroupAccL3DRCancelpercentage_Object = MibTableColumn
sonusIsupsgServiceGroupAccL3DRCancelpercentage = _SonusIsupsgServiceGroupAccL3DRCancelpercentage_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 36),
    _SonusIsupsgServiceGroupAccL3DRCancelpercentage_Type()
)
sonusIsupsgServiceGroupAccL3DRCancelpercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupAccL3DRCancelpercentage.setStatus("current")


class _SonusIsupsgServiceGroupAccSendACL_Type(Integer32):
    """Custom type sonusIsupsgServiceGroupAccSendACL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_SonusIsupsgServiceGroupAccSendACL_Type.__name__ = "Integer32"
_SonusIsupsgServiceGroupAccSendACL_Object = MibTableColumn
sonusIsupsgServiceGroupAccSendACL = _SonusIsupsgServiceGroupAccSendACL_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 37),
    _SonusIsupsgServiceGroupAccSendACL_Type()
)
sonusIsupsgServiceGroupAccSendACL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupAccSendACL.setStatus("current")


class _SonusIsupsgServiceGroupGatewayOutage_Type(Integer32):
    """Custom type sonusIsupsgServiceGroupGatewayOutage based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("keepCalls", 1),
          ("removeCalls", 2))
    )


_SonusIsupsgServiceGroupGatewayOutage_Type.__name__ = "Integer32"
_SonusIsupsgServiceGroupGatewayOutage_Object = MibTableColumn
sonusIsupsgServiceGroupGatewayOutage = _SonusIsupsgServiceGroupGatewayOutage_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 1, 2, 1, 38),
    _SonusIsupsgServiceGroupGatewayOutage_Type()
)
sonusIsupsgServiceGroupGatewayOutage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupGatewayOutage.setStatus("current")
_SonusIsupsgServiceGroupStatTable_Object = MibTable
sonusIsupsgServiceGroupStatTable = _SonusIsupsgServiceGroupStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupStatTable.setStatus("current")
_SonusIsupsgServiceGroupStatEntry_Object = MibTableRow
sonusIsupsgServiceGroupStatEntry = _SonusIsupsgServiceGroupStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 2, 1)
)
sonusIsupsgServiceGroupStatEntry.setIndexNames(
    (0, "SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupsgServiceGroupStatListIndex"),
)
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupStatEntry.setStatus("current")


class _SonusIsupsgServiceGroupStatListIndex_Type(Integer32):
    """Custom type sonusIsupsgServiceGroupStatListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsupsgServiceGroupStatListIndex_Type.__name__ = "Integer32"
_SonusIsupsgServiceGroupStatListIndex_Object = MibTableColumn
sonusIsupsgServiceGroupStatListIndex = _SonusIsupsgServiceGroupStatListIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 2, 1, 1),
    _SonusIsupsgServiceGroupStatListIndex_Type()
)
sonusIsupsgServiceGroupStatListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupStatListIndex.setStatus("current")
_SonusIsupsgServiceGroupStatName_Type = SonusNameReference
_SonusIsupsgServiceGroupStatName_Object = MibTableColumn
sonusIsupsgServiceGroupStatName = _SonusIsupsgServiceGroupStatName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 2, 1, 2),
    _SonusIsupsgServiceGroupStatName_Type()
)
sonusIsupsgServiceGroupStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupStatName.setStatus("current")


class _SonusIsupsgServiceGroupStatStatus_Type(Integer32):
    """Custom type sonusIsupsgServiceGroupStatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("congested", 3),
          ("unavailable", 2))
    )


_SonusIsupsgServiceGroupStatStatus_Type.__name__ = "Integer32"
_SonusIsupsgServiceGroupStatStatus_Object = MibTableColumn
sonusIsupsgServiceGroupStatStatus = _SonusIsupsgServiceGroupStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 2, 1, 3),
    _SonusIsupsgServiceGroupStatStatus_Type()
)
sonusIsupsgServiceGroupStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupStatStatus.setStatus("current")
_SonusIsupsgServiceGroupStatLastInspectionTime_Type = DateAndTime
_SonusIsupsgServiceGroupStatLastInspectionTime_Object = MibTableColumn
sonusIsupsgServiceGroupStatLastInspectionTime = _SonusIsupsgServiceGroupStatLastInspectionTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 2, 1, 4),
    _SonusIsupsgServiceGroupStatLastInspectionTime_Type()
)
sonusIsupsgServiceGroupStatLastInspectionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupStatLastInspectionTime.setStatus("current")
_SonusIsupsgServiceGroupStatNextInspectionTime_Type = DateAndTime
_SonusIsupsgServiceGroupStatNextInspectionTime_Object = MibTableColumn
sonusIsupsgServiceGroupStatNextInspectionTime = _SonusIsupsgServiceGroupStatNextInspectionTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 2, 1, 5),
    _SonusIsupsgServiceGroupStatNextInspectionTime_Type()
)
sonusIsupsgServiceGroupStatNextInspectionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgServiceGroupStatNextInspectionTime.setStatus("current")
_SonusIsupsgSvcGrpProfile_ObjectIdentity = ObjectIdentity
sonusIsupsgSvcGrpProfile = _SonusIsupsgSvcGrpProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3)
)
_SonusIsupsgSvcGrpProfileNextIndex_Type = Integer32
_SonusIsupsgSvcGrpProfileNextIndex_Object = MibScalar
sonusIsupsgSvcGrpProfileNextIndex = _SonusIsupsgSvcGrpProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 1),
    _SonusIsupsgSvcGrpProfileNextIndex_Type()
)
sonusIsupsgSvcGrpProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileNextIndex.setStatus("current")
_SonusIsupsgSvcGrpProfileTable_Object = MibTable
sonusIsupsgSvcGrpProfileTable = _SonusIsupsgSvcGrpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileTable.setStatus("current")
_SonusIsupsgSvcGrpProfileEntry_Object = MibTableRow
sonusIsupsgSvcGrpProfileEntry = _SonusIsupsgSvcGrpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1)
)
sonusIsupsgSvcGrpProfileEntry.setIndexNames(
    (0, "SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupsgSvcGrpProfileListIndex"),
)
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileEntry.setStatus("current")


class _SonusIsupsgSvcGrpProfileListIndex_Type(Integer32):
    """Custom type sonusIsupsgSvcGrpProfileListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SonusIsupsgSvcGrpProfileListIndex_Type.__name__ = "Integer32"
_SonusIsupsgSvcGrpProfileListIndex_Object = MibTableColumn
sonusIsupsgSvcGrpProfileListIndex = _SonusIsupsgSvcGrpProfileListIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 1),
    _SonusIsupsgSvcGrpProfileListIndex_Type()
)
sonusIsupsgSvcGrpProfileListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileListIndex.setStatus("current")
_SonusIsupsgSvcGrpProfileName_Type = SonusName
_SonusIsupsgSvcGrpProfileName_Object = MibTableColumn
sonusIsupsgSvcGrpProfileName = _SonusIsupsgSvcGrpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 2),
    _SonusIsupsgSvcGrpProfileName_Type()
)
sonusIsupsgSvcGrpProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileName.setStatus("current")
_SonusIsupsgSvcGrpProfileTG_Type = SonusNameReference
_SonusIsupsgSvcGrpProfileTG_Object = MibTableColumn
sonusIsupsgSvcGrpProfileTG = _SonusIsupsgSvcGrpProfileTG_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 3),
    _SonusIsupsgSvcGrpProfileTG_Type()
)
sonusIsupsgSvcGrpProfileTG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileTG.setStatus("current")


class _SonusIsupsgSvcGrpProfileSwitchType_Type(Integer32):
    """Custom type sonusIsupsgSvcGrpProfileSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dms100", 4),
          ("dms200", 3),
          ("dms250", 2),
          ("dms500", 1),
          ("lucent4ESS", 6),
          ("lucent5ESS", 5))
    )


_SonusIsupsgSvcGrpProfileSwitchType_Type.__name__ = "Integer32"
_SonusIsupsgSvcGrpProfileSwitchType_Object = MibTableColumn
sonusIsupsgSvcGrpProfileSwitchType = _SonusIsupsgSvcGrpProfileSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 4),
    _SonusIsupsgSvcGrpProfileSwitchType_Type()
)
sonusIsupsgSvcGrpProfileSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileSwitchType.setStatus("current")


class _SonusIsupsgSvcGrpProfileRevision_Type(Integer32):
    """Custom type sonusIsupsgSvcGrpProfileRevision based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ansi1992", 1),
          ("ansi1995", 2),
          ("belgacom", 9),
          ("etsi2", 4),
          ("itu1988", 7),
          ("itu1993", 3),
          ("itu1997", 6),
          ("ituq767", 8),
          ("nttfcc", 5))
    )


_SonusIsupsgSvcGrpProfileRevision_Type.__name__ = "Integer32"
_SonusIsupsgSvcGrpProfileRevision_Object = MibTableColumn
sonusIsupsgSvcGrpProfileRevision = _SonusIsupsgSvcGrpProfileRevision_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 5),
    _SonusIsupsgSvcGrpProfileRevision_Type()
)
sonusIsupsgSvcGrpProfileRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileRevision.setStatus("current")


class _SonusIsupsgSvcGrpProfileHuntAlgorithm_Type(Integer32):
    """Custom type sonusIsupsgSvcGrpProfileHuntAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("bottom2top", 1),
          ("circuithi2lo", 3),
          ("circuitlo2hi", 4),
          ("circularbottom2top", 6),
          ("circulartop2bottom", 7),
          ("mostnleastidle", 5),
          ("top2bottom", 2))
    )


_SonusIsupsgSvcGrpProfileHuntAlgorithm_Type.__name__ = "Integer32"
_SonusIsupsgSvcGrpProfileHuntAlgorithm_Object = MibTableColumn
sonusIsupsgSvcGrpProfileHuntAlgorithm = _SonusIsupsgSvcGrpProfileHuntAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 6),
    _SonusIsupsgSvcGrpProfileHuntAlgorithm_Type()
)
sonusIsupsgSvcGrpProfileHuntAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileHuntAlgorithm.setStatus("current")


class _SonusIsupsgSvcGrpProfileCost_Type(Integer32):
    """Custom type sonusIsupsgSvcGrpProfileCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SonusIsupsgSvcGrpProfileCost_Type.__name__ = "Integer32"
_SonusIsupsgSvcGrpProfileCost_Object = MibTableColumn
sonusIsupsgSvcGrpProfileCost = _SonusIsupsgSvcGrpProfileCost_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 7),
    _SonusIsupsgSvcGrpProfileCost_Type()
)
sonusIsupsgSvcGrpProfileCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileCost.setStatus("current")


class _SonusIsupsgSvcGrpProfileCicControl_Type(Integer32):
    """Custom type sonusIsupsgSvcGrpProfileCicControl based on Integer32"""
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
        *(("allCics", 4),
          ("evenCics", 3),
          ("noCics", 1),
          ("oddCics", 2))
    )


_SonusIsupsgSvcGrpProfileCicControl_Type.__name__ = "Integer32"
_SonusIsupsgSvcGrpProfileCicControl_Object = MibTableColumn
sonusIsupsgSvcGrpProfileCicControl = _SonusIsupsgSvcGrpProfileCicControl_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 8),
    _SonusIsupsgSvcGrpProfileCicControl_Type()
)
sonusIsupsgSvcGrpProfileCicControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileCicControl.setStatus("current")


class _SonusIsupsgSvcGrpProfileContTestFreq_Type(Integer32):
    """Custom type sonusIsupsgSvcGrpProfileContTestFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SonusIsupsgSvcGrpProfileContTestFreq_Type.__name__ = "Integer32"
_SonusIsupsgSvcGrpProfileContTestFreq_Object = MibTableColumn
sonusIsupsgSvcGrpProfileContTestFreq = _SonusIsupsgSvcGrpProfileContTestFreq_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 9),
    _SonusIsupsgSvcGrpProfileContTestFreq_Type()
)
sonusIsupsgSvcGrpProfileContTestFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileContTestFreq.setStatus("current")
_SonusIsupsgSvcGrpProfileAdminState_Type = SonusAdminState
_SonusIsupsgSvcGrpProfileAdminState_Object = MibTableColumn
sonusIsupsgSvcGrpProfileAdminState = _SonusIsupsgSvcGrpProfileAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 10),
    _SonusIsupsgSvcGrpProfileAdminState_Type()
)
sonusIsupsgSvcGrpProfileAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileAdminState.setStatus("current")
_SonusIsupsgSvcGrpProfileRowStatus_Type = RowStatus
_SonusIsupsgSvcGrpProfileRowStatus_Object = MibTableColumn
sonusIsupsgSvcGrpProfileRowStatus = _SonusIsupsgSvcGrpProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 11),
    _SonusIsupsgSvcGrpProfileRowStatus_Type()
)
sonusIsupsgSvcGrpProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileRowStatus.setStatus("current")
_SonusIsupsgSvcGrpProfileHopCounterState_Type = SonusAdminState
_SonusIsupsgSvcGrpProfileHopCounterState_Object = MibTableColumn
sonusIsupsgSvcGrpProfileHopCounterState = _SonusIsupsgSvcGrpProfileHopCounterState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 12),
    _SonusIsupsgSvcGrpProfileHopCounterState_Type()
)
sonusIsupsgSvcGrpProfileHopCounterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileHopCounterState.setStatus("current")


class _SonusIsupsgSvcGrpProfileHopCounterValue_Type(Integer32):
    """Custom type sonusIsupsgSvcGrpProfileHopCounterValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 20),
    )


_SonusIsupsgSvcGrpProfileHopCounterValue_Type.__name__ = "Integer32"
_SonusIsupsgSvcGrpProfileHopCounterValue_Object = MibTableColumn
sonusIsupsgSvcGrpProfileHopCounterValue = _SonusIsupsgSvcGrpProfileHopCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 13),
    _SonusIsupsgSvcGrpProfileHopCounterValue_Type()
)
sonusIsupsgSvcGrpProfileHopCounterValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileHopCounterValue.setStatus("current")
_SonusIsupsgSvcGrpProfileDiscTreatmentProfileName_Type = SonusNameReference
_SonusIsupsgSvcGrpProfileDiscTreatmentProfileName_Object = MibTableColumn
sonusIsupsgSvcGrpProfileDiscTreatmentProfileName = _SonusIsupsgSvcGrpProfileDiscTreatmentProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 14),
    _SonusIsupsgSvcGrpProfileDiscTreatmentProfileName_Type()
)
sonusIsupsgSvcGrpProfileDiscTreatmentProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileDiscTreatmentProfileName.setStatus("current")
_SonusIsupsgSvcGrpProfileTonePackageName_Type = SonusNameReference
_SonusIsupsgSvcGrpProfileTonePackageName_Object = MibTableColumn
sonusIsupsgSvcGrpProfileTonePackageName = _SonusIsupsgSvcGrpProfileTonePackageName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 15),
    _SonusIsupsgSvcGrpProfileTonePackageName_Type()
)
sonusIsupsgSvcGrpProfileTonePackageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileTonePackageName.setStatus("current")


class _SonusIsupsgSvcGrpProfileGrsStartup_Type(Integer32):
    """Custom type sonusIsupsgSvcGrpProfileGrsStartup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusIsupsgSvcGrpProfileGrsStartup_Type.__name__ = "Integer32"
_SonusIsupsgSvcGrpProfileGrsStartup_Object = MibTableColumn
sonusIsupsgSvcGrpProfileGrsStartup = _SonusIsupsgSvcGrpProfileGrsStartup_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 16),
    _SonusIsupsgSvcGrpProfileGrsStartup_Type()
)
sonusIsupsgSvcGrpProfileGrsStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileGrsStartup.setStatus("current")


class _SonusIsupsgSvcGrpProfileOlipCheck_Type(Integer32):
    """Custom type sonusIsupsgSvcGrpProfileOlipCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SonusIsupsgSvcGrpProfileOlipCheck_Type.__name__ = "Integer32"
_SonusIsupsgSvcGrpProfileOlipCheck_Object = MibTableColumn
sonusIsupsgSvcGrpProfileOlipCheck = _SonusIsupsgSvcGrpProfileOlipCheck_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 17),
    _SonusIsupsgSvcGrpProfileOlipCheck_Type()
)
sonusIsupsgSvcGrpProfileOlipCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileOlipCheck.setStatus("current")


class _SonusIsupsgSvcGrpProfileExchangeType_Type(Integer32):
    """Custom type sonusIsupsgSvcGrpProfileExchangeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("typeA", 2),
          ("typeB", 3))
    )


_SonusIsupsgSvcGrpProfileExchangeType_Type.__name__ = "Integer32"
_SonusIsupsgSvcGrpProfileExchangeType_Object = MibTableColumn
sonusIsupsgSvcGrpProfileExchangeType = _SonusIsupsgSvcGrpProfileExchangeType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 18),
    _SonusIsupsgSvcGrpProfileExchangeType_Type()
)
sonusIsupsgSvcGrpProfileExchangeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileExchangeType.setStatus("current")
_SonusIsupsgSvcGrpProfileInspectionTime_Type = DateAndTime
_SonusIsupsgSvcGrpProfileInspectionTime_Object = MibTableColumn
sonusIsupsgSvcGrpProfileInspectionTime = _SonusIsupsgSvcGrpProfileInspectionTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 19),
    _SonusIsupsgSvcGrpProfileInspectionTime_Type()
)
sonusIsupsgSvcGrpProfileInspectionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileInspectionTime.setStatus("current")


class _SonusIsupsgSvcGrpProfileInspectionFreq_Type(Integer32):
    """Custom type sonusIsupsgSvcGrpProfileInspectionFreq based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("oneday", 5),
          ("onehour", 1),
          ("sixhours", 3),
          ("threehours", 2),
          ("twelvehours", 4),
          ("twodays", 6))
    )


_SonusIsupsgSvcGrpProfileInspectionFreq_Type.__name__ = "Integer32"
_SonusIsupsgSvcGrpProfileInspectionFreq_Object = MibTableColumn
sonusIsupsgSvcGrpProfileInspectionFreq = _SonusIsupsgSvcGrpProfileInspectionFreq_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 20),
    _SonusIsupsgSvcGrpProfileInspectionFreq_Type()
)
sonusIsupsgSvcGrpProfileInspectionFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileInspectionFreq.setStatus("current")


class _SonusIsupsgSvcGrpProfileInspectionState_Type(SonusAdminState):
    """Custom type sonusIsupsgSvcGrpProfileInspectionState based on SonusAdminState"""


_SonusIsupsgSvcGrpProfileInspectionState_Object = MibTableColumn
sonusIsupsgSvcGrpProfileInspectionState = _SonusIsupsgSvcGrpProfileInspectionState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 21),
    _SonusIsupsgSvcGrpProfileInspectionState_Type()
)
sonusIsupsgSvcGrpProfileInspectionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileInspectionState.setStatus("current")
_SonusIsupsgSvcGrpProfileSignalingProfileName_Type = SonusNameReference
_SonusIsupsgSvcGrpProfileSignalingProfileName_Object = MibTableColumn
sonusIsupsgSvcGrpProfileSignalingProfileName = _SonusIsupsgSvcGrpProfileSignalingProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 22),
    _SonusIsupsgSvcGrpProfileSignalingProfileName_Type()
)
sonusIsupsgSvcGrpProfileSignalingProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileSignalingProfileName.setStatus("current")


class _SonusIsupsgSvcGrpProfileAccRespProcess_Type(Integer32):
    """Custom type sonusIsupsgSvcGrpProfileAccRespProcess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusIsupsgSvcGrpProfileAccRespProcess_Type.__name__ = "Integer32"
_SonusIsupsgSvcGrpProfileAccRespProcess_Object = MibTableColumn
sonusIsupsgSvcGrpProfileAccRespProcess = _SonusIsupsgSvcGrpProfileAccRespProcess_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 23),
    _SonusIsupsgSvcGrpProfileAccRespProcess_Type()
)
sonusIsupsgSvcGrpProfileAccRespProcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileAccRespProcess.setStatus("current")


class _SonusIsupsgSvcGrpProfileAccL1ARCancelpercentage_Type(Integer32):
    """Custom type sonusIsupsgSvcGrpProfileAccL1ARCancelpercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SonusIsupsgSvcGrpProfileAccL1ARCancelpercentage_Type.__name__ = "Integer32"
_SonusIsupsgSvcGrpProfileAccL1ARCancelpercentage_Object = MibTableColumn
sonusIsupsgSvcGrpProfileAccL1ARCancelpercentage = _SonusIsupsgSvcGrpProfileAccL1ARCancelpercentage_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 24),
    _SonusIsupsgSvcGrpProfileAccL1ARCancelpercentage_Type()
)
sonusIsupsgSvcGrpProfileAccL1ARCancelpercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileAccL1ARCancelpercentage.setStatus("current")


class _SonusIsupsgSvcGrpProfileAccL1DRCancelpercentage_Type(Integer32):
    """Custom type sonusIsupsgSvcGrpProfileAccL1DRCancelpercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SonusIsupsgSvcGrpProfileAccL1DRCancelpercentage_Type.__name__ = "Integer32"
_SonusIsupsgSvcGrpProfileAccL1DRCancelpercentage_Object = MibTableColumn
sonusIsupsgSvcGrpProfileAccL1DRCancelpercentage = _SonusIsupsgSvcGrpProfileAccL1DRCancelpercentage_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 25),
    _SonusIsupsgSvcGrpProfileAccL1DRCancelpercentage_Type()
)
sonusIsupsgSvcGrpProfileAccL1DRCancelpercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileAccL1DRCancelpercentage.setStatus("current")


class _SonusIsupsgSvcGrpProfileAccL2ARCancelpercentage_Type(Integer32):
    """Custom type sonusIsupsgSvcGrpProfileAccL2ARCancelpercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SonusIsupsgSvcGrpProfileAccL2ARCancelpercentage_Type.__name__ = "Integer32"
_SonusIsupsgSvcGrpProfileAccL2ARCancelpercentage_Object = MibTableColumn
sonusIsupsgSvcGrpProfileAccL2ARCancelpercentage = _SonusIsupsgSvcGrpProfileAccL2ARCancelpercentage_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 26),
    _SonusIsupsgSvcGrpProfileAccL2ARCancelpercentage_Type()
)
sonusIsupsgSvcGrpProfileAccL2ARCancelpercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileAccL2ARCancelpercentage.setStatus("current")


class _SonusIsupsgSvcGrpProfileAccL2DRCancelpercentage_Type(Integer32):
    """Custom type sonusIsupsgSvcGrpProfileAccL2DRCancelpercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SonusIsupsgSvcGrpProfileAccL2DRCancelpercentage_Type.__name__ = "Integer32"
_SonusIsupsgSvcGrpProfileAccL2DRCancelpercentage_Object = MibTableColumn
sonusIsupsgSvcGrpProfileAccL2DRCancelpercentage = _SonusIsupsgSvcGrpProfileAccL2DRCancelpercentage_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 27),
    _SonusIsupsgSvcGrpProfileAccL2DRCancelpercentage_Type()
)
sonusIsupsgSvcGrpProfileAccL2DRCancelpercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileAccL2DRCancelpercentage.setStatus("current")


class _SonusIsupsgSvcGrpProfileAccL3ARCancelpercentage_Type(Integer32):
    """Custom type sonusIsupsgSvcGrpProfileAccL3ARCancelpercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SonusIsupsgSvcGrpProfileAccL3ARCancelpercentage_Type.__name__ = "Integer32"
_SonusIsupsgSvcGrpProfileAccL3ARCancelpercentage_Object = MibTableColumn
sonusIsupsgSvcGrpProfileAccL3ARCancelpercentage = _SonusIsupsgSvcGrpProfileAccL3ARCancelpercentage_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 28),
    _SonusIsupsgSvcGrpProfileAccL3ARCancelpercentage_Type()
)
sonusIsupsgSvcGrpProfileAccL3ARCancelpercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileAccL3ARCancelpercentage.setStatus("current")


class _SonusIsupsgSvcGrpProfileAccL3DRCancelpercentage_Type(Integer32):
    """Custom type sonusIsupsgSvcGrpProfileAccL3DRCancelpercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SonusIsupsgSvcGrpProfileAccL3DRCancelpercentage_Type.__name__ = "Integer32"
_SonusIsupsgSvcGrpProfileAccL3DRCancelpercentage_Object = MibTableColumn
sonusIsupsgSvcGrpProfileAccL3DRCancelpercentage = _SonusIsupsgSvcGrpProfileAccL3DRCancelpercentage_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 29),
    _SonusIsupsgSvcGrpProfileAccL3DRCancelpercentage_Type()
)
sonusIsupsgSvcGrpProfileAccL3DRCancelpercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileAccL3DRCancelpercentage.setStatus("current")


class _SonusIsupsgSvcGrpProfileAccSendACL_Type(Integer32):
    """Custom type sonusIsupsgSvcGrpProfileAccSendACL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_SonusIsupsgSvcGrpProfileAccSendACL_Type.__name__ = "Integer32"
_SonusIsupsgSvcGrpProfileAccSendACL_Object = MibTableColumn
sonusIsupsgSvcGrpProfileAccSendACL = _SonusIsupsgSvcGrpProfileAccSendACL_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 3, 2, 1, 30),
    _SonusIsupsgSvcGrpProfileAccSendACL_Type()
)
sonusIsupsgSvcGrpProfileAccSendACL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSvcGrpProfileAccSendACL.setStatus("current")
_SonusIsupsgCircuitTable_Object = MibTable
sonusIsupsgCircuitTable = _SonusIsupsgCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 4)
)
if mibBuilder.loadTexts:
    sonusIsupsgCircuitTable.setStatus("current")
_SonusIsupsgCircuitEntry_Object = MibTableRow
sonusIsupsgCircuitEntry = _SonusIsupsgCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 4, 1)
)
sonusIsupsgCircuitEntry.setIndexNames(
    (0, "SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupsgCircuitServiceListIndex"),
    (0, "SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupsgCircuitIdentityCode"),
)
if mibBuilder.loadTexts:
    sonusIsupsgCircuitEntry.setStatus("current")
_SonusIsupsgCircuitServiceListIndex_Type = Integer32
_SonusIsupsgCircuitServiceListIndex_Object = MibTableColumn
sonusIsupsgCircuitServiceListIndex = _SonusIsupsgCircuitServiceListIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 4, 1, 1),
    _SonusIsupsgCircuitServiceListIndex_Type()
)
sonusIsupsgCircuitServiceListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgCircuitServiceListIndex.setStatus("current")


class _SonusIsupsgCircuitIdentityCode_Type(Integer32):
    """Custom type sonusIsupsgCircuitIdentityCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_SonusIsupsgCircuitIdentityCode_Type.__name__ = "Integer32"
_SonusIsupsgCircuitIdentityCode_Object = MibTableColumn
sonusIsupsgCircuitIdentityCode = _SonusIsupsgCircuitIdentityCode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 4, 1, 2),
    _SonusIsupsgCircuitIdentityCode_Type()
)
sonusIsupsgCircuitIdentityCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgCircuitIdentityCode.setStatus("current")
_SonusIsupsgCircuitServiceName_Type = SonusNameReference
_SonusIsupsgCircuitServiceName_Object = MibTableColumn
sonusIsupsgCircuitServiceName = _SonusIsupsgCircuitServiceName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 4, 1, 3),
    _SonusIsupsgCircuitServiceName_Type()
)
sonusIsupsgCircuitServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgCircuitServiceName.setStatus("current")
_SonusIsupsgCircuitPortName_Type = SonusNameReference
_SonusIsupsgCircuitPortName_Object = MibTableColumn
sonusIsupsgCircuitPortName = _SonusIsupsgCircuitPortName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 4, 1, 4),
    _SonusIsupsgCircuitPortName_Type()
)
sonusIsupsgCircuitPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgCircuitPortName.setStatus("current")


class _SonusIsupsgCircuitChannel_Type(Integer32):
    """Custom type sonusIsupsgCircuitChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SonusIsupsgCircuitChannel_Type.__name__ = "Integer32"
_SonusIsupsgCircuitChannel_Object = MibTableColumn
sonusIsupsgCircuitChannel = _SonusIsupsgCircuitChannel_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 4, 1, 5),
    _SonusIsupsgCircuitChannel_Type()
)
sonusIsupsgCircuitChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgCircuitChannel.setStatus("current")


class _SonusIsupsgCircuitDirection_Type(Integer32):
    """Custom type sonusIsupsgCircuitDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneWayIn", 2),
          ("oneWayOut", 3),
          ("twoWay", 1))
    )


_SonusIsupsgCircuitDirection_Type.__name__ = "Integer32"
_SonusIsupsgCircuitDirection_Object = MibTableColumn
sonusIsupsgCircuitDirection = _SonusIsupsgCircuitDirection_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 4, 1, 6),
    _SonusIsupsgCircuitDirection_Type()
)
sonusIsupsgCircuitDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgCircuitDirection.setStatus("current")


class _SonusIsupsgCircuitMode_Type(Integer32):
    """Custom type sonusIsupsgCircuitMode based on Integer32"""
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
        *(("block", 1),
          ("cot", 4),
          ("reset", 3),
          ("unblock", 2))
    )


_SonusIsupsgCircuitMode_Type.__name__ = "Integer32"
_SonusIsupsgCircuitMode_Object = MibTableColumn
sonusIsupsgCircuitMode = _SonusIsupsgCircuitMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 4, 1, 7),
    _SonusIsupsgCircuitMode_Type()
)
sonusIsupsgCircuitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgCircuitMode.setStatus("current")


class _SonusIsupsgCircuitAction_Type(Integer32):
    """Custom type sonusIsupsgCircuitAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dryUp", 1),
          ("force", 2))
    )


_SonusIsupsgCircuitAction_Type.__name__ = "Integer32"
_SonusIsupsgCircuitAction_Object = MibTableColumn
sonusIsupsgCircuitAction = _SonusIsupsgCircuitAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 4, 1, 8),
    _SonusIsupsgCircuitAction_Type()
)
sonusIsupsgCircuitAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgCircuitAction.setStatus("current")


class _SonusIsupsgCircuitTimeout_Type(Integer32):
    """Custom type sonusIsupsgCircuitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_SonusIsupsgCircuitTimeout_Type.__name__ = "Integer32"
_SonusIsupsgCircuitTimeout_Object = MibTableColumn
sonusIsupsgCircuitTimeout = _SonusIsupsgCircuitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 4, 1, 9),
    _SonusIsupsgCircuitTimeout_Type()
)
sonusIsupsgCircuitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgCircuitTimeout.setStatus("current")
_SonusIsupsgCircuitAdminState_Type = SonusAdminState
_SonusIsupsgCircuitAdminState_Object = MibTableColumn
sonusIsupsgCircuitAdminState = _SonusIsupsgCircuitAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 4, 1, 10),
    _SonusIsupsgCircuitAdminState_Type()
)
sonusIsupsgCircuitAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgCircuitAdminState.setStatus("current")
_SonusIsupsgCircuitProfileName_Type = SonusNameReference
_SonusIsupsgCircuitProfileName_Object = MibTableColumn
sonusIsupsgCircuitProfileName = _SonusIsupsgCircuitProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 4, 1, 11),
    _SonusIsupsgCircuitProfileName_Type()
)
sonusIsupsgCircuitProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgCircuitProfileName.setStatus("current")
_SonusIsupsgCircuitRowStatus_Type = RowStatus
_SonusIsupsgCircuitRowStatus_Object = MibTableColumn
sonusIsupsgCircuitRowStatus = _SonusIsupsgCircuitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 4, 1, 12),
    _SonusIsupsgCircuitRowStatus_Type()
)
sonusIsupsgCircuitRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgCircuitRowStatus.setStatus("current")
_SonusIsupsgCircuitStatTable_Object = MibTable
sonusIsupsgCircuitStatTable = _SonusIsupsgCircuitStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 5)
)
if mibBuilder.loadTexts:
    sonusIsupsgCircuitStatTable.setStatus("current")
_SonusIsupsgCircuitStatEntry_Object = MibTableRow
sonusIsupsgCircuitStatEntry = _SonusIsupsgCircuitStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 5, 1)
)
sonusIsupsgCircuitStatEntry.setIndexNames(
    (0, "SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupsgCircuitStatServiceListIndex"),
    (0, "SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupsgCircuitStatIdentityCode"),
)
if mibBuilder.loadTexts:
    sonusIsupsgCircuitStatEntry.setStatus("current")
_SonusIsupsgCircuitStatServiceListIndex_Type = Integer32
_SonusIsupsgCircuitStatServiceListIndex_Object = MibTableColumn
sonusIsupsgCircuitStatServiceListIndex = _SonusIsupsgCircuitStatServiceListIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 5, 1, 1),
    _SonusIsupsgCircuitStatServiceListIndex_Type()
)
sonusIsupsgCircuitStatServiceListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgCircuitStatServiceListIndex.setStatus("current")


class _SonusIsupsgCircuitStatIdentityCode_Type(Integer32):
    """Custom type sonusIsupsgCircuitStatIdentityCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_SonusIsupsgCircuitStatIdentityCode_Type.__name__ = "Integer32"
_SonusIsupsgCircuitStatIdentityCode_Object = MibTableColumn
sonusIsupsgCircuitStatIdentityCode = _SonusIsupsgCircuitStatIdentityCode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 5, 1, 2),
    _SonusIsupsgCircuitStatIdentityCode_Type()
)
sonusIsupsgCircuitStatIdentityCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgCircuitStatIdentityCode.setStatus("current")


class _SonusIsupsgCircuitStatUsage_Type(Integer32):
    """Custom type sonusIsupsgCircuitStatUsage based on Integer32"""
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
        *(("idle", 2),
          ("inBusy", 3),
          ("inContinuity", 7),
          ("outBusy", 4),
          ("outContinuity", 8),
          ("transientRelease", 6),
          ("transientSetup", 5),
          ("unequipped", 1))
    )


_SonusIsupsgCircuitStatUsage_Type.__name__ = "Integer32"
_SonusIsupsgCircuitStatUsage_Object = MibTableColumn
sonusIsupsgCircuitStatUsage = _SonusIsupsgCircuitStatUsage_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 5, 1, 3),
    _SonusIsupsgCircuitStatUsage_Type()
)
sonusIsupsgCircuitStatUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgCircuitStatUsage.setStatus("current")


class _SonusIsupsgCircuitStatLocalMaint_Type(Integer32):
    """Custom type sonusIsupsgCircuitStatLocalMaint based on Integer32"""
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
        *(("blocked", 2),
          ("notAvailable", 5),
          ("transientBlock", 4),
          ("transientUnblock", 3),
          ("unblocked", 1))
    )


_SonusIsupsgCircuitStatLocalMaint_Type.__name__ = "Integer32"
_SonusIsupsgCircuitStatLocalMaint_Object = MibTableColumn
sonusIsupsgCircuitStatLocalMaint = _SonusIsupsgCircuitStatLocalMaint_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 5, 1, 4),
    _SonusIsupsgCircuitStatLocalMaint_Type()
)
sonusIsupsgCircuitStatLocalMaint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgCircuitStatLocalMaint.setStatus("current")


class _SonusIsupsgCircuitStatLocalHw_Type(Integer32):
    """Custom type sonusIsupsgCircuitStatLocalHw based on Integer32"""
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
        *(("blocked", 2),
          ("notAvailable", 5),
          ("transientBlock", 4),
          ("transientUnblock", 3),
          ("unblocked", 1))
    )


_SonusIsupsgCircuitStatLocalHw_Type.__name__ = "Integer32"
_SonusIsupsgCircuitStatLocalHw_Object = MibTableColumn
sonusIsupsgCircuitStatLocalHw = _SonusIsupsgCircuitStatLocalHw_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 5, 1, 5),
    _SonusIsupsgCircuitStatLocalHw_Type()
)
sonusIsupsgCircuitStatLocalHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgCircuitStatLocalHw.setStatus("current")


class _SonusIsupsgCircuitStatRemoteMaint_Type(Integer32):
    """Custom type sonusIsupsgCircuitStatRemoteMaint based on Integer32"""
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
        *(("blocked", 2),
          ("notAvailable", 5),
          ("transientBlock", 4),
          ("transientUnblock", 3),
          ("unblocked", 1))
    )


_SonusIsupsgCircuitStatRemoteMaint_Type.__name__ = "Integer32"
_SonusIsupsgCircuitStatRemoteMaint_Object = MibTableColumn
sonusIsupsgCircuitStatRemoteMaint = _SonusIsupsgCircuitStatRemoteMaint_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 5, 1, 6),
    _SonusIsupsgCircuitStatRemoteMaint_Type()
)
sonusIsupsgCircuitStatRemoteMaint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgCircuitStatRemoteMaint.setStatus("current")


class _SonusIsupsgCircuitStatRemoteHw_Type(Integer32):
    """Custom type sonusIsupsgCircuitStatRemoteHw based on Integer32"""
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
        *(("blocked", 2),
          ("notAvailable", 5),
          ("transientBlock", 4),
          ("transientUnblock", 3),
          ("unblocked", 1))
    )


_SonusIsupsgCircuitStatRemoteHw_Type.__name__ = "Integer32"
_SonusIsupsgCircuitStatRemoteHw_Object = MibTableColumn
sonusIsupsgCircuitStatRemoteHw = _SonusIsupsgCircuitStatRemoteHw_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 5, 1, 7),
    _SonusIsupsgCircuitStatRemoteHw_Type()
)
sonusIsupsgCircuitStatRemoteHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgCircuitStatRemoteHw.setStatus("current")


class _SonusIsupsgCircuitStatManualCot_Type(Integer32):
    """Custom type sonusIsupsgCircuitStatManualCot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("abort", 6),
          ("fail", 5),
          ("inProgress", 3),
          ("lpaFail", 7),
          ("notAvailable", 1),
          ("pass", 4),
          ("pending", 2))
    )


_SonusIsupsgCircuitStatManualCot_Type.__name__ = "Integer32"
_SonusIsupsgCircuitStatManualCot_Object = MibTableColumn
sonusIsupsgCircuitStatManualCot = _SonusIsupsgCircuitStatManualCot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 5, 1, 8),
    _SonusIsupsgCircuitStatManualCot_Type()
)
sonusIsupsgCircuitStatManualCot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgCircuitStatManualCot.setStatus("current")
_SonusIsupsgFarEndCircuitAdminTable_Object = MibTable
sonusIsupsgFarEndCircuitAdminTable = _SonusIsupsgFarEndCircuitAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 6)
)
if mibBuilder.loadTexts:
    sonusIsupsgFarEndCircuitAdminTable.setStatus("current")
_SonusIsupsgFarEndCircuitAdminEntry_Object = MibTableRow
sonusIsupsgFarEndCircuitAdminEntry = _SonusIsupsgFarEndCircuitAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 6, 1)
)
sonusIsupsgFarEndCircuitAdminEntry.setIndexNames(
    (0, "SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupsgFarEndCircuitServiceListIndex"),
    (0, "SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupsgFarEndCircuitIdentityCode"),
)
if mibBuilder.loadTexts:
    sonusIsupsgFarEndCircuitAdminEntry.setStatus("current")
_SonusIsupsgFarEndCircuitServiceListIndex_Type = Integer32
_SonusIsupsgFarEndCircuitServiceListIndex_Object = MibTableColumn
sonusIsupsgFarEndCircuitServiceListIndex = _SonusIsupsgFarEndCircuitServiceListIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 6, 1, 1),
    _SonusIsupsgFarEndCircuitServiceListIndex_Type()
)
sonusIsupsgFarEndCircuitServiceListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgFarEndCircuitServiceListIndex.setStatus("current")


class _SonusIsupsgFarEndCircuitIdentityCode_Type(Integer32):
    """Custom type sonusIsupsgFarEndCircuitIdentityCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_SonusIsupsgFarEndCircuitIdentityCode_Type.__name__ = "Integer32"
_SonusIsupsgFarEndCircuitIdentityCode_Object = MibTableColumn
sonusIsupsgFarEndCircuitIdentityCode = _SonusIsupsgFarEndCircuitIdentityCode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 6, 1, 2),
    _SonusIsupsgFarEndCircuitIdentityCode_Type()
)
sonusIsupsgFarEndCircuitIdentityCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgFarEndCircuitIdentityCode.setStatus("current")


class _SonusIsupsgFarEndCircuitValidationTestResult_Type(Integer32):
    """Custom type sonusIsupsgFarEndCircuitValidationTestResult based on Integer32"""
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
        *(("failure", 2),
          ("noResponse", 0),
          ("notAvailable", 3),
          ("successful", 1))
    )


_SonusIsupsgFarEndCircuitValidationTestResult_Type.__name__ = "Integer32"
_SonusIsupsgFarEndCircuitValidationTestResult_Object = MibTableColumn
sonusIsupsgFarEndCircuitValidationTestResult = _SonusIsupsgFarEndCircuitValidationTestResult_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 6, 1, 3),
    _SonusIsupsgFarEndCircuitValidationTestResult_Type()
)
sonusIsupsgFarEndCircuitValidationTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgFarEndCircuitValidationTestResult.setStatus("current")


class _SonusIsupsgFarEndCircuitGroupCarrier_Type(Integer32):
    """Custom type sonusIsupsgFarEndCircuitGroupCarrier based on Integer32"""
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
        *(("analog", 2),
          ("digital", 3),
          ("digitalAndAnalog", 4),
          ("noResponse", 0),
          ("unknown", 1))
    )


_SonusIsupsgFarEndCircuitGroupCarrier_Type.__name__ = "Integer32"
_SonusIsupsgFarEndCircuitGroupCarrier_Object = MibTableColumn
sonusIsupsgFarEndCircuitGroupCarrier = _SonusIsupsgFarEndCircuitGroupCarrier_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 6, 1, 4),
    _SonusIsupsgFarEndCircuitGroupCarrier_Type()
)
sonusIsupsgFarEndCircuitGroupCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgFarEndCircuitGroupCarrier.setStatus("current")


class _SonusIsupsgFarEndCircuitCicControl_Type(Integer32):
    """Custom type sonusIsupsgFarEndCircuitCicControl based on Integer32"""
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
        *(("allCics", 4),
          ("evenCics", 3),
          ("noCics", 1),
          ("noResponse", 0),
          ("oddCics", 2))
    )


_SonusIsupsgFarEndCircuitCicControl_Type.__name__ = "Integer32"
_SonusIsupsgFarEndCircuitCicControl_Object = MibTableColumn
sonusIsupsgFarEndCircuitCicControl = _SonusIsupsgFarEndCircuitCicControl_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 6, 1, 5),
    _SonusIsupsgFarEndCircuitCicControl_Type()
)
sonusIsupsgFarEndCircuitCicControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgFarEndCircuitCicControl.setStatus("current")


class _SonusIsupsgFarEndCircuitAlarmCarrier_Type(Integer32):
    """Custom type sonusIsupsgFarEndCircuitAlarmCarrier based on Integer32"""
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
        *(("hardwareCarrier", 3),
          ("noResponse", 0),
          ("softwareCarrier", 2),
          ("unknown", 1))
    )


_SonusIsupsgFarEndCircuitAlarmCarrier_Type.__name__ = "Integer32"
_SonusIsupsgFarEndCircuitAlarmCarrier_Object = MibTableColumn
sonusIsupsgFarEndCircuitAlarmCarrier = _SonusIsupsgFarEndCircuitAlarmCarrier_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 6, 1, 6),
    _SonusIsupsgFarEndCircuitAlarmCarrier_Type()
)
sonusIsupsgFarEndCircuitAlarmCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgFarEndCircuitAlarmCarrier.setStatus("current")


class _SonusIsupsgFarEndCircuitContinuityRequirement_Type(Integer32):
    """Custom type sonusIsupsgFarEndCircuitContinuityRequirement based on Integer32"""
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
        *(("noResponse", 0),
          ("none", 2),
          ("perCall", 4),
          ("statistical", 3),
          ("unknown", 1))
    )


_SonusIsupsgFarEndCircuitContinuityRequirement_Type.__name__ = "Integer32"
_SonusIsupsgFarEndCircuitContinuityRequirement_Object = MibTableColumn
sonusIsupsgFarEndCircuitContinuityRequirement = _SonusIsupsgFarEndCircuitContinuityRequirement_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 6, 1, 7),
    _SonusIsupsgFarEndCircuitContinuityRequirement_Type()
)
sonusIsupsgFarEndCircuitContinuityRequirement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgFarEndCircuitContinuityRequirement.setStatus("current")
_SonusIsupsgFarEndCircuitIdentificationTrunkNumber_Type = SonusNameReference
_SonusIsupsgFarEndCircuitIdentificationTrunkNumber_Object = MibTableColumn
sonusIsupsgFarEndCircuitIdentificationTrunkNumber = _SonusIsupsgFarEndCircuitIdentificationTrunkNumber_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 6, 1, 8),
    _SonusIsupsgFarEndCircuitIdentificationTrunkNumber_Type()
)
sonusIsupsgFarEndCircuitIdentificationTrunkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgFarEndCircuitIdentificationTrunkNumber.setStatus("current")
_SonusIsupsgFarEndCircuitIdentificationOfficeA_Type = SonusNameReference
_SonusIsupsgFarEndCircuitIdentificationOfficeA_Object = MibTableColumn
sonusIsupsgFarEndCircuitIdentificationOfficeA = _SonusIsupsgFarEndCircuitIdentificationOfficeA_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 6, 1, 9),
    _SonusIsupsgFarEndCircuitIdentificationOfficeA_Type()
)
sonusIsupsgFarEndCircuitIdentificationOfficeA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgFarEndCircuitIdentificationOfficeA.setStatus("current")
_SonusIsupsgFarEndCircuitIdentificationOfficeZ_Type = SonusNameReference
_SonusIsupsgFarEndCircuitIdentificationOfficeZ_Object = MibTableColumn
sonusIsupsgFarEndCircuitIdentificationOfficeZ = _SonusIsupsgFarEndCircuitIdentificationOfficeZ_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 6, 1, 10),
    _SonusIsupsgFarEndCircuitIdentificationOfficeZ_Type()
)
sonusIsupsgFarEndCircuitIdentificationOfficeZ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgFarEndCircuitIdentificationOfficeZ.setStatus("current")
_SonusIsupsgFarEndCircuitLocationIdentification_Type = SonusNameReference
_SonusIsupsgFarEndCircuitLocationIdentification_Object = MibTableColumn
sonusIsupsgFarEndCircuitLocationIdentification = _SonusIsupsgFarEndCircuitLocationIdentification_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 6, 1, 11),
    _SonusIsupsgFarEndCircuitLocationIdentification_Type()
)
sonusIsupsgFarEndCircuitLocationIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgFarEndCircuitLocationIdentification.setStatus("current")


class _SonusIsupsgFarEndCircuitCicControlConflict_Type(Integer32):
    """Custom type sonusIsupsgFarEndCircuitCicControlConflict based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("noResponse", 0),
          ("yes", 1))
    )


_SonusIsupsgFarEndCircuitCicControlConflict_Type.__name__ = "Integer32"
_SonusIsupsgFarEndCircuitCicControlConflict_Object = MibTableColumn
sonusIsupsgFarEndCircuitCicControlConflict = _SonusIsupsgFarEndCircuitCicControlConflict_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 6, 1, 12),
    _SonusIsupsgFarEndCircuitCicControlConflict_Type()
)
sonusIsupsgFarEndCircuitCicControlConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgFarEndCircuitCicControlConflict.setStatus("current")
_SonusIsupsgFarEndCircuitStatTable_Object = MibTable
sonusIsupsgFarEndCircuitStatTable = _SonusIsupsgFarEndCircuitStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 7)
)
if mibBuilder.loadTexts:
    sonusIsupsgFarEndCircuitStatTable.setStatus("current")
_SonusIsupsgFarEndCircuitStatEntry_Object = MibTableRow
sonusIsupsgFarEndCircuitStatEntry = _SonusIsupsgFarEndCircuitStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 7, 1)
)
sonusIsupsgFarEndCircuitStatEntry.setIndexNames(
    (0, "SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupsgFarEndCircuitStatServiceListIndex"),
    (0, "SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupsgFarEndCircuitStatIdentityCode"),
)
if mibBuilder.loadTexts:
    sonusIsupsgFarEndCircuitStatEntry.setStatus("current")
_SonusIsupsgFarEndCircuitStatServiceListIndex_Type = Integer32
_SonusIsupsgFarEndCircuitStatServiceListIndex_Object = MibTableColumn
sonusIsupsgFarEndCircuitStatServiceListIndex = _SonusIsupsgFarEndCircuitStatServiceListIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 7, 1, 1),
    _SonusIsupsgFarEndCircuitStatServiceListIndex_Type()
)
sonusIsupsgFarEndCircuitStatServiceListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgFarEndCircuitStatServiceListIndex.setStatus("current")


class _SonusIsupsgFarEndCircuitStatIdentityCode_Type(Integer32):
    """Custom type sonusIsupsgFarEndCircuitStatIdentityCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_SonusIsupsgFarEndCircuitStatIdentityCode_Type.__name__ = "Integer32"
_SonusIsupsgFarEndCircuitStatIdentityCode_Object = MibTableColumn
sonusIsupsgFarEndCircuitStatIdentityCode = _SonusIsupsgFarEndCircuitStatIdentityCode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 7, 1, 2),
    _SonusIsupsgFarEndCircuitStatIdentityCode_Type()
)
sonusIsupsgFarEndCircuitStatIdentityCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgFarEndCircuitStatIdentityCode.setStatus("current")


class _SonusIsupsgFarEndCircuitStatStatus_Type(Integer32):
    """Custom type sonusIsupsgFarEndCircuitStatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("idle", 11),
          ("idleLocalBlocked", 12),
          ("idleLocalRemoteBlocked", 14),
          ("idleRemoteBlocked", 13),
          ("inbusyActive", 3),
          ("inbusyLocalBlocked", 4),
          ("inbusyLocalRemoteBlocked", 6),
          ("inbusyRemoteBlocked", 5),
          ("noResponse", 0),
          ("notAvailable", 15),
          ("outbusyActive", 7),
          ("outbusyLocalBlocked", 8),
          ("outbusyLocalRemoteBlocked", 10),
          ("outbusyRemoteBlocked", 9),
          ("transient", 1),
          ("unequipped", 2))
    )


_SonusIsupsgFarEndCircuitStatStatus_Type.__name__ = "Integer32"
_SonusIsupsgFarEndCircuitStatStatus_Object = MibTableColumn
sonusIsupsgFarEndCircuitStatStatus = _SonusIsupsgFarEndCircuitStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 7, 1, 3),
    _SonusIsupsgFarEndCircuitStatStatus_Type()
)
sonusIsupsgFarEndCircuitStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgFarEndCircuitStatStatus.setStatus("current")


class _SonusIsupsgFarEndCircuitStatLocalMaint_Type(Integer32):
    """Custom type sonusIsupsgFarEndCircuitStatLocalMaint based on Integer32"""
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
        *(("blocked", 2),
          ("notAvailable", 5),
          ("transientBlock", 4),
          ("transientUnblock", 3),
          ("unblocked", 1))
    )


_SonusIsupsgFarEndCircuitStatLocalMaint_Type.__name__ = "Integer32"
_SonusIsupsgFarEndCircuitStatLocalMaint_Object = MibTableColumn
sonusIsupsgFarEndCircuitStatLocalMaint = _SonusIsupsgFarEndCircuitStatLocalMaint_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 7, 1, 4),
    _SonusIsupsgFarEndCircuitStatLocalMaint_Type()
)
sonusIsupsgFarEndCircuitStatLocalMaint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgFarEndCircuitStatLocalMaint.setStatus("current")
_SonusIsupsgSignalingProfile_ObjectIdentity = ObjectIdentity
sonusIsupsgSignalingProfile = _SonusIsupsgSignalingProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8)
)
_SonusIsupsgSignalingProfileNextIndex_Type = Integer32
_SonusIsupsgSignalingProfileNextIndex_Object = MibScalar
sonusIsupsgSignalingProfileNextIndex = _SonusIsupsgSignalingProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 1),
    _SonusIsupsgSignalingProfileNextIndex_Type()
)
sonusIsupsgSignalingProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileNextIndex.setStatus("current")
_SonusIsupsgSignalingProfileTable_Object = MibTable
sonusIsupsgSignalingProfileTable = _SonusIsupsgSignalingProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2)
)
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileTable.setStatus("current")
_SonusIsupsgSignalingProfileEntry_Object = MibTableRow
sonusIsupsgSignalingProfileEntry = _SonusIsupsgSignalingProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1)
)
sonusIsupsgSignalingProfileEntry.setIndexNames(
    (0, "SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupsgSignalingProfileListIndex"),
)
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileEntry.setStatus("current")


class _SonusIsupsgSignalingProfileListIndex_Type(Integer32):
    """Custom type sonusIsupsgSignalingProfileListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SonusIsupsgSignalingProfileListIndex_Type.__name__ = "Integer32"
_SonusIsupsgSignalingProfileListIndex_Object = MibTableColumn
sonusIsupsgSignalingProfileListIndex = _SonusIsupsgSignalingProfileListIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 1),
    _SonusIsupsgSignalingProfileListIndex_Type()
)
sonusIsupsgSignalingProfileListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileListIndex.setStatus("current")
_SonusIsupsgSignalingProfileName_Type = SonusName
_SonusIsupsgSignalingProfileName_Object = MibTableColumn
sonusIsupsgSignalingProfileName = _SonusIsupsgSignalingProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 2),
    _SonusIsupsgSignalingProfileName_Type()
)
sonusIsupsgSignalingProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileName.setStatus("current")
_SonusIsupsgSignalingProfileCompat_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileCompat_Object = MibTableColumn
sonusIsupsgSignalingProfileCompat = _SonusIsupsgSignalingProfileCompat_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 3),
    _SonusIsupsgSignalingProfileCompat_Type()
)
sonusIsupsgSignalingProfileCompat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileCompat.setStatus("current")
_SonusIsupsgSignalingProfileAccessDel_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileAccessDel_Object = MibTableColumn
sonusIsupsgSignalingProfileAccessDel = _SonusIsupsgSignalingProfileAccessDel_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 4),
    _SonusIsupsgSignalingProfileAccessDel_Type()
)
sonusIsupsgSignalingProfileAccessDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileAccessDel.setStatus("current")
_SonusIsupsgSignalingProfileGenNum_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileGenNum_Object = MibTableColumn
sonusIsupsgSignalingProfileGenNum = _SonusIsupsgSignalingProfileGenNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 5),
    _SonusIsupsgSignalingProfileGenNum_Type()
)
sonusIsupsgSignalingProfileGenNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileGenNum.setStatus("current")
_SonusIsupsgSignalingProfileGenNotif_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileGenNotif_Object = MibTableColumn
sonusIsupsgSignalingProfileGenNotif = _SonusIsupsgSignalingProfileGenNotif_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 6),
    _SonusIsupsgSignalingProfileGenNotif_Type()
)
sonusIsupsgSignalingProfileGenNotif.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileGenNotif.setStatus("current")
_SonusIsupsgSignalingProfileGenDigs_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileGenDigs_Object = MibTableColumn
sonusIsupsgSignalingProfileGenDigs = _SonusIsupsgSignalingProfileGenDigs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 7),
    _SonusIsupsgSignalingProfileGenDigs_Type()
)
sonusIsupsgSignalingProfileGenDigs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileGenDigs.setStatus("current")
_SonusIsupsgSignalingProfileLocNum_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileLocNum_Object = MibTableColumn
sonusIsupsgSignalingProfileLocNum = _SonusIsupsgSignalingProfileLocNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 8),
    _SonusIsupsgSignalingProfileLocNum_Type()
)
sonusIsupsgSignalingProfileLocNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileLocNum.setStatus("current")
_SonusIsupsgSignalingProfileOrigIscPC_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileOrigIscPC_Object = MibTableColumn
sonusIsupsgSignalingProfileOrigIscPC = _SonusIsupsgSignalingProfileOrigIscPC_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 9),
    _SonusIsupsgSignalingProfileOrigIscPC_Type()
)
sonusIsupsgSignalingProfileOrigIscPC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileOrigIscPC.setStatus("current")
_SonusIsupsgSignalingProfileUserTeleService_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileUserTeleService_Object = MibTableColumn
sonusIsupsgSignalingProfileUserTeleService = _SonusIsupsgSignalingProfileUserTeleService_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 10),
    _SonusIsupsgSignalingProfileUserTeleService_Type()
)
sonusIsupsgSignalingProfileUserTeleService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileUserTeleService.setStatus("current")
_SonusIsupsgSignalingProfileSegmentation_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileSegmentation_Object = MibTableColumn
sonusIsupsgSignalingProfileSegmentation = _SonusIsupsgSignalingProfileSegmentation_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 11),
    _SonusIsupsgSignalingProfileSegmentation_Type()
)
sonusIsupsgSignalingProfileSegmentation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileSegmentation.setStatus("current")
_SonusIsupsgSignalingProfileFallback_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileFallback_Object = MibTableColumn
sonusIsupsgSignalingProfileFallback = _SonusIsupsgSignalingProfileFallback_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 12),
    _SonusIsupsgSignalingProfileFallback_Type()
)
sonusIsupsgSignalingProfileFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileFallback.setStatus("current")
_SonusIsupsgSignalingProfilePropDelay_Type = SonusSupportFlag
_SonusIsupsgSignalingProfilePropDelay_Object = MibTableColumn
sonusIsupsgSignalingProfilePropDelay = _SonusIsupsgSignalingProfilePropDelay_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 13),
    _SonusIsupsgSignalingProfilePropDelay_Type()
)
sonusIsupsgSignalingProfilePropDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfilePropDelay.setStatus("current")
_SonusIsupsgSignalingProfileEMcid_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileEMcid_Object = MibTableColumn
sonusIsupsgSignalingProfileEMcid = _SonusIsupsgSignalingProfileEMcid_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 14),
    _SonusIsupsgSignalingProfileEMcid_Type()
)
sonusIsupsgSignalingProfileEMcid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileEMcid.setStatus("current")
_SonusIsupsgSignalingProfileHopCounter_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileHopCounter_Object = MibTableColumn
sonusIsupsgSignalingProfileHopCounter = _SonusIsupsgSignalingProfileHopCounter_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 15),
    _SonusIsupsgSignalingProfileHopCounter_Type()
)
sonusIsupsgSignalingProfileHopCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileHopCounter.setStatus("current")
_SonusIsupsgSignalingProfileSubPriorityCls_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileSubPriorityCls_Object = MibTableColumn
sonusIsupsgSignalingProfileSubPriorityCls = _SonusIsupsgSignalingProfileSubPriorityCls_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 16),
    _SonusIsupsgSignalingProfileSubPriorityCls_Type()
)
sonusIsupsgSignalingProfileSubPriorityCls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileSubPriorityCls.setStatus("current")
_SonusIsupsgSignalingProfileAPM_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileAPM_Object = MibTableColumn
sonusIsupsgSignalingProfileAPM = _SonusIsupsgSignalingProfileAPM_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 17),
    _SonusIsupsgSignalingProfileAPM_Type()
)
sonusIsupsgSignalingProfileAPM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileAPM.setStatus("current")
_SonusIsupsgSignalingProfileConNumInAcm_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileConNumInAcm_Object = MibTableColumn
sonusIsupsgSignalingProfileConNumInAcm = _SonusIsupsgSignalingProfileConNumInAcm_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 18),
    _SonusIsupsgSignalingProfileConNumInAcm_Type()
)
sonusIsupsgSignalingProfileConNumInAcm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileConNumInAcm.setStatus("current")
_SonusIsupsgSignalingProfileCauseInCpg_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileCauseInCpg_Object = MibTableColumn
sonusIsupsgSignalingProfileCauseInCpg = _SonusIsupsgSignalingProfileCauseInCpg_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 19),
    _SonusIsupsgSignalingProfileCauseInCpg_Type()
)
sonusIsupsgSignalingProfileCauseInCpg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileCauseInCpg.setStatus("current")
_SonusIsupsgSignalingProfileMultiCarrierEnv_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileMultiCarrierEnv_Object = MibTableColumn
sonusIsupsgSignalingProfileMultiCarrierEnv = _SonusIsupsgSignalingProfileMultiCarrierEnv_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 20),
    _SonusIsupsgSignalingProfileMultiCarrierEnv_Type()
)
sonusIsupsgSignalingProfileMultiCarrierEnv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileMultiCarrierEnv.setStatus("current")
_SonusIsupsgSignalingProfileCarrierSelection_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileCarrierSelection_Object = MibTableColumn
sonusIsupsgSignalingProfileCarrierSelection = _SonusIsupsgSignalingProfileCarrierSelection_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 21),
    _SonusIsupsgSignalingProfileCarrierSelection_Type()
)
sonusIsupsgSignalingProfileCarrierSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileCarrierSelection.setStatus("current")
_SonusIsupsgSignalingProfileInrInf_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileInrInf_Object = MibTableColumn
sonusIsupsgSignalingProfileInrInf = _SonusIsupsgSignalingProfileInrInf_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 22),
    _SonusIsupsgSignalingProfileInrInf_Type()
)
sonusIsupsgSignalingProfileInrInf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileInrInf.setStatus("current")
_SonusIsupsgSignalingProfileCqmCqr_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileCqmCqr_Object = MibTableColumn
sonusIsupsgSignalingProfileCqmCqr = _SonusIsupsgSignalingProfileCqmCqr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 23),
    _SonusIsupsgSignalingProfileCqmCqr_Type()
)
sonusIsupsgSignalingProfileCqmCqr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileCqmCqr.setStatus("current")
_SonusIsupsgSignalingProfileCallRef_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileCallRef_Object = MibTableColumn
sonusIsupsgSignalingProfileCallRef = _SonusIsupsgSignalingProfileCallRef_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 24),
    _SonusIsupsgSignalingProfileCallRef_Type()
)
sonusIsupsgSignalingProfileCallRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileCallRef.setStatus("current")
_SonusIsupsgSignalingProfileCfn_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileCfn_Object = MibTableColumn
sonusIsupsgSignalingProfileCfn = _SonusIsupsgSignalingProfileCfn_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 25),
    _SonusIsupsgSignalingProfileCfn_Type()
)
sonusIsupsgSignalingProfileCfn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileCfn.setStatus("current")
_SonusIsupsgSignalingProfileFacility_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileFacility_Object = MibTableColumn
sonusIsupsgSignalingProfileFacility = _SonusIsupsgSignalingProfileFacility_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 26),
    _SonusIsupsgSignalingProfileFacility_Type()
)
sonusIsupsgSignalingProfileFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileFacility.setStatus("current")
_SonusIsupsgSignalingProfilePam_Type = SonusSupportFlag
_SonusIsupsgSignalingProfilePam_Object = MibTableColumn
sonusIsupsgSignalingProfilePam = _SonusIsupsgSignalingProfilePam_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 27),
    _SonusIsupsgSignalingProfilePam_Type()
)
sonusIsupsgSignalingProfilePam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfilePam.setStatus("current")
_SonusIsupsgSignalingProfileObciAnm_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileObciAnm_Object = MibTableColumn
sonusIsupsgSignalingProfileObciAnm = _SonusIsupsgSignalingProfileObciAnm_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 28),
    _SonusIsupsgSignalingProfileObciAnm_Type()
)
sonusIsupsgSignalingProfileObciAnm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileObciAnm.setStatus("current")
_SonusIsupsgSignalingProfileDrs_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileDrs_Object = MibTableColumn
sonusIsupsgSignalingProfileDrs = _SonusIsupsgSignalingProfileDrs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 29),
    _SonusIsupsgSignalingProfileDrs_Type()
)
sonusIsupsgSignalingProfileDrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileDrs.setStatus("current")
_SonusIsupsgSignalingProfileRedNum_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileRedNum_Object = MibTableColumn
sonusIsupsgSignalingProfileRedNum = _SonusIsupsgSignalingProfileRedNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 30),
    _SonusIsupsgSignalingProfileRedNum_Type()
)
sonusIsupsgSignalingProfileRedNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileRedNum.setStatus("current")
_SonusIsupsgSignalingProfileLpa_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileLpa_Object = MibTableColumn
sonusIsupsgSignalingProfileLpa = _SonusIsupsgSignalingProfileLpa_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 31),
    _SonusIsupsgSignalingProfileLpa_Type()
)
sonusIsupsgSignalingProfileLpa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileLpa.setStatus("current")
_SonusIsupsgSignalingProfileUcic_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileUcic_Object = MibTableColumn
sonusIsupsgSignalingProfileUcic = _SonusIsupsgSignalingProfileUcic_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 32),
    _SonusIsupsgSignalingProfileUcic_Type()
)
sonusIsupsgSignalingProfileUcic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileUcic.setStatus("current")
_SonusIsupsgSignalingProfileOlm_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileOlm_Object = MibTableColumn
sonusIsupsgSignalingProfileOlm = _SonusIsupsgSignalingProfileOlm_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 33),
    _SonusIsupsgSignalingProfileOlm_Type()
)
sonusIsupsgSignalingProfileOlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileOlm.setStatus("current")
_SonusIsupsgSignalingProfileBBRel_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileBBRel_Object = MibTableColumn
sonusIsupsgSignalingProfileBBRel = _SonusIsupsgSignalingProfileBBRel_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 34),
    _SonusIsupsgSignalingProfileBBRel_Type()
)
sonusIsupsgSignalingProfileBBRel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileBBRel.setStatus("current")
_SonusIsupsgSignalingProfileUsr_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileUsr_Object = MibTableColumn
sonusIsupsgSignalingProfileUsr = _SonusIsupsgSignalingProfileUsr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 35),
    _SonusIsupsgSignalingProfileUsr_Type()
)
sonusIsupsgSignalingProfileUsr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileUsr.setStatus("current")
_SonusIsupsgSignalingProfileBBIam_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileBBIam_Object = MibTableColumn
sonusIsupsgSignalingProfileBBIam = _SonusIsupsgSignalingProfileBBIam_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 36),
    _SonusIsupsgSignalingProfileBBIam_Type()
)
sonusIsupsgSignalingProfileBBIam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileBBIam.setStatus("current")
_SonusIsupsgSignalingProfileCallModMsgs_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileCallModMsgs_Object = MibTableColumn
sonusIsupsgSignalingProfileCallModMsgs = _SonusIsupsgSignalingProfileCallModMsgs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 37),
    _SonusIsupsgSignalingProfileCallModMsgs_Type()
)
sonusIsupsgSignalingProfileCallModMsgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileCallModMsgs.setStatus("current")
_SonusIsupsgSignalingProfileCallDiv_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileCallDiv_Object = MibTableColumn
sonusIsupsgSignalingProfileCallDiv = _SonusIsupsgSignalingProfileCallDiv_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 38),
    _SonusIsupsgSignalingProfileCallDiv_Type()
)
sonusIsupsgSignalingProfileCallDiv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileCallDiv.setStatus("current")
_SonusIsupsgSignalingProfileCallHist_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileCallHist_Object = MibTableColumn
sonusIsupsgSignalingProfileCallHist = _SonusIsupsgSignalingProfileCallHist_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 39),
    _SonusIsupsgSignalingProfileCallHist_Type()
)
sonusIsupsgSignalingProfileCallHist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileCallHist.setStatus("current")
_SonusIsupsgSignalingProfileGenRef_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileGenRef_Object = MibTableColumn
sonusIsupsgSignalingProfileGenRef = _SonusIsupsgSignalingProfileGenRef_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 40),
    _SonusIsupsgSignalingProfileGenRef_Type()
)
sonusIsupsgSignalingProfileGenRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileGenRef.setStatus("current")
_SonusIsupsgSignalingProfileMLPP_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileMLPP_Object = MibTableColumn
sonusIsupsgSignalingProfileMLPP = _SonusIsupsgSignalingProfileMLPP_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 41),
    _SonusIsupsgSignalingProfileMLPP_Type()
)
sonusIsupsgSignalingProfileMLPP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileMLPP.setStatus("current")
_SonusIsupsgSignalingProfileNSF_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileNSF_Object = MibTableColumn
sonusIsupsgSignalingProfileNSF = _SonusIsupsgSignalingProfileNSF_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 42),
    _SonusIsupsgSignalingProfileNSF_Type()
)
sonusIsupsgSignalingProfileNSF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileNSF.setStatus("current")
_SonusIsupsgSignalingProfileRedNumRist_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileRedNumRist_Object = MibTableColumn
sonusIsupsgSignalingProfileRedNumRist = _SonusIsupsgSignalingProfileRedNumRist_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 43),
    _SonusIsupsgSignalingProfileRedNumRist_Type()
)
sonusIsupsgSignalingProfileRedNumRist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileRedNumRist.setStatus("current")
_SonusIsupsgSignalingProfileRemoteOp_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileRemoteOp_Object = MibTableColumn
sonusIsupsgSignalingProfileRemoteOp = _SonusIsupsgSignalingProfileRemoteOp_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 44),
    _SonusIsupsgSignalingProfileRemoteOp_Type()
)
sonusIsupsgSignalingProfileRemoteOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileRemoteOp.setStatus("current")
_SonusIsupsgSignalingProfileServActv_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileServActv_Object = MibTableColumn
sonusIsupsgSignalingProfileServActv = _SonusIsupsgSignalingProfileServActv_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 45),
    _SonusIsupsgSignalingProfileServActv_Type()
)
sonusIsupsgSignalingProfileServActv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileServActv.setStatus("current")
_SonusIsupsgSignalingProfileSigPointCode_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileSigPointCode_Object = MibTableColumn
sonusIsupsgSignalingProfileSigPointCode = _SonusIsupsgSignalingProfileSigPointCode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 46),
    _SonusIsupsgSignalingProfileSigPointCode_Type()
)
sonusIsupsgSignalingProfileSigPointCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileSigPointCode.setStatus("current")
_SonusIsupsgSignalingProfileTmrPrime_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileTmrPrime_Object = MibTableColumn
sonusIsupsgSignalingProfileTmrPrime = _SonusIsupsgSignalingProfileTmrPrime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 47),
    _SonusIsupsgSignalingProfileTmrPrime_Type()
)
sonusIsupsgSignalingProfileTmrPrime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileTmrPrime.setStatus("current")
_SonusIsupsgSignalingProfileTransMedUsed_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileTransMedUsed_Object = MibTableColumn
sonusIsupsgSignalingProfileTransMedUsed = _SonusIsupsgSignalingProfileTransMedUsed_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 48),
    _SonusIsupsgSignalingProfileTransMedUsed_Type()
)
sonusIsupsgSignalingProfileTransMedUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileTransMedUsed.setStatus("current")
_SonusIsupsgSignalingProfileUsiPrime_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileUsiPrime_Object = MibTableColumn
sonusIsupsgSignalingProfileUsiPrime = _SonusIsupsgSignalingProfileUsiPrime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 49),
    _SonusIsupsgSignalingProfileUsiPrime_Type()
)
sonusIsupsgSignalingProfileUsiPrime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileUsiPrime.setStatus("current")
_SonusIsupsgSignalingProfileRedNumInAcm_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileRedNumInAcm_Object = MibTableColumn
sonusIsupsgSignalingProfileRedNumInAcm = _SonusIsupsgSignalingProfileRedNumInAcm_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 50),
    _SonusIsupsgSignalingProfileRedNumInAcm_Type()
)
sonusIsupsgSignalingProfileRedNumInAcm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileRedNumInAcm.setStatus("current")
_SonusIsupsgSignalingProfileRedNumInAnm_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileRedNumInAnm_Object = MibTableColumn
sonusIsupsgSignalingProfileRedNumInAnm = _SonusIsupsgSignalingProfileRedNumInAnm_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 51),
    _SonusIsupsgSignalingProfileRedNumInAnm_Type()
)
sonusIsupsgSignalingProfileRedNumInAnm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileRedNumInAnm.setStatus("current")
_SonusIsupsgSignalingProfileUuiInRel_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileUuiInRel_Object = MibTableColumn
sonusIsupsgSignalingProfileUuiInRel = _SonusIsupsgSignalingProfileUuiInRel_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 52),
    _SonusIsupsgSignalingProfileUuiInRel_Type()
)
sonusIsupsgSignalingProfileUuiInRel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileUuiInRel.setStatus("current")
_SonusIsupsgSignalingProfileConReqInFaa_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileConReqInFaa_Object = MibTableColumn
sonusIsupsgSignalingProfileConReqInFaa = _SonusIsupsgSignalingProfileConReqInFaa_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 53),
    _SonusIsupsgSignalingProfileConReqInFaa_Type()
)
sonusIsupsgSignalingProfileConReqInFaa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileConReqInFaa.setStatus("current")
_SonusIsupsgSignalingProfileConReqInFar_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileConReqInFar_Object = MibTableColumn
sonusIsupsgSignalingProfileConReqInFar = _SonusIsupsgSignalingProfileConReqInFar_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 54),
    _SonusIsupsgSignalingProfileConReqInFar_Type()
)
sonusIsupsgSignalingProfileConReqInFar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileConReqInFar.setStatus("current")
_SonusIsupsgSignalingProfileFac_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileFac_Object = MibTableColumn
sonusIsupsgSignalingProfileFac = _SonusIsupsgSignalingProfileFac_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 55),
    _SonusIsupsgSignalingProfileFac_Type()
)
sonusIsupsgSignalingProfileFac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileFac.setStatus("current")
_SonusIsupsgSignalingProfileEchoControl_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileEchoControl_Object = MibTableColumn
sonusIsupsgSignalingProfileEchoControl = _SonusIsupsgSignalingProfileEchoControl_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 56),
    _SonusIsupsgSignalingProfileEchoControl_Type()
)
sonusIsupsgSignalingProfileEchoControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileEchoControl.setStatus("current")
_SonusIsupsgSignalingProfileBackwardGVNS_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileBackwardGVNS_Object = MibTableColumn
sonusIsupsgSignalingProfileBackwardGVNS = _SonusIsupsgSignalingProfileBackwardGVNS_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 57),
    _SonusIsupsgSignalingProfileBackwardGVNS_Type()
)
sonusIsupsgSignalingProfileBackwardGVNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileBackwardGVNS.setStatus("current")
_SonusIsupsgSignalingProfileCircAssMap_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileCircAssMap_Object = MibTableColumn
sonusIsupsgSignalingProfileCircAssMap = _SonusIsupsgSignalingProfileCircAssMap_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 58),
    _SonusIsupsgSignalingProfileCircAssMap_Type()
)
sonusIsupsgSignalingProfileCircAssMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileCircAssMap.setStatus("current")
_SonusIsupsgSignalingProfileCCSS_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileCCSS_Object = MibTableColumn
sonusIsupsgSignalingProfileCCSS = _SonusIsupsgSignalingProfileCCSS_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 59),
    _SonusIsupsgSignalingProfileCCSS_Type()
)
sonusIsupsgSignalingProfileCCSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileCCSS.setStatus("current")
_SonusIsupsgSignalingProfileCallDivTreat_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileCallDivTreat_Object = MibTableColumn
sonusIsupsgSignalingProfileCallDivTreat = _SonusIsupsgSignalingProfileCallDivTreat_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 60),
    _SonusIsupsgSignalingProfileCallDivTreat_Type()
)
sonusIsupsgSignalingProfileCallDivTreat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileCallDivTreat.setStatus("current")
_SonusIsupsgSignalingProfileCalledInNum_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileCalledInNum_Object = MibTableColumn
sonusIsupsgSignalingProfileCalledInNum = _SonusIsupsgSignalingProfileCalledInNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 61),
    _SonusIsupsgSignalingProfileCalledInNum_Type()
)
sonusIsupsgSignalingProfileCalledInNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileCalledInNum.setStatus("current")
_SonusIsupsgSignalingProfileCollectCallReq_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileCollectCallReq_Object = MibTableColumn
sonusIsupsgSignalingProfileCollectCallReq = _SonusIsupsgSignalingProfileCollectCallReq_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 62),
    _SonusIsupsgSignalingProfileCollectCallReq_Type()
)
sonusIsupsgSignalingProfileCollectCallReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileCollectCallReq.setStatus("current")
_SonusIsupsgSignalingProfileConfTreat_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileConfTreat_Object = MibTableColumn
sonusIsupsgSignalingProfileConfTreat = _SonusIsupsgSignalingProfileConfTreat_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 63),
    _SonusIsupsgSignalingProfileConfTreat_Type()
)
sonusIsupsgSignalingProfileConfTreat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileConfTreat.setStatus("current")
_SonusIsupsgSignalingProfileCorrelationId_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileCorrelationId_Object = MibTableColumn
sonusIsupsgSignalingProfileCorrelationId = _SonusIsupsgSignalingProfileCorrelationId_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 64),
    _SonusIsupsgSignalingProfileCorrelationId_Type()
)
sonusIsupsgSignalingProfileCorrelationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileCorrelationId.setStatus("current")
_SonusIsupsgSignalingProfileCallOfrTreat_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileCallOfrTreat_Object = MibTableColumn
sonusIsupsgSignalingProfileCallOfrTreat = _SonusIsupsgSignalingProfileCallOfrTreat_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 65),
    _SonusIsupsgSignalingProfileCallOfrTreat_Type()
)
sonusIsupsgSignalingProfileCallOfrTreat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileCallOfrTreat.setStatus("current")
_SonusIsupsgSignalingProfileCallTransNum_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileCallTransNum_Object = MibTableColumn
sonusIsupsgSignalingProfileCallTransNum = _SonusIsupsgSignalingProfileCallTransNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 66),
    _SonusIsupsgSignalingProfileCallTransNum_Type()
)
sonusIsupsgSignalingProfileCallTransNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileCallTransNum.setStatus("current")
_SonusIsupsgSignalingProfileCallTransRef_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileCallTransRef_Object = MibTableColumn
sonusIsupsgSignalingProfileCallTransRef = _SonusIsupsgSignalingProfileCallTransRef_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 67),
    _SonusIsupsgSignalingProfileCallTransRef_Type()
)
sonusIsupsgSignalingProfileCallTransRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileCallTransRef.setStatus("current")
_SonusIsupsgSignalingProfileDispInfo_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileDispInfo_Object = MibTableColumn
sonusIsupsgSignalingProfileDispInfo = _SonusIsupsgSignalingProfileDispInfo_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 68),
    _SonusIsupsgSignalingProfileDispInfo_Type()
)
sonusIsupsgSignalingProfileDispInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileDispInfo.setStatus("current")
_SonusIsupsgSignalingProfileForwardGVNS_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileForwardGVNS_Object = MibTableColumn
sonusIsupsgSignalingProfileForwardGVNS = _SonusIsupsgSignalingProfileForwardGVNS_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 69),
    _SonusIsupsgSignalingProfileForwardGVNS_Type()
)
sonusIsupsgSignalingProfileForwardGVNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileForwardGVNS.setStatus("current")
_SonusIsupsgSignalingProfileLoopPrevention_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileLoopPrevention_Object = MibTableColumn
sonusIsupsgSignalingProfileLoopPrevention = _SonusIsupsgSignalingProfileLoopPrevention_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 70),
    _SonusIsupsgSignalingProfileLoopPrevention_Type()
)
sonusIsupsgSignalingProfileLoopPrevention.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileLoopPrevention.setStatus("current")
_SonusIsupsgSignalingProfileNetworkMgmt_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileNetworkMgmt_Object = MibTableColumn
sonusIsupsgSignalingProfileNetworkMgmt = _SonusIsupsgSignalingProfileNetworkMgmt_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 71),
    _SonusIsupsgSignalingProfileNetworkMgmt_Type()
)
sonusIsupsgSignalingProfileNetworkMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileNetworkMgmt.setStatus("current")
_SonusIsupsgSignalingProfileSCFId_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileSCFId_Object = MibTableColumn
sonusIsupsgSignalingProfileSCFId = _SonusIsupsgSignalingProfileSCFId_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 72),
    _SonusIsupsgSignalingProfileSCFId_Type()
)
sonusIsupsgSignalingProfileSCFId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileSCFId.setStatus("current")
_SonusIsupsgSignalingProfileUIDActionInd_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileUIDActionInd_Object = MibTableColumn
sonusIsupsgSignalingProfileUIDActionInd = _SonusIsupsgSignalingProfileUIDActionInd_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 73),
    _SonusIsupsgSignalingProfileUIDActionInd_Type()
)
sonusIsupsgSignalingProfileUIDActionInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileUIDActionInd.setStatus("current")
_SonusIsupsgSignalingProfileUIDCapInd_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileUIDCapInd_Object = MibTableColumn
sonusIsupsgSignalingProfileUIDCapInd = _SonusIsupsgSignalingProfileUIDCapInd_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 74),
    _SonusIsupsgSignalingProfileUIDCapInd_Type()
)
sonusIsupsgSignalingProfileUIDCapInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileUIDCapInd.setStatus("current")
_SonusIsupsgSignalingProfileConNumInCpg_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileConNumInCpg_Object = MibTableColumn
sonusIsupsgSignalingProfileConNumInCpg = _SonusIsupsgSignalingProfileConNumInCpg_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 75),
    _SonusIsupsgSignalingProfileConNumInCpg_Type()
)
sonusIsupsgSignalingProfileConNumInCpg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileConNumInCpg.setStatus("current")
_SonusIsupsgSignalingProfileGenNumInCpg_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileGenNumInCpg_Object = MibTableColumn
sonusIsupsgSignalingProfileGenNumInCpg = _SonusIsupsgSignalingProfileGenNumInCpg_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 76),
    _SonusIsupsgSignalingProfileGenNumInCpg_Type()
)
sonusIsupsgSignalingProfileGenNumInCpg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileGenNumInCpg.setStatus("current")
_SonusIsupsgSignalingProfileEchoCntrlInIam_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileEchoCntrlInIam_Object = MibTableColumn
sonusIsupsgSignalingProfileEchoCntrlInIam = _SonusIsupsgSignalingProfileEchoCntrlInIam_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 77),
    _SonusIsupsgSignalingProfileEchoCntrlInIam_Type()
)
sonusIsupsgSignalingProfileEchoCntrlInIam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileEchoCntrlInIam.setStatus("current")
_SonusIsupsgSignalingProfileRemoteOpInRel_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileRemoteOpInRel_Object = MibTableColumn
sonusIsupsgSignalingProfileRemoteOpInRel = _SonusIsupsgSignalingProfileRemoteOpInRel_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 78),
    _SonusIsupsgSignalingProfileRemoteOpInRel_Type()
)
sonusIsupsgSignalingProfileRemoteOpInRel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileRemoteOpInRel.setStatus("current")
_SonusIsupsgSignalingProfileAccessTransInFac_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileAccessTransInFac_Object = MibTableColumn
sonusIsupsgSignalingProfileAccessTransInFac = _SonusIsupsgSignalingProfileAccessTransInFac_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 79),
    _SonusIsupsgSignalingProfileAccessTransInFac_Type()
)
sonusIsupsgSignalingProfileAccessTransInFac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileAccessTransInFac.setStatus("current")
_SonusIsupsgSignalingProfileGenNotifInFac_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileGenNotifInFac_Object = MibTableColumn
sonusIsupsgSignalingProfileGenNotifInFac = _SonusIsupsgSignalingProfileGenNotifInFac_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 80),
    _SonusIsupsgSignalingProfileGenNotifInFac_Type()
)
sonusIsupsgSignalingProfileGenNotifInFac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileGenNotifInFac.setStatus("current")
_SonusIsupsgSignalingProfileUuindAnm_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileUuindAnm_Object = MibTableColumn
sonusIsupsgSignalingProfileUuindAnm = _SonusIsupsgSignalingProfileUuindAnm_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 81),
    _SonusIsupsgSignalingProfileUuindAnm_Type()
)
sonusIsupsgSignalingProfileUuindAnm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileUuindAnm.setStatus("current")
_SonusIsupsgSignalingProfileUuindCpg_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileUuindCpg_Object = MibTableColumn
sonusIsupsgSignalingProfileUuindCpg = _SonusIsupsgSignalingProfileUuindCpg_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 82),
    _SonusIsupsgSignalingProfileUuindCpg_Type()
)
sonusIsupsgSignalingProfileUuindCpg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileUuindCpg.setStatus("current")
_SonusIsupsgSignalingProfileNrmSupport_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileNrmSupport_Object = MibTableColumn
sonusIsupsgSignalingProfileNrmSupport = _SonusIsupsgSignalingProfileNrmSupport_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 83),
    _SonusIsupsgSignalingProfileNrmSupport_Type()
)
sonusIsupsgSignalingProfileNrmSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileNrmSupport.setStatus("current")
_SonusIsupsgSignalingProfileCseInRlc_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileCseInRlc_Object = MibTableColumn
sonusIsupsgSignalingProfileCseInRlc = _SonusIsupsgSignalingProfileCseInRlc_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 84),
    _SonusIsupsgSignalingProfileCseInRlc_Type()
)
sonusIsupsgSignalingProfileCseInRlc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileCseInRlc.setStatus("current")
_SonusIsupsgSignalingProfileUpaUpt_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileUpaUpt_Object = MibTableColumn
sonusIsupsgSignalingProfileUpaUpt = _SonusIsupsgSignalingProfileUpaUpt_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 85),
    _SonusIsupsgSignalingProfileUpaUpt_Type()
)
sonusIsupsgSignalingProfileUpaUpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileUpaUpt.setStatus("current")
_SonusIsupsgSignalingProfileRecInCai_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileRecInCai_Object = MibTableColumn
sonusIsupsgSignalingProfileRecInCai = _SonusIsupsgSignalingProfileRecInCai_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 86),
    _SonusIsupsgSignalingProfileRecInCai_Type()
)
sonusIsupsgSignalingProfileRecInCai.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileRecInCai.setStatus("current")
_SonusIsupsgSignalingProfileTransitUnrec_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileTransitUnrec_Object = MibTableColumn
sonusIsupsgSignalingProfileTransitUnrec = _SonusIsupsgSignalingProfileTransitUnrec_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 87),
    _SonusIsupsgSignalingProfileTransitUnrec_Type()
)
sonusIsupsgSignalingProfileTransitUnrec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileTransitUnrec.setStatus("current")
_SonusIsupsgSignalingProfileCcRaw_Type = SonusSupportFlag
_SonusIsupsgSignalingProfileCcRaw_Object = MibTableColumn
sonusIsupsgSignalingProfileCcRaw = _SonusIsupsgSignalingProfileCcRaw_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 88),
    _SonusIsupsgSignalingProfileCcRaw_Type()
)
sonusIsupsgSignalingProfileCcRaw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileCcRaw.setStatus("current")


class _SonusIsupsgSignalingProfileCctGrpBlockFlag_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileCctGrpBlockFlag based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileCctGrpBlockFlag_Object = MibTableColumn
sonusIsupsgSignalingProfileCctGrpBlockFlag = _SonusIsupsgSignalingProfileCctGrpBlockFlag_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 89),
    _SonusIsupsgSignalingProfileCctGrpBlockFlag_Type()
)
sonusIsupsgSignalingProfileCctGrpBlockFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileCctGrpBlockFlag.setStatus("current")


class _SonusIsupsgSignalingProfileCctGrpResetFlag_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileCctGrpResetFlag based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileCctGrpResetFlag_Object = MibTableColumn
sonusIsupsgSignalingProfileCctGrpResetFlag = _SonusIsupsgSignalingProfileCctGrpResetFlag_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 90),
    _SonusIsupsgSignalingProfileCctGrpResetFlag_Type()
)
sonusIsupsgSignalingProfileCctGrpResetFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileCctGrpResetFlag.setStatus("current")
_SonusIsupsgSignalingProfileBaseProfileName_Type = SonusNameReference
_SonusIsupsgSignalingProfileBaseProfileName_Object = MibTableColumn
sonusIsupsgSignalingProfileBaseProfileName = _SonusIsupsgSignalingProfileBaseProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 91),
    _SonusIsupsgSignalingProfileBaseProfileName_Type()
)
sonusIsupsgSignalingProfileBaseProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileBaseProfileName.setStatus("current")
_SonusIsupsgSignalingProfileAdminState_Type = SonusAdminState
_SonusIsupsgSignalingProfileAdminState_Object = MibTableColumn
sonusIsupsgSignalingProfileAdminState = _SonusIsupsgSignalingProfileAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 92),
    _SonusIsupsgSignalingProfileAdminState_Type()
)
sonusIsupsgSignalingProfileAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileAdminState.setStatus("current")
_SonusIsupsgSignalingProfileRowStatus_Type = RowStatus
_SonusIsupsgSignalingProfileRowStatus_Object = MibTableColumn
sonusIsupsgSignalingProfileRowStatus = _SonusIsupsgSignalingProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 93),
    _SonusIsupsgSignalingProfileRowStatus_Type()
)
sonusIsupsgSignalingProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileRowStatus.setStatus("current")


class _SonusIsupsgSignalingProfilePropDelayValue_Type(Integer32):
    """Custom type sonusIsupsgSignalingProfilePropDelayValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 400),
    )


_SonusIsupsgSignalingProfilePropDelayValue_Type.__name__ = "Integer32"
_SonusIsupsgSignalingProfilePropDelayValue_Object = MibTableColumn
sonusIsupsgSignalingProfilePropDelayValue = _SonusIsupsgSignalingProfilePropDelayValue_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 94),
    _SonusIsupsgSignalingProfilePropDelayValue_Type()
)
sonusIsupsgSignalingProfilePropDelayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfilePropDelayValue.setStatus("current")


class _SonusIsupsgSignalingProfileU2USrvcLevel_Type(Integer32):
    """Custom type sonusIsupsgSignalingProfileU2USrvcLevel based on Integer32"""
    defaultValue = 0

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
        *(("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("none", 0))
    )


_SonusIsupsgSignalingProfileU2USrvcLevel_Type.__name__ = "Integer32"
_SonusIsupsgSignalingProfileU2USrvcLevel_Object = MibTableColumn
sonusIsupsgSignalingProfileU2USrvcLevel = _SonusIsupsgSignalingProfileU2USrvcLevel_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 95),
    _SonusIsupsgSignalingProfileU2USrvcLevel_Type()
)
sonusIsupsgSignalingProfileU2USrvcLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileU2USrvcLevel.setStatus("current")


class _SonusIsupsgSignalingProfileSAM_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileSAM based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileSAM_Object = MibTableColumn
sonusIsupsgSignalingProfileSAM = _SonusIsupsgSignalingProfileSAM_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 96),
    _SonusIsupsgSignalingProfileSAM_Type()
)
sonusIsupsgSignalingProfileSAM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileSAM.setStatus("current")


class _SonusIsupsgSignalingProfileFOT_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileFOT based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileFOT_Object = MibTableColumn
sonusIsupsgSignalingProfileFOT = _SonusIsupsgSignalingProfileFOT_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 97),
    _SonusIsupsgSignalingProfileFOT_Type()
)
sonusIsupsgSignalingProfileFOT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileFOT.setStatus("current")


class _SonusIsupsgSignalingProfileSpecialDigits_Type(Bits):
    """Custom type sonusIsupsgSignalingProfileSpecialDigits based on Bits"""
    namedValues = NamedValues(
        *(("digitA", 0),
          ("digitB", 1),
          ("digitC", 2),
          ("digitD", 3),
          ("digitE", 4),
          ("digitF", 5),
          ("none", 6))
    )

_SonusIsupsgSignalingProfileSpecialDigits_Type.__name__ = "Bits"
_SonusIsupsgSignalingProfileSpecialDigits_Object = MibTableColumn
sonusIsupsgSignalingProfileSpecialDigits = _SonusIsupsgSignalingProfileSpecialDigits_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 98),
    _SonusIsupsgSignalingProfileSpecialDigits_Type()
)
sonusIsupsgSignalingProfileSpecialDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileSpecialDigits.setStatus("current")


class _SonusIsupsgSignalingProfileTNS_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileTNS based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileTNS_Object = MibTableColumn
sonusIsupsgSignalingProfileTNS = _SonusIsupsgSignalingProfileTNS_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 99),
    _SonusIsupsgSignalingProfileTNS_Type()
)
sonusIsupsgSignalingProfileTNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileTNS.setStatus("current")


class _SonusIsupsgSignalingProfileAwaitDigits_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileAwaitDigits based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileAwaitDigits_Object = MibTableColumn
sonusIsupsgSignalingProfileAwaitDigits = _SonusIsupsgSignalingProfileAwaitDigits_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 100),
    _SonusIsupsgSignalingProfileAwaitDigits_Type()
)
sonusIsupsgSignalingProfileAwaitDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileAwaitDigits.setStatus("current")


class _SonusIsupsgSignalingProfileAccessTrans_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileAccessTrans based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileAccessTrans_Object = MibTableColumn
sonusIsupsgSignalingProfileAccessTrans = _SonusIsupsgSignalingProfileAccessTrans_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 101),
    _SonusIsupsgSignalingProfileAccessTrans_Type()
)
sonusIsupsgSignalingProfileAccessTrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileAccessTrans.setStatus("current")


class _SonusIsupsgSignalingProfileJurisdiction_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileJurisdiction based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileJurisdiction_Object = MibTableColumn
sonusIsupsgSignalingProfileJurisdiction = _SonusIsupsgSignalingProfileJurisdiction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 102),
    _SonusIsupsgSignalingProfileJurisdiction_Type()
)
sonusIsupsgSignalingProfileJurisdiction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileJurisdiction.setStatus("current")


class _SonusIsupsgSignalingProfileOCN_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileOCN based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileOCN_Object = MibTableColumn
sonusIsupsgSignalingProfileOCN = _SonusIsupsgSignalingProfileOCN_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 103),
    _SonusIsupsgSignalingProfileOCN_Type()
)
sonusIsupsgSignalingProfileOCN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileOCN.setStatus("current")


class _SonusIsupsgSignalingProfileBusinessGrp_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileBusinessGrp based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileBusinessGrp_Object = MibTableColumn
sonusIsupsgSignalingProfileBusinessGrp = _SonusIsupsgSignalingProfileBusinessGrp_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 104),
    _SonusIsupsgSignalingProfileBusinessGrp_Type()
)
sonusIsupsgSignalingProfileBusinessGrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileBusinessGrp.setStatus("current")


class _SonusIsupsgSignalingProfileConReq_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileConReq based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileConReq_Object = MibTableColumn
sonusIsupsgSignalingProfileConReq = _SonusIsupsgSignalingProfileConReq_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 105),
    _SonusIsupsgSignalingProfileConReq_Type()
)
sonusIsupsgSignalingProfileConReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileConReq.setStatus("current")


class _SonusIsupsgSignalingProfileInfoInd_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileInfoInd based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileInfoInd_Object = MibTableColumn
sonusIsupsgSignalingProfileInfoInd = _SonusIsupsgSignalingProfileInfoInd_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 106),
    _SonusIsupsgSignalingProfileInfoInd_Type()
)
sonusIsupsgSignalingProfileInfoInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileInfoInd.setStatus("current")


class _SonusIsupsgSignalingProfileNtp_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileNtp based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileNtp_Object = MibTableColumn
sonusIsupsgSignalingProfileNtp = _SonusIsupsgSignalingProfileNtp_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 107),
    _SonusIsupsgSignalingProfileNtp_Type()
)
sonusIsupsgSignalingProfileNtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileNtp.setStatus("current")


class _SonusIsupsgSignalingProfileNotifInd_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileNotifInd based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileNotifInd_Object = MibTableColumn
sonusIsupsgSignalingProfileNotifInd = _SonusIsupsgSignalingProfileNotifInd_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 108),
    _SonusIsupsgSignalingProfileNotifInd_Type()
)
sonusIsupsgSignalingProfileNotifInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileNotifInd.setStatus("current")


class _SonusIsupsgSignalingProfileRedInfoAcm_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileRedInfoAcm based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileRedInfoAcm_Object = MibTableColumn
sonusIsupsgSignalingProfileRedInfoAcm = _SonusIsupsgSignalingProfileRedInfoAcm_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 109),
    _SonusIsupsgSignalingProfileRedInfoAcm_Type()
)
sonusIsupsgSignalingProfileRedInfoAcm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileRedInfoAcm.setStatus("current")


class _SonusIsupsgSignalingProfileEgressService_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileEgressService based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileEgressService_Object = MibTableColumn
sonusIsupsgSignalingProfileEgressService = _SonusIsupsgSignalingProfileEgressService_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 110),
    _SonusIsupsgSignalingProfileEgressService_Type()
)
sonusIsupsgSignalingProfileEgressService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileEgressService.setStatus("current")


class _SonusIsupsgSignalingProfileServCodeInd_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileServCodeInd based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileServCodeInd_Object = MibTableColumn
sonusIsupsgSignalingProfileServCodeInd = _SonusIsupsgSignalingProfileServCodeInd_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 111),
    _SonusIsupsgSignalingProfileServCodeInd_Type()
)
sonusIsupsgSignalingProfileServCodeInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileServCodeInd.setStatus("current")


class _SonusIsupsgSignalingProfileSpecProcReq_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileSpecProcReq based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileSpecProcReq_Object = MibTableColumn
sonusIsupsgSignalingProfileSpecProcReq = _SonusIsupsgSignalingProfileSpecProcReq_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 112),
    _SonusIsupsgSignalingProfileSpecProcReq_Type()
)
sonusIsupsgSignalingProfileSpecProcReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileSpecProcReq.setStatus("current")


class _SonusIsupsgSignalingProfileTransReq_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileTransReq based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileTransReq_Object = MibTableColumn
sonusIsupsgSignalingProfileTransReq = _SonusIsupsgSignalingProfileTransReq_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 113),
    _SonusIsupsgSignalingProfileTransReq_Type()
)
sonusIsupsgSignalingProfileTransReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileTransReq.setStatus("current")


class _SonusIsupsgSignalingProfileChgNum_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileChgNum based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileChgNum_Object = MibTableColumn
sonusIsupsgSignalingProfileChgNum = _SonusIsupsgSignalingProfileChgNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 114),
    _SonusIsupsgSignalingProfileChgNum_Type()
)
sonusIsupsgSignalingProfileChgNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileChgNum.setStatus("current")


class _SonusIsupsgSignalingProfileGenAddressREL_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileGenAddressREL based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileGenAddressREL_Object = MibTableColumn
sonusIsupsgSignalingProfileGenAddressREL = _SonusIsupsgSignalingProfileGenAddressREL_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 115),
    _SonusIsupsgSignalingProfileGenAddressREL_Type()
)
sonusIsupsgSignalingProfileGenAddressREL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileGenAddressREL.setStatus("current")


class _SonusIsupsgSignalingProfileUUIndAcm_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileUUIndAcm based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileUUIndAcm_Object = MibTableColumn
sonusIsupsgSignalingProfileUUIndAcm = _SonusIsupsgSignalingProfileUUIndAcm_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 116),
    _SonusIsupsgSignalingProfileUUIndAcm_Type()
)
sonusIsupsgSignalingProfileUUIndAcm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileUUIndAcm.setStatus("current")


class _SonusIsupsgSignalingProfileUUInfo_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileUUInfo based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileUUInfo_Object = MibTableColumn
sonusIsupsgSignalingProfileUUInfo = _SonusIsupsgSignalingProfileUUInfo_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 117),
    _SonusIsupsgSignalingProfileUUInfo_Type()
)
sonusIsupsgSignalingProfileUUInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileUUInfo.setStatus("current")


class _SonusIsupsgSignalingProfileOperatorServInfo_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileOperatorServInfo based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileOperatorServInfo_Object = MibTableColumn
sonusIsupsgSignalingProfileOperatorServInfo = _SonusIsupsgSignalingProfileOperatorServInfo_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 118),
    _SonusIsupsgSignalingProfileOperatorServInfo_Type()
)
sonusIsupsgSignalingProfileOperatorServInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileOperatorServInfo.setStatus("current")


class _SonusIsupsgSignalingProfileCvtCvr_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileCvtCvr based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileCvtCvr_Object = MibTableColumn
sonusIsupsgSignalingProfileCvtCvr = _SonusIsupsgSignalingProfileCvtCvr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 119),
    _SonusIsupsgSignalingProfileCvtCvr_Type()
)
sonusIsupsgSignalingProfileCvtCvr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileCvtCvr.setStatus("current")


class _SonusIsupsgSignalingProfileGenName_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileGenName based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileGenName_Object = MibTableColumn
sonusIsupsgSignalingProfileGenName = _SonusIsupsgSignalingProfileGenName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 120),
    _SonusIsupsgSignalingProfileGenName_Type()
)
sonusIsupsgSignalingProfileGenName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileGenName.setStatus("current")


class _SonusIsupsgSignalingProfileRedCap_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileRedCap based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileRedCap_Object = MibTableColumn
sonusIsupsgSignalingProfileRedCap = _SonusIsupsgSignalingProfileRedCap_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 121),
    _SonusIsupsgSignalingProfileRedCap_Type()
)
sonusIsupsgSignalingProfileRedCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileRedCap.setStatus("current")


class _SonusIsupsgSignalingProfileRedCount_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileRedCount based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileRedCount_Object = MibTableColumn
sonusIsupsgSignalingProfileRedCount = _SonusIsupsgSignalingProfileRedCount_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 122),
    _SonusIsupsgSignalingProfileRedCount_Type()
)
sonusIsupsgSignalingProfileRedCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileRedCount.setStatus("current")


class _SonusIsupsgSignalingProfileSendTwoGrpMsgs_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileSendTwoGrpMsgs based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileSendTwoGrpMsgs_Object = MibTableColumn
sonusIsupsgSignalingProfileSendTwoGrpMsgs = _SonusIsupsgSignalingProfileSendTwoGrpMsgs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 123),
    _SonusIsupsgSignalingProfileSendTwoGrpMsgs_Type()
)
sonusIsupsgSignalingProfileSendTwoGrpMsgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileSendTwoGrpMsgs.setStatus("current")


class _SonusIsupsgSignalingProfileAwaitTwoGrpMsgs_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileAwaitTwoGrpMsgs based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileAwaitTwoGrpMsgs_Object = MibTableColumn
sonusIsupsgSignalingProfileAwaitTwoGrpMsgs = _SonusIsupsgSignalingProfileAwaitTwoGrpMsgs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 124),
    _SonusIsupsgSignalingProfileAwaitTwoGrpMsgs_Type()
)
sonusIsupsgSignalingProfileAwaitTwoGrpMsgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileAwaitTwoGrpMsgs.setStatus("current")


class _SonusIsupsgSignalingProfileCqmOnCardSwap_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileCqmOnCardSwap based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileCqmOnCardSwap_Object = MibTableColumn
sonusIsupsgSignalingProfileCqmOnCardSwap = _SonusIsupsgSignalingProfileCqmOnCardSwap_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 125),
    _SonusIsupsgSignalingProfileCqmOnCardSwap_Type()
)
sonusIsupsgSignalingProfileCqmOnCardSwap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileCqmOnCardSwap.setStatus("current")


class _SonusIsupsgSignalingProfileAnsi95Grs_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileAnsi95Grs based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileAnsi95Grs_Object = MibTableColumn
sonusIsupsgSignalingProfileAnsi95Grs = _SonusIsupsgSignalingProfileAnsi95Grs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 126),
    _SonusIsupsgSignalingProfileAnsi95Grs_Type()
)
sonusIsupsgSignalingProfileAnsi95Grs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileAnsi95Grs.setStatus("current")


class _SonusIsupsgSignalingProfileCpgBeforeAcm_Type(SonusSupportFlag):
    """Custom type sonusIsupsgSignalingProfileCpgBeforeAcm based on SonusSupportFlag"""


_SonusIsupsgSignalingProfileCpgBeforeAcm_Object = MibTableColumn
sonusIsupsgSignalingProfileCpgBeforeAcm = _SonusIsupsgSignalingProfileCpgBeforeAcm_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 1, 8, 2, 1, 127),
    _SonusIsupsgSignalingProfileCpgBeforeAcm_Type()
)
sonusIsupsgSignalingProfileCpgBeforeAcm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusIsupsgSignalingProfileCpgBeforeAcm.setStatus("current")
_SonusIsupServiceGroupMIBNotifications_ObjectIdentity = ObjectIdentity
sonusIsupServiceGroupMIBNotifications = _SonusIsupServiceGroupMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 2)
)
_SonusIsupServiceGroupMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusIsupServiceGroupMIBNotificationsPrefix = _SonusIsupServiceGroupMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 2, 0)
)
_SonusIsupServiceGroupMIBNotificationsObjects_ObjectIdentity = ObjectIdentity
sonusIsupServiceGroupMIBNotificationsObjects = _SonusIsupServiceGroupMIBNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 2, 1)
)


class _SonusIsupSvcGrpName_Type(DisplayString):
    """Custom type sonusIsupSvcGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusIsupSvcGrpName_Type.__name__ = "DisplayString"
_SonusIsupSvcGrpName_Object = MibScalar
sonusIsupSvcGrpName = _SonusIsupSvcGrpName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 2, 1, 1),
    _SonusIsupSvcGrpName_Type()
)
sonusIsupSvcGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupSvcGrpName.setStatus("current")


class _SonusIsupMaintReason_Type(Integer32):
    """Custom type sonusIsupMaintReason based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("circuitMode", 5),
          ("ds1Mode", 6),
          ("localHardware", 8),
          ("remoteHardware", 10),
          ("remoteMaintenance", 9),
          ("remoteSs7PointCodeAccess", 2),
          ("remoteUnequipped", 11),
          ("serverMode", 7),
          ("serviceGroupMode", 4),
          ("ss7GwRegistration", 1),
          ("ss7GwResynchronization", 12),
          ("trunkGroupMode", 3))
    )


_SonusIsupMaintReason_Type.__name__ = "Integer32"
_SonusIsupMaintReason_Object = MibScalar
sonusIsupMaintReason = _SonusIsupMaintReason_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 2, 1, 2),
    _SonusIsupMaintReason_Type()
)
sonusIsupMaintReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupMaintReason.setStatus("current")


class _SonusIsupTrunkGrpName_Type(DisplayString):
    """Custom type sonusIsupTrunkGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusIsupTrunkGrpName_Type.__name__ = "DisplayString"
_SonusIsupTrunkGrpName_Object = MibScalar
sonusIsupTrunkGrpName = _SonusIsupTrunkGrpName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 2, 1, 3),
    _SonusIsupTrunkGrpName_Type()
)
sonusIsupTrunkGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupTrunkGrpName.setStatus("current")


class _SonusIsupCircuit_Type(Integer32):
    """Custom type sonusIsupCircuit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_SonusIsupCircuit_Type.__name__ = "Integer32"
_SonusIsupCircuit_Object = MibScalar
sonusIsupCircuit = _SonusIsupCircuit_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 2, 1, 4),
    _SonusIsupCircuit_Type()
)
sonusIsupCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupCircuit.setStatus("current")


class _SonusIsupCircuitOffsets_Type(Bits):
    """Custom type sonusIsupCircuitOffsets based on Bits"""
    namedValues = NamedValues(
        *(("cicOffset0", 0),
          ("cicOffset1", 1),
          ("cicOffset10", 10),
          ("cicOffset11", 11),
          ("cicOffset12", 12),
          ("cicOffset13", 13),
          ("cicOffset14", 14),
          ("cicOffset15", 15),
          ("cicOffset16", 16),
          ("cicOffset17", 17),
          ("cicOffset18", 18),
          ("cicOffset19", 19),
          ("cicOffset2", 2),
          ("cicOffset20", 20),
          ("cicOffset21", 21),
          ("cicOffset22", 22),
          ("cicOffset23", 23),
          ("cicOffset3", 3),
          ("cicOffset4", 4),
          ("cicOffset5", 5),
          ("cicOffset6", 6),
          ("cicOffset7", 7),
          ("cicOffset8", 8),
          ("cicOffset9", 9))
    )

_SonusIsupCircuitOffsets_Type.__name__ = "Bits"
_SonusIsupCircuitOffsets_Object = MibScalar
sonusIsupCircuitOffsets = _SonusIsupCircuitOffsets_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 2, 1, 5),
    _SonusIsupCircuitOffsets_Type()
)
sonusIsupCircuitOffsets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupCircuitOffsets.setStatus("current")


class _SonusIsupCalledPartyNumber_Type(DisplayString):
    """Custom type sonusIsupCalledPartyNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SonusIsupCalledPartyNumber_Type.__name__ = "DisplayString"
_SonusIsupCalledPartyNumber_Object = MibScalar
sonusIsupCalledPartyNumber = _SonusIsupCalledPartyNumber_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 2, 1, 6),
    _SonusIsupCalledPartyNumber_Type()
)
sonusIsupCalledPartyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupCalledPartyNumber.setStatus("current")


class _SonusIsupCallingPartyNumber_Type(DisplayString):
    """Custom type sonusIsupCallingPartyNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SonusIsupCallingPartyNumber_Type.__name__ = "DisplayString"
_SonusIsupCallingPartyNumber_Object = MibScalar
sonusIsupCallingPartyNumber = _SonusIsupCallingPartyNumber_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 2, 1, 7),
    _SonusIsupCallingPartyNumber_Type()
)
sonusIsupCallingPartyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupCallingPartyNumber.setStatus("current")


class _SonusIsupMaintCode_Type(DisplayString):
    """Custom type sonusIsupMaintCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SonusIsupMaintCode_Type.__name__ = "DisplayString"
_SonusIsupMaintCode_Object = MibScalar
sonusIsupMaintCode = _SonusIsupMaintCode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 2, 1, 8),
    _SonusIsupMaintCode_Type()
)
sonusIsupMaintCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIsupMaintCode.setStatus("current")

# Managed Objects groups


# Notification objects

sonusIsupSvcGrpInServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 2, 0, 1)
)
sonusIsupSvcGrpInServiceNotification.setObjects(
      *(("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupSvcGrpName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusIsupSvcGrpInServiceNotification.setStatus(
        "current"
    )

sonusIsupSvcGrpOutOfServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 2, 0, 2)
)
sonusIsupSvcGrpOutOfServiceNotification.setObjects(
      *(("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupSvcGrpName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusIsupSvcGrpOutOfServiceNotification.setStatus(
        "current"
    )

sonusIsupCircuitBlockedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 2, 0, 3)
)
sonusIsupCircuitBlockedNotification.setObjects(
      *(("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupSvcGrpName"),
        ("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupMaintReason"),
        ("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupTrunkGrpName"),
        ("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupCircuit"),
        ("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupCircuitOffsets"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusIsupCircuitBlockedNotification.setStatus(
        "current"
    )

sonusIsupCircuitUnblockedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 2, 0, 4)
)
sonusIsupCircuitUnblockedNotification.setObjects(
      *(("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupSvcGrpName"),
        ("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupMaintReason"),
        ("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupTrunkGrpName"),
        ("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupCircuit"),
        ("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupCircuitOffsets"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusIsupCircuitUnblockedNotification.setStatus(
        "current"
    )

sonusIsupCircuitResetNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 2, 0, 5)
)
sonusIsupCircuitResetNotification.setObjects(
      *(("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupSvcGrpName"),
        ("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupTrunkGrpName"),
        ("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupCircuit"),
        ("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupCircuitOffsets"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusIsupCircuitResetNotification.setStatus(
        "current"
    )

sonusIsupContinuityRecheckFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 2, 0, 6)
)
sonusIsupContinuityRecheckFailureNotification.setObjects(
      *(("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupSvcGrpName"),
        ("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupCircuit"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusIsupContinuityRecheckFailureNotification.setStatus(
        "current"
    )

sonusIsupCicRegistrationFailedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 2, 0, 7)
)
sonusIsupCicRegistrationFailedNotification.setObjects(
      *(("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupCircuit"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusIsupCicRegistrationFailedNotification.setStatus(
        "current"
    )

sonusIsupHopCounterExhaustedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 2, 0, 8)
)
sonusIsupHopCounterExhaustedNotification.setObjects(
      *(("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupSvcGrpName"),
        ("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupCircuit"),
        ("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupCalledPartyNumber"),
        ("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupCallingPartyNumber"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusIsupHopCounterExhaustedNotification.setStatus(
        "current"
    )

sonusIsupRelWithExchangeRoutingErrorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 2, 0, 9)
)
sonusIsupRelWithExchangeRoutingErrorNotification.setObjects(
      *(("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupSvcGrpName"),
        ("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupCircuit"),
        ("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupCalledPartyNumber"),
        ("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupCallingPartyNumber"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusIsupRelWithExchangeRoutingErrorNotification.setStatus(
        "current"
    )

sonusIsupCqmTimeoutNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 2, 0, 10)
)
sonusIsupCqmTimeoutNotification.setObjects(
      *(("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupCircuit"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusIsupCqmTimeoutNotification.setStatus(
        "current"
    )

sonusIsupCvtTimeoutNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 2, 0, 11)
)
sonusIsupCvtTimeoutNotification.setObjects(
      *(("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupCircuit"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusIsupCvtTimeoutNotification.setStatus(
        "current"
    )

sonusIsupFarendCircuitStateMismatchedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 2, 0, 12)
)
sonusIsupFarendCircuitStateMismatchedNotification.setObjects(
      *(("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupCircuit"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusIsupFarendCircuitStateMismatchedNotification.setStatus(
        "current"
    )

sonusIsupCircuitTimerExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 1, 2, 0, 13)
)
sonusIsupCircuitTimerExpired.setObjects(
      *(("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupTrunkGrpName"),
        ("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupSvcGrpName"),
        ("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupCircuit"),
        ("SONUS-ISUP-SERVICE-GROUP-MIB", "sonusIsupMaintCode"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusIsupCircuitTimerExpired.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-ISUP-SERVICE-GROUP-MIB",
    **{"sonusIsupServiceGroupMIB": sonusIsupServiceGroupMIB,
       "sonusIsupServiceGroupMIBObjects": sonusIsupServiceGroupMIBObjects,
       "sonusIsupsgServiceGroup": sonusIsupsgServiceGroup,
       "sonusIsupsgServiceGroupNextIndex": sonusIsupsgServiceGroupNextIndex,
       "sonusIsupsgServiceGroupTable": sonusIsupsgServiceGroupTable,
       "sonusIsupsgServiceGroupEntry": sonusIsupsgServiceGroupEntry,
       "sonusIsupsgServiceGroupListIndex": sonusIsupsgServiceGroupListIndex,
       "sonusIsupsgServiceGroupName": sonusIsupsgServiceGroupName,
       "sonusIsupsgServiceGroupRemotePointCode": sonusIsupsgServiceGroupRemotePointCode,
       "sonusIsupsgServiceGroupTG": sonusIsupsgServiceGroupTG,
       "sonusIsupsgServiceGroupSwitchType": sonusIsupsgServiceGroupSwitchType,
       "sonusIsupsgServiceGroupRevision": sonusIsupsgServiceGroupRevision,
       "sonusIsupsgServiceGroupHuntAlgorithm": sonusIsupsgServiceGroupHuntAlgorithm,
       "sonusIsupsgServiceGroupCost": sonusIsupsgServiceGroupCost,
       "sonusIsupsgServiceGroupCicControl": sonusIsupsgServiceGroupCicControl,
       "sonusIsupsgServiceGroupContTestFreq": sonusIsupsgServiceGroupContTestFreq,
       "sonusIsupsgServiceGroupOperation": sonusIsupsgServiceGroupOperation,
       "sonusIsupsgServiceGroupMode": sonusIsupsgServiceGroupMode,
       "sonusIsupsgServiceGroupAction": sonusIsupsgServiceGroupAction,
       "sonusIsupsgServiceGroupTimeout": sonusIsupsgServiceGroupTimeout,
       "sonusIsupsgServiceGroupAdminState": sonusIsupsgServiceGroupAdminState,
       "sonusIsupsgServiceGroupProfileName": sonusIsupsgServiceGroupProfileName,
       "sonusIsupsgServiceGroupRowStatus": sonusIsupsgServiceGroupRowStatus,
       "sonusIsupsgServiceGroupHopCounterState": sonusIsupsgServiceGroupHopCounterState,
       "sonusIsupsgServiceGroupHopCounterValue": sonusIsupsgServiceGroupHopCounterValue,
       "sonusIsupsgServiceGroupDiscTreatmentProfileName": sonusIsupsgServiceGroupDiscTreatmentProfileName,
       "sonusIsupsgServiceGroupTonePackageName": sonusIsupsgServiceGroupTonePackageName,
       "sonusIsupsgServiceGroupGrsStartup": sonusIsupsgServiceGroupGrsStartup,
       "sonusIsupsgServiceGroupOlipCheck": sonusIsupsgServiceGroupOlipCheck,
       "sonusIsupsgServiceGroupRemPc": sonusIsupsgServiceGroupRemPc,
       "sonusIsupsgServiceGroupExchangeType": sonusIsupsgServiceGroupExchangeType,
       "sonusIsupsgServiceGroupInspectionTime": sonusIsupsgServiceGroupInspectionTime,
       "sonusIsupsgServiceGroupInspectionFreq": sonusIsupsgServiceGroupInspectionFreq,
       "sonusIsupsgServiceGroupInspectionState": sonusIsupsgServiceGroupInspectionState,
       "sonusIsupsgServiceGroupSignalingProfileName": sonusIsupsgServiceGroupSignalingProfileName,
       "sonusIsupsgServiceGroupAccRespProcess": sonusIsupsgServiceGroupAccRespProcess,
       "sonusIsupsgServiceGroupAccL1ARCancelpercentage": sonusIsupsgServiceGroupAccL1ARCancelpercentage,
       "sonusIsupsgServiceGroupAccL1DRCancelpercentage": sonusIsupsgServiceGroupAccL1DRCancelpercentage,
       "sonusIsupsgServiceGroupAccL2ARCancelpercentage": sonusIsupsgServiceGroupAccL2ARCancelpercentage,
       "sonusIsupsgServiceGroupAccL2DRCancelpercentage": sonusIsupsgServiceGroupAccL2DRCancelpercentage,
       "sonusIsupsgServiceGroupAccL3ARCancelpercentage": sonusIsupsgServiceGroupAccL3ARCancelpercentage,
       "sonusIsupsgServiceGroupAccL3DRCancelpercentage": sonusIsupsgServiceGroupAccL3DRCancelpercentage,
       "sonusIsupsgServiceGroupAccSendACL": sonusIsupsgServiceGroupAccSendACL,
       "sonusIsupsgServiceGroupGatewayOutage": sonusIsupsgServiceGroupGatewayOutage,
       "sonusIsupsgServiceGroupStatTable": sonusIsupsgServiceGroupStatTable,
       "sonusIsupsgServiceGroupStatEntry": sonusIsupsgServiceGroupStatEntry,
       "sonusIsupsgServiceGroupStatListIndex": sonusIsupsgServiceGroupStatListIndex,
       "sonusIsupsgServiceGroupStatName": sonusIsupsgServiceGroupStatName,
       "sonusIsupsgServiceGroupStatStatus": sonusIsupsgServiceGroupStatStatus,
       "sonusIsupsgServiceGroupStatLastInspectionTime": sonusIsupsgServiceGroupStatLastInspectionTime,
       "sonusIsupsgServiceGroupStatNextInspectionTime": sonusIsupsgServiceGroupStatNextInspectionTime,
       "sonusIsupsgSvcGrpProfile": sonusIsupsgSvcGrpProfile,
       "sonusIsupsgSvcGrpProfileNextIndex": sonusIsupsgSvcGrpProfileNextIndex,
       "sonusIsupsgSvcGrpProfileTable": sonusIsupsgSvcGrpProfileTable,
       "sonusIsupsgSvcGrpProfileEntry": sonusIsupsgSvcGrpProfileEntry,
       "sonusIsupsgSvcGrpProfileListIndex": sonusIsupsgSvcGrpProfileListIndex,
       "sonusIsupsgSvcGrpProfileName": sonusIsupsgSvcGrpProfileName,
       "sonusIsupsgSvcGrpProfileTG": sonusIsupsgSvcGrpProfileTG,
       "sonusIsupsgSvcGrpProfileSwitchType": sonusIsupsgSvcGrpProfileSwitchType,
       "sonusIsupsgSvcGrpProfileRevision": sonusIsupsgSvcGrpProfileRevision,
       "sonusIsupsgSvcGrpProfileHuntAlgorithm": sonusIsupsgSvcGrpProfileHuntAlgorithm,
       "sonusIsupsgSvcGrpProfileCost": sonusIsupsgSvcGrpProfileCost,
       "sonusIsupsgSvcGrpProfileCicControl": sonusIsupsgSvcGrpProfileCicControl,
       "sonusIsupsgSvcGrpProfileContTestFreq": sonusIsupsgSvcGrpProfileContTestFreq,
       "sonusIsupsgSvcGrpProfileAdminState": sonusIsupsgSvcGrpProfileAdminState,
       "sonusIsupsgSvcGrpProfileRowStatus": sonusIsupsgSvcGrpProfileRowStatus,
       "sonusIsupsgSvcGrpProfileHopCounterState": sonusIsupsgSvcGrpProfileHopCounterState,
       "sonusIsupsgSvcGrpProfileHopCounterValue": sonusIsupsgSvcGrpProfileHopCounterValue,
       "sonusIsupsgSvcGrpProfileDiscTreatmentProfileName": sonusIsupsgSvcGrpProfileDiscTreatmentProfileName,
       "sonusIsupsgSvcGrpProfileTonePackageName": sonusIsupsgSvcGrpProfileTonePackageName,
       "sonusIsupsgSvcGrpProfileGrsStartup": sonusIsupsgSvcGrpProfileGrsStartup,
       "sonusIsupsgSvcGrpProfileOlipCheck": sonusIsupsgSvcGrpProfileOlipCheck,
       "sonusIsupsgSvcGrpProfileExchangeType": sonusIsupsgSvcGrpProfileExchangeType,
       "sonusIsupsgSvcGrpProfileInspectionTime": sonusIsupsgSvcGrpProfileInspectionTime,
       "sonusIsupsgSvcGrpProfileInspectionFreq": sonusIsupsgSvcGrpProfileInspectionFreq,
       "sonusIsupsgSvcGrpProfileInspectionState": sonusIsupsgSvcGrpProfileInspectionState,
       "sonusIsupsgSvcGrpProfileSignalingProfileName": sonusIsupsgSvcGrpProfileSignalingProfileName,
       "sonusIsupsgSvcGrpProfileAccRespProcess": sonusIsupsgSvcGrpProfileAccRespProcess,
       "sonusIsupsgSvcGrpProfileAccL1ARCancelpercentage": sonusIsupsgSvcGrpProfileAccL1ARCancelpercentage,
       "sonusIsupsgSvcGrpProfileAccL1DRCancelpercentage": sonusIsupsgSvcGrpProfileAccL1DRCancelpercentage,
       "sonusIsupsgSvcGrpProfileAccL2ARCancelpercentage": sonusIsupsgSvcGrpProfileAccL2ARCancelpercentage,
       "sonusIsupsgSvcGrpProfileAccL2DRCancelpercentage": sonusIsupsgSvcGrpProfileAccL2DRCancelpercentage,
       "sonusIsupsgSvcGrpProfileAccL3ARCancelpercentage": sonusIsupsgSvcGrpProfileAccL3ARCancelpercentage,
       "sonusIsupsgSvcGrpProfileAccL3DRCancelpercentage": sonusIsupsgSvcGrpProfileAccL3DRCancelpercentage,
       "sonusIsupsgSvcGrpProfileAccSendACL": sonusIsupsgSvcGrpProfileAccSendACL,
       "sonusIsupsgCircuitTable": sonusIsupsgCircuitTable,
       "sonusIsupsgCircuitEntry": sonusIsupsgCircuitEntry,
       "sonusIsupsgCircuitServiceListIndex": sonusIsupsgCircuitServiceListIndex,
       "sonusIsupsgCircuitIdentityCode": sonusIsupsgCircuitIdentityCode,
       "sonusIsupsgCircuitServiceName": sonusIsupsgCircuitServiceName,
       "sonusIsupsgCircuitPortName": sonusIsupsgCircuitPortName,
       "sonusIsupsgCircuitChannel": sonusIsupsgCircuitChannel,
       "sonusIsupsgCircuitDirection": sonusIsupsgCircuitDirection,
       "sonusIsupsgCircuitMode": sonusIsupsgCircuitMode,
       "sonusIsupsgCircuitAction": sonusIsupsgCircuitAction,
       "sonusIsupsgCircuitTimeout": sonusIsupsgCircuitTimeout,
       "sonusIsupsgCircuitAdminState": sonusIsupsgCircuitAdminState,
       "sonusIsupsgCircuitProfileName": sonusIsupsgCircuitProfileName,
       "sonusIsupsgCircuitRowStatus": sonusIsupsgCircuitRowStatus,
       "sonusIsupsgCircuitStatTable": sonusIsupsgCircuitStatTable,
       "sonusIsupsgCircuitStatEntry": sonusIsupsgCircuitStatEntry,
       "sonusIsupsgCircuitStatServiceListIndex": sonusIsupsgCircuitStatServiceListIndex,
       "sonusIsupsgCircuitStatIdentityCode": sonusIsupsgCircuitStatIdentityCode,
       "sonusIsupsgCircuitStatUsage": sonusIsupsgCircuitStatUsage,
       "sonusIsupsgCircuitStatLocalMaint": sonusIsupsgCircuitStatLocalMaint,
       "sonusIsupsgCircuitStatLocalHw": sonusIsupsgCircuitStatLocalHw,
       "sonusIsupsgCircuitStatRemoteMaint": sonusIsupsgCircuitStatRemoteMaint,
       "sonusIsupsgCircuitStatRemoteHw": sonusIsupsgCircuitStatRemoteHw,
       "sonusIsupsgCircuitStatManualCot": sonusIsupsgCircuitStatManualCot,
       "sonusIsupsgFarEndCircuitAdminTable": sonusIsupsgFarEndCircuitAdminTable,
       "sonusIsupsgFarEndCircuitAdminEntry": sonusIsupsgFarEndCircuitAdminEntry,
       "sonusIsupsgFarEndCircuitServiceListIndex": sonusIsupsgFarEndCircuitServiceListIndex,
       "sonusIsupsgFarEndCircuitIdentityCode": sonusIsupsgFarEndCircuitIdentityCode,
       "sonusIsupsgFarEndCircuitValidationTestResult": sonusIsupsgFarEndCircuitValidationTestResult,
       "sonusIsupsgFarEndCircuitGroupCarrier": sonusIsupsgFarEndCircuitGroupCarrier,
       "sonusIsupsgFarEndCircuitCicControl": sonusIsupsgFarEndCircuitCicControl,
       "sonusIsupsgFarEndCircuitAlarmCarrier": sonusIsupsgFarEndCircuitAlarmCarrier,
       "sonusIsupsgFarEndCircuitContinuityRequirement": sonusIsupsgFarEndCircuitContinuityRequirement,
       "sonusIsupsgFarEndCircuitIdentificationTrunkNumber": sonusIsupsgFarEndCircuitIdentificationTrunkNumber,
       "sonusIsupsgFarEndCircuitIdentificationOfficeA": sonusIsupsgFarEndCircuitIdentificationOfficeA,
       "sonusIsupsgFarEndCircuitIdentificationOfficeZ": sonusIsupsgFarEndCircuitIdentificationOfficeZ,
       "sonusIsupsgFarEndCircuitLocationIdentification": sonusIsupsgFarEndCircuitLocationIdentification,
       "sonusIsupsgFarEndCircuitCicControlConflict": sonusIsupsgFarEndCircuitCicControlConflict,
       "sonusIsupsgFarEndCircuitStatTable": sonusIsupsgFarEndCircuitStatTable,
       "sonusIsupsgFarEndCircuitStatEntry": sonusIsupsgFarEndCircuitStatEntry,
       "sonusIsupsgFarEndCircuitStatServiceListIndex": sonusIsupsgFarEndCircuitStatServiceListIndex,
       "sonusIsupsgFarEndCircuitStatIdentityCode": sonusIsupsgFarEndCircuitStatIdentityCode,
       "sonusIsupsgFarEndCircuitStatStatus": sonusIsupsgFarEndCircuitStatStatus,
       "sonusIsupsgFarEndCircuitStatLocalMaint": sonusIsupsgFarEndCircuitStatLocalMaint,
       "sonusIsupsgSignalingProfile": sonusIsupsgSignalingProfile,
       "sonusIsupsgSignalingProfileNextIndex": sonusIsupsgSignalingProfileNextIndex,
       "sonusIsupsgSignalingProfileTable": sonusIsupsgSignalingProfileTable,
       "sonusIsupsgSignalingProfileEntry": sonusIsupsgSignalingProfileEntry,
       "sonusIsupsgSignalingProfileListIndex": sonusIsupsgSignalingProfileListIndex,
       "sonusIsupsgSignalingProfileName": sonusIsupsgSignalingProfileName,
       "sonusIsupsgSignalingProfileCompat": sonusIsupsgSignalingProfileCompat,
       "sonusIsupsgSignalingProfileAccessDel": sonusIsupsgSignalingProfileAccessDel,
       "sonusIsupsgSignalingProfileGenNum": sonusIsupsgSignalingProfileGenNum,
       "sonusIsupsgSignalingProfileGenNotif": sonusIsupsgSignalingProfileGenNotif,
       "sonusIsupsgSignalingProfileGenDigs": sonusIsupsgSignalingProfileGenDigs,
       "sonusIsupsgSignalingProfileLocNum": sonusIsupsgSignalingProfileLocNum,
       "sonusIsupsgSignalingProfileOrigIscPC": sonusIsupsgSignalingProfileOrigIscPC,
       "sonusIsupsgSignalingProfileUserTeleService": sonusIsupsgSignalingProfileUserTeleService,
       "sonusIsupsgSignalingProfileSegmentation": sonusIsupsgSignalingProfileSegmentation,
       "sonusIsupsgSignalingProfileFallback": sonusIsupsgSignalingProfileFallback,
       "sonusIsupsgSignalingProfilePropDelay": sonusIsupsgSignalingProfilePropDelay,
       "sonusIsupsgSignalingProfileEMcid": sonusIsupsgSignalingProfileEMcid,
       "sonusIsupsgSignalingProfileHopCounter": sonusIsupsgSignalingProfileHopCounter,
       "sonusIsupsgSignalingProfileSubPriorityCls": sonusIsupsgSignalingProfileSubPriorityCls,
       "sonusIsupsgSignalingProfileAPM": sonusIsupsgSignalingProfileAPM,
       "sonusIsupsgSignalingProfileConNumInAcm": sonusIsupsgSignalingProfileConNumInAcm,
       "sonusIsupsgSignalingProfileCauseInCpg": sonusIsupsgSignalingProfileCauseInCpg,
       "sonusIsupsgSignalingProfileMultiCarrierEnv": sonusIsupsgSignalingProfileMultiCarrierEnv,
       "sonusIsupsgSignalingProfileCarrierSelection": sonusIsupsgSignalingProfileCarrierSelection,
       "sonusIsupsgSignalingProfileInrInf": sonusIsupsgSignalingProfileInrInf,
       "sonusIsupsgSignalingProfileCqmCqr": sonusIsupsgSignalingProfileCqmCqr,
       "sonusIsupsgSignalingProfileCallRef": sonusIsupsgSignalingProfileCallRef,
       "sonusIsupsgSignalingProfileCfn": sonusIsupsgSignalingProfileCfn,
       "sonusIsupsgSignalingProfileFacility": sonusIsupsgSignalingProfileFacility,
       "sonusIsupsgSignalingProfilePam": sonusIsupsgSignalingProfilePam,
       "sonusIsupsgSignalingProfileObciAnm": sonusIsupsgSignalingProfileObciAnm,
       "sonusIsupsgSignalingProfileDrs": sonusIsupsgSignalingProfileDrs,
       "sonusIsupsgSignalingProfileRedNum": sonusIsupsgSignalingProfileRedNum,
       "sonusIsupsgSignalingProfileLpa": sonusIsupsgSignalingProfileLpa,
       "sonusIsupsgSignalingProfileUcic": sonusIsupsgSignalingProfileUcic,
       "sonusIsupsgSignalingProfileOlm": sonusIsupsgSignalingProfileOlm,
       "sonusIsupsgSignalingProfileBBRel": sonusIsupsgSignalingProfileBBRel,
       "sonusIsupsgSignalingProfileUsr": sonusIsupsgSignalingProfileUsr,
       "sonusIsupsgSignalingProfileBBIam": sonusIsupsgSignalingProfileBBIam,
       "sonusIsupsgSignalingProfileCallModMsgs": sonusIsupsgSignalingProfileCallModMsgs,
       "sonusIsupsgSignalingProfileCallDiv": sonusIsupsgSignalingProfileCallDiv,
       "sonusIsupsgSignalingProfileCallHist": sonusIsupsgSignalingProfileCallHist,
       "sonusIsupsgSignalingProfileGenRef": sonusIsupsgSignalingProfileGenRef,
       "sonusIsupsgSignalingProfileMLPP": sonusIsupsgSignalingProfileMLPP,
       "sonusIsupsgSignalingProfileNSF": sonusIsupsgSignalingProfileNSF,
       "sonusIsupsgSignalingProfileRedNumRist": sonusIsupsgSignalingProfileRedNumRist,
       "sonusIsupsgSignalingProfileRemoteOp": sonusIsupsgSignalingProfileRemoteOp,
       "sonusIsupsgSignalingProfileServActv": sonusIsupsgSignalingProfileServActv,
       "sonusIsupsgSignalingProfileSigPointCode": sonusIsupsgSignalingProfileSigPointCode,
       "sonusIsupsgSignalingProfileTmrPrime": sonusIsupsgSignalingProfileTmrPrime,
       "sonusIsupsgSignalingProfileTransMedUsed": sonusIsupsgSignalingProfileTransMedUsed,
       "sonusIsupsgSignalingProfileUsiPrime": sonusIsupsgSignalingProfileUsiPrime,
       "sonusIsupsgSignalingProfileRedNumInAcm": sonusIsupsgSignalingProfileRedNumInAcm,
       "sonusIsupsgSignalingProfileRedNumInAnm": sonusIsupsgSignalingProfileRedNumInAnm,
       "sonusIsupsgSignalingProfileUuiInRel": sonusIsupsgSignalingProfileUuiInRel,
       "sonusIsupsgSignalingProfileConReqInFaa": sonusIsupsgSignalingProfileConReqInFaa,
       "sonusIsupsgSignalingProfileConReqInFar": sonusIsupsgSignalingProfileConReqInFar,
       "sonusIsupsgSignalingProfileFac": sonusIsupsgSignalingProfileFac,
       "sonusIsupsgSignalingProfileEchoControl": sonusIsupsgSignalingProfileEchoControl,
       "sonusIsupsgSignalingProfileBackwardGVNS": sonusIsupsgSignalingProfileBackwardGVNS,
       "sonusIsupsgSignalingProfileCircAssMap": sonusIsupsgSignalingProfileCircAssMap,
       "sonusIsupsgSignalingProfileCCSS": sonusIsupsgSignalingProfileCCSS,
       "sonusIsupsgSignalingProfileCallDivTreat": sonusIsupsgSignalingProfileCallDivTreat,
       "sonusIsupsgSignalingProfileCalledInNum": sonusIsupsgSignalingProfileCalledInNum,
       "sonusIsupsgSignalingProfileCollectCallReq": sonusIsupsgSignalingProfileCollectCallReq,
       "sonusIsupsgSignalingProfileConfTreat": sonusIsupsgSignalingProfileConfTreat,
       "sonusIsupsgSignalingProfileCorrelationId": sonusIsupsgSignalingProfileCorrelationId,
       "sonusIsupsgSignalingProfileCallOfrTreat": sonusIsupsgSignalingProfileCallOfrTreat,
       "sonusIsupsgSignalingProfileCallTransNum": sonusIsupsgSignalingProfileCallTransNum,
       "sonusIsupsgSignalingProfileCallTransRef": sonusIsupsgSignalingProfileCallTransRef,
       "sonusIsupsgSignalingProfileDispInfo": sonusIsupsgSignalingProfileDispInfo,
       "sonusIsupsgSignalingProfileForwardGVNS": sonusIsupsgSignalingProfileForwardGVNS,
       "sonusIsupsgSignalingProfileLoopPrevention": sonusIsupsgSignalingProfileLoopPrevention,
       "sonusIsupsgSignalingProfileNetworkMgmt": sonusIsupsgSignalingProfileNetworkMgmt,
       "sonusIsupsgSignalingProfileSCFId": sonusIsupsgSignalingProfileSCFId,
       "sonusIsupsgSignalingProfileUIDActionInd": sonusIsupsgSignalingProfileUIDActionInd,
       "sonusIsupsgSignalingProfileUIDCapInd": sonusIsupsgSignalingProfileUIDCapInd,
       "sonusIsupsgSignalingProfileConNumInCpg": sonusIsupsgSignalingProfileConNumInCpg,
       "sonusIsupsgSignalingProfileGenNumInCpg": sonusIsupsgSignalingProfileGenNumInCpg,
       "sonusIsupsgSignalingProfileEchoCntrlInIam": sonusIsupsgSignalingProfileEchoCntrlInIam,
       "sonusIsupsgSignalingProfileRemoteOpInRel": sonusIsupsgSignalingProfileRemoteOpInRel,
       "sonusIsupsgSignalingProfileAccessTransInFac": sonusIsupsgSignalingProfileAccessTransInFac,
       "sonusIsupsgSignalingProfileGenNotifInFac": sonusIsupsgSignalingProfileGenNotifInFac,
       "sonusIsupsgSignalingProfileUuindAnm": sonusIsupsgSignalingProfileUuindAnm,
       "sonusIsupsgSignalingProfileUuindCpg": sonusIsupsgSignalingProfileUuindCpg,
       "sonusIsupsgSignalingProfileNrmSupport": sonusIsupsgSignalingProfileNrmSupport,
       "sonusIsupsgSignalingProfileCseInRlc": sonusIsupsgSignalingProfileCseInRlc,
       "sonusIsupsgSignalingProfileUpaUpt": sonusIsupsgSignalingProfileUpaUpt,
       "sonusIsupsgSignalingProfileRecInCai": sonusIsupsgSignalingProfileRecInCai,
       "sonusIsupsgSignalingProfileTransitUnrec": sonusIsupsgSignalingProfileTransitUnrec,
       "sonusIsupsgSignalingProfileCcRaw": sonusIsupsgSignalingProfileCcRaw,
       "sonusIsupsgSignalingProfileCctGrpBlockFlag": sonusIsupsgSignalingProfileCctGrpBlockFlag,
       "sonusIsupsgSignalingProfileCctGrpResetFlag": sonusIsupsgSignalingProfileCctGrpResetFlag,
       "sonusIsupsgSignalingProfileBaseProfileName": sonusIsupsgSignalingProfileBaseProfileName,
       "sonusIsupsgSignalingProfileAdminState": sonusIsupsgSignalingProfileAdminState,
       "sonusIsupsgSignalingProfileRowStatus": sonusIsupsgSignalingProfileRowStatus,
       "sonusIsupsgSignalingProfilePropDelayValue": sonusIsupsgSignalingProfilePropDelayValue,
       "sonusIsupsgSignalingProfileU2USrvcLevel": sonusIsupsgSignalingProfileU2USrvcLevel,
       "sonusIsupsgSignalingProfileSAM": sonusIsupsgSignalingProfileSAM,
       "sonusIsupsgSignalingProfileFOT": sonusIsupsgSignalingProfileFOT,
       "sonusIsupsgSignalingProfileSpecialDigits": sonusIsupsgSignalingProfileSpecialDigits,
       "sonusIsupsgSignalingProfileTNS": sonusIsupsgSignalingProfileTNS,
       "sonusIsupsgSignalingProfileAwaitDigits": sonusIsupsgSignalingProfileAwaitDigits,
       "sonusIsupsgSignalingProfileAccessTrans": sonusIsupsgSignalingProfileAccessTrans,
       "sonusIsupsgSignalingProfileJurisdiction": sonusIsupsgSignalingProfileJurisdiction,
       "sonusIsupsgSignalingProfileOCN": sonusIsupsgSignalingProfileOCN,
       "sonusIsupsgSignalingProfileBusinessGrp": sonusIsupsgSignalingProfileBusinessGrp,
       "sonusIsupsgSignalingProfileConReq": sonusIsupsgSignalingProfileConReq,
       "sonusIsupsgSignalingProfileInfoInd": sonusIsupsgSignalingProfileInfoInd,
       "sonusIsupsgSignalingProfileNtp": sonusIsupsgSignalingProfileNtp,
       "sonusIsupsgSignalingProfileNotifInd": sonusIsupsgSignalingProfileNotifInd,
       "sonusIsupsgSignalingProfileRedInfoAcm": sonusIsupsgSignalingProfileRedInfoAcm,
       "sonusIsupsgSignalingProfileEgressService": sonusIsupsgSignalingProfileEgressService,
       "sonusIsupsgSignalingProfileServCodeInd": sonusIsupsgSignalingProfileServCodeInd,
       "sonusIsupsgSignalingProfileSpecProcReq": sonusIsupsgSignalingProfileSpecProcReq,
       "sonusIsupsgSignalingProfileTransReq": sonusIsupsgSignalingProfileTransReq,
       "sonusIsupsgSignalingProfileChgNum": sonusIsupsgSignalingProfileChgNum,
       "sonusIsupsgSignalingProfileGenAddressREL": sonusIsupsgSignalingProfileGenAddressREL,
       "sonusIsupsgSignalingProfileUUIndAcm": sonusIsupsgSignalingProfileUUIndAcm,
       "sonusIsupsgSignalingProfileUUInfo": sonusIsupsgSignalingProfileUUInfo,
       "sonusIsupsgSignalingProfileOperatorServInfo": sonusIsupsgSignalingProfileOperatorServInfo,
       "sonusIsupsgSignalingProfileCvtCvr": sonusIsupsgSignalingProfileCvtCvr,
       "sonusIsupsgSignalingProfileGenName": sonusIsupsgSignalingProfileGenName,
       "sonusIsupsgSignalingProfileRedCap": sonusIsupsgSignalingProfileRedCap,
       "sonusIsupsgSignalingProfileRedCount": sonusIsupsgSignalingProfileRedCount,
       "sonusIsupsgSignalingProfileSendTwoGrpMsgs": sonusIsupsgSignalingProfileSendTwoGrpMsgs,
       "sonusIsupsgSignalingProfileAwaitTwoGrpMsgs": sonusIsupsgSignalingProfileAwaitTwoGrpMsgs,
       "sonusIsupsgSignalingProfileCqmOnCardSwap": sonusIsupsgSignalingProfileCqmOnCardSwap,
       "sonusIsupsgSignalingProfileAnsi95Grs": sonusIsupsgSignalingProfileAnsi95Grs,
       "sonusIsupsgSignalingProfileCpgBeforeAcm": sonusIsupsgSignalingProfileCpgBeforeAcm,
       "sonusIsupServiceGroupMIBNotifications": sonusIsupServiceGroupMIBNotifications,
       "sonusIsupServiceGroupMIBNotificationsPrefix": sonusIsupServiceGroupMIBNotificationsPrefix,
       "sonusIsupSvcGrpInServiceNotification": sonusIsupSvcGrpInServiceNotification,
       "sonusIsupSvcGrpOutOfServiceNotification": sonusIsupSvcGrpOutOfServiceNotification,
       "sonusIsupCircuitBlockedNotification": sonusIsupCircuitBlockedNotification,
       "sonusIsupCircuitUnblockedNotification": sonusIsupCircuitUnblockedNotification,
       "sonusIsupCircuitResetNotification": sonusIsupCircuitResetNotification,
       "sonusIsupContinuityRecheckFailureNotification": sonusIsupContinuityRecheckFailureNotification,
       "sonusIsupCicRegistrationFailedNotification": sonusIsupCicRegistrationFailedNotification,
       "sonusIsupHopCounterExhaustedNotification": sonusIsupHopCounterExhaustedNotification,
       "sonusIsupRelWithExchangeRoutingErrorNotification": sonusIsupRelWithExchangeRoutingErrorNotification,
       "sonusIsupCqmTimeoutNotification": sonusIsupCqmTimeoutNotification,
       "sonusIsupCvtTimeoutNotification": sonusIsupCvtTimeoutNotification,
       "sonusIsupFarendCircuitStateMismatchedNotification": sonusIsupFarendCircuitStateMismatchedNotification,
       "sonusIsupCircuitTimerExpired": sonusIsupCircuitTimerExpired,
       "sonusIsupServiceGroupMIBNotificationsObjects": sonusIsupServiceGroupMIBNotificationsObjects,
       "sonusIsupSvcGrpName": sonusIsupSvcGrpName,
       "sonusIsupMaintReason": sonusIsupMaintReason,
       "sonusIsupTrunkGrpName": sonusIsupTrunkGrpName,
       "sonusIsupCircuit": sonusIsupCircuit,
       "sonusIsupCircuitOffsets": sonusIsupCircuitOffsets,
       "sonusIsupCalledPartyNumber": sonusIsupCalledPartyNumber,
       "sonusIsupCallingPartyNumber": sonusIsupCallingPartyNumber,
       "sonusIsupMaintCode": sonusIsupMaintCode}
)
