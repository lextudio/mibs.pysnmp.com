# SNMP MIB module (SONUS-CAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-CAS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:52 2024
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

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
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

(SonusAdminAction,
 SonusAdminState,
 SonusName,
 SonusNameReference,
 SonusServiceState) = mibBuilder.importSymbols(
    "SONUS-TC",
    "SonusAdminAction",
    "SonusAdminState",
    "SonusName",
    "SonusNameReference",
    "SonusServiceState")


# MODULE-IDENTITY

sonusCasMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusCasMIBObjects_ObjectIdentity = ObjectIdentity
sonusCasMIBObjects = _SonusCasMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1)
)
_SonusCasServiceGroup_ObjectIdentity = ObjectIdentity
sonusCasServiceGroup = _SonusCasServiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1)
)
_SonusCasServiceGroupNextIndex_Type = Integer32
_SonusCasServiceGroupNextIndex_Object = MibScalar
sonusCasServiceGroupNextIndex = _SonusCasServiceGroupNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 1),
    _SonusCasServiceGroupNextIndex_Type()
)
sonusCasServiceGroupNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCasServiceGroupNextIndex.setStatus("current")
_SonusCasServiceGroupAdmnTable_Object = MibTable
sonusCasServiceGroupAdmnTable = _SonusCasServiceGroupAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sonusCasServiceGroupAdmnTable.setStatus("current")
_SonusCasServiceGroupAdmnEntry_Object = MibTableRow
sonusCasServiceGroupAdmnEntry = _SonusCasServiceGroupAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1)
)
sonusCasServiceGroupAdmnEntry.setIndexNames(
    (0, "SONUS-CAS-MIB", "sonusCassgServiceGroupIndex"),
)
if mibBuilder.loadTexts:
    sonusCasServiceGroupAdmnEntry.setStatus("current")


class _SonusCassgServiceGroupIndex_Type(Integer32):
    """Custom type sonusCassgServiceGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SonusCassgServiceGroupIndex_Type.__name__ = "Integer32"
_SonusCassgServiceGroupIndex_Object = MibTableColumn
sonusCassgServiceGroupIndex = _SonusCassgServiceGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 1),
    _SonusCassgServiceGroupIndex_Type()
)
sonusCassgServiceGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupIndex.setStatus("current")
_SonusCassgServiceGroupName_Type = SonusName
_SonusCassgServiceGroupName_Object = MibTableColumn
sonusCassgServiceGroupName = _SonusCassgServiceGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 2),
    _SonusCassgServiceGroupName_Type()
)
sonusCassgServiceGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupName.setStatus("current")
_SonusCassgServiceGroupProfileName_Type = SonusNameReference
_SonusCassgServiceGroupProfileName_Object = MibTableColumn
sonusCassgServiceGroupProfileName = _SonusCassgServiceGroupProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 3),
    _SonusCassgServiceGroupProfileName_Type()
)
sonusCassgServiceGroupProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupProfileName.setStatus("current")
_SonusCassgServiceGroupTG_Type = SonusNameReference
_SonusCassgServiceGroupTG_Object = MibTableColumn
sonusCassgServiceGroupTG = _SonusCassgServiceGroupTG_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 4),
    _SonusCassgServiceGroupTG_Type()
)
sonusCassgServiceGroupTG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupTG.setStatus("current")


class _SonusCassgServiceGroupHuntAlgorithm_Type(Integer32):
    """Custom type sonusCassgServiceGroupHuntAlgorithm based on Integer32"""
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
        *(("bottom2Top", 1),
          ("circularBottom2Top", 3),
          ("circularTop2Bottom", 4),
          ("top2Bottom", 2))
    )


_SonusCassgServiceGroupHuntAlgorithm_Type.__name__ = "Integer32"
_SonusCassgServiceGroupHuntAlgorithm_Object = MibTableColumn
sonusCassgServiceGroupHuntAlgorithm = _SonusCassgServiceGroupHuntAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 5),
    _SonusCassgServiceGroupHuntAlgorithm_Type()
)
sonusCassgServiceGroupHuntAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupHuntAlgorithm.setStatus("current")


class _SonusCassgServiceGroupCost_Type(Integer32):
    """Custom type sonusCassgServiceGroupCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SonusCassgServiceGroupCost_Type.__name__ = "Integer32"
_SonusCassgServiceGroupCost_Object = MibTableColumn
sonusCassgServiceGroupCost = _SonusCassgServiceGroupCost_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 6),
    _SonusCassgServiceGroupCost_Type()
)
sonusCassgServiceGroupCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupCost.setStatus("current")


class _SonusCassgServiceGroupSignalType_Type(Integer32):
    """Custom type sonusCassgServiceGroupSignalType based on Integer32"""
    defaultValue = 1

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
        *(("e1Mfr2", 6),
          ("eM", 1),
          ("gsFxo", 2),
          ("gsFxs", 3),
          ("lsFxo", 4),
          ("lsFxs", 5))
    )


_SonusCassgServiceGroupSignalType_Type.__name__ = "Integer32"
_SonusCassgServiceGroupSignalType_Object = MibTableColumn
sonusCassgServiceGroupSignalType = _SonusCassgServiceGroupSignalType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 7),
    _SonusCassgServiceGroupSignalType_Type()
)
sonusCassgServiceGroupSignalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupSignalType.setStatus("current")
_SonusCassgServiceGroupIngressSSP_Type = SonusNameReference
_SonusCassgServiceGroupIngressSSP_Object = MibTableColumn
sonusCassgServiceGroupIngressSSP = _SonusCassgServiceGroupIngressSSP_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 8),
    _SonusCassgServiceGroupIngressSSP_Type()
)
sonusCassgServiceGroupIngressSSP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupIngressSSP.setStatus("current")
_SonusCassgServiceGroupEgressSSP_Type = SonusNameReference
_SonusCassgServiceGroupEgressSSP_Object = MibTableColumn
sonusCassgServiceGroupEgressSSP = _SonusCassgServiceGroupEgressSSP_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 9),
    _SonusCassgServiceGroupEgressSSP_Type()
)
sonusCassgServiceGroupEgressSSP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupEgressSSP.setStatus("current")
_SonusCassgServiceGroupHookflashSSP_Type = SonusNameReference
_SonusCassgServiceGroupHookflashSSP_Object = MibTableColumn
sonusCassgServiceGroupHookflashSSP = _SonusCassgServiceGroupHookflashSSP_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 10),
    _SonusCassgServiceGroupHookflashSSP_Type()
)
sonusCassgServiceGroupHookflashSSP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupHookflashSSP.setStatus("current")
_SonusCassgServiceGroupPscSSP_Type = SonusNameReference
_SonusCassgServiceGroupPscSSP_Object = MibTableColumn
sonusCassgServiceGroupPscSSP = _SonusCassgServiceGroupPscSSP_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 11),
    _SonusCassgServiceGroupPscSSP_Type()
)
sonusCassgServiceGroupPscSSP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupPscSSP.setStatus("current")


class _SonusCassgServiceGroupMaintBusy_Type(SonusAdminState):
    """Custom type sonusCassgServiceGroupMaintBusy based on SonusAdminState"""


_SonusCassgServiceGroupMaintBusy_Object = MibTableColumn
sonusCassgServiceGroupMaintBusy = _SonusCassgServiceGroupMaintBusy_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 12),
    _SonusCassgServiceGroupMaintBusy_Type()
)
sonusCassgServiceGroupMaintBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupMaintBusy.setStatus("current")


class _SonusCassgServiceGroupAutoBusyThreshold_Type(Integer32):
    """Custom type sonusCassgServiceGroupAutoBusyThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SonusCassgServiceGroupAutoBusyThreshold_Type.__name__ = "Integer32"
_SonusCassgServiceGroupAutoBusyThreshold_Object = MibTableColumn
sonusCassgServiceGroupAutoBusyThreshold = _SonusCassgServiceGroupAutoBusyThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 13),
    _SonusCassgServiceGroupAutoBusyThreshold_Type()
)
sonusCassgServiceGroupAutoBusyThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupAutoBusyThreshold.setStatus("current")


class _SonusCassgServiceGroupRequiresCPTone_Type(SonusAdminState):
    """Custom type sonusCassgServiceGroupRequiresCPTone based on SonusAdminState"""


_SonusCassgServiceGroupRequiresCPTone_Object = MibTableColumn
sonusCassgServiceGroupRequiresCPTone = _SonusCassgServiceGroupRequiresCPTone_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 14),
    _SonusCassgServiceGroupRequiresCPTone_Type()
)
sonusCassgServiceGroupRequiresCPTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupRequiresCPTone.setStatus("current")


class _SonusCassgServiceGroupProvidesCPTone_Type(SonusAdminState):
    """Custom type sonusCassgServiceGroupProvidesCPTone based on SonusAdminState"""


_SonusCassgServiceGroupProvidesCPTone_Object = MibTableColumn
sonusCassgServiceGroupProvidesCPTone = _SonusCassgServiceGroupProvidesCPTone_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 15),
    _SonusCassgServiceGroupProvidesCPTone_Type()
)
sonusCassgServiceGroupProvidesCPTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupProvidesCPTone.setStatus("current")
_SonusCassgServiceGroupDTMFProfileName_Type = SonusNameReference
_SonusCassgServiceGroupDTMFProfileName_Object = MibTableColumn
sonusCassgServiceGroupDTMFProfileName = _SonusCassgServiceGroupDTMFProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 16),
    _SonusCassgServiceGroupDTMFProfileName_Type()
)
sonusCassgServiceGroupDTMFProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupDTMFProfileName.setStatus("current")
_SonusCassgServiceGroupMFProfileName_Type = SonusNameReference
_SonusCassgServiceGroupMFProfileName_Object = MibTableColumn
sonusCassgServiceGroupMFProfileName = _SonusCassgServiceGroupMFProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 17),
    _SonusCassgServiceGroupMFProfileName_Type()
)
sonusCassgServiceGroupMFProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupMFProfileName.setStatus("current")
_SonusCassgServiceGroupCPTonePkgName_Type = SonusNameReference
_SonusCassgServiceGroupCPTonePkgName_Object = MibTableColumn
sonusCassgServiceGroupCPTonePkgName = _SonusCassgServiceGroupCPTonePkgName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 18),
    _SonusCassgServiceGroupCPTonePkgName_Type()
)
sonusCassgServiceGroupCPTonePkgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupCPTonePkgName.setStatus("current")


class _SonusCassgServiceGroupMinRxWinkTime_Type(Integer32):
    """Custom type sonusCassgServiceGroupMinRxWinkTime based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 800),
    )


_SonusCassgServiceGroupMinRxWinkTime_Type.__name__ = "Integer32"
_SonusCassgServiceGroupMinRxWinkTime_Object = MibTableColumn
sonusCassgServiceGroupMinRxWinkTime = _SonusCassgServiceGroupMinRxWinkTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 19),
    _SonusCassgServiceGroupMinRxWinkTime_Type()
)
sonusCassgServiceGroupMinRxWinkTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupMinRxWinkTime.setStatus("current")


class _SonusCassgServiceGroupMaxRxWinkTime_Type(Integer32):
    """Custom type sonusCassgServiceGroupMaxRxWinkTime based on Integer32"""
    defaultValue = 700

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 800),
    )


_SonusCassgServiceGroupMaxRxWinkTime_Type.__name__ = "Integer32"
_SonusCassgServiceGroupMaxRxWinkTime_Object = MibTableColumn
sonusCassgServiceGroupMaxRxWinkTime = _SonusCassgServiceGroupMaxRxWinkTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 20),
    _SonusCassgServiceGroupMaxRxWinkTime_Type()
)
sonusCassgServiceGroupMaxRxWinkTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupMaxRxWinkTime.setStatus("current")


