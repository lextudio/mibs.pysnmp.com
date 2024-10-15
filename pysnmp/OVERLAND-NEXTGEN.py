# SNMP MIB module (OVERLAND-NEXTGEN) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OVERLAND-NEXTGEN
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:50 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

overlandGlobalRegModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3351, 1, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OverlandRoot_ObjectIdentity = ObjectIdentity
overlandRoot = _OverlandRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3351, 1)
)
_OverlandReg_ObjectIdentity = ObjectIdentity
overlandReg = _OverlandReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3351, 1, 1)
)
_OverlandModules_ObjectIdentity = ObjectIdentity
overlandModules = _OverlandModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3351, 1, 1, 1)
)
_OverlandGeneric_ObjectIdentity = ObjectIdentity
overlandGeneric = _OverlandGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3351, 1, 2)
)
_OverlandProducts_ObjectIdentity = ObjectIdentity
overlandProducts = _OverlandProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3)
)
_OverlandNextGen_ObjectIdentity = ObjectIdentity
overlandNextGen = _OverlandNextGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2)
)
_OverlandNextGenActions_ObjectIdentity = ObjectIdentity
overlandNextGenActions = _OverlandNextGenActions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 1)
)


class _OverlandLoopback_Type(DisplayString):
    """Custom type overlandLoopback based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OverlandLoopback_Type.__name__ = "DisplayString"
_OverlandLoopback_Object = MibScalar
overlandLoopback = _OverlandLoopback_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 1, 1),
    _OverlandLoopback_Type()
)
overlandLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overlandLoopback.setStatus("current")
_OverlandNextGenStatistics_ObjectIdentity = ObjectIdentity
overlandNextGenStatistics = _OverlandNextGenStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 2)
)
_OverlandNextGenState_ObjectIdentity = ObjectIdentity
overlandNextGenState = _OverlandNextGenState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 3)
)
_DriveStatusTable_Object = MibTable
driveStatusTable = _DriveStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    driveStatusTable.setStatus("current")
_DriveStatusEntry_Object = MibTableRow
driveStatusEntry = _DriveStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 3, 1, 1)
)
driveStatusEntry.setIndexNames(
    (0, "OVERLAND-NEXTGEN", "dstIndex"),
)
if mibBuilder.loadTexts:
    driveStatusEntry.setStatus("current")
_DstRowValid_Type = DisplayString
_DstRowValid_Object = MibTableColumn
dstRowValid = _DstRowValid_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 3, 1, 1, 1),
    _DstRowValid_Type()
)
dstRowValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstRowValid.setStatus("current")


class _DstIndex_Type(Integer32):
    """Custom type dstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DstIndex_Type.__name__ = "Integer32"
_DstIndex_Object = MibTableColumn
dstIndex = _DstIndex_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 3, 1, 1, 2),
    _DstIndex_Type()
)
dstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstIndex.setStatus("current")


class _DstState_Type(Integer32):
    """Custom type dstState based on Integer32"""
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
        *(("initializedNoError", 0),
          ("initializedWithError", 1),
          ("notInitialized", 2),
          ("notInserted", 4),
          ("notInstalled", 3))
    )


_DstState_Type.__name__ = "Integer32"
_DstState_Object = MibTableColumn
dstState = _DstState_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 3, 1, 1, 3),
    _DstState_Type()
)
dstState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstState.setStatus("current")
_DstMotion_Type = DisplayString
_DstMotion_Object = MibTableColumn
dstMotion = _DstMotion_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 3, 1, 1, 4),
    _DstMotion_Type()
)
dstMotion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstMotion.setStatus("current")
_DstCodeRevDrive_Type = Integer32
_DstCodeRevDrive_Object = MibTableColumn
dstCodeRevDrive = _DstCodeRevDrive_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 3, 1, 1, 5),
    _DstCodeRevDrive_Type()
)
dstCodeRevDrive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstCodeRevDrive.setStatus("current")
_DstCodeRevController_Type = Integer32
_DstCodeRevController_Object = MibTableColumn
dstCodeRevController = _DstCodeRevController_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 3, 1, 1, 6),
    _DstCodeRevController_Type()
)
dstCodeRevController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstCodeRevController.setStatus("current")


