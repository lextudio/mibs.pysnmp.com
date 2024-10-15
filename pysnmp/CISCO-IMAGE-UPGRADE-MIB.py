# SNMP MIB module (CISCO-IMAGE-UPGRADE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IMAGE-UPGRADE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:28 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(EntPhysicalIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "EntPhysicalIndexOrZero")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
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

ciscoImageUpgradeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 360)
)
ciscoImageUpgradeMIB.setRevisions(
        ("2011-03-28 00:00",
         "2008-03-18 00:00",
         "2007-07-18 00:00",
         "2006-12-21 00:00",
         "2004-01-20 00:00",
         "2003-11-04 00:00",
         "2003-10-28 00:00",
         "2003-07-11 00:00",
         "2003-07-08 00:00",
         "2003-06-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiuImageVariableTypeName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoImageUpgradeMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoImageUpgradeMIBNotifs = _CiscoImageUpgradeMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 0)
)
_CiscoImageUpgradeMIBObjects_ObjectIdentity = ObjectIdentity
ciscoImageUpgradeMIBObjects = _CiscoImageUpgradeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1)
)
_CiscoImageUpgradeConfig_ObjectIdentity = ObjectIdentity
ciscoImageUpgradeConfig = _CiscoImageUpgradeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1)
)
_CiuTotalImageVariables_Type = Unsigned32
_CiuTotalImageVariables_Object = MibScalar
ciuTotalImageVariables = _CiuTotalImageVariables_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 1),
    _CiuTotalImageVariables_Type()
)
ciuTotalImageVariables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuTotalImageVariables.setStatus("current")
_CiuImageVariableTable_Object = MibTable
ciuImageVariableTable = _CiuImageVariableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ciuImageVariableTable.setStatus("current")
_CiuImageVariableEntry_Object = MibTableRow
ciuImageVariableEntry = _CiuImageVariableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 2, 1)
)
ciuImageVariableEntry.setIndexNames(
    (0, "CISCO-IMAGE-UPGRADE-MIB", "ciuImageVariableName"),
)
if mibBuilder.loadTexts:
    ciuImageVariableEntry.setStatus("current")
_CiuImageVariableName_Type = CiuImageVariableTypeName
_CiuImageVariableName_Object = MibTableColumn
ciuImageVariableName = _CiuImageVariableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 2, 1, 1),
    _CiuImageVariableName_Type()
)
ciuImageVariableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuImageVariableName.setStatus("current")
_CiuImageURITable_Object = MibTable
ciuImageURITable = _CiuImageURITable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ciuImageURITable.setStatus("current")
_CiuImageURIEntry_Object = MibTableRow
ciuImageURIEntry = _CiuImageURIEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 3, 1)
)
ciuImageURIEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-IMAGE-UPGRADE-MIB", "ciuImageVariableName"),
)
if mibBuilder.loadTexts:
    ciuImageURIEntry.setStatus("current")
_CiuImageURI_Type = SnmpAdminString
_CiuImageURI_Object = MibTableColumn
ciuImageURI = _CiuImageURI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 3, 1, 1),
    _CiuImageURI_Type()
)
ciuImageURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciuImageURI.setStatus("current")
_CiscoImageUpgradeOp_ObjectIdentity = ObjectIdentity
ciscoImageUpgradeOp = _CiscoImageUpgradeOp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 4)
)


class _CiuUpgradeOpCommand_Type(Integer32):
    """Custom type ciuUpgradeOpCommand based on Integer32"""
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
        *(("check", 4),
          ("done", 2),
          ("install", 3),
          ("none", 1))
    )


_CiuUpgradeOpCommand_Type.__name__ = "Integer32"
_CiuUpgradeOpCommand_Object = MibScalar
ciuUpgradeOpCommand = _CiuUpgradeOpCommand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 4, 1),
    _CiuUpgradeOpCommand_Type()
)
ciuUpgradeOpCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciuUpgradeOpCommand.setStatus("current")


