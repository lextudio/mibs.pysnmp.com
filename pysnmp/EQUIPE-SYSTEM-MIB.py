# SNMP MIB module (EQUIPE-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EQUIPE-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:18 2024
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
 enterprises,
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
    "enterprises",
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


# MODULE-IDENTITY

eqSystemMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5022, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EqModuleType(Integer32, TextualConvention):
    status = "current"
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("controlProcessor", 4),
          ("crossConnect", 8),
          ("fanTray", 3),
          ("mgmtInterface", 6),
          ("other", 1),
          ("powerSupply", 2),
          ("processorCard", 7),
          ("switchFabric", 9),
          ("switchScheduler", 10),
          ("timingControl", 5),
          ("universalPort16xOC12", 13),
          ("universalPort16xOC3", 11),
          ("universalPort4xOC48", 14),
          ("universalPort8xOC12", 12))
    )



class EqModuleStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("booting", 2),
          ("diags", 1),
          ("disabled", 6),
          ("failed", 5),
          ("mismatched", 7),
          ("reset", 4),
          ("up", 3))
    )



class EqModuleHealthStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bad", 3),
          ("good", 1),
          ("marginal", 2))
    )



class EqModuleFeedStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bad", 3),
          ("good", 2),
          ("notAvail", 1))
    )



class EqModuleRedRole(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 3),
          ("notApplicable", 1),
          ("primary", 2))
    )



class EqIfType(Integer32, TextualConvention):
    status = "current"
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
        *(("atmIntf", 4),
          ("other", 1),
          ("sonetPort", 2),
          ("stsPath", 3),
          ("virtAtmIntf", 5))
    )



class EqAtmPvcType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atmHardPvc", 1),
          ("atmSoftPvc", 2))
    )



class EqApsLineState(Integer32, TextualConvention):
    status = "current"
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
        *(("active", 2),
          ("clear", 7),
          ("forceSwitch", 6),
          ("lockoutOfProtect", 8),
          ("manualSwitch", 5),
          ("other", 1),
          ("signalDegrade", 4),
          ("signalFail", 3))
    )



class EqSeverityLevel(Integer32, TextualConvention):
    status = "current"
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
        *(("critical", 7),
          ("debug", 1),
          ("informational", 3),
          ("major", 6),
          ("minor", 5),
          ("normal", 2),
          ("warning", 4))
    )



class EqFaultClass(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 1),
          ("software", 2))
    )



class EqFaultSeverity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hard", 1),
          ("soft", 2))
    )



class EqFaultScope(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chassis", 3),
          ("module", 2),
          ("softwareLoadModule", 1))
    )



class EqReleaseVerificationStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("backupNotFound", 10),
          ("checksumError", 7),
          ("internalError", 8),
          ("missingModule", 6),
          ("noPackingList", 4),
          ("parseError", 5),
          ("removing", 9),
          ("unverified", 1),
          ("verified", 3),
          ("verifying", 2))
    )



class EqReleaseUpgradeScope(Integer32, TextualConvention):
    status = "current"
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
        *(("cold", 2),
          ("frosty", 3),
          ("hot", 1),
          ("unknown", 0))
    )



class EqReleaseState(Integer32, TextualConvention):
    status = "current"
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
        *(("active", 2),
          ("activeCommitted", 1),
          ("committed", 3),
          ("inactive", 4),
          ("unknown", 0))
    )



class EqReleaseCommand(Integer32, TextualConvention):
    status = "current"
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
        *(("boot", 5),
          ("commit", 6),
          ("delete", 3),
          ("none", 1),
          ("upgrade", 2),
          ("verify", 4))
    )



class EqReleaseCommandStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("clear", 1),
          ("done", 3),
          ("error", 4),
          ("processing", 2))
    )



class EqReleaseSchemaChange(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("change", 1),
          ("nochange", 2))
    )



class EqReleaseConfigAvail(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("avail", 1),
          ("notAvail", 2))
    )



class EqReleaseRevert(Integer32, TextualConvention):
    status = "current"
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
        *(("revertActive", 2),
          ("revertAllowed", 4),
          ("revertInactive", 1),
          ("revertNotAllowed", 5),
          ("revertStart", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Equipe_ObjectIdentity = ObjectIdentity
equipe = _Equipe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5022)
)
_EqSysProducts_ObjectIdentity = ObjectIdentity
eqSysProducts = _EqSysProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5022, 1, 1)
)
_EqSysProductE3200_ObjectIdentity = ObjectIdentity
eqSysProductE3200 = _EqSysProductE3200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5022, 1, 1, 1)
)
_EqSysSystemGrp_ObjectIdentity = ObjectIdentity
eqSysSystemGrp = _EqSysSystemGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5022, 1, 2)
)
_EqSysSystem_ObjectIdentity = ObjectIdentity
eqSysSystem = _EqSysSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5022, 1, 2, 1)
)


class _EqSysSystemId_Type(OctetString):
    """Custom type eqSysSystemId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_EqSysSystemId_Type.__name__ = "OctetString"
_EqSysSystemId_Object = MibScalar
eqSysSystemId = _EqSysSystemId_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 2, 1, 1),
    _EqSysSystemId_Type()
)
eqSysSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqSysSystemId.setStatus("current")
_EqSysPhysEntLastChangeTime_Type = TimeTicks
_EqSysPhysEntLastChangeTime_Object = MibScalar
eqSysPhysEntLastChangeTime = _EqSysPhysEntLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 2, 1, 2),
    _EqSysPhysEntLastChangeTime_Type()
)
eqSysPhysEntLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqSysPhysEntLastChangeTime.setStatus("current")
_EqSysConfig_ObjectIdentity = ObjectIdentity
eqSysConfig = _EqSysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5022, 1, 2, 2)
)


class _EqSysCfgCopyConfigFileAction_Type(Integer32):
    """Custom type eqSysCfgCopyConfigFileAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copyCfgFile", 2),
          ("other", 1))
    )


_EqSysCfgCopyConfigFileAction_Type.__name__ = "Integer32"
_EqSysCfgCopyConfigFileAction_Object = MibScalar
eqSysCfgCopyConfigFileAction = _EqSysCfgCopyConfigFileAction_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 2, 2, 1),
    _EqSysCfgCopyConfigFileAction_Type()
)
eqSysCfgCopyConfigFileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqSysCfgCopyConfigFileAction.setStatus("current")


class _EqSysCfgCopyConfigFileStatus_Type(Integer32):
    """Custom type eqSysCfgCopyConfigFileStatus based on Integer32"""
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
        *(("copyCfgDoneError", 4),
          ("copyCfgDoneSuccess", 3),
          ("copyCfgIdle", 1),
          ("copyCfgInProgress", 2))
    )


_EqSysCfgCopyConfigFileStatus_Type.__name__ = "Integer32"
_EqSysCfgCopyConfigFileStatus_Object = MibScalar
eqSysCfgCopyConfigFileStatus = _EqSysCfgCopyConfigFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 2, 2, 2),
    _EqSysCfgCopyConfigFileStatus_Type()
)
eqSysCfgCopyConfigFileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqSysCfgCopyConfigFileStatus.setStatus("current")
_EqSysCfgSavedFilename_Type = DisplayString
_EqSysCfgSavedFilename_Object = MibScalar
eqSysCfgSavedFilename = _EqSysCfgSavedFilename_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 2, 2, 3),
    _EqSysCfgSavedFilename_Type()
)
eqSysCfgSavedFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqSysCfgSavedFilename.setStatus("current")
_EqEidReqTable_Object = MibTable
eqEidReqTable = _EqEidReqTable_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 2, 3)
)
if mibBuilder.loadTexts:
    eqEidReqTable.setStatus("current")
_EqEidReqEntry_Object = MibTableRow
eqEidReqEntry = _EqEidReqEntry_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 2, 3, 1)
)
eqEidReqEntry.setIndexNames(
    (0, "EQUIPE-SYSTEM-MIB", "eqEidReqIndex"),
)
if mibBuilder.loadTexts:
    eqEidReqEntry.setStatus("current")


class _EqEidReqIndex_Type(Integer32):
    """Custom type eqEidReqIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqEidReqIndex_Type.__name__ = "Integer32"
_EqEidReqIndex_Object = MibTableColumn
eqEidReqIndex = _EqEidReqIndex_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 2, 3, 1, 1),
    _EqEidReqIndex_Type()
)
eqEidReqIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqEidReqIndex.setStatus("current")
_EqEidReqUser_Type = DisplayString
_EqEidReqUser_Object = MibTableColumn
eqEidReqUser = _EqEidReqUser_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 2, 3, 1, 2),
    _EqEidReqUser_Type()
)
eqEidReqUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqEidReqUser.setStatus("current")


class _EqEidReqCount_Type(Integer32):
    """Custom type eqEidReqCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 400),
    )


