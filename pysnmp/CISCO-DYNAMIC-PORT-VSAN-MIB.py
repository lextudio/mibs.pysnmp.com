# SNMP MIB module (CISCO-DYNAMIC-PORT-VSAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DYNAMIC-PORT-VSAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:15 2024
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

(CpsmActivateResult,
 CpsmDbActivate,
 CpsmDiffDb,
 CpsmDiffReason) = mibBuilder.importSymbols(
    "CISCO-PSM-MIB",
    "CpsmActivateResult",
    "CpsmDbActivate",
    "CpsmDiffDb",
    "CpsmDiffReason")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(FcNameId,
 FcNameIdOrZero,
 VsanIndex) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "FcNameId",
    "FcNameIdOrZero",
    "VsanIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

ciscoDpvmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 421)
)
ciscoDpvmMIB.setRevisions(
        ("2004-06-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CdpvmDevType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nwwn", 2),
          ("pwwn", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoDpvmMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoDpvmMIBNotifs = _CiscoDpvmMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 0)
)
_CiscoDpvmMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDpvmMIBObjects = _CiscoDpvmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1)
)
_CdpvmConfiguration_ObjectIdentity = ObjectIdentity
cdpvmConfiguration = _CdpvmConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1)
)


class _CdpvmNextAvailIndex_Type(Unsigned32):
    """Custom type cdpvmNextAvailIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_CdpvmNextAvailIndex_Type.__name__ = "Unsigned32"
_CdpvmNextAvailIndex_Object = MibScalar
cdpvmNextAvailIndex = _CdpvmNextAvailIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 1),
    _CdpvmNextAvailIndex_Type()
)
cdpvmNextAvailIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpvmNextAvailIndex.setStatus("current")
_CdpvmTable_Object = MibTable
cdpvmTable = _CdpvmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cdpvmTable.setStatus("current")
_CdpvmEntry_Object = MibTableRow
cdpvmEntry = _CdpvmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 2, 1)
)
cdpvmEntry.setIndexNames(
    (0, "CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmIndex"),
)
if mibBuilder.loadTexts:
    cdpvmEntry.setStatus("current")


class _CdpvmIndex_Type(Unsigned32):
    """Custom type cdpvmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_CdpvmIndex_Type.__name__ = "Unsigned32"
_CdpvmIndex_Object = MibTableColumn
cdpvmIndex = _CdpvmIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 2, 1, 1),
    _CdpvmIndex_Type()
)
cdpvmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdpvmIndex.setStatus("current")


class _CdpvmLoginDevType_Type(CdpvmDevType):
    """Custom type cdpvmLoginDevType based on CdpvmDevType"""


_CdpvmLoginDevType_Object = MibTableColumn
cdpvmLoginDevType = _CdpvmLoginDevType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 2, 1, 2),
    _CdpvmLoginDevType_Type()
)
cdpvmLoginDevType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdpvmLoginDevType.setStatus("current")
_CdpvmLoginDev_Type = FcNameId
_CdpvmLoginDev_Object = MibTableColumn
cdpvmLoginDev = _CdpvmLoginDev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 2, 1, 3),
    _CdpvmLoginDev_Type()
)
cdpvmLoginDev.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdpvmLoginDev.setStatus("current")


class _CdpvmLoginDevVsan_Type(VsanIndex):
    """Custom type cdpvmLoginDevVsan based on VsanIndex"""
    defaultValue = 1


