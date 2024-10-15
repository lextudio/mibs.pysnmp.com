# SNMP MIB module (HH3C-VSAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-VSAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:15 2024
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

(Hh3cFcDmState,
 Hh3cFcDomainId,
 Hh3cFcDomainIdList,
 Hh3cFcDomainIdOrZero,
 Hh3cFcDomainPriority,
 Hh3cFcNameId,
 Hh3cFcNameIdOrZero,
 Hh3cFcVsanIndex) = mibBuilder.importSymbols(
    "HH3C-FC-TC-MIB",
    "Hh3cFcDmState",
    "Hh3cFcDomainId",
    "Hh3cFcDomainIdList",
    "Hh3cFcDomainIdOrZero",
    "Hh3cFcDomainPriority",
    "Hh3cFcNameId",
    "Hh3cFcNameIdOrZero",
    "Hh3cFcVsanIndex")

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cSan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127)
)
hh3cSan.setRevisions(
        ("2014-03-04 15:50",
         "2013-02-28 09:40")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cVsan_ObjectIdentity = ObjectIdentity
hh3cVsan = _Hh3cVsan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1)
)
_Hh3cVsanMibObjects_ObjectIdentity = ObjectIdentity
hh3cVsanMibObjects = _Hh3cVsanMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1)
)
_Hh3cVsanDmConfiguration_ObjectIdentity = ObjectIdentity
hh3cVsanDmConfiguration = _Hh3cVsanDmConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1)
)
_Hh3cVsanTable_Object = MibTable
hh3cVsanTable = _Hh3cVsanTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cVsanTable.setStatus("current")
_Hh3cVsanEntry_Object = MibTableRow
hh3cVsanEntry = _Hh3cVsanEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 1, 1)
)
hh3cVsanEntry.setIndexNames(
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
)
if mibBuilder.loadTexts:
    hh3cVsanEntry.setStatus("current")
_Hh3cVsanIndex_Type = Hh3cFcVsanIndex
_Hh3cVsanIndex_Object = MibTableColumn
hh3cVsanIndex = _Hh3cVsanIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 1, 1, 1),
    _Hh3cVsanIndex_Type()
)
hh3cVsanIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVsanIndex.setStatus("current")


class _Hh3cVsanCoreSwitchName_Type(Hh3cFcNameIdOrZero):
    """Custom type hh3cVsanCoreSwitchName based on Hh3cFcNameIdOrZero"""
    subtypeSpec = Hh3cFcNameIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
    )


_Hh3cVsanCoreSwitchName_Type.__name__ = "Hh3cFcNameIdOrZero"
_Hh3cVsanCoreSwitchName_Object = MibTableColumn
hh3cVsanCoreSwitchName = _Hh3cVsanCoreSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 1, 1, 2),
    _Hh3cVsanCoreSwitchName_Type()
)
hh3cVsanCoreSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanCoreSwitchName.setStatus("current")
_Hh3cVsanRowStatus_Type = RowStatus
_Hh3cVsanRowStatus_Object = MibTableColumn
hh3cVsanRowStatus = _Hh3cVsanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 1, 1, 3),
    _Hh3cVsanRowStatus_Type()
)
hh3cVsanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsanRowStatus.setStatus("current")
_Hh3cVsanDmTable_Object = MibTable
hh3cVsanDmTable = _Hh3cVsanDmTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cVsanDmTable.setStatus("current")
_Hh3cVsanDmEntry_Object = MibTableRow
hh3cVsanDmEntry = _Hh3cVsanDmEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1)
)
hh3cVsanDmEntry.setIndexNames(
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
)
if mibBuilder.loadTexts:
    hh3cVsanDmEntry.setStatus("current")


class _Hh3cVsanDmDomainConfigureEnable_Type(TruthValue):
    """Custom type hh3cVsanDmDomainConfigureEnable based on TruthValue"""