class _SonusCassgServiceGroupMinRxFlashTime_Type(Integer32):
    """Custom type sonusCassgServiceGroupMinRxFlashTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1100),
    )


_SonusCassgServiceGroupMinRxFlashTime_Type.__name__ = "Integer32"
_SonusCassgServiceGroupMinRxFlashTime_Object = MibTableColumn
sonusCassgServiceGroupMinRxFlashTime = _SonusCassgServiceGroupMinRxFlashTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 21),
    _SonusCassgServiceGroupMinRxFlashTime_Type()
)
sonusCassgServiceGroupMinRxFlashTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupMinRxFlashTime.setStatus("current")


class _SonusCassgServiceGroupMaxRxFlashTime_Type(Integer32):
    """Custom type sonusCassgServiceGroupMaxRxFlashTime based on Integer32"""
    defaultValue = 700

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1100),
    )


_SonusCassgServiceGroupMaxRxFlashTime_Type.__name__ = "Integer32"
_SonusCassgServiceGroupMaxRxFlashTime_Object = MibTableColumn
sonusCassgServiceGroupMaxRxFlashTime = _SonusCassgServiceGroupMaxRxFlashTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 22),
    _SonusCassgServiceGroupMaxRxFlashTime_Type()
)
sonusCassgServiceGroupMaxRxFlashTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupMaxRxFlashTime.setStatus("current")


class _SonusCassgServiceGroupTxWinkTime_Type(Integer32):
    """Custom type sonusCassgServiceGroupTxWinkTime based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 800),
    )


_SonusCassgServiceGroupTxWinkTime_Type.__name__ = "Integer32"
_SonusCassgServiceGroupTxWinkTime_Object = MibTableColumn
sonusCassgServiceGroupTxWinkTime = _SonusCassgServiceGroupTxWinkTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 23),
    _SonusCassgServiceGroupTxWinkTime_Type()
)
sonusCassgServiceGroupTxWinkTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupTxWinkTime.setStatus("current")


class _SonusCassgServiceGroupTxFlashTime_Type(Integer32):
    """Custom type sonusCassgServiceGroupTxFlashTime based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1100),
    )


_SonusCassgServiceGroupTxFlashTime_Type.__name__ = "Integer32"
_SonusCassgServiceGroupTxFlashTime_Object = MibTableColumn
sonusCassgServiceGroupTxFlashTime = _SonusCassgServiceGroupTxFlashTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 24),
    _SonusCassgServiceGroupTxFlashTime_Type()
)
sonusCassgServiceGroupTxFlashTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupTxFlashTime.setStatus("current")


class _SonusCassgServiceGroupGuardTime_Type(Integer32):
    """Custom type sonusCassgServiceGroupGuardTime based on Integer32"""
    defaultValue = 700

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1500),
    )


_SonusCassgServiceGroupGuardTime_Type.__name__ = "Integer32"
_SonusCassgServiceGroupGuardTime_Object = MibTableColumn
sonusCassgServiceGroupGuardTime = _SonusCassgServiceGroupGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 25),
    _SonusCassgServiceGroupGuardTime_Type()
)
sonusCassgServiceGroupGuardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupGuardTime.setStatus("current")


class _SonusCassgServiceGroupOperation_Type(Integer32):
    """Custom type sonusCassgServiceGroupOperation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("resetStats", 2))
    )


_SonusCassgServiceGroupOperation_Type.__name__ = "Integer32"
_SonusCassgServiceGroupOperation_Object = MibTableColumn
sonusCassgServiceGroupOperation = _SonusCassgServiceGroupOperation_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 26),
    _SonusCassgServiceGroupOperation_Type()
)
sonusCassgServiceGroupOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupOperation.setStatus("current")


class _SonusCassgServiceGroupAdminState_Type(SonusAdminState):
    """Custom type sonusCassgServiceGroupAdminState based on SonusAdminState"""


_SonusCassgServiceGroupAdminState_Object = MibTableColumn
sonusCassgServiceGroupAdminState = _SonusCassgServiceGroupAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 27),
    _SonusCassgServiceGroupAdminState_Type()
)
sonusCassgServiceGroupAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupAdminState.setStatus("current")


class _SonusCassgServiceGroupMode_Type(SonusServiceState):
    """Custom type sonusCassgServiceGroupMode based on SonusServiceState"""


_SonusCassgServiceGroupMode_Object = MibTableColumn
sonusCassgServiceGroupMode = _SonusCassgServiceGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 28),
    _SonusCassgServiceGroupMode_Type()
)
sonusCassgServiceGroupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupMode.setStatus("current")


class _SonusCassgServiceGroupAction_Type(SonusAdminAction):
    """Custom type sonusCassgServiceGroupAction based on SonusAdminAction"""


_SonusCassgServiceGroupAction_Object = MibTableColumn
sonusCassgServiceGroupAction = _SonusCassgServiceGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 29),
    _SonusCassgServiceGroupAction_Type()
)
sonusCassgServiceGroupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupAction.setStatus("current")


class _SonusCassgServiceGroupTimeout_Type(Integer32):
    """Custom type sonusCassgServiceGroupTimeout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_SonusCassgServiceGroupTimeout_Type.__name__ = "Integer32"
_SonusCassgServiceGroupTimeout_Object = MibTableColumn
sonusCassgServiceGroupTimeout = _SonusCassgServiceGroupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 30),
    _SonusCassgServiceGroupTimeout_Type()
)
sonusCassgServiceGroupTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupTimeout.setStatus("current")
_SonusCassgServiceGroupAlertToneName_Type = SonusNameReference
_SonusCassgServiceGroupAlertToneName_Object = MibTableColumn
sonusCassgServiceGroupAlertToneName = _SonusCassgServiceGroupAlertToneName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 31),
    _SonusCassgServiceGroupAlertToneName_Type()
)
sonusCassgServiceGroupAlertToneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupAlertToneName.setStatus("current")
_SonusCassgServiceGroupRowStatus_Type = RowStatus
_SonusCassgServiceGroupRowStatus_Object = MibTableColumn
sonusCassgServiceGroupRowStatus = _SonusCassgServiceGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 32),
    _SonusCassgServiceGroupRowStatus_Type()
)
sonusCassgServiceGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupRowStatus.setStatus("current")
_SonusCassgServiceGroupDTProfileName_Type = SonusNameReference
_SonusCassgServiceGroupDTProfileName_Object = MibTableColumn
sonusCassgServiceGroupDTProfileName = _SonusCassgServiceGroupDTProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 1, 2, 1, 33),
    _SonusCassgServiceGroupDTProfileName_Type()
)
sonusCassgServiceGroupDTProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgServiceGroupDTProfileName.setStatus("current")
_SonusCasSvcGrpProfileAdmn_ObjectIdentity = ObjectIdentity
sonusCasSvcGrpProfileAdmn = _SonusCasSvcGrpProfileAdmn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2)
)
_SonusCasSvcGrpProfileNextIndex_Type = Integer32
_SonusCasSvcGrpProfileNextIndex_Object = MibScalar
sonusCasSvcGrpProfileNextIndex = _SonusCasSvcGrpProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 1),
    _SonusCasSvcGrpProfileNextIndex_Type()
)
sonusCasSvcGrpProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCasSvcGrpProfileNextIndex.setStatus("current")
_SonusCasSvcGrpProfileAdmnTable_Object = MibTable
sonusCasSvcGrpProfileAdmnTable = _SonusCasSvcGrpProfileAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2)
)
if mibBuilder.loadTexts:
    sonusCasSvcGrpProfileAdmnTable.setStatus("current")
_SonusCasSvcGrpProfileAdmnEntry_Object = MibTableRow
sonusCasSvcGrpProfileAdmnEntry = _SonusCasSvcGrpProfileAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1)
)
sonusCasSvcGrpProfileAdmnEntry.setIndexNames(
    (0, "SONUS-CAS-MIB", "sonusCassgSvcGrpProfileIndex"),
)
if mibBuilder.loadTexts:
    sonusCasSvcGrpProfileAdmnEntry.setStatus("current")


class _SonusCassgSvcGrpProfileIndex_Type(Integer32):
    """Custom type sonusCassgSvcGrpProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SonusCassgSvcGrpProfileIndex_Type.__name__ = "Integer32"
_SonusCassgSvcGrpProfileIndex_Object = MibTableColumn
sonusCassgSvcGrpProfileIndex = _SonusCassgSvcGrpProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1, 1),
    _SonusCassgSvcGrpProfileIndex_Type()
)
sonusCassgSvcGrpProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgSvcGrpProfileIndex.setStatus("current")
_SonusCassgSvcGrpProfileName_Type = SonusName
_SonusCassgSvcGrpProfileName_Object = MibTableColumn
sonusCassgSvcGrpProfileName = _SonusCassgSvcGrpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1, 2),
    _SonusCassgSvcGrpProfileName_Type()
)
sonusCassgSvcGrpProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSvcGrpProfileName.setStatus("current")
_SonusCassgSvcGrpProfileTG_Type = SonusNameReference
_SonusCassgSvcGrpProfileTG_Object = MibTableColumn
sonusCassgSvcGrpProfileTG = _SonusCassgSvcGrpProfileTG_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1, 3),
    _SonusCassgSvcGrpProfileTG_Type()
)
sonusCassgSvcGrpProfileTG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSvcGrpProfileTG.setStatus("current")


class _SonusCassgSvcGrpProfileHuntAlgorithm_Type(Integer32):
    """Custom type sonusCassgSvcGrpProfileHuntAlgorithm based on Integer32"""
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
        *(("bottom2Top", 1),
          ("circularBottom2Top", 3),
          ("circularTop2Bottom", 4),
          ("top2Bottom", 2))
    )


_SonusCassgSvcGrpProfileHuntAlgorithm_Type.__name__ = "Integer32"
_SonusCassgSvcGrpProfileHuntAlgorithm_Object = MibTableColumn
sonusCassgSvcGrpProfileHuntAlgorithm = _SonusCassgSvcGrpProfileHuntAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1, 4),
    _SonusCassgSvcGrpProfileHuntAlgorithm_Type()
)
sonusCassgSvcGrpProfileHuntAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSvcGrpProfileHuntAlgorithm.setStatus("current")


class _SonusCassgSvcGrpProfileCost_Type(Integer32):
    """Custom type sonusCassgSvcGrpProfileCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SonusCassgSvcGrpProfileCost_Type.__name__ = "Integer32"
_SonusCassgSvcGrpProfileCost_Object = MibTableColumn
sonusCassgSvcGrpProfileCost = _SonusCassgSvcGrpProfileCost_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1, 5),
    _SonusCassgSvcGrpProfileCost_Type()
)
sonusCassgSvcGrpProfileCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSvcGrpProfileCost.setStatus("current")


class _SonusCassgSvcGrpProfileSignalType_Type(Integer32):
    """Custom type sonusCassgSvcGrpProfileSignalType based on Integer32"""
    defaultValue = 1

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
        *(("e1Mfr2", 6),
          ("eM", 1),
          ("gsFxo", 2),
          ("gsFxs", 3),
          ("lsFxo", 4),
          ("lsFxs", 5))
    )


_SonusCassgSvcGrpProfileSignalType_Type.__name__ = "Integer32"
_SonusCassgSvcGrpProfileSignalType_Object = MibTableColumn
sonusCassgSvcGrpProfileSignalType = _SonusCassgSvcGrpProfileSignalType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1, 6),
    _SonusCassgSvcGrpProfileSignalType_Type()
)
sonusCassgSvcGrpProfileSignalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSvcGrpProfileSignalType.setStatus("current")
_SonusCassgSvcGrpProfileIngressSSP_Type = SonusNameReference
_SonusCassgSvcGrpProfileIngressSSP_Object = MibTableColumn
sonusCassgSvcGrpProfileIngressSSP = _SonusCassgSvcGrpProfileIngressSSP_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1, 7),
    _SonusCassgSvcGrpProfileIngressSSP_Type()
)
sonusCassgSvcGrpProfileIngressSSP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSvcGrpProfileIngressSSP.setStatus("current")
_SonusCassgSvcGrpProfileEgressSSP_Type = SonusNameReference
_SonusCassgSvcGrpProfileEgressSSP_Object = MibTableColumn
sonusCassgSvcGrpProfileEgressSSP = _SonusCassgSvcGrpProfileEgressSSP_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1, 8),
    _SonusCassgSvcGrpProfileEgressSSP_Type()
)
sonusCassgSvcGrpProfileEgressSSP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSvcGrpProfileEgressSSP.setStatus("current")
_SonusCassgSvcGrpProfileHookflashSSP_Type = SonusNameReference
_SonusCassgSvcGrpProfileHookflashSSP_Object = MibTableColumn
sonusCassgSvcGrpProfileHookflashSSP = _SonusCassgSvcGrpProfileHookflashSSP_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1, 9),
    _SonusCassgSvcGrpProfileHookflashSSP_Type()
)
sonusCassgSvcGrpProfileHookflashSSP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSvcGrpProfileHookflashSSP.setStatus("current")
_SonusCassgSvcGrpProfilePscSSP_Type = SonusNameReference
_SonusCassgSvcGrpProfilePscSSP_Object = MibTableColumn
sonusCassgSvcGrpProfilePscSSP = _SonusCassgSvcGrpProfilePscSSP_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1, 10),
    _SonusCassgSvcGrpProfilePscSSP_Type()
)
sonusCassgSvcGrpProfilePscSSP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSvcGrpProfilePscSSP.setStatus("current")


class _SonusCassgSvcGrpProfileMaintBusy_Type(SonusAdminState):
    """Custom type sonusCassgSvcGrpProfileMaintBusy based on SonusAdminState"""


_SonusCassgSvcGrpProfileMaintBusy_Object = MibTableColumn
sonusCassgSvcGrpProfileMaintBusy = _SonusCassgSvcGrpProfileMaintBusy_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1, 11),
    _SonusCassgSvcGrpProfileMaintBusy_Type()
)
sonusCassgSvcGrpProfileMaintBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSvcGrpProfileMaintBusy.setStatus("current")


class _SonusCassgSvcGrpProfileAutoBusyThreshold_Type(Integer32):
    """Custom type sonusCassgSvcGrpProfileAutoBusyThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SonusCassgSvcGrpProfileAutoBusyThreshold_Type.__name__ = "Integer32"
