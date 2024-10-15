# SNMP MIB module (CT-CMMPHYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CT-CMMPHYS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:01 2024
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

(mBusBoardID,) = mibBuilder.importSymbols(
    "CT-HSIMPHYS-MIB",
    "mBusBoardID")

(ctCMM,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctCMM")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CmmModemInfo_ObjectIdentity = ObjectIdentity
cmmModemInfo = _CmmModemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1)
)
_CmmBoardTable_Object = MibTable
cmmBoardTable = _CmmBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 1)
)
if mibBuilder.loadTexts:
    cmmBoardTable.setStatus("mandatory")
_CmmBoardEntry_Object = MibTableRow
cmmBoardEntry = _CmmBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 1, 1)
)
cmmBoardEntry.setIndexNames(
    (0, "CT-HSIMPHYS-MIB", "mBusBoardID"),
)
if mibBuilder.loadTexts:
    cmmBoardEntry.setStatus("mandatory")
_CmmBoardType_Type = ObjectIdentifier
_CmmBoardType_Object = MibTableColumn
cmmBoardType = _CmmBoardType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 1, 1, 1),
    _CmmBoardType_Type()
)
cmmBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmBoardType.setStatus("mandatory")
_CmmNumModules_Type = Integer32
_CmmNumModules_Object = MibTableColumn
cmmNumModules = _CmmNumModules_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 1, 1, 2),
    _CmmNumModules_Type()
)
cmmNumModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmNumModules.setStatus("mandatory")
_CmmModuleNumModems_Type = Integer32
_CmmModuleNumModems_Object = MibTableColumn
cmmModuleNumModems = _CmmModuleNumModems_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 1, 1, 3),
    _CmmModuleNumModems_Type()
)
cmmModuleNumModems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmModuleNumModems.setStatus("mandatory")
_CmmTFTPServer_Type = IpAddress
_CmmTFTPServer_Object = MibTableColumn
cmmTFTPServer = _CmmTFTPServer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 1, 1, 4),
    _CmmTFTPServer_Type()
)
cmmTFTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmTFTPServer.setStatus("mandatory")
_CmmUpgradePath_Type = DisplayString
_CmmUpgradePath_Object = MibTableColumn
cmmUpgradePath = _CmmUpgradePath_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 1, 1, 5),
    _CmmUpgradePath_Type()
)
cmmUpgradePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmUpgradePath.setStatus("mandatory")


class _CmmUpgradeFlag_Type(Integer32):
    """Custom type cmmUpgradeFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_CmmUpgradeFlag_Type.__name__ = "Integer32"
_CmmUpgradeFlag_Object = MibTableColumn
cmmUpgradeFlag = _CmmUpgradeFlag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 1, 1, 6),
    _CmmUpgradeFlag_Type()
)
cmmUpgradeFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmUpgradeFlag.setStatus("mandatory")


class _CmmCommitFlag_Type(Integer32):
    """Custom type cmmCommitFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_CmmCommitFlag_Type.__name__ = "Integer32"
