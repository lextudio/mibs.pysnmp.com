# SNMP MIB module (CISCO-ENTITY-DIAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ENTITY-DIAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:32 2024
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

(CeDiagDiagnosticLevel,
 CeDiagDiagnosticMethod,
 CeDiagErrorIdentifier,
 CeDiagErrorIdentifierOrZero,
 CeDiagJobIdentifier,
 CeDiagJobSuite,
 CeDiagPortList,
 CeDiagTestIdentifier,
 CeDiagTestList) = mibBuilder.importSymbols(
    "CISCO-ENTITY-DIAG-TC-MIB",
    "CeDiagDiagnosticLevel",
    "CeDiagDiagnosticMethod",
    "CeDiagErrorIdentifier",
    "CeDiagErrorIdentifierOrZero",
    "CeDiagJobIdentifier",
    "CeDiagJobSuite",
    "CeDiagPortList",
    "CeDiagTestIdentifier",
    "CeDiagTestList")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(EntPhysicalIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "EntPhysicalIndexOrZero")

(PhysicalIndex,
 entPhysicalDescr,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalDescr",
    "entPhysicalIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoEntityDiagMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 350)
)
ciscoEntityDiagMIB.setRevisions(
        ("2016-03-11 00:00",
         "2010-05-26 00:00",
         "2009-06-30 00:00",
         "2008-03-12 00:00",
         "2007-01-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoEntityDiagMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoEntityDiagMIBNotifs = _CiscoEntityDiagMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 0)
)
_CiscoEntityDiagMIBObjects_ObjectIdentity = ObjectIdentity
ciscoEntityDiagMIBObjects = _CiscoEntityDiagMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1)
)
_CeDiagDescriptions_ObjectIdentity = ObjectIdentity
ceDiagDescriptions = _CeDiagDescriptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 1)
)
_CeDiagTestInfoTable_Object = MibTable
ceDiagTestInfoTable = _CeDiagTestInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ceDiagTestInfoTable.setStatus("current")
_CeDiagTestInfoEntry_Object = MibTableRow
ceDiagTestInfoEntry = _CeDiagTestInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 1, 1, 1)
)
ceDiagTestInfoEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENTITY-DIAG-MIB", "ceDiagTestId"),
)
if mibBuilder.loadTexts:
    ceDiagTestInfoEntry.setStatus("current")
_CeDiagTestId_Type = CeDiagTestIdentifier
_CeDiagTestId_Object = MibTableColumn
ceDiagTestId = _CeDiagTestId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 1, 1, 1, 1),
    _CeDiagTestId_Type()
)
ceDiagTestId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceDiagTestId.setStatus("current")
_CeDiagTestText_Type = SnmpAdminString
_CeDiagTestText_Object = MibTableColumn
ceDiagTestText = _CeDiagTestText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 1, 1, 1, 2),
    _CeDiagTestText_Type()
)
ceDiagTestText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDiagTestText.setStatus("current")


class _CeDiagTestAttributes_Type(Bits):
    """Custom type ceDiagTestAttributes based on Bits"""
    namedValues = NamedValues(
        *(("activeToStandby", 12),
          ("basicOnDemand", 4),
          ("complete", 1),
          ("disruptive", 15),
          ("fatal", 3),
          ("hmAlwaysEnable", 8),
          ("hmFixedInterval", 9),
          ("minimal", 0),
          ("nonDisruptive", 7),
          ("nonHM", 10),
          ("offline", 13),
          ("parallel", 6),
          ("perDevice", 14),
          ("perPort", 2),
          ("proxy", 11),
          ("standby", 5))
    )

_CeDiagTestAttributes_Type.__name__ = "Bits"
_CeDiagTestAttributes_Object = MibTableColumn
ceDiagTestAttributes = _CeDiagTestAttributes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 1, 1, 1, 3),
    _CeDiagTestAttributes_Type()
)
ceDiagTestAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDiagTestAttributes.setStatus("current")
_CeDiagTestCustomAttributeTable_Object = MibTable
ceDiagTestCustomAttributeTable = _CeDiagTestCustomAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ceDiagTestCustomAttributeTable.setStatus("current")
_CeDiagTestCustomAttributeEntry_Object = MibTableRow
ceDiagTestCustomAttributeEntry = _CeDiagTestCustomAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 1, 2, 1)
)
ceDiagTestCustomAttributeEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENTITY-DIAG-MIB", "ceDiagTestId"),
    (0, "CISCO-ENTITY-DIAG-MIB", "ceDiagTestCustomAttributeIndex"),
)
if mibBuilder.loadTexts:
    ceDiagTestCustomAttributeEntry.setStatus("current")
_CeDiagTestCustomAttributeIndex_Type = Unsigned32
_CeDiagTestCustomAttributeIndex_Object = MibTableColumn
ceDiagTestCustomAttributeIndex = _CeDiagTestCustomAttributeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 1, 2, 1, 1),
    _CeDiagTestCustomAttributeIndex_Type()
)
ceDiagTestCustomAttributeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceDiagTestCustomAttributeIndex.setStatus("current")
_CeDiagTestCustomAttributeDesc_Type = SnmpAdminString
_CeDiagTestCustomAttributeDesc_Object = MibTableColumn
ceDiagTestCustomAttributeDesc = _CeDiagTestCustomAttributeDesc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 1, 2, 1, 2),
    _CeDiagTestCustomAttributeDesc_Type()
)
ceDiagTestCustomAttributeDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDiagTestCustomAttributeDesc.setStatus("current")
_CeDiagErrorInfoTable_Object = MibTable
ceDiagErrorInfoTable = _CeDiagErrorInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ceDiagErrorInfoTable.setStatus("current")
_CeDiagErrorInfoEntry_Object = MibTableRow
ceDiagErrorInfoEntry = _CeDiagErrorInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 1, 3, 1)
)
ceDiagErrorInfoEntry.setIndexNames(
    (0, "CISCO-ENTITY-DIAG-MIB", "ceDiagErrorId"),
)
if mibBuilder.loadTexts:
    ceDiagErrorInfoEntry.setStatus("current")
_CeDiagErrorId_Type = CeDiagErrorIdentifier
_CeDiagErrorId_Object = MibTableColumn
ceDiagErrorId = _CeDiagErrorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 1, 3, 1, 1),
    _CeDiagErrorId_Type()
)
ceDiagErrorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceDiagErrorId.setStatus("current")
_CeDiagErrorText_Type = SnmpAdminString
_CeDiagErrorText_Object = MibTableColumn
ceDiagErrorText = _CeDiagErrorText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 1, 3, 1, 2),
    _CeDiagErrorText_Type()
)
ceDiagErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDiagErrorText.setStatus("current")
_CeDiagGlobalConfig_ObjectIdentity = ObjectIdentity
ceDiagGlobalConfig = _CeDiagGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 2)
)


class _CeDiagBootupLevel_Type(CeDiagDiagnosticLevel):
    """Custom type ceDiagBootupLevel based on CeDiagDiagnosticLevel"""


