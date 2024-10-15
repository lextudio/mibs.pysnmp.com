# SNMP MIB module (BDCOM-FLASH) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BDCOM-FLASH
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:32 2024
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

(bdlocal,) = mibBuilder.importSymbols(
    "BDCOM-SMI",
    "bdlocal")

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

_Bdlflash_ObjectIdentity = ObjectIdentity
bdlflash = _Bdlflash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 2, 10)
)
_BdflashSize_Type = Integer32
_BdflashSize_Object = MibScalar
bdflashSize = _BdflashSize_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 10, 1),
    _BdflashSize_Type()
)
bdflashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdflashSize.setStatus("mandatory")
_BdflashFree_Type = Integer32
_BdflashFree_Object = MibScalar
bdflashFree = _BdflashFree_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 10, 2),
    _BdflashFree_Type()
)
bdflashFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdflashFree.setStatus("mandatory")
_BdflashController_Type = DisplayString
_BdflashController_Object = MibScalar
bdflashController = _BdflashController_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 10, 3),
    _BdflashController_Type()
)
bdflashController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdflashController.setStatus("mandatory")
_BdflashCard_Type = DisplayString
_BdflashCard_Object = MibScalar
bdflashCard = _BdflashCard_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 10, 4),
    _BdflashCard_Type()
)
bdflashCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdflashCard.setStatus("mandatory")


class _BdflashVPP_Type(Integer32):
    """Custom type bdflashVPP based on Integer32"""
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


_BdflashVPP_Type.__name__ = "Integer32"
_BdflashVPP_Object = MibScalar
bdflashVPP = _BdflashVPP_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 10, 5),
    _BdflashVPP_Type()
)
bdflashVPP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdflashVPP.setStatus("mandatory")
_BdflashErase_Type = Integer32
_BdflashErase_Object = MibScalar
bdflashErase = _BdflashErase_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 10, 6),
    _BdflashErase_Type()
)
bdflashErase.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    bdflashErase.setStatus("mandatory")
_BdflashEraseTime_Type = TimeTicks
_BdflashEraseTime_Object = MibScalar
bdflashEraseTime = _BdflashEraseTime_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 10, 7),
    _BdflashEraseTime_Type()
)
bdflashEraseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdflashEraseTime.setStatus("mandatory")


class _BdflashEraseStatus_Type(Integer32):
    """Custom type bdflashEraseStatus based on Integer32"""
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


_BdflashEraseStatus_Type.__name__ = "Integer32"
_BdflashEraseStatus_Object = MibScalar
bdflashEraseStatus = _BdflashEraseStatus_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 10, 8),
    _BdflashEraseStatus_Type()
)
bdflashEraseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdflashEraseStatus.setStatus("mandatory")
_BdflashToNet_Type = DisplayString
_BdflashToNet_Object = MibScalar
bdflashToNet = _BdflashToNet_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 10, 9),
    _BdflashToNet_Type()
)
bdflashToNet.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    bdflashToNet.setStatus("mandatory")
_BdflashToNetTime_Type = TimeTicks
_BdflashToNetTime_Object = MibScalar
bdflashToNetTime = _BdflashToNetTime_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 10, 10),
    _BdflashToNetTime_Type()
)
bdflashToNetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdflashToNetTime.setStatus("mandatory")


class _BdflashToNetStatus_Type(Integer32):
    """Custom type bdflashToNetStatus based on Integer32"""
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


_BdflashToNetStatus_Type.__name__ = "Integer32"
_BdflashToNetStatus_Object = MibScalar
bdflashToNetStatus = _BdflashToNetStatus_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 10, 11),
    _BdflashToNetStatus_Type()
)
bdflashToNetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdflashToNetStatus.setStatus("mandatory")
_BdnetToFlash_Type = DisplayString
_BdnetToFlash_Object = MibScalar
bdnetToFlash = _BdnetToFlash_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 10, 12),
    _BdnetToFlash_Type()
)
bdnetToFlash.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    bdnetToFlash.setStatus("mandatory")
_BdnetToFlashTime_Type = TimeTicks
_BdnetToFlashTime_Object = MibScalar
bdnetToFlashTime = _BdnetToFlashTime_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 10, 13),
    _BdnetToFlashTime_Type()
)
bdnetToFlashTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdnetToFlashTime.setStatus("mandatory")


