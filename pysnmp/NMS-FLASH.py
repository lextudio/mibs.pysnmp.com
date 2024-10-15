# SNMP MIB module (NMS-FLASH) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-FLASH
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:54 2024
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

(nmslocal,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmslocal")

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

_Nmslflash_ObjectIdentity = ObjectIdentity
nmslflash = _Nmslflash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 10)
)
_NmsflashSize_Type = Integer32
_NmsflashSize_Object = MibScalar
nmsflashSize = _NmsflashSize_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 1),
    _NmsflashSize_Type()
)
nmsflashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsflashSize.setStatus("mandatory")
_NmsflashFree_Type = Integer32
_NmsflashFree_Object = MibScalar
nmsflashFree = _NmsflashFree_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 2),
    _NmsflashFree_Type()
)
nmsflashFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsflashFree.setStatus("mandatory")
_NmsflashController_Type = DisplayString
_NmsflashController_Object = MibScalar
nmsflashController = _NmsflashController_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 3),
    _NmsflashController_Type()
)
nmsflashController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsflashController.setStatus("mandatory")
_NmsflashCard_Type = DisplayString
_NmsflashCard_Object = MibScalar
nmsflashCard = _NmsflashCard_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 4),
    _NmsflashCard_Type()
)
nmsflashCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsflashCard.setStatus("mandatory")


class _NmsflashVPP_Type(Integer32):
    """Custom type nmsflashVPP based on Integer32"""
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


_NmsflashVPP_Type.__name__ = "Integer32"
_NmsflashVPP_Object = MibScalar
nmsflashVPP = _NmsflashVPP_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 5),
    _NmsflashVPP_Type()
)
nmsflashVPP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsflashVPP.setStatus("mandatory")
_NmsflashErase_Type = Integer32
_NmsflashErase_Object = MibScalar
nmsflashErase = _NmsflashErase_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 6),
    _NmsflashErase_Type()
)
nmsflashErase.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    nmsflashErase.setStatus("mandatory")
_NmsflashEraseTime_Type = TimeTicks
_NmsflashEraseTime_Object = MibScalar
nmsflashEraseTime = _NmsflashEraseTime_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 7),
    _NmsflashEraseTime_Type()
)
nmsflashEraseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsflashEraseTime.setStatus("mandatory")


class _NmsflashEraseStatus_Type(Integer32):
    """Custom type nmsflashEraseStatus based on Integer32"""
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


_NmsflashEraseStatus_Type.__name__ = "Integer32"
_NmsflashEraseStatus_Object = MibScalar
nmsflashEraseStatus = _NmsflashEraseStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 8),
    _NmsflashEraseStatus_Type()
)
nmsflashEraseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsflashEraseStatus.setStatus("mandatory")
_NmsflashToNet_Type = DisplayString
_NmsflashToNet_Object = MibScalar
nmsflashToNet = _NmsflashToNet_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 9),
    _NmsflashToNet_Type()
)
nmsflashToNet.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    nmsflashToNet.setStatus("mandatory")
_NmsflashToNetTime_Type = TimeTicks
_NmsflashToNetTime_Object = MibScalar
nmsflashToNetTime = _NmsflashToNetTime_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 10),
    _NmsflashToNetTime_Type()
)
nmsflashToNetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsflashToNetTime.setStatus("mandatory")


class _NmsflashToNetStatus_Type(Integer32):
    """Custom type nmsflashToNetStatus based on Integer32"""
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


_NmsflashToNetStatus_Type.__name__ = "Integer32"
_NmsflashToNetStatus_Object = MibScalar
nmsflashToNetStatus = _NmsflashToNetStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 11),
    _NmsflashToNetStatus_Type()
)
nmsflashToNetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsflashToNetStatus.setStatus("mandatory")
_NmsnetToFlash_Type = DisplayString
_NmsnetToFlash_Object = MibScalar
nmsnetToFlash = _NmsnetToFlash_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 12),
    _NmsnetToFlash_Type()
)
nmsnetToFlash.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    nmsnetToFlash.setStatus("mandatory")
_NmsnetToFlashTime_Type = TimeTicks
_NmsnetToFlashTime_Object = MibScalar
nmsnetToFlashTime = _NmsnetToFlashTime_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 13),
    _NmsnetToFlashTime_Type()
)
nmsnetToFlashTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsnetToFlashTime.setStatus("mandatory")


