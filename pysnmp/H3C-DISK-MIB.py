# SNMP MIB module (H3C-DISK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-DISK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:05 2024
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

(H3cStorageActionType,
 H3cStorageEnableState,
 h3cStorageRef) = mibBuilder.importSymbols(
    "H3C-STORAGE-REF-MIB",
    "H3cStorageActionType",
    "H3cStorageEnableState",
    "h3cStorageRef")

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

h3cDisk = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cDiskMibObjects_ObjectIdentity = ObjectIdentity
h3cDiskMibObjects = _H3cDiskMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1)
)
_H3cDiskTable_Object = MibTable
h3cDiskTable = _H3cDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1)
)
if mibBuilder.loadTexts:
    h3cDiskTable.setStatus("current")
_H3cDiskEntry_Object = MibTableRow
h3cDiskEntry = _H3cDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1)
)
h3cDiskEntry.setIndexNames(
    (0, "H3C-DISK-MIB", "h3cDiskIndex"),
)
if mibBuilder.loadTexts:
    h3cDiskEntry.setStatus("current")
_H3cDiskIndex_Type = Integer32
_H3cDiskIndex_Object = MibTableColumn
h3cDiskIndex = _H3cDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1, 1),
    _H3cDiskIndex_Type()
)
h3cDiskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDiskIndex.setStatus("current")


class _H3cDiskPortType_Type(Integer32):
    """Custom type h3cDiskPortType based on Integer32"""
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
        *(("fcal", 6),
          ("ieee1394", 5),
          ("pata", 2),
          ("sas", 3),
          ("sata", 1),
          ("scsi", 4))
    )


_H3cDiskPortType_Type.__name__ = "Integer32"
_H3cDiskPortType_Object = MibTableColumn
h3cDiskPortType = _H3cDiskPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1, 2),
    _H3cDiskPortType_Type()
)
h3cDiskPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDiskPortType.setStatus("current")
_H3cDiskPortSpeed_Type = Integer32
_H3cDiskPortSpeed_Object = MibTableColumn
h3cDiskPortSpeed = _H3cDiskPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1, 3),
    _H3cDiskPortSpeed_Type()
)
h3cDiskPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDiskPortSpeed.setStatus("current")
if mibBuilder.loadTexts:
    h3cDiskPortSpeed.setUnits("MB/second")
_H3cDiskSize_Type = Integer32
_H3cDiskSize_Object = MibTableColumn
h3cDiskSize = _H3cDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1, 4),
    _H3cDiskSize_Type()
)
h3cDiskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDiskSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cDiskSize.setUnits("MB")
_H3cDiskFreeSpace_Type = Integer32
_H3cDiskFreeSpace_Object = MibTableColumn
h3cDiskFreeSpace = _H3cDiskFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1, 5),
    _H3cDiskFreeSpace_Type()
)
h3cDiskFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDiskFreeSpace.setStatus("current")
if mibBuilder.loadTexts:
    h3cDiskFreeSpace.setUnits("MB")


class _H3cDiskLocationState_Type(H3cStorageEnableState):
    """Custom type h3cDiskLocationState based on H3cStorageEnableState"""


_H3cDiskLocationState_Object = MibTableColumn
h3cDiskLocationState = _H3cDiskLocationState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1, 6),
    _H3cDiskLocationState_Type()
)
h3cDiskLocationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDiskLocationState.setStatus("current")


class _H3cDiskRunLedState_Type(Integer32):
    """Custom type h3cDiskRunLedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blink", 2),
          ("fastblink", 3),
          ("on", 1))
    )


_H3cDiskRunLedState_Type.__name__ = "Integer32"
_H3cDiskRunLedState_Object = MibTableColumn
h3cDiskRunLedState = _H3cDiskRunLedState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1, 7),
    _H3cDiskRunLedState_Type()
)
h3cDiskRunLedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDiskRunLedState.setStatus("current")


class _H3cDiskFaultLedState_Type(Integer32):
    """Custom type h3cDiskFaultLedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blink", 3),
          ("off", 1),
          ("on", 2))
    )