_EqEidReqCount_Type.__name__ = "Integer32"
_EqEidReqCount_Object = MibTableColumn
eqEidReqCount = _EqEidReqCount_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 2, 3, 1, 3),
    _EqEidReqCount_Type()
)
eqEidReqCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqEidReqCount.setStatus("current")


class _EqEidReqCountAlloc_Type(Integer32):
    """Custom type eqEidReqCountAlloc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 400),
    )


_EqEidReqCountAlloc_Type.__name__ = "Integer32"
_EqEidReqCountAlloc_Object = MibTableColumn
eqEidReqCountAlloc = _EqEidReqCountAlloc_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 2, 3, 1, 4),
    _EqEidReqCountAlloc_Type()
)
eqEidReqCountAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqEidReqCountAlloc.setStatus("current")


class _EqEidReqAction_Type(Integer32):
    """Custom type eqEidReqAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alloc", 2),
          ("other", 1))
    )


_EqEidReqAction_Type.__name__ = "Integer32"
_EqEidReqAction_Object = MibTableColumn
eqEidReqAction = _EqEidReqAction_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 2, 3, 1, 5),
    _EqEidReqAction_Type()
)
eqEidReqAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqEidReqAction.setStatus("current")


class _EqEidReqActionStatus_Type(Integer32):
    """Custom type eqEidReqActionStatus based on Integer32"""
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
        *(("none", 1),
          ("reqErrorEidsUnavailable", 4),
          ("reqErrorReqCountTooBig", 3),
          ("reqSuccess", 2))
    )


_EqEidReqActionStatus_Type.__name__ = "Integer32"
_EqEidReqActionStatus_Object = MibTableColumn
eqEidReqActionStatus = _EqEidReqActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 2, 3, 1, 6),
    _EqEidReqActionStatus_Type()
)
eqEidReqActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqEidReqActionStatus.setStatus("current")
_EqEidReqRowStatus_Type = RowStatus
_EqEidReqRowStatus_Object = MibTableColumn
eqEidReqRowStatus = _EqEidReqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 2, 3, 1, 7),
    _EqEidReqRowStatus_Type()
)
eqEidReqRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqEidReqRowStatus.setStatus("current")
_EqEidResTable_Object = MibTable
eqEidResTable = _EqEidResTable_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 2, 4)
)
if mibBuilder.loadTexts:
    eqEidResTable.setStatus("current")
_EqEidResEntry_Object = MibTableRow
eqEidResEntry = _EqEidResEntry_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 2, 4, 1)
)
eqEidResEntry.setIndexNames(
    (0, "EQUIPE-SYSTEM-MIB", "eqEidReqIndex"),
    (0, "EQUIPE-SYSTEM-MIB", "eqEidResIndex"),
)
if mibBuilder.loadTexts:
    eqEidResEntry.setStatus("current")


class _EqEidResIndex_Type(Integer32):
    """Custom type eqEidResIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqEidResIndex_Type.__name__ = "Integer32"
_EqEidResIndex_Object = MibTableColumn
eqEidResIndex = _EqEidResIndex_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 2, 4, 1, 1),
    _EqEidResIndex_Type()
)
eqEidResIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqEidResIndex.setStatus("current")
_EqEidResData_Type = ObjectIdentifier
_EqEidResData_Object = MibTableColumn
eqEidResData = _EqEidResData_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 2, 4, 1, 2),
    _EqEidResData_Type()
)
eqEidResData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqEidResData.setStatus("current")
_EqSysModuleGrp_ObjectIdentity = ObjectIdentity
eqSysModuleGrp = _EqSysModuleGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3)
)
_EqSysModule_ObjectIdentity = ObjectIdentity
eqSysModule = _EqSysModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1)
)
_EqModuleTable_Object = MibTable
eqModuleTable = _EqModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    eqModuleTable.setStatus("current")
_EqModuleEntry_Object = MibTableRow
eqModuleEntry = _EqModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 1, 1)
)
eqModuleEntry.setIndexNames(
    (0, "EQUIPE-SYSTEM-MIB", "eqModuleEid"),
)
if mibBuilder.loadTexts:
    eqModuleEntry.setStatus("current")


class _EqModuleEid_Type(Integer32):
    """Custom type eqModuleEid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqModuleEid_Type.__name__ = "Integer32"
_EqModuleEid_Object = MibTableColumn
eqModuleEid = _EqModuleEid_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 1, 1, 1),
    _EqModuleEid_Type()
)
eqModuleEid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqModuleEid.setStatus("current")


class _EqModuleShelfId_Type(Integer32):
    """Custom type eqModuleShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_EqModuleShelfId_Type.__name__ = "Integer32"
_EqModuleShelfId_Object = MibTableColumn
eqModuleShelfId = _EqModuleShelfId_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 1, 1, 2),
    _EqModuleShelfId_Type()
)
eqModuleShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqModuleShelfId.setStatus("current")


class _EqModuleSlotId_Type(Integer32):
    """Custom type eqModuleSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EqModuleSlotId_Type.__name__ = "Integer32"
_EqModuleSlotId_Object = MibTableColumn
eqModuleSlotId = _EqModuleSlotId_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 1, 1, 3),
    _EqModuleSlotId_Type()
)
eqModuleSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqModuleSlotId.setStatus("current")
_EqModuleType_Type = EqModuleType
_EqModuleType_Object = MibTableColumn
eqModuleType = _EqModuleType_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 1, 1, 4),
    _EqModuleType_Type()
)
eqModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqModuleType.setStatus("current")


class _EqModuleHwVersion_Type(OctetString):
    """Custom type eqModuleHwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_EqModuleHwVersion_Type.__name__ = "OctetString"
_EqModuleHwVersion_Object = MibTableColumn
eqModuleHwVersion = _EqModuleHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 1, 1, 5),
    _EqModuleHwVersion_Type()
)
eqModuleHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqModuleHwVersion.setStatus("current")
_EqModuleStatus_Type = EqModuleStatus
_EqModuleStatus_Object = MibTableColumn
eqModuleStatus = _EqModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 1, 1, 6),
    _EqModuleStatus_Type()
)
eqModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqModuleStatus.setStatus("current")


class _EqModuleAction_Type(Integer32):
    """Custom type eqModuleAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_EqModuleAction_Type.__name__ = "Integer32"
_EqModuleAction_Object = MibTableColumn
eqModuleAction = _EqModuleAction_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 1, 1, 7),
    _EqModuleAction_Type()
)
eqModuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqModuleAction.setStatus("current")
_EqModuleHealthTable_Object = MibTable
eqModuleHealthTable = _EqModuleHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    eqModuleHealthTable.setStatus("current")
_EqModuleHealthEntry_Object = MibTableRow
eqModuleHealthEntry = _EqModuleHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 2, 1)
)
eqModuleHealthEntry.setIndexNames(
    (0, "EQUIPE-SYSTEM-MIB", "eqModuleEid"),
)
if mibBuilder.loadTexts:
    eqModuleHealthEntry.setStatus("current")
_EqModuleHealthStatus_Type = EqModuleHealthStatus
_EqModuleHealthStatus_Object = MibTableColumn
eqModuleHealthStatus = _EqModuleHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 2, 1, 1),
    _EqModuleHealthStatus_Type()
)
eqModuleHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqModuleHealthStatus.setStatus("current")


class _EqModuleMemTotal_Type(Integer32):
    """Custom type eqModuleMemTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_EqModuleMemTotal_Type.__name__ = "Integer32"
_EqModuleMemTotal_Object = MibTableColumn
eqModuleMemTotal = _EqModuleMemTotal_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 2, 1, 2),
    _EqModuleMemTotal_Type()
)
eqModuleMemTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqModuleMemTotal.setStatus("current")


class _EqModuleMemUsed_Type(Integer32):
    """Custom type eqModuleMemUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_EqModuleMemUsed_Type.__name__ = "Integer32"
_EqModuleMemUsed_Object = MibTableColumn
eqModuleMemUsed = _EqModuleMemUsed_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 2, 1, 3),
    _EqModuleMemUsed_Type()
)
eqModuleMemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqModuleMemUsed.setStatus("current")


class _EqModuleMemUsedPercent_Type(Integer32):
    """Custom type eqModuleMemUsedPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EqModuleMemUsedPercent_Type.__name__ = "Integer32"
_EqModuleMemUsedPercent_Object = MibTableColumn
eqModuleMemUsedPercent = _EqModuleMemUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 2, 1, 4),
    _EqModuleMemUsedPercent_Type()
)
eqModuleMemUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqModuleMemUsedPercent.setStatus("current")


class _EqModuleTemp_Type(Integer32):
    """Custom type eqModuleTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EqModuleTemp_Type.__name__ = "Integer32"