_SonusCassgSvcGrpProfileAutoBusyThreshold_Object = MibTableColumn
sonusCassgSvcGrpProfileAutoBusyThreshold = _SonusCassgSvcGrpProfileAutoBusyThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1, 12),
    _SonusCassgSvcGrpProfileAutoBusyThreshold_Type()
)
sonusCassgSvcGrpProfileAutoBusyThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSvcGrpProfileAutoBusyThreshold.setStatus("current")


class _SonusCassgSvcGrpProfileRequiresCPTone_Type(SonusAdminState):
    """Custom type sonusCassgSvcGrpProfileRequiresCPTone based on SonusAdminState"""


_SonusCassgSvcGrpProfileRequiresCPTone_Object = MibTableColumn
sonusCassgSvcGrpProfileRequiresCPTone = _SonusCassgSvcGrpProfileRequiresCPTone_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1, 13),
    _SonusCassgSvcGrpProfileRequiresCPTone_Type()
)
sonusCassgSvcGrpProfileRequiresCPTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSvcGrpProfileRequiresCPTone.setStatus("current")


class _SonusCassgSvcGrpProfileProvidesCPTone_Type(SonusAdminState):
    """Custom type sonusCassgSvcGrpProfileProvidesCPTone based on SonusAdminState"""


_SonusCassgSvcGrpProfileProvidesCPTone_Object = MibTableColumn
sonusCassgSvcGrpProfileProvidesCPTone = _SonusCassgSvcGrpProfileProvidesCPTone_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1, 14),
    _SonusCassgSvcGrpProfileProvidesCPTone_Type()
)
sonusCassgSvcGrpProfileProvidesCPTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSvcGrpProfileProvidesCPTone.setStatus("current")
_SonusCassgSvcGrpProfileDTMFProfileName_Type = SonusNameReference
_SonusCassgSvcGrpProfileDTMFProfileName_Object = MibTableColumn
sonusCassgSvcGrpProfileDTMFProfileName = _SonusCassgSvcGrpProfileDTMFProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1, 15),
    _SonusCassgSvcGrpProfileDTMFProfileName_Type()
)
sonusCassgSvcGrpProfileDTMFProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSvcGrpProfileDTMFProfileName.setStatus("current")
_SonusCassgSvcGrpProfileMFProfileName_Type = SonusNameReference
_SonusCassgSvcGrpProfileMFProfileName_Object = MibTableColumn
sonusCassgSvcGrpProfileMFProfileName = _SonusCassgSvcGrpProfileMFProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1, 16),
    _SonusCassgSvcGrpProfileMFProfileName_Type()
)
sonusCassgSvcGrpProfileMFProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSvcGrpProfileMFProfileName.setStatus("current")
_SonusCassgSvcGrpProfileCPTonePkgName_Type = SonusNameReference
_SonusCassgSvcGrpProfileCPTonePkgName_Object = MibTableColumn
sonusCassgSvcGrpProfileCPTonePkgName = _SonusCassgSvcGrpProfileCPTonePkgName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1, 17),
    _SonusCassgSvcGrpProfileCPTonePkgName_Type()
)
sonusCassgSvcGrpProfileCPTonePkgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSvcGrpProfileCPTonePkgName.setStatus("current")


class _SonusCassgSvcGrpProfileMinRxWinkTime_Type(Integer32):
    """Custom type sonusCassgSvcGrpProfileMinRxWinkTime based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 800),
    )


_SonusCassgSvcGrpProfileMinRxWinkTime_Type.__name__ = "Integer32"
_SonusCassgSvcGrpProfileMinRxWinkTime_Object = MibTableColumn
sonusCassgSvcGrpProfileMinRxWinkTime = _SonusCassgSvcGrpProfileMinRxWinkTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1, 18),
    _SonusCassgSvcGrpProfileMinRxWinkTime_Type()
)
sonusCassgSvcGrpProfileMinRxWinkTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSvcGrpProfileMinRxWinkTime.setStatus("current")


class _SonusCassgSvcGrpProfileMaxRxWinkTime_Type(Integer32):
    """Custom type sonusCassgSvcGrpProfileMaxRxWinkTime based on Integer32"""
    defaultValue = 700

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 800),
    )


_SonusCassgSvcGrpProfileMaxRxWinkTime_Type.__name__ = "Integer32"
_SonusCassgSvcGrpProfileMaxRxWinkTime_Object = MibTableColumn
sonusCassgSvcGrpProfileMaxRxWinkTime = _SonusCassgSvcGrpProfileMaxRxWinkTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1, 19),
    _SonusCassgSvcGrpProfileMaxRxWinkTime_Type()
)
sonusCassgSvcGrpProfileMaxRxWinkTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSvcGrpProfileMaxRxWinkTime.setStatus("current")


class _SonusCassgSvcGrpProfileMinRxFlashTime_Type(Integer32):
    """Custom type sonusCassgSvcGrpProfileMinRxFlashTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1100),
    )


_SonusCassgSvcGrpProfileMinRxFlashTime_Type.__name__ = "Integer32"
_SonusCassgSvcGrpProfileMinRxFlashTime_Object = MibTableColumn
sonusCassgSvcGrpProfileMinRxFlashTime = _SonusCassgSvcGrpProfileMinRxFlashTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1, 20),
    _SonusCassgSvcGrpProfileMinRxFlashTime_Type()
)
sonusCassgSvcGrpProfileMinRxFlashTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSvcGrpProfileMinRxFlashTime.setStatus("current")


class _SonusCassgSvcGrpProfileMaxRxFlashTime_Type(Integer32):
    """Custom type sonusCassgSvcGrpProfileMaxRxFlashTime based on Integer32"""
    defaultValue = 700

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1100),
    )


_SonusCassgSvcGrpProfileMaxRxFlashTime_Type.__name__ = "Integer32"
_SonusCassgSvcGrpProfileMaxRxFlashTime_Object = MibTableColumn
sonusCassgSvcGrpProfileMaxRxFlashTime = _SonusCassgSvcGrpProfileMaxRxFlashTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1, 21),
    _SonusCassgSvcGrpProfileMaxRxFlashTime_Type()
)
sonusCassgSvcGrpProfileMaxRxFlashTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSvcGrpProfileMaxRxFlashTime.setStatus("current")


class _SonusCassgSvcGrpProfileTxWinkTime_Type(Integer32):
    """Custom type sonusCassgSvcGrpProfileTxWinkTime based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 800),
    )


_SonusCassgSvcGrpProfileTxWinkTime_Type.__name__ = "Integer32"
_SonusCassgSvcGrpProfileTxWinkTime_Object = MibTableColumn
sonusCassgSvcGrpProfileTxWinkTime = _SonusCassgSvcGrpProfileTxWinkTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1, 22),
    _SonusCassgSvcGrpProfileTxWinkTime_Type()
)
sonusCassgSvcGrpProfileTxWinkTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSvcGrpProfileTxWinkTime.setStatus("current")


class _SonusCassgSvcGrpProfileTxFlashTime_Type(Integer32):
    """Custom type sonusCassgSvcGrpProfileTxFlashTime based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1100),
    )


_SonusCassgSvcGrpProfileTxFlashTime_Type.__name__ = "Integer32"
_SonusCassgSvcGrpProfileTxFlashTime_Object = MibTableColumn
sonusCassgSvcGrpProfileTxFlashTime = _SonusCassgSvcGrpProfileTxFlashTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1, 23),
    _SonusCassgSvcGrpProfileTxFlashTime_Type()
)
sonusCassgSvcGrpProfileTxFlashTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSvcGrpProfileTxFlashTime.setStatus("current")


class _SonusCassgSvcGrpProfileGuardTime_Type(Integer32):
    """Custom type sonusCassgSvcGrpProfileGuardTime based on Integer32"""
    defaultValue = 700

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1500),
    )


_SonusCassgSvcGrpProfileGuardTime_Type.__name__ = "Integer32"
_SonusCassgSvcGrpProfileGuardTime_Object = MibTableColumn
sonusCassgSvcGrpProfileGuardTime = _SonusCassgSvcGrpProfileGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1, 24),
    _SonusCassgSvcGrpProfileGuardTime_Type()
)
sonusCassgSvcGrpProfileGuardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSvcGrpProfileGuardTime.setStatus("current")


class _SonusCassgSvcGrpProfileAdminState_Type(SonusAdminState):
    """Custom type sonusCassgSvcGrpProfileAdminState based on SonusAdminState"""


_SonusCassgSvcGrpProfileAdminState_Object = MibTableColumn
sonusCassgSvcGrpProfileAdminState = _SonusCassgSvcGrpProfileAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1, 25),
    _SonusCassgSvcGrpProfileAdminState_Type()
)
sonusCassgSvcGrpProfileAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSvcGrpProfileAdminState.setStatus("current")
_SonusCassgSvcGrpProfileAlertToneName_Type = SonusNameReference
_SonusCassgSvcGrpProfileAlertToneName_Object = MibTableColumn
sonusCassgSvcGrpProfileAlertToneName = _SonusCassgSvcGrpProfileAlertToneName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1, 26),
    _SonusCassgSvcGrpProfileAlertToneName_Type()
)
sonusCassgSvcGrpProfileAlertToneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSvcGrpProfileAlertToneName.setStatus("current")
_SonusCassgSvcGrpProfileRowStatus_Type = RowStatus
_SonusCassgSvcGrpProfileRowStatus_Object = MibTableColumn
sonusCassgSvcGrpProfileRowStatus = _SonusCassgSvcGrpProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1, 27),
    _SonusCassgSvcGrpProfileRowStatus_Type()
)
sonusCassgSvcGrpProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSvcGrpProfileRowStatus.setStatus("current")
_SonusCassgSvcGrpProfileDTProfileName_Type = SonusNameReference
_SonusCassgSvcGrpProfileDTProfileName_Object = MibTableColumn
sonusCassgSvcGrpProfileDTProfileName = _SonusCassgSvcGrpProfileDTProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 2, 2, 1, 28),
    _SonusCassgSvcGrpProfileDTProfileName_Type()
)
sonusCassgSvcGrpProfileDTProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSvcGrpProfileDTProfileName.setStatus("current")
_SonusCasChannelAdmnTable_Object = MibTable
sonusCasChannelAdmnTable = _SonusCasChannelAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 3)
)
if mibBuilder.loadTexts:
    sonusCasChannelAdmnTable.setStatus("current")
_SonusCasChannelAdmnEntry_Object = MibTableRow
sonusCasChannelAdmnEntry = _SonusCasChannelAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 3, 1)
)
sonusCasChannelAdmnEntry.setIndexNames(
    (0, "SONUS-CAS-MIB", "sonusCassgChannelServiceIndex"),
    (0, "SONUS-CAS-MIB", "sonusCassgChannelShelfIndex"),
    (0, "SONUS-CAS-MIB", "sonusCassgChannelSlotIndex"),
    (0, "SONUS-CAS-MIB", "sonusCassgChannelPortIndex"),
    (0, "SONUS-CAS-MIB", "sonusCassgChannelDs3Index"),
    (0, "SONUS-CAS-MIB", "sonusCassgChannelDs1Index"),
    (0, "SONUS-CAS-MIB", "sonusCassgChannelIndex"),
)
if mibBuilder.loadTexts:
    sonusCasChannelAdmnEntry.setStatus("current")