_Hh3cVsanDmDomainConfigureEnable_Object = MibTableColumn
hh3cVsanDmDomainConfigureEnable = _Hh3cVsanDmDomainConfigureEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 1),
    _Hh3cVsanDmDomainConfigureEnable_Type()
)
hh3cVsanDmDomainConfigureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVsanDmDomainConfigureEnable.setStatus("current")
_Hh3cVsanDmFabricNameConfigured_Type = Hh3cFcNameIdOrZero
_Hh3cVsanDmFabricNameConfigured_Object = MibTableColumn
hh3cVsanDmFabricNameConfigured = _Hh3cVsanDmFabricNameConfigured_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 2),
    _Hh3cVsanDmFabricNameConfigured_Type()
)
hh3cVsanDmFabricNameConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVsanDmFabricNameConfigured.setStatus("current")


class _Hh3cVsanDmPriorityConfigured_Type(Hh3cFcDomainPriority):
    """Custom type hh3cVsanDmPriorityConfigured based on Hh3cFcDomainPriority"""
    defaultValue = 128


_Hh3cVsanDmPriorityConfigured_Object = MibTableColumn
hh3cVsanDmPriorityConfigured = _Hh3cVsanDmPriorityConfigured_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 3),
    _Hh3cVsanDmPriorityConfigured_Type()
)
hh3cVsanDmPriorityConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVsanDmPriorityConfigured.setStatus("current")
_Hh3cVsanDmAllowedDomainIdList_Type = Hh3cFcDomainIdList
_Hh3cVsanDmAllowedDomainIdList_Object = MibTableColumn
hh3cVsanDmAllowedDomainIdList = _Hh3cVsanDmAllowedDomainIdList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 4),
    _Hh3cVsanDmAllowedDomainIdList_Type()
)
hh3cVsanDmAllowedDomainIdList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVsanDmAllowedDomainIdList.setStatus("current")


class _Hh3cVsanDmDomainIdConfigured_Type(Hh3cFcDomainIdOrZero):
    """Custom type hh3cVsanDmDomainIdConfigured based on Hh3cFcDomainIdOrZero"""
    defaultValue = 0


_Hh3cVsanDmDomainIdConfigured_Object = MibTableColumn
hh3cVsanDmDomainIdConfigured = _Hh3cVsanDmDomainIdConfigured_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 5),
    _Hh3cVsanDmDomainIdConfigured_Type()
)
hh3cVsanDmDomainIdConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVsanDmDomainIdConfigured.setStatus("current")


class _Hh3cVsanDmDomainIdTypeConfigured_Type(Integer32):
    """Custom type hh3cVsanDmDomainIdTypeConfigured based on Integer32"""
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


_Hh3cVsanDmDomainIdTypeConfigured_Type.__name__ = "Integer32"
_Hh3cVsanDmDomainIdTypeConfigured_Object = MibTableColumn
hh3cVsanDmDomainIdTypeConfigured = _Hh3cVsanDmDomainIdTypeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 6),
    _Hh3cVsanDmDomainIdTypeConfigured_Type()
)
hh3cVsanDmDomainIdTypeConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVsanDmDomainIdTypeConfigured.setStatus("current")


class _Hh3cVsanDmAutoReconfigureEnable_Type(TruthValue):
    """Custom type hh3cVsanDmAutoReconfigureEnable based on TruthValue"""


_Hh3cVsanDmAutoReconfigureEnable_Object = MibTableColumn
hh3cVsanDmAutoReconfigureEnable = _Hh3cVsanDmAutoReconfigureEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 7),
    _Hh3cVsanDmAutoReconfigureEnable_Type()
)
hh3cVsanDmAutoReconfigureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVsanDmAutoReconfigureEnable.setStatus("current")


class _Hh3cVsanDmDomainRestart_Type(Integer32):
    """Custom type hh3cVsanDmDomainRestart based on Integer32"""
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