_EqModuleTemp_Object = MibTableColumn
eqModuleTemp = _EqModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 2, 1, 5),
    _EqModuleTemp_Type()
)
eqModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqModuleTemp.setStatus("current")


class _EqModuleCpuUtil_Type(Integer32):
    """Custom type eqModuleCpuUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EqModuleCpuUtil_Type.__name__ = "Integer32"
_EqModuleCpuUtil_Object = MibTableColumn
eqModuleCpuUtil = _EqModuleCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 2, 1, 6),
    _EqModuleCpuUtil_Type()
)
eqModuleCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqModuleCpuUtil.setStatus("current")
_EqModuleFeedStatusA_Type = EqModuleFeedStatus
_EqModuleFeedStatusA_Object = MibTableColumn
eqModuleFeedStatusA = _EqModuleFeedStatusA_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 2, 1, 7),
    _EqModuleFeedStatusA_Type()
)
eqModuleFeedStatusA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqModuleFeedStatusA.setStatus("current")
_EqModuleFeedStatusB_Type = EqModuleFeedStatus
_EqModuleFeedStatusB_Object = MibTableColumn
eqModuleFeedStatusB = _EqModuleFeedStatusB_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 2, 1, 8),
    _EqModuleFeedStatusB_Type()
)
eqModuleFeedStatusB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqModuleFeedStatusB.setStatus("current")
_EqHardDiskTable_Object = MibTable
eqHardDiskTable = _EqHardDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    eqHardDiskTable.setStatus("current")
_EqHardDiskEntry_Object = MibTableRow
eqHardDiskEntry = _EqHardDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 3, 1)
)
eqHardDiskEntry.setIndexNames(
    (0, "EQUIPE-SYSTEM-MIB", "eqHardDiskEid"),
)
if mibBuilder.loadTexts:
    eqHardDiskEntry.setStatus("current")


class _EqHardDiskEid_Type(Integer32):
    """Custom type eqHardDiskEid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqHardDiskEid_Type.__name__ = "Integer32"
_EqHardDiskEid_Object = MibTableColumn
eqHardDiskEid = _EqHardDiskEid_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 3, 1, 1),
    _EqHardDiskEid_Type()
)
eqHardDiskEid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqHardDiskEid.setStatus("current")


class _EqHardDiskShelfId_Type(Integer32):
    """Custom type eqHardDiskShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_EqHardDiskShelfId_Type.__name__ = "Integer32"
_EqHardDiskShelfId_Object = MibTableColumn
eqHardDiskShelfId = _EqHardDiskShelfId_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 3, 1, 2),
    _EqHardDiskShelfId_Type()
)
eqHardDiskShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqHardDiskShelfId.setStatus("current")


class _EqHardDiskSlotId_Type(Integer32):
    """Custom type eqHardDiskSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EqHardDiskSlotId_Type.__name__ = "Integer32"
_EqHardDiskSlotId_Object = MibTableColumn
eqHardDiskSlotId = _EqHardDiskSlotId_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 3, 1, 3),
    _EqHardDiskSlotId_Type()
)
eqHardDiskSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqHardDiskSlotId.setStatus("current")


class _EqHardDiskCapacity_Type(Integer32):
    """Custom type eqHardDiskCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_EqHardDiskCapacity_Type.__name__ = "Integer32"
_EqHardDiskCapacity_Object = MibTableColumn
eqHardDiskCapacity = _EqHardDiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 3, 1, 4),
    _EqHardDiskCapacity_Type()
)
eqHardDiskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqHardDiskCapacity.setStatus("current")


class _EqHardDiskUsed_Type(Integer32):
    """Custom type eqHardDiskUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_EqHardDiskUsed_Type.__name__ = "Integer32"
_EqHardDiskUsed_Object = MibTableColumn
eqHardDiskUsed = _EqHardDiskUsed_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 3, 1, 5),
    _EqHardDiskUsed_Type()
)
eqHardDiskUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqHardDiskUsed.setStatus("current")


class _EqHardDiskUsedHiMark_Type(Integer32):
    """Custom type eqHardDiskUsedHiMark based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_EqHardDiskUsedHiMark_Type.__name__ = "Integer32"
_EqHardDiskUsedHiMark_Object = MibTableColumn
eqHardDiskUsedHiMark = _EqHardDiskUsedHiMark_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 3, 1, 6),
    _EqHardDiskUsedHiMark_Type()
)
eqHardDiskUsedHiMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqHardDiskUsedHiMark.setStatus("current")


class _EqHardDiskUsedLowMark_Type(Integer32):
    """Custom type eqHardDiskUsedLowMark based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_EqHardDiskUsedLowMark_Type.__name__ = "Integer32"
_EqHardDiskUsedLowMark_Object = MibTableColumn
eqHardDiskUsedLowMark = _EqHardDiskUsedLowMark_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 3, 1, 7),
    _EqHardDiskUsedLowMark_Type()
)
eqHardDiskUsedLowMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqHardDiskUsedLowMark.setStatus("current")
_EqFanUnitTable_Object = MibTable
eqFanUnitTable = _EqFanUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    eqFanUnitTable.setStatus("current")
_EqFanUnitEntry_Object = MibTableRow
eqFanUnitEntry = _EqFanUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 4, 1)
)
eqFanUnitEntry.setIndexNames(
    (0, "EQUIPE-SYSTEM-MIB", "eqFanUnitEid"),
)
if mibBuilder.loadTexts:
    eqFanUnitEntry.setStatus("current")


class _EqFanUnitEid_Type(Integer32):
    """Custom type eqFanUnitEid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqFanUnitEid_Type.__name__ = "Integer32"
_EqFanUnitEid_Object = MibTableColumn
eqFanUnitEid = _EqFanUnitEid_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 4, 1, 1),
    _EqFanUnitEid_Type()
)
eqFanUnitEid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqFanUnitEid.setStatus("current")


class _EqFanUnitShelfId_Type(Integer32):
    """Custom type eqFanUnitShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_EqFanUnitShelfId_Type.__name__ = "Integer32"
_EqFanUnitShelfId_Object = MibTableColumn
eqFanUnitShelfId = _EqFanUnitShelfId_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 4, 1, 2),
    _EqFanUnitShelfId_Type()
)
eqFanUnitShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqFanUnitShelfId.setStatus("current")


class _EqFanUnitSlotId_Type(Integer32):
    """Custom type eqFanUnitSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EqFanUnitSlotId_Type.__name__ = "Integer32"
_EqFanUnitSlotId_Object = MibTableColumn
eqFanUnitSlotId = _EqFanUnitSlotId_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 4, 1, 3),
    _EqFanUnitSlotId_Type()
)
eqFanUnitSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqFanUnitSlotId.setStatus("current")


class _EqFanUnitRpm_Type(Integer32):
    """Custom type eqFanUnitRpm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_EqFanUnitRpm_Type.__name__ = "Integer32"
_EqFanUnitRpm_Object = MibTableColumn
eqFanUnitRpm = _EqFanUnitRpm_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 4, 1, 4),
    _EqFanUnitRpm_Type()
)
eqFanUnitRpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqFanUnitRpm.setStatus("current")


class _EqFanUnitRpmHiMark_Type(Integer32):
    """Custom type eqFanUnitRpmHiMark based on Integer32"""
    defaultValue = 999

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_EqFanUnitRpmHiMark_Type.__name__ = "Integer32"
_EqFanUnitRpmHiMark_Object = MibTableColumn
eqFanUnitRpmHiMark = _EqFanUnitRpmHiMark_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 4, 1, 5),
    _EqFanUnitRpmHiMark_Type()
)
eqFanUnitRpmHiMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqFanUnitRpmHiMark.setStatus("current")


class _EqFanUnitRpmLowMark_Type(Integer32):
    """Custom type eqFanUnitRpmLowMark based on Integer32"""
    defaultValue = 999

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_EqFanUnitRpmLowMark_Type.__name__ = "Integer32"
_EqFanUnitRpmLowMark_Object = MibTableColumn
eqFanUnitRpmLowMark = _EqFanUnitRpmLowMark_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 4, 1, 6),
    _EqFanUnitRpmLowMark_Type()
)
eqFanUnitRpmLowMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqFanUnitRpmLowMark.setStatus("current")
_EqModuleRedTable_Object = MibTable
eqModuleRedTable = _EqModuleRedTable_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 5)
)
if mibBuilder.loadTexts:
    eqModuleRedTable.setStatus("current")