class _CiuUpgradeOpStatus_Type(Integer32):
    """Custom type ciuUpgradeOpStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("abortFailed", 8),
          ("abortInProgress", 6),
          ("abortSuccess", 7),
          ("failure", 3),
          ("fsUpgReset", 10),
          ("inProgress", 4),
          ("invalidOperation", 2),
          ("none", 1),
          ("success", 5),
          ("successReset", 9))
    )


_CiuUpgradeOpStatus_Type.__name__ = "Integer32"
_CiuUpgradeOpStatus_Object = MibScalar
ciuUpgradeOpStatus = _CiuUpgradeOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 4, 2),
    _CiuUpgradeOpStatus_Type()
)
ciuUpgradeOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuUpgradeOpStatus.setStatus("current")


class _CiuUpgradeOpNotifyOnCompletion_Type(TruthValue):
    """Custom type ciuUpgradeOpNotifyOnCompletion based on TruthValue"""


_CiuUpgradeOpNotifyOnCompletion_Object = MibScalar
ciuUpgradeOpNotifyOnCompletion = _CiuUpgradeOpNotifyOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 4, 3),
    _CiuUpgradeOpNotifyOnCompletion_Type()
)
ciuUpgradeOpNotifyOnCompletion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciuUpgradeOpNotifyOnCompletion.setStatus("current")
_CiuUpgradeOpTimeStarted_Type = TimeStamp
_CiuUpgradeOpTimeStarted_Object = MibScalar
ciuUpgradeOpTimeStarted = _CiuUpgradeOpTimeStarted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 4, 4),
    _CiuUpgradeOpTimeStarted_Type()
)
ciuUpgradeOpTimeStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuUpgradeOpTimeStarted.setStatus("current")
_CiuUpgradeOpTimeCompleted_Type = TimeStamp
_CiuUpgradeOpTimeCompleted_Object = MibScalar
ciuUpgradeOpTimeCompleted = _CiuUpgradeOpTimeCompleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 4, 5),
    _CiuUpgradeOpTimeCompleted_Type()
)
ciuUpgradeOpTimeCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuUpgradeOpTimeCompleted.setStatus("current")


class _CiuUpgradeOpAbort_Type(TruthValue):
    """Custom type ciuUpgradeOpAbort based on TruthValue"""


_CiuUpgradeOpAbort_Object = MibScalar
ciuUpgradeOpAbort = _CiuUpgradeOpAbort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 4, 6),
    _CiuUpgradeOpAbort_Type()
)
ciuUpgradeOpAbort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciuUpgradeOpAbort.setStatus("current")
_CiuUpgradeOpStatusReason_Type = SnmpAdminString
_CiuUpgradeOpStatusReason_Object = MibScalar
ciuUpgradeOpStatusReason = _CiuUpgradeOpStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 4, 7),
    _CiuUpgradeOpStatusReason_Type()
)
ciuUpgradeOpStatusReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuUpgradeOpStatusReason.setStatus("current")


class _CiuUpgradeOpLastCommand_Type(Integer32):
    """Custom type ciuUpgradeOpLastCommand based on Integer32"""
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
        *(("check", 4),
          ("done", 2),
          ("install", 3),
          ("none", 1))
    )


_CiuUpgradeOpLastCommand_Type.__name__ = "Integer32"
_CiuUpgradeOpLastCommand_Object = MibScalar
ciuUpgradeOpLastCommand = _CiuUpgradeOpLastCommand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 4, 8),
    _CiuUpgradeOpLastCommand_Type()
)
ciuUpgradeOpLastCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuUpgradeOpLastCommand.setStatus("current")


class _CiuUpgradeOpLastStatus_Type(Integer32):
    """Custom type ciuUpgradeOpLastStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("abortFailed", 8),
          ("abortInProgress", 6),
          ("abortSuccess", 7),
          ("failure", 3),
          ("fsUpgReset", 10),
          ("inProgress", 4),
          ("invalidOperation", 2),
          ("none", 1),
          ("success", 5),
          ("successReset", 9))
    )


_CiuUpgradeOpLastStatus_Type.__name__ = "Integer32"
_CiuUpgradeOpLastStatus_Object = MibScalar
ciuUpgradeOpLastStatus = _CiuUpgradeOpLastStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 4, 9),
    _CiuUpgradeOpLastStatus_Type()
)
ciuUpgradeOpLastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuUpgradeOpLastStatus.setStatus("current")
_CiuUpgradeOpLastStatusReason_Type = SnmpAdminString
_CiuUpgradeOpLastStatusReason_Object = MibScalar
ciuUpgradeOpLastStatusReason = _CiuUpgradeOpLastStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 4, 10),
    _CiuUpgradeOpLastStatusReason_Type()
)
ciuUpgradeOpLastStatusReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuUpgradeOpLastStatusReason.setStatus("current")
_CiuUpgradeJobStatusNotifyOnCompletion_Type = TruthValue
_CiuUpgradeJobStatusNotifyOnCompletion_Object = MibScalar
ciuUpgradeJobStatusNotifyOnCompletion = _CiuUpgradeJobStatusNotifyOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 4, 11),
    _CiuUpgradeJobStatusNotifyOnCompletion_Type()
)
ciuUpgradeJobStatusNotifyOnCompletion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciuUpgradeJobStatusNotifyOnCompletion.setStatus("current")
_CiuUpgradeTargetTable_Object = MibTable
ciuUpgradeTargetTable = _CiuUpgradeTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ciuUpgradeTargetTable.setStatus("current")
_CiuUpgradeTargetEntry_Object = MibTableRow
ciuUpgradeTargetEntry = _CiuUpgradeTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 5, 1)
)
ciuUpgradeTargetEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ciuUpgradeTargetEntry.setStatus("current")


class _CiuUpgradeTargetAction_Type(Integer32):
    """Custom type ciuUpgradeTargetAction based on Integer32"""
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
        *(("bios", 2),
          ("bootrom", 4),
          ("image", 1),
          ("loader", 3))
    )


_CiuUpgradeTargetAction_Type.__name__ = "Integer32"
_CiuUpgradeTargetAction_Object = MibTableColumn
ciuUpgradeTargetAction = _CiuUpgradeTargetAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 5, 1, 1),
    _CiuUpgradeTargetAction_Type()
)
ciuUpgradeTargetAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciuUpgradeTargetAction.setStatus("current")
_CiuUpgradeTargetEntryStatus_Type = RowStatus
_CiuUpgradeTargetEntryStatus_Object = MibTableColumn
ciuUpgradeTargetEntryStatus = _CiuUpgradeTargetEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 5, 1, 2),
    _CiuUpgradeTargetEntryStatus_Type()
)
ciuUpgradeTargetEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciuUpgradeTargetEntryStatus.setStatus("current")
_CiuImageLocInputTable_Object = MibTable
ciuImageLocInputTable = _CiuImageLocInputTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ciuImageLocInputTable.setStatus("current")
_CiuImageLocInputEntry_Object = MibTableRow
ciuImageLocInputEntry = _CiuImageLocInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 6, 1)
)
ciuImageLocInputEntry.setIndexNames(
    (0, "CISCO-IMAGE-UPGRADE-MIB", "ciuImageVariableName"),
)
if mibBuilder.loadTexts:
    ciuImageLocInputEntry.setStatus("current")


