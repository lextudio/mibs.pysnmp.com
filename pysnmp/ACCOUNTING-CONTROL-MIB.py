# SNMP MIB module (ACCOUNTING-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACCOUNTING-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:16 2024
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TruthValue")


# MODULE-IDENTITY

accountingControlMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 60)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DataCollectionSubtree(ObjectIdentifier, TextualConvention):
    status = "current"


class DataCollectionList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )



class FileIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_AcctngMIBObjects_ObjectIdentity = ObjectIdentity
acctngMIBObjects = _AcctngMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 60, 1)
)
_AcctngSelectionControl_ObjectIdentity = ObjectIdentity
acctngSelectionControl = _AcctngSelectionControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 60, 1, 1)
)
_AcctngSelectionTable_Object = MibTable
acctngSelectionTable = _AcctngSelectionTable_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 1, 1)
)
if mibBuilder.loadTexts:
    acctngSelectionTable.setStatus("current")
_AcctngSelectionEntry_Object = MibTableRow
acctngSelectionEntry = _AcctngSelectionEntry_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 1, 1, 1)
)
acctngSelectionEntry.setIndexNames(
    (0, "ACCOUNTING-CONTROL-MIB", "acctngSelectionIndex"),
)
if mibBuilder.loadTexts:
    acctngSelectionEntry.setStatus("current")


class _AcctngSelectionIndex_Type(Integer32):
    """Custom type acctngSelectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AcctngSelectionIndex_Type.__name__ = "Integer32"
_AcctngSelectionIndex_Object = MibTableColumn
acctngSelectionIndex = _AcctngSelectionIndex_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 1, 1, 1, 1),
    _AcctngSelectionIndex_Type()
)
acctngSelectionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acctngSelectionIndex.setStatus("current")
_AcctngSelectionSubtree_Type = DataCollectionSubtree
_AcctngSelectionSubtree_Object = MibTableColumn
acctngSelectionSubtree = _AcctngSelectionSubtree_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 1, 1, 1, 2),
    _AcctngSelectionSubtree_Type()
)
acctngSelectionSubtree.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acctngSelectionSubtree.setStatus("current")
_AcctngSelectionList_Type = DataCollectionList
_AcctngSelectionList_Object = MibTableColumn
acctngSelectionList = _AcctngSelectionList_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 1, 1, 1, 3),
    _AcctngSelectionList_Type()
)
acctngSelectionList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acctngSelectionList.setStatus("current")
_AcctngSelectionFile_Type = FileIndex
_AcctngSelectionFile_Object = MibTableColumn
acctngSelectionFile = _AcctngSelectionFile_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 1, 1, 1, 4),
    _AcctngSelectionFile_Type()
)
acctngSelectionFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acctngSelectionFile.setStatus("current")


class _AcctngSelectionType_Type(Bits):
    """Custom type acctngSelectionType based on Bits"""
    defaultBinValue = "1111"

    namedValues = NamedValues(
        *(("pvc", 4),
          ("pvp", 5),
          ("spvcOriginator", 6),
          ("spvcTarget", 7),
          ("spvpOriginator", 8),
          ("spvpTarget", 9),
          ("svcIncoming", 0),
          ("svcOutgoing", 1),
          ("svpIncoming", 2),
          ("svpOutgoing", 3))
    )

_AcctngSelectionType_Type.__name__ = "Bits"
_AcctngSelectionType_Object = MibTableColumn
acctngSelectionType = _AcctngSelectionType_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 1, 1, 1, 5),
    _AcctngSelectionType_Type()
)
acctngSelectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acctngSelectionType.setStatus("current")
_AcctngSelectionRowStatus_Type = RowStatus
_AcctngSelectionRowStatus_Object = MibTableColumn
acctngSelectionRowStatus = _AcctngSelectionRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 1, 1, 1, 6),
    _AcctngSelectionRowStatus_Type()
)
acctngSelectionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acctngSelectionRowStatus.setStatus("current")
_AcctngFileControl_ObjectIdentity = ObjectIdentity
acctngFileControl = _AcctngFileControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 60, 1, 2)
)
_AcctngFileTable_Object = MibTable
acctngFileTable = _AcctngFileTable_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 2, 1)
)
if mibBuilder.loadTexts:
    acctngFileTable.setStatus("current")
_AcctngFileEntry_Object = MibTableRow
acctngFileEntry = _AcctngFileEntry_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 2, 1, 1)
)
acctngFileEntry.setIndexNames(
    (0, "ACCOUNTING-CONTROL-MIB", "acctngFileIndex"),
)
if mibBuilder.loadTexts:
    acctngFileEntry.setStatus("current")
_AcctngFileIndex_Type = FileIndex
_AcctngFileIndex_Object = MibTableColumn
acctngFileIndex = _AcctngFileIndex_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 2, 1, 1, 1),
    _AcctngFileIndex_Type()
)
acctngFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acctngFileIndex.setStatus("current")


class _AcctngFileName_Type(DisplayString):
    """Custom type acctngFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AcctngFileName_Type.__name__ = "DisplayString"