_SonusCassgChannelServiceIndex_Type = Integer32
_SonusCassgChannelServiceIndex_Object = MibTableColumn
sonusCassgChannelServiceIndex = _SonusCassgChannelServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 3, 1, 1),
    _SonusCassgChannelServiceIndex_Type()
)
sonusCassgChannelServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgChannelServiceIndex.setStatus("current")
_SonusCassgChannelShelfIndex_Type = Integer32
_SonusCassgChannelShelfIndex_Object = MibTableColumn
sonusCassgChannelShelfIndex = _SonusCassgChannelShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 3, 1, 2),
    _SonusCassgChannelShelfIndex_Type()
)
sonusCassgChannelShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgChannelShelfIndex.setStatus("current")
_SonusCassgChannelSlotIndex_Type = Integer32
_SonusCassgChannelSlotIndex_Object = MibTableColumn
sonusCassgChannelSlotIndex = _SonusCassgChannelSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 3, 1, 3),
    _SonusCassgChannelSlotIndex_Type()
)
sonusCassgChannelSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgChannelSlotIndex.setStatus("current")
_SonusCassgChannelPortIndex_Type = Integer32
_SonusCassgChannelPortIndex_Object = MibTableColumn
sonusCassgChannelPortIndex = _SonusCassgChannelPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 3, 1, 4),
    _SonusCassgChannelPortIndex_Type()
)
sonusCassgChannelPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgChannelPortIndex.setStatus("current")
_SonusCassgChannelDs3Index_Type = Integer32
_SonusCassgChannelDs3Index_Object = MibTableColumn
sonusCassgChannelDs3Index = _SonusCassgChannelDs3Index_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 3, 1, 5),
    _SonusCassgChannelDs3Index_Type()
)
sonusCassgChannelDs3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgChannelDs3Index.setStatus("current")
_SonusCassgChannelDs1Index_Type = Integer32
_SonusCassgChannelDs1Index_Object = MibTableColumn
sonusCassgChannelDs1Index = _SonusCassgChannelDs1Index_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 3, 1, 6),
    _SonusCassgChannelDs1Index_Type()
)
sonusCassgChannelDs1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgChannelDs1Index.setStatus("current")


class _SonusCassgChannelIndex_Type(Integer32):
    """Custom type sonusCassgChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SonusCassgChannelIndex_Type.__name__ = "Integer32"
_SonusCassgChannelIndex_Object = MibTableColumn
sonusCassgChannelIndex = _SonusCassgChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 3, 1, 7),
    _SonusCassgChannelIndex_Type()
)
sonusCassgChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgChannelIndex.setStatus("current")
_SonusCassgChannelCircuitProfileName_Type = SonusNameReference
_SonusCassgChannelCircuitProfileName_Object = MibTableColumn
sonusCassgChannelCircuitProfileName = _SonusCassgChannelCircuitProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 3, 1, 8),
    _SonusCassgChannelCircuitProfileName_Type()
)
sonusCassgChannelCircuitProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgChannelCircuitProfileName.setStatus("current")


class _SonusCassgChannelDirection_Type(Integer32):
    """Custom type sonusCassgChannelDirection based on Integer32"""
    defaultValue = 1

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


_SonusCassgChannelDirection_Type.__name__ = "Integer32"
_SonusCassgChannelDirection_Object = MibTableColumn
sonusCassgChannelDirection = _SonusCassgChannelDirection_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 3, 1, 9),
    _SonusCassgChannelDirection_Type()
)
sonusCassgChannelDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgChannelDirection.setStatus("current")


class _SonusCassgChannelMode_Type(SonusServiceState):
    """Custom type sonusCassgChannelMode based on SonusServiceState"""


_SonusCassgChannelMode_Object = MibTableColumn
sonusCassgChannelMode = _SonusCassgChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 3, 1, 10),
    _SonusCassgChannelMode_Type()
)
sonusCassgChannelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgChannelMode.setStatus("current")


class _SonusCassgChannelAction_Type(SonusAdminAction):
    """Custom type sonusCassgChannelAction based on SonusAdminAction"""


_SonusCassgChannelAction_Object = MibTableColumn
sonusCassgChannelAction = _SonusCassgChannelAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 3, 1, 11),
    _SonusCassgChannelAction_Type()
)
sonusCassgChannelAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgChannelAction.setStatus("current")


class _SonusCassgChannelTimeout_Type(Integer32):
    """Custom type sonusCassgChannelTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_SonusCassgChannelTimeout_Type.__name__ = "Integer32"
_SonusCassgChannelTimeout_Object = MibTableColumn
sonusCassgChannelTimeout = _SonusCassgChannelTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 3, 1, 12),
    _SonusCassgChannelTimeout_Type()
)
sonusCassgChannelTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgChannelTimeout.setStatus("current")


class _SonusCassgChannelAdminState_Type(SonusAdminState):
    """Custom type sonusCassgChannelAdminState based on SonusAdminState"""


_SonusCassgChannelAdminState_Object = MibTableColumn
sonusCassgChannelAdminState = _SonusCassgChannelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 3, 1, 13),
    _SonusCassgChannelAdminState_Type()
)
sonusCassgChannelAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgChannelAdminState.setStatus("current")
_SonusCassgChannelRowStatus_Type = RowStatus
_SonusCassgChannelRowStatus_Object = MibTableColumn
sonusCassgChannelRowStatus = _SonusCassgChannelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 3, 1, 14),
    _SonusCassgChannelRowStatus_Type()
)
sonusCassgChannelRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgChannelRowStatus.setStatus("current")
_SonusCasChannelStatTable_Object = MibTable
sonusCasChannelStatTable = _SonusCasChannelStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 4)
)
if mibBuilder.loadTexts:
    sonusCasChannelStatTable.setStatus("current")
_SonusCasChannelStatEntry_Object = MibTableRow
sonusCasChannelStatEntry = _SonusCasChannelStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 4, 1)
)
sonusCasChannelStatEntry.setIndexNames(
    (0, "SONUS-CAS-MIB", "sonusCassgChannelStatServiceIndex"),
    (0, "SONUS-CAS-MIB", "sonusCassgChannelStatShelfIndex"),
    (0, "SONUS-CAS-MIB", "sonusCassgChannelStatSlotIndex"),
    (0, "SONUS-CAS-MIB", "sonusCassgChannelStatPortIndex"),
    (0, "SONUS-CAS-MIB", "sonusCassgChannelStatIndex"),
)
if mibBuilder.loadTexts:
    sonusCasChannelStatEntry.setStatus("current")
_SonusCassgChannelStatServiceIndex_Type = Integer32
_SonusCassgChannelStatServiceIndex_Object = MibTableColumn
sonusCassgChannelStatServiceIndex = _SonusCassgChannelStatServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 4, 1, 1),
    _SonusCassgChannelStatServiceIndex_Type()
)
sonusCassgChannelStatServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgChannelStatServiceIndex.setStatus("current")
_SonusCassgChannelStatShelfIndex_Type = Integer32
_SonusCassgChannelStatShelfIndex_Object = MibTableColumn
sonusCassgChannelStatShelfIndex = _SonusCassgChannelStatShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 4, 1, 2),
    _SonusCassgChannelStatShelfIndex_Type()
)
sonusCassgChannelStatShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgChannelStatShelfIndex.setStatus("current")
_SonusCassgChannelStatSlotIndex_Type = Integer32
_SonusCassgChannelStatSlotIndex_Object = MibTableColumn
sonusCassgChannelStatSlotIndex = _SonusCassgChannelStatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 4, 1, 3),
    _SonusCassgChannelStatSlotIndex_Type()
)
sonusCassgChannelStatSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgChannelStatSlotIndex.setStatus("current")
_SonusCassgChannelStatPortIndex_Type = Integer32
_SonusCassgChannelStatPortIndex_Object = MibTableColumn
sonusCassgChannelStatPortIndex = _SonusCassgChannelStatPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 4, 1, 4),
    _SonusCassgChannelStatPortIndex_Type()
)
sonusCassgChannelStatPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgChannelStatPortIndex.setStatus("current")
_SonusCassgChannelStatIndex_Type = Integer32
_SonusCassgChannelStatIndex_Object = MibTableColumn
sonusCassgChannelStatIndex = _SonusCassgChannelStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 4, 1, 5),
    _SonusCassgChannelStatIndex_Type()
)
sonusCassgChannelStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgChannelStatIndex.setStatus("current")


class _SonusCassgChannelStatUsage_Type(Integer32):
    """Custom type sonusCassgChannelStatUsage based on Integer32"""
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
        *(("idle", 2),
          ("inBusy", 3),
          ("outBusy", 4),
          ("transientRelease", 6),
          ("transientSetup", 5),
          ("unequipped", 1))
    )


_SonusCassgChannelStatUsage_Type.__name__ = "Integer32"
_SonusCassgChannelStatUsage_Object = MibTableColumn
sonusCassgChannelStatUsage = _SonusCassgChannelStatUsage_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 4, 1, 6),
    _SonusCassgChannelStatUsage_Type()
)
sonusCassgChannelStatUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgChannelStatUsage.setStatus("current")