class _CiuImageLocInputURI_Type(SnmpAdminString):
    """Custom type ciuImageLocInputURI based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CiuImageLocInputURI_Type.__name__ = "SnmpAdminString"
_CiuImageLocInputURI_Object = MibTableColumn
ciuImageLocInputURI = _CiuImageLocInputURI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 6, 1, 1),
    _CiuImageLocInputURI_Type()
)
ciuImageLocInputURI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciuImageLocInputURI.setStatus("current")
_CiuImageLocInputEntryStatus_Type = RowStatus
_CiuImageLocInputEntryStatus_Object = MibTableColumn
ciuImageLocInputEntryStatus = _CiuImageLocInputEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 6, 1, 2),
    _CiuImageLocInputEntryStatus_Type()
)
ciuImageLocInputEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciuImageLocInputEntryStatus.setStatus("current")
_CiuVersionCompChkTable_Object = MibTable
ciuVersionCompChkTable = _CiuVersionCompChkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 7)
)
if mibBuilder.loadTexts:
    ciuVersionCompChkTable.setStatus("current")
_CiuVersionCompChkEntry_Object = MibTableRow
ciuVersionCompChkEntry = _CiuVersionCompChkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 7, 1)
)
ciuVersionCompChkEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ciuVersionCompChkEntry.setStatus("current")
_CiuVersionCompImageSame_Type = TruthValue
_CiuVersionCompImageSame_Object = MibTableColumn
ciuVersionCompImageSame = _CiuVersionCompImageSame_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 7, 1, 1),
    _CiuVersionCompImageSame_Type()
)
ciuVersionCompImageSame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuVersionCompImageSame.setStatus("current")
_CiuVersionCompUpgradable_Type = TruthValue
_CiuVersionCompUpgradable_Object = MibTableColumn
ciuVersionCompUpgradable = _CiuVersionCompUpgradable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 7, 1, 2),
    _CiuVersionCompUpgradable_Type()
)
ciuVersionCompUpgradable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuVersionCompUpgradable.setStatus("current")


class _CiuVersionCompUpgradeAction_Type(Integer32):
    """Custom type ciuVersionCompUpgradeAction based on Integer32"""
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
        *(("copy", 6),
          ("none", 1),
          ("notApplicable", 7),
          ("other", 2),
          ("plugin", 8),
          ("reset", 5),
          ("rollingUpgrade", 3),
          ("switchOverReset", 4))
    )


_CiuVersionCompUpgradeAction_Type.__name__ = "Integer32"
_CiuVersionCompUpgradeAction_Object = MibTableColumn
ciuVersionCompUpgradeAction = _CiuVersionCompUpgradeAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 7, 1, 3),
    _CiuVersionCompUpgradeAction_Type()
)
ciuVersionCompUpgradeAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuVersionCompUpgradeAction.setStatus("current")
_CiuVersionCompUpgradeBios_Type = TruthValue
_CiuVersionCompUpgradeBios_Object = MibTableColumn
ciuVersionCompUpgradeBios = _CiuVersionCompUpgradeBios_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 7, 1, 4),
    _CiuVersionCompUpgradeBios_Type()
)
ciuVersionCompUpgradeBios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuVersionCompUpgradeBios.setStatus("current")
_CiuVersionCompUpgradeBootrom_Type = TruthValue
_CiuVersionCompUpgradeBootrom_Object = MibTableColumn
ciuVersionCompUpgradeBootrom = _CiuVersionCompUpgradeBootrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 7, 1, 5),
    _CiuVersionCompUpgradeBootrom_Type()
)
ciuVersionCompUpgradeBootrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuVersionCompUpgradeBootrom.setStatus("current")
_CiuVersionCompUpgradeLoader_Type = TruthValue
_CiuVersionCompUpgradeLoader_Object = MibTableColumn
ciuVersionCompUpgradeLoader = _CiuVersionCompUpgradeLoader_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 7, 1, 6),
    _CiuVersionCompUpgradeLoader_Type()
)
ciuVersionCompUpgradeLoader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuVersionCompUpgradeLoader.setStatus("current")


class _CiuVersionCompUpgradeImpact_Type(Integer32):
    """Custom type ciuVersionCompUpgradeImpact based on Integer32"""
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
        *(("disruptive", 3),
          ("nonDisruptive", 2),
          ("notApplicable", 4),
          ("other", 1))
    )


_CiuVersionCompUpgradeImpact_Type.__name__ = "Integer32"
_CiuVersionCompUpgradeImpact_Object = MibTableColumn
ciuVersionCompUpgradeImpact = _CiuVersionCompUpgradeImpact_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 7, 1, 7),
    _CiuVersionCompUpgradeImpact_Type()
)
ciuVersionCompUpgradeImpact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuVersionCompUpgradeImpact.setStatus("current")
_CiuVersionCompUpgradeReason_Type = SnmpAdminString
_CiuVersionCompUpgradeReason_Object = MibTableColumn
ciuVersionCompUpgradeReason = _CiuVersionCompUpgradeReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 7, 1, 8),
    _CiuVersionCompUpgradeReason_Type()
)
ciuVersionCompUpgradeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuVersionCompUpgradeReason.setStatus("current")
_CiuUpgradeImageVersionTable_Object = MibTable
ciuUpgradeImageVersionTable = _CiuUpgradeImageVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 8)
)
if mibBuilder.loadTexts:
    ciuUpgradeImageVersionTable.setStatus("current")
_CiuUpgradeImageVersionEntry_Object = MibTableRow
ciuUpgradeImageVersionEntry = _CiuUpgradeImageVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 8, 1)
)
ciuUpgradeImageVersionEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeImageVersionIndex"),
)
if mibBuilder.loadTexts:
    ciuUpgradeImageVersionEntry.setStatus("current")
_CiuUpgradeImageVersionIndex_Type = Unsigned32
_CiuUpgradeImageVersionIndex_Object = MibTableColumn
ciuUpgradeImageVersionIndex = _CiuUpgradeImageVersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 8, 1, 1),
    _CiuUpgradeImageVersionIndex_Type()
)
ciuUpgradeImageVersionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciuUpgradeImageVersionIndex.setStatus("current")
_CiuUpgradeImageVersionVarName_Type = CiuImageVariableTypeName
_CiuUpgradeImageVersionVarName_Object = MibTableColumn
ciuUpgradeImageVersionVarName = _CiuUpgradeImageVersionVarName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 8, 1, 2),
    _CiuUpgradeImageVersionVarName_Type()
)
ciuUpgradeImageVersionVarName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuUpgradeImageVersionVarName.setStatus("current")


class _CiuUpgradeImageVersionRunning_Type(SnmpAdminString):
    """Custom type ciuUpgradeImageVersionRunning based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CiuUpgradeImageVersionRunning_Type.__name__ = "SnmpAdminString"