_AcctngFileName_Object = MibTableColumn
acctngFileName = _AcctngFileName_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 2, 1, 1, 2),
    _AcctngFileName_Type()
)
acctngFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acctngFileName.setStatus("current")


class _AcctngFileNameSuffix_Type(DisplayString):
    """Custom type acctngFileNameSuffix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AcctngFileNameSuffix_Type.__name__ = "DisplayString"
_AcctngFileNameSuffix_Object = MibTableColumn
acctngFileNameSuffix = _AcctngFileNameSuffix_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 2, 1, 1, 3),
    _AcctngFileNameSuffix_Type()
)
acctngFileNameSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acctngFileNameSuffix.setStatus("current")
_AcctngFileDescription_Type = DisplayString
_AcctngFileDescription_Object = MibTableColumn
acctngFileDescription = _AcctngFileDescription_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 2, 1, 1, 4),
    _AcctngFileDescription_Type()
)
acctngFileDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acctngFileDescription.setStatus("current")


class _AcctngFileCommand_Type(Integer32):
    """Custom type acctngFileCommand based on Integer32"""
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
        *(("cmdInProgress", 2),
          ("collectNow", 4),
          ("idle", 1),
          ("swapToNewFile", 3))
    )


_AcctngFileCommand_Type.__name__ = "Integer32"
_AcctngFileCommand_Object = MibTableColumn
acctngFileCommand = _AcctngFileCommand_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 2, 1, 1, 5),
    _AcctngFileCommand_Type()
)
acctngFileCommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acctngFileCommand.setStatus("current")


class _AcctngFileMaximumSize_Type(Integer32):
    """Custom type acctngFileMaximumSize based on Integer32"""
    defaultValue = 5000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 2147483647),
    )


_AcctngFileMaximumSize_Type.__name__ = "Integer32"
_AcctngFileMaximumSize_Object = MibTableColumn
acctngFileMaximumSize = _AcctngFileMaximumSize_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 2, 1, 1, 6),
    _AcctngFileMaximumSize_Type()
)
acctngFileMaximumSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acctngFileMaximumSize.setStatus("current")
if mibBuilder.loadTexts:
    acctngFileMaximumSize.setUnits("bytes")


class _AcctngFileCurrentSize_Type(Integer32):
    """Custom type acctngFileCurrentSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcctngFileCurrentSize_Type.__name__ = "Integer32"
_AcctngFileCurrentSize_Object = MibTableColumn
acctngFileCurrentSize = _AcctngFileCurrentSize_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 2, 1, 1, 7),
    _AcctngFileCurrentSize_Type()
)
acctngFileCurrentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acctngFileCurrentSize.setStatus("current")
if mibBuilder.loadTexts:
    acctngFileCurrentSize.setUnits("bytes")


class _AcctngFileFormat_Type(Integer32):
    """Custom type acctngFileFormat based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ber", 2),
          ("other", 1))
    )


_AcctngFileFormat_Type.__name__ = "Integer32"
_AcctngFileFormat_Object = MibTableColumn
acctngFileFormat = _AcctngFileFormat_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 2, 1, 1, 8),
    _AcctngFileFormat_Type()
)
acctngFileFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acctngFileFormat.setStatus("current")


class _AcctngFileCollectMode_Type(Bits):
    """Custom type acctngFileCollectMode based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("onRelease", 0),
          ("periodically", 1))
    )

_AcctngFileCollectMode_Type.__name__ = "Bits"
_AcctngFileCollectMode_Object = MibTableColumn
acctngFileCollectMode = _AcctngFileCollectMode_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 2, 1, 1, 9),
    _AcctngFileCollectMode_Type()
)
acctngFileCollectMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acctngFileCollectMode.setStatus("current")


