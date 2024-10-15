# SNMP MIB module (OLD-CISCO-FLASH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OLD-CISCO-FLASH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:01 2024
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

(local,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "local")

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

_Lflash_ObjectIdentity = ObjectIdentity
lflash = _Lflash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2, 10)
)
_FlashSize_Type = Integer32
_FlashSize_Object = MibScalar
flashSize = _FlashSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 1),
    _FlashSize_Type()
)
flashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashSize.setStatus("mandatory")
_FlashFree_Type = Integer32
_FlashFree_Object = MibScalar
flashFree = _FlashFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 2),
    _FlashFree_Type()
)
flashFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashFree.setStatus("mandatory")
_FlashController_Type = DisplayString
_FlashController_Object = MibScalar
flashController = _FlashController_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 3),
    _FlashController_Type()
)
flashController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashController.setStatus("mandatory")
_FlashCard_Type = DisplayString
_FlashCard_Object = MibScalar
flashCard = _FlashCard_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 4),
    _FlashCard_Type()
)
flashCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCard.setStatus("mandatory")


class _FlashVPP_Type(Integer32):
    """Custom type flashVPP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("missing", 2))
    )


_FlashVPP_Type.__name__ = "Integer32"
_FlashVPP_Object = MibScalar
flashVPP = _FlashVPP_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 5),
    _FlashVPP_Type()
)
flashVPP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashVPP.setStatus("mandatory")
_FlashErase_Type = Integer32
_FlashErase_Object = MibScalar
flashErase = _FlashErase_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 6),
    _FlashErase_Type()
)
flashErase.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    flashErase.setStatus("mandatory")
_FlashEraseTime_Type = TimeTicks
_FlashEraseTime_Object = MibScalar
flashEraseTime = _FlashEraseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 7),
    _FlashEraseTime_Type()
)
flashEraseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashEraseTime.setStatus("mandatory")


class _FlashEraseStatus_Type(Integer32):
    """Custom type flashEraseStatus based on Integer32"""
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
        *(("bufferAllocationFailure", 6),
          ("flashOpFailure", 3),
          ("flashOpInProgress", 1),
          ("flashOpSuccess", 2),
          ("flashOpenFailure", 5),
          ("flashReadOnly", 4),
          ("noOpAfterPowerOn", 7))
    )


_FlashEraseStatus_Type.__name__ = "Integer32"
_FlashEraseStatus_Object = MibScalar
flashEraseStatus = _FlashEraseStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 8),
    _FlashEraseStatus_Type()
)
flashEraseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashEraseStatus.setStatus("mandatory")
_FlashToNet_Type = DisplayString
_FlashToNet_Object = MibScalar
flashToNet = _FlashToNet_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 9),
    _FlashToNet_Type()
)
flashToNet.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    flashToNet.setStatus("mandatory")
_FlashToNetTime_Type = TimeTicks
_FlashToNetTime_Object = MibScalar
flashToNetTime = _FlashToNetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 10),
    _FlashToNetTime_Type()
)
flashToNetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashToNetTime.setStatus("mandatory")


class _FlashToNetStatus_Type(Integer32):
    """Custom type flashToNetStatus based on Integer32"""
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
        *(("bufferAllocationFailure", 6),
          ("flashOpFailure", 3),
          ("flashOpInProgress", 1),
          ("flashOpSuccess", 2),
          ("flashOpenFailure", 5),
          ("flashReadOnly", 4),
          ("noOpAfterPowerOn", 7))
    )


_FlashToNetStatus_Type.__name__ = "Integer32"
_FlashToNetStatus_Object = MibScalar
flashToNetStatus = _FlashToNetStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 11),
    _FlashToNetStatus_Type()
)
flashToNetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashToNetStatus.setStatus("mandatory")
_NetToFlash_Type = DisplayString
_NetToFlash_Object = MibScalar
netToFlash = _NetToFlash_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 12),
    _NetToFlash_Type()
)
netToFlash.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    netToFlash.setStatus("mandatory")
_NetToFlashTime_Type = TimeTicks
_NetToFlashTime_Object = MibScalar
netToFlashTime = _NetToFlashTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 13),
    _NetToFlashTime_Type()
)
netToFlashTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netToFlashTime.setStatus("mandatory")


class _NetToFlashStatus_Type(Integer32):
    """Custom type netToFlashStatus based on Integer32"""
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
        *(("bufferAllocationFailure", 6),
          ("flashOpFailure", 3),
          ("flashOpInProgress", 1),
          ("flashOpSuccess", 2),
          ("flashOpenFailure", 5),
          ("flashReadOnly", 4),
          ("noOpAfterPowerOn", 7))
    )


_NetToFlashStatus_Type.__name__ = "Integer32"
_NetToFlashStatus_Object = MibScalar
netToFlashStatus = _NetToFlashStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 14),
    _NetToFlashStatus_Type()
)
netToFlashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netToFlashStatus.setStatus("mandatory")


class _FlashStatus_Type(Integer32):
    """Custom type flashStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("busy", 1))
    )


