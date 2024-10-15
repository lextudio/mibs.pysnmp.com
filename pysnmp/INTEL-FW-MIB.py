# SNMP MIB module (INTEL-FW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-FW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:43 2024
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

(mib2ext,) = mibBuilder.importSymbols(
    "INTEL-GEN-MIB",
    "mib2ext")

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

_Fw_ObjectIdentity = ObjectIdentity
fw = _Fw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 9)
)
_FwInfo_ObjectIdentity = ObjectIdentity
fwInfo = _FwInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1)
)
_FwModuleTable_Object = MibTable
fwModuleTable = _FwModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1)
)
if mibBuilder.loadTexts:
    fwModuleTable.setStatus("mandatory")
_FwModuleEntry_Object = MibTableRow
fwModuleEntry = _FwModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1)
)
fwModuleEntry.setIndexNames(
    (0, "INTEL-FW-MIB", "fwModuleChassisIndex"),
    (0, "INTEL-FW-MIB", "fwModuleModuleIndex"),
    (0, "INTEL-FW-MIB", "fwModuleSWSectionIndex"),
    (0, "INTEL-FW-MIB", "fwModuleSWNumberIndex"),
)
if mibBuilder.loadTexts:
    fwModuleEntry.setStatus("mandatory")
_FwModuleChassisIndex_Type = Integer32
_FwModuleChassisIndex_Object = MibTableColumn
fwModuleChassisIndex = _FwModuleChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 1),
    _FwModuleChassisIndex_Type()
)
fwModuleChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwModuleChassisIndex.setStatus("mandatory")
_FwModuleModuleIndex_Type = Integer32
_FwModuleModuleIndex_Object = MibTableColumn
fwModuleModuleIndex = _FwModuleModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 2),
    _FwModuleModuleIndex_Type()
)
fwModuleModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwModuleModuleIndex.setStatus("mandatory")


class _FwModuleSWSectionIndex_Type(Integer32):
    """Custom type fwModuleSWSectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backUpSW", 2),
          ("runningSW", 1),
          ("upgradeSW", 3))
    )


_FwModuleSWSectionIndex_Type.__name__ = "Integer32"
_FwModuleSWSectionIndex_Object = MibTableColumn
fwModuleSWSectionIndex = _FwModuleSWSectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 3),
    _FwModuleSWSectionIndex_Type()
)
fwModuleSWSectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwModuleSWSectionIndex.setStatus("mandatory")
_FwModuleSWNumberIndex_Type = Integer32
_FwModuleSWNumberIndex_Object = MibTableColumn
fwModuleSWNumberIndex = _FwModuleSWNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 4),
    _FwModuleSWNumberIndex_Type()
)
fwModuleSWNumberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwModuleSWNumberIndex.setStatus("mandatory")
_FwModuleDeletePlugIn_Type = Integer32
_FwModuleDeletePlugIn_Object = MibTableColumn
fwModuleDeletePlugIn = _FwModuleDeletePlugIn_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 5),
    _FwModuleDeletePlugIn_Type()
)
fwModuleDeletePlugIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwModuleDeletePlugIn.setStatus("mandatory")
_FwModuleDeleteBackup_Type = Integer32
_FwModuleDeleteBackup_Object = MibTableColumn
fwModuleDeleteBackup = _FwModuleDeleteBackup_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 6),
    _FwModuleDeleteBackup_Type()
)
fwModuleDeleteBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwModuleDeleteBackup.setStatus("mandatory")


class _FwModuleFileName_Type(DisplayString):
    """Custom type fwModuleFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_FwModuleFileName_Type.__name__ = "DisplayString"
_FwModuleFileName_Object = MibTableColumn
fwModuleFileName = _FwModuleFileName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 7),
    _FwModuleFileName_Type()
)
fwModuleFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwModuleFileName.setStatus("mandatory")


class _FwModuleDescription_Type(DisplayString):
    """Custom type fwModuleDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_FwModuleDescription_Type.__name__ = "DisplayString"
_FwModuleDescription_Object = MibTableColumn
fwModuleDescription = _FwModuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 8),
    _FwModuleDescription_Type()
)
fwModuleDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwModuleDescription.setStatus("mandatory")
_FwModuleLoadTime_Type = Integer32
_FwModuleLoadTime_Object = MibTableColumn
fwModuleLoadTime = _FwModuleLoadTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 9),
    _FwModuleLoadTime_Type()
)
fwModuleLoadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwModuleLoadTime.setStatus("mandatory")
_FwModuleIpAddress_Type = IpAddress
_FwModuleIpAddress_Object = MibTableColumn
fwModuleIpAddress = _FwModuleIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 10),
    _FwModuleIpAddress_Type()
)
fwModuleIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwModuleIpAddress.setStatus("mandatory")
_FwModuleMajorVersion_Type = Integer32
_FwModuleMajorVersion_Object = MibTableColumn
fwModuleMajorVersion = _FwModuleMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 11),
    _FwModuleMajorVersion_Type()
)
fwModuleMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwModuleMajorVersion.setStatus("mandatory")
_FwModuleMinorVersion_Type = Integer32
_FwModuleMinorVersion_Object = MibTableColumn
fwModuleMinorVersion = _FwModuleMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 12),
    _FwModuleMinorVersion_Type()
)
fwModuleMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwModuleMinorVersion.setStatus("mandatory")


class _FwModuleVersionTxt_Type(DisplayString):
    """Custom type fwModuleVersionTxt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_FwModuleVersionTxt_Type.__name__ = "DisplayString"