_CmmCommitFlag_Object = MibTableColumn
cmmCommitFlag = _CmmCommitFlag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 1, 1, 7),
    _CmmCommitFlag_Type()
)
cmmCommitFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmCommitFlag.setStatus("mandatory")
_CmmModemResetLimit_Type = Integer32
_CmmModemResetLimit_Object = MibTableColumn
cmmModemResetLimit = _CmmModemResetLimit_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 1, 1, 8),
    _CmmModemResetLimit_Type()
)
cmmModemResetLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmModemResetLimit.setStatus("mandatory")
_CmmModemResetTime_Type = Integer32
_CmmModemResetTime_Object = MibTableColumn
cmmModemResetTime = _CmmModemResetTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 1, 1, 9),
    _CmmModemResetTime_Type()
)
cmmModemResetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmModemResetTime.setStatus("mandatory")
_CmmOutgoingInactivityTimeout_Type = Integer32
_CmmOutgoingInactivityTimeout_Object = MibTableColumn
cmmOutgoingInactivityTimeout = _CmmOutgoingInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 1, 1, 10),
    _CmmOutgoingInactivityTimeout_Type()
)
cmmOutgoingInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmOutgoingInactivityTimeout.setStatus("mandatory")
_CmmIncomingInactivityTimeout_Type = Integer32
_CmmIncomingInactivityTimeout_Object = MibTableColumn
cmmIncomingInactivityTimeout = _CmmIncomingInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 1, 1, 11),
    _CmmIncomingInactivityTimeout_Type()
)
cmmIncomingInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmIncomingInactivityTimeout.setStatus("mandatory")
_CmmAsyncBaseOrigATCmdStr_Type = DisplayString
_CmmAsyncBaseOrigATCmdStr_Object = MibTableColumn
cmmAsyncBaseOrigATCmdStr = _CmmAsyncBaseOrigATCmdStr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 1, 1, 12),
    _CmmAsyncBaseOrigATCmdStr_Type()
)
cmmAsyncBaseOrigATCmdStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmAsyncBaseOrigATCmdStr.setStatus("mandatory")
_CmmAsyncBaseAnswerATCmdStr_Type = DisplayString
_CmmAsyncBaseAnswerATCmdStr_Object = MibTableColumn
cmmAsyncBaseAnswerATCmdStr = _CmmAsyncBaseAnswerATCmdStr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 1, 1, 13),
    _CmmAsyncBaseAnswerATCmdStr_Type()
)
cmmAsyncBaseAnswerATCmdStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmAsyncBaseAnswerATCmdStr.setStatus("mandatory")
_CmmAsyncOrigStrModifier_Type = DisplayString
_CmmAsyncOrigStrModifier_Object = MibTableColumn
cmmAsyncOrigStrModifier = _CmmAsyncOrigStrModifier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 1, 1, 14),
    _CmmAsyncOrigStrModifier_Type()
)
cmmAsyncOrigStrModifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmAsyncOrigStrModifier.setStatus("mandatory")
_CmmAsyncAnswerStrModifier_Type = DisplayString
_CmmAsyncAnswerStrModifier_Object = MibTableColumn
cmmAsyncAnswerStrModifier = _CmmAsyncAnswerStrModifier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 1, 1, 15),
    _CmmAsyncAnswerStrModifier_Type()
)
cmmAsyncAnswerStrModifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmAsyncAnswerStrModifier.setStatus("mandatory")
_CmmAsyncOperOrigATCmdStr_Type = DisplayString
_CmmAsyncOperOrigATCmdStr_Object = MibTableColumn
cmmAsyncOperOrigATCmdStr = _CmmAsyncOperOrigATCmdStr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 1, 1, 16),
    _CmmAsyncOperOrigATCmdStr_Type()
)
cmmAsyncOperOrigATCmdStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmAsyncOperOrigATCmdStr.setStatus("mandatory")
_CmmAsyncOperAnswerATCmdStr_Type = DisplayString
_CmmAsyncOperAnswerATCmdStr_Object = MibTableColumn
cmmAsyncOperAnswerATCmdStr = _CmmAsyncOperAnswerATCmdStr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 1, 1, 17),
    _CmmAsyncOperAnswerATCmdStr_Type()
)
cmmAsyncOperAnswerATCmdStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmAsyncOperAnswerATCmdStr.setStatus("mandatory")
_CmmHdlcBaseOrigATCmdStr_Type = DisplayString
_CmmHdlcBaseOrigATCmdStr_Object = MibTableColumn
cmmHdlcBaseOrigATCmdStr = _CmmHdlcBaseOrigATCmdStr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 1, 1, 18),
    _CmmHdlcBaseOrigATCmdStr_Type()
)
cmmHdlcBaseOrigATCmdStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmHdlcBaseOrigATCmdStr.setStatus("mandatory")
_CmmHdlcBaseAnswerATCmdStr_Type = DisplayString
_CmmHdlcBaseAnswerATCmdStr_Object = MibTableColumn
cmmHdlcBaseAnswerATCmdStr = _CmmHdlcBaseAnswerATCmdStr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 1, 1, 19),
    _CmmHdlcBaseAnswerATCmdStr_Type()
)
cmmHdlcBaseAnswerATCmdStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmHdlcBaseAnswerATCmdStr.setStatus("mandatory")
_CmmHdlcOrigStrModifier_Type = DisplayString
_CmmHdlcOrigStrModifier_Object = MibTableColumn
cmmHdlcOrigStrModifier = _CmmHdlcOrigStrModifier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 1, 1, 20),
    _CmmHdlcOrigStrModifier_Type()
)
cmmHdlcOrigStrModifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmHdlcOrigStrModifier.setStatus("mandatory")
_CmmHdlcAnswerStrModifier_Type = DisplayString
_CmmHdlcAnswerStrModifier_Object = MibTableColumn
cmmHdlcAnswerStrModifier = _CmmHdlcAnswerStrModifier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 1, 1, 21),
    _CmmHdlcAnswerStrModifier_Type()
)
cmmHdlcAnswerStrModifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmHdlcAnswerStrModifier.setStatus("mandatory")
_CmmHdlcOperOrigATCmdStr_Type = DisplayString
_CmmHdlcOperOrigATCmdStr_Object = MibTableColumn
cmmHdlcOperOrigATCmdStr = _CmmHdlcOperOrigATCmdStr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 1, 1, 22),
    _CmmHdlcOperOrigATCmdStr_Type()
)
cmmHdlcOperOrigATCmdStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmHdlcOperOrigATCmdStr.setStatus("mandatory")
_CmmHdlcOperAnswerATCmdStr_Type = DisplayString
_CmmHdlcOperAnswerATCmdStr_Object = MibTableColumn
cmmHdlcOperAnswerATCmdStr = _CmmHdlcOperAnswerATCmdStr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 1, 1, 23),
    _CmmHdlcOperAnswerATCmdStr_Type()
)
cmmHdlcOperAnswerATCmdStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmHdlcOperAnswerATCmdStr.setStatus("mandatory")