_H3cDiskFaultLedState_Type.__name__ = "Integer32"
_H3cDiskFaultLedState_Object = MibTableColumn
h3cDiskFaultLedState = _H3cDiskFaultLedState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1, 8),
    _H3cDiskFaultLedState_Type()
)
h3cDiskFaultLedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDiskFaultLedState.setStatus("current")
_H3cDiskInitialize_Type = H3cStorageActionType
_H3cDiskInitialize_Object = MibTableColumn
h3cDiskInitialize = _H3cDiskInitialize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1, 9),
    _H3cDiskInitialize_Type()
)
h3cDiskInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDiskInitialize.setStatus("current")


class _H3cDiskGlobalSpare_Type(Integer32):
    """Custom type h3cDiskGlobalSpare based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("globalSpare", 1),
          ("nonglobalSpare", 2))
    )


_H3cDiskGlobalSpare_Type.__name__ = "Integer32"
_H3cDiskGlobalSpare_Object = MibTableColumn
h3cDiskGlobalSpare = _H3cDiskGlobalSpare_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1, 10),
    _H3cDiskGlobalSpare_Type()
)
h3cDiskGlobalSpare.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDiskGlobalSpare.setStatus("current")


class _H3cDiskLocalSpare_Type(Integer32):
    """Custom type h3cDiskLocalSpare based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localSpare", 1),
          ("nonlocalSpare", 2))
    )


_H3cDiskLocalSpare_Type.__name__ = "Integer32"
_H3cDiskLocalSpare_Object = MibTableColumn
h3cDiskLocalSpare = _H3cDiskLocalSpare_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1, 11),
    _H3cDiskLocalSpare_Type()
)
h3cDiskLocalSpare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDiskLocalSpare.setStatus("current")


class _H3cDiskReadCache_Type(H3cStorageEnableState):
    """Custom type h3cDiskReadCache based on H3cStorageEnableState"""


_H3cDiskReadCache_Object = MibTableColumn
h3cDiskReadCache = _H3cDiskReadCache_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1, 12),
    _H3cDiskReadCache_Type()
)
h3cDiskReadCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDiskReadCache.setStatus("current")


class _H3cDiskWriteCache_Type(H3cStorageEnableState):
    """Custom type h3cDiskWriteCache based on H3cStorageEnableState"""


_H3cDiskWriteCache_Object = MibTableColumn
h3cDiskWriteCache = _H3cDiskWriteCache_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1, 13),
    _H3cDiskWriteCache_Type()
)
h3cDiskWriteCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDiskWriteCache.setStatus("current")


class _H3cDiskPowerOffReason_Type(Integer32):
    """Custom type h3cDiskPowerOffReason based on Integer32"""
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
        *(("environmentUnstable", 1),
          ("generalError", 4),
          ("mediumError", 2),
          ("smartCheckError", 3))
    )


_H3cDiskPowerOffReason_Type.__name__ = "Integer32"
_H3cDiskPowerOffReason_Object = MibTableColumn
h3cDiskPowerOffReason = _H3cDiskPowerOffReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 10, 3, 1, 1, 1, 14),
    _H3cDiskPowerOffReason_Type()
)
h3cDiskPowerOffReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDiskPowerOffReason.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-DISK-MIB",
    **{"h3cDisk": h3cDisk,
       "h3cDiskMibObjects": h3cDiskMibObjects,
       "h3cDiskTable": h3cDiskTable,
       "h3cDiskEntry": h3cDiskEntry,
       "h3cDiskIndex": h3cDiskIndex,
       "h3cDiskPortType": h3cDiskPortType,
       "h3cDiskPortSpeed": h3cDiskPortSpeed,
       "h3cDiskSize": h3cDiskSize,
       "h3cDiskFreeSpace": h3cDiskFreeSpace,
       "h3cDiskLocationState": h3cDiskLocationState,
       "h3cDiskRunLedState": h3cDiskRunLedState,
       "h3cDiskFaultLedState": h3cDiskFaultLedState,
       "h3cDiskInitialize": h3cDiskInitialize,
       "h3cDiskGlobalSpare": h3cDiskGlobalSpare,
       "h3cDiskLocalSpare": h3cDiskLocalSpare,
       "h3cDiskReadCache": h3cDiskReadCache,
       "h3cDiskWriteCache": h3cDiskWriteCache,
       "h3cDiskPowerOffReason": h3cDiskPowerOffReason}
)