_EqModuleRedEntry_Object = MibTableRow
eqModuleRedEntry = _EqModuleRedEntry_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 5, 1)
)
eqModuleRedEntry.setIndexNames(
    (0, "EQUIPE-SYSTEM-MIB", "eqModuleRedEid"),
)
if mibBuilder.loadTexts:
    eqModuleRedEntry.setStatus("current")


class _EqModuleRedEid_Type(Integer32):
    """Custom type eqModuleRedEid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqModuleRedEid_Type.__name__ = "Integer32"
_EqModuleRedEid_Object = MibTableColumn
eqModuleRedEid = _EqModuleRedEid_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 5, 1, 1),
    _EqModuleRedEid_Type()
)
eqModuleRedEid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqModuleRedEid.setStatus("current")
_EqModuleRedAdminRole_Type = EqModuleRedRole
_EqModuleRedAdminRole_Object = MibTableColumn
eqModuleRedAdminRole = _EqModuleRedAdminRole_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 5, 1, 2),
    _EqModuleRedAdminRole_Type()
)
eqModuleRedAdminRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqModuleRedAdminRole.setStatus("current")
_EqModuleRedOperRole_Type = EqModuleRedRole
_EqModuleRedOperRole_Object = MibTableColumn
eqModuleRedOperRole = _EqModuleRedOperRole_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 5, 1, 3),
    _EqModuleRedOperRole_Type()
)
eqModuleRedOperRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqModuleRedOperRole.setStatus("current")


class _EqModuleRedPeerId_Type(Integer32):
    """Custom type eqModuleRedPeerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EqModuleRedPeerId_Type.__name__ = "Integer32"
_EqModuleRedPeerId_Object = MibTableColumn
eqModuleRedPeerId = _EqModuleRedPeerId_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 5, 1, 4),
    _EqModuleRedPeerId_Type()
)
eqModuleRedPeerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqModuleRedPeerId.setStatus("current")


class _EqModuleRedAction_Type(Integer32):
    """Custom type eqModuleRedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("switchRole", 2))
    )


_EqModuleRedAction_Type.__name__ = "Integer32"
_EqModuleRedAction_Object = MibTableColumn
eqModuleRedAction = _EqModuleRedAction_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 5, 1, 5),
    _EqModuleRedAction_Type()
)
eqModuleRedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqModuleRedAction.setStatus("current")
_EqStratumCentTable_Object = MibTable
eqStratumCentTable = _EqStratumCentTable_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 6)
)
if mibBuilder.loadTexts:
    eqStratumCentTable.setStatus("current")
_EqStratumCentEntry_Object = MibTableRow
eqStratumCentEntry = _EqStratumCentEntry_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 6, 1)
)
eqStratumCentEntry.setIndexNames(
    (0, "EQUIPE-SYSTEM-MIB", "eqStratumCentEid"),
)
if mibBuilder.loadTexts:
    eqStratumCentEntry.setStatus("current")


class _EqStratumCentEid_Type(Integer32):
    """Custom type eqStratumCentEid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqStratumCentEid_Type.__name__ = "Integer32"
_EqStratumCentEid_Object = MibTableColumn
eqStratumCentEid = _EqStratumCentEid_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 6, 1, 1),
    _EqStratumCentEid_Type()
)
eqStratumCentEid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqStratumCentEid.setStatus("current")


class _EqStratumCentStatus_Type(Integer32):
    """Custom type eqStratumCentStatus based on Integer32"""
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
        *(("freeRun", 2),
          ("holdover", 3),
          ("lockedPrimary", 4),
          ("lockedSecondary", 5),
          ("none", 1))
    )


_EqStratumCentStatus_Type.__name__ = "Integer32"
_EqStratumCentStatus_Object = MibTableColumn
eqStratumCentStatus = _EqStratumCentStatus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 6, 1, 2),
    _EqStratumCentStatus_Type()
)
eqStratumCentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqStratumCentStatus.setStatus("current")


class _EqStratumCentRedStatus_Type(Integer32):
    """Custom type eqStratumCentRedStatus based on Integer32"""
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
        *(("offline", 2),
          ("online", 4),
          ("reset", 1),
          ("standby", 3))
    )


_EqStratumCentRedStatus_Type.__name__ = "Integer32"
_EqStratumCentRedStatus_Object = MibTableColumn
eqStratumCentRedStatus = _EqStratumCentRedStatus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 6, 1, 3),
    _EqStratumCentRedStatus_Type()
)
eqStratumCentRedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqStratumCentRedStatus.setStatus("current")


class _EqStratumCentLevel_Type(Integer32):
    """Custom type eqStratumCentLevel based on Integer32"""
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
        *(("sonetMin", 6),
          ("stratum1", 1),
          ("stratum2", 2),
          ("stratum3", 4),
          ("stratum3E", 3),
          ("stratum4", 5))
    )


_EqStratumCentLevel_Type.__name__ = "Integer32"
_EqStratumCentLevel_Object = MibTableColumn
eqStratumCentLevel = _EqStratumCentLevel_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 6, 1, 4),
    _EqStratumCentLevel_Type()
)
eqStratumCentLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqStratumCentLevel.setStatus("current")


class _EqStratumCentPrimaryRefStatus_Type(Integer32):
    """Custom type eqStratumCentPrimaryRefStatus based on Integer32"""
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
        *(("noSignal", 2),
          ("outOfLock", 4),
          ("outOfRange", 3),
          ("qualified", 1))
    )


_EqStratumCentPrimaryRefStatus_Type.__name__ = "Integer32"
_EqStratumCentPrimaryRefStatus_Object = MibTableColumn
eqStratumCentPrimaryRefStatus = _EqStratumCentPrimaryRefStatus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 6, 1, 5),
    _EqStratumCentPrimaryRefStatus_Type()
)
eqStratumCentPrimaryRefStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqStratumCentPrimaryRefStatus.setStatus("current")


class _EqStratumCentSecondaryRefStatus_Type(Integer32):
    """Custom type eqStratumCentSecondaryRefStatus based on Integer32"""
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
        *(("noSignal", 2),
          ("outOfLock", 4),
          ("outOfRange", 3),
          ("qualified", 1))
    )


_EqStratumCentSecondaryRefStatus_Type.__name__ = "Integer32"
_EqStratumCentSecondaryRefStatus_Object = MibTableColumn
eqStratumCentSecondaryRefStatus = _EqStratumCentSecondaryRefStatus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 6, 1, 6),
    _EqStratumCentSecondaryRefStatus_Type()
)
eqStratumCentSecondaryRefStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqStratumCentSecondaryRefStatus.setStatus("current")


class _EqStratumCentStatusAction_Type(Integer32):
    """Custom type eqStratumCentStatusAction based on Integer32"""
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
        *(("freeRun", 2),
          ("holdOver", 3),
          ("lockedPrimary", 4),
          ("lockedSecondary", 5),
          ("other", 1))
    )


_EqStratumCentStatusAction_Type.__name__ = "Integer32"
_EqStratumCentStatusAction_Object = MibTableColumn
eqStratumCentStatusAction = _EqStratumCentStatusAction_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 6, 1, 7),
    _EqStratumCentStatusAction_Type()
)
eqStratumCentStatusAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqStratumCentStatusAction.setStatus("current")


class _EqStratumCentRedAction_Type(Integer32):
    """Custom type eqStratumCentRedAction based on Integer32"""
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
        *(("offline", 3),
          ("online", 5),
          ("other", 1),
          ("reset", 2),
          ("standby", 4))
    )


_EqStratumCentRedAction_Type.__name__ = "Integer32"
_EqStratumCentRedAction_Object = MibTableColumn
eqStratumCentRedAction = _EqStratumCentRedAction_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 6, 1, 8),
    _EqStratumCentRedAction_Type()
)
eqStratumCentRedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqStratumCentRedAction.setStatus("current")
_EqStratumLocalTable_Object = MibTable
eqStratumLocalTable = _EqStratumLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 7)
)
if mibBuilder.loadTexts:
    eqStratumLocalTable.setStatus("current")
_EqStratumLocalEntry_Object = MibTableRow
eqStratumLocalEntry = _EqStratumLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 7, 1)
)
eqStratumLocalEntry.setIndexNames(
    (0, "EQUIPE-SYSTEM-MIB", "eqStratumLocalEid"),
)
if mibBuilder.loadTexts:
    eqStratumLocalEntry.setStatus("current")