class _CmmBoardAdminStatus_Type(Integer32):
    """Custom type cmmBoardAdminStatus based on Integer32"""
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
        *(("down", 1),
          ("leave-service", 2),
          ("up", 3),
          ("upgrade", 4))
    )


_CmmBoardAdminStatus_Type.__name__ = "Integer32"
_CmmBoardAdminStatus_Object = MibTableColumn
cmmBoardAdminStatus = _CmmBoardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 1, 1, 24),
    _CmmBoardAdminStatus_Type()
)
cmmBoardAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmBoardAdminStatus.setStatus("mandatory")


class _CmmBoardOperStatus_Type(Integer32):
    """Custom type cmmBoardOperStatus based on Integer32"""
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
        *(("active", 2),
          ("faulty", 5),
          ("impaired", 6),
          ("initializing", 1),
          ("leaving-service", 3),
          ("out-of-service", 4))
    )


_CmmBoardOperStatus_Type.__name__ = "Integer32"
_CmmBoardOperStatus_Object = MibTableColumn
cmmBoardOperStatus = _CmmBoardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 1, 1, 25),
    _CmmBoardOperStatus_Type()
)
cmmBoardOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmBoardOperStatus.setStatus("mandatory")
_CmmModuleTable_Object = MibTable
cmmModuleTable = _CmmModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 2)
)
if mibBuilder.loadTexts:
    cmmModuleTable.setStatus("mandatory")
_CmmModuleEntry_Object = MibTableRow
cmmModuleEntry = _CmmModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 2, 1)
)
cmmModuleEntry.setIndexNames(
    (0, "CT-HSIMPHYS-MIB", "mBusBoardID"),
    (0, "CT-CMMPHYS-MIB", "cmmModuleID"),
)
if mibBuilder.loadTexts:
    cmmModuleEntry.setStatus("mandatory")
_CmmModuleID_Type = Integer32
_CmmModuleID_Object = MibTableColumn
cmmModuleID = _CmmModuleID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 2, 1, 1),
    _CmmModuleID_Type()
)
cmmModuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmModuleID.setStatus("mandatory")
_CmmDpramSize_Type = Integer32
_CmmDpramSize_Object = MibTableColumn
cmmDpramSize = _CmmDpramSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 2, 1, 2),
    _CmmDpramSize_Type()
)
cmmDpramSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmDpramSize.setStatus("mandatory")
_CmmSdramSize_Type = Integer32
_CmmSdramSize_Object = MibTableColumn
cmmSdramSize = _CmmSdramSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 2, 1, 3),
    _CmmSdramSize_Type()
)
cmmSdramSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSdramSize.setStatus("mandatory")