class _SonusCassgChannelStatLocalMaint_Type(Integer32):
    """Custom type sonusCassgChannelStatLocalMaint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inService", 3),
          ("outOfServiceAuto", 2),
          ("outOfServiceManual", 1))
    )


_SonusCassgChannelStatLocalMaint_Type.__name__ = "Integer32"
_SonusCassgChannelStatLocalMaint_Object = MibTableColumn
sonusCassgChannelStatLocalMaint = _SonusCassgChannelStatLocalMaint_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 4, 1, 7),
    _SonusCassgChannelStatLocalMaint_Type()
)
sonusCassgChannelStatLocalMaint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgChannelStatLocalMaint.setStatus("current")


class _SonusCassgChannelStatLocalHw_Type(Integer32):
    """Custom type sonusCassgChannelStatLocalHw based on Integer32"""
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


_SonusCassgChannelStatLocalHw_Type.__name__ = "Integer32"
_SonusCassgChannelStatLocalHw_Object = MibTableColumn
sonusCassgChannelStatLocalHw = _SonusCassgChannelStatLocalHw_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 4, 1, 8),
    _SonusCassgChannelStatLocalHw_Type()
)
sonusCassgChannelStatLocalHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgChannelStatLocalHw.setStatus("current")


class _SonusCassgChannelStatRemoteMaint_Type(Integer32):
    """Custom type sonusCassgChannelStatRemoteMaint based on Integer32"""
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


_SonusCassgChannelStatRemoteMaint_Type.__name__ = "Integer32"
_SonusCassgChannelStatRemoteMaint_Object = MibTableColumn
sonusCassgChannelStatRemoteMaint = _SonusCassgChannelStatRemoteMaint_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 4, 1, 9),
    _SonusCassgChannelStatRemoteMaint_Type()
)
sonusCassgChannelStatRemoteMaint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgChannelStatRemoteMaint.setStatus("current")
_SonusCassgChannelStatIngressAttempts_Type = Integer32
_SonusCassgChannelStatIngressAttempts_Object = MibTableColumn
sonusCassgChannelStatIngressAttempts = _SonusCassgChannelStatIngressAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 4, 1, 10),
    _SonusCassgChannelStatIngressAttempts_Type()
)
sonusCassgChannelStatIngressAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgChannelStatIngressAttempts.setStatus("current")
_SonusCassgChannelStatIngressFailures_Type = Integer32
_SonusCassgChannelStatIngressFailures_Object = MibTableColumn
sonusCassgChannelStatIngressFailures = _SonusCassgChannelStatIngressFailures_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 4, 1, 11),
    _SonusCassgChannelStatIngressFailures_Type()
)
sonusCassgChannelStatIngressFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgChannelStatIngressFailures.setStatus("current")
_SonusCassgChannelStatEgressAttempts_Type = Integer32
_SonusCassgChannelStatEgressAttempts_Object = MibTableColumn
sonusCassgChannelStatEgressAttempts = _SonusCassgChannelStatEgressAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 4, 1, 12),
    _SonusCassgChannelStatEgressAttempts_Type()
)
sonusCassgChannelStatEgressAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgChannelStatEgressAttempts.setStatus("current")
_SonusCassgChannelStatEgressFailures_Type = Integer32
_SonusCassgChannelStatEgressFailures_Object = MibTableColumn
sonusCassgChannelStatEgressFailures = _SonusCassgChannelStatEgressFailures_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 4, 1, 13),
    _SonusCassgChannelStatEgressFailures_Type()
)
sonusCassgChannelStatEgressFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgChannelStatEgressFailures.setStatus("current")
_SonusCassgChannelStatMakeBusyFailures_Type = Integer32
_SonusCassgChannelStatMakeBusyFailures_Object = MibTableColumn
sonusCassgChannelStatMakeBusyFailures = _SonusCassgChannelStatMakeBusyFailures_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 4, 1, 14),
    _SonusCassgChannelStatMakeBusyFailures_Type()
)
sonusCassgChannelStatMakeBusyFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgChannelStatMakeBusyFailures.setStatus("current")
_SonusCassgChannelStatIngressCompletions_Type = Integer32
_SonusCassgChannelStatIngressCompletions_Object = MibTableColumn
sonusCassgChannelStatIngressCompletions = _SonusCassgChannelStatIngressCompletions_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 4, 1, 15),
    _SonusCassgChannelStatIngressCompletions_Type()
)
sonusCassgChannelStatIngressCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgChannelStatIngressCompletions.setStatus("current")
_SonusCassgChannelStatEgressCompletions_Type = Integer32
_SonusCassgChannelStatEgressCompletions_Object = MibTableColumn
sonusCassgChannelStatEgressCompletions = _SonusCassgChannelStatEgressCompletions_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 4, 1, 16),
    _SonusCassgChannelStatEgressCompletions_Type()
)
sonusCassgChannelStatEgressCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgChannelStatEgressCompletions.setStatus("current")
_SonusCasCollectionProfileAdmn_ObjectIdentity = ObjectIdentity
sonusCasCollectionProfileAdmn = _SonusCasCollectionProfileAdmn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 5)
)
_SonusCasCollectionProfileNextIndex_Type = Integer32
_SonusCasCollectionProfileNextIndex_Object = MibScalar
sonusCasCollectionProfileNextIndex = _SonusCasCollectionProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 5, 1),
    _SonusCasCollectionProfileNextIndex_Type()
)
sonusCasCollectionProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCasCollectionProfileNextIndex.setStatus("current")
_SonusCasCollectionProfileAdmnTable_Object = MibTable
sonusCasCollectionProfileAdmnTable = _SonusCasCollectionProfileAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 5, 2)
)
if mibBuilder.loadTexts:
    sonusCasCollectionProfileAdmnTable.setStatus("current")
_SonusCasCollectionProfileAdmnEntry_Object = MibTableRow
sonusCasCollectionProfileAdmnEntry = _SonusCasCollectionProfileAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 5, 2, 1)
)
sonusCasCollectionProfileAdmnEntry.setIndexNames(
    (0, "SONUS-CAS-MIB", "sonusCassgCollectProfileIndex"),
)
if mibBuilder.loadTexts:
    sonusCasCollectionProfileAdmnEntry.setStatus("current")
_SonusCassgCollectProfileIndex_Type = Integer32
_SonusCassgCollectProfileIndex_Object = MibTableColumn
sonusCassgCollectProfileIndex = _SonusCassgCollectProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 5, 2, 1, 1),
    _SonusCassgCollectProfileIndex_Type()
)
sonusCassgCollectProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgCollectProfileIndex.setStatus("current")
_SonusCassgCollectProfileName_Type = SonusName
_SonusCassgCollectProfileName_Object = MibTableColumn
sonusCassgCollectProfileName = _SonusCassgCollectProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 5, 2, 1, 2),
    _SonusCassgCollectProfileName_Type()
)
sonusCassgCollectProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgCollectProfileName.setStatus("current")


class _SonusCassgCollectProfileCollectId_Type(Integer32):
    """Custom type sonusCassgCollectProfileCollectId based on Integer32"""
    defaultValue = 1

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
        *(("ani", 3),
          ("calledParty", 1),
          ("callingParty", 2),
          ("carrierId", 7),
          ("dnis", 6),
          ("iani", 4),
          ("iiani", 5),
          ("internationalCountryCode", 8))
    )


_SonusCassgCollectProfileCollectId_Type.__name__ = "Integer32"
_SonusCassgCollectProfileCollectId_Object = MibTableColumn
sonusCassgCollectProfileCollectId = _SonusCassgCollectProfileCollectId_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 5, 2, 1, 3),
    _SonusCassgCollectProfileCollectId_Type()
)
sonusCassgCollectProfileCollectId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgCollectProfileCollectId.setStatus("current")


class _SonusCassgCollectProfileCollectType_Type(Integer32):
    """Custom type sonusCassgCollectProfileCollectType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtmf", 1),
          ("mf", 2))
    )


_SonusCassgCollectProfileCollectType_Type.__name__ = "Integer32"
_SonusCassgCollectProfileCollectType_Object = MibTableColumn
sonusCassgCollectProfileCollectType = _SonusCassgCollectProfileCollectType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 5, 2, 1, 4),
    _SonusCassgCollectProfileCollectType_Type()
)
sonusCassgCollectProfileCollectType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgCollectProfileCollectType.setStatus("current")


class _SonusCassgCollectProfileMinDigits_Type(Integer32):
    """Custom type sonusCassgCollectProfileMinDigits based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_SonusCassgCollectProfileMinDigits_Type.__name__ = "Integer32"
_SonusCassgCollectProfileMinDigits_Object = MibTableColumn
sonusCassgCollectProfileMinDigits = _SonusCassgCollectProfileMinDigits_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 5, 2, 1, 5),
    _SonusCassgCollectProfileMinDigits_Type()
)
sonusCassgCollectProfileMinDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgCollectProfileMinDigits.setStatus("current")


class _SonusCassgCollectProfileMaxDigits_Type(Integer32):
    """Custom type sonusCassgCollectProfileMaxDigits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_SonusCassgCollectProfileMaxDigits_Type.__name__ = "Integer32"
_SonusCassgCollectProfileMaxDigits_Object = MibTableColumn
sonusCassgCollectProfileMaxDigits = _SonusCassgCollectProfileMaxDigits_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 5, 2, 1, 6),
    _SonusCassgCollectProfileMaxDigits_Type()
)
sonusCassgCollectProfileMaxDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgCollectProfileMaxDigits.setStatus("current")


class _SonusCassgCollectProfileFirstDigitTime_Type(Integer32):
    """Custom type sonusCassgCollectProfileFirstDigitTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_SonusCassgCollectProfileFirstDigitTime_Type.__name__ = "Integer32"
_SonusCassgCollectProfileFirstDigitTime_Object = MibTableColumn
sonusCassgCollectProfileFirstDigitTime = _SonusCassgCollectProfileFirstDigitTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 5, 2, 1, 7),
    _SonusCassgCollectProfileFirstDigitTime_Type()
)
sonusCassgCollectProfileFirstDigitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgCollectProfileFirstDigitTime.setStatus("current")


class _SonusCassgCollectProfileInterDigitTime_Type(Integer32):
    """Custom type sonusCassgCollectProfileInterDigitTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_SonusCassgCollectProfileInterDigitTime_Type.__name__ = "Integer32"
_SonusCassgCollectProfileInterDigitTime_Object = MibTableColumn
sonusCassgCollectProfileInterDigitTime = _SonusCassgCollectProfileInterDigitTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 5, 2, 1, 8),
    _SonusCassgCollectProfileInterDigitTime_Type()
)
sonusCassgCollectProfileInterDigitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgCollectProfileInterDigitTime.setStatus("current")


class _SonusCassgCollectProfileFieldTime_Type(Integer32):
    """Custom type sonusCassgCollectProfileFieldTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_SonusCassgCollectProfileFieldTime_Type.__name__ = "Integer32"
_SonusCassgCollectProfileFieldTime_Object = MibTableColumn
sonusCassgCollectProfileFieldTime = _SonusCassgCollectProfileFieldTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 5, 2, 1, 9),
    _SonusCassgCollectProfileFieldTime_Type()
)
sonusCassgCollectProfileFieldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgCollectProfileFieldTime.setStatus("current")


class _SonusCassgCollectProfileTermDigit_Type(Integer32):
    """Custom type sonusCassgCollectProfileTermDigit based on Integer32"""
    defaultValue = 1

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
        *(("dtmfA", 4),
          ("dtmfB", 5),
          ("dtmfC", 6),
          ("dtmfD", 7),
          ("none", 1),
          ("pound", 3),
          ("star", 2))
    )


_SonusCassgCollectProfileTermDigit_Type.__name__ = "Integer32"
_SonusCassgCollectProfileTermDigit_Object = MibTableColumn
sonusCassgCollectProfileTermDigit = _SonusCassgCollectProfileTermDigit_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 5, 2, 1, 10),
    _SonusCassgCollectProfileTermDigit_Type()
)
sonusCassgCollectProfileTermDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgCollectProfileTermDigit.setStatus("current")


class _SonusCassgCollectProfileRestartDigit_Type(DisplayString):
    """Custom type sonusCassgCollectProfileRestartDigit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_SonusCassgCollectProfileRestartDigit_Type.__name__ = "DisplayString"
_SonusCassgCollectProfileRestartDigit_Object = MibTableColumn
sonusCassgCollectProfileRestartDigit = _SonusCassgCollectProfileRestartDigit_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 5, 2, 1, 11),
    _SonusCassgCollectProfileRestartDigit_Type()
)
sonusCassgCollectProfileRestartDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgCollectProfileRestartDigit.setStatus("current")


class _SonusCassgCollectProfileReinputDigit_Type(DisplayString):
    """Custom type sonusCassgCollectProfileReinputDigit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_SonusCassgCollectProfileReinputDigit_Type.__name__ = "DisplayString"
_SonusCassgCollectProfileReinputDigit_Object = MibTableColumn
sonusCassgCollectProfileReinputDigit = _SonusCassgCollectProfileReinputDigit_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 5, 2, 1, 12),
    _SonusCassgCollectProfileReinputDigit_Type()
)
sonusCassgCollectProfileReinputDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgCollectProfileReinputDigit.setStatus("current")


class _SonusCassgCollectProfileReportDigits_Type(Integer32):
    """Custom type sonusCassgCollectProfileReportDigits based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_SonusCassgCollectProfileReportDigits_Type.__name__ = "Integer32"
_SonusCassgCollectProfileReportDigits_Object = MibTableColumn
sonusCassgCollectProfileReportDigits = _SonusCassgCollectProfileReportDigits_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 5, 2, 1, 13),
    _SonusCassgCollectProfileReportDigits_Type()
)
sonusCassgCollectProfileReportDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgCollectProfileReportDigits.setStatus("current")


class _SonusCassgCollectProfileFirstDigitQuiet_Type(SonusAdminState):
    """Custom type sonusCassgCollectProfileFirstDigitQuiet based on SonusAdminState"""


_SonusCassgCollectProfileFirstDigitQuiet_Object = MibTableColumn
sonusCassgCollectProfileFirstDigitQuiet = _SonusCassgCollectProfileFirstDigitQuiet_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 5, 2, 1, 14),
    _SonusCassgCollectProfileFirstDigitQuiet_Type()
)
sonusCassgCollectProfileFirstDigitQuiet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgCollectProfileFirstDigitQuiet.setStatus("current")


class _SonusCassgCollectProfileAnnouncementPrompt_Type(Integer32):
    """Custom type sonusCassgCollectProfileAnnouncementPrompt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonusCassgCollectProfileAnnouncementPrompt_Type.__name__ = "Integer32"
_SonusCassgCollectProfileAnnouncementPrompt_Object = MibTableColumn
sonusCassgCollectProfileAnnouncementPrompt = _SonusCassgCollectProfileAnnouncementPrompt_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 5, 2, 1, 15),
    _SonusCassgCollectProfileAnnouncementPrompt_Type()
)
sonusCassgCollectProfileAnnouncementPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgCollectProfileAnnouncementPrompt.setStatus("current")


class _SonusCassgCollectProfileTonePrompt_Type(DisplayString):
    """Custom type sonusCassgCollectProfileTonePrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusCassgCollectProfileTonePrompt_Type.__name__ = "DisplayString"
