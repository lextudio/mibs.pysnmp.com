# SNMP MIB module (HPN-ICF-VSAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-VSAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:15 2024
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

(HpnicfFcDmState,
 HpnicfFcDomainId,
 HpnicfFcDomainIdList,
 HpnicfFcDomainIdOrZero,
 HpnicfFcDomainPriority,
 HpnicfFcNameId,
 HpnicfFcNameIdOrZero,
 HpnicfFcVsanIndex) = mibBuilder.importSymbols(
    "HPN-ICF-FC-TC-MIB",
    "HpnicfFcDmState",
    "HpnicfFcDomainId",
    "HpnicfFcDomainIdList",
    "HpnicfFcDomainIdOrZero",
    "HpnicfFcDomainPriority",
    "HpnicfFcNameId",
    "HpnicfFcNameIdOrZero",
    "HpnicfFcVsanIndex")

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpnicfSan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127)
)
hpnicfSan.setRevisions(
        ("2014-03-04 15:50",
         "2013-02-28 09:40")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfVsan_ObjectIdentity = ObjectIdentity
hpnicfVsan = _HpnicfVsan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1)
)
_HpnicfVsanMibObjects_ObjectIdentity = ObjectIdentity
hpnicfVsanMibObjects = _HpnicfVsanMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1)
)
_HpnicfVsanDmConfiguration_ObjectIdentity = ObjectIdentity
hpnicfVsanDmConfiguration = _HpnicfVsanDmConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1)
)
_HpnicfVsanTable_Object = MibTable
hpnicfVsanTable = _HpnicfVsanTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfVsanTable.setStatus("current")
_HpnicfVsanEntry_Object = MibTableRow
hpnicfVsanEntry = _HpnicfVsanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1, 1, 1)
)
hpnicfVsanEntry.setIndexNames(
    (0, "HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
)
if mibBuilder.loadTexts:
    hpnicfVsanEntry.setStatus("current")
_HpnicfVsanIndex_Type = HpnicfFcVsanIndex
_HpnicfVsanIndex_Object = MibTableColumn
hpnicfVsanIndex = _HpnicfVsanIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1, 1, 1, 1),
    _HpnicfVsanIndex_Type()
)
hpnicfVsanIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfVsanIndex.setStatus("current")


class _HpnicfVsanCoreSwitchName_Type(HpnicfFcNameIdOrZero):
    """Custom type hpnicfVsanCoreSwitchName based on HpnicfFcNameIdOrZero"""
    subtypeSpec = HpnicfFcNameIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
    )


_HpnicfVsanCoreSwitchName_Type.__name__ = "HpnicfFcNameIdOrZero"
_HpnicfVsanCoreSwitchName_Object = MibTableColumn
hpnicfVsanCoreSwitchName = _HpnicfVsanCoreSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1, 1, 1, 2),
    _HpnicfVsanCoreSwitchName_Type()
)
hpnicfVsanCoreSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsanCoreSwitchName.setStatus("current")
_HpnicfVsanRowStatus_Type = RowStatus
_HpnicfVsanRowStatus_Object = MibTableColumn
hpnicfVsanRowStatus = _HpnicfVsanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1, 1, 1, 3),
    _HpnicfVsanRowStatus_Type()
)
hpnicfVsanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVsanRowStatus.setStatus("current")
_HpnicfVsanDmTable_Object = MibTable
hpnicfVsanDmTable = _HpnicfVsanDmTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfVsanDmTable.setStatus("current")
_HpnicfVsanDmEntry_Object = MibTableRow
hpnicfVsanDmEntry = _HpnicfVsanDmEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1, 2, 1)
)
hpnicfVsanDmEntry.setIndexNames(
    (0, "HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
)
if mibBuilder.loadTexts:
    hpnicfVsanDmEntry.setStatus("current")


class _HpnicfVsanDmDomainConfigureEnable_Type(TruthValue):
    """Custom type hpnicfVsanDmDomainConfigureEnable based on TruthValue"""


_HpnicfVsanDmDomainConfigureEnable_Object = MibTableColumn
hpnicfVsanDmDomainConfigureEnable = _HpnicfVsanDmDomainConfigureEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1, 2, 1, 1),
    _HpnicfVsanDmDomainConfigureEnable_Type()
)
hpnicfVsanDmDomainConfigureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVsanDmDomainConfigureEnable.setStatus("current")
_HpnicfVsanDmFabricNameConfigured_Type = HpnicfFcNameIdOrZero
_HpnicfVsanDmFabricNameConfigured_Object = MibTableColumn
hpnicfVsanDmFabricNameConfigured = _HpnicfVsanDmFabricNameConfigured_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1, 2, 1, 2),
    _HpnicfVsanDmFabricNameConfigured_Type()
)
hpnicfVsanDmFabricNameConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVsanDmFabricNameConfigured.setStatus("current")