_FlashStatus_Type.__name__ = "Integer32"
_FlashStatus_Object = MibScalar
flashStatus = _FlashStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 15),
    _FlashStatus_Type()
)
flashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashStatus.setStatus("mandatory")
_FlashEntries_Type = Integer32
_FlashEntries_Object = MibScalar
flashEntries = _FlashEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 16),
    _FlashEntries_Type()
)
flashEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashEntries.setStatus("mandatory")
_LflashFileDirTable_Object = MibTable
lflashFileDirTable = _LflashFileDirTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 17)
)
if mibBuilder.loadTexts:
    lflashFileDirTable.setStatus("mandatory")
_LflashFileDirEntry_Object = MibTableRow
lflashFileDirEntry = _LflashFileDirEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 17, 1)
)
lflashFileDirEntry.setIndexNames(
    (0, "OLD-CISCO-FLASH-MIB", "flashEntries"),
)
if mibBuilder.loadTexts:
    lflashFileDirEntry.setStatus("mandatory")
_FlashDirName_Type = DisplayString
_FlashDirName_Object = MibTableColumn
flashDirName = _FlashDirName_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 17, 1, 1),
    _FlashDirName_Type()
)
flashDirName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashDirName.setStatus("mandatory")
_FlashDirSize_Type = Integer32
_FlashDirSize_Object = MibTableColumn
flashDirSize = _FlashDirSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 17, 1, 2),
    _FlashDirSize_Type()
)
flashDirSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashDirSize.setStatus("mandatory")


class _FlashDirStatus_Type(Integer32):
    """Custom type flashDirStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 2),
          ("valid", 1))
    )


_FlashDirStatus_Type.__name__ = "Integer32"
_FlashDirStatus_Object = MibTableColumn
flashDirStatus = _FlashDirStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 17, 1, 3),
    _FlashDirStatus_Type()
)
flashDirStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashDirStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OLD-CISCO-FLASH-MIB",
    **{"lflash": lflash,
       "flashSize": flashSize,
       "flashFree": flashFree,
       "flashController": flashController,
       "flashCard": flashCard,
       "flashVPP": flashVPP,
       "flashErase": flashErase,
       "flashEraseTime": flashEraseTime,
       "flashEraseStatus": flashEraseStatus,
       "flashToNet": flashToNet,
       "flashToNetTime": flashToNetTime,
       "flashToNetStatus": flashToNetStatus,
       "netToFlash": netToFlash,
       "netToFlashTime": netToFlashTime,
       "netToFlashStatus": netToFlashStatus,
       "flashStatus": flashStatus,
       "flashEntries": flashEntries,
       "lflashFileDirTable": lflashFileDirTable,
       "lflashFileDirEntry": lflashFileDirEntry,
       "flashDirName": flashDirName,
       "flashDirSize": flashDirSize,
       "flashDirStatus": flashDirStatus}
)