_CiuUpgradeImageVersionRunning_Object = MibTableColumn
ciuUpgradeImageVersionRunning = _CiuUpgradeImageVersionRunning_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 8, 1, 3),
    _CiuUpgradeImageVersionRunning_Type()
)
ciuUpgradeImageVersionRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuUpgradeImageVersionRunning.setStatus("current")


class _CiuUpgradeImageVersionNew_Type(SnmpAdminString):
    """Custom type ciuUpgradeImageVersionNew based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CiuUpgradeImageVersionNew_Type.__name__ = "SnmpAdminString"
_CiuUpgradeImageVersionNew_Object = MibTableColumn
ciuUpgradeImageVersionNew = _CiuUpgradeImageVersionNew_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 8, 1, 4),
    _CiuUpgradeImageVersionNew_Type()
)
ciuUpgradeImageVersionNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuUpgradeImageVersionNew.setStatus("current")
_CiuUpgradeImageVersionUpgReqd_Type = TruthValue
_CiuUpgradeImageVersionUpgReqd_Object = MibTableColumn
ciuUpgradeImageVersionUpgReqd = _CiuUpgradeImageVersionUpgReqd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 8, 1, 5),
    _CiuUpgradeImageVersionUpgReqd_Type()
)
ciuUpgradeImageVersionUpgReqd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuUpgradeImageVersionUpgReqd.setStatus("current")
_CiuUpgradeOpStatusTable_Object = MibTable
ciuUpgradeOpStatusTable = _CiuUpgradeOpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 9)
)
if mibBuilder.loadTexts:
    ciuUpgradeOpStatusTable.setStatus("current")
_CiuUpgradeOpStatusEntry_Object = MibTableRow
ciuUpgradeOpStatusEntry = _CiuUpgradeOpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 9, 1)
)
ciuUpgradeOpStatusEntry.setIndexNames(
    (0, "CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusOperIndex"),
)
if mibBuilder.loadTexts:
    ciuUpgradeOpStatusEntry.setStatus("current")
_CiuUpgradeOpStatusOperIndex_Type = Unsigned32
_CiuUpgradeOpStatusOperIndex_Object = MibTableColumn
ciuUpgradeOpStatusOperIndex = _CiuUpgradeOpStatusOperIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 9, 1, 1),
    _CiuUpgradeOpStatusOperIndex_Type()
)
ciuUpgradeOpStatusOperIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciuUpgradeOpStatusOperIndex.setStatus("current")


class _CiuUpgradeOpStatusOperation_Type(Integer32):
    """Custom type ciuUpgradeOpStatusOperation based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35)
        )
    )
    namedValues = NamedValues(
        *(("additionalInfo", 21),
          ("compactFlashTcamSanity", 34),
          ("configSync", 7),
          ("convertStartUp", 14),
          ("copy", 3),
          ("externalLcWarmBootStatus", 32),
          ("forceDownload", 9),
          ("fsUpgBegin", 28),
          ("fsUpgCleanup", 26),
          ("haSeqNumMismatch", 16),
          ("hitfulLCUpgrade", 12),
          ("hitlessLCUpgrade", 11),
          ("imageSync", 6),
          ("informLcmFsUpg", 23),
          ("informLcmFsUpgExternalLc", 31),
          ("kexecLoadUpgImages", 25),
          ("lcWarmBootStatus", 29),
          ("looseIncompatibility", 15),
          ("moduleOnline", 10),
          ("other", 2),
          ("preUpgrade", 8),
          ("recommendedAction", 18),
          ("recoveryAction", 19),
          ("remainingAction", 20),
          ("saveMtsState", 27),
          ("settingBootvars", 22),
          ("sysmgrSaveRuntimeStateAndSuccessReset", 24),
          ("systemPreupgradeBegin", 35),
          ("total", 33),
          ("unknown", 1),
          ("unknownModuleOnline", 17),
          ("unusedBootvar", 13),
          ("verify", 4),
          ("versionExtraction", 5),
          ("waitStateVerificationStatus", 30))
    )