_CeDiagBootupLevel_Object = MibScalar
ceDiagBootupLevel = _CeDiagBootupLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 2, 1),
    _CeDiagBootupLevel_Type()
)
ceDiagBootupLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceDiagBootupLevel.setStatus("current")
_CeDiagEntity_ObjectIdentity = ObjectIdentity
ceDiagEntity = _CeDiagEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 3)
)
_CeDiagEntityTable_Object = MibTable
ceDiagEntityTable = _CeDiagEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ceDiagEntityTable.setStatus("current")
_CeDiagEntityEntry_Object = MibTableRow
ceDiagEntityEntry = _CeDiagEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 3, 1, 1)
)
ceDiagEntityEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ceDiagEntityEntry.setStatus("current")
_CeDiagEntityBootLevel_Type = CeDiagDiagnosticLevel
_CeDiagEntityBootLevel_Object = MibTableColumn
ceDiagEntityBootLevel = _CeDiagEntityBootLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 3, 1, 1, 1),
    _CeDiagEntityBootLevel_Type()
)
ceDiagEntityBootLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDiagEntityBootLevel.setStatus("current")


class _CeDiagEntityImageAdminStatus_Type(Integer32):
    """Custom type ceDiagEntityImageAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fieldDiagnostic", 2),
          ("operational", 1))
    )


_CeDiagEntityImageAdminStatus_Type.__name__ = "Integer32"
_CeDiagEntityImageAdminStatus_Object = MibTableColumn
ceDiagEntityImageAdminStatus = _CeDiagEntityImageAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 3, 1, 1, 2),
    _CeDiagEntityImageAdminStatus_Type()
)
ceDiagEntityImageAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceDiagEntityImageAdminStatus.setStatus("current")


class _CeDiagEntityImageOperStatus_Type(Integer32):
    """Custom type ceDiagEntityImageOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("booting", 3),
          ("fieldDiagnostic", 2),
          ("operational", 1))
    )


_CeDiagEntityImageOperStatus_Type.__name__ = "Integer32"
_CeDiagEntityImageOperStatus_Object = MibTableColumn
ceDiagEntityImageOperStatus = _CeDiagEntityImageOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 3, 1, 1, 3),
    _CeDiagEntityImageOperStatus_Type()
)
ceDiagEntityImageOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDiagEntityImageOperStatus.setStatus("current")
_CeDiagEntityFieldDiagnosticUrl_Type = SnmpAdminString
_CeDiagEntityFieldDiagnosticUrl_Object = MibTableColumn
ceDiagEntityFieldDiagnosticUrl = _CeDiagEntityFieldDiagnosticUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 3, 1, 1, 4),
    _CeDiagEntityFieldDiagnosticUrl_Type()
)
ceDiagEntityFieldDiagnosticUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceDiagEntityFieldDiagnosticUrl.setStatus("current")
_CeDiagEntityCurrentTestTable_Object = MibTable
ceDiagEntityCurrentTestTable = _CeDiagEntityCurrentTestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ceDiagEntityCurrentTestTable.setStatus("current")
_CeDiagEntityCurrentTestEntry_Object = MibTableRow
ceDiagEntityCurrentTestEntry = _CeDiagEntityCurrentTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 3, 2, 1)
)
ceDiagEntityCurrentTestEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENTITY-DIAG-MIB", "ceDiagTestId"),
)
if mibBuilder.loadTexts:
    ceDiagEntityCurrentTestEntry.setStatus("current")
_CeDiagEntityCurrentTestMethod_Type = CeDiagDiagnosticMethod
_CeDiagEntityCurrentTestMethod_Object = MibTableColumn
ceDiagEntityCurrentTestMethod = _CeDiagEntityCurrentTestMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 3, 2, 1, 1),
    _CeDiagEntityCurrentTestMethod_Type()
)
ceDiagEntityCurrentTestMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDiagEntityCurrentTestMethod.setStatus("current")
_CeDiagOnDemand_ObjectIdentity = ObjectIdentity
ceDiagOnDemand = _CeDiagOnDemand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 4)
)
_CeDiagOnDemandErrorAllowed_Type = Unsigned32
_CeDiagOnDemandErrorAllowed_Object = MibScalar
ceDiagOnDemandErrorAllowed = _CeDiagOnDemandErrorAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 4, 1),
    _CeDiagOnDemandErrorAllowed_Type()
)
ceDiagOnDemandErrorAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceDiagOnDemandErrorAllowed.setStatus("current")


class _CeDiagOnDemandErrorAction_Type(Integer32):
    """Custom type ceDiagOnDemandErrorAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("continue", 1),
          ("stop", 2))
    )


_CeDiagOnDemandErrorAction_Type.__name__ = "Integer32"
_CeDiagOnDemandErrorAction_Object = MibScalar
ceDiagOnDemandErrorAction = _CeDiagOnDemandErrorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 4, 2),
    _CeDiagOnDemandErrorAction_Type()
)
ceDiagOnDemandErrorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceDiagOnDemandErrorAction.setStatus("current")
_CeDiagOnDemandIterations_Type = Unsigned32
_CeDiagOnDemandIterations_Object = MibScalar
ceDiagOnDemandIterations = _CeDiagOnDemandIterations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 4, 3),
    _CeDiagOnDemandIterations_Type()
)
ceDiagOnDemandIterations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceDiagOnDemandIterations.setStatus("current")
_CeDiagOnDemandJobTable_Object = MibTable
ceDiagOnDemandJobTable = _CeDiagOnDemandJobTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 4, 4)
)
if mibBuilder.loadTexts:
    ceDiagOnDemandJobTable.setStatus("current")
_CeDiagOnDemandJobEntry_Object = MibTableRow
ceDiagOnDemandJobEntry = _CeDiagOnDemandJobEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 4, 4, 1)
)
ceDiagOnDemandJobEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ceDiagOnDemandJobEntry.setStatus("current")
_CeDiagOnDemandJobSuite_Type = CeDiagJobSuite
_CeDiagOnDemandJobSuite_Object = MibTableColumn
ceDiagOnDemandJobSuite = _CeDiagOnDemandJobSuite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 4, 4, 1, 1),
    _CeDiagOnDemandJobSuite_Type()
)
ceDiagOnDemandJobSuite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceDiagOnDemandJobSuite.setStatus("current")
_CeDiagOnDemandJobTestList_Type = CeDiagTestList
_CeDiagOnDemandJobTestList_Object = MibTableColumn
ceDiagOnDemandJobTestList = _CeDiagOnDemandJobTestList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 4, 4, 1, 2),
    _CeDiagOnDemandJobTestList_Type()
)
ceDiagOnDemandJobTestList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceDiagOnDemandJobTestList.setStatus("current")
_CeDiagOnDemandJobPortList_Type = CeDiagPortList
_CeDiagOnDemandJobPortList_Object = MibTableColumn
ceDiagOnDemandJobPortList = _CeDiagOnDemandJobPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 4, 4, 1, 3),
    _CeDiagOnDemandJobPortList_Type()
)
ceDiagOnDemandJobPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceDiagOnDemandJobPortList.setStatus("current")
_CeDiagOnDemandJobRowStatus_Type = RowStatus
_CeDiagOnDemandJobRowStatus_Object = MibTableColumn
ceDiagOnDemandJobRowStatus = _CeDiagOnDemandJobRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 4, 4, 1, 4),
    _CeDiagOnDemandJobRowStatus_Type()
)
ceDiagOnDemandJobRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceDiagOnDemandJobRowStatus.setStatus("current")
_CeDiagScheduled_ObjectIdentity = ObjectIdentity
ceDiagScheduled = _CeDiagScheduled_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 5)
)
_CeDiagScheduledJobTable_Object = MibTable
ceDiagScheduledJobTable = _CeDiagScheduledJobTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ceDiagScheduledJobTable.setStatus("current")
_CeDiagScheduledJobEntry_Object = MibTableRow
ceDiagScheduledJobEntry = _CeDiagScheduledJobEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 5, 1, 1)
)
ceDiagScheduledJobEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENTITY-DIAG-MIB", "ceDiagScheduledJobIndex"),
)
if mibBuilder.loadTexts:
    ceDiagScheduledJobEntry.setStatus("current")
_CeDiagScheduledJobIndex_Type = CeDiagJobIdentifier
_CeDiagScheduledJobIndex_Object = MibTableColumn
ceDiagScheduledJobIndex = _CeDiagScheduledJobIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 5, 1, 1, 1),
    _CeDiagScheduledJobIndex_Type()
)
ceDiagScheduledJobIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceDiagScheduledJobIndex.setStatus("current")


class _CeDiagScheduledJobType_Type(Integer32):
    """Custom type ceDiagScheduledJobType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("scheduledOneShot", 1),
          ("scheduledPeriodicDaily", 2),
          ("scheduledPeriodicWeekly", 3))
    )