class _DstScsiId_Type(Integer32):
    """Custom type dstScsiId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DstScsiId_Type.__name__ = "Integer32"
_DstScsiId_Object = MibTableColumn
dstScsiId = _DstScsiId_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 3, 1, 1, 7),
    _DstScsiId_Type()
)
dstScsiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstScsiId.setStatus("current")
_DstSerialNum_Type = DisplayString
_DstSerialNum_Object = MibTableColumn
dstSerialNum = _DstSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 3, 1, 1, 8),
    _DstSerialNum_Type()
)
dstSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstSerialNum.setStatus("current")


class _DstCleanRequested_Type(Integer32):
    """Custom type dstCleanRequested based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cleanNeeded", 1),
          ("cleanNotNeeded", 0))
    )


_DstCleanRequested_Type.__name__ = "Integer32"
_DstCleanRequested_Object = MibTableColumn
dstCleanRequested = _DstCleanRequested_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 3, 1, 1, 9),
    _DstCleanRequested_Type()
)
dstCleanRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstCleanRequested.setStatus("current")
_LibraryStatusTable_Object = MibTable
libraryStatusTable = _LibraryStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 3, 2)
)
if mibBuilder.loadTexts:
    libraryStatusTable.setStatus("current")
_LibraryStatusEntry_Object = MibTableRow
libraryStatusEntry = _LibraryStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 3, 2, 1)
)
libraryStatusEntry.setIndexNames(
    (0, "OVERLAND-NEXTGEN", "lstIndex"),
)
if mibBuilder.loadTexts:
    libraryStatusEntry.setStatus("current")


class _LstIndex_Type(Integer32):
    """Custom type lstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_LstIndex_Type.__name__ = "Integer32"
_LstIndex_Object = MibTableColumn
lstIndex = _LstIndex_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 3, 2, 1, 1),
    _LstIndex_Type()
)
lstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lstIndex.setStatus("current")


class _LstConfig_Type(Integer32):
    """Custom type lstConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("multimodule", 1),
          ("standalone", 0))
    )


_LstConfig_Type.__name__ = "Integer32"
_LstConfig_Object = MibTableColumn
lstConfig = _LstConfig_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 3, 2, 1, 2),
    _LstConfig_Type()
)
lstConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lstConfig.setStatus("current")


class _LstScsiId_Type(Integer32):
    """Custom type lstScsiId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_LstScsiId_Type.__name__ = "Integer32"
_LstScsiId_Object = MibTableColumn
lstScsiId = _LstScsiId_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 3, 2, 1, 3),
    _LstScsiId_Type()
)
lstScsiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lstScsiId.setStatus("current")
_LstStatus_Type = DisplayString
_LstStatus_Object = MibTableColumn
lstStatus = _LstStatus_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 3, 2, 1, 4),
    _LstStatus_Type()
)
lstStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lstStatus.setStatus("current")
_LstChangerStatus_Type = Integer32
_LstChangerStatus_Object = MibTableColumn
lstChangerStatus = _LstChangerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 3, 2, 1, 5),
    _LstChangerStatus_Type()
)
lstChangerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lstChangerStatus.setStatus("current")


class _LstLibraryState_Type(Integer32):
    """Custom type lstLibraryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initializing", 0),
          ("offline", 2),
          ("online", 1))
    )


_LstLibraryState_Type.__name__ = "Integer32"
_LstLibraryState_Object = MibTableColumn
lstLibraryState = _LstLibraryState_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 3, 2, 1, 6),
    _LstLibraryState_Type()
)
lstLibraryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lstLibraryState.setStatus("current")
_ErrorTable_Object = MibTable
errorTable = _ErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 3, 3)
)
if mibBuilder.loadTexts:
    errorTable.setStatus("current")
_ErrorEntry_Object = MibTableRow
errorEntry = _ErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 3, 3, 1)
)
errorEntry.setIndexNames(
    (0, "OVERLAND-NEXTGEN", "errIndex"),
)
if mibBuilder.loadTexts:
    errorEntry.setStatus("current")