_Hh3cVsanDmDomainRestart_Type.__name__ = "Integer32"
_Hh3cVsanDmDomainRestart_Object = MibTableColumn
hh3cVsanDmDomainRestart = _Hh3cVsanDmDomainRestart_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 8),
    _Hh3cVsanDmDomainRestart_Type()
)
hh3cVsanDmDomainRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVsanDmDomainRestart.setStatus("current")
_Hh3cVsanDmState_Type = Hh3cFcDmState
_Hh3cVsanDmState_Object = MibTableColumn
hh3cVsanDmState = _Hh3cVsanDmState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 9),
    _Hh3cVsanDmState_Type()
)
hh3cVsanDmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanDmState.setStatus("current")
_Hh3cVsanDmDomainIdAssigned_Type = Hh3cFcDomainIdOrZero
_Hh3cVsanDmDomainIdAssigned_Object = MibTableColumn
hh3cVsanDmDomainIdAssigned = _Hh3cVsanDmDomainIdAssigned_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 10),
    _Hh3cVsanDmDomainIdAssigned_Type()
)
hh3cVsanDmDomainIdAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanDmDomainIdAssigned.setStatus("current")
_Hh3cVsanDmPrincipalSwitchWWN_Type = Hh3cFcNameId
_Hh3cVsanDmPrincipalSwitchWWN_Object = MibTableColumn
hh3cVsanDmPrincipalSwitchWWN = _Hh3cVsanDmPrincipalSwitchWWN_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 11),
    _Hh3cVsanDmPrincipalSwitchWWN_Type()
)
hh3cVsanDmPrincipalSwitchWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanDmPrincipalSwitchWWN.setStatus("current")
_Hh3cVsanDmLocalSwitchWWN_Type = Hh3cFcNameId
_Hh3cVsanDmLocalSwitchWWN_Object = MibTableColumn
hh3cVsanDmLocalSwitchWWN = _Hh3cVsanDmLocalSwitchWWN_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 12),
    _Hh3cVsanDmLocalSwitchWWN_Type()
)
hh3cVsanDmLocalSwitchWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanDmLocalSwitchWWN.setStatus("current")
_Hh3cVsanDmPrincipalSwRunPriority_Type = Hh3cFcDomainPriority
_Hh3cVsanDmPrincipalSwRunPriority_Object = MibTableColumn
hh3cVsanDmPrincipalSwRunPriority = _Hh3cVsanDmPrincipalSwRunPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 13),
    _Hh3cVsanDmPrincipalSwRunPriority_Type()
)
hh3cVsanDmPrincipalSwRunPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanDmPrincipalSwRunPriority.setStatus("current")
_Hh3cVsanDmLocalSwRunPriority_Type = Hh3cFcDomainPriority
_Hh3cVsanDmLocalSwRunPriority_Object = MibTableColumn
hh3cVsanDmLocalSwRunPriority = _Hh3cVsanDmLocalSwRunPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 14),
    _Hh3cVsanDmLocalSwRunPriority_Type()
)
hh3cVsanDmLocalSwRunPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanDmLocalSwRunPriority.setStatus("current")
_Hh3cVsanDmPrincipalSwSlctCnt_Type = Counter32
_Hh3cVsanDmPrincipalSwSlctCnt_Object = MibTableColumn
hh3cVsanDmPrincipalSwSlctCnt = _Hh3cVsanDmPrincipalSwSlctCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 15),
    _Hh3cVsanDmPrincipalSwSlctCnt_Type()
)
hh3cVsanDmPrincipalSwSlctCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanDmPrincipalSwSlctCnt.setStatus("current")
_Hh3cVsanDmLocalPrincipalSwSlctCnt_Type = Counter32
_Hh3cVsanDmLocalPrincipalSwSlctCnt_Object = MibTableColumn
hh3cVsanDmLocalPrincipalSwSlctCnt = _Hh3cVsanDmLocalPrincipalSwSlctCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 16),
    _Hh3cVsanDmLocalPrincipalSwSlctCnt_Type()
)
hh3cVsanDmLocalPrincipalSwSlctCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanDmLocalPrincipalSwSlctCnt.setStatus("current")
_Hh3cVsanDmBFCnt_Type = Counter32
_Hh3cVsanDmBFCnt_Object = MibTableColumn
hh3cVsanDmBFCnt = _Hh3cVsanDmBFCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 17),
    _Hh3cVsanDmBFCnt_Type()
)
hh3cVsanDmBFCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanDmBFCnt.setStatus("current")
_Hh3cVsanDmRCFCnt_Type = Counter32
_Hh3cVsanDmRCFCnt_Object = MibTableColumn
hh3cVsanDmRCFCnt = _Hh3cVsanDmRCFCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 18),
    _Hh3cVsanDmRCFCnt_Type()
)
hh3cVsanDmRCFCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanDmRCFCnt.setStatus("current")
_Hh3cVsanDmIfConfigTable_Object = MibTable
hh3cVsanDmIfConfigTable = _Hh3cVsanDmIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cVsanDmIfConfigTable.setStatus("current")
_Hh3cVsanDmIfConfigEntry_Object = MibTableRow
hh3cVsanDmIfConfigEntry = _Hh3cVsanDmIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 3, 1)
)
hh3cVsanDmIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
)
if mibBuilder.loadTexts:
    hh3cVsanDmIfConfigEntry.setStatus("current")