class _AcctngFileCollectFailedAttempts_Type(Bits):
    """Custom type acctngFileCollectFailedAttempts based on Bits"""
    defaultBinValue = "11"

    namedValues = NamedValues(
        *(("regular", 1),
          ("soft", 0))
    )

_AcctngFileCollectFailedAttempts_Type.__name__ = "Bits"
_AcctngFileCollectFailedAttempts_Object = MibTableColumn
acctngFileCollectFailedAttempts = _AcctngFileCollectFailedAttempts_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 2, 1, 1, 10),
    _AcctngFileCollectFailedAttempts_Type()
)
acctngFileCollectFailedAttempts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acctngFileCollectFailedAttempts.setStatus("current")


class _AcctngFileInterval_Type(Integer32):
    """Custom type acctngFileInterval based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_AcctngFileInterval_Type.__name__ = "Integer32"
_AcctngFileInterval_Object = MibTableColumn
acctngFileInterval = _AcctngFileInterval_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 2, 1, 1, 11),
    _AcctngFileInterval_Type()
)
acctngFileInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acctngFileInterval.setStatus("current")
if mibBuilder.loadTexts:
    acctngFileInterval.setUnits("seconds")


class _AcctngFileMinAge_Type(Integer32):
    """Custom type acctngFileMinAge based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_AcctngFileMinAge_Type.__name__ = "Integer32"
_AcctngFileMinAge_Object = MibTableColumn
acctngFileMinAge = _AcctngFileMinAge_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 2, 1, 1, 12),
    _AcctngFileMinAge_Type()
)
acctngFileMinAge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acctngFileMinAge.setStatus("current")
if mibBuilder.loadTexts:
    acctngFileMinAge.setUnits("seconds")
_AcctngFileRowStatus_Type = RowStatus
_AcctngFileRowStatus_Object = MibTableColumn
acctngFileRowStatus = _AcctngFileRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 2, 1, 1, 13),
    _AcctngFileRowStatus_Type()
)
acctngFileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acctngFileRowStatus.setStatus("current")
_AcctngInterfaceControl_ObjectIdentity = ObjectIdentity
acctngInterfaceControl = _AcctngInterfaceControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 60, 1, 3)
)


class _AcctngAdminStatus_Type(Integer32):
    """Custom type acctngAdminStatus based on Integer32"""
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


_AcctngAdminStatus_Type.__name__ = "Integer32"
_AcctngAdminStatus_Object = MibScalar
acctngAdminStatus = _AcctngAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 3, 1),
    _AcctngAdminStatus_Type()
)
acctngAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acctngAdminStatus.setStatus("current")


class _AcctngOperStatus_Type(Integer32):
    """Custom type acctngOperStatus based on Integer32"""
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


_AcctngOperStatus_Type.__name__ = "Integer32"
_AcctngOperStatus_Object = MibScalar
acctngOperStatus = _AcctngOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 3, 2),
    _AcctngOperStatus_Type()
)
acctngOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acctngOperStatus.setStatus("current")
_AcctngProtection_Type = TestAndIncr
_AcctngProtection_Object = MibScalar
acctngProtection = _AcctngProtection_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 3, 3),
    _AcctngProtection_Type()
)
acctngProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acctngProtection.setStatus("current")


class _AcctngAgentMode_Type(Integer32):
    """Custom type acctngAgentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("swapOnCommand", 1),
          ("swapOnFull", 2))
    )


_AcctngAgentMode_Type.__name__ = "Integer32"
_AcctngAgentMode_Object = MibScalar
acctngAgentMode = _AcctngAgentMode_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 3, 4),
    _AcctngAgentMode_Type()
)
acctngAgentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acctngAgentMode.setStatus("current")
_AcctngInterfaceTable_Object = MibTable
acctngInterfaceTable = _AcctngInterfaceTable_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 3, 5)
)
if mibBuilder.loadTexts:
    acctngInterfaceTable.setStatus("current")
_AcctngInterfaceEntry_Object = MibTableRow
acctngInterfaceEntry = _AcctngInterfaceEntry_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 3, 5, 1)
)
acctngInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    acctngInterfaceEntry.setStatus("current")
_AcctngInterfaceEnable_Type = TruthValue
_AcctngInterfaceEnable_Object = MibTableColumn
acctngInterfaceEnable = _AcctngInterfaceEnable_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 3, 5, 1, 1),
    _AcctngInterfaceEnable_Type()
)
acctngInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acctngInterfaceEnable.setStatus("current")
_AcctngTrapControl_ObjectIdentity = ObjectIdentity
acctngTrapControl = _AcctngTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 60, 1, 4)
)


class _AcctngControlTrapThreshold_Type(Integer32):
    """Custom type acctngControlTrapThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AcctngControlTrapThreshold_Type.__name__ = "Integer32"