class _ErrIndex_Type(Integer32):
    """Custom type errIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ErrIndex_Type.__name__ = "Integer32"
_ErrIndex_Object = MibTableColumn
errIndex = _ErrIndex_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 3, 3, 1, 1),
    _ErrIndex_Type()
)
errIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errIndex.setStatus("current")
_ErrCode_Type = Integer32
_ErrCode_Object = MibTableColumn
errCode = _ErrCode_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 3, 3, 1, 2),
    _ErrCode_Type()
)
errCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errCode.setStatus("current")


class _ErrSeverity_Type(Integer32):
    """Custom type errSeverity based on Integer32"""
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
        *(("hard", 2),
          ("informational", 0),
          ("mild", 1),
          ("severe", 3))
    )


_ErrSeverity_Type.__name__ = "Integer32"
_ErrSeverity_Object = MibTableColumn
errSeverity = _ErrSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 3, 3, 1, 3),
    _ErrSeverity_Type()
)
errSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errSeverity.setStatus("current")
_ErrMsg_Type = DisplayString
_ErrMsg_Object = MibTableColumn
errMsg = _ErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 3, 3, 1, 4),
    _ErrMsg_Type()
)
errMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errMsg.setStatus("current")
_ErrActionMsg_Type = DisplayString
_ErrActionMsg_Object = MibTableColumn
errActionMsg = _ErrActionMsg_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 3, 3, 1, 5),
    _ErrActionMsg_Type()
)
errActionMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errActionMsg.setStatus("current")
_OverlandNextGenComponents_ObjectIdentity = ObjectIdentity
overlandNextGenComponents = _OverlandNextGenComponents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 4)
)
_OverlandNextGenAttributes_ObjectIdentity = ObjectIdentity
overlandNextGenAttributes = _OverlandNextGenAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 5)
)


class _NumModules_Type(Integer32):
    """Custom type numModules based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_NumModules_Type.__name__ = "Integer32"
_NumModules_Object = MibScalar
numModules = _NumModules_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 5, 1),
    _NumModules_Type()
)
numModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numModules.setStatus("current")


class _NumBins_Type(Integer32):
    """Custom type numBins based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_NumBins_Type.__name__ = "Integer32"
_NumBins_Object = MibScalar
numBins = _NumBins_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 5, 2),
    _NumBins_Type()
)
numBins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBins.setStatus("current")


class _NumDrives_Type(Integer32):
    """Custom type numDrives based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_NumDrives_Type.__name__ = "Integer32"
_NumDrives_Object = MibScalar
numDrives = _NumDrives_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 5, 3),
    _NumDrives_Type()
)
numDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numDrives.setStatus("current")


class _NumMailSlots_Type(Integer32):
    """Custom type numMailSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NumMailSlots_Type.__name__ = "Integer32"
_NumMailSlots_Object = MibScalar
numMailSlots = _NumMailSlots_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 5, 4),
    _NumMailSlots_Type()
)
numMailSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numMailSlots.setStatus("current")
_ModuleGeometryTable_Object = MibTable
moduleGeometryTable = _ModuleGeometryTable_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 5, 5)
)
if mibBuilder.loadTexts:
    moduleGeometryTable.setStatus("current")
_ModuleGeometryEntry_Object = MibTableRow
moduleGeometryEntry = _ModuleGeometryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 5, 5, 1)
)
moduleGeometryEntry.setIndexNames(
    (0, "OVERLAND-NEXTGEN", "modIndex"),
)
if mibBuilder.loadTexts:
    moduleGeometryEntry.setStatus("current")
_ModDesc_Type = DisplayString
_ModDesc_Object = MibTableColumn
modDesc = _ModDesc_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 5, 5, 1, 1),
    _ModDesc_Type()
)
modDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modDesc.setStatus("current")


class _ModIndex_Type(Integer32):
    """Custom type modIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(8, 8),
    )


_ModIndex_Type.__name__ = "Integer32"
_ModIndex_Object = MibTableColumn
modIndex = _ModIndex_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 5, 5, 1, 2),
    _ModIndex_Type()
)
modIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modIndex.setStatus("current")