_CiuUpgradeOpStatusOperation_Type.__name__ = "Integer32"
_CiuUpgradeOpStatusOperation_Object = MibTableColumn
ciuUpgradeOpStatusOperation = _CiuUpgradeOpStatusOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 9, 1, 2),
    _CiuUpgradeOpStatusOperation_Type()
)
ciuUpgradeOpStatusOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuUpgradeOpStatusOperation.setStatus("current")
_CiuUpgradeOpStatusModule_Type = EntPhysicalIndexOrZero
_CiuUpgradeOpStatusModule_Object = MibTableColumn
ciuUpgradeOpStatusModule = _CiuUpgradeOpStatusModule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 9, 1, 3),
    _CiuUpgradeOpStatusModule_Type()
)
ciuUpgradeOpStatusModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuUpgradeOpStatusModule.setStatus("current")
_CiuUpgradeOpStatusSrcImageLoc_Type = SnmpAdminString
_CiuUpgradeOpStatusSrcImageLoc_Object = MibTableColumn
ciuUpgradeOpStatusSrcImageLoc = _CiuUpgradeOpStatusSrcImageLoc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 9, 1, 4),
    _CiuUpgradeOpStatusSrcImageLoc_Type()
)
ciuUpgradeOpStatusSrcImageLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuUpgradeOpStatusSrcImageLoc.setStatus("current")
_CiuUpgradeOpStatusDestImageLoc_Type = SnmpAdminString
_CiuUpgradeOpStatusDestImageLoc_Object = MibTableColumn
ciuUpgradeOpStatusDestImageLoc = _CiuUpgradeOpStatusDestImageLoc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 9, 1, 5),
    _CiuUpgradeOpStatusDestImageLoc_Type()
)
ciuUpgradeOpStatusDestImageLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuUpgradeOpStatusDestImageLoc.setStatus("current")


class _CiuUpgradeOpStatusJobStatus_Type(Integer32):
    """Custom type ciuUpgradeOpStatusJobStatus based on Integer32"""
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
        *(("failed", 3),
          ("inProgress", 4),
          ("other", 2),
          ("planned", 6),
          ("success", 5),
          ("unknown", 1))
    )


_CiuUpgradeOpStatusJobStatus_Type.__name__ = "Integer32"
_CiuUpgradeOpStatusJobStatus_Object = MibTableColumn
ciuUpgradeOpStatusJobStatus = _CiuUpgradeOpStatusJobStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 9, 1, 6),
    _CiuUpgradeOpStatusJobStatus_Type()
)
ciuUpgradeOpStatusJobStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuUpgradeOpStatusJobStatus.setStatus("current")
_CiuUpgradeOpStatusPercentCompl_Type = Integer32
_CiuUpgradeOpStatusPercentCompl_Object = MibTableColumn
ciuUpgradeOpStatusPercentCompl = _CiuUpgradeOpStatusPercentCompl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 9, 1, 7),
    _CiuUpgradeOpStatusPercentCompl_Type()
)
ciuUpgradeOpStatusPercentCompl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuUpgradeOpStatusPercentCompl.setStatus("current")
_CiuUpgradeOpStatusJobStatusReas_Type = SnmpAdminString
_CiuUpgradeOpStatusJobStatusReas_Object = MibTableColumn
ciuUpgradeOpStatusJobStatusReas = _CiuUpgradeOpStatusJobStatusReas_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 9, 1, 8),
    _CiuUpgradeOpStatusJobStatusReas_Type()
)
ciuUpgradeOpStatusJobStatusReas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuUpgradeOpStatusJobStatusReas.setStatus("current")
_CiscoImageUpgradeMisc_ObjectIdentity = ObjectIdentity
ciscoImageUpgradeMisc = _CiscoImageUpgradeMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 10)
)


class _CiuUpgradeMiscAutoCopy_Type(TruthValue):
    """Custom type ciuUpgradeMiscAutoCopy based on TruthValue"""


_CiuUpgradeMiscAutoCopy_Object = MibScalar
ciuUpgradeMiscAutoCopy = _CiuUpgradeMiscAutoCopy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 10, 1),
    _CiuUpgradeMiscAutoCopy_Type()
)
ciuUpgradeMiscAutoCopy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciuUpgradeMiscAutoCopy.setStatus("current")
_CiuUpgradeMiscInfoTable_Object = MibTable
ciuUpgradeMiscInfoTable = _CiuUpgradeMiscInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 11)
)
if mibBuilder.loadTexts:
    ciuUpgradeMiscInfoTable.setStatus("current")