_AcctngControlTrapThreshold_Object = MibScalar
acctngControlTrapThreshold = _AcctngControlTrapThreshold_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 4, 1),
    _AcctngControlTrapThreshold_Type()
)
acctngControlTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acctngControlTrapThreshold.setStatus("current")
_AcctngControlTrapEnable_Type = TruthValue
_AcctngControlTrapEnable_Object = MibScalar
acctngControlTrapEnable = _AcctngControlTrapEnable_Object(
    (1, 3, 6, 1, 2, 1, 60, 1, 4, 2),
    _AcctngControlTrapEnable_Type()
)
acctngControlTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acctngControlTrapEnable.setStatus("current")
_AcctngNotifications_ObjectIdentity = ObjectIdentity
acctngNotifications = _AcctngNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 60, 2)
)
_AcctngNotifyPrefix_ObjectIdentity = ObjectIdentity
acctngNotifyPrefix = _AcctngNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 60, 2, 0)
)
_AcctngConformance_ObjectIdentity = ObjectIdentity
acctngConformance = _AcctngConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 60, 3)
)
_AcctngGroups_ObjectIdentity = ObjectIdentity
acctngGroups = _AcctngGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 60, 3, 1)
)
_AcctngCompliances_ObjectIdentity = ObjectIdentity
acctngCompliances = _AcctngCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 60, 3, 2)
)

# Managed Objects groups

acctngBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 60, 3, 1, 1)
)
acctngBasicGroup.setObjects(
      *(("ACCOUNTING-CONTROL-MIB", "acctngSelectionSubtree"),
        ("ACCOUNTING-CONTROL-MIB", "acctngSelectionList"),
        ("ACCOUNTING-CONTROL-MIB", "acctngSelectionFile"),
        ("ACCOUNTING-CONTROL-MIB", "acctngSelectionType"),
        ("ACCOUNTING-CONTROL-MIB", "acctngSelectionRowStatus"),
        ("ACCOUNTING-CONTROL-MIB", "acctngFileName"),
        ("ACCOUNTING-CONTROL-MIB", "acctngFileNameSuffix"),
        ("ACCOUNTING-CONTROL-MIB", "acctngFileDescription"),
        ("ACCOUNTING-CONTROL-MIB", "acctngFileCommand"),
        ("ACCOUNTING-CONTROL-MIB", "acctngFileMaximumSize"),
        ("ACCOUNTING-CONTROL-MIB", "acctngFileCurrentSize"),
        ("ACCOUNTING-CONTROL-MIB", "acctngFileRowStatus"),
        ("ACCOUNTING-CONTROL-MIB", "acctngFileFormat"),
        ("ACCOUNTING-CONTROL-MIB", "acctngFileCollectMode"),
        ("ACCOUNTING-CONTROL-MIB", "acctngFileCollectFailedAttempts"),
        ("ACCOUNTING-CONTROL-MIB", "acctngFileInterval"),
        ("ACCOUNTING-CONTROL-MIB", "acctngFileMinAge"),
        ("ACCOUNTING-CONTROL-MIB", "acctngAdminStatus"),
        ("ACCOUNTING-CONTROL-MIB", "acctngOperStatus"),
        ("ACCOUNTING-CONTROL-MIB", "acctngProtection"),
        ("ACCOUNTING-CONTROL-MIB", "acctngAgentMode"),
        ("ACCOUNTING-CONTROL-MIB", "acctngInterfaceEnable"),
        ("ACCOUNTING-CONTROL-MIB", "acctngControlTrapThreshold"),
        ("ACCOUNTING-CONTROL-MIB", "acctngControlTrapEnable"))
)
if mibBuilder.loadTexts:
    acctngBasicGroup.setStatus("current")


# Notification objects

