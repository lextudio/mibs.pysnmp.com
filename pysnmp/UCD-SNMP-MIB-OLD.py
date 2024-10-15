# SNMP MIB module (UCD-SNMP-MIB-OLD) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/UCD-SNMP-MIB-OLD
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:23 2024
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

(ucdavis,) = mibBuilder.importSymbols(
    "UCD-SNMP-MIB",
    "ucdavis")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Processes_Object = MibTable
processes = _Processes_Object(
    (1, 3, 6, 1, 4, 1, 2021, 1)
)
if mibBuilder.loadTexts:
    processes.setStatus("mandatory")
_ProcessIndex_Type = Integer32
_ProcessIndex_Object = MibTableColumn
processIndex = _ProcessIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 1, 1),
    _ProcessIndex_Type()
)
processIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processIndex.setStatus("mandatory")


class _ProcessNames_Type(DisplayString):
    """Custom type processNames based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ProcessNames_Type.__name__ = "DisplayString"
_ProcessNames_Object = MibTableColumn
processNames = _ProcessNames_Object(
    (1, 3, 6, 1, 4, 1, 2021, 1, 2),
    _ProcessNames_Type()
)
processNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processNames.setStatus("mandatory")
_ProcessMin_Type = Integer32
_ProcessMin_Object = MibTableColumn
processMin = _ProcessMin_Object(
    (1, 3, 6, 1, 4, 1, 2021, 1, 3),
    _ProcessMin_Type()
)
processMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processMin.setStatus("mandatory")
_ProcessMax_Type = Integer32
_ProcessMax_Object = MibTableColumn
processMax = _ProcessMax_Object(
    (1, 3, 6, 1, 4, 1, 2021, 1, 4),
    _ProcessMax_Type()
)
processMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processMax.setStatus("mandatory")
_ProcessCount_Type = Integer32
_ProcessCount_Object = MibTableColumn
processCount = _ProcessCount_Object(
    (1, 3, 6, 1, 4, 1, 2021, 1, 5),
    _ProcessCount_Type()
)
processCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processCount.setStatus("mandatory")
_ProcessErrorFlag_Type = Integer32
_ProcessErrorFlag_Object = MibTableColumn
processErrorFlag = _ProcessErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 2021, 1, 100),
    _ProcessErrorFlag_Type()
)
processErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processErrorFlag.setStatus("mandatory")


class _ProcessErrMessage_Type(DisplayString):
    """Custom type processErrMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ProcessErrMessage_Type.__name__ = "DisplayString"
_ProcessErrMessage_Object = MibTableColumn
processErrMessage = _ProcessErrMessage_Object(
    (1, 3, 6, 1, 4, 1, 2021, 1, 101),
    _ProcessErrMessage_Type()
)
processErrMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processErrMessage.setStatus("mandatory")
_ProcessErrFix_Type = Integer32
_ProcessErrFix_Object = MibTableColumn
processErrFix = _ProcessErrFix_Object(
    (1, 3, 6, 1, 4, 1, 2021, 1, 102),
    _ProcessErrFix_Type()
)
processErrFix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    processErrFix.setStatus("mandatory")
_Extensible_Object = MibTable
extensible = _Extensible_Object(
    (1, 3, 6, 1, 4, 1, 2021, 3)
)
if mibBuilder.loadTexts:
    extensible.setStatus("mandatory")
_ExtensibleIndex_Type = Integer32
_ExtensibleIndex_Object = MibTableColumn
extensibleIndex = _ExtensibleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 3, 1),
    _ExtensibleIndex_Type()
)
extensibleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extensibleIndex.setStatus("mandatory")


class _ExtensibleNames_Type(DisplayString):
    """Custom type extensibleNames based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtensibleNames_Type.__name__ = "DisplayString"
_ExtensibleNames_Object = MibTableColumn
extensibleNames = _ExtensibleNames_Object(
    (1, 3, 6, 1, 4, 1, 2021, 3, 2),
    _ExtensibleNames_Type()
)
extensibleNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extensibleNames.setStatus("mandatory")


class _ExtensibleCommand_Type(DisplayString):
    """Custom type extensibleCommand based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtensibleCommand_Type.__name__ = "DisplayString"