_CiuUpgradeMiscInfoEntry_Object = MibTableRow
ciuUpgradeMiscInfoEntry = _CiuUpgradeMiscInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 11, 1)
)
ciuUpgradeMiscInfoEntry.setIndexNames(
    (0, "CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeMiscInfoIndex"),
)
if mibBuilder.loadTexts:
    ciuUpgradeMiscInfoEntry.setStatus("current")
_CiuUpgradeMiscInfoIndex_Type = Unsigned32
_CiuUpgradeMiscInfoIndex_Object = MibTableColumn
ciuUpgradeMiscInfoIndex = _CiuUpgradeMiscInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 11, 1, 1),
    _CiuUpgradeMiscInfoIndex_Type()
)
ciuUpgradeMiscInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciuUpgradeMiscInfoIndex.setStatus("current")
_CiuUpgradeMiscInfoModule_Type = EntPhysicalIndexOrZero
_CiuUpgradeMiscInfoModule_Object = MibTableColumn
ciuUpgradeMiscInfoModule = _CiuUpgradeMiscInfoModule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 11, 1, 2),
    _CiuUpgradeMiscInfoModule_Type()
)
ciuUpgradeMiscInfoModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuUpgradeMiscInfoModule.setStatus("current")
_CiuUpgradeMiscInfoDescr_Type = SnmpAdminString
_CiuUpgradeMiscInfoDescr_Object = MibTableColumn
ciuUpgradeMiscInfoDescr = _CiuUpgradeMiscInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 1, 1, 11, 1, 3),
    _CiuUpgradeMiscInfoDescr_Type()
)
ciuUpgradeMiscInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuUpgradeMiscInfoDescr.setStatus("current")
_CiscoImageUpgradeMIBConform_ObjectIdentity = ObjectIdentity
ciscoImageUpgradeMIBConform = _CiscoImageUpgradeMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 2)
)
_CiuImageUpgradeCompliances_ObjectIdentity = ObjectIdentity
ciuImageUpgradeCompliances = _CiuImageUpgradeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 1)
)
_CiuImageUpgradeGroups_ObjectIdentity = ObjectIdentity
ciuImageUpgradeGroups = _CiuImageUpgradeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2)
)

# Managed Objects groups

ciuImageUpgradeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2, 1)
)
ciuImageUpgradeGroup.setObjects(
    ("CISCO-IMAGE-UPGRADE-MIB", "ciuTotalImageVariables")
)
if mibBuilder.loadTexts:
    ciuImageUpgradeGroup.setStatus("current")

ciuImageVariableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2, 2)
)
ciuImageVariableGroup.setObjects(
    ("CISCO-IMAGE-UPGRADE-MIB", "ciuImageVariableName")
)
if mibBuilder.loadTexts:
    ciuImageVariableGroup.setStatus("current")

ciuImageURIGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2, 3)
)
ciuImageURIGroup.setObjects(
    ("CISCO-IMAGE-UPGRADE-MIB", "ciuImageURI")
)
if mibBuilder.loadTexts:
    ciuImageURIGroup.setStatus("current")

ciuUpgradeOpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2, 4)
)
ciuUpgradeOpGroup.setObjects(
      *(("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpCommand"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatus"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpNotifyOnCompletion"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpTimeStarted"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpTimeCompleted"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpAbort"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusReason"))
)
if mibBuilder.loadTexts:
    ciuUpgradeOpGroup.setStatus("current")

ciuUpgradeTargetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2, 5)
)
ciuUpgradeTargetGroup.setObjects(
      *(("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeTargetAction"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeTargetEntryStatus"))
)
if mibBuilder.loadTexts:
    ciuUpgradeTargetGroup.setStatus("current")

ciuImageLocInputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2, 6)
)
ciuImageLocInputGroup.setObjects(
      *(("CISCO-IMAGE-UPGRADE-MIB", "ciuImageLocInputURI"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuImageLocInputEntryStatus"))
)
if mibBuilder.loadTexts:
    ciuImageLocInputGroup.setStatus("current")

ciuVersionCompChkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2, 7)
)
ciuVersionCompChkGroup.setObjects(
      *(("CISCO-IMAGE-UPGRADE-MIB", "ciuVersionCompImageSame"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuVersionCompUpgradable"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuVersionCompUpgradeAction"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuVersionCompUpgradeBios"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuVersionCompUpgradeBootrom"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuVersionCompUpgradeLoader"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuVersionCompUpgradeImpact"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuVersionCompUpgradeReason"))
)
if mibBuilder.loadTexts:
    ciuVersionCompChkGroup.setStatus("current")

ciuUpgradeImageVersionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2, 8)
)
ciuUpgradeImageVersionGroup.setObjects(
      *(("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeImageVersionVarName"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeImageVersionRunning"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeImageVersionNew"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeImageVersionUpgReqd"))
)
if mibBuilder.loadTexts:
    ciuUpgradeImageVersionGroup.setStatus("current")

ciuUpgradeOpStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2, 9)
)
ciuUpgradeOpStatusGroup.setObjects(
      *(("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusOperation"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusModule"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusSrcImageLoc"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusDestImageLoc"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusJobStatus"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusPercentCompl"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusJobStatusReas"))
)
if mibBuilder.loadTexts:
    ciuUpgradeOpStatusGroup.setStatus("current")

ciuUpgradeMiscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2, 11)
)
ciuUpgradeMiscGroup.setObjects(
    ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeMiscAutoCopy")
)
if mibBuilder.loadTexts:
    ciuUpgradeMiscGroup.setStatus("current")

ciuUpgradeMiscInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2, 12)
)
ciuUpgradeMiscInfoGroup.setObjects(
      *(("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeMiscInfoModule"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeMiscInfoDescr"))
)
if mibBuilder.loadTexts:
    ciuUpgradeMiscInfoGroup.setStatus("current")

ciuUpgradeOpNewGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2, 14)
)
ciuUpgradeOpNewGroup.setObjects(
      *(("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeJobStatusNotifyOnCompletion"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpLastCommand"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpLastStatus"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpLastStatusReason"))
)
if mibBuilder.loadTexts:
    ciuUpgradeOpNewGroup.setStatus("current")


# Notification objects

ciuUpgradeOpCompletionNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 0, 1)
)
ciuUpgradeOpCompletionNotify.setObjects(
      *(("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpCommand"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatus"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpTimeCompleted"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpLastCommand"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpLastStatus"))
)
if mibBuilder.loadTexts:
    ciuUpgradeOpCompletionNotify.setStatus(
        "current"
    )

ciuUpgradeJobStatusNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 0, 2)
)
ciuUpgradeJobStatusNotify.setObjects(
      *(("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusOperation"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusModule"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusSrcImageLoc"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusDestImageLoc"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusJobStatus"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusPercentCompl"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusJobStatusReas"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatus"),
        ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpStatusReason"))
)
if mibBuilder.loadTexts:
    ciuUpgradeJobStatusNotify.setStatus(
        "current"
    )


# Notifications groups

ciuUpgradeNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2, 10)
)
ciuUpgradeNotificationGroup.setObjects(
    ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeOpCompletionNotify")
)
if mibBuilder.loadTexts:
    ciuUpgradeNotificationGroup.setStatus(
        "current"
    )

ciuUpgradeNotificationGroupSup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 2, 13)
)
ciuUpgradeNotificationGroupSup.setObjects(
    ("CISCO-IMAGE-UPGRADE-MIB", "ciuUpgradeJobStatusNotify")
)
if mibBuilder.loadTexts:
    ciuUpgradeNotificationGroupSup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciuImageUpgradeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciuImageUpgradeCompliance.setStatus(
        "deprecated"
    )

ciuImageUpgradeComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciuImageUpgradeComplianceRev1.setStatus(
        "deprecated"
    )

ciuImageUpgradeComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciuImageUpgradeComplianceRev2.setStatus(
        "deprecated"
    )

ciuImageUpgradeComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciuImageUpgradeComplianceRev3.setStatus(
        "deprecated"
    )

ciuImageUpgradeComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 360, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ciuImageUpgradeComplianceRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IMAGE-UPGRADE-MIB",
    **{"CiuImageVariableTypeName": CiuImageVariableTypeName,
       "ciscoImageUpgradeMIB": ciscoImageUpgradeMIB,
       "ciscoImageUpgradeMIBNotifs": ciscoImageUpgradeMIBNotifs,
       "ciuUpgradeOpCompletionNotify": ciuUpgradeOpCompletionNotify,
       "ciuUpgradeJobStatusNotify": ciuUpgradeJobStatusNotify,
       "ciscoImageUpgradeMIBObjects": ciscoImageUpgradeMIBObjects,
       "ciscoImageUpgradeConfig": ciscoImageUpgradeConfig,
       "ciuTotalImageVariables": ciuTotalImageVariables,
       "ciuImageVariableTable": ciuImageVariableTable,
       "ciuImageVariableEntry": ciuImageVariableEntry,
       "ciuImageVariableName": ciuImageVariableName,
       "ciuImageURITable": ciuImageURITable,
       "ciuImageURIEntry": ciuImageURIEntry,
       "ciuImageURI": ciuImageURI,
       "ciscoImageUpgradeOp": ciscoImageUpgradeOp,
       "ciuUpgradeOpCommand": ciuUpgradeOpCommand,
       "ciuUpgradeOpStatus": ciuUpgradeOpStatus,
       "ciuUpgradeOpNotifyOnCompletion": ciuUpgradeOpNotifyOnCompletion,
       "ciuUpgradeOpTimeStarted": ciuUpgradeOpTimeStarted,
       "ciuUpgradeOpTimeCompleted": ciuUpgradeOpTimeCompleted,
       "ciuUpgradeOpAbort": ciuUpgradeOpAbort,
       "ciuUpgradeOpStatusReason": ciuUpgradeOpStatusReason,
       "ciuUpgradeOpLastCommand": ciuUpgradeOpLastCommand,
       "ciuUpgradeOpLastStatus": ciuUpgradeOpLastStatus,
       "ciuUpgradeOpLastStatusReason": ciuUpgradeOpLastStatusReason,
       "ciuUpgradeJobStatusNotifyOnCompletion": ciuUpgradeJobStatusNotifyOnCompletion,
       "ciuUpgradeTargetTable": ciuUpgradeTargetTable,
       "ciuUpgradeTargetEntry": ciuUpgradeTargetEntry,
       "ciuUpgradeTargetAction": ciuUpgradeTargetAction,
       "ciuUpgradeTargetEntryStatus": ciuUpgradeTargetEntryStatus,
       "ciuImageLocInputTable": ciuImageLocInputTable,
       "ciuImageLocInputEntry": ciuImageLocInputEntry,
       "ciuImageLocInputURI": ciuImageLocInputURI,
       "ciuImageLocInputEntryStatus": ciuImageLocInputEntryStatus,
       "ciuVersionCompChkTable": ciuVersionCompChkTable,
       "ciuVersionCompChkEntry": ciuVersionCompChkEntry,
       "ciuVersionCompImageSame": ciuVersionCompImageSame,
       "ciuVersionCompUpgradable": ciuVersionCompUpgradable,
       "ciuVersionCompUpgradeAction": ciuVersionCompUpgradeAction,
       "ciuVersionCompUpgradeBios": ciuVersionCompUpgradeBios,
       "ciuVersionCompUpgradeBootrom": ciuVersionCompUpgradeBootrom,
       "ciuVersionCompUpgradeLoader": ciuVersionCompUpgradeLoader,
       "ciuVersionCompUpgradeImpact": ciuVersionCompUpgradeImpact,
       "ciuVersionCompUpgradeReason": ciuVersionCompUpgradeReason,
       "ciuUpgradeImageVersionTable": ciuUpgradeImageVersionTable,
       "ciuUpgradeImageVersionEntry": ciuUpgradeImageVersionEntry,
       "ciuUpgradeImageVersionIndex": ciuUpgradeImageVersionIndex,
       "ciuUpgradeImageVersionVarName": ciuUpgradeImageVersionVarName,
       "ciuUpgradeImageVersionRunning": ciuUpgradeImageVersionRunning,
       "ciuUpgradeImageVersionNew": ciuUpgradeImageVersionNew,
       "ciuUpgradeImageVersionUpgReqd": ciuUpgradeImageVersionUpgReqd,
       "ciuUpgradeOpStatusTable": ciuUpgradeOpStatusTable,
       "ciuUpgradeOpStatusEntry": ciuUpgradeOpStatusEntry,
       "ciuUpgradeOpStatusOperIndex": ciuUpgradeOpStatusOperIndex,
       "ciuUpgradeOpStatusOperation": ciuUpgradeOpStatusOperation,
       "ciuUpgradeOpStatusModule": ciuUpgradeOpStatusModule,
       "ciuUpgradeOpStatusSrcImageLoc": ciuUpgradeOpStatusSrcImageLoc,
       "ciuUpgradeOpStatusDestImageLoc": ciuUpgradeOpStatusDestImageLoc,
       "ciuUpgradeOpStatusJobStatus": ciuUpgradeOpStatusJobStatus,
       "ciuUpgradeOpStatusPercentCompl": ciuUpgradeOpStatusPercentCompl,
       "ciuUpgradeOpStatusJobStatusReas": ciuUpgradeOpStatusJobStatusReas,
       "ciscoImageUpgradeMisc": ciscoImageUpgradeMisc,
       "ciuUpgradeMiscAutoCopy": ciuUpgradeMiscAutoCopy,
       "ciuUpgradeMiscInfoTable": ciuUpgradeMiscInfoTable,
       "ciuUpgradeMiscInfoEntry": ciuUpgradeMiscInfoEntry,
       "ciuUpgradeMiscInfoIndex": ciuUpgradeMiscInfoIndex,
       "ciuUpgradeMiscInfoModule": ciuUpgradeMiscInfoModule,
       "ciuUpgradeMiscInfoDescr": ciuUpgradeMiscInfoDescr,
       "ciscoImageUpgradeMIBConform": ciscoImageUpgradeMIBConform,
       "ciuImageUpgradeCompliances": ciuImageUpgradeCompliances,
       "ciuImageUpgradeCompliance": ciuImageUpgradeCompliance,
       "ciuImageUpgradeComplianceRev1": ciuImageUpgradeComplianceRev1,
       "ciuImageUpgradeComplianceRev2": ciuImageUpgradeComplianceRev2,
       "ciuImageUpgradeComplianceRev3": ciuImageUpgradeComplianceRev3,
       "ciuImageUpgradeComplianceRev4": ciuImageUpgradeComplianceRev4,
       "ciuImageUpgradeGroups": ciuImageUpgradeGroups,
       "ciuImageUpgradeGroup": ciuImageUpgradeGroup,
       "ciuImageVariableGroup": ciuImageVariableGroup,
       "ciuImageURIGroup": ciuImageURIGroup,
       "ciuUpgradeOpGroup": ciuUpgradeOpGroup,
       "ciuUpgradeTargetGroup": ciuUpgradeTargetGroup,
       "ciuImageLocInputGroup": ciuImageLocInputGroup,
       "ciuVersionCompChkGroup": ciuVersionCompChkGroup,
       "ciuUpgradeImageVersionGroup": ciuUpgradeImageVersionGroup,
       "ciuUpgradeOpStatusGroup": ciuUpgradeOpStatusGroup,
       "ciuUpgradeNotificationGroup": ciuUpgradeNotificationGroup,
       "ciuUpgradeMiscGroup": ciuUpgradeMiscGroup,
       "ciuUpgradeMiscInfoGroup": ciuUpgradeMiscInfoGroup,
       "ciuUpgradeNotificationGroupSup": ciuUpgradeNotificationGroupSup,
       "ciuUpgradeOpNewGroup": ciuUpgradeOpNewGroup}
)