class _Hh3cVsanDmIfConfigRcfReject_Type(TruthValue):
    """Custom type hh3cVsanDmIfConfigRcfReject based on TruthValue"""


_Hh3cVsanDmIfConfigRcfReject_Object = MibTableColumn
hh3cVsanDmIfConfigRcfReject = _Hh3cVsanDmIfConfigRcfReject_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 3, 1, 1),
    _Hh3cVsanDmIfConfigRcfReject_Type()
)
hh3cVsanDmIfConfigRcfReject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVsanDmIfConfigRcfReject.setStatus("current")
_Hh3cVsanDmInformation_ObjectIdentity = ObjectIdentity
hh3cVsanDmInformation = _Hh3cVsanDmInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 2)
)
_Hh3cVsanDmDatabaseTable_Object = MibTable
hh3cVsanDmDatabaseTable = _Hh3cVsanDmDatabaseTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cVsanDmDatabaseTable.setStatus("current")
_Hh3cVsanDmDatabaseEntry_Object = MibTableRow
hh3cVsanDmDatabaseEntry = _Hh3cVsanDmDatabaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 2, 1, 1)
)
hh3cVsanDmDatabaseEntry.setIndexNames(
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
    (0, "HH3C-VSAN-MIB", "hh3cVsanDmDatabaseDomainId"),
)
if mibBuilder.loadTexts:
    hh3cVsanDmDatabaseEntry.setStatus("current")
_Hh3cVsanDmDatabaseDomainId_Type = Hh3cFcDomainId
_Hh3cVsanDmDatabaseDomainId_Object = MibTableColumn
hh3cVsanDmDatabaseDomainId = _Hh3cVsanDmDatabaseDomainId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 2, 1, 1, 1),
    _Hh3cVsanDmDatabaseDomainId_Type()
)
hh3cVsanDmDatabaseDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVsanDmDatabaseDomainId.setStatus("current")
_Hh3cVsanDmDatabaseSwitchWWN_Type = Hh3cFcNameId
_Hh3cVsanDmDatabaseSwitchWWN_Object = MibTableColumn
hh3cVsanDmDatabaseSwitchWWN = _Hh3cVsanDmDatabaseSwitchWWN_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 2, 1, 1, 2),
    _Hh3cVsanDmDatabaseSwitchWWN_Type()
)
hh3cVsanDmDatabaseSwitchWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanDmDatabaseSwitchWWN.setStatus("current")
_Hh3cVsanDmIfInfoTable_Object = MibTable
hh3cVsanDmIfInfoTable = _Hh3cVsanDmIfInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cVsanDmIfInfoTable.setStatus("current")
_Hh3cVsanDmIfInfoEntry_Object = MibTableRow
hh3cVsanDmIfInfoEntry = _Hh3cVsanDmIfInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 2, 2, 1)
)
hh3cVsanDmIfInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
)
if mibBuilder.loadTexts:
    hh3cVsanDmIfInfoEntry.setStatus("current")


class _Hh3cVsanDmIfInfoRole_Type(Integer32):
    """Custom type hh3cVsanDmIfInfoRole based on Integer32"""
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