_FwModuleVersionTxt_Object = MibTableColumn
fwModuleVersionTxt = _FwModuleVersionTxt_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 13),
    _FwModuleVersionTxt_Type()
)
fwModuleVersionTxt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwModuleVersionTxt.setStatus("mandatory")


class _FwModuleSwStatus_Type(Integer32):
    """Custom type fwModuleSwStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("approved", 1),
          ("experimental", 2),
          ("invalid", 3))
    )


_FwModuleSwStatus_Type.__name__ = "Integer32"
_FwModuleSwStatus_Object = MibTableColumn
fwModuleSwStatus = _FwModuleSwStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 14),
    _FwModuleSwStatus_Type()
)
fwModuleSwStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwModuleSwStatus.setStatus("mandatory")


class _FwModuleSwType_Type(Integer32):
    """Custom type fwModuleSwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("firmware", 1),
          ("plugin", 2))
    )


_FwModuleSwType_Type.__name__ = "Integer32"
_FwModuleSwType_Object = MibTableColumn
fwModuleSwType = _FwModuleSwType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 15),
    _FwModuleSwType_Type()
)
fwModuleSwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwModuleSwType.setStatus("mandatory")
_FwModuleFileID_Type = Integer32
_FwModuleFileID_Object = MibTableColumn
fwModuleFileID = _FwModuleFileID_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 1, 1, 16),
    _FwModuleFileID_Type()
)
fwModuleFileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwModuleFileID.setStatus("mandatory")
_FwPatternTable_Object = MibTable
fwPatternTable = _FwPatternTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 2)
)
if mibBuilder.loadTexts:
    fwPatternTable.setStatus("mandatory")
_FwPatternEntry_Object = MibTableRow
fwPatternEntry = _FwPatternEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 2, 1)
)
fwPatternEntry.setIndexNames(
    (0, "INTEL-FW-MIB", "fwPatternChassisIndex"),
    (0, "INTEL-FW-MIB", "fwPatternModuleIndex"),
    (0, "INTEL-FW-MIB", "fwPatternFileIndex"),
)
if mibBuilder.loadTexts:
    fwPatternEntry.setStatus("mandatory")
_FwPatternChassisIndex_Type = Integer32
_FwPatternChassisIndex_Object = MibTableColumn
fwPatternChassisIndex = _FwPatternChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 2, 1, 1),
    _FwPatternChassisIndex_Type()
)
fwPatternChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwPatternChassisIndex.setStatus("mandatory")
_FwPatternModuleIndex_Type = Integer32
_FwPatternModuleIndex_Object = MibTableColumn
fwPatternModuleIndex = _FwPatternModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 2, 1, 2),
    _FwPatternModuleIndex_Type()
)
fwPatternModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwPatternModuleIndex.setStatus("mandatory")
_FwPatternFileIndex_Type = Integer32
_FwPatternFileIndex_Object = MibTableColumn
fwPatternFileIndex = _FwPatternFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 2, 1, 3),
    _FwPatternFileIndex_Type()
)
fwPatternFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwPatternFileIndex.setStatus("mandatory")


class _FwPatternFileFilter_Type(DisplayString):
    """Custom type fwPatternFileFilter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_FwPatternFileFilter_Type.__name__ = "DisplayString"
_FwPatternFileFilter_Object = MibTableColumn
fwPatternFileFilter = _FwPatternFileFilter_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 2, 1, 4),
    _FwPatternFileFilter_Type()
)
fwPatternFileFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwPatternFileFilter.setStatus("mandatory")


class _FwPatternFileDesc_Type(DisplayString):
    """Custom type fwPatternFileDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_FwPatternFileDesc_Type.__name__ = "DisplayString"
_FwPatternFileDesc_Object = MibTableColumn
fwPatternFileDesc = _FwPatternFileDesc_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 2, 1, 5),
    _FwPatternFileDesc_Type()
)
fwPatternFileDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwPatternFileDesc.setStatus("mandatory")