acctngFileNearlyFull = NotificationType(
    (1, 3, 6, 1, 2, 1, 60, 2, 0, 1)
)
acctngFileNearlyFull.setObjects(
      *(("ACCOUNTING-CONTROL-MIB", "acctngFileName"),
        ("ACCOUNTING-CONTROL-MIB", "acctngFileMaximumSize"),
        ("ACCOUNTING-CONTROL-MIB", "acctngControlTrapThreshold"),
        ("ACCOUNTING-CONTROL-MIB", "acctngFileNameSuffix"))
)
if mibBuilder.loadTexts:
    acctngFileNearlyFull.setStatus(
        "current"
    )

acctngFileFull = NotificationType(
    (1, 3, 6, 1, 2, 1, 60, 2, 0, 2)
)
acctngFileFull.setObjects(
      *(("ACCOUNTING-CONTROL-MIB", "acctngFileName"),
        ("ACCOUNTING-CONTROL-MIB", "acctngFileMaximumSize"),
        ("ACCOUNTING-CONTROL-MIB", "acctngFileNameSuffix"))
)
if mibBuilder.loadTexts:
    acctngFileFull.setStatus(
        "current"
    )


# Notifications groups

acctngNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 60, 3, 1, 2)
)
acctngNotificationsGroup.setObjects(
      *(("ACCOUNTING-CONTROL-MIB", "acctngFileNearlyFull"),
        ("ACCOUNTING-CONTROL-MIB", "acctngFileFull"))
)
if mibBuilder.loadTexts:
    acctngNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

acctngCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 60, 3, 2, 1)
)
if mibBuilder.loadTexts:
    acctngCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACCOUNTING-CONTROL-MIB",
    **{"DataCollectionSubtree": DataCollectionSubtree,
       "DataCollectionList": DataCollectionList,
       "FileIndex": FileIndex,
       "accountingControlMIB": accountingControlMIB,
       "acctngMIBObjects": acctngMIBObjects,
       "acctngSelectionControl": acctngSelectionControl,
       "acctngSelectionTable": acctngSelectionTable,
       "acctngSelectionEntry": acctngSelectionEntry,
       "acctngSelectionIndex": acctngSelectionIndex,
       "acctngSelectionSubtree": acctngSelectionSubtree,
       "acctngSelectionList": acctngSelectionList,
       "acctngSelectionFile": acctngSelectionFile,
       "acctngSelectionType": acctngSelectionType,
       "acctngSelectionRowStatus": acctngSelectionRowStatus,
       "acctngFileControl": acctngFileControl,
       "acctngFileTable": acctngFileTable,
       "acctngFileEntry": acctngFileEntry,
       "acctngFileIndex": acctngFileIndex,
       "acctngFileName": acctngFileName,
       "acctngFileNameSuffix": acctngFileNameSuffix,
       "acctngFileDescription": acctngFileDescription,
       "acctngFileCommand": acctngFileCommand,
       "acctngFileMaximumSize": acctngFileMaximumSize,
       "acctngFileCurrentSize": acctngFileCurrentSize,
       "acctngFileFormat": acctngFileFormat,
       "acctngFileCollectMode": acctngFileCollectMode,
       "acctngFileCollectFailedAttempts": acctngFileCollectFailedAttempts,
       "acctngFileInterval": acctngFileInterval,
       "acctngFileMinAge": acctngFileMinAge,
       "acctngFileRowStatus": acctngFileRowStatus,
       "acctngInterfaceControl": acctngInterfaceControl,
       "acctngAdminStatus": acctngAdminStatus,
       "acctngOperStatus": acctngOperStatus,
       "acctngProtection": acctngProtection,
       "acctngAgentMode": acctngAgentMode,
       "acctngInterfaceTable": acctngInterfaceTable,
       "acctngInterfaceEntry": acctngInterfaceEntry,
       "acctngInterfaceEnable": acctngInterfaceEnable,
       "acctngTrapControl": acctngTrapControl,
       "acctngControlTrapThreshold": acctngControlTrapThreshold,
       "acctngControlTrapEnable": acctngControlTrapEnable,
       "acctngNotifications": acctngNotifications,
       "acctngNotifyPrefix": acctngNotifyPrefix,
       "acctngFileNearlyFull": acctngFileNearlyFull,
       "acctngFileFull": acctngFileFull,
       "acctngConformance": acctngConformance,
       "acctngGroups": acctngGroups,
       "acctngBasicGroup": acctngBasicGroup,
       "acctngNotificationsGroup": acctngNotificationsGroup,
       "acctngCompliances": acctngCompliances,
       "acctngCompliance": acctngCompliance}
)