class _CmmCpuType_Type(Integer32):
    """Custom type cmmCpuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hitachish3", 2),
          ("hitachish4", 3),
          ("unknown", 1))
    )


_CmmCpuType_Type.__name__ = "Integer32"
_CmmCpuType_Object = MibTableColumn
cmmCpuType = _CmmCpuType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 2, 1, 4),
    _CmmCpuType_Type()
)
cmmCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmCpuType.setStatus("mandatory")
_CmmCpuSpeed_Type = Integer32
_CmmCpuSpeed_Object = MibTableColumn
cmmCpuSpeed = _CmmCpuSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 2, 1, 5),
    _CmmCpuSpeed_Type()
)
cmmCpuSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmCpuSpeed.setStatus("mandatory")
_CmmCpuFwRev_Type = DisplayString
_CmmCpuFwRev_Object = MibTableColumn
cmmCpuFwRev = _CmmCpuFwRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 2, 1, 6),
    _CmmCpuFwRev_Type()
)
cmmCpuFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmCpuFwRev.setStatus("mandatory")
_CmmEpldId_Type = DisplayString
_CmmEpldId_Object = MibTableColumn
cmmEpldId = _CmmEpldId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 2, 1, 7),
    _CmmEpldId_Type()
)
cmmEpldId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmEpldId.setStatus("mandatory")
_CmmEpldRev_Type = DisplayString
_CmmEpldRev_Object = MibTableColumn
cmmEpldRev = _CmmEpldRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 2, 1, 8),
    _CmmEpldRev_Type()
)
cmmEpldRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmEpldRev.setStatus("mandatory")
_CmmNumBadModems_Type = Integer32
_CmmNumBadModems_Object = MibTableColumn
cmmNumBadModems = _CmmNumBadModems_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 2, 1, 9),
    _CmmNumBadModems_Type()
)
cmmNumBadModems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmNumBadModems.setStatus("mandatory")


class _CmmModuleAdminStatus_Type(Integer32):
    """Custom type cmmModuleAdminStatus based on Integer32"""
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
        *(("down", 1),
          ("faulty", 6),
          ("leave-service", 2),
          ("reset", 5),
          ("run-diagnostics", 4),
          ("up", 3))
    )


_CmmModuleAdminStatus_Type.__name__ = "Integer32"
_CmmModuleAdminStatus_Object = MibTableColumn
cmmModuleAdminStatus = _CmmModuleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 2, 1, 10),
    _CmmModuleAdminStatus_Type()
)
cmmModuleAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmModuleAdminStatus.setStatus("mandatory")


class _CmmModuleOperStatus_Type(Integer32):
    """Custom type cmmModuleOperStatus based on Integer32"""
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
        *(("active", 2),
          ("faulty", 5),
          ("impaired", 6),
          ("initializing", 1),
          ("leaving-service", 3),
          ("out-of-service", 4))
    )


_CmmModuleOperStatus_Type.__name__ = "Integer32"
_CmmModuleOperStatus_Object = MibTableColumn
cmmModuleOperStatus = _CmmModuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 2, 1, 11),
    _CmmModuleOperStatus_Type()
)
cmmModuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmModuleOperStatus.setStatus("mandatory")
_CmmModemTable_Object = MibTable
cmmModemTable = _CmmModemTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3)
)
if mibBuilder.loadTexts:
    cmmModemTable.setStatus("mandatory")
_CmmModemEntry_Object = MibTableRow
cmmModemEntry = _CmmModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1)
)
cmmModemEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cmmModemEntry.setStatus("mandatory")
_CmmBoardID_Type = Integer32
_CmmBoardID_Object = MibTableColumn
cmmBoardID = _CmmBoardID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 1),
    _CmmBoardID_Type()
)
cmmBoardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmBoardID.setStatus("mandatory")
_CmmModemID_Type = Integer32
_CmmModemID_Object = MibTableColumn
cmmModemID = _CmmModemID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 2),
    _CmmModemID_Type()
)
cmmModemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmModemID.setStatus("mandatory")
_CmmIFNum_Type = Integer32
_CmmIFNum_Object = MibTableColumn
cmmIFNum = _CmmIFNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 3),
    _CmmIFNum_Type()
)
cmmIFNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIFNum.setStatus("mandatory")
_CmmSessionNum_Type = Integer32
_CmmSessionNum_Object = MibTableColumn
cmmSessionNum = _CmmSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 4),
    _CmmSessionNum_Type()
)
cmmSessionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSessionNum.setStatus("mandatory")
_CmmDdpPartNum_Type = DisplayString
_CmmDdpPartNum_Object = MibTableColumn
cmmDdpPartNum = _CmmDdpPartNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 5),
    _CmmDdpPartNum_Type()
)
cmmDdpPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmDdpPartNum.setStatus("mandatory")
_CmmDdpRevLevel_Type = DisplayString
_CmmDdpRevLevel_Object = MibTableColumn
cmmDdpRevLevel = _CmmDdpRevLevel_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 6),
    _CmmDdpRevLevel_Type()
)
cmmDdpRevLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmDdpRevLevel.setStatus("mandatory")
_CmmDdpFwRev_Type = DisplayString
_CmmDdpFwRev_Object = MibTableColumn
cmmDdpFwRev = _CmmDdpFwRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 7),
    _CmmDdpFwRev_Type()
)
cmmDdpFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmDdpFwRev.setStatus("mandatory")
_CmmDDPInterrupts_Type = Counter32
_CmmDDPInterrupts_Object = MibTableColumn
cmmDDPInterrupts = _CmmDDPInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 8),
    _CmmDDPInterrupts_Type()
)
cmmDDPInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmDDPInterrupts.setStatus("mandatory")
_CmmRxFlowCtlEvts_Type = Counter32
_CmmRxFlowCtlEvts_Object = MibTableColumn
cmmRxFlowCtlEvts = _CmmRxFlowCtlEvts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 9),
    _CmmRxFlowCtlEvts_Type()
)
cmmRxFlowCtlEvts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmRxFlowCtlEvts.setStatus("mandatory")
_CmmTxFlowCtlEvts_Type = Counter32
_CmmTxFlowCtlEvts_Object = MibTableColumn
cmmTxFlowCtlEvts = _CmmTxFlowCtlEvts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 10),
    _CmmTxFlowCtlEvts_Type()
)
cmmTxFlowCtlEvts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmTxFlowCtlEvts.setStatus("mandatory")


class _CmmCallStatus_Type(Integer32):
    """Custom type cmmCallStatus based on Integer32"""
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
        *(("connected", 2),
          ("dropping", 4),
          ("idle", 1),
          ("local-test", 5),
          ("remote-test", 6),
          ("retraining", 3))
    )


_CmmCallStatus_Type.__name__ = "Integer32"
_CmmCallStatus_Object = MibTableColumn
cmmCallStatus = _CmmCallStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 11),
    _CmmCallStatus_Type()
)
cmmCallStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmCallStatus.setStatus("mandatory")


class _CmmCallOrigin_Type(Integer32):
    """Custom type cmmCallOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("answer", 1),
          ("originate", 2))
    )