_CeDiagScheduledJobType_Type.__name__ = "Integer32"
_CeDiagScheduledJobType_Object = MibTableColumn
ceDiagScheduledJobType = _CeDiagScheduledJobType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 5, 1, 1, 2),
    _CeDiagScheduledJobType_Type()
)
ceDiagScheduledJobType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceDiagScheduledJobType.setStatus("current")
_CeDiagScheduledJobStart_Type = DateAndTime
_CeDiagScheduledJobStart_Object = MibTableColumn
ceDiagScheduledJobStart = _CeDiagScheduledJobStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 5, 1, 1, 3),
    _CeDiagScheduledJobStart_Type()
)
ceDiagScheduledJobStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceDiagScheduledJobStart.setStatus("current")


class _CeDiagScheduledJobDayOfWeek_Type(Integer32):
    """Custom type ceDiagScheduledJobDayOfWeek based on Integer32"""
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
        *(("friday", 6),
          ("monday", 2),
          ("notApplicable", 8),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )


_CeDiagScheduledJobDayOfWeek_Type.__name__ = "Integer32"
_CeDiagScheduledJobDayOfWeek_Object = MibTableColumn
ceDiagScheduledJobDayOfWeek = _CeDiagScheduledJobDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 5, 1, 1, 4),
    _CeDiagScheduledJobDayOfWeek_Type()
)
ceDiagScheduledJobDayOfWeek.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceDiagScheduledJobDayOfWeek.setStatus("current")
_CeDiagScheduledJobTestList_Type = CeDiagTestList
_CeDiagScheduledJobTestList_Object = MibTableColumn
ceDiagScheduledJobTestList = _CeDiagScheduledJobTestList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 5, 1, 1, 5),
    _CeDiagScheduledJobTestList_Type()
)
ceDiagScheduledJobTestList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceDiagScheduledJobTestList.setStatus("current")
_CeDiagScheduledJobPortList_Type = CeDiagPortList
_CeDiagScheduledJobPortList_Object = MibTableColumn
ceDiagScheduledJobPortList = _CeDiagScheduledJobPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 5, 1, 1, 6),
    _CeDiagScheduledJobPortList_Type()
)
ceDiagScheduledJobPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceDiagScheduledJobPortList.setStatus("current")
_CeDiagScheduledJobRowStatus_Type = RowStatus
_CeDiagScheduledJobRowStatus_Object = MibTableColumn
ceDiagScheduledJobRowStatus = _CeDiagScheduledJobRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 5, 1, 1, 7),
    _CeDiagScheduledJobRowStatus_Type()
)
ceDiagScheduledJobRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceDiagScheduledJobRowStatus.setStatus("current")
_CeDiagScheduledJobSuite_Type = CeDiagJobSuite
_CeDiagScheduledJobSuite_Object = MibTableColumn
ceDiagScheduledJobSuite = _CeDiagScheduledJobSuite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 5, 1, 1, 8),
    _CeDiagScheduledJobSuite_Type()
)
ceDiagScheduledJobSuite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceDiagScheduledJobSuite.setStatus("current")
_CeDiagTest_ObjectIdentity = ObjectIdentity
ceDiagTest = _CeDiagTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 6)
)
_CeDiagTestPerfTable_Object = MibTable
ceDiagTestPerfTable = _CeDiagTestPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ceDiagTestPerfTable.setStatus("current")
_CeDiagTestPerfEntry_Object = MibTableRow
ceDiagTestPerfEntry = _CeDiagTestPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 6, 1, 1)
)
ceDiagTestPerfEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENTITY-DIAG-MIB", "ceDiagTestId"),
)
if mibBuilder.loadTexts:
    ceDiagTestPerfEntry.setStatus("current")


class _CeDiagTestPerfLastResult_Type(Integer32):
    """Custom type ceDiagTestPerfLastResult based on Integer32"""
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
        *(("fail", 2),
          ("pass", 3),
          ("skipped", 4),
          ("unknown", 1))
    )