class _ModAttached_Type(Integer32):
    """Custom type modAttached based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("isAttached", 1),
          ("isNotAttached", 0))
    )


_ModAttached_Type.__name__ = "Integer32"
_ModAttached_Object = MibTableColumn
modAttached = _ModAttached_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 5, 5, 1, 3),
    _ModAttached_Type()
)
modAttached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modAttached.setStatus("current")
_ModStatus_Type = DisplayString
_ModStatus_Object = MibTableColumn
modStatus = _ModStatus_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 5, 5, 1, 4),
    _ModStatus_Type()
)
modStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modStatus.setStatus("current")


class _ModConfig_Type(Integer32):
    """Custom type modConfig based on Integer32"""
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
        *(("invalid", 3),
          ("lightning", 1),
          ("thunder", 2),
          ("unknown", 0))
    )


_ModConfig_Type.__name__ = "Integer32"
_ModConfig_Object = MibTableColumn
modConfig = _ModConfig_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 5, 5, 1, 5),
    _ModConfig_Type()
)
modConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modConfig.setStatus("current")
_ModFwRev_Type = Integer32
_ModFwRev_Object = MibTableColumn
modFwRev = _ModFwRev_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 5, 5, 1, 6),
    _ModFwRev_Type()
)
modFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modFwRev.setStatus("current")
_ModNumBins_Type = Integer32
_ModNumBins_Object = MibTableColumn
modNumBins = _ModNumBins_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 5, 5, 1, 7),
    _ModNumBins_Type()
)
modNumBins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modNumBins.setStatus("current")
_ModNumDrives_Type = Integer32
_ModNumDrives_Object = MibTableColumn
modNumDrives = _ModNumDrives_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 5, 5, 1, 8),
    _ModNumDrives_Type()
)
modNumDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modNumDrives.setStatus("current")
_ModNumMailSlots_Type = Integer32
_ModNumMailSlots_Object = MibTableColumn
modNumMailSlots = _ModNumMailSlots_Object(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 5, 5, 1, 9),
    _ModNumMailSlots_Type()
)
modNumMailSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modNumMailSlots.setStatus("current")
_OverlandNextGenEvents_ObjectIdentity = ObjectIdentity
overlandNextGenEvents = _OverlandNextGenEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 6)
)
_OverlandNextGenGroups_ObjectIdentity = ObjectIdentity
overlandNextGenGroups = _OverlandNextGenGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 7)
)
_OverlandCaps_ObjectIdentity = ObjectIdentity
overlandCaps = _OverlandCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3351, 1, 4)
)
_OverlandReqs_ObjectIdentity = ObjectIdentity
overlandReqs = _OverlandReqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3351, 1, 5)
)
_OverlandExpr_ObjectIdentity = ObjectIdentity
overlandExpr = _OverlandExpr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3351, 1, 6)
)

# Managed Objects groups

overlandActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 7, 1)
)
overlandActionGroup.setObjects(
    ("OVERLAND-NEXTGEN", "overlandLoopback")
)
if mibBuilder.loadTexts:
    overlandActionGroup.setStatus("current")

overlandStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 7, 3)
)
overlandStateGroup.setObjects(
      *(("OVERLAND-NEXTGEN", "errIndex"),
        ("OVERLAND-NEXTGEN", "errCode"),
        ("OVERLAND-NEXTGEN", "errSeverity"),
        ("OVERLAND-NEXTGEN", "errMsg"),
        ("OVERLAND-NEXTGEN", "errActionMsg"),
        ("OVERLAND-NEXTGEN", "dstRowValid"),
        ("OVERLAND-NEXTGEN", "dstIndex"),
        ("OVERLAND-NEXTGEN", "dstState"),
        ("OVERLAND-NEXTGEN", "dstMotion"),
        ("OVERLAND-NEXTGEN", "dstCodeRevDrive"),
        ("OVERLAND-NEXTGEN", "dstCodeRevController"),
        ("OVERLAND-NEXTGEN", "dstScsiId"),
        ("OVERLAND-NEXTGEN", "dstSerialNum"),
        ("OVERLAND-NEXTGEN", "dstCleanRequested"),
        ("OVERLAND-NEXTGEN", "lstIndex"),
        ("OVERLAND-NEXTGEN", "lstConfig"),
        ("OVERLAND-NEXTGEN", "lstScsiId"),
        ("OVERLAND-NEXTGEN", "lstStatus"),
        ("OVERLAND-NEXTGEN", "lstChangerStatus"),
        ("OVERLAND-NEXTGEN", "lstLibraryState"))
)
if mibBuilder.loadTexts:
    overlandStateGroup.setStatus("current")

overlandAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 7, 4)
)
overlandAttributesGroup.setObjects(
      *(("OVERLAND-NEXTGEN", "numModules"),
        ("OVERLAND-NEXTGEN", "numBins"),
        ("OVERLAND-NEXTGEN", "numDrives"),
        ("OVERLAND-NEXTGEN", "numMailSlots"),
        ("OVERLAND-NEXTGEN", "modDesc"),
        ("OVERLAND-NEXTGEN", "modIndex"),
        ("OVERLAND-NEXTGEN", "modAttached"),
        ("OVERLAND-NEXTGEN", "modStatus"),
        ("OVERLAND-NEXTGEN", "modConfig"),
        ("OVERLAND-NEXTGEN", "modFwRev"),
        ("OVERLAND-NEXTGEN", "modNumBins"),
        ("OVERLAND-NEXTGEN", "modNumDrives"),
        ("OVERLAND-NEXTGEN", "modNumMailSlots"))
)
if mibBuilder.loadTexts:
    overlandAttributesGroup.setStatus("current")


# Notification objects

eventDoorOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 6, 1)
)
if mibBuilder.loadTexts:
    eventDoorOpen.setStatus(
        "current"
    )

eventMailSlotAccessed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 6, 2)
)
if mibBuilder.loadTexts:
    eventMailSlotAccessed.setStatus(
        "current"
    )

eventHardFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 6, 3)
)
if mibBuilder.loadTexts:
    eventHardFault.setStatus(
        "current"
    )

eventSlaveFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 6, 4)
)
if mibBuilder.loadTexts:
    eventSlaveFailed.setStatus(
        "current"
    )

eventPowerSupplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 6, 5)
)
if mibBuilder.loadTexts:
    eventPowerSupplyFailed.setStatus(
        "current"
    )

eventRequestDriveClean = NotificationType(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 6, 6)
)
if mibBuilder.loadTexts:
    eventRequestDriveClean.setStatus(
        "current"
    )

eventFanStalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 6, 7)
)
if mibBuilder.loadTexts:
    eventFanStalled.setStatus(
        "current"
    )

eventDriveError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 6, 8)
)
if mibBuilder.loadTexts:
    eventDriveError.setStatus(
        "current"
    )

eventDriveRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 6, 9)
)
if mibBuilder.loadTexts:
    eventDriveRemoved.setStatus(
        "current"
    )

eventSlaveRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 6, 10)
)
if mibBuilder.loadTexts:
    eventSlaveRemoved.setStatus(
        "current"
    )

eventFailedOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 6, 11)
)
if mibBuilder.loadTexts:
    eventFailedOver.setStatus(
        "current"
    )

eventLoaderRetriesExcessive = NotificationType(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 6, 12)
)
if mibBuilder.loadTexts:
    eventLoaderRetriesExcessive.setStatus(
        "current"
    )


# Notifications groups

overlandNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3351, 1, 3, 2, 7, 7)
)
overlandNotificationGroup.setObjects(
      *(("OVERLAND-NEXTGEN", "eventDoorOpen"),
        ("OVERLAND-NEXTGEN", "eventMailSlotAccessed"),
        ("OVERLAND-NEXTGEN", "eventHardFault"),
        ("OVERLAND-NEXTGEN", "eventSlaveFailed"),
        ("OVERLAND-NEXTGEN", "eventPowerSupplyFailed"),
        ("OVERLAND-NEXTGEN", "eventRequestDriveClean"),
        ("OVERLAND-NEXTGEN", "eventFanStalled"),
        ("OVERLAND-NEXTGEN", "eventDriveError"),
        ("OVERLAND-NEXTGEN", "eventDriveRemoved"),
        ("OVERLAND-NEXTGEN", "eventSlaveRemoved"),
        ("OVERLAND-NEXTGEN", "eventFailedOver"),
        ("OVERLAND-NEXTGEN", "eventLoaderRetriesExcessive"))
)
if mibBuilder.loadTexts:
    overlandNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OVERLAND-NEXTGEN",
    **{"overlandRoot": overlandRoot,
       "overlandReg": overlandReg,
       "overlandModules": overlandModules,
       "overlandGlobalRegModule": overlandGlobalRegModule,
       "overlandGeneric": overlandGeneric,
       "overlandProducts": overlandProducts,
       "overlandNextGen": overlandNextGen,
       "overlandNextGenActions": overlandNextGenActions,
       "overlandLoopback": overlandLoopback,
       "overlandNextGenStatistics": overlandNextGenStatistics,
       "overlandNextGenState": overlandNextGenState,
       "driveStatusTable": driveStatusTable,
       "driveStatusEntry": driveStatusEntry,
       "dstRowValid": dstRowValid,
       "dstIndex": dstIndex,
       "dstState": dstState,
       "dstMotion": dstMotion,
       "dstCodeRevDrive": dstCodeRevDrive,
       "dstCodeRevController": dstCodeRevController,
       "dstScsiId": dstScsiId,
       "dstSerialNum": dstSerialNum,
       "dstCleanRequested": dstCleanRequested,
       "libraryStatusTable": libraryStatusTable,
       "libraryStatusEntry": libraryStatusEntry,
       "lstIndex": lstIndex,
       "lstConfig": lstConfig,
       "lstScsiId": lstScsiId,
       "lstStatus": lstStatus,
       "lstChangerStatus": lstChangerStatus,
       "lstLibraryState": lstLibraryState,
       "errorTable": errorTable,
       "errorEntry": errorEntry,
       "errIndex": errIndex,
       "errCode": errCode,
       "errSeverity": errSeverity,
       "errMsg": errMsg,
       "errActionMsg": errActionMsg,
       "overlandNextGenComponents": overlandNextGenComponents,
       "overlandNextGenAttributes": overlandNextGenAttributes,
       "numModules": numModules,
       "numBins": numBins,
       "numDrives": numDrives,
       "numMailSlots": numMailSlots,
       "moduleGeometryTable": moduleGeometryTable,
       "moduleGeometryEntry": moduleGeometryEntry,
       "modDesc": modDesc,
       "modIndex": modIndex,
       "modAttached": modAttached,
       "modStatus": modStatus,
       "modConfig": modConfig,
       "modFwRev": modFwRev,
       "modNumBins": modNumBins,
       "modNumDrives": modNumDrives,
       "modNumMailSlots": modNumMailSlots,
       "overlandNextGenEvents": overlandNextGenEvents,
       "eventDoorOpen": eventDoorOpen,
       "eventMailSlotAccessed": eventMailSlotAccessed,
       "eventHardFault": eventHardFault,
       "eventSlaveFailed": eventSlaveFailed,
       "eventPowerSupplyFailed": eventPowerSupplyFailed,
       "eventRequestDriveClean": eventRequestDriveClean,
       "eventFanStalled": eventFanStalled,
       "eventDriveError": eventDriveError,
       "eventDriveRemoved": eventDriveRemoved,
       "eventSlaveRemoved": eventSlaveRemoved,
       "eventFailedOver": eventFailedOver,
       "eventLoaderRetriesExcessive": eventLoaderRetriesExcessive,
       "overlandNextGenGroups": overlandNextGenGroups,
       "overlandActionGroup": overlandActionGroup,
       "overlandStateGroup": overlandStateGroup,
       "overlandAttributesGroup": overlandAttributesGroup,
       "overlandNotificationGroup": overlandNotificationGroup,
       "overlandCaps": overlandCaps,
       "overlandReqs": overlandReqs,
       "overlandExpr": overlandExpr}
)