_CmmCallOrigin_Type.__name__ = "Integer32"
_CmmCallOrigin_Object = MibTableColumn
cmmCallOrigin = _CmmCallOrigin_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 12),
    _CmmCallOrigin_Type()
)
cmmCallOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmCallOrigin.setStatus("mandatory")
_CmmRobbedBitDetected_Type = DisplayString
_CmmRobbedBitDetected_Object = MibTableColumn
cmmRobbedBitDetected = _CmmRobbedBitDetected_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 13),
    _CmmRobbedBitDetected_Type()
)
cmmRobbedBitDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmRobbedBitDetected.setStatus("mandatory")


class _CmmCorrectionType_Type(Integer32):
    """Custom type cmmCorrectionType based on Integer32"""
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
        *(("detection", 2),
          ("hanging-up", 4),
          ("lapm", 6),
          ("mnp", 3),
          ("mnp10", 7),
          ("no-ec", 1),
          ("speed-matching", 5))
    )


_CmmCorrectionType_Type.__name__ = "Integer32"
_CmmCorrectionType_Object = MibTableColumn
cmmCorrectionType = _CmmCorrectionType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 14),
    _CmmCorrectionType_Type()
)
cmmCorrectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmCorrectionType.setStatus("mandatory")


class _CmmCompressionType_Type(Integer32):
    """Custom type cmmCompressionType based on Integer32"""
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
        *(("mnp-class-5", 2),
          ("none", 1),
          ("v42bis", 5),
          ("v42bis-rx-only", 4),
          ("v42bis-tx-only", 3))
    )


_CmmCompressionType_Type.__name__ = "Integer32"
_CmmCompressionType_Object = MibTableColumn
cmmCompressionType = _CmmCompressionType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 15),
    _CmmCompressionType_Type()
)
cmmCompressionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmCompressionType.setStatus("mandatory")
_CmmRxRate_Type = Integer32
_CmmRxRate_Object = MibTableColumn
cmmRxRate = _CmmRxRate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 16),
    _CmmRxRate_Type()
)
cmmRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmRxRate.setStatus("mandatory")
_CmmTxRate_Type = Integer32
_CmmTxRate_Object = MibTableColumn
cmmTxRate = _CmmTxRate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 17),
    _CmmTxRate_Type()
)
cmmTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTxRate.setStatus("mandatory")


class _CmmEncoding_Type(Integer32):
    """Custom type cmmEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a-law", 2),
          ("u-law", 1))
    )


_CmmEncoding_Type.__name__ = "Integer32"
_CmmEncoding_Object = MibTableColumn
cmmEncoding = _CmmEncoding_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 18),
    _CmmEncoding_Type()
)
cmmEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmEncoding.setStatus("mandatory")


class _CmmFraming_Type(Integer32):
    """Custom type cmmFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hdlc-framing", 2),
          ("ppp-async", 3),
          ("pseudo-framing", 1))
    )