class _FwPatternFileShortDesc_Type(DisplayString):
    """Custom type fwPatternFileShortDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_FwPatternFileShortDesc_Type.__name__ = "DisplayString"
_FwPatternFileShortDesc_Object = MibTableColumn
fwPatternFileShortDesc = _FwPatternFileShortDesc_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 2, 1, 6),
    _FwPatternFileShortDesc_Type()
)
fwPatternFileShortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwPatternFileShortDesc.setStatus("mandatory")
_FwPatternDefaultEnable_Type = Integer32
_FwPatternDefaultEnable_Object = MibTableColumn
fwPatternDefaultEnable = _FwPatternDefaultEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 2, 1, 7),
    _FwPatternDefaultEnable_Type()
)
fwPatternDefaultEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwPatternDefaultEnable.setStatus("mandatory")
_FwPatternFileID_Type = Integer32
_FwPatternFileID_Object = MibTableColumn
fwPatternFileID = _FwPatternFileID_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 2, 1, 8),
    _FwPatternFileID_Type()
)
fwPatternFileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwPatternFileID.setStatus("mandatory")
_FwInfoNoOfEntries_Type = Integer32
_FwInfoNoOfEntries_Object = MibScalar
fwInfoNoOfEntries = _FwInfoNoOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 3),
    _FwInfoNoOfEntries_Type()
)
fwInfoNoOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwInfoNoOfEntries.setStatus("mandatory")
_FwInfoLastUpdateTime_Type = TimeTicks
_FwInfoLastUpdateTime_Object = MibScalar
fwInfoLastUpdateTime = _FwInfoLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 4),
    _FwInfoLastUpdateTime_Type()
)
fwInfoLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwInfoLastUpdateTime.setStatus("mandatory")
_FwInfoGoUpgrade_Type = Integer32
_FwInfoGoUpgrade_Object = MibScalar
fwInfoGoUpgrade = _FwInfoGoUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 5),
    _FwInfoGoUpgrade_Type()
)
fwInfoGoUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwInfoGoUpgrade.setStatus("mandatory")
_FwInfoLastTftpToStatusMsgTimeout_Type = Integer32
_FwInfoLastTftpToStatusMsgTimeout_Object = MibScalar
fwInfoLastTftpToStatusMsgTimeout = _FwInfoLastTftpToStatusMsgTimeout_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 6),
    _FwInfoLastTftpToStatusMsgTimeout_Type()
)
fwInfoLastTftpToStatusMsgTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwInfoLastTftpToStatusMsgTimeout.setStatus("mandatory")
_FwInfoResetToRebootTimeout_Type = Integer32
_FwInfoResetToRebootTimeout_Object = MibScalar
fwInfoResetToRebootTimeout = _FwInfoResetToRebootTimeout_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 9, 1, 7),
    _FwInfoResetToRebootTimeout_Type()
)
fwInfoResetToRebootTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwInfoResetToRebootTimeout.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-FW-MIB",
    **{"fw": fw,
       "fwInfo": fwInfo,
       "fwModuleTable": fwModuleTable,
       "fwModuleEntry": fwModuleEntry,
       "fwModuleChassisIndex": fwModuleChassisIndex,
       "fwModuleModuleIndex": fwModuleModuleIndex,
       "fwModuleSWSectionIndex": fwModuleSWSectionIndex,
       "fwModuleSWNumberIndex": fwModuleSWNumberIndex,
       "fwModuleDeletePlugIn": fwModuleDeletePlugIn,
       "fwModuleDeleteBackup": fwModuleDeleteBackup,
       "fwModuleFileName": fwModuleFileName,
       "fwModuleDescription": fwModuleDescription,
       "fwModuleLoadTime": fwModuleLoadTime,
       "fwModuleIpAddress": fwModuleIpAddress,
       "fwModuleMajorVersion": fwModuleMajorVersion,
       "fwModuleMinorVersion": fwModuleMinorVersion,
       "fwModuleVersionTxt": fwModuleVersionTxt,
       "fwModuleSwStatus": fwModuleSwStatus,
       "fwModuleSwType": fwModuleSwType,
       "fwModuleFileID": fwModuleFileID,
       "fwPatternTable": fwPatternTable,
       "fwPatternEntry": fwPatternEntry,
       "fwPatternChassisIndex": fwPatternChassisIndex,
       "fwPatternModuleIndex": fwPatternModuleIndex,
       "fwPatternFileIndex": fwPatternFileIndex,
       "fwPatternFileFilter": fwPatternFileFilter,
       "fwPatternFileDesc": fwPatternFileDesc,
       "fwPatternFileShortDesc": fwPatternFileShortDesc,
       "fwPatternDefaultEnable": fwPatternDefaultEnable,
       "fwPatternFileID": fwPatternFileID,
       "fwInfoNoOfEntries": fwInfoNoOfEntries,
       "fwInfoLastUpdateTime": fwInfoLastUpdateTime,
       "fwInfoGoUpgrade": fwInfoGoUpgrade,
       "fwInfoLastTftpToStatusMsgTimeout": fwInfoLastTftpToStatusMsgTimeout,
       "fwInfoResetToRebootTimeout": fwInfoResetToRebootTimeout}
)