_CeDiagTestPerfLastResult_Type.__name__ = "Integer32"
_CeDiagTestPerfLastResult_Object = MibTableColumn
ceDiagTestPerfLastResult = _CeDiagTestPerfLastResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 6, 1, 1, 1),
    _CeDiagTestPerfLastResult_Type()
)
ceDiagTestPerfLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDiagTestPerfLastResult.setStatus("current")
_CeDiagTestPerfLastErrorID_Type = CeDiagErrorIdentifierOrZero
_CeDiagTestPerfLastErrorID_Object = MibTableColumn
ceDiagTestPerfLastErrorID = _CeDiagTestPerfLastErrorID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 6, 1, 1, 2),
    _CeDiagTestPerfLastErrorID_Type()
)
ceDiagTestPerfLastErrorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDiagTestPerfLastErrorID.setStatus("current")
_CeDiagTestPerfLastRun_Type = DateAndTime
_CeDiagTestPerfLastRun_Object = MibTableColumn
ceDiagTestPerfLastRun = _CeDiagTestPerfLastRun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 6, 1, 1, 3),
    _CeDiagTestPerfLastRun_Type()
)
ceDiagTestPerfLastRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDiagTestPerfLastRun.setStatus("current")
_CeDiagTestPerfFirstFail_Type = DateAndTime
_CeDiagTestPerfFirstFail_Object = MibTableColumn
ceDiagTestPerfFirstFail = _CeDiagTestPerfFirstFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 6, 1, 1, 4),
    _CeDiagTestPerfFirstFail_Type()
)
ceDiagTestPerfFirstFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDiagTestPerfFirstFail.setStatus("current")
_CeDiagTestPerfLastSuccess_Type = DateAndTime
_CeDiagTestPerfLastSuccess_Object = MibTableColumn
ceDiagTestPerfLastSuccess = _CeDiagTestPerfLastSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 6, 1, 1, 5),
    _CeDiagTestPerfLastSuccess_Type()
)
ceDiagTestPerfLastSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDiagTestPerfLastSuccess.setStatus("current")
_CeDiagTestPeffLastFail_Type = DateAndTime
_CeDiagTestPeffLastFail_Object = MibTableColumn
ceDiagTestPeffLastFail = _CeDiagTestPeffLastFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 6, 1, 1, 6),
    _CeDiagTestPeffLastFail_Type()
)
ceDiagTestPeffLastFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDiagTestPeffLastFail.setStatus("current")
_CeDiagTestPerfTotalRuns_Type = Counter32
_CeDiagTestPerfTotalRuns_Object = MibTableColumn
ceDiagTestPerfTotalRuns = _CeDiagTestPerfTotalRuns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 6, 1, 1, 7),
    _CeDiagTestPerfTotalRuns_Type()
)
ceDiagTestPerfTotalRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDiagTestPerfTotalRuns.setStatus("current")
_CeDiagTestPerfTotalFails_Type = Counter32
_CeDiagTestPerfTotalFails_Object = MibTableColumn
ceDiagTestPerfTotalFails = _CeDiagTestPerfTotalFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 6, 1, 1, 8),
    _CeDiagTestPerfTotalFails_Type()
)
ceDiagTestPerfTotalFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDiagTestPerfTotalFails.setStatus("current")
_CeDiagTestPerfConsecutiveFails_Type = Gauge32
_CeDiagTestPerfConsecutiveFails_Object = MibTableColumn
ceDiagTestPerfConsecutiveFails = _CeDiagTestPerfConsecutiveFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 6, 1, 1, 9),
    _CeDiagTestPerfConsecutiveFails_Type()
)
ceDiagTestPerfConsecutiveFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDiagTestPerfConsecutiveFails.setStatus("current")
_CeDiagTestPerfLastTestMethod_Type = CeDiagDiagnosticMethod
_CeDiagTestPerfLastTestMethod_Object = MibTableColumn
ceDiagTestPerfLastTestMethod = _CeDiagTestPerfLastTestMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 6, 1, 1, 10),
    _CeDiagTestPerfLastTestMethod_Type()
)
ceDiagTestPerfLastTestMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDiagTestPerfLastTestMethod.setStatus("current")
_CeDiagHealthMonitor_ObjectIdentity = ObjectIdentity
ceDiagHealthMonitor = _CeDiagHealthMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 7)
)
_CeDiagHMSyslogEnabled_Type = TruthValue
_CeDiagHMSyslogEnabled_Object = MibScalar
ceDiagHMSyslogEnabled = _CeDiagHMSyslogEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 7, 1),
    _CeDiagHMSyslogEnabled_Type()
)
ceDiagHMSyslogEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceDiagHMSyslogEnabled.setStatus("current")
_CeDiagHMTestTable_Object = MibTable
ceDiagHMTestTable = _CeDiagHMTestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 7, 2)
)
if mibBuilder.loadTexts:
    ceDiagHMTestTable.setStatus("current")
_CeDiagHMTestEntry_Object = MibTableRow
ceDiagHMTestEntry = _CeDiagHMTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 7, 2, 1)
)
ceDiagHMTestEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENTITY-DIAG-MIB", "ceDiagTestId"),
)
if mibBuilder.loadTexts:
    ceDiagHMTestEntry.setStatus("current")
_CeDiagHMTestEnabled_Type = TruthValue
_CeDiagHMTestEnabled_Object = MibTableColumn
ceDiagHMTestEnabled = _CeDiagHMTestEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 7, 2, 1, 1),
    _CeDiagHMTestEnabled_Type()
)
ceDiagHMTestEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceDiagHMTestEnabled.setStatus("current")


class _CeDiagHMTestIntervalMin_Type(Unsigned32):
    """Custom type ceDiagHMTestIntervalMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CeDiagHMTestIntervalMin_Type.__name__ = "Unsigned32"
_CeDiagHMTestIntervalMin_Object = MibTableColumn
ceDiagHMTestIntervalMin = _CeDiagHMTestIntervalMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 7, 2, 1, 2),
    _CeDiagHMTestIntervalMin_Type()
)
ceDiagHMTestIntervalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDiagHMTestIntervalMin.setStatus("current")
if mibBuilder.loadTexts:
    ceDiagHMTestIntervalMin.setUnits("milliseconds")


class _CeDiagHMTestIntervalDefault_Type(Unsigned32):
    """Custom type ceDiagHMTestIntervalDefault based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CeDiagHMTestIntervalDefault_Type.__name__ = "Unsigned32"
_CeDiagHMTestIntervalDefault_Object = MibTableColumn
ceDiagHMTestIntervalDefault = _CeDiagHMTestIntervalDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 7, 2, 1, 3),
    _CeDiagHMTestIntervalDefault_Type()
)
ceDiagHMTestIntervalDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDiagHMTestIntervalDefault.setStatus("current")
if mibBuilder.loadTexts:
    ceDiagHMTestIntervalDefault.setUnits("milliseconds")


class _CeDiagHMTestInterval_Type(Unsigned32):
    """Custom type ceDiagHMTestInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CeDiagHMTestInterval_Type.__name__ = "Unsigned32"
_CeDiagHMTestInterval_Object = MibTableColumn
ceDiagHMTestInterval = _CeDiagHMTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 7, 2, 1, 4),
    _CeDiagHMTestInterval_Type()
)
ceDiagHMTestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceDiagHMTestInterval.setStatus("current")
if mibBuilder.loadTexts:
    ceDiagHMTestInterval.setUnits("milliseconds")


class _CeDiagHMTestThresholdDefault_Type(Unsigned32):
    """Custom type ceDiagHMTestThresholdDefault based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CeDiagHMTestThresholdDefault_Type.__name__ = "Unsigned32"
_CeDiagHMTestThresholdDefault_Object = MibTableColumn
ceDiagHMTestThresholdDefault = _CeDiagHMTestThresholdDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 7, 2, 1, 5),
    _CeDiagHMTestThresholdDefault_Type()
)
ceDiagHMTestThresholdDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDiagHMTestThresholdDefault.setStatus("current")


class _CeDiagHMTestThreshold_Type(Unsigned32):
    """Custom type ceDiagHMTestThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CeDiagHMTestThreshold_Type.__name__ = "Unsigned32"
_CeDiagHMTestThreshold_Object = MibTableColumn
ceDiagHMTestThreshold = _CeDiagHMTestThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 7, 2, 1, 6),
    _CeDiagHMTestThreshold_Type()
)
ceDiagHMTestThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceDiagHMTestThreshold.setStatus("current")


class _CeDiagHMTestThreshWindowSuite_Type(Integer32):
    """Custom type ceDiagHMTestThreshWindowSuite based on Integer32"""
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
        *(("days", 6),
          ("default", 1),
          ("hours", 5),
          ("milliseconds", 2),
          ("minutes", 4),
          ("runs", 7),
          ("seconds", 3))
    )


_CeDiagHMTestThreshWindowSuite_Type.__name__ = "Integer32"
_CeDiagHMTestThreshWindowSuite_Object = MibTableColumn
ceDiagHMTestThreshWindowSuite = _CeDiagHMTestThreshWindowSuite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 7, 2, 1, 7),
    _CeDiagHMTestThreshWindowSuite_Type()
)
ceDiagHMTestThreshWindowSuite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceDiagHMTestThreshWindowSuite.setStatus("current")


class _CeDiagHMTestThreshWindowSize_Type(Unsigned32):
    """Custom type ceDiagHMTestThreshWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CeDiagHMTestThreshWindowSize_Type.__name__ = "Unsigned32"