_CmmFraming_Type.__name__ = "Integer32"
_CmmFraming_Object = MibTableColumn
cmmFraming = _CmmFraming_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 19),
    _CmmFraming_Type()
)
cmmFraming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFraming.setStatus("mandatory")
_CmmInitialConnectRate_Type = Integer32
_CmmInitialConnectRate_Object = MibTableColumn
cmmInitialConnectRate = _CmmInitialConnectRate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 20),
    _CmmInitialConnectRate_Type()
)
cmmInitialConnectRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmInitialConnectRate.setStatus("mandatory")
_CmmMaxHostWindows_Type = Integer32
_CmmMaxHostWindows_Object = MibTableColumn
cmmMaxHostWindows = _CmmMaxHostWindows_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 21),
    _CmmMaxHostWindows_Type()
)
cmmMaxHostWindows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmMaxHostWindows.setStatus("mandatory")
_CmmMaxCmmWindows_Type = Integer32
_CmmMaxCmmWindows_Object = MibTableColumn
cmmMaxCmmWindows = _CmmMaxCmmWindows_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 22),
    _CmmMaxCmmWindows_Type()
)
cmmMaxCmmWindows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmMaxCmmWindows.setStatus("mandatory")
_CmmNumOutHostAcks_Type = Gauge32
_CmmNumOutHostAcks_Object = MibTableColumn
cmmNumOutHostAcks = _CmmNumOutHostAcks_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 23),
    _CmmNumOutHostAcks_Type()
)
cmmNumOutHostAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmNumOutHostAcks.setStatus("mandatory")
_CmmNumOutCmmAcks_Type = Gauge32
_CmmNumOutCmmAcks_Object = MibTableColumn
cmmNumOutCmmAcks = _CmmNumOutCmmAcks_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 24),
    _CmmNumOutCmmAcks_Type()
)
cmmNumOutCmmAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmNumOutCmmAcks.setStatus("mandatory")
_CmmToNetworkOctets_Type = Counter32
_CmmToNetworkOctets_Object = MibTableColumn
cmmToNetworkOctets = _CmmToNetworkOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 25),
    _CmmToNetworkOctets_Type()
)
cmmToNetworkOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmToNetworkOctets.setStatus("mandatory")
_CmmFromNetworkOctets_Type = Counter32
_CmmFromNetworkOctets_Object = MibTableColumn
cmmFromNetworkOctets = _CmmFromNetworkOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 26),
    _CmmFromNetworkOctets_Type()
)
cmmFromNetworkOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFromNetworkOctets.setStatus("mandatory")
_CmmToHostOctets_Type = Counter32
_CmmToHostOctets_Object = MibTableColumn
cmmToHostOctets = _CmmToHostOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 27),
    _CmmToHostOctets_Type()
)
cmmToHostOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmToHostOctets.setStatus("mandatory")
_CmmFromHostOctets_Type = Counter32
_CmmFromHostOctets_Object = MibTableColumn
cmmFromHostOctets = _CmmFromHostOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 28),
    _CmmFromHostOctets_Type()
)
cmmFromHostOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFromHostOctets.setStatus("mandatory")
_CmmToNetworkFrames_Type = Counter32
_CmmToNetworkFrames_Object = MibTableColumn
cmmToNetworkFrames = _CmmToNetworkFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 29),
    _CmmToNetworkFrames_Type()
)
cmmToNetworkFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmToNetworkFrames.setStatus("mandatory")
_CmmFromNetworkFrames_Type = Counter32
_CmmFromNetworkFrames_Object = MibTableColumn
cmmFromNetworkFrames = _CmmFromNetworkFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 30),
    _CmmFromNetworkFrames_Type()
)
cmmFromNetworkFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFromNetworkFrames.setStatus("mandatory")
_CmmOversizeFrames_Type = Counter32
_CmmOversizeFrames_Object = MibTableColumn
cmmOversizeFrames = _CmmOversizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 31),
    _CmmOversizeFrames_Type()
)
cmmOversizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmOversizeFrames.setStatus("mandatory")
_CmmOverrunErrors_Type = Counter32
_CmmOverrunErrors_Object = MibTableColumn
cmmOverrunErrors = _CmmOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 32),
    _CmmOverrunErrors_Type()
)
cmmOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmOverrunErrors.setStatus("mandatory")
_CmmCRCErrors_Type = Counter32
_CmmCRCErrors_Object = MibTableColumn
cmmCRCErrors = _CmmCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 33),
    _CmmCRCErrors_Type()
)
cmmCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmCRCErrors.setStatus("mandatory")
_CmmAbortedFrames_Type = Counter32
_CmmAbortedFrames_Object = MibTableColumn
cmmAbortedFrames = _CmmAbortedFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 34),
    _CmmAbortedFrames_Type()
)
cmmAbortedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmAbortedFrames.setStatus("mandatory")
_CmmRetrainEvents_Type = Counter32
_CmmRetrainEvents_Object = MibTableColumn
cmmRetrainEvents = _CmmRetrainEvents_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 35),
    _CmmRetrainEvents_Type()
)
cmmRetrainEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmRetrainEvents.setStatus("mandatory")
_CmmARAEvents_Type = Counter32
_CmmARAEvents_Object = MibTableColumn
cmmARAEvents = _CmmARAEvents_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 36),
    _CmmARAEvents_Type()
)
cmmARAEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmARAEvents.setStatus("mandatory")


class _CmmARAFlag_Type(Integer32):
    """Custom type cmmARAFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_CmmARAFlag_Type.__name__ = "Integer32"
_CmmARAFlag_Object = MibTableColumn
cmmARAFlag = _CmmARAFlag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 37),
    _CmmARAFlag_Type()
)
cmmARAFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmARAFlag.setStatus("mandatory")
_CmmCarrierLossEvents_Type = Counter32
_CmmCarrierLossEvents_Object = MibTableColumn
cmmCarrierLossEvents = _CmmCarrierLossEvents_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 38),
    _CmmCarrierLossEvents_Type()
)
cmmCarrierLossEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmCarrierLossEvents.setStatus("mandatory")


class _CmmCarrierLossFlag_Type(Integer32):
    """Custom type cmmCarrierLossFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_CmmCarrierLossFlag_Type.__name__ = "Integer32"
_CmmCarrierLossFlag_Object = MibTableColumn
cmmCarrierLossFlag = _CmmCarrierLossFlag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 39),
    _CmmCarrierLossFlag_Type()
)
cmmCarrierLossFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmCarrierLossFlag.setStatus("mandatory")
_CmmRcvSignalLevel_Type = Integer32
_CmmRcvSignalLevel_Object = MibTableColumn
cmmRcvSignalLevel = _CmmRcvSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 40),
    _CmmRcvSignalLevel_Type()
)
cmmRcvSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmRcvSignalLevel.setStatus("mandatory")
_CmmRcvSignalEQM_Type = Integer32
_CmmRcvSignalEQM_Object = MibTableColumn
cmmRcvSignalEQM = _CmmRcvSignalEQM_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 41),
    _CmmRcvSignalEQM_Type()
)
cmmRcvSignalEQM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmRcvSignalEQM.setStatus("mandatory")
_CmmTDMSlot_Type = Integer32
_CmmTDMSlot_Object = MibTableColumn
cmmTDMSlot = _CmmTDMSlot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 42),
    _CmmTDMSlot_Type()
)
cmmTDMSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTDMSlot.setStatus("mandatory")