_Hh3cVsanDmIfInfoRole_Type.__name__ = "Integer32"
_Hh3cVsanDmIfInfoRole_Object = MibTableColumn
hh3cVsanDmIfInfoRole = _Hh3cVsanDmIfInfoRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 2, 2, 1, 1),
    _Hh3cVsanDmIfInfoRole_Type()
)
hh3cVsanDmIfInfoRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanDmIfInfoRole.setStatus("current")
_Hh3cVsanDmNotifications_ObjectIdentity = ObjectIdentity
hh3cVsanDmNotifications = _Hh3cVsanDmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 3)
)
_Hh3cVsanDmNotificationPrefix_ObjectIdentity = ObjectIdentity
hh3cVsanDmNotificationPrefix = _Hh3cVsanDmNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 3, 0)
)
_Hh3cVsanDmNotificationSwitch_ObjectIdentity = ObjectIdentity
hh3cVsanDmNotificationSwitch = _Hh3cVsanDmNotificationSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 3, 1)
)


class _Hh3cVsanDmFabricChangeNotifyEnable_Type(TruthValue):
    """Custom type hh3cVsanDmFabricChangeNotifyEnable based on TruthValue"""


_Hh3cVsanDmFabricChangeNotifyEnable_Object = MibScalar
hh3cVsanDmFabricChangeNotifyEnable = _Hh3cVsanDmFabricChangeNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 3, 1, 1),
    _Hh3cVsanDmFabricChangeNotifyEnable_Type()
)
hh3cVsanDmFabricChangeNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVsanDmFabricChangeNotifyEnable.setStatus("current")


class _Hh3cVsanDmDomainIdChangeNotifyEnable_Type(TruthValue):
    """Custom type hh3cVsanDmDomainIdChangeNotifyEnable based on TruthValue"""


_Hh3cVsanDmDomainIdChangeNotifyEnable_Object = MibScalar
hh3cVsanDmDomainIdChangeNotifyEnable = _Hh3cVsanDmDomainIdChangeNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 3, 1, 2),
    _Hh3cVsanDmDomainIdChangeNotifyEnable_Type()
)
hh3cVsanDmDomainIdChangeNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVsanDmDomainIdChangeNotifyEnable.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cVsanDmDomainIdNotAssignedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 3, 0, 1)
)
hh3cVsanDmDomainIdNotAssignedNotify.setObjects(
      *(("HH3C-VSAN-MIB", "hh3cVsanIndex"),
        ("HH3C-VSAN-MIB", "hh3cVsanDmLocalSwitchWWN"))
)
if mibBuilder.loadTexts:
    hh3cVsanDmDomainIdNotAssignedNotify.setStatus(
        "current"
    )

hh3cVsanDmNewPrincipalSwitchNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 3, 0, 2)
)
hh3cVsanDmNewPrincipalSwitchNotify.setObjects(
      *(("HH3C-VSAN-MIB", "hh3cVsanIndex"),
        ("HH3C-VSAN-MIB", "hh3cVsanDmLocalSwitchWWN"))
)
if mibBuilder.loadTexts:
    hh3cVsanDmNewPrincipalSwitchNotify.setStatus(
        "current"
    )

hh3cVsanDmFabricChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 3, 0, 3)
)
hh3cVsanDmFabricChangeNotify.setObjects(
    ("HH3C-VSAN-MIB", "hh3cVsanIndex")
)
if mibBuilder.loadTexts:
    hh3cVsanDmFabricChangeNotify.setStatus(
        "current"
    )