_CeDiagHMTestThreshWindowSize_Object = MibTableColumn
ceDiagHMTestThreshWindowSize = _CeDiagHMTestThreshWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 7, 2, 1, 8),
    _CeDiagHMTestThreshWindowSize_Type()
)
ceDiagHMTestThreshWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceDiagHMTestThreshWindowSize.setStatus("current")
_CeDiagEvents_ObjectIdentity = ObjectIdentity
ceDiagEvents = _CeDiagEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 8)
)
_CeDiagEventLogSize_Type = Unsigned32
_CeDiagEventLogSize_Object = MibScalar
ceDiagEventLogSize = _CeDiagEventLogSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 8, 1),
    _CeDiagEventLogSize_Type()
)
ceDiagEventLogSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceDiagEventLogSize.setStatus("current")
_CeDiagEventCount_Type = Unsigned32
_CeDiagEventCount_Object = MibScalar
ceDiagEventCount = _CeDiagEventCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 8, 2),
    _CeDiagEventCount_Type()
)
ceDiagEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDiagEventCount.setStatus("current")
_CeDiagEventMaxQueries_Type = Unsigned32
_CeDiagEventMaxQueries_Object = MibScalar
ceDiagEventMaxQueries = _CeDiagEventMaxQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 8, 3),
    _CeDiagEventMaxQueries_Type()
)
ceDiagEventMaxQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDiagEventMaxQueries.setStatus("current")
_CeDiagEventQueryTable_Object = MibTable
ceDiagEventQueryTable = _CeDiagEventQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 8, 4)
)
if mibBuilder.loadTexts:
    ceDiagEventQueryTable.setStatus("current")
_CeDiagEventQueryEntry_Object = MibTableRow
ceDiagEventQueryEntry = _CeDiagEventQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 8, 4, 1)
)
ceDiagEventQueryEntry.setIndexNames(
    (0, "CISCO-ENTITY-DIAG-MIB", "ceDiagEventQueryIndex"),
)
if mibBuilder.loadTexts:
    ceDiagEventQueryEntry.setStatus("current")
_CeDiagEventQueryIndex_Type = Unsigned32
_CeDiagEventQueryIndex_Object = MibTableColumn
ceDiagEventQueryIndex = _CeDiagEventQueryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 8, 4, 1, 1),
    _CeDiagEventQueryIndex_Type()
)
ceDiagEventQueryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceDiagEventQueryIndex.setStatus("current")
_CeDiagEventQueryPhysicalIndex_Type = EntPhysicalIndexOrZero
_CeDiagEventQueryPhysicalIndex_Object = MibTableColumn
ceDiagEventQueryPhysicalIndex = _CeDiagEventQueryPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 8, 4, 1, 2),
    _CeDiagEventQueryPhysicalIndex_Type()
)
ceDiagEventQueryPhysicalIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceDiagEventQueryPhysicalIndex.setStatus("current")


class _CeDiagEventQuerySeverity_Type(Integer32):
    """Custom type ceDiagEventQuerySeverity based on Integer32"""
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
        *(("all", 0),
          ("error", 3),
          ("info", 1),
          ("warning", 2))
    )


_CeDiagEventQuerySeverity_Type.__name__ = "Integer32"
_CeDiagEventQuerySeverity_Object = MibTableColumn
ceDiagEventQuerySeverity = _CeDiagEventQuerySeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 8, 4, 1, 3),
    _CeDiagEventQuerySeverity_Type()
)
ceDiagEventQuerySeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceDiagEventQuerySeverity.setStatus("current")
_CeDiagEventQueryOwner_Type = SnmpAdminString
_CeDiagEventQueryOwner_Object = MibTableColumn
ceDiagEventQueryOwner = _CeDiagEventQueryOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 8, 4, 1, 4),
    _CeDiagEventQueryOwner_Type()
)
ceDiagEventQueryOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceDiagEventQueryOwner.setStatus("current")


class _CeDiagEventQueryResultingRows_Type(Integer32):
    """Custom type ceDiagEventQueryResultingRows based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_CeDiagEventQueryResultingRows_Type.__name__ = "Integer32"
_CeDiagEventQueryResultingRows_Object = MibTableColumn
ceDiagEventQueryResultingRows = _CeDiagEventQueryResultingRows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 8, 4, 1, 5),
    _CeDiagEventQueryResultingRows_Type()
)
ceDiagEventQueryResultingRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDiagEventQueryResultingRows.setStatus("current")
_CeDiagEventQueryStatus_Type = RowStatus
_CeDiagEventQueryStatus_Object = MibTableColumn
ceDiagEventQueryStatus = _CeDiagEventQueryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 8, 4, 1, 6),
    _CeDiagEventQueryStatus_Type()
)
ceDiagEventQueryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceDiagEventQueryStatus.setStatus("current")
_CeDiagEventResultTable_Object = MibTable
ceDiagEventResultTable = _CeDiagEventResultTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 8, 5)
)
if mibBuilder.loadTexts:
    ceDiagEventResultTable.setStatus("current")
_CeDiagEventResultEntry_Object = MibTableRow
ceDiagEventResultEntry = _CeDiagEventResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 8, 5, 1)
)
ceDiagEventResultEntry.setIndexNames(
    (0, "CISCO-ENTITY-DIAG-MIB", "ceDiagEventQueryIndex"),
    (0, "CISCO-ENTITY-DIAG-MIB", "ceDiagEventResultIndex"),
)
if mibBuilder.loadTexts:
    ceDiagEventResultEntry.setStatus("current")
_CeDiagEventResultIndex_Type = Unsigned32
_CeDiagEventResultIndex_Object = MibTableColumn
ceDiagEventResultIndex = _CeDiagEventResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 8, 5, 1, 1),
    _CeDiagEventResultIndex_Type()
)
ceDiagEventResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceDiagEventResultIndex.setStatus("current")
_CeDiagEventResultPhysicalIndex_Type = PhysicalIndex
_CeDiagEventResultPhysicalIndex_Object = MibTableColumn
ceDiagEventResultPhysicalIndex = _CeDiagEventResultPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 8, 5, 1, 2),
    _CeDiagEventResultPhysicalIndex_Type()
)
ceDiagEventResultPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDiagEventResultPhysicalIndex.setStatus("current")
_CeDiagEventResultPhysicalDescr_Type = SnmpAdminString
_CeDiagEventResultPhysicalDescr_Object = MibTableColumn
ceDiagEventResultPhysicalDescr = _CeDiagEventResultPhysicalDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 8, 5, 1, 3),
    _CeDiagEventResultPhysicalDescr_Type()
)
ceDiagEventResultPhysicalDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDiagEventResultPhysicalDescr.setStatus("current")
_CeDiagEventResultTime_Type = DateAndTime
_CeDiagEventResultTime_Object = MibTableColumn
ceDiagEventResultTime = _CeDiagEventResultTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 8, 5, 1, 4),
    _CeDiagEventResultTime_Type()
)
ceDiagEventResultTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDiagEventResultTime.setStatus("current")


class _CeDiagEventResultSeverity_Type(Integer32):
    """Custom type ceDiagEventResultSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 3),
          ("info", 1),
          ("warning", 2))
    )