_SonusCassgCollectProfileTonePrompt_Object = MibTableColumn
sonusCassgCollectProfileTonePrompt = _SonusCassgCollectProfileTonePrompt_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 5, 2, 1, 16),
    _SonusCassgCollectProfileTonePrompt_Type()
)
sonusCassgCollectProfileTonePrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgCollectProfileTonePrompt.setStatus("current")
_SonusCassgCollectProfileRowStatus_Type = RowStatus
_SonusCassgCollectProfileRowStatus_Object = MibTableColumn
sonusCassgCollectProfileRowStatus = _SonusCassgCollectProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 5, 2, 1, 17),
    _SonusCassgCollectProfileRowStatus_Type()
)
sonusCassgCollectProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgCollectProfileRowStatus.setStatus("current")
_SonusCasSspGroupAdmn_ObjectIdentity = ObjectIdentity
sonusCasSspGroupAdmn = _SonusCasSspGroupAdmn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 6)
)
_SonusCasSspNextIndex_Type = Integer32
_SonusCasSspNextIndex_Object = MibScalar
sonusCasSspNextIndex = _SonusCasSspNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 6, 1),
    _SonusCasSspNextIndex_Type()
)
sonusCasSspNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCasSspNextIndex.setStatus("current")
_SonusCasSspAdmnTable_Object = MibTable
sonusCasSspAdmnTable = _SonusCasSspAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 6, 2)
)
if mibBuilder.loadTexts:
    sonusCasSspAdmnTable.setStatus("current")
_SonusCasSspAdmnEntry_Object = MibTableRow
sonusCasSspAdmnEntry = _SonusCasSspAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 6, 2, 1)
)
sonusCasSspAdmnEntry.setIndexNames(
    (0, "SONUS-CAS-MIB", "sonusCassgSigSeqProfileIndex"),
)
if mibBuilder.loadTexts:
    sonusCasSspAdmnEntry.setStatus("current")
_SonusCassgSigSeqProfileIndex_Type = Integer32
_SonusCassgSigSeqProfileIndex_Object = MibTableColumn
sonusCassgSigSeqProfileIndex = _SonusCassgSigSeqProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 6, 2, 1, 1),
    _SonusCassgSigSeqProfileIndex_Type()
)
sonusCassgSigSeqProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgSigSeqProfileIndex.setStatus("current")
_SonusCassgSigSeqProfileName_Type = SonusName
_SonusCassgSigSeqProfileName_Object = MibTableColumn
sonusCassgSigSeqProfileName = _SonusCassgSigSeqProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 6, 2, 1, 2),
    _SonusCassgSigSeqProfileName_Type()
)
sonusCassgSigSeqProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSigSeqProfileName.setStatus("current")
_SonusCassgSigSeqProfileRowStatus_Type = RowStatus
_SonusCassgSigSeqProfileRowStatus_Object = MibTableColumn
sonusCassgSigSeqProfileRowStatus = _SonusCassgSigSeqProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 6, 2, 1, 3),
    _SonusCassgSigSeqProfileRowStatus_Type()
)
sonusCassgSigSeqProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSigSeqProfileRowStatus.setStatus("current")
_SonusCasSignalSeqAdmnTable_Object = MibTable
sonusCasSignalSeqAdmnTable = _SonusCasSignalSeqAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 7)
)
if mibBuilder.loadTexts:
    sonusCasSignalSeqAdmnTable.setStatus("current")
_SonusCasSignalSeqAdmnEntry_Object = MibTableRow
sonusCasSignalSeqAdmnEntry = _SonusCasSignalSeqAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 7, 1)
)
sonusCasSignalSeqAdmnEntry.setIndexNames(
    (0, "SONUS-CAS-MIB", "sonusCassgSigSequenceProfileIndex"),
    (0, "SONUS-CAS-MIB", "sonusCassgSigSequenceIndex"),
)
if mibBuilder.loadTexts:
    sonusCasSignalSeqAdmnEntry.setStatus("current")
_SonusCassgSigSequenceProfileIndex_Type = Integer32
_SonusCassgSigSequenceProfileIndex_Object = MibTableColumn
sonusCassgSigSequenceProfileIndex = _SonusCassgSigSequenceProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 7, 1, 1),
    _SonusCassgSigSequenceProfileIndex_Type()
)
sonusCassgSigSequenceProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgSigSequenceProfileIndex.setStatus("current")
_SonusCassgSigSequenceIndex_Type = Integer32
_SonusCassgSigSequenceIndex_Object = MibTableColumn
sonusCassgSigSequenceIndex = _SonusCassgSigSequenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 7, 1, 2),
    _SonusCassgSigSequenceIndex_Type()
)
sonusCassgSigSequenceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgSigSequenceIndex.setStatus("current")


class _SonusCassgSigSequencePosition_Type(Integer32):
    """Custom type sonusCassgSigSequencePosition based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_SonusCassgSigSequencePosition_Type.__name__ = "Integer32"
_SonusCassgSigSequencePosition_Object = MibTableColumn
sonusCassgSigSequencePosition = _SonusCassgSigSequencePosition_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 7, 1, 3),
    _SonusCassgSigSequencePosition_Type()
)
sonusCassgSigSequencePosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSigSequencePosition.setStatus("current")


class _SonusCassgSigSequenceToken_Type(Integer32):
    """Custom type sonusCassgSigSequenceToken based on Integer32"""
    defaultValue = 1

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
              17)
        )
    )
    namedValues = NamedValues(
        *(("clear", 16),
          ("collectDigit", 14),
          ("collectField", 13),
          ("delay", 9),
          ("dialDTMF", 5),
          ("dialDigit", 6),
          ("dialMF", 4),
          ("exec", 17),
          ("flash", 3),
          ("playAnn", 8),
          ("playTone", 7),
          ("report", 15),
          ("seize", 1),
          ("waitAnswer", 12),
          ("waitFlash", 11),
          ("waitWink", 10),
          ("wink", 2))
    )


_SonusCassgSigSequenceToken_Type.__name__ = "Integer32"
_SonusCassgSigSequenceToken_Object = MibTableColumn
sonusCassgSigSequenceToken = _SonusCassgSigSequenceToken_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 7, 1, 4),
    _SonusCassgSigSequenceToken_Type()
)
sonusCassgSigSequenceToken.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSigSequenceToken.setStatus("current")


class _SonusCassgSigSequenceParam1_Type(DisplayString):
    """Custom type sonusCassgSigSequenceParam1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SonusCassgSigSequenceParam1_Type.__name__ = "DisplayString"
_SonusCassgSigSequenceParam1_Object = MibTableColumn
sonusCassgSigSequenceParam1 = _SonusCassgSigSequenceParam1_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 7, 1, 5),
    _SonusCassgSigSequenceParam1_Type()
)
sonusCassgSigSequenceParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSigSequenceParam1.setStatus("current")


class _SonusCassgSigSequenceParam2_Type(DisplayString):
    """Custom type sonusCassgSigSequenceParam2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SonusCassgSigSequenceParam2_Type.__name__ = "DisplayString"
_SonusCassgSigSequenceParam2_Object = MibTableColumn
sonusCassgSigSequenceParam2 = _SonusCassgSigSequenceParam2_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 7, 1, 6),
    _SonusCassgSigSequenceParam2_Type()
)
sonusCassgSigSequenceParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSigSequenceParam2.setStatus("current")
_SonusCassgSigSequenceSigCondProfileName_Type = SonusNameReference
_SonusCassgSigSequenceSigCondProfileName_Object = MibTableColumn
sonusCassgSigSequenceSigCondProfileName = _SonusCassgSigSequenceSigCondProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 7, 1, 7),
    _SonusCassgSigSequenceSigCondProfileName_Type()
)
sonusCassgSigSequenceSigCondProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSigSequenceSigCondProfileName.setStatus("current")


class _SonusCassgSigSequenceAdminState_Type(SonusAdminState):
    """Custom type sonusCassgSigSequenceAdminState based on SonusAdminState"""


_SonusCassgSigSequenceAdminState_Object = MibTableColumn
sonusCassgSigSequenceAdminState = _SonusCassgSigSequenceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 7, 1, 8),
    _SonusCassgSigSequenceAdminState_Type()
)
sonusCassgSigSequenceAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSigSequenceAdminState.setStatus("current")
_SonusCassgSigSequenceRowStatus_Type = RowStatus
_SonusCassgSigSequenceRowStatus_Object = MibTableColumn
sonusCassgSigSequenceRowStatus = _SonusCassgSigSequenceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 7, 1, 9),
    _SonusCassgSigSequenceRowStatus_Type()
)
sonusCassgSigSequenceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSigSequenceRowStatus.setStatus("current")
_SonusCasScpAdmn_ObjectIdentity = ObjectIdentity
sonusCasScpAdmn = _SonusCasScpAdmn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 8)
)
_SonusCasScpNextIndex_Type = Integer32
_SonusCasScpNextIndex_Object = MibScalar
sonusCasScpNextIndex = _SonusCasScpNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 8, 1),
    _SonusCasScpNextIndex_Type()
)
sonusCasScpNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCasScpNextIndex.setStatus("current")
_SonusCasScpAdmnTable_Object = MibTable
sonusCasScpAdmnTable = _SonusCasScpAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 8, 2)
)
if mibBuilder.loadTexts:
    sonusCasScpAdmnTable.setStatus("current")
_SonusCasScpAdmnEntry_Object = MibTableRow
sonusCasScpAdmnEntry = _SonusCasScpAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 8, 2, 1)
)
sonusCasScpAdmnEntry.setIndexNames(
    (0, "SONUS-CAS-MIB", "sonusCassgSigCondProfileIndex"),
)
if mibBuilder.loadTexts:
    sonusCasScpAdmnEntry.setStatus("current")
_SonusCassgSigCondProfileIndex_Type = Integer32
_SonusCassgSigCondProfileIndex_Object = MibTableColumn
sonusCassgSigCondProfileIndex = _SonusCassgSigCondProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 8, 2, 1, 1),
    _SonusCassgSigCondProfileIndex_Type()
)
sonusCassgSigCondProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgSigCondProfileIndex.setStatus("current")
_SonusCassgSigCondProfileName_Type = SonusName
_SonusCassgSigCondProfileName_Object = MibTableColumn
sonusCassgSigCondProfileName = _SonusCassgSigCondProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 8, 2, 1, 2),
    _SonusCassgSigCondProfileName_Type()
)
sonusCassgSigCondProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSigCondProfileName.setStatus("current")
_SonusCassgSigCondProfileRowStatus_Type = RowStatus
_SonusCassgSigCondProfileRowStatus_Object = MibTableColumn
sonusCassgSigCondProfileRowStatus = _SonusCassgSigCondProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 8, 2, 1, 3),
    _SonusCassgSigCondProfileRowStatus_Type()
)
sonusCassgSigCondProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSigCondProfileRowStatus.setStatus("current")
_SonusCasSignalCondAdmnTable_Object = MibTable
sonusCasSignalCondAdmnTable = _SonusCasSignalCondAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 8, 3)
)
if mibBuilder.loadTexts:
    sonusCasSignalCondAdmnTable.setStatus("current")
_SonusCasSignalCondAdmnEntry_Object = MibTableRow
sonusCasSignalCondAdmnEntry = _SonusCasSignalCondAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 8, 3, 1)
)
sonusCasSignalCondAdmnEntry.setIndexNames(
    (0, "SONUS-CAS-MIB", "sonusCassgSigConditionProfileIndex"),
    (0, "SONUS-CAS-MIB", "sonusCassgSigConditionIndex"),
)
if mibBuilder.loadTexts:
    sonusCasSignalCondAdmnEntry.setStatus("current")
_SonusCassgSigConditionProfileIndex_Type = Integer32
_SonusCassgSigConditionProfileIndex_Object = MibTableColumn
sonusCassgSigConditionProfileIndex = _SonusCassgSigConditionProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 8, 3, 1, 1),
    _SonusCassgSigConditionProfileIndex_Type()
)
sonusCassgSigConditionProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgSigConditionProfileIndex.setStatus("current")
_SonusCassgSigConditionIndex_Type = Integer32
_SonusCassgSigConditionIndex_Object = MibTableColumn
sonusCassgSigConditionIndex = _SonusCassgSigConditionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 8, 3, 1, 2),
    _SonusCassgSigConditionIndex_Type()
)
sonusCassgSigConditionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgSigConditionIndex.setStatus("current")


class _SonusCassgSigConditionToken_Type(Integer32):
    """Custom type sonusCassgSigConditionToken based on Integer32"""
    defaultValue = 1

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
              13)
        )
    )
    namedValues = NamedValues(
        *(("answerTimeout", 12),
          ("cutThrough", 13),
          ("default", 1),
          ("fieldTimeout", 4),
          ("firstDigitTimeout", 2),
          ("flashTimeout", 11),
          ("interDigitTimeout", 3),
          ("rxAnswer", 9),
          ("rxFlash", 8),
          ("rxWink", 7),
          ("shortCollection", 5),
          ("unexpectedDigit", 6),
          ("winkTimeout", 10))
    )


_SonusCassgSigConditionToken_Type.__name__ = "Integer32"
_SonusCassgSigConditionToken_Object = MibTableColumn
sonusCassgSigConditionToken = _SonusCassgSigConditionToken_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 8, 3, 1, 3),
    _SonusCassgSigConditionToken_Type()
)
sonusCassgSigConditionToken.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSigConditionToken.setStatus("current")


class _SonusCassgSigConditionControl_Type(Integer32):
    """Custom type sonusCassgSigConditionControl based on Integer32"""
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
        *(("abort", 3),
          ("abortMB", 4),
          ("exec", 2),
          ("proceed", 1))
    )


_SonusCassgSigConditionControl_Type.__name__ = "Integer32"
_SonusCassgSigConditionControl_Object = MibTableColumn
sonusCassgSigConditionControl = _SonusCassgSigConditionControl_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 8, 3, 1, 4),
    _SonusCassgSigConditionControl_Type()
)
sonusCassgSigConditionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSigConditionControl.setStatus("current")


class _SonusCassgSigConditionParam_Type(DisplayString):
    """Custom type sonusCassgSigConditionParam based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SonusCassgSigConditionParam_Type.__name__ = "DisplayString"