class _EqStratumLocalEid_Type(Integer32):
    """Custom type eqStratumLocalEid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqStratumLocalEid_Type.__name__ = "Integer32"
_EqStratumLocalEid_Object = MibTableColumn
eqStratumLocalEid = _EqStratumLocalEid_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 7, 1, 1),
    _EqStratumLocalEid_Type()
)
eqStratumLocalEid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqStratumLocalEid.setStatus("current")


class _EqStratumLocalInputA1Status_Type(Integer32):
    """Custom type eqStratumLocalInputA1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSignal", 2),
          ("signal", 1))
    )


_EqStratumLocalInputA1Status_Type.__name__ = "Integer32"
_EqStratumLocalInputA1Status_Object = MibTableColumn
eqStratumLocalInputA1Status = _EqStratumLocalInputA1Status_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 7, 1, 2),
    _EqStratumLocalInputA1Status_Type()
)
eqStratumLocalInputA1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqStratumLocalInputA1Status.setStatus("current")


class _EqStratumLocalInputA2Status_Type(Integer32):
    """Custom type eqStratumLocalInputA2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSignal", 2),
          ("signal", 1))
    )


_EqStratumLocalInputA2Status_Type.__name__ = "Integer32"
_EqStratumLocalInputA2Status_Object = MibTableColumn
eqStratumLocalInputA2Status = _EqStratumLocalInputA2Status_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 7, 1, 3),
    _EqStratumLocalInputA2Status_Type()
)
eqStratumLocalInputA2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqStratumLocalInputA2Status.setStatus("current")


class _EqStratumLocalInputB1Status_Type(Integer32):
    """Custom type eqStratumLocalInputB1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSignal", 2),
          ("signal", 1))
    )


_EqStratumLocalInputB1Status_Type.__name__ = "Integer32"
_EqStratumLocalInputB1Status_Object = MibTableColumn
eqStratumLocalInputB1Status = _EqStratumLocalInputB1Status_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 7, 1, 4),
    _EqStratumLocalInputB1Status_Type()
)
eqStratumLocalInputB1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqStratumLocalInputB1Status.setStatus("current")


class _EqStratumLocalInputB2Status_Type(Integer32):
    """Custom type eqStratumLocalInputB2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSignal", 2),
          ("signal", 1))
    )


_EqStratumLocalInputB2Status_Type.__name__ = "Integer32"
_EqStratumLocalInputB2Status_Object = MibTableColumn
eqStratumLocalInputB2Status = _EqStratumLocalInputB2Status_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 7, 1, 5),
    _EqStratumLocalInputB2Status_Type()
)
eqStratumLocalInputB2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqStratumLocalInputB2Status.setStatus("current")


class _EqStratumLocalInputUsed_Type(Integer32):
    """Custom type eqStratumLocalInputUsed based on Integer32"""
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
          ("usingInputA", 2),
          ("usingInputB", 3))
    )


_EqStratumLocalInputUsed_Type.__name__ = "Integer32"
_EqStratumLocalInputUsed_Object = MibTableColumn
eqStratumLocalInputUsed = _EqStratumLocalInputUsed_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 7, 1, 6),
    _EqStratumLocalInputUsed_Type()
)
eqStratumLocalInputUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqStratumLocalInputUsed.setStatus("current")


class _EqStratumLocalRecoveredRefStatus_Type(Integer32):
    """Custom type eqStratumLocalRecoveredRefStatus based on Integer32"""
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
          ("priRef", 2),
          ("secRef", 3))
    )


_EqStratumLocalRecoveredRefStatus_Type.__name__ = "Integer32"
_EqStratumLocalRecoveredRefStatus_Object = MibTableColumn
eqStratumLocalRecoveredRefStatus = _EqStratumLocalRecoveredRefStatus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 7, 1, 7),
    _EqStratumLocalRecoveredRefStatus_Type()
)
eqStratumLocalRecoveredRefStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqStratumLocalRecoveredRefStatus.setStatus("current")


class _EqStratumLocalStatusAction_Type(Integer32):
    """Custom type eqStratumLocalStatusAction based on Integer32"""
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
        *(("other", 1),
          ("useInputA", 3),
          ("useInputB", 4),
          ("useNeither", 2))
    )


_EqStratumLocalStatusAction_Type.__name__ = "Integer32"
_EqStratumLocalStatusAction_Object = MibTableColumn
eqStratumLocalStatusAction = _EqStratumLocalStatusAction_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 3, 1, 7, 1, 8),
    _EqStratumLocalStatusAction_Type()
)
eqStratumLocalStatusAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqStratumLocalStatusAction.setStatus("current")
_EqSysFaultGrp_ObjectIdentity = ObjectIdentity
eqSysFaultGrp = _EqSysFaultGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5022, 1, 4)
)
_EqSysFault_ObjectIdentity = ObjectIdentity
eqSysFault = _EqSysFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5022, 1, 4, 1)
)
_EqFaultTable_Object = MibTable
eqFaultTable = _EqFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    eqFaultTable.setStatus("current")
_EqFaultEntry_Object = MibTableRow
eqFaultEntry = _EqFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 4, 1, 1, 1)
)
eqFaultEntry.setIndexNames(
    (0, "EQUIPE-SYSTEM-MIB", "eqFaultDomain"),
    (0, "EQUIPE-SYSTEM-MIB", "eqFaultHandle"),
)
if mibBuilder.loadTexts:
    eqFaultEntry.setStatus("current")


class _EqFaultDomain_Type(Integer32):
    """Custom type eqFaultDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqFaultDomain_Type.__name__ = "Integer32"
_EqFaultDomain_Object = MibTableColumn
eqFaultDomain = _EqFaultDomain_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 4, 1, 1, 1, 1),
    _EqFaultDomain_Type()
)
eqFaultDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqFaultDomain.setStatus("current")


class _EqFaultHandle_Type(Integer32):
    """Custom type eqFaultHandle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqFaultHandle_Type.__name__ = "Integer32"
_EqFaultHandle_Object = MibTableColumn
eqFaultHandle = _EqFaultHandle_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 4, 1, 1, 1, 2),
    _EqFaultHandle_Type()
)
eqFaultHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqFaultHandle.setStatus("current")
_EqFaultClass_Type = EqFaultClass
_EqFaultClass_Object = MibTableColumn
eqFaultClass = _EqFaultClass_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 4, 1, 1, 1, 3),
    _EqFaultClass_Type()
)
eqFaultClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqFaultClass.setStatus("current")


class _EqFaultSubclass_Type(Integer32):
    """Custom type eqFaultSubclass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqFaultSubclass_Type.__name__ = "Integer32"
_EqFaultSubclass_Object = MibTableColumn
eqFaultSubclass = _EqFaultSubclass_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 4, 1, 1, 1, 4),
    _EqFaultSubclass_Type()
)
eqFaultSubclass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqFaultSubclass.setStatus("current")


class _EqFaultType_Type(Integer32):
    """Custom type eqFaultType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqFaultType_Type.__name__ = "Integer32"
_EqFaultType_Object = MibTableColumn
eqFaultType = _EqFaultType_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 4, 1, 1, 1, 5),
    _EqFaultType_Type()
)
eqFaultType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqFaultType.setStatus("current")


class _EqFaultInstance_Type(Integer32):
    """Custom type eqFaultInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqFaultInstance_Type.__name__ = "Integer32"
_EqFaultInstance_Object = MibTableColumn
eqFaultInstance = _EqFaultInstance_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 4, 1, 1, 1, 6),
    _EqFaultInstance_Type()
)
eqFaultInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqFaultInstance.setStatus("current")
_EqFaultSeverity_Type = EqFaultSeverity
_EqFaultSeverity_Object = MibTableColumn
eqFaultSeverity = _EqFaultSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 4, 1, 1, 1, 7),
    _EqFaultSeverity_Type()
)
eqFaultSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqFaultSeverity.setStatus("current")
_EqFaultScope_Type = EqFaultScope
_EqFaultScope_Object = MibTableColumn
eqFaultScope = _EqFaultScope_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 4, 1, 1, 1, 8),
    _EqFaultScope_Type()
)
eqFaultScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqFaultScope.setStatus("current")
_EqFaultSwlm_Type = DisplayString
_EqFaultSwlm_Object = MibTableColumn
eqFaultSwlm = _EqFaultSwlm_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 4, 1, 1, 1, 9),
    _EqFaultSwlm_Type()
)
eqFaultSwlm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqFaultSwlm.setStatus("current")