_CeDiagEventResultSeverity_Type.__name__ = "Integer32"
_CeDiagEventResultSeverity_Object = MibTableColumn
ceDiagEventResultSeverity = _CeDiagEventResultSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 8, 5, 1, 5),
    _CeDiagEventResultSeverity_Type()
)
ceDiagEventResultSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDiagEventResultSeverity.setStatus("current")
_CeDiagEventResultLogText_Type = SnmpAdminString
_CeDiagEventResultLogText_Object = MibTableColumn
ceDiagEventResultLogText = _CeDiagEventResultLogText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 8, 5, 1, 6),
    _CeDiagEventResultLogText_Type()
)
ceDiagEventResultLogText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDiagEventResultLogText.setStatus("current")
_CeDiagEventErrorMsg_Type = SnmpAdminString
_CeDiagEventErrorMsg_Object = MibScalar
ceDiagEventErrorMsg = _CeDiagEventErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 8, 6),
    _CeDiagEventErrorMsg_Type()
)
ceDiagEventErrorMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ceDiagEventErrorMsg.setStatus("current")
_CeDiagNotificationControl_ObjectIdentity = ObjectIdentity
ceDiagNotificationControl = _CeDiagNotificationControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 9)
)
_CeDiagEnableBootUpFailedNotif_Type = TruthValue
_CeDiagEnableBootUpFailedNotif_Object = MibScalar
ceDiagEnableBootUpFailedNotif = _CeDiagEnableBootUpFailedNotif_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 9, 1),
    _CeDiagEnableBootUpFailedNotif_Type()
)
ceDiagEnableBootUpFailedNotif.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceDiagEnableBootUpFailedNotif.setStatus("current")
_CeDiagEnableHMThreshReachedNotif_Type = TruthValue
_CeDiagEnableHMThreshReachedNotif_Object = MibScalar
ceDiagEnableHMThreshReachedNotif = _CeDiagEnableHMThreshReachedNotif_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 9, 2),
    _CeDiagEnableHMThreshReachedNotif_Type()
)
ceDiagEnableHMThreshReachedNotif.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceDiagEnableHMThreshReachedNotif.setStatus("current")
_CeDiagEnableHMTestRecoverNotif_Type = TruthValue
_CeDiagEnableHMTestRecoverNotif_Object = MibScalar
ceDiagEnableHMTestRecoverNotif = _CeDiagEnableHMTestRecoverNotif_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 9, 3),
    _CeDiagEnableHMTestRecoverNotif_Type()
)
ceDiagEnableHMTestRecoverNotif.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceDiagEnableHMTestRecoverNotif.setStatus("current")
_CeDiagEnableSchedTestFailedNotif_Type = TruthValue
_CeDiagEnableSchedTestFailedNotif_Object = MibScalar
ceDiagEnableSchedTestFailedNotif = _CeDiagEnableSchedTestFailedNotif_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 1, 9, 4),
    _CeDiagEnableSchedTestFailedNotif_Type()
)
ceDiagEnableSchedTestFailedNotif.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceDiagEnableSchedTestFailedNotif.setStatus("current")
_CiscoEntityDiagMIBConform_ObjectIdentity = ObjectIdentity
ciscoEntityDiagMIBConform = _CiscoEntityDiagMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 2)
)
_CiscoEntityDiagMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoEntityDiagMIBCompliances = _CiscoEntityDiagMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 2, 1)
)
_CiscoEntityDiagMIBGroups_ObjectIdentity = ObjectIdentity
ciscoEntityDiagMIBGroups = _CiscoEntityDiagMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 2, 2)
)

# Managed Objects groups

ceDiagDescrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 2, 2, 1)
)
ceDiagDescrGroup.setObjects(
      *(("CISCO-ENTITY-DIAG-MIB", "ceDiagTestText"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagTestAttributes"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagTestCustomAttributeDesc"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagErrorText"))
)
if mibBuilder.loadTexts:
    ceDiagDescrGroup.setStatus("current")

ceDiagGlobalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 2, 2, 2)
)
ceDiagGlobalConfigGroup.setObjects(
    ("CISCO-ENTITY-DIAG-MIB", "ceDiagBootupLevel")
)
if mibBuilder.loadTexts:
    ceDiagGlobalConfigGroup.setStatus("current")

ceDiagEntityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 2, 2, 3)
)
ceDiagEntityGroup.setObjects(
      *(("CISCO-ENTITY-DIAG-MIB", "ceDiagEntityBootLevel"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagEntityCurrentTestMethod"))
)
if mibBuilder.loadTexts:
    ceDiagEntityGroup.setStatus("current")

ceDiagEntityImageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 2, 2, 4)
)
ceDiagEntityImageGroup.setObjects(
      *(("CISCO-ENTITY-DIAG-MIB", "ceDiagEntityImageAdminStatus"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagEntityImageOperStatus"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagEntityFieldDiagnosticUrl"))
)
if mibBuilder.loadTexts:
    ceDiagEntityImageGroup.setStatus("current")

ceDiagOnDemandGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 2, 2, 5)
)
ceDiagOnDemandGroup.setObjects(
      *(("CISCO-ENTITY-DIAG-MIB", "ceDiagOnDemandErrorAllowed"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagOnDemandErrorAction"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagOnDemandIterations"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagOnDemandJobSuite"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagOnDemandJobTestList"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagOnDemandJobPortList"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagOnDemandJobRowStatus"))
)
if mibBuilder.loadTexts:
    ceDiagOnDemandGroup.setStatus("current")

ceDiagScheduledGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 2, 2, 6)
)
ceDiagScheduledGroup.setObjects(
      *(("CISCO-ENTITY-DIAG-MIB", "ceDiagScheduledJobType"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagScheduledJobStart"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagScheduledJobDayOfWeek"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagScheduledJobTestList"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagScheduledJobPortList"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagScheduledJobRowStatus"))
)
if mibBuilder.loadTexts:
    ceDiagScheduledGroup.setStatus("current")

ceDiagTestPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 2, 2, 7)
)
ceDiagTestPerfGroup.setObjects(
      *(("CISCO-ENTITY-DIAG-MIB", "ceDiagTestPerfLastResult"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagTestPerfLastErrorID"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagTestPerfLastRun"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagTestPerfFirstFail"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagTestPerfLastSuccess"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagTestPeffLastFail"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagTestPerfTotalRuns"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagTestPerfTotalFails"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagTestPerfConsecutiveFails"))
)
if mibBuilder.loadTexts:
    ceDiagTestPerfGroup.setStatus("current")

ceDiagHealthMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 2, 2, 8)
)
ceDiagHealthMonitorGroup.setObjects(
      *(("CISCO-ENTITY-DIAG-MIB", "ceDiagHMSyslogEnabled"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagHMTestEnabled"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagHMTestIntervalMin"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagHMTestInterval"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagHMTestIntervalDefault"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagHMTestThresholdDefault"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagHMTestThreshold"))
)
if mibBuilder.loadTexts:
    ceDiagHealthMonitorGroup.setStatus("current")

ceDiagEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 2, 2, 9)
)
ceDiagEventGroup.setObjects(
      *(("CISCO-ENTITY-DIAG-MIB", "ceDiagEventLogSize"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagEventCount"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagEventMaxQueries"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagEventQueryPhysicalIndex"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagEventQuerySeverity"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagEventQueryOwner"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagEventQueryResultingRows"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagEventQueryStatus"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagEventResultPhysicalIndex"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagEventResultPhysicalDescr"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagEventResultTime"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagEventResultSeverity"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagEventResultLogText"))
)
if mibBuilder.loadTexts:
    ceDiagEventGroup.setStatus("current")

ceDiagScheduledJobSuiteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 2, 2, 10)
)
ceDiagScheduledJobSuiteGroup.setObjects(
    ("CISCO-ENTITY-DIAG-MIB", "ceDiagScheduledJobSuite")
)
if mibBuilder.loadTexts:
    ceDiagScheduledJobSuiteGroup.setStatus("current")

ceDiagNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 2, 2, 11)
)
ceDiagNotifControlGroup.setObjects(
      *(("CISCO-ENTITY-DIAG-MIB", "ceDiagEnableBootUpFailedNotif"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagEnableHMThreshReachedNotif"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagEnableHMTestRecoverNotif"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagEnableSchedTestFailedNotif"))
)
if mibBuilder.loadTexts:
    ceDiagNotifControlGroup.setStatus("current")

ceDiagNotifErrorMsgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 2, 2, 12)
)
ceDiagNotifErrorMsgGroup.setObjects(
    ("CISCO-ENTITY-DIAG-MIB", "ceDiagEventErrorMsg")
)
if mibBuilder.loadTexts:
    ceDiagNotifErrorMsgGroup.setStatus("current")

ceDiagTestPerfLastTestMethodGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 2, 2, 14)
)
ceDiagTestPerfLastTestMethodGroup.setObjects(
    ("CISCO-ENTITY-DIAG-MIB", "ceDiagTestPerfLastTestMethod")
)
if mibBuilder.loadTexts:
    ceDiagTestPerfLastTestMethodGroup.setStatus("current")

ceDiagHMTestThreshWindowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 2, 2, 15)
)
ceDiagHMTestThreshWindowGroup.setObjects(
      *(("CISCO-ENTITY-DIAG-MIB", "ceDiagHMTestThreshWindowSuite"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagHMTestThreshWindowSize"))
)
if mibBuilder.loadTexts:
    ceDiagHMTestThreshWindowGroup.setStatus("current")


# Notification objects

ceDiagBootUpFailedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 0, 1)
)
ceDiagBootUpFailedNotif.setObjects(
      *(("ENTITY-MIB", "entPhysicalDescr"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagEntityBootLevel"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagEventErrorMsg"))
)
if mibBuilder.loadTexts:
    ceDiagBootUpFailedNotif.setStatus(
        "current"
    )

ceDiagHMThresholdReachedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 0, 2)
)
ceDiagHMThresholdReachedNotif.setObjects(
      *(("ENTITY-MIB", "entPhysicalDescr"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagHMTestThreshold"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagTestText"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagTestAttributes"))
)
if mibBuilder.loadTexts:
    ceDiagHMThresholdReachedNotif.setStatus(
        "current"
    )

ceDiagHMTestRecoverNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 0, 3)
)
ceDiagHMTestRecoverNotif.setObjects(
      *(("ENTITY-MIB", "entPhysicalDescr"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagTestText"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagTestAttributes"))
)
if mibBuilder.loadTexts:
    ceDiagHMTestRecoverNotif.setStatus(
        "current"
    )

ceDiagScheduledTestFailedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 0, 4)
)
ceDiagScheduledTestFailedNotif.setObjects(
      *(("ENTITY-MIB", "entPhysicalDescr"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagTestText"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagEventErrorMsg"))
)
if mibBuilder.loadTexts:
    ceDiagScheduledTestFailedNotif.setStatus(
        "current"
    )


# Notifications groups

ceDiagNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 2, 2, 13)
)
ceDiagNotificationGroup.setObjects(
      *(("CISCO-ENTITY-DIAG-MIB", "ceDiagBootUpFailedNotif"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagHMThresholdReachedNotif"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagHMTestRecoverNotif"),
        ("CISCO-ENTITY-DIAG-MIB", "ceDiagScheduledTestFailedNotif"))
)
if mibBuilder.loadTexts:
    ceDiagNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoEntityDiagMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoEntityDiagMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoEntityDiagMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoEntityDiagMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoEntityDiagMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoEntityDiagMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoEntityDiagMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 350, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoEntityDiagMIBComplianceRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENTITY-DIAG-MIB",
    **{"ciscoEntityDiagMIB": ciscoEntityDiagMIB,
       "ciscoEntityDiagMIBNotifs": ciscoEntityDiagMIBNotifs,
       "ceDiagBootUpFailedNotif": ceDiagBootUpFailedNotif,
       "ceDiagHMThresholdReachedNotif": ceDiagHMThresholdReachedNotif,
       "ceDiagHMTestRecoverNotif": ceDiagHMTestRecoverNotif,
       "ceDiagScheduledTestFailedNotif": ceDiagScheduledTestFailedNotif,
       "ciscoEntityDiagMIBObjects": ciscoEntityDiagMIBObjects,
       "ceDiagDescriptions": ceDiagDescriptions,
       "ceDiagTestInfoTable": ceDiagTestInfoTable,
       "ceDiagTestInfoEntry": ceDiagTestInfoEntry,
       "ceDiagTestId": ceDiagTestId,
       "ceDiagTestText": ceDiagTestText,
       "ceDiagTestAttributes": ceDiagTestAttributes,
       "ceDiagTestCustomAttributeTable": ceDiagTestCustomAttributeTable,
       "ceDiagTestCustomAttributeEntry": ceDiagTestCustomAttributeEntry,
       "ceDiagTestCustomAttributeIndex": ceDiagTestCustomAttributeIndex,
       "ceDiagTestCustomAttributeDesc": ceDiagTestCustomAttributeDesc,
       "ceDiagErrorInfoTable": ceDiagErrorInfoTable,
       "ceDiagErrorInfoEntry": ceDiagErrorInfoEntry,
       "ceDiagErrorId": ceDiagErrorId,
       "ceDiagErrorText": ceDiagErrorText,
       "ceDiagGlobalConfig": ceDiagGlobalConfig,
       "ceDiagBootupLevel": ceDiagBootupLevel,
       "ceDiagEntity": ceDiagEntity,
       "ceDiagEntityTable": ceDiagEntityTable,
       "ceDiagEntityEntry": ceDiagEntityEntry,
       "ceDiagEntityBootLevel": ceDiagEntityBootLevel,
       "ceDiagEntityImageAdminStatus": ceDiagEntityImageAdminStatus,
       "ceDiagEntityImageOperStatus": ceDiagEntityImageOperStatus,
       "ceDiagEntityFieldDiagnosticUrl": ceDiagEntityFieldDiagnosticUrl,
       "ceDiagEntityCurrentTestTable": ceDiagEntityCurrentTestTable,
       "ceDiagEntityCurrentTestEntry": ceDiagEntityCurrentTestEntry,
       "ceDiagEntityCurrentTestMethod": ceDiagEntityCurrentTestMethod,
       "ceDiagOnDemand": ceDiagOnDemand,
       "ceDiagOnDemandErrorAllowed": ceDiagOnDemandErrorAllowed,
       "ceDiagOnDemandErrorAction": ceDiagOnDemandErrorAction,
       "ceDiagOnDemandIterations": ceDiagOnDemandIterations,
       "ceDiagOnDemandJobTable": ceDiagOnDemandJobTable,
       "ceDiagOnDemandJobEntry": ceDiagOnDemandJobEntry,
       "ceDiagOnDemandJobSuite": ceDiagOnDemandJobSuite,
       "ceDiagOnDemandJobTestList": ceDiagOnDemandJobTestList,
       "ceDiagOnDemandJobPortList": ceDiagOnDemandJobPortList,
       "ceDiagOnDemandJobRowStatus": ceDiagOnDemandJobRowStatus,
       "ceDiagScheduled": ceDiagScheduled,
       "ceDiagScheduledJobTable": ceDiagScheduledJobTable,
       "ceDiagScheduledJobEntry": ceDiagScheduledJobEntry,
       "ceDiagScheduledJobIndex": ceDiagScheduledJobIndex,
       "ceDiagScheduledJobType": ceDiagScheduledJobType,
       "ceDiagScheduledJobStart": ceDiagScheduledJobStart,
       "ceDiagScheduledJobDayOfWeek": ceDiagScheduledJobDayOfWeek,
       "ceDiagScheduledJobTestList": ceDiagScheduledJobTestList,
       "ceDiagScheduledJobPortList": ceDiagScheduledJobPortList,
       "ceDiagScheduledJobRowStatus": ceDiagScheduledJobRowStatus,
       "ceDiagScheduledJobSuite": ceDiagScheduledJobSuite,
       "ceDiagTest": ceDiagTest,
       "ceDiagTestPerfTable": ceDiagTestPerfTable,
       "ceDiagTestPerfEntry": ceDiagTestPerfEntry,
       "ceDiagTestPerfLastResult": ceDiagTestPerfLastResult,
       "ceDiagTestPerfLastErrorID": ceDiagTestPerfLastErrorID,
       "ceDiagTestPerfLastRun": ceDiagTestPerfLastRun,
       "ceDiagTestPerfFirstFail": ceDiagTestPerfFirstFail,
       "ceDiagTestPerfLastSuccess": ceDiagTestPerfLastSuccess,
       "ceDiagTestPeffLastFail": ceDiagTestPeffLastFail,
       "ceDiagTestPerfTotalRuns": ceDiagTestPerfTotalRuns,
       "ceDiagTestPerfTotalFails": ceDiagTestPerfTotalFails,
       "ceDiagTestPerfConsecutiveFails": ceDiagTestPerfConsecutiveFails,
       "ceDiagTestPerfLastTestMethod": ceDiagTestPerfLastTestMethod,
       "ceDiagHealthMonitor": ceDiagHealthMonitor,
       "ceDiagHMSyslogEnabled": ceDiagHMSyslogEnabled,
       "ceDiagHMTestTable": ceDiagHMTestTable,
       "ceDiagHMTestEntry": ceDiagHMTestEntry,
       "ceDiagHMTestEnabled": ceDiagHMTestEnabled,
       "ceDiagHMTestIntervalMin": ceDiagHMTestIntervalMin,
       "ceDiagHMTestIntervalDefault": ceDiagHMTestIntervalDefault,
       "ceDiagHMTestInterval": ceDiagHMTestInterval,
       "ceDiagHMTestThresholdDefault": ceDiagHMTestThresholdDefault,
       "ceDiagHMTestThreshold": ceDiagHMTestThreshold,
       "ceDiagHMTestThreshWindowSuite": ceDiagHMTestThreshWindowSuite,
       "ceDiagHMTestThreshWindowSize": ceDiagHMTestThreshWindowSize,
       "ceDiagEvents": ceDiagEvents,
       "ceDiagEventLogSize": ceDiagEventLogSize,
       "ceDiagEventCount": ceDiagEventCount,
       "ceDiagEventMaxQueries": ceDiagEventMaxQueries,
       "ceDiagEventQueryTable": ceDiagEventQueryTable,
       "ceDiagEventQueryEntry": ceDiagEventQueryEntry,
       "ceDiagEventQueryIndex": ceDiagEventQueryIndex,
       "ceDiagEventQueryPhysicalIndex": ceDiagEventQueryPhysicalIndex,
       "ceDiagEventQuerySeverity": ceDiagEventQuerySeverity,
       "ceDiagEventQueryOwner": ceDiagEventQueryOwner,
       "ceDiagEventQueryResultingRows": ceDiagEventQueryResultingRows,
       "ceDiagEventQueryStatus": ceDiagEventQueryStatus,
       "ceDiagEventResultTable": ceDiagEventResultTable,
       "ceDiagEventResultEntry": ceDiagEventResultEntry,
       "ceDiagEventResultIndex": ceDiagEventResultIndex,
       "ceDiagEventResultPhysicalIndex": ceDiagEventResultPhysicalIndex,
       "ceDiagEventResultPhysicalDescr": ceDiagEventResultPhysicalDescr,
       "ceDiagEventResultTime": ceDiagEventResultTime,
       "ceDiagEventResultSeverity": ceDiagEventResultSeverity,
       "ceDiagEventResultLogText": ceDiagEventResultLogText,
       "ceDiagEventErrorMsg": ceDiagEventErrorMsg,
       "ceDiagNotificationControl": ceDiagNotificationControl,
       "ceDiagEnableBootUpFailedNotif": ceDiagEnableBootUpFailedNotif,
       "ceDiagEnableHMThreshReachedNotif": ceDiagEnableHMThreshReachedNotif,
       "ceDiagEnableHMTestRecoverNotif": ceDiagEnableHMTestRecoverNotif,
       "ceDiagEnableSchedTestFailedNotif": ceDiagEnableSchedTestFailedNotif,
       "ciscoEntityDiagMIBConform": ciscoEntityDiagMIBConform,
       "ciscoEntityDiagMIBCompliances": ciscoEntityDiagMIBCompliances,
       "ciscoEntityDiagMIBComplianceRev1": ciscoEntityDiagMIBComplianceRev1,
       "ciscoEntityDiagMIBComplianceRev2": ciscoEntityDiagMIBComplianceRev2,
       "ciscoEntityDiagMIBComplianceRev3": ciscoEntityDiagMIBComplianceRev3,
       "ciscoEntityDiagMIBComplianceRev4": ciscoEntityDiagMIBComplianceRev4,
       "ciscoEntityDiagMIBGroups": ciscoEntityDiagMIBGroups,
       "ceDiagDescrGroup": ceDiagDescrGroup,
       "ceDiagGlobalConfigGroup": ceDiagGlobalConfigGroup,
       "ceDiagEntityGroup": ceDiagEntityGroup,
       "ceDiagEntityImageGroup": ceDiagEntityImageGroup,
       "ceDiagOnDemandGroup": ceDiagOnDemandGroup,
       "ceDiagScheduledGroup": ceDiagScheduledGroup,
       "ceDiagTestPerfGroup": ceDiagTestPerfGroup,
       "ceDiagHealthMonitorGroup": ceDiagHealthMonitorGroup,
       "ceDiagEventGroup": ceDiagEventGroup,
       "ceDiagScheduledJobSuiteGroup": ceDiagScheduledJobSuiteGroup,
       "ceDiagNotifControlGroup": ceDiagNotifControlGroup,
       "ceDiagNotifErrorMsgGroup": ceDiagNotifErrorMsgGroup,
       "ceDiagNotificationGroup": ceDiagNotificationGroup,
       "ceDiagTestPerfLastTestMethodGroup": ceDiagTestPerfLastTestMethodGroup,
       "ceDiagHMTestThreshWindowGroup": ceDiagHMTestThreshWindowGroup}
)