_CdpvmLoginDevVsan_Object = MibTableColumn
cdpvmLoginDevVsan = _CdpvmLoginDevVsan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 2, 1, 4),
    _CdpvmLoginDevVsan_Type()
)
cdpvmLoginDevVsan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdpvmLoginDevVsan.setStatus("current")
_CdpvmRowStatus_Type = RowStatus
_CdpvmRowStatus_Object = MibTableColumn
cdpvmRowStatus = _CdpvmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 2, 1, 5),
    _CdpvmRowStatus_Type()
)
cdpvmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdpvmRowStatus.setStatus("current")
_CdpvmActivate_Type = CpsmDbActivate
_CdpvmActivate_Object = MibScalar
cdpvmActivate = _CdpvmActivate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 3),
    _CdpvmActivate_Type()
)
cdpvmActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdpvmActivate.setStatus("current")
_CdpvmActivateResult_Type = CpsmActivateResult
_CdpvmActivateResult_Object = MibScalar
cdpvmActivateResult = _CdpvmActivateResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 4),
    _CdpvmActivateResult_Type()
)
cdpvmActivateResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpvmActivateResult.setStatus("current")
_CdpvmAutoLearn_Type = TruthValue
_CdpvmAutoLearn_Object = MibScalar
cdpvmAutoLearn = _CdpvmAutoLearn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 5),
    _CdpvmAutoLearn_Type()
)
cdpvmAutoLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdpvmAutoLearn.setStatus("current")


class _CdpvmCopyEnfToConfig_Type(Integer32):
    """Custom type cdpvmCopyEnfToConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copy", 1),
          ("noop", 2))
    )


_CdpvmCopyEnfToConfig_Type.__name__ = "Integer32"
_CdpvmCopyEnfToConfig_Object = MibScalar
cdpvmCopyEnfToConfig = _CdpvmCopyEnfToConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 6),
    _CdpvmCopyEnfToConfig_Type()
)
cdpvmCopyEnfToConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdpvmCopyEnfToConfig.setStatus("current")
_CdpvmEnfTable_Object = MibTable
cdpvmEnfTable = _CdpvmEnfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cdpvmEnfTable.setStatus("current")
_CdpvmEnfEntry_Object = MibTableRow
cdpvmEnfEntry = _CdpvmEnfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 7, 1)
)
cdpvmEnfEntry.setIndexNames(
    (0, "CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmEnfIndex"),
)
if mibBuilder.loadTexts:
    cdpvmEnfEntry.setStatus("current")


class _CdpvmEnfIndex_Type(Unsigned32):
    """Custom type cdpvmEnfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_CdpvmEnfIndex_Type.__name__ = "Unsigned32"