_ExtensibleCommand_Object = MibTableColumn
extensibleCommand = _ExtensibleCommand_Object(
    (1, 3, 6, 1, 4, 1, 2021, 3, 3),
    _ExtensibleCommand_Type()
)
extensibleCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extensibleCommand.setStatus("mandatory")
_ExtensibleResult_Type = Integer32
_ExtensibleResult_Object = MibTableColumn
extensibleResult = _ExtensibleResult_Object(
    (1, 3, 6, 1, 4, 1, 2021, 3, 100),
    _ExtensibleResult_Type()
)
extensibleResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extensibleResult.setStatus("mandatory")


class _ExtensibleOutput_Type(DisplayString):
    """Custom type extensibleOutput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtensibleOutput_Type.__name__ = "DisplayString"
_ExtensibleOutput_Object = MibTableColumn
extensibleOutput = _ExtensibleOutput_Object(
    (1, 3, 6, 1, 4, 1, 2021, 3, 101),
    _ExtensibleOutput_Type()
)
extensibleOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extensibleOutput.setStatus("mandatory")
_ExtensibleErrFix_Type = Integer32
_ExtensibleErrFix_Object = MibTableColumn
extensibleErrFix = _ExtensibleErrFix_Object(
    (1, 3, 6, 1, 4, 1, 2021, 3, 102),
    _ExtensibleErrFix_Type()
)
extensibleErrFix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extensibleErrFix.setStatus("mandatory")
_Disk_Object = MibTable
disk = _Disk_Object(
    (1, 3, 6, 1, 4, 1, 2021, 6)
)
if mibBuilder.loadTexts:
    disk.setStatus("mandatory")
_DiskIndex_Type = Integer32
_DiskIndex_Object = MibTableColumn
diskIndex = _DiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 6, 1),
    _DiskIndex_Type()
)
diskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskIndex.setStatus("mandatory")
_DiskPath_Type = DisplayString
_DiskPath_Object = MibTableColumn
diskPath = _DiskPath_Object(
    (1, 3, 6, 1, 4, 1, 2021, 6, 2),
    _DiskPath_Type()
)
diskPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPath.setStatus("mandatory")
_DiskDevice_Type = DisplayString
_DiskDevice_Object = MibTableColumn
diskDevice = _DiskDevice_Object(
    (1, 3, 6, 1, 4, 1, 2021, 6, 3),
    _DiskDevice_Type()
)
diskDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskDevice.setStatus("mandatory")
_DiskMinimum_Type = Integer32
_DiskMinimum_Object = MibTableColumn
diskMinimum = _DiskMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2021, 6, 4),
    _DiskMinimum_Type()
)
diskMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskMinimum.setStatus("mandatory")
_DiskMinPercent_Type = Integer32
_DiskMinPercent_Object = MibTableColumn
diskMinPercent = _DiskMinPercent_Object(
    (1, 3, 6, 1, 4, 1, 2021, 6, 5),
    _DiskMinPercent_Type()
)
diskMinPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskMinPercent.setStatus("mandatory")
_DiskTotal_Type = Integer32
_DiskTotal_Object = MibTableColumn
diskTotal = _DiskTotal_Object(
    (1, 3, 6, 1, 4, 1, 2021, 6, 6),
    _DiskTotal_Type()
)
diskTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTotal.setStatus("mandatory")
_DiskAvail_Type = Integer32
_DiskAvail_Object = MibTableColumn
diskAvail = _DiskAvail_Object(
    (1, 3, 6, 1, 4, 1, 2021, 6, 7),
    _DiskAvail_Type()
)
diskAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskAvail.setStatus("mandatory")
_DiskUsed_Type = Integer32
_DiskUsed_Object = MibTableColumn
diskUsed = _DiskUsed_Object(
    (1, 3, 6, 1, 4, 1, 2021, 6, 8),
    _DiskUsed_Type()
)
diskUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskUsed.setStatus("mandatory")
_DiskPercent_Type = Integer32
_DiskPercent_Object = MibTableColumn
diskPercent = _DiskPercent_Object(
    (1, 3, 6, 1, 4, 1, 2021, 6, 9),
    _DiskPercent_Type()
)
diskPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPercent.setStatus("mandatory")
_DiskErrorFlag_Type = Integer32
_DiskErrorFlag_Object = MibTableColumn
diskErrorFlag = _DiskErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 2021, 6, 100),
    _DiskErrorFlag_Type()
)
diskErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskErrorFlag.setStatus("mandatory")
_DiskErrorMsg_Type = DisplayString
_DiskErrorMsg_Object = MibTableColumn
diskErrorMsg = _DiskErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 2021, 6, 101),
    _DiskErrorMsg_Type()
)
diskErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskErrorMsg.setStatus("mandatory")
_Loadaves_Object = MibTable
loadaves = _Loadaves_Object(
    (1, 3, 6, 1, 4, 1, 2021, 7)
)
if mibBuilder.loadTexts:
    loadaves.setStatus("mandatory")
_LoadaveIndex_Type = Integer32
_LoadaveIndex_Object = MibTableColumn
loadaveIndex = _LoadaveIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 7, 1),
    _LoadaveIndex_Type()
)
loadaveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadaveIndex.setStatus("mandatory")


class _LoadaveNames_Type(DisplayString):
    """Custom type loadaveNames based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LoadaveNames_Type.__name__ = "DisplayString"