class _HpnicfVsanDmPriorityConfigured_Type(HpnicfFcDomainPriority):
    """Custom type hpnicfVsanDmPriorityConfigured based on HpnicfFcDomainPriority"""
    defaultValue = 128


_HpnicfVsanDmPriorityConfigured_Object = MibTableColumn
hpnicfVsanDmPriorityConfigured = _HpnicfVsanDmPriorityConfigured_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1, 2, 1, 3),
    _HpnicfVsanDmPriorityConfigured_Type()
)
hpnicfVsanDmPriorityConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVsanDmPriorityConfigured.setStatus("current")
_HpnicfVsanDmAllowedDomainIdList_Type = HpnicfFcDomainIdList
_HpnicfVsanDmAllowedDomainIdList_Object = MibTableColumn
hpnicfVsanDmAllowedDomainIdList = _HpnicfVsanDmAllowedDomainIdList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1, 2, 1, 4),
    _HpnicfVsanDmAllowedDomainIdList_Type()
)
hpnicfVsanDmAllowedDomainIdList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVsanDmAllowedDomainIdList.setStatus("current")


class _HpnicfVsanDmDomainIdConfigured_Type(HpnicfFcDomainIdOrZero):
    """Custom type hpnicfVsanDmDomainIdConfigured based on HpnicfFcDomainIdOrZero"""
    defaultValue = 0


_HpnicfVsanDmDomainIdConfigured_Object = MibTableColumn
hpnicfVsanDmDomainIdConfigured = _HpnicfVsanDmDomainIdConfigured_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1, 2, 1, 5),
    _HpnicfVsanDmDomainIdConfigured_Type()
)
hpnicfVsanDmDomainIdConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVsanDmDomainIdConfigured.setStatus("current")


