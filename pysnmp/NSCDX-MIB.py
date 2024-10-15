# SNMP MIB module (NSCDX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NSCDX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:28 2024
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

(nscDx,) = mibBuilder.importSymbols(
    "NSC-MIB",
    "nscDx")

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

_NscDxConfig_ObjectIdentity = ObjectIdentity
nscDxConfig = _NscDxConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 1)
)
_NscDxConfigSecondsToReset_Type = Integer32
_NscDxConfigSecondsToReset_Object = MibScalar
nscDxConfigSecondsToReset = _NscDxConfigSecondsToReset_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 1, 1),
    _NscDxConfigSecondsToReset_Type()
)
nscDxConfigSecondsToReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscDxConfigSecondsToReset.setStatus("mandatory")


class _NscDxConfigFirmwareRevTab_Type(DisplayString):
    """Custom type nscDxConfigFirmwareRevTab based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 7),
    )


_NscDxConfigFirmwareRevTab_Type.__name__ = "DisplayString"
_NscDxConfigFirmwareRevTab_Object = MibScalar
nscDxConfigFirmwareRevTab = _NscDxConfigFirmwareRevTab_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 1, 2),
    _NscDxConfigFirmwareRevTab_Type()
)
nscDxConfigFirmwareRevTab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxConfigFirmwareRevTab.setStatus("mandatory")
_NscDxConfigBufferMemorySize_Type = Integer32
_NscDxConfigBufferMemorySize_Object = MibScalar
nscDxConfigBufferMemorySize = _NscDxConfigBufferMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 1, 3),
    _NscDxConfigBufferMemorySize_Type()
)
nscDxConfigBufferMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxConfigBufferMemorySize.setStatus("mandatory")
_NscDxConfigSecondsSinceMc_Type = Integer32
_NscDxConfigSecondsSinceMc_Object = MibScalar
nscDxConfigSecondsSinceMc = _NscDxConfigSecondsSinceMc_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 1, 4),
    _NscDxConfigSecondsSinceMc_Type()
)
nscDxConfigSecondsSinceMc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxConfigSecondsSinceMc.setStatus("mandatory")


class _NscDxConfigProcessorMask_Type(DisplayString):
    """Custom type nscDxConfigProcessorMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_NscDxConfigProcessorMask_Type.__name__ = "DisplayString"
_NscDxConfigProcessorMask_Object = MibScalar
nscDxConfigProcessorMask = _NscDxConfigProcessorMask_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 1, 5),
    _NscDxConfigProcessorMask_Type()
)
nscDxConfigProcessorMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxConfigProcessorMask.setStatus("mandatory")


class _NscDxConfigControlAddr_Type(OctetString):
    """Custom type nscDxConfigControlAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_NscDxConfigControlAddr_Type.__name__ = "OctetString"
_NscDxConfigControlAddr_Object = MibScalar
nscDxConfigControlAddr = _NscDxConfigControlAddr_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 1, 6),
    _NscDxConfigControlAddr_Type()
)
nscDxConfigControlAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxConfigControlAddr.setStatus("mandatory")
_NscDxConfigLargePageSize_Type = Integer32
_NscDxConfigLargePageSize_Object = MibScalar
nscDxConfigLargePageSize = _NscDxConfigLargePageSize_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 1, 7),
    _NscDxConfigLargePageSize_Type()
)
nscDxConfigLargePageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxConfigLargePageSize.setStatus("mandatory")
_NscDxConfigBoardInfoTable_Object = MibTable
nscDxConfigBoardInfoTable = _NscDxConfigBoardInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 1, 8)
)
if mibBuilder.loadTexts:
    nscDxConfigBoardInfoTable.setStatus("mandatory")
_NscDxConfigBoardInfoEntry_Object = MibTableRow
nscDxConfigBoardInfoEntry = _NscDxConfigBoardInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 1, 8, 1)
)
nscDxConfigBoardInfoEntry.setIndexNames(
    (0, "NSCDX-MIB", "nscDxConfigBoardInfoEntSlotNum"),
)
if mibBuilder.loadTexts:
    nscDxConfigBoardInfoEntry.setStatus("mandatory")
_NscDxConfigBoardInfoEntSlotNum_Type = Integer32
_NscDxConfigBoardInfoEntSlotNum_Object = MibTableColumn
nscDxConfigBoardInfoEntSlotNum = _NscDxConfigBoardInfoEntSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 1, 8, 1, 1),
    _NscDxConfigBoardInfoEntSlotNum_Type()
)
nscDxConfigBoardInfoEntSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxConfigBoardInfoEntSlotNum.setStatus("mandatory")


class _NscDxConfigBoardInfoEntBoardPart_Type(DisplayString):
    """Custom type nscDxConfigBoardInfoEntBoardPart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )


_NscDxConfigBoardInfoEntBoardPart_Type.__name__ = "DisplayString"
_NscDxConfigBoardInfoEntBoardPart_Object = MibTableColumn
nscDxConfigBoardInfoEntBoardPart = _NscDxConfigBoardInfoEntBoardPart_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 1, 8, 1, 2),
    _NscDxConfigBoardInfoEntBoardPart_Type()
)
nscDxConfigBoardInfoEntBoardPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxConfigBoardInfoEntBoardPart.setStatus("mandatory")


class _NscDxConfigTime_Type(DisplayString):
    """Custom type nscDxConfigTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_NscDxConfigTime_Type.__name__ = "DisplayString"
_NscDxConfigTime_Object = MibScalar
nscDxConfigTime = _NscDxConfigTime_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 1, 9),
    _NscDxConfigTime_Type()
)
nscDxConfigTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxConfigTime.setStatus("mandatory")


class _NscDxConfigDate_Type(DisplayString):
    """Custom type nscDxConfigDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_NscDxConfigDate_Type.__name__ = "DisplayString"
_NscDxConfigDate_Object = MibScalar
nscDxConfigDate = _NscDxConfigDate_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 1, 10),
    _NscDxConfigDate_Type()
)
nscDxConfigDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxConfigDate.setStatus("mandatory")


class _NscDxConfigStartType_Type(Integer32):
    """Custom type nscDxConfigStartType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerup", 2),
          ("reset", 1))
    )


_NscDxConfigStartType_Type.__name__ = "Integer32"
_NscDxConfigStartType_Object = MibScalar
nscDxConfigStartType = _NscDxConfigStartType_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 1, 11),
    _NscDxConfigStartType_Type()
)
nscDxConfigStartType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxConfigStartType.setStatus("mandatory")
_NscDxConfigMemoryDivision_Type = Integer32
_NscDxConfigMemoryDivision_Object = MibScalar
nscDxConfigMemoryDivision = _NscDxConfigMemoryDivision_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 1, 12),
    _NscDxConfigMemoryDivision_Type()
)
nscDxConfigMemoryDivision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxConfigMemoryDivision.setStatus("mandatory")
_NscDxProcTable_Object = MibTable
nscDxProcTable = _NscDxProcTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    nscDxProcTable.setStatus("mandatory")
_NscDxProcTableEntry_Object = MibTableRow
nscDxProcTableEntry = _NscDxProcTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 2, 1)
)
nscDxProcTableEntry.setIndexNames(
    (0, "NSCDX-MIB", "nscDxProcTableEntKeyId"),
)
if mibBuilder.loadTexts:
    nscDxProcTableEntry.setStatus("mandatory")


class _NscDxProcTableEntKeyId_Type(Integer32):
    """Custom type nscDxProcTableEntKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NscDxProcTableEntKeyId_Type.__name__ = "Integer32"
_NscDxProcTableEntKeyId_Object = MibTableColumn
nscDxProcTableEntKeyId = _NscDxProcTableEntKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 2, 1, 1),
    _NscDxProcTableEntKeyId_Type()
)
nscDxProcTableEntKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxProcTableEntKeyId.setStatus("mandatory")


class _NscDxProcTableEntType_Type(DisplayString):
    """Custom type nscDxProcTableEntType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_NscDxProcTableEntType_Type.__name__ = "DisplayString"
_NscDxProcTableEntType_Object = MibTableColumn
nscDxProcTableEntType = _NscDxProcTableEntType_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 2, 1, 2),
    _NscDxProcTableEntType_Type()
)
nscDxProcTableEntType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxProcTableEntType.setStatus("mandatory")


class _NscDxProcTableEntFirmwareNum_Type(DisplayString):
    """Custom type nscDxProcTableEntFirmwareNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )


_NscDxProcTableEntFirmwareNum_Type.__name__ = "DisplayString"
_NscDxProcTableEntFirmwareNum_Object = MibTableColumn
nscDxProcTableEntFirmwareNum = _NscDxProcTableEntFirmwareNum_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 2, 1, 3),
    _NscDxProcTableEntFirmwareNum_Type()
)
nscDxProcTableEntFirmwareNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxProcTableEntFirmwareNum.setStatus("mandatory")


class _NscDxProcTableEntHardwareNum_Type(DisplayString):
    """Custom type nscDxProcTableEntHardwareNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )


_NscDxProcTableEntHardwareNum_Type.__name__ = "DisplayString"
_NscDxProcTableEntHardwareNum_Object = MibTableColumn
nscDxProcTableEntHardwareNum = _NscDxProcTableEntHardwareNum_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 2, 1, 4),
    _NscDxProcTableEntHardwareNum_Type()
)
nscDxProcTableEntHardwareNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxProcTableEntHardwareNum.setStatus("mandatory")


class _NscDxProcTableEntBaseAddr_Type(OctetString):
    """Custom type nscDxProcTableEntBaseAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_NscDxProcTableEntBaseAddr_Type.__name__ = "OctetString"
_NscDxProcTableEntBaseAddr_Object = MibTableColumn
nscDxProcTableEntBaseAddr = _NscDxProcTableEntBaseAddr_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 2, 1, 5),
    _NscDxProcTableEntBaseAddr_Type()
)
nscDxProcTableEntBaseAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxProcTableEntBaseAddr.setStatus("mandatory")


class _NscDxProcTableEntPost_Type(DisplayString):
    """Custom type nscDxProcTableEntPost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_NscDxProcTableEntPost_Type.__name__ = "DisplayString"
_NscDxProcTableEntPost_Object = MibTableColumn
nscDxProcTableEntPost = _NscDxProcTableEntPost_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 2, 1, 6),
    _NscDxProcTableEntPost_Type()
)
nscDxProcTableEntPost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxProcTableEntPost.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCDX-MIB",
    **{"nscDxConfig": nscDxConfig,
       "nscDxConfigSecondsToReset": nscDxConfigSecondsToReset,
       "nscDxConfigFirmwareRevTab": nscDxConfigFirmwareRevTab,
       "nscDxConfigBufferMemorySize": nscDxConfigBufferMemorySize,
       "nscDxConfigSecondsSinceMc": nscDxConfigSecondsSinceMc,
       "nscDxConfigProcessorMask": nscDxConfigProcessorMask,
       "nscDxConfigControlAddr": nscDxConfigControlAddr,
       "nscDxConfigLargePageSize": nscDxConfigLargePageSize,
       "nscDxConfigBoardInfoTable": nscDxConfigBoardInfoTable,
       "nscDxConfigBoardInfoEntry": nscDxConfigBoardInfoEntry,
       "nscDxConfigBoardInfoEntSlotNum": nscDxConfigBoardInfoEntSlotNum,
       "nscDxConfigBoardInfoEntBoardPart": nscDxConfigBoardInfoEntBoardPart,
       "nscDxConfigTime": nscDxConfigTime,
       "nscDxConfigDate": nscDxConfigDate,
       "nscDxConfigStartType": nscDxConfigStartType,
       "nscDxConfigMemoryDivision": nscDxConfigMemoryDivision,
       "nscDxProcTable": nscDxProcTable,
       "nscDxProcTableEntry": nscDxProcTableEntry,
       "nscDxProcTableEntKeyId": nscDxProcTableEntKeyId,
       "nscDxProcTableEntType": nscDxProcTableEntType,
       "nscDxProcTableEntFirmwareNum": nscDxProcTableEntFirmwareNum,
       "nscDxProcTableEntHardwareNum": nscDxProcTableEntHardwareNum,
       "nscDxProcTableEntBaseAddr": nscDxProcTableEntBaseAddr,
       "nscDxProcTableEntPost": nscDxProcTableEntPost}
)