_LoadaveNames_Object = MibTableColumn
loadaveNames = _LoadaveNames_Object(
    (1, 3, 6, 1, 4, 1, 2021, 7, 2),
    _LoadaveNames_Type()
)
loadaveNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadaveNames.setStatus("mandatory")
_LoadaveLoad_Type = DisplayString
_LoadaveLoad_Object = MibTableColumn
loadaveLoad = _LoadaveLoad_Object(
    (1, 3, 6, 1, 4, 1, 2021, 7, 3),
    _LoadaveLoad_Type()
)
loadaveLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadaveLoad.setStatus("mandatory")
_LoadaveConfig_Type = DisplayString
_LoadaveConfig_Object = MibTableColumn
loadaveConfig = _LoadaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 2021, 7, 4),
    _LoadaveConfig_Type()
)
loadaveConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadaveConfig.setStatus("mandatory")
_LoadaveErrorFlag_Type = Integer32
_LoadaveErrorFlag_Object = MibTableColumn
loadaveErrorFlag = _LoadaveErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 2021, 7, 100),
    _LoadaveErrorFlag_Type()
)
loadaveErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadaveErrorFlag.setStatus("mandatory")


class _LoadaveErrMessage_Type(DisplayString):
    """Custom type loadaveErrMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LoadaveErrMessage_Type.__name__ = "DisplayString"
_LoadaveErrMessage_Object = MibTableColumn
loadaveErrMessage = _LoadaveErrMessage_Object(
    (1, 3, 6, 1, 4, 1, 2021, 7, 101),
    _LoadaveErrMessage_Type()
)
loadaveErrMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadaveErrMessage.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UCD-SNMP-MIB-OLD",
    **{"processes": processes,
       "processIndex": processIndex,
       "processNames": processNames,
       "processMin": processMin,
       "processMax": processMax,
       "processCount": processCount,
       "processErrorFlag": processErrorFlag,
       "processErrMessage": processErrMessage,
       "processErrFix": processErrFix,
       "extensible": extensible,
       "extensibleIndex": extensibleIndex,
       "extensibleNames": extensibleNames,
       "extensibleCommand": extensibleCommand,
       "extensibleResult": extensibleResult,
       "extensibleOutput": extensibleOutput,
       "extensibleErrFix": extensibleErrFix,
       "disk": disk,
       "diskIndex": diskIndex,
       "diskPath": diskPath,
       "diskDevice": diskDevice,
       "diskMinimum": diskMinimum,
       "diskMinPercent": diskMinPercent,
       "diskTotal": diskTotal,
       "diskAvail": diskAvail,
       "diskUsed": diskUsed,
       "diskPercent": diskPercent,
       "diskErrorFlag": diskErrorFlag,
       "diskErrorMsg": diskErrorMsg,
       "loadaves": loadaves,
       "loadaveIndex": loadaveIndex,
       "loadaveNames": loadaveNames,
       "loadaveLoad": loadaveLoad,
       "loadaveConfig": loadaveConfig,
       "loadaveErrorFlag": loadaveErrorFlag,
       "loadaveErrMessage": loadaveErrMessage}
)