class _CmmResetModemStats_Type(Integer32):
    """Custom type cmmResetModemStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_CmmResetModemStats_Type.__name__ = "Integer32"
_CmmResetModemStats_Object = MibTableColumn
cmmResetModemStats = _CmmResetModemStats_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 43),
    _CmmResetModemStats_Type()
)
cmmResetModemStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmResetModemStats.setStatus("mandatory")


class _CmmModemAdminStatus_Type(Integer32):
    """Custom type cmmModemAdminStatus based on Integer32"""
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
        *(("down", 1),
          ("faulty", 6),
          ("leave-service", 2),
          ("reset", 5),
          ("run-diagnostics", 4),
          ("up", 3))
    )


_CmmModemAdminStatus_Type.__name__ = "Integer32"
_CmmModemAdminStatus_Object = MibTableColumn
cmmModemAdminStatus = _CmmModemAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 44),
    _CmmModemAdminStatus_Type()
)
cmmModemAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmModemAdminStatus.setStatus("mandatory")


class _CmmModemOperStatus_Type(Integer32):
    """Custom type cmmModemOperStatus based on Integer32"""
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
        *(("active", 3),
          ("faulty", 7),
          ("idle", 2),
          ("initializing", 1),
          ("leaving-service", 4),
          ("out-of-service", 5),
          ("resetting", 8),
          ("testing", 6))
    )


_CmmModemOperStatus_Type.__name__ = "Integer32"
_CmmModemOperStatus_Object = MibTableColumn
cmmModemOperStatus = _CmmModemOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 3, 1, 45),
    _CmmModemOperStatus_Type()
)
cmmModemOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmModemOperStatus.setStatus("mandatory")
_CmmFreeFormAtCmdGroup_ObjectIdentity = ObjectIdentity
cmmFreeFormAtCmdGroup = _CmmFreeFormAtCmdGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 5)
)
_CmmATCommand_Type = OctetString
_CmmATCommand_Object = MibScalar
cmmATCommand = _CmmATCommand_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 5, 1),
    _CmmATCommand_Type()
)
cmmATCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmATCommand.setStatus("mandatory")
_CmmSelectedModem_Type = Integer32
_CmmSelectedModem_Object = MibScalar
cmmSelectedModem = _CmmSelectedModem_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 5, 2),
    _CmmSelectedModem_Type()
)
cmmSelectedModem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmSelectedModem.setStatus("mandatory")


class _CmmATCmdStatus_Type(Integer32):
    """Custom type cmmATCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-sending", 2),
          ("sending", 1))
    )


_CmmATCmdStatus_Type.__name__ = "Integer32"
_CmmATCmdStatus_Object = MibScalar
cmmATCmdStatus = _CmmATCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 5, 3),
    _CmmATCmdStatus_Type()
)
cmmATCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmATCmdStatus.setStatus("mandatory")