_SonusCassgSigConditionParam_Object = MibTableColumn
sonusCassgSigConditionParam = _SonusCassgSigConditionParam_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 8, 3, 1, 5),
    _SonusCassgSigConditionParam_Type()
)
sonusCassgSigConditionParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSigConditionParam.setStatus("current")


class _SonusCassgSigConditionAdminState_Type(SonusAdminState):
    """Custom type sonusCassgSigConditionAdminState based on SonusAdminState"""


_SonusCassgSigConditionAdminState_Object = MibTableColumn
sonusCassgSigConditionAdminState = _SonusCassgSigConditionAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 8, 3, 1, 6),
    _SonusCassgSigConditionAdminState_Type()
)
sonusCassgSigConditionAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSigConditionAdminState.setStatus("current")
_SonusCassgSigConditionRowStatus_Type = RowStatus
_SonusCassgSigConditionRowStatus_Object = MibTableColumn
sonusCassgSigConditionRowStatus = _SonusCassgSigConditionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 8, 3, 1, 7),
    _SonusCassgSigConditionRowStatus_Type()
)
sonusCassgSigConditionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgSigConditionRowStatus.setStatus("current")
_SonusCasDisconnectTreatAdmnTable_Object = MibTable
sonusCasDisconnectTreatAdmnTable = _SonusCasDisconnectTreatAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 9)
)
if mibBuilder.loadTexts:
    sonusCasDisconnectTreatAdmnTable.setStatus("deprecated")
_SonusCasDisconnectTreatAdmnEntry_Object = MibTableRow
sonusCasDisconnectTreatAdmnEntry = _SonusCasDisconnectTreatAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 9, 1)
)
sonusCasDisconnectTreatAdmnEntry.setIndexNames(
    (0, "SONUS-CAS-MIB", "sonusCassgDiscTreatmentIndex"),
)
if mibBuilder.loadTexts:
    sonusCasDisconnectTreatAdmnEntry.setStatus("deprecated")
_SonusCassgDiscTreatmentIndex_Type = Integer32
_SonusCassgDiscTreatmentIndex_Object = MibTableColumn
sonusCassgDiscTreatmentIndex = _SonusCassgDiscTreatmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 9, 1, 1),
    _SonusCassgDiscTreatmentIndex_Type()
)
sonusCassgDiscTreatmentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgDiscTreatmentIndex.setStatus("deprecated")


class _SonusCassgDiscTreatmentReason_Type(Integer32):
    """Custom type sonusCassgDiscTreatmentReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SonusCassgDiscTreatmentReason_Type.__name__ = "Integer32"
_SonusCassgDiscTreatmentReason_Object = MibTableColumn
sonusCassgDiscTreatmentReason = _SonusCassgDiscTreatmentReason_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 9, 1, 2),
    _SonusCassgDiscTreatmentReason_Type()
)
sonusCassgDiscTreatmentReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCassgDiscTreatmentReason.setStatus("deprecated")
_SonusCassgDiscTreatmentSigSeqProfileName_Type = SonusNameReference
_SonusCassgDiscTreatmentSigSeqProfileName_Object = MibTableColumn
sonusCassgDiscTreatmentSigSeqProfileName = _SonusCassgDiscTreatmentSigSeqProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 9, 1, 3),
    _SonusCassgDiscTreatmentSigSeqProfileName_Type()
)
sonusCassgDiscTreatmentSigSeqProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgDiscTreatmentSigSeqProfileName.setStatus("deprecated")
_SonusCassgDiscTreatmentRowStatus_Type = RowStatus
_SonusCassgDiscTreatmentRowStatus_Object = MibTableColumn
sonusCassgDiscTreatmentRowStatus = _SonusCassgDiscTreatmentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 9, 1, 4),
    _SonusCassgDiscTreatmentRowStatus_Type()
)
sonusCassgDiscTreatmentRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusCassgDiscTreatmentRowStatus.setStatus("deprecated")
_SonusCasServiceGroupMIBNotifications_ObjectIdentity = ObjectIdentity
sonusCasServiceGroupMIBNotifications = _SonusCasServiceGroupMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 10)
)
_SonusCasServiceGroupMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusCasServiceGroupMIBNotificationsPrefix = _SonusCasServiceGroupMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 10, 0)
)
_SonusCasServiceGroupMIBNotificationsObjects_ObjectIdentity = ObjectIdentity
sonusCasServiceGroupMIBNotificationsObjects = _SonusCasServiceGroupMIBNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 10, 1)
)


class _SonusCasSvcGrpName_Type(DisplayString):
    """Custom type sonusCasSvcGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusCasSvcGrpName_Type.__name__ = "DisplayString"
_SonusCasSvcGrpName_Object = MibScalar
sonusCasSvcGrpName = _SonusCasSvcGrpName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 10, 1, 1),
    _SonusCasSvcGrpName_Type()
)
sonusCasSvcGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusCasSvcGrpName.setStatus("current")

# Managed Objects groups


# Notification objects

sonusCasSvcGrpInServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 10, 0, 1)
)
sonusCasSvcGrpInServiceNotification.setObjects(
      *(("SONUS-CAS-MIB", "sonusCasSvcGrpName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusCasSvcGrpInServiceNotification.setStatus(
        "current"
    )

sonusCasSvcGrpOutOfServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 10, 0, 2)
)
sonusCasSvcGrpOutOfServiceNotification.setObjects(
      *(("SONUS-CAS-MIB", "sonusCasSvcGrpName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusCasSvcGrpOutOfServiceNotification.setStatus(
        "current"
    )

sonusCasChannelInServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 10, 0, 3)
)
sonusCasChannelInServiceNotification.setObjects(
      *(("SONUS-CAS-MIB", "sonusCasSvcGrpName"),
        ("SONUS-CAS-MIB", "sonusCassgChannelShelfIndex"),
        ("SONUS-CAS-MIB", "sonusCassgChannelSlotIndex"),
        ("SONUS-CAS-MIB", "sonusCassgChannelPortIndex"),
        ("SONUS-CAS-MIB", "sonusCassgChannelIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusCasChannelInServiceNotification.setStatus(
        "current"
    )

sonusCasChannelOutOfServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 5, 1, 10, 0, 4)
)
sonusCasChannelOutOfServiceNotification.setObjects(
      *(("SONUS-CAS-MIB", "sonusCasSvcGrpName"),
        ("SONUS-CAS-MIB", "sonusCassgChannelShelfIndex"),
        ("SONUS-CAS-MIB", "sonusCassgChannelSlotIndex"),
        ("SONUS-CAS-MIB", "sonusCassgChannelPortIndex"),
        ("SONUS-CAS-MIB", "sonusCassgChannelIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusCasChannelOutOfServiceNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-CAS-MIB",
    **{"sonusCasMIB": sonusCasMIB,
       "sonusCasMIBObjects": sonusCasMIBObjects,
       "sonusCasServiceGroup": sonusCasServiceGroup,
       "sonusCasServiceGroupNextIndex": sonusCasServiceGroupNextIndex,
       "sonusCasServiceGroupAdmnTable": sonusCasServiceGroupAdmnTable,
       "sonusCasServiceGroupAdmnEntry": sonusCasServiceGroupAdmnEntry,
       "sonusCassgServiceGroupIndex": sonusCassgServiceGroupIndex,
       "sonusCassgServiceGroupName": sonusCassgServiceGroupName,
       "sonusCassgServiceGroupProfileName": sonusCassgServiceGroupProfileName,
       "sonusCassgServiceGroupTG": sonusCassgServiceGroupTG,
       "sonusCassgServiceGroupHuntAlgorithm": sonusCassgServiceGroupHuntAlgorithm,
       "sonusCassgServiceGroupCost": sonusCassgServiceGroupCost,
       "sonusCassgServiceGroupSignalType": sonusCassgServiceGroupSignalType,
       "sonusCassgServiceGroupIngressSSP": sonusCassgServiceGroupIngressSSP,
       "sonusCassgServiceGroupEgressSSP": sonusCassgServiceGroupEgressSSP,
       "sonusCassgServiceGroupHookflashSSP": sonusCassgServiceGroupHookflashSSP,
       "sonusCassgServiceGroupPscSSP": sonusCassgServiceGroupPscSSP,
       "sonusCassgServiceGroupMaintBusy": sonusCassgServiceGroupMaintBusy,
       "sonusCassgServiceGroupAutoBusyThreshold": sonusCassgServiceGroupAutoBusyThreshold,
       "sonusCassgServiceGroupRequiresCPTone": sonusCassgServiceGroupRequiresCPTone,
       "sonusCassgServiceGroupProvidesCPTone": sonusCassgServiceGroupProvidesCPTone,
       "sonusCassgServiceGroupDTMFProfileName": sonusCassgServiceGroupDTMFProfileName,
       "sonusCassgServiceGroupMFProfileName": sonusCassgServiceGroupMFProfileName,
       "sonusCassgServiceGroupCPTonePkgName": sonusCassgServiceGroupCPTonePkgName,
       "sonusCassgServiceGroupMinRxWinkTime": sonusCassgServiceGroupMinRxWinkTime,
       "sonusCassgServiceGroupMaxRxWinkTime": sonusCassgServiceGroupMaxRxWinkTime,
       "sonusCassgServiceGroupMinRxFlashTime": sonusCassgServiceGroupMinRxFlashTime,
       "sonusCassgServiceGroupMaxRxFlashTime": sonusCassgServiceGroupMaxRxFlashTime,
       "sonusCassgServiceGroupTxWinkTime": sonusCassgServiceGroupTxWinkTime,
       "sonusCassgServiceGroupTxFlashTime": sonusCassgServiceGroupTxFlashTime,
       "sonusCassgServiceGroupGuardTime": sonusCassgServiceGroupGuardTime,
       "sonusCassgServiceGroupOperation": sonusCassgServiceGroupOperation,
       "sonusCassgServiceGroupAdminState": sonusCassgServiceGroupAdminState,
       "sonusCassgServiceGroupMode": sonusCassgServiceGroupMode,
       "sonusCassgServiceGroupAction": sonusCassgServiceGroupAction,
       "sonusCassgServiceGroupTimeout": sonusCassgServiceGroupTimeout,
       "sonusCassgServiceGroupAlertToneName": sonusCassgServiceGroupAlertToneName,
       "sonusCassgServiceGroupRowStatus": sonusCassgServiceGroupRowStatus,
       "sonusCassgServiceGroupDTProfileName": sonusCassgServiceGroupDTProfileName,
       "sonusCasSvcGrpProfileAdmn": sonusCasSvcGrpProfileAdmn,
       "sonusCasSvcGrpProfileNextIndex": sonusCasSvcGrpProfileNextIndex,
       "sonusCasSvcGrpProfileAdmnTable": sonusCasSvcGrpProfileAdmnTable,
       "sonusCasSvcGrpProfileAdmnEntry": sonusCasSvcGrpProfileAdmnEntry,
       "sonusCassgSvcGrpProfileIndex": sonusCassgSvcGrpProfileIndex,
       "sonusCassgSvcGrpProfileName": sonusCassgSvcGrpProfileName,
       "sonusCassgSvcGrpProfileTG": sonusCassgSvcGrpProfileTG,
       "sonusCassgSvcGrpProfileHuntAlgorithm": sonusCassgSvcGrpProfileHuntAlgorithm,
       "sonusCassgSvcGrpProfileCost": sonusCassgSvcGrpProfileCost,
       "sonusCassgSvcGrpProfileSignalType": sonusCassgSvcGrpProfileSignalType,
       "sonusCassgSvcGrpProfileIngressSSP": sonusCassgSvcGrpProfileIngressSSP,
       "sonusCassgSvcGrpProfileEgressSSP": sonusCassgSvcGrpProfileEgressSSP,
       "sonusCassgSvcGrpProfileHookflashSSP": sonusCassgSvcGrpProfileHookflashSSP,
       "sonusCassgSvcGrpProfilePscSSP": sonusCassgSvcGrpProfilePscSSP,
       "sonusCassgSvcGrpProfileMaintBusy": sonusCassgSvcGrpProfileMaintBusy,
       "sonusCassgSvcGrpProfileAutoBusyThreshold": sonusCassgSvcGrpProfileAutoBusyThreshold,
       "sonusCassgSvcGrpProfileRequiresCPTone": sonusCassgSvcGrpProfileRequiresCPTone,
       "sonusCassgSvcGrpProfileProvidesCPTone": sonusCassgSvcGrpProfileProvidesCPTone,
       "sonusCassgSvcGrpProfileDTMFProfileName": sonusCassgSvcGrpProfileDTMFProfileName,
       "sonusCassgSvcGrpProfileMFProfileName": sonusCassgSvcGrpProfileMFProfileName,
       "sonusCassgSvcGrpProfileCPTonePkgName": sonusCassgSvcGrpProfileCPTonePkgName,
       "sonusCassgSvcGrpProfileMinRxWinkTime": sonusCassgSvcGrpProfileMinRxWinkTime,
       "sonusCassgSvcGrpProfileMaxRxWinkTime": sonusCassgSvcGrpProfileMaxRxWinkTime,
       "sonusCassgSvcGrpProfileMinRxFlashTime": sonusCassgSvcGrpProfileMinRxFlashTime,
       "sonusCassgSvcGrpProfileMaxRxFlashTime": sonusCassgSvcGrpProfileMaxRxFlashTime,
       "sonusCassgSvcGrpProfileTxWinkTime": sonusCassgSvcGrpProfileTxWinkTime,
       "sonusCassgSvcGrpProfileTxFlashTime": sonusCassgSvcGrpProfileTxFlashTime,
       "sonusCassgSvcGrpProfileGuardTime": sonusCassgSvcGrpProfileGuardTime,
       "sonusCassgSvcGrpProfileAdminState": sonusCassgSvcGrpProfileAdminState,
       "sonusCassgSvcGrpProfileAlertToneName": sonusCassgSvcGrpProfileAlertToneName,
       "sonusCassgSvcGrpProfileRowStatus": sonusCassgSvcGrpProfileRowStatus,
       "sonusCassgSvcGrpProfileDTProfileName": sonusCassgSvcGrpProfileDTProfileName,
       "sonusCasChannelAdmnTable": sonusCasChannelAdmnTable,
       "sonusCasChannelAdmnEntry": sonusCasChannelAdmnEntry,
       "sonusCassgChannelServiceIndex": sonusCassgChannelServiceIndex,
       "sonusCassgChannelShelfIndex": sonusCassgChannelShelfIndex,
       "sonusCassgChannelSlotIndex": sonusCassgChannelSlotIndex,
       "sonusCassgChannelPortIndex": sonusCassgChannelPortIndex,
       "sonusCassgChannelDs3Index": sonusCassgChannelDs3Index,
       "sonusCassgChannelDs1Index": sonusCassgChannelDs1Index,
       "sonusCassgChannelIndex": sonusCassgChannelIndex,
       "sonusCassgChannelCircuitProfileName": sonusCassgChannelCircuitProfileName,
       "sonusCassgChannelDirection": sonusCassgChannelDirection,
       "sonusCassgChannelMode": sonusCassgChannelMode,
       "sonusCassgChannelAction": sonusCassgChannelAction,
       "sonusCassgChannelTimeout": sonusCassgChannelTimeout,
       "sonusCassgChannelAdminState": sonusCassgChannelAdminState,
       "sonusCassgChannelRowStatus": sonusCassgChannelRowStatus,
       "sonusCasChannelStatTable": sonusCasChannelStatTable,
       "sonusCasChannelStatEntry": sonusCasChannelStatEntry,
       "sonusCassgChannelStatServiceIndex": sonusCassgChannelStatServiceIndex,
       "sonusCassgChannelStatShelfIndex": sonusCassgChannelStatShelfIndex,
       "sonusCassgChannelStatSlotIndex": sonusCassgChannelStatSlotIndex,
       "sonusCassgChannelStatPortIndex": sonusCassgChannelStatPortIndex,
       "sonusCassgChannelStatIndex": sonusCassgChannelStatIndex,
       "sonusCassgChannelStatUsage": sonusCassgChannelStatUsage,
       "sonusCassgChannelStatLocalMaint": sonusCassgChannelStatLocalMaint,
       "sonusCassgChannelStatLocalHw": sonusCassgChannelStatLocalHw,
       "sonusCassgChannelStatRemoteMaint": sonusCassgChannelStatRemoteMaint,
       "sonusCassgChannelStatIngressAttempts": sonusCassgChannelStatIngressAttempts,
       "sonusCassgChannelStatIngressFailures": sonusCassgChannelStatIngressFailures,
       "sonusCassgChannelStatEgressAttempts": sonusCassgChannelStatEgressAttempts,
       "sonusCassgChannelStatEgressFailures": sonusCassgChannelStatEgressFailures,
       "sonusCassgChannelStatMakeBusyFailures": sonusCassgChannelStatMakeBusyFailures,
       "sonusCassgChannelStatIngressCompletions": sonusCassgChannelStatIngressCompletions,
       "sonusCassgChannelStatEgressCompletions": sonusCassgChannelStatEgressCompletions,
       "sonusCasCollectionProfileAdmn": sonusCasCollectionProfileAdmn,
       "sonusCasCollectionProfileNextIndex": sonusCasCollectionProfileNextIndex,
       "sonusCasCollectionProfileAdmnTable": sonusCasCollectionProfileAdmnTable,
       "sonusCasCollectionProfileAdmnEntry": sonusCasCollectionProfileAdmnEntry,
       "sonusCassgCollectProfileIndex": sonusCassgCollectProfileIndex,
       "sonusCassgCollectProfileName": sonusCassgCollectProfileName,
       "sonusCassgCollectProfileCollectId": sonusCassgCollectProfileCollectId,
       "sonusCassgCollectProfileCollectType": sonusCassgCollectProfileCollectType,
       "sonusCassgCollectProfileMinDigits": sonusCassgCollectProfileMinDigits,
       "sonusCassgCollectProfileMaxDigits": sonusCassgCollectProfileMaxDigits,
       "sonusCassgCollectProfileFirstDigitTime": sonusCassgCollectProfileFirstDigitTime,
       "sonusCassgCollectProfileInterDigitTime": sonusCassgCollectProfileInterDigitTime,
       "sonusCassgCollectProfileFieldTime": sonusCassgCollectProfileFieldTime,
       "sonusCassgCollectProfileTermDigit": sonusCassgCollectProfileTermDigit,
       "sonusCassgCollectProfileRestartDigit": sonusCassgCollectProfileRestartDigit,
       "sonusCassgCollectProfileReinputDigit": sonusCassgCollectProfileReinputDigit,
       "sonusCassgCollectProfileReportDigits": sonusCassgCollectProfileReportDigits,
       "sonusCassgCollectProfileFirstDigitQuiet": sonusCassgCollectProfileFirstDigitQuiet,
       "sonusCassgCollectProfileAnnouncementPrompt": sonusCassgCollectProfileAnnouncementPrompt,
       "sonusCassgCollectProfileTonePrompt": sonusCassgCollectProfileTonePrompt,
       "sonusCassgCollectProfileRowStatus": sonusCassgCollectProfileRowStatus,
       "sonusCasSspGroupAdmn": sonusCasSspGroupAdmn,
       "sonusCasSspNextIndex": sonusCasSspNextIndex,
       "sonusCasSspAdmnTable": sonusCasSspAdmnTable,
       "sonusCasSspAdmnEntry": sonusCasSspAdmnEntry,
       "sonusCassgSigSeqProfileIndex": sonusCassgSigSeqProfileIndex,
       "sonusCassgSigSeqProfileName": sonusCassgSigSeqProfileName,
       "sonusCassgSigSeqProfileRowStatus": sonusCassgSigSeqProfileRowStatus,
       "sonusCasSignalSeqAdmnTable": sonusCasSignalSeqAdmnTable,
       "sonusCasSignalSeqAdmnEntry": sonusCasSignalSeqAdmnEntry,
       "sonusCassgSigSequenceProfileIndex": sonusCassgSigSequenceProfileIndex,
       "sonusCassgSigSequenceIndex": sonusCassgSigSequenceIndex,
       "sonusCassgSigSequencePosition": sonusCassgSigSequencePosition,
       "sonusCassgSigSequenceToken": sonusCassgSigSequenceToken,
       "sonusCassgSigSequenceParam1": sonusCassgSigSequenceParam1,
       "sonusCassgSigSequenceParam2": sonusCassgSigSequenceParam2,
       "sonusCassgSigSequenceSigCondProfileName": sonusCassgSigSequenceSigCondProfileName,
       "sonusCassgSigSequenceAdminState": sonusCassgSigSequenceAdminState,
       "sonusCassgSigSequenceRowStatus": sonusCassgSigSequenceRowStatus,
       "sonusCasScpAdmn": sonusCasScpAdmn,
       "sonusCasScpNextIndex": sonusCasScpNextIndex,
       "sonusCasScpAdmnTable": sonusCasScpAdmnTable,
       "sonusCasScpAdmnEntry": sonusCasScpAdmnEntry,
       "sonusCassgSigCondProfileIndex": sonusCassgSigCondProfileIndex,
       "sonusCassgSigCondProfileName": sonusCassgSigCondProfileName,
       "sonusCassgSigCondProfileRowStatus": sonusCassgSigCondProfileRowStatus,
       "sonusCasSignalCondAdmnTable": sonusCasSignalCondAdmnTable,
       "sonusCasSignalCondAdmnEntry": sonusCasSignalCondAdmnEntry,
       "sonusCassgSigConditionProfileIndex": sonusCassgSigConditionProfileIndex,
       "sonusCassgSigConditionIndex": sonusCassgSigConditionIndex,
       "sonusCassgSigConditionToken": sonusCassgSigConditionToken,
       "sonusCassgSigConditionControl": sonusCassgSigConditionControl,
       "sonusCassgSigConditionParam": sonusCassgSigConditionParam,
       "sonusCassgSigConditionAdminState": sonusCassgSigConditionAdminState,
       "sonusCassgSigConditionRowStatus": sonusCassgSigConditionRowStatus,
       "sonusCasDisconnectTreatAdmnTable": sonusCasDisconnectTreatAdmnTable,
       "sonusCasDisconnectTreatAdmnEntry": sonusCasDisconnectTreatAdmnEntry,
       "sonusCassgDiscTreatmentIndex": sonusCassgDiscTreatmentIndex,
       "sonusCassgDiscTreatmentReason": sonusCassgDiscTreatmentReason,
       "sonusCassgDiscTreatmentSigSeqProfileName": sonusCassgDiscTreatmentSigSeqProfileName,
       "sonusCassgDiscTreatmentRowStatus": sonusCassgDiscTreatmentRowStatus,
       "sonusCasServiceGroupMIBNotifications": sonusCasServiceGroupMIBNotifications,
       "sonusCasServiceGroupMIBNotificationsPrefix": sonusCasServiceGroupMIBNotificationsPrefix,
       "sonusCasSvcGrpInServiceNotification": sonusCasSvcGrpInServiceNotification,
       "sonusCasSvcGrpOutOfServiceNotification": sonusCasSvcGrpOutOfServiceNotification,
       "sonusCasChannelInServiceNotification": sonusCasChannelInServiceNotification,
       "sonusCasChannelOutOfServiceNotification": sonusCasChannelOutOfServiceNotification,
       "sonusCasServiceGroupMIBNotificationsObjects": sonusCasServiceGroupMIBNotificationsObjects,
       "sonusCasSvcGrpName": sonusCasSvcGrpName}
)