_CdpvmEnfIndex_Object = MibTableColumn
cdpvmEnfIndex = _CdpvmEnfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 7, 1, 1),
    _CdpvmEnfIndex_Type()
)
cdpvmEnfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdpvmEnfIndex.setStatus("current")
_CdpvmEnfLoginDevType_Type = CdpvmDevType
_CdpvmEnfLoginDevType_Object = MibTableColumn
cdpvmEnfLoginDevType = _CdpvmEnfLoginDevType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 7, 1, 2),
    _CdpvmEnfLoginDevType_Type()
)
cdpvmEnfLoginDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpvmEnfLoginDevType.setStatus("current")
_CdpvmEnfLoginDev_Type = FcNameId
_CdpvmEnfLoginDev_Object = MibTableColumn
cdpvmEnfLoginDev = _CdpvmEnfLoginDev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 7, 1, 3),
    _CdpvmEnfLoginDev_Type()
)
cdpvmEnfLoginDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpvmEnfLoginDev.setStatus("current")
_CdpvmEnfLoginDevVsan_Type = VsanIndex
_CdpvmEnfLoginDevVsan_Object = MibTableColumn
cdpvmEnfLoginDevVsan = _CdpvmEnfLoginDevVsan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 7, 1, 4),
    _CdpvmEnfLoginDevVsan_Type()
)
cdpvmEnfLoginDevVsan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpvmEnfLoginDevVsan.setStatus("current")
_CdpvmEnfIsLearnt_Type = TruthValue
_CdpvmEnfIsLearnt_Object = MibTableColumn
cdpvmEnfIsLearnt = _CdpvmEnfIsLearnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 7, 1, 5),
    _CdpvmEnfIsLearnt_Type()
)
cdpvmEnfIsLearnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpvmEnfIsLearnt.setStatus("current")
_CdpvmDynPortsTable_Object = MibTable
cdpvmDynPortsTable = _CdpvmDynPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cdpvmDynPortsTable.setStatus("current")
_CdpvmDynPortsEntry_Object = MibTableRow
cdpvmDynPortsEntry = _CdpvmDynPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 8, 1)
)
cdpvmDynPortsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cdpvmDynPortsEntry.setStatus("current")
_CdpvmDynPortVsan_Type = VsanIndex
_CdpvmDynPortVsan_Object = MibTableColumn
cdpvmDynPortVsan = _CdpvmDynPortVsan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 8, 1, 1),
    _CdpvmDynPortVsan_Type()
)
cdpvmDynPortVsan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpvmDynPortVsan.setStatus("current")
_CdpvmDynPortDevPwwn_Type = FcNameId
_CdpvmDynPortDevPwwn_Object = MibTableColumn
cdpvmDynPortDevPwwn = _CdpvmDynPortDevPwwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 8, 1, 2),
    _CdpvmDynPortDevPwwn_Type()
)
cdpvmDynPortDevPwwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpvmDynPortDevPwwn.setStatus("current")
_CdpvmDynPortDevNwwn_Type = FcNameId
_CdpvmDynPortDevNwwn_Object = MibTableColumn
cdpvmDynPortDevNwwn = _CdpvmDynPortDevNwwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 8, 1, 3),
    _CdpvmDynPortDevNwwn_Type()
)
cdpvmDynPortDevNwwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpvmDynPortDevNwwn.setStatus("current")
_CdpvmDiffConfig_Type = CpsmDiffDb
_CdpvmDiffConfig_Object = MibScalar
cdpvmDiffConfig = _CdpvmDiffConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 9),
    _CdpvmDiffConfig_Type()
)
cdpvmDiffConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdpvmDiffConfig.setStatus("current")
_CdpvmDiffTable_Object = MibTable
cdpvmDiffTable = _CdpvmDiffTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 10)
)
if mibBuilder.loadTexts:
    cdpvmDiffTable.setStatus("current")
_CdpvmDiffEntry_Object = MibTableRow
cdpvmDiffEntry = _CdpvmDiffEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 10, 1)
)
cdpvmDiffEntry.setIndexNames(
    (0, "CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmDiffIndex"),
)
if mibBuilder.loadTexts:
    cdpvmDiffEntry.setStatus("current")


class _CdpvmDiffIndex_Type(Unsigned32):
    """Custom type cdpvmDiffIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_CdpvmDiffIndex_Type.__name__ = "Unsigned32"
_CdpvmDiffIndex_Object = MibTableColumn
cdpvmDiffIndex = _CdpvmDiffIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 10, 1, 1),
    _CdpvmDiffIndex_Type()
)
cdpvmDiffIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdpvmDiffIndex.setStatus("current")
_CdpvmDiffReason_Type = CpsmDiffReason
_CdpvmDiffReason_Object = MibTableColumn
cdpvmDiffReason = _CdpvmDiffReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 10, 1, 2),
    _CdpvmDiffReason_Type()
)
cdpvmDiffReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpvmDiffReason.setStatus("current")
_CdpvmDiffLoginDevType_Type = CdpvmDevType
_CdpvmDiffLoginDevType_Object = MibTableColumn
cdpvmDiffLoginDevType = _CdpvmDiffLoginDevType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 10, 1, 3),
    _CdpvmDiffLoginDevType_Type()
)
cdpvmDiffLoginDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpvmDiffLoginDevType.setStatus("current")
_CdpvmDiffLoginDev_Type = FcNameId
_CdpvmDiffLoginDev_Object = MibTableColumn
cdpvmDiffLoginDev = _CdpvmDiffLoginDev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 10, 1, 4),
    _CdpvmDiffLoginDev_Type()
)
cdpvmDiffLoginDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpvmDiffLoginDev.setStatus("current")
_CdpvmDiffLoginDevVsan_Type = VsanIndex
_CdpvmDiffLoginDevVsan_Object = MibTableColumn
cdpvmDiffLoginDevVsan = _CdpvmDiffLoginDevVsan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 10, 1, 5),
    _CdpvmDiffLoginDevVsan_Type()
)
cdpvmDiffLoginDevVsan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpvmDiffLoginDevVsan.setStatus("current")


class _CdpvmClearAutoLearn_Type(Integer32):
    """Custom type cdpvmClearAutoLearn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("clearOnWwn", 2),
          ("noop", 3))
    )