class _EqFaultModule_Type(Integer32):
    """Custom type eqFaultModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqFaultModule_Type.__name__ = "Integer32"
_EqFaultModule_Object = MibTableColumn
eqFaultModule = _EqFaultModule_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 4, 1, 1, 1, 10),
    _EqFaultModule_Type()
)
eqFaultModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqFaultModule.setStatus("current")
_EqFaultTime_Type = DisplayString
_EqFaultTime_Object = MibTableColumn
eqFaultTime = _EqFaultTime_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 4, 1, 1, 1, 11),
    _EqFaultTime_Type()
)
eqFaultTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqFaultTime.setStatus("current")
_EqFaultDetails_Type = DisplayString
_EqFaultDetails_Object = MibTableColumn
eqFaultDetails = _EqFaultDetails_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 4, 1, 1, 1, 12),
    _EqFaultDetails_Type()
)
eqFaultDetails.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqFaultDetails.setStatus("current")
_EqSysSmsGrp_ObjectIdentity = ObjectIdentity
eqSysSmsGrp = _EqSysSmsGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5022, 1, 5)
)
_EqSysSms_ObjectIdentity = ObjectIdentity
eqSysSms = _EqSysSms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5022, 1, 5, 1)
)


class _EqReleaseNextId_Type(Integer32):
    """Custom type eqReleaseNextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqReleaseNextId_Type.__name__ = "Integer32"
_EqReleaseNextId_Object = MibScalar
eqReleaseNextId = _EqReleaseNextId_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 5, 1, 1),
    _EqReleaseNextId_Type()
)
eqReleaseNextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqReleaseNextId.setStatus("current")
_EqReleaseRevert_Type = EqReleaseRevert
_EqReleaseRevert_Object = MibScalar
eqReleaseRevert = _EqReleaseRevert_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 5, 1, 2),
    _EqReleaseRevert_Type()
)
eqReleaseRevert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqReleaseRevert.setStatus("current")
_EqReleaseTable_Object = MibTable
eqReleaseTable = _EqReleaseTable_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 5, 1, 3)
)
if mibBuilder.loadTexts:
    eqReleaseTable.setStatus("current")
_EqReleaseEntry_Object = MibTableRow
eqReleaseEntry = _EqReleaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 5, 1, 3, 1)
)
eqReleaseEntry.setIndexNames(
    (0, "EQUIPE-SYSTEM-MIB", "eqReleaseId"),
)
if mibBuilder.loadTexts:
    eqReleaseEntry.setStatus("current")


class _EqReleaseId_Type(Integer32):
    """Custom type eqReleaseId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqReleaseId_Type.__name__ = "Integer32"
_EqReleaseId_Object = MibTableColumn
eqReleaseId = _EqReleaseId_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 5, 1, 3, 1, 1),
    _EqReleaseId_Type()
)
eqReleaseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqReleaseId.setStatus("current")
_EqReleaseName_Type = DisplayString
_EqReleaseName_Object = MibTableColumn
eqReleaseName = _EqReleaseName_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 5, 1, 3, 1, 2),
    _EqReleaseName_Type()
)
eqReleaseName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqReleaseName.setStatus("current")


class _EqReleaseVerificationStatus_Type(EqReleaseVerificationStatus):
    """Custom type eqReleaseVerificationStatus based on EqReleaseVerificationStatus"""


_EqReleaseVerificationStatus_Object = MibTableColumn
eqReleaseVerificationStatus = _EqReleaseVerificationStatus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 5, 1, 3, 1, 3),
    _EqReleaseVerificationStatus_Type()
)
eqReleaseVerificationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqReleaseVerificationStatus.setStatus("current")


class _EqReleaseUpgradeScope_Type(EqReleaseUpgradeScope):
    """Custom type eqReleaseUpgradeScope based on EqReleaseUpgradeScope"""


_EqReleaseUpgradeScope_Object = MibTableColumn
eqReleaseUpgradeScope = _EqReleaseUpgradeScope_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 5, 1, 3, 1, 4),
    _EqReleaseUpgradeScope_Type()
)
eqReleaseUpgradeScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqReleaseUpgradeScope.setStatus("current")


class _EqReleaseSchemaChange_Type(EqReleaseSchemaChange):
    """Custom type eqReleaseSchemaChange based on EqReleaseSchemaChange"""


_EqReleaseSchemaChange_Object = MibTableColumn
eqReleaseSchemaChange = _EqReleaseSchemaChange_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 5, 1, 3, 1, 5),
    _EqReleaseSchemaChange_Type()
)
eqReleaseSchemaChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqReleaseSchemaChange.setStatus("current")


class _EqReleaseState_Type(EqReleaseState):
    """Custom type eqReleaseState based on EqReleaseState"""


_EqReleaseState_Object = MibTableColumn
eqReleaseState = _EqReleaseState_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 5, 1, 3, 1, 6),
    _EqReleaseState_Type()
)
eqReleaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqReleaseState.setStatus("current")


class _EqReleaseModulesVerified_Type(Integer32):
    """Custom type eqReleaseModulesVerified based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_EqReleaseModulesVerified_Type.__name__ = "Integer32"
_EqReleaseModulesVerified_Object = MibTableColumn
eqReleaseModulesVerified = _EqReleaseModulesVerified_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 5, 1, 3, 1, 7),
    _EqReleaseModulesVerified_Type()
)
eqReleaseModulesVerified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqReleaseModulesVerified.setStatus("current")


class _EqReleaseNumModules_Type(Integer32):
    """Custom type eqReleaseNumModules based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_EqReleaseNumModules_Type.__name__ = "Integer32"
_EqReleaseNumModules_Object = MibTableColumn
eqReleaseNumModules = _EqReleaseNumModules_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 5, 1, 3, 1, 8),
    _EqReleaseNumModules_Type()
)
eqReleaseNumModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqReleaseNumModules.setStatus("current")
_EqReleaseBadModule_Type = DisplayString
_EqReleaseBadModule_Object = MibTableColumn
eqReleaseBadModule = _EqReleaseBadModule_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 5, 1, 3, 1, 9),
    _EqReleaseBadModule_Type()
)
eqReleaseBadModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqReleaseBadModule.setStatus("current")


class _EqReleaseCommand_Type(EqReleaseCommand):
    """Custom type eqReleaseCommand based on EqReleaseCommand"""


_EqReleaseCommand_Object = MibTableColumn
eqReleaseCommand = _EqReleaseCommand_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 5, 1, 3, 1, 10),
    _EqReleaseCommand_Type()
)
eqReleaseCommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqReleaseCommand.setStatus("current")


class _EqReleaseCommandStatus_Type(EqReleaseCommandStatus):
    """Custom type eqReleaseCommandStatus based on EqReleaseCommandStatus"""


_EqReleaseCommandStatus_Object = MibTableColumn
eqReleaseCommandStatus = _EqReleaseCommandStatus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 5, 1, 3, 1, 11),
    _EqReleaseCommandStatus_Type()
)
eqReleaseCommandStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqReleaseCommandStatus.setStatus("current")
_EqReleaseSchemaVersion_Type = DisplayString
_EqReleaseSchemaVersion_Object = MibTableColumn
eqReleaseSchemaVersion = _EqReleaseSchemaVersion_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 5, 1, 3, 1, 12),
    _EqReleaseSchemaVersion_Type()
)
eqReleaseSchemaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqReleaseSchemaVersion.setStatus("current")


class _EqReleaseConfigAvail_Type(EqReleaseConfigAvail):
    """Custom type eqReleaseConfigAvail based on EqReleaseConfigAvail"""


_EqReleaseConfigAvail_Object = MibTableColumn
eqReleaseConfigAvail = _EqReleaseConfigAvail_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 5, 1, 3, 1, 13),
    _EqReleaseConfigAvail_Type()
)
eqReleaseConfigAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqReleaseConfigAvail.setStatus("current")
_EqReleaseRowStatus_Type = RowStatus
_EqReleaseRowStatus_Object = MibTableColumn
eqReleaseRowStatus = _EqReleaseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 5, 1, 3, 1, 14),
    _EqReleaseRowStatus_Type()
)
eqReleaseRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqReleaseRowStatus.setStatus("current")
_EqInstallTable_Object = MibTable
eqInstallTable = _EqInstallTable_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 5, 1, 4)
)
if mibBuilder.loadTexts:
    eqInstallTable.setStatus("current")
_EqInstallEntry_Object = MibTableRow
eqInstallEntry = _EqInstallEntry_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 5, 1, 4, 1)
)
eqInstallEntry.setIndexNames(
    (0, "EQUIPE-SYSTEM-MIB", "eqInstallId"),
)
if mibBuilder.loadTexts:
    eqInstallEntry.setStatus("current")


class _EqInstallId_Type(Integer32):
    """Custom type eqInstallId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqInstallId_Type.__name__ = "Integer32"