class _HpnicfVsanDmDomainIdTypeConfigured_Type(Integer32):
    """Custom type hpnicfVsanDmDomainIdTypeConfigured based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("preferred", 2),
          ("static", 1))
    )


_HpnicfVsanDmDomainIdTypeConfigured_Type.__name__ = "Integer32"
_HpnicfVsanDmDomainIdTypeConfigured_Object = MibTableColumn
hpnicfVsanDmDomainIdTypeConfigured = _HpnicfVsanDmDomainIdTypeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1, 2, 1, 6),
    _HpnicfVsanDmDomainIdTypeConfigured_Type()
)
hpnicfVsanDmDomainIdTypeConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVsanDmDomainIdTypeConfigured.setStatus("current")


class _HpnicfVsanDmAutoReconfigureEnable_Type(TruthValue):
    """Custom type hpnicfVsanDmAutoReconfigureEnable based on TruthValue"""


_HpnicfVsanDmAutoReconfigureEnable_Object = MibTableColumn
hpnicfVsanDmAutoReconfigureEnable = _HpnicfVsanDmAutoReconfigureEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1, 2, 1, 7),
    _HpnicfVsanDmAutoReconfigureEnable_Type()
)
hpnicfVsanDmAutoReconfigureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVsanDmAutoReconfigureEnable.setStatus("current")


class _HpnicfVsanDmDomainRestart_Type(Integer32):
    """Custom type hpnicfVsanDmDomainRestart based on Integer32"""
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
        *(("disruptive", 3),
          ("noOperation", 1),
          ("nonDisruptive", 2))
    )


_HpnicfVsanDmDomainRestart_Type.__name__ = "Integer32"
_HpnicfVsanDmDomainRestart_Object = MibTableColumn
hpnicfVsanDmDomainRestart = _HpnicfVsanDmDomainRestart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1, 2, 1, 8),
    _HpnicfVsanDmDomainRestart_Type()
)
hpnicfVsanDmDomainRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVsanDmDomainRestart.setStatus("current")
_HpnicfVsanDmState_Type = HpnicfFcDmState
_HpnicfVsanDmState_Object = MibTableColumn
hpnicfVsanDmState = _HpnicfVsanDmState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1, 2, 1, 9),
    _HpnicfVsanDmState_Type()
)
hpnicfVsanDmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsanDmState.setStatus("current")
_HpnicfVsanDmDomainIdAssigned_Type = HpnicfFcDomainIdOrZero
_HpnicfVsanDmDomainIdAssigned_Object = MibTableColumn
hpnicfVsanDmDomainIdAssigned = _HpnicfVsanDmDomainIdAssigned_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1, 2, 1, 10),
    _HpnicfVsanDmDomainIdAssigned_Type()
)
hpnicfVsanDmDomainIdAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsanDmDomainIdAssigned.setStatus("current")
_HpnicfVsanDmPrincipalSwitchWWN_Type = HpnicfFcNameId
_HpnicfVsanDmPrincipalSwitchWWN_Object = MibTableColumn
hpnicfVsanDmPrincipalSwitchWWN = _HpnicfVsanDmPrincipalSwitchWWN_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1, 2, 1, 11),
    _HpnicfVsanDmPrincipalSwitchWWN_Type()
)
hpnicfVsanDmPrincipalSwitchWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsanDmPrincipalSwitchWWN.setStatus("current")
_HpnicfVsanDmLocalSwitchWWN_Type = HpnicfFcNameId
_HpnicfVsanDmLocalSwitchWWN_Object = MibTableColumn
hpnicfVsanDmLocalSwitchWWN = _HpnicfVsanDmLocalSwitchWWN_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1, 2, 1, 12),
    _HpnicfVsanDmLocalSwitchWWN_Type()
)
hpnicfVsanDmLocalSwitchWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsanDmLocalSwitchWWN.setStatus("current")
_HpnicfVsanDmPrincipalSwRunPriority_Type = HpnicfFcDomainPriority
_HpnicfVsanDmPrincipalSwRunPriority_Object = MibTableColumn
hpnicfVsanDmPrincipalSwRunPriority = _HpnicfVsanDmPrincipalSwRunPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1, 2, 1, 13),
    _HpnicfVsanDmPrincipalSwRunPriority_Type()
)
hpnicfVsanDmPrincipalSwRunPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsanDmPrincipalSwRunPriority.setStatus("current")
_HpnicfVsanDmLocalSwRunPriority_Type = HpnicfFcDomainPriority
_HpnicfVsanDmLocalSwRunPriority_Object = MibTableColumn
hpnicfVsanDmLocalSwRunPriority = _HpnicfVsanDmLocalSwRunPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1, 2, 1, 14),
    _HpnicfVsanDmLocalSwRunPriority_Type()
)
hpnicfVsanDmLocalSwRunPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsanDmLocalSwRunPriority.setStatus("current")
_HpnicfVsanDmPrincipalSwSlctCnt_Type = Counter32
_HpnicfVsanDmPrincipalSwSlctCnt_Object = MibTableColumn
hpnicfVsanDmPrincipalSwSlctCnt = _HpnicfVsanDmPrincipalSwSlctCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1, 2, 1, 15),
    _HpnicfVsanDmPrincipalSwSlctCnt_Type()
)
hpnicfVsanDmPrincipalSwSlctCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsanDmPrincipalSwSlctCnt.setStatus("current")
_HpnicfVsanDmLocalPrincipalSwSlctCnt_Type = Counter32
_HpnicfVsanDmLocalPrincipalSwSlctCnt_Object = MibTableColumn
hpnicfVsanDmLocalPrincipalSwSlctCnt = _HpnicfVsanDmLocalPrincipalSwSlctCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1, 2, 1, 16),
    _HpnicfVsanDmLocalPrincipalSwSlctCnt_Type()
)
hpnicfVsanDmLocalPrincipalSwSlctCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsanDmLocalPrincipalSwSlctCnt.setStatus("current")
_HpnicfVsanDmBFCnt_Type = Counter32
_HpnicfVsanDmBFCnt_Object = MibTableColumn
hpnicfVsanDmBFCnt = _HpnicfVsanDmBFCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1, 2, 1, 17),
    _HpnicfVsanDmBFCnt_Type()
)
hpnicfVsanDmBFCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsanDmBFCnt.setStatus("current")
_HpnicfVsanDmRCFCnt_Type = Counter32
_HpnicfVsanDmRCFCnt_Object = MibTableColumn
hpnicfVsanDmRCFCnt = _HpnicfVsanDmRCFCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1, 2, 1, 18),
    _HpnicfVsanDmRCFCnt_Type()
)
hpnicfVsanDmRCFCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsanDmRCFCnt.setStatus("current")
_HpnicfVsanDmIfConfigTable_Object = MibTable
hpnicfVsanDmIfConfigTable = _HpnicfVsanDmIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfVsanDmIfConfigTable.setStatus("current")
_HpnicfVsanDmIfConfigEntry_Object = MibTableRow
hpnicfVsanDmIfConfigEntry = _HpnicfVsanDmIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1, 3, 1)
)
hpnicfVsanDmIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
)
if mibBuilder.loadTexts:
    hpnicfVsanDmIfConfigEntry.setStatus("current")


class _HpnicfVsanDmIfConfigRcfReject_Type(TruthValue):
    """Custom type hpnicfVsanDmIfConfigRcfReject based on TruthValue"""


_HpnicfVsanDmIfConfigRcfReject_Object = MibTableColumn
hpnicfVsanDmIfConfigRcfReject = _HpnicfVsanDmIfConfigRcfReject_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 1, 3, 1, 1),
    _HpnicfVsanDmIfConfigRcfReject_Type()
)
hpnicfVsanDmIfConfigRcfReject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVsanDmIfConfigRcfReject.setStatus("current")
_HpnicfVsanDmInformation_ObjectIdentity = ObjectIdentity
hpnicfVsanDmInformation = _HpnicfVsanDmInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 2)
)
_HpnicfVsanDmDatabaseTable_Object = MibTable
hpnicfVsanDmDatabaseTable = _HpnicfVsanDmDatabaseTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfVsanDmDatabaseTable.setStatus("current")
_HpnicfVsanDmDatabaseEntry_Object = MibTableRow
hpnicfVsanDmDatabaseEntry = _HpnicfVsanDmDatabaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 2, 1, 1)
)
hpnicfVsanDmDatabaseEntry.setIndexNames(
    (0, "HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
    (0, "HPN-ICF-VSAN-MIB", "hpnicfVsanDmDatabaseDomainId"),
)
if mibBuilder.loadTexts:
    hpnicfVsanDmDatabaseEntry.setStatus("current")
_HpnicfVsanDmDatabaseDomainId_Type = HpnicfFcDomainId
_HpnicfVsanDmDatabaseDomainId_Object = MibTableColumn
hpnicfVsanDmDatabaseDomainId = _HpnicfVsanDmDatabaseDomainId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 2, 1, 1, 1),
    _HpnicfVsanDmDatabaseDomainId_Type()
)
hpnicfVsanDmDatabaseDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfVsanDmDatabaseDomainId.setStatus("current")
_HpnicfVsanDmDatabaseSwitchWWN_Type = HpnicfFcNameId
_HpnicfVsanDmDatabaseSwitchWWN_Object = MibTableColumn
hpnicfVsanDmDatabaseSwitchWWN = _HpnicfVsanDmDatabaseSwitchWWN_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 2, 1, 1, 2),
    _HpnicfVsanDmDatabaseSwitchWWN_Type()
)
hpnicfVsanDmDatabaseSwitchWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsanDmDatabaseSwitchWWN.setStatus("current")
_HpnicfVsanDmIfInfoTable_Object = MibTable
hpnicfVsanDmIfInfoTable = _HpnicfVsanDmIfInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfVsanDmIfInfoTable.setStatus("current")
_HpnicfVsanDmIfInfoEntry_Object = MibTableRow
hpnicfVsanDmIfInfoEntry = _HpnicfVsanDmIfInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 2, 2, 1)
)
hpnicfVsanDmIfInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
)
if mibBuilder.loadTexts:
    hpnicfVsanDmIfInfoEntry.setStatus("current")


class _HpnicfVsanDmIfInfoRole_Type(Integer32):
    """Custom type hpnicfVsanDmIfInfoRole based on Integer32"""
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
        *(("isolated", 4),
          ("nonPrincipal", 1),
          ("principalDownstream", 3),
          ("principalUpstream", 2),
          ("unknown", 5))
    )


_HpnicfVsanDmIfInfoRole_Type.__name__ = "Integer32"
_HpnicfVsanDmIfInfoRole_Object = MibTableColumn
hpnicfVsanDmIfInfoRole = _HpnicfVsanDmIfInfoRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 2, 2, 1, 1),
    _HpnicfVsanDmIfInfoRole_Type()
)
hpnicfVsanDmIfInfoRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsanDmIfInfoRole.setStatus("current")
_HpnicfVsanDmNotifications_ObjectIdentity = ObjectIdentity
hpnicfVsanDmNotifications = _HpnicfVsanDmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 3)
)
_HpnicfVsanDmNotificationPrefix_ObjectIdentity = ObjectIdentity
hpnicfVsanDmNotificationPrefix = _HpnicfVsanDmNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 3, 0)
)
_HpnicfVsanDmNotificationSwitch_ObjectIdentity = ObjectIdentity
hpnicfVsanDmNotificationSwitch = _HpnicfVsanDmNotificationSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 3, 1)
)


class _HpnicfVsanDmFabricChangeNotifyEnable_Type(TruthValue):
    """Custom type hpnicfVsanDmFabricChangeNotifyEnable based on TruthValue"""


_HpnicfVsanDmFabricChangeNotifyEnable_Object = MibScalar
hpnicfVsanDmFabricChangeNotifyEnable = _HpnicfVsanDmFabricChangeNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 3, 1, 1),
    _HpnicfVsanDmFabricChangeNotifyEnable_Type()
)
hpnicfVsanDmFabricChangeNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVsanDmFabricChangeNotifyEnable.setStatus("current")


class _HpnicfVsanDmDomainIdChangeNotifyEnable_Type(TruthValue):
    """Custom type hpnicfVsanDmDomainIdChangeNotifyEnable based on TruthValue"""


_HpnicfVsanDmDomainIdChangeNotifyEnable_Object = MibScalar
hpnicfVsanDmDomainIdChangeNotifyEnable = _HpnicfVsanDmDomainIdChangeNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 3, 1, 2),
    _HpnicfVsanDmDomainIdChangeNotifyEnable_Type()
)
hpnicfVsanDmDomainIdChangeNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVsanDmDomainIdChangeNotifyEnable.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfVsanDmDomainIdNotAssignedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 3, 0, 1)
)
hpnicfVsanDmDomainIdNotAssignedNotify.setObjects(
      *(("HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
        ("HPN-ICF-VSAN-MIB", "hpnicfVsanDmLocalSwitchWWN"))
)
if mibBuilder.loadTexts:
    hpnicfVsanDmDomainIdNotAssignedNotify.setStatus(
        "current"
    )

hpnicfVsanDmNewPrincipalSwitchNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 3, 0, 2)
)
hpnicfVsanDmNewPrincipalSwitchNotify.setObjects(
      *(("HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
        ("HPN-ICF-VSAN-MIB", "hpnicfVsanDmLocalSwitchWWN"))
)
if mibBuilder.loadTexts:
    hpnicfVsanDmNewPrincipalSwitchNotify.setStatus(
        "current"
    )

hpnicfVsanDmFabricChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 3, 0, 3)
)
hpnicfVsanDmFabricChangeNotify.setObjects(
    ("HPN-ICF-VSAN-MIB", "hpnicfVsanIndex")
)
if mibBuilder.loadTexts:
    hpnicfVsanDmFabricChangeNotify.setStatus(
        "current"
    )

hpnicfVsanDmDomainIdChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 1, 1, 3, 0, 4)
)
hpnicfVsanDmDomainIdChangeNotify.setObjects(
      *(("HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
        ("HPN-ICF-VSAN-MIB", "hpnicfVsanDmDomainIdAssigned"),
        ("HPN-ICF-VSAN-MIB", "hpnicfVsanDmLocalSwitchWWN"))
)
if mibBuilder.loadTexts:
    hpnicfVsanDmDomainIdChangeNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-VSAN-MIB",
    **{"hpnicfSan": hpnicfSan,
       "hpnicfVsan": hpnicfVsan,
       "hpnicfVsanMibObjects": hpnicfVsanMibObjects,
       "hpnicfVsanDmConfiguration": hpnicfVsanDmConfiguration,
       "hpnicfVsanTable": hpnicfVsanTable,
       "hpnicfVsanEntry": hpnicfVsanEntry,
       "hpnicfVsanIndex": hpnicfVsanIndex,
       "hpnicfVsanCoreSwitchName": hpnicfVsanCoreSwitchName,
       "hpnicfVsanRowStatus": hpnicfVsanRowStatus,
       "hpnicfVsanDmTable": hpnicfVsanDmTable,
       "hpnicfVsanDmEntry": hpnicfVsanDmEntry,
       "hpnicfVsanDmDomainConfigureEnable": hpnicfVsanDmDomainConfigureEnable,
       "hpnicfVsanDmFabricNameConfigured": hpnicfVsanDmFabricNameConfigured,
       "hpnicfVsanDmPriorityConfigured": hpnicfVsanDmPriorityConfigured,
       "hpnicfVsanDmAllowedDomainIdList": hpnicfVsanDmAllowedDomainIdList,
       "hpnicfVsanDmDomainIdConfigured": hpnicfVsanDmDomainIdConfigured,
       "hpnicfVsanDmDomainIdTypeConfigured": hpnicfVsanDmDomainIdTypeConfigured,
       "hpnicfVsanDmAutoReconfigureEnable": hpnicfVsanDmAutoReconfigureEnable,
       "hpnicfVsanDmDomainRestart": hpnicfVsanDmDomainRestart,
       "hpnicfVsanDmState": hpnicfVsanDmState,
       "hpnicfVsanDmDomainIdAssigned": hpnicfVsanDmDomainIdAssigned,
       "hpnicfVsanDmPrincipalSwitchWWN": hpnicfVsanDmPrincipalSwitchWWN,
       "hpnicfVsanDmLocalSwitchWWN": hpnicfVsanDmLocalSwitchWWN,
       "hpnicfVsanDmPrincipalSwRunPriority": hpnicfVsanDmPrincipalSwRunPriority,
       "hpnicfVsanDmLocalSwRunPriority": hpnicfVsanDmLocalSwRunPriority,
       "hpnicfVsanDmPrincipalSwSlctCnt": hpnicfVsanDmPrincipalSwSlctCnt,
       "hpnicfVsanDmLocalPrincipalSwSlctCnt": hpnicfVsanDmLocalPrincipalSwSlctCnt,
       "hpnicfVsanDmBFCnt": hpnicfVsanDmBFCnt,
       "hpnicfVsanDmRCFCnt": hpnicfVsanDmRCFCnt,
       "hpnicfVsanDmIfConfigTable": hpnicfVsanDmIfConfigTable,
       "hpnicfVsanDmIfConfigEntry": hpnicfVsanDmIfConfigEntry,
       "hpnicfVsanDmIfConfigRcfReject": hpnicfVsanDmIfConfigRcfReject,
       "hpnicfVsanDmInformation": hpnicfVsanDmInformation,
       "hpnicfVsanDmDatabaseTable": hpnicfVsanDmDatabaseTable,
       "hpnicfVsanDmDatabaseEntry": hpnicfVsanDmDatabaseEntry,
       "hpnicfVsanDmDatabaseDomainId": hpnicfVsanDmDatabaseDomainId,
       "hpnicfVsanDmDatabaseSwitchWWN": hpnicfVsanDmDatabaseSwitchWWN,
       "hpnicfVsanDmIfInfoTable": hpnicfVsanDmIfInfoTable,
       "hpnicfVsanDmIfInfoEntry": hpnicfVsanDmIfInfoEntry,
       "hpnicfVsanDmIfInfoRole": hpnicfVsanDmIfInfoRole,
       "hpnicfVsanDmNotifications": hpnicfVsanDmNotifications,
       "hpnicfVsanDmNotificationPrefix": hpnicfVsanDmNotificationPrefix,
       "hpnicfVsanDmDomainIdNotAssignedNotify": hpnicfVsanDmDomainIdNotAssignedNotify,
       "hpnicfVsanDmNewPrincipalSwitchNotify": hpnicfVsanDmNewPrincipalSwitchNotify,
       "hpnicfVsanDmFabricChangeNotify": hpnicfVsanDmFabricChangeNotify,
       "hpnicfVsanDmDomainIdChangeNotify": hpnicfVsanDmDomainIdChangeNotify,
       "hpnicfVsanDmNotificationSwitch": hpnicfVsanDmNotificationSwitch,
       "hpnicfVsanDmFabricChangeNotifyEnable": hpnicfVsanDmFabricChangeNotifyEnable,
       "hpnicfVsanDmDomainIdChangeNotifyEnable": hpnicfVsanDmDomainIdChangeNotifyEnable}
)