hh3cVsanDmDomainIdChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 3, 0, 4)
)
hh3cVsanDmDomainIdChangeNotify.setObjects(
      *(("HH3C-VSAN-MIB", "hh3cVsanIndex"),
        ("HH3C-VSAN-MIB", "hh3cVsanDmDomainIdAssigned"),
        ("HH3C-VSAN-MIB", "hh3cVsanDmLocalSwitchWWN"))
)
if mibBuilder.loadTexts:
    hh3cVsanDmDomainIdChangeNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-VSAN-MIB",
    **{"hh3cSan": hh3cSan,
       "hh3cVsan": hh3cVsan,
       "hh3cVsanMibObjects": hh3cVsanMibObjects,
       "hh3cVsanDmConfiguration": hh3cVsanDmConfiguration,
       "hh3cVsanTable": hh3cVsanTable,
       "hh3cVsanEntry": hh3cVsanEntry,
       "hh3cVsanIndex": hh3cVsanIndex,
       "hh3cVsanCoreSwitchName": hh3cVsanCoreSwitchName,
       "hh3cVsanRowStatus": hh3cVsanRowStatus,
       "hh3cVsanDmTable": hh3cVsanDmTable,
       "hh3cVsanDmEntry": hh3cVsanDmEntry,
       "hh3cVsanDmDomainConfigureEnable": hh3cVsanDmDomainConfigureEnable,
       "hh3cVsanDmFabricNameConfigured": hh3cVsanDmFabricNameConfigured,
       "hh3cVsanDmPriorityConfigured": hh3cVsanDmPriorityConfigured,
       "hh3cVsanDmAllowedDomainIdList": hh3cVsanDmAllowedDomainIdList,
       "hh3cVsanDmDomainIdConfigured": hh3cVsanDmDomainIdConfigured,
       "hh3cVsanDmDomainIdTypeConfigured": hh3cVsanDmDomainIdTypeConfigured,
       "hh3cVsanDmAutoReconfigureEnable": hh3cVsanDmAutoReconfigureEnable,
       "hh3cVsanDmDomainRestart": hh3cVsanDmDomainRestart,
       "hh3cVsanDmState": hh3cVsanDmState,
       "hh3cVsanDmDomainIdAssigned": hh3cVsanDmDomainIdAssigned,
       "hh3cVsanDmPrincipalSwitchWWN": hh3cVsanDmPrincipalSwitchWWN,
       "hh3cVsanDmLocalSwitchWWN": hh3cVsanDmLocalSwitchWWN,
       "hh3cVsanDmPrincipalSwRunPriority": hh3cVsanDmPrincipalSwRunPriority,
       "hh3cVsanDmLocalSwRunPriority": hh3cVsanDmLocalSwRunPriority,
       "hh3cVsanDmPrincipalSwSlctCnt": hh3cVsanDmPrincipalSwSlctCnt,
       "hh3cVsanDmLocalPrincipalSwSlctCnt": hh3cVsanDmLocalPrincipalSwSlctCnt,
       "hh3cVsanDmBFCnt": hh3cVsanDmBFCnt,
       "hh3cVsanDmRCFCnt": hh3cVsanDmRCFCnt,
       "hh3cVsanDmIfConfigTable": hh3cVsanDmIfConfigTable,
       "hh3cVsanDmIfConfigEntry": hh3cVsanDmIfConfigEntry,
       "hh3cVsanDmIfConfigRcfReject": hh3cVsanDmIfConfigRcfReject,
       "hh3cVsanDmInformation": hh3cVsanDmInformation,
       "hh3cVsanDmDatabaseTable": hh3cVsanDmDatabaseTable,
       "hh3cVsanDmDatabaseEntry": hh3cVsanDmDatabaseEntry,
       "hh3cVsanDmDatabaseDomainId": hh3cVsanDmDatabaseDomainId,
       "hh3cVsanDmDatabaseSwitchWWN": hh3cVsanDmDatabaseSwitchWWN,
       "hh3cVsanDmIfInfoTable": hh3cVsanDmIfInfoTable,
       "hh3cVsanDmIfInfoEntry": hh3cVsanDmIfInfoEntry,
       "hh3cVsanDmIfInfoRole": hh3cVsanDmIfInfoRole,
       "hh3cVsanDmNotifications": hh3cVsanDmNotifications,
       "hh3cVsanDmNotificationPrefix": hh3cVsanDmNotificationPrefix,
       "hh3cVsanDmDomainIdNotAssignedNotify": hh3cVsanDmDomainIdNotAssignedNotify,
       "hh3cVsanDmNewPrincipalSwitchNotify": hh3cVsanDmNewPrincipalSwitchNotify,
       "hh3cVsanDmFabricChangeNotify": hh3cVsanDmFabricChangeNotify,
       "hh3cVsanDmDomainIdChangeNotify": hh3cVsanDmDomainIdChangeNotify,
       "hh3cVsanDmNotificationSwitch": hh3cVsanDmNotificationSwitch,
       "hh3cVsanDmFabricChangeNotifyEnable": hh3cVsanDmFabricChangeNotifyEnable,
       "hh3cVsanDmDomainIdChangeNotifyEnable": hh3cVsanDmDomainIdChangeNotifyEnable}
)