_EqInstallId_Object = MibTableColumn
eqInstallId = _EqInstallId_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 5, 1, 4, 1, 1),
    _EqInstallId_Type()
)
eqInstallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqInstallId.setStatus("current")
_EqInstallPath_Type = DisplayString
_EqInstallPath_Object = MibTableColumn
eqInstallPath = _EqInstallPath_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 5, 1, 4, 1, 2),
    _EqInstallPath_Type()
)
eqInstallPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqInstallPath.setStatus("current")
_EqUpgradeState_Type = DisplayString
_EqUpgradeState_Object = MibScalar
eqUpgradeState = _EqUpgradeState_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 5, 1, 5),
    _EqUpgradeState_Type()
)
eqUpgradeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqUpgradeState.setStatus("current")
_EqSysIntfGrp_ObjectIdentity = ObjectIdentity
eqSysIntfGrp = _EqSysIntfGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5022, 1, 6)
)
_EqIntfBertTable_Object = MibTable
eqIntfBertTable = _EqIntfBertTable_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 6, 1)
)
if mibBuilder.loadTexts:
    eqIntfBertTable.setStatus("current")
_EqIntfBertEntry_Object = MibTableRow
eqIntfBertEntry = _EqIntfBertEntry_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 6, 1, 1)
)
eqIntfBertEntry.setIndexNames(
    (0, "EQUIPE-SYSTEM-MIB", "eqIntfBertEid"),
)
if mibBuilder.loadTexts:
    eqIntfBertEntry.setStatus("current")


class _EqIntfBertEid_Type(Integer32):
    """Custom type eqIntfBertEid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqIntfBertEid_Type.__name__ = "Integer32"
_EqIntfBertEid_Object = MibTableColumn
eqIntfBertEid = _EqIntfBertEid_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 6, 1, 1, 1),
    _EqIntfBertEid_Type()
)
eqIntfBertEid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqIntfBertEid.setStatus("current")


class _EqIntfBertGeneratorState_Type(Integer32):
    """Custom type eqIntfBertGeneratorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_EqIntfBertGeneratorState_Type.__name__ = "Integer32"
_EqIntfBertGeneratorState_Object = MibTableColumn
eqIntfBertGeneratorState = _EqIntfBertGeneratorState_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 6, 1, 1, 2),
    _EqIntfBertGeneratorState_Type()
)
eqIntfBertGeneratorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqIntfBertGeneratorState.setStatus("current")


class _EqIntfBertMonitorState_Type(Integer32):
    """Custom type eqIntfBertMonitorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_EqIntfBertMonitorState_Type.__name__ = "Integer32"
_EqIntfBertMonitorState_Object = MibTableColumn
eqIntfBertMonitorState = _EqIntfBertMonitorState_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 6, 1, 1, 3),
    _EqIntfBertMonitorState_Type()
)
eqIntfBertMonitorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqIntfBertMonitorState.setStatus("current")


class _EqIntfBertMonitorStatus_Type(Integer32):
    """Custom type eqIntfBertMonitorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inSync", 1),
          ("outOfSync", 2))
    )


_EqIntfBertMonitorStatus_Type.__name__ = "Integer32"
_EqIntfBertMonitorStatus_Object = MibTableColumn
eqIntfBertMonitorStatus = _EqIntfBertMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 6, 1, 1, 4),
    _EqIntfBertMonitorStatus_Type()
)
eqIntfBertMonitorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqIntfBertMonitorStatus.setStatus("current")


class _EqIntfBertMonitorOutOfSyncTime_Type(Integer32):
    """Custom type eqIntfBertMonitorOutOfSyncTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EqIntfBertMonitorOutOfSyncTime_Type.__name__ = "Integer32"
_EqIntfBertMonitorOutOfSyncTime_Object = MibTableColumn
eqIntfBertMonitorOutOfSyncTime = _EqIntfBertMonitorOutOfSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 6, 1, 1, 5),
    _EqIntfBertMonitorOutOfSyncTime_Type()
)
eqIntfBertMonitorOutOfSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqIntfBertMonitorOutOfSyncTime.setStatus("current")


class _EqIntfBertRequestedBitErrorCount_Type(Integer32):
    """Custom type eqIntfBertRequestedBitErrorCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EqIntfBertRequestedBitErrorCount_Type.__name__ = "Integer32"
_EqIntfBertRequestedBitErrorCount_Object = MibTableColumn
eqIntfBertRequestedBitErrorCount = _EqIntfBertRequestedBitErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 6, 1, 1, 6),
    _EqIntfBertRequestedBitErrorCount_Type()
)
eqIntfBertRequestedBitErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqIntfBertRequestedBitErrorCount.setStatus("current")


class _EqIntfBertInsertedBitErrorCount_Type(Integer32):
    """Custom type eqIntfBertInsertedBitErrorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EqIntfBertInsertedBitErrorCount_Type.__name__ = "Integer32"
_EqIntfBertInsertedBitErrorCount_Object = MibTableColumn
eqIntfBertInsertedBitErrorCount = _EqIntfBertInsertedBitErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 6, 1, 1, 7),
    _EqIntfBertInsertedBitErrorCount_Type()
)
eqIntfBertInsertedBitErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqIntfBertInsertedBitErrorCount.setStatus("current")


class _EqIntfBertMeasuredByteErrorCount_Type(Integer32):
    """Custom type eqIntfBertMeasuredByteErrorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EqIntfBertMeasuredByteErrorCount_Type.__name__ = "Integer32"
_EqIntfBertMeasuredByteErrorCount_Object = MibTableColumn
eqIntfBertMeasuredByteErrorCount = _EqIntfBertMeasuredByteErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 6, 1, 1, 8),
    _EqIntfBertMeasuredByteErrorCount_Type()
)
eqIntfBertMeasuredByteErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqIntfBertMeasuredByteErrorCount.setStatus("current")
_EqIntfBertTestStartTime_Type = DateAndTime
_EqIntfBertTestStartTime_Object = MibTableColumn
eqIntfBertTestStartTime = _EqIntfBertTestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 6, 1, 1, 9),
    _EqIntfBertTestStartTime_Type()
)
eqIntfBertTestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqIntfBertTestStartTime.setStatus("current")


class _EqIntfBertTestDuration_Type(Integer32):
    """Custom type eqIntfBertTestDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EqIntfBertTestDuration_Type.__name__ = "Integer32"
_EqIntfBertTestDuration_Object = MibTableColumn
eqIntfBertTestDuration = _EqIntfBertTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 6, 1, 1, 10),
    _EqIntfBertTestDuration_Type()
)
eqIntfBertTestDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqIntfBertTestDuration.setStatus("current")


class _EqIntfBertAction_Type(Integer32):
    """Custom type eqIntfBertAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("insertBitError", 2),
          ("other", 1))
    )