class _NmsnetToFlashStatus_Type(Integer32):
    """Custom type nmsnetToFlashStatus based on Integer32"""
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


_NmsnetToFlashStatus_Type.__name__ = "Integer32"
_NmsnetToFlashStatus_Object = MibScalar
nmsnetToFlashStatus = _NmsnetToFlashStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 14),
    _NmsnetToFlashStatus_Type()
)
nmsnetToFlashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsnetToFlashStatus.setStatus("mandatory")


class _NmsflashStatus_Type(Integer32):
    """Custom type nmsflashStatus based on Integer32"""
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


_NmsflashStatus_Type.__name__ = "Integer32"
_NmsflashStatus_Object = MibScalar
nmsflashStatus = _NmsflashStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 15),
    _NmsflashStatus_Type()
)
nmsflashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsflashStatus.setStatus("mandatory")
_NmsflashEntries_Type = Integer32
_NmsflashEntries_Object = MibScalar
nmsflashEntries = _NmsflashEntries_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 16),
    _NmsflashEntries_Type()
)
nmsflashEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsflashEntries.setStatus("mandatory")
_NmslflashFileDirTable_Object = MibTable
nmslflashFileDirTable = _NmslflashFileDirTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 17)
)
if mibBuilder.loadTexts:
    nmslflashFileDirTable.setStatus("mandatory")
_NmslflashFileDirEntry_Object = MibTableRow
nmslflashFileDirEntry = _NmslflashFileDirEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 17, 1)
)
nmslflashFileDirEntry.setIndexNames(
    (0, "NMS-FLASH", "flashEntries"),
)
if mibBuilder.loadTexts:
    nmslflashFileDirEntry.setStatus("mandatory")
_NmsflashDirName_Type = DisplayString
_NmsflashDirName_Object = MibTableColumn
nmsflashDirName = _NmsflashDirName_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 17, 1, 1),
    _NmsflashDirName_Type()
)
nmsflashDirName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsflashDirName.setStatus("mandatory")
_NmsflashDirSize_Type = Integer32
_NmsflashDirSize_Object = MibTableColumn
nmsflashDirSize = _NmsflashDirSize_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 17, 1, 2),
    _NmsflashDirSize_Type()
)
nmsflashDirSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsflashDirSize.setStatus("mandatory")


class _NmsflashDirStatus_Type(Integer32):
    """Custom type nmsflashDirStatus based on Integer32"""
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


_NmsflashDirStatus_Type.__name__ = "Integer32"
_NmsflashDirStatus_Object = MibTableColumn
nmsflashDirStatus = _NmsflashDirStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 17, 1, 3),
    _NmsflashDirStatus_Type()
)
nmsflashDirStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsflashDirStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-FLASH",
    **{"nmslflash": nmslflash,
       "nmsflashSize": nmsflashSize,
       "nmsflashFree": nmsflashFree,
       "nmsflashController": nmsflashController,
       "nmsflashCard": nmsflashCard,
       "nmsflashVPP": nmsflashVPP,
       "nmsflashErase": nmsflashErase,
       "nmsflashEraseTime": nmsflashEraseTime,
       "nmsflashEraseStatus": nmsflashEraseStatus,
       "nmsflashToNet": nmsflashToNet,
       "nmsflashToNetTime": nmsflashToNetTime,
       "nmsflashToNetStatus": nmsflashToNetStatus,
       "nmsnetToFlash": nmsnetToFlash,
       "nmsnetToFlashTime": nmsnetToFlashTime,
       "nmsnetToFlashStatus": nmsnetToFlashStatus,
       "nmsflashStatus": nmsflashStatus,
       "nmsflashEntries": nmsflashEntries,
       "nmslflashFileDirTable": nmslflashFileDirTable,
       "nmslflashFileDirEntry": nmslflashFileDirEntry,
       "nmsflashDirName": nmsflashDirName,
       "nmsflashDirSize": nmsflashDirSize,
       "nmsflashDirStatus": nmsflashDirStatus}
)