class _BdnetToFlashStatus_Type(Integer32):
    """Custom type bdnetToFlashStatus based on Integer32"""
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


_BdnetToFlashStatus_Type.__name__ = "Integer32"
_BdnetToFlashStatus_Object = MibScalar
bdnetToFlashStatus = _BdnetToFlashStatus_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 10, 14),
    _BdnetToFlashStatus_Type()
)
bdnetToFlashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdnetToFlashStatus.setStatus("mandatory")


class _BdflashStatus_Type(Integer32):
    """Custom type bdflashStatus based on Integer32"""
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


_BdflashStatus_Type.__name__ = "Integer32"
_BdflashStatus_Object = MibScalar
bdflashStatus = _BdflashStatus_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 10, 15),
    _BdflashStatus_Type()
)
bdflashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdflashStatus.setStatus("mandatory")
_BdflashEntries_Type = Integer32
_BdflashEntries_Object = MibScalar
bdflashEntries = _BdflashEntries_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 10, 16),
    _BdflashEntries_Type()
)
bdflashEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdflashEntries.setStatus("mandatory")
_BdlflashFileDirTable_Object = MibTable
bdlflashFileDirTable = _BdlflashFileDirTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 10, 17)
)
if mibBuilder.loadTexts:
    bdlflashFileDirTable.setStatus("mandatory")
_BdlflashFileDirEntry_Object = MibTableRow
bdlflashFileDirEntry = _BdlflashFileDirEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 10, 17, 1)
)
bdlflashFileDirEntry.setIndexNames(
    (0, "BDCOM-FLASH", "flashEntries"),
)
if mibBuilder.loadTexts:
    bdlflashFileDirEntry.setStatus("mandatory")
_BdflashDirName_Type = DisplayString
_BdflashDirName_Object = MibTableColumn
bdflashDirName = _BdflashDirName_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 10, 17, 1, 1),
    _BdflashDirName_Type()
)
bdflashDirName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdflashDirName.setStatus("mandatory")
_BdflashDirSize_Type = Integer32
_BdflashDirSize_Object = MibTableColumn
bdflashDirSize = _BdflashDirSize_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 10, 17, 1, 2),
    _BdflashDirSize_Type()
)
bdflashDirSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdflashDirSize.setStatus("mandatory")


class _BdflashDirStatus_Type(Integer32):
    """Custom type bdflashDirStatus based on Integer32"""
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


_BdflashDirStatus_Type.__name__ = "Integer32"
_BdflashDirStatus_Object = MibTableColumn
bdflashDirStatus = _BdflashDirStatus_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 10, 17, 1, 3),
    _BdflashDirStatus_Type()
)
bdflashDirStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdflashDirStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BDCOM-FLASH",
    **{"bdlflash": bdlflash,
       "bdflashSize": bdflashSize,
       "bdflashFree": bdflashFree,
       "bdflashController": bdflashController,
       "bdflashCard": bdflashCard,
       "bdflashVPP": bdflashVPP,
       "bdflashErase": bdflashErase,
       "bdflashEraseTime": bdflashEraseTime,
       "bdflashEraseStatus": bdflashEraseStatus,
       "bdflashToNet": bdflashToNet,
       "bdflashToNetTime": bdflashToNetTime,
       "bdflashToNetStatus": bdflashToNetStatus,
       "bdnetToFlash": bdnetToFlash,
       "bdnetToFlashTime": bdnetToFlashTime,
       "bdnetToFlashStatus": bdnetToFlashStatus,
       "bdflashStatus": bdflashStatus,
       "bdflashEntries": bdflashEntries,
       "bdlflashFileDirTable": bdlflashFileDirTable,
       "bdlflashFileDirEntry": bdlflashFileDirEntry,
       "bdflashDirName": bdflashDirName,
       "bdflashDirSize": bdflashDirSize,
       "bdflashDirStatus": bdflashDirStatus}
)