_CdpvmClearAutoLearn_Type.__name__ = "Integer32"
_CdpvmClearAutoLearn_Object = MibScalar
cdpvmClearAutoLearn = _CdpvmClearAutoLearn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 11),
    _CdpvmClearAutoLearn_Type()
)
cdpvmClearAutoLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdpvmClearAutoLearn.setStatus("current")


class _CdpvmClearAutoLearnWwn_Type(FcNameIdOrZero):
    """Custom type cdpvmClearAutoLearnWwn based on FcNameIdOrZero"""
    defaultHexValue = ""


_CdpvmClearAutoLearnWwn_Object = MibScalar
cdpvmClearAutoLearnWwn = _CdpvmClearAutoLearnWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 12),
    _CdpvmClearAutoLearnWwn_Type()
)
cdpvmClearAutoLearnWwn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdpvmClearAutoLearnWwn.setStatus("current")
_CdpvmActivationState_Type = TruthValue
_CdpvmActivationState_Object = MibScalar
cdpvmActivationState = _CdpvmActivationState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 13),
    _CdpvmActivationState_Type()
)
cdpvmActivationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpvmActivationState.setStatus("current")
_CiscoDpvmMIBConform_ObjectIdentity = ObjectIdentity
ciscoDpvmMIBConform = _CiscoDpvmMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 2)
)
_CiscoDpvmMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDpvmMIBCompliances = _CiscoDpvmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 2, 1)
)
_CiscoDpvmMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDpvmMIBGroups = _CiscoDpvmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 2, 2)
)

# Managed Objects groups

ciscoDpvmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 2, 2, 1)
)
ciscoDpvmConfigGroup.setObjects(
      *(("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmNextAvailIndex"),
        ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmLoginDevType"),
        ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmLoginDev"),
        ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmLoginDevVsan"),
        ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmRowStatus"),
        ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmActivate"),
        ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmActivateResult"),
        ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmCopyEnfToConfig"),
        ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmDynPortVsan"),
        ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmDynPortDevPwwn"),
        ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmDynPortDevNwwn"),
        ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmActivationState"))
)
if mibBuilder.loadTexts:
    ciscoDpvmConfigGroup.setStatus("current")

ciscoDpvmEnforcedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 2, 2, 2)
)
ciscoDpvmEnforcedGroup.setObjects(
      *(("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmEnfLoginDevType"),
        ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmEnfLoginDev"),
        ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmEnfLoginDevVsan"),
        ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmEnfIsLearnt"))
)
if mibBuilder.loadTexts:
    ciscoDpvmEnforcedGroup.setStatus("current")

ciscoDpvmAutoLearnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 2, 2, 3)
)
ciscoDpvmAutoLearnGroup.setObjects(
      *(("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmAutoLearn"),
        ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmClearAutoLearn"),
        ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmClearAutoLearnWwn"))
)
if mibBuilder.loadTexts:
    ciscoDpvmAutoLearnGroup.setStatus("current")

ciscoDpvmDiffGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 2, 2, 4)
)
ciscoDpvmDiffGroup.setObjects(
      *(("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmDiffConfig"),
        ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmDiffReason"),
        ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmDiffLoginDevType"),
        ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmDiffLoginDev"),
        ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmDiffLoginDevVsan"))
)
if mibBuilder.loadTexts:
    ciscoDpvmDiffGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoDpvmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 421, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDpvmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DYNAMIC-PORT-VSAN-MIB",
    **{"CdpvmDevType": CdpvmDevType,
       "ciscoDpvmMIB": ciscoDpvmMIB,
       "ciscoDpvmMIBNotifs": ciscoDpvmMIBNotifs,
       "ciscoDpvmMIBObjects": ciscoDpvmMIBObjects,
       "cdpvmConfiguration": cdpvmConfiguration,
       "cdpvmNextAvailIndex": cdpvmNextAvailIndex,
       "cdpvmTable": cdpvmTable,
       "cdpvmEntry": cdpvmEntry,
       "cdpvmIndex": cdpvmIndex,
       "cdpvmLoginDevType": cdpvmLoginDevType,
       "cdpvmLoginDev": cdpvmLoginDev,
       "cdpvmLoginDevVsan": cdpvmLoginDevVsan,
       "cdpvmRowStatus": cdpvmRowStatus,
       "cdpvmActivate": cdpvmActivate,
       "cdpvmActivateResult": cdpvmActivateResult,
       "cdpvmAutoLearn": cdpvmAutoLearn,
       "cdpvmCopyEnfToConfig": cdpvmCopyEnfToConfig,
       "cdpvmEnfTable": cdpvmEnfTable,
       "cdpvmEnfEntry": cdpvmEnfEntry,
       "cdpvmEnfIndex": cdpvmEnfIndex,
       "cdpvmEnfLoginDevType": cdpvmEnfLoginDevType,
       "cdpvmEnfLoginDev": cdpvmEnfLoginDev,
       "cdpvmEnfLoginDevVsan": cdpvmEnfLoginDevVsan,
       "cdpvmEnfIsLearnt": cdpvmEnfIsLearnt,
       "cdpvmDynPortsTable": cdpvmDynPortsTable,
       "cdpvmDynPortsEntry": cdpvmDynPortsEntry,
       "cdpvmDynPortVsan": cdpvmDynPortVsan,
       "cdpvmDynPortDevPwwn": cdpvmDynPortDevPwwn,
       "cdpvmDynPortDevNwwn": cdpvmDynPortDevNwwn,
       "cdpvmDiffConfig": cdpvmDiffConfig,
       "cdpvmDiffTable": cdpvmDiffTable,
       "cdpvmDiffEntry": cdpvmDiffEntry,
       "cdpvmDiffIndex": cdpvmDiffIndex,
       "cdpvmDiffReason": cdpvmDiffReason,
       "cdpvmDiffLoginDevType": cdpvmDiffLoginDevType,
       "cdpvmDiffLoginDev": cdpvmDiffLoginDev,
       "cdpvmDiffLoginDevVsan": cdpvmDiffLoginDevVsan,
       "cdpvmClearAutoLearn": cdpvmClearAutoLearn,
       "cdpvmClearAutoLearnWwn": cdpvmClearAutoLearnWwn,
       "cdpvmActivationState": cdpvmActivationState,
       "ciscoDpvmMIBConform": ciscoDpvmMIBConform,
       "ciscoDpvmMIBCompliances": ciscoDpvmMIBCompliances,
       "ciscoDpvmMIBCompliance": ciscoDpvmMIBCompliance,
       "ciscoDpvmMIBGroups": ciscoDpvmMIBGroups,
       "ciscoDpvmConfigGroup": ciscoDpvmConfigGroup,
       "ciscoDpvmEnforcedGroup": ciscoDpvmEnforcedGroup,
       "ciscoDpvmAutoLearnGroup": ciscoDpvmAutoLearnGroup,
       "ciscoDpvmDiffGroup": ciscoDpvmDiffGroup}
)