class _CmmATCmdResult_Type(DisplayString):
    """Custom type cmmATCmdResult based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CmmATCmdResult_Type.__name__ = "DisplayString"
_CmmATCmdResult_Object = MibScalar
cmmATCmdResult = _CmmATCmdResult_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18, 1, 5, 4),
    _CmmATCmdResult_Type()
)
cmmATCmdResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmATCmdResult.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CT-CMMPHYS-MIB",
    **{"cmmModemInfo": cmmModemInfo,
       "cmmBoardTable": cmmBoardTable,
       "cmmBoardEntry": cmmBoardEntry,
       "cmmBoardType": cmmBoardType,
       "cmmNumModules": cmmNumModules,
       "cmmModuleNumModems": cmmModuleNumModems,
       "cmmTFTPServer": cmmTFTPServer,
       "cmmUpgradePath": cmmUpgradePath,
       "cmmUpgradeFlag": cmmUpgradeFlag,
       "cmmCommitFlag": cmmCommitFlag,
       "cmmModemResetLimit": cmmModemResetLimit,
       "cmmModemResetTime": cmmModemResetTime,
       "cmmOutgoingInactivityTimeout": cmmOutgoingInactivityTimeout,
       "cmmIncomingInactivityTimeout": cmmIncomingInactivityTimeout,
       "cmmAsyncBaseOrigATCmdStr": cmmAsyncBaseOrigATCmdStr,
       "cmmAsyncBaseAnswerATCmdStr": cmmAsyncBaseAnswerATCmdStr,
       "cmmAsyncOrigStrModifier": cmmAsyncOrigStrModifier,
       "cmmAsyncAnswerStrModifier": cmmAsyncAnswerStrModifier,
       "cmmAsyncOperOrigATCmdStr": cmmAsyncOperOrigATCmdStr,
       "cmmAsyncOperAnswerATCmdStr": cmmAsyncOperAnswerATCmdStr,
       "cmmHdlcBaseOrigATCmdStr": cmmHdlcBaseOrigATCmdStr,
       "cmmHdlcBaseAnswerATCmdStr": cmmHdlcBaseAnswerATCmdStr,
       "cmmHdlcOrigStrModifier": cmmHdlcOrigStrModifier,
       "cmmHdlcAnswerStrModifier": cmmHdlcAnswerStrModifier,
       "cmmHdlcOperOrigATCmdStr": cmmHdlcOperOrigATCmdStr,
       "cmmHdlcOperAnswerATCmdStr": cmmHdlcOperAnswerATCmdStr,
       "cmmBoardAdminStatus": cmmBoardAdminStatus,
       "cmmBoardOperStatus": cmmBoardOperStatus,
       "cmmModuleTable": cmmModuleTable,
       "cmmModuleEntry": cmmModuleEntry,
       "cmmModuleID": cmmModuleID,
       "cmmDpramSize": cmmDpramSize,
       "cmmSdramSize": cmmSdramSize,
       "cmmCpuType": cmmCpuType,
       "cmmCpuSpeed": cmmCpuSpeed,
       "cmmCpuFwRev": cmmCpuFwRev,
       "cmmEpldId": cmmEpldId,
       "cmmEpldRev": cmmEpldRev,
       "cmmNumBadModems": cmmNumBadModems,
       "cmmModuleAdminStatus": cmmModuleAdminStatus,
       "cmmModuleOperStatus": cmmModuleOperStatus,
       "cmmModemTable": cmmModemTable,
       "cmmModemEntry": cmmModemEntry,
       "cmmBoardID": cmmBoardID,
       "cmmModemID": cmmModemID,
       "cmmIFNum": cmmIFNum,
       "cmmSessionNum": cmmSessionNum,
       "cmmDdpPartNum": cmmDdpPartNum,
       "cmmDdpRevLevel": cmmDdpRevLevel,
       "cmmDdpFwRev": cmmDdpFwRev,
       "cmmDDPInterrupts": cmmDDPInterrupts,
       "cmmRxFlowCtlEvts": cmmRxFlowCtlEvts,
       "cmmTxFlowCtlEvts": cmmTxFlowCtlEvts,
       "cmmCallStatus": cmmCallStatus,
       "cmmCallOrigin": cmmCallOrigin,
       "cmmRobbedBitDetected": cmmRobbedBitDetected,
       "cmmCorrectionType": cmmCorrectionType,
       "cmmCompressionType": cmmCompressionType,
       "cmmRxRate": cmmRxRate,
       "cmmTxRate": cmmTxRate,
       "cmmEncoding": cmmEncoding,
       "cmmFraming": cmmFraming,
       "cmmInitialConnectRate": cmmInitialConnectRate,
       "cmmMaxHostWindows": cmmMaxHostWindows,
       "cmmMaxCmmWindows": cmmMaxCmmWindows,
       "cmmNumOutHostAcks": cmmNumOutHostAcks,
       "cmmNumOutCmmAcks": cmmNumOutCmmAcks,
       "cmmToNetworkOctets": cmmToNetworkOctets,
       "cmmFromNetworkOctets": cmmFromNetworkOctets,
       "cmmToHostOctets": cmmToHostOctets,
       "cmmFromHostOctets": cmmFromHostOctets,
       "cmmToNetworkFrames": cmmToNetworkFrames,
       "cmmFromNetworkFrames": cmmFromNetworkFrames,
       "cmmOversizeFrames": cmmOversizeFrames,
       "cmmOverrunErrors": cmmOverrunErrors,
       "cmmCRCErrors": cmmCRCErrors,
       "cmmAbortedFrames": cmmAbortedFrames,
       "cmmRetrainEvents": cmmRetrainEvents,
       "cmmARAEvents": cmmARAEvents,
       "cmmARAFlag": cmmARAFlag,
       "cmmCarrierLossEvents": cmmCarrierLossEvents,
       "cmmCarrierLossFlag": cmmCarrierLossFlag,
       "cmmRcvSignalLevel": cmmRcvSignalLevel,
       "cmmRcvSignalEQM": cmmRcvSignalEQM,
       "cmmTDMSlot": cmmTDMSlot,
       "cmmResetModemStats": cmmResetModemStats,
       "cmmModemAdminStatus": cmmModemAdminStatus,
       "cmmModemOperStatus": cmmModemOperStatus,
       "cmmFreeFormAtCmdGroup": cmmFreeFormAtCmdGroup,
       "cmmATCommand": cmmATCommand,
       "cmmSelectedModem": cmmSelectedModem,
       "cmmATCmdStatus": cmmATCmdStatus,
       "cmmATCmdResult": cmmATCmdResult}
)