_EqIntfBertAction_Type.__name__ = "Integer32"
_EqIntfBertAction_Object = MibTableColumn
eqIntfBertAction = _EqIntfBertAction_Object(
    (1, 3, 6, 1, 4, 1, 5022, 1, 6, 1, 1, 11),
    _EqIntfBertAction_Type()
)
eqIntfBertAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqIntfBertAction.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQUIPE-SYSTEM-MIB",
    **{"EqModuleType": EqModuleType,
       "EqModuleStatus": EqModuleStatus,
       "EqModuleHealthStatus": EqModuleHealthStatus,
       "EqModuleFeedStatus": EqModuleFeedStatus,
       "EqModuleRedRole": EqModuleRedRole,
       "EqIfType": EqIfType,
       "EqAtmPvcType": EqAtmPvcType,
       "EqApsLineState": EqApsLineState,
       "EqSeverityLevel": EqSeverityLevel,
       "EqFaultClass": EqFaultClass,
       "EqFaultSeverity": EqFaultSeverity,
       "EqFaultScope": EqFaultScope,
       "EqReleaseVerificationStatus": EqReleaseVerificationStatus,
       "EqReleaseUpgradeScope": EqReleaseUpgradeScope,
       "EqReleaseState": EqReleaseState,
       "EqReleaseCommand": EqReleaseCommand,
       "EqReleaseCommandStatus": EqReleaseCommandStatus,
       "EqReleaseSchemaChange": EqReleaseSchemaChange,
       "EqReleaseConfigAvail": EqReleaseConfigAvail,
       "EqReleaseRevert": EqReleaseRevert,
       "equipe": equipe,
       "eqSystemMib": eqSystemMib,
       "eqSysProducts": eqSysProducts,
       "eqSysProductE3200": eqSysProductE3200,
       "eqSysSystemGrp": eqSysSystemGrp,
       "eqSysSystem": eqSysSystem,
       "eqSysSystemId": eqSysSystemId,
       "eqSysPhysEntLastChangeTime": eqSysPhysEntLastChangeTime,
       "eqSysConfig": eqSysConfig,
       "eqSysCfgCopyConfigFileAction": eqSysCfgCopyConfigFileAction,
       "eqSysCfgCopyConfigFileStatus": eqSysCfgCopyConfigFileStatus,
       "eqSysCfgSavedFilename": eqSysCfgSavedFilename,
       "eqEidReqTable": eqEidReqTable,
       "eqEidReqEntry": eqEidReqEntry,
       "eqEidReqIndex": eqEidReqIndex,
       "eqEidReqUser": eqEidReqUser,
       "eqEidReqCount": eqEidReqCount,
       "eqEidReqCountAlloc": eqEidReqCountAlloc,
       "eqEidReqAction": eqEidReqAction,
       "eqEidReqActionStatus": eqEidReqActionStatus,
       "eqEidReqRowStatus": eqEidReqRowStatus,
       "eqEidResTable": eqEidResTable,
       "eqEidResEntry": eqEidResEntry,
       "eqEidResIndex": eqEidResIndex,
       "eqEidResData": eqEidResData,
       "eqSysModuleGrp": eqSysModuleGrp,
       "eqSysModule": eqSysModule,
       "eqModuleTable": eqModuleTable,
       "eqModuleEntry": eqModuleEntry,
       "eqModuleEid": eqModuleEid,
       "eqModuleShelfId": eqModuleShelfId,
       "eqModuleSlotId": eqModuleSlotId,
       "eqModuleType": eqModuleType,
       "eqModuleHwVersion": eqModuleHwVersion,
       "eqModuleStatus": eqModuleStatus,
       "eqModuleAction": eqModuleAction,
       "eqModuleHealthTable": eqModuleHealthTable,
       "eqModuleHealthEntry": eqModuleHealthEntry,
       "eqModuleHealthStatus": eqModuleHealthStatus,
       "eqModuleMemTotal": eqModuleMemTotal,
       "eqModuleMemUsed": eqModuleMemUsed,
       "eqModuleMemUsedPercent": eqModuleMemUsedPercent,
       "eqModuleTemp": eqModuleTemp,
       "eqModuleCpuUtil": eqModuleCpuUtil,
       "eqModuleFeedStatusA": eqModuleFeedStatusA,
       "eqModuleFeedStatusB": eqModuleFeedStatusB,
       "eqHardDiskTable": eqHardDiskTable,
       "eqHardDiskEntry": eqHardDiskEntry,
       "eqHardDiskEid": eqHardDiskEid,
       "eqHardDiskShelfId": eqHardDiskShelfId,
       "eqHardDiskSlotId": eqHardDiskSlotId,
       "eqHardDiskCapacity": eqHardDiskCapacity,
       "eqHardDiskUsed": eqHardDiskUsed,
       "eqHardDiskUsedHiMark": eqHardDiskUsedHiMark,
       "eqHardDiskUsedLowMark": eqHardDiskUsedLowMark,
       "eqFanUnitTable": eqFanUnitTable,
       "eqFanUnitEntry": eqFanUnitEntry,
       "eqFanUnitEid": eqFanUnitEid,
       "eqFanUnitShelfId": eqFanUnitShelfId,
       "eqFanUnitSlotId": eqFanUnitSlotId,
       "eqFanUnitRpm": eqFanUnitRpm,
       "eqFanUnitRpmHiMark": eqFanUnitRpmHiMark,
       "eqFanUnitRpmLowMark": eqFanUnitRpmLowMark,
       "eqModuleRedTable": eqModuleRedTable,
       "eqModuleRedEntry": eqModuleRedEntry,
       "eqModuleRedEid": eqModuleRedEid,
       "eqModuleRedAdminRole": eqModuleRedAdminRole,
       "eqModuleRedOperRole": eqModuleRedOperRole,
       "eqModuleRedPeerId": eqModuleRedPeerId,
       "eqModuleRedAction": eqModuleRedAction,
       "eqStratumCentTable": eqStratumCentTable,
       "eqStratumCentEntry": eqStratumCentEntry,
       "eqStratumCentEid": eqStratumCentEid,
       "eqStratumCentStatus": eqStratumCentStatus,
       "eqStratumCentRedStatus": eqStratumCentRedStatus,
       "eqStratumCentLevel": eqStratumCentLevel,
       "eqStratumCentPrimaryRefStatus": eqStratumCentPrimaryRefStatus,
       "eqStratumCentSecondaryRefStatus": eqStratumCentSecondaryRefStatus,
       "eqStratumCentStatusAction": eqStratumCentStatusAction,
       "eqStratumCentRedAction": eqStratumCentRedAction,
       "eqStratumLocalTable": eqStratumLocalTable,
       "eqStratumLocalEntry": eqStratumLocalEntry,
       "eqStratumLocalEid": eqStratumLocalEid,
       "eqStratumLocalInputA1Status": eqStratumLocalInputA1Status,
       "eqStratumLocalInputA2Status": eqStratumLocalInputA2Status,
       "eqStratumLocalInputB1Status": eqStratumLocalInputB1Status,
       "eqStratumLocalInputB2Status": eqStratumLocalInputB2Status,
       "eqStratumLocalInputUsed": eqStratumLocalInputUsed,
       "eqStratumLocalRecoveredRefStatus": eqStratumLocalRecoveredRefStatus,
       "eqStratumLocalStatusAction": eqStratumLocalStatusAction,
       "eqSysFaultGrp": eqSysFaultGrp,
       "eqSysFault": eqSysFault,
       "eqFaultTable": eqFaultTable,
       "eqFaultEntry": eqFaultEntry,
       "eqFaultDomain": eqFaultDomain,
       "eqFaultHandle": eqFaultHandle,
       "eqFaultClass": eqFaultClass,
       "eqFaultSubclass": eqFaultSubclass,
       "eqFaultType": eqFaultType,
       "eqFaultInstance": eqFaultInstance,
       "eqFaultSeverity": eqFaultSeverity,
       "eqFaultScope": eqFaultScope,
       "eqFaultSwlm": eqFaultSwlm,
       "eqFaultModule": eqFaultModule,
       "eqFaultTime": eqFaultTime,
       "eqFaultDetails": eqFaultDetails,
       "eqSysSmsGrp": eqSysSmsGrp,
       "eqSysSms": eqSysSms,
       "eqReleaseNextId": eqReleaseNextId,
       "eqReleaseRevert": eqReleaseRevert,
       "eqReleaseTable": eqReleaseTable,
       "eqReleaseEntry": eqReleaseEntry,
       "eqReleaseId": eqReleaseId,
       "eqReleaseName": eqReleaseName,
       "eqReleaseVerificationStatus": eqReleaseVerificationStatus,
       "eqReleaseUpgradeScope": eqReleaseUpgradeScope,
       "eqReleaseSchemaChange": eqReleaseSchemaChange,
       "eqReleaseState": eqReleaseState,
       "eqReleaseModulesVerified": eqReleaseModulesVerified,
       "eqReleaseNumModules": eqReleaseNumModules,
       "eqReleaseBadModule": eqReleaseBadModule,
       "eqReleaseCommand": eqReleaseCommand,
       "eqReleaseCommandStatus": eqReleaseCommandStatus,
       "eqReleaseSchemaVersion": eqReleaseSchemaVersion,
       "eqReleaseConfigAvail": eqReleaseConfigAvail,
       "eqReleaseRowStatus": eqReleaseRowStatus,
       "eqInstallTable": eqInstallTable,
       "eqInstallEntry": eqInstallEntry,
       "eqInstallId": eqInstallId,
       "eqInstallPath": eqInstallPath,
       "eqUpgradeState": eqUpgradeState,
       "eqSysIntfGrp": eqSysIntfGrp,
       "eqIntfBertTable": eqIntfBertTable,
       "eqIntfBertEntry": eqIntfBertEntry,
       "eqIntfBertEid": eqIntfBertEid,
       "eqIntfBertGeneratorState": eqIntfBertGeneratorState,
       "eqIntfBertMonitorState": eqIntfBertMonitorState,
       "eqIntfBertMonitorStatus": eqIntfBertMonitorStatus,
       "eqIntfBertMonitorOutOfSyncTime": eqIntfBertMonitorOutOfSyncTime,
       "eqIntfBertRequestedBitErrorCount": eqIntfBertRequestedBitErrorCount,
       "eqIntfBertInsertedBitErrorCount": eqIntfBertInsertedBitErrorCount,
       "eqIntfBertMeasuredByteErrorCount": eqIntfBertMeasuredByteErrorCount,
       "eqIntfBertTestStartTime": eqIntfBertTestStartTime,
       "eqIntfBertTestDuration": eqIntfBertTestDuration,
       "eqIntfBertAction": eqIntfBertAction}
)
