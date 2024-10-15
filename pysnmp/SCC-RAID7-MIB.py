# SNMP MIB module (SCC-RAID7-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SCC-RAID7-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:59 2024
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

(raid7mib,) = mibBuilder.importSymbols(
    "SCC-ENTERPRISE-MIB",
    "raid7mib")

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
 NotificationType,
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
    "NotificationType",
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

_Raid7Sys_ObjectIdentity = ObjectIdentity
raid7Sys = _Raid7Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 1)
)
_Raid7SysVersion_Type = IpAddress
_Raid7SysVersion_Object = MibScalar
raid7SysVersion = _Raid7SysVersion_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 1, 1),
    _Raid7SysVersion_Type()
)
raid7SysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7SysVersion.setStatus("mandatory")
_Raid7Memory_ObjectIdentity = ObjectIdentity
raid7Memory = _Raid7Memory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 2)
)
_Raid7TotalMem_Type = Integer32
_Raid7TotalMem_Object = MibScalar
raid7TotalMem = _Raid7TotalMem_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 2, 1),
    _Raid7TotalMem_Type()
)
raid7TotalMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7TotalMem.setStatus("mandatory")
_Raid7GoodMem_Type = Integer32
_Raid7GoodMem_Object = MibScalar
raid7GoodMem = _Raid7GoodMem_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 2, 2),
    _Raid7GoodMem_Type()
)
raid7GoodMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7GoodMem.setStatus("mandatory")
_Raid7MemAvail_Type = Integer32
_Raid7MemAvail_Object = MibScalar
raid7MemAvail = _Raid7MemAvail_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 2, 3),
    _Raid7MemAvail_Type()
)
raid7MemAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7MemAvail.setStatus("mandatory")


class _Raid7CacheHitPercent_Type(Integer32):
    """Custom type raid7CacheHitPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Raid7CacheHitPercent_Type.__name__ = "Integer32"
_Raid7CacheHitPercent_Object = MibScalar
raid7CacheHitPercent = _Raid7CacheHitPercent_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 2, 4),
    _Raid7CacheHitPercent_Type()
)
raid7CacheHitPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7CacheHitPercent.setStatus("mandatory")
_Raid7BlockTable_Object = MibTable
raid7BlockTable = _Raid7BlockTable_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    raid7BlockTable.setStatus("mandatory")
_Raid7BlockEntry_Object = MibTableRow
raid7BlockEntry = _Raid7BlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 2, 5, 1)
)
raid7BlockEntry.setIndexNames(
    (0, "SCC-RAID7-MIB", "raid7BlockSize"),
)
if mibBuilder.loadTexts:
    raid7BlockEntry.setStatus("mandatory")
_Raid7BlockSize_Type = Integer32
_Raid7BlockSize_Object = MibTableColumn
raid7BlockSize = _Raid7BlockSize_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 2, 5, 1, 1),
    _Raid7BlockSize_Type()
)
raid7BlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7BlockSize.setStatus("mandatory")
_Raid7NumBlocks_Type = Gauge32
_Raid7NumBlocks_Object = MibTableColumn
raid7NumBlocks = _Raid7NumBlocks_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 2, 5, 1, 2),
    _Raid7NumBlocks_Type()
)
raid7NumBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7NumBlocks.setStatus("mandatory")
_Raid7Host_ObjectIdentity = ObjectIdentity
raid7Host = _Raid7Host_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 3)
)


class _Raid7NumHostChannels_Type(Integer32):
    """Custom type raid7NumHostChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Raid7NumHostChannels_Type.__name__ = "Integer32"
_Raid7NumHostChannels_Object = MibScalar
raid7NumHostChannels = _Raid7NumHostChannels_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 3, 1),
    _Raid7NumHostChannels_Type()
)
raid7NumHostChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7NumHostChannels.setStatus("mandatory")
_Raid7ChannelTable_Object = MibTable
raid7ChannelTable = _Raid7ChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    raid7ChannelTable.setStatus("mandatory")
_Raid7ChannelEntry_Object = MibTableRow
raid7ChannelEntry = _Raid7ChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 3, 2, 1)
)
raid7ChannelEntry.setIndexNames(
    (0, "SCC-RAID7-MIB", "raid7ChannelNumber"),
)
if mibBuilder.loadTexts:
    raid7ChannelEntry.setStatus("mandatory")


class _Raid7ChannelNumber_Type(Integer32):
    """Custom type raid7ChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Raid7ChannelNumber_Type.__name__ = "Integer32"
_Raid7ChannelNumber_Object = MibTableColumn
raid7ChannelNumber = _Raid7ChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 3, 2, 1, 1),
    _Raid7ChannelNumber_Type()
)
raid7ChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7ChannelNumber.setStatus("mandatory")
_Raid7ChannelTransferRate_Type = Gauge32
_Raid7ChannelTransferRate_Object = MibTableColumn
raid7ChannelTransferRate = _Raid7ChannelTransferRate_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 3, 2, 1, 2),
    _Raid7ChannelTransferRate_Type()
)
raid7ChannelTransferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7ChannelTransferRate.setStatus("mandatory")
_Raid7ChannelTransactionRate_Type = Gauge32
_Raid7ChannelTransactionRate_Object = MibTableColumn
raid7ChannelTransactionRate = _Raid7ChannelTransactionRate_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 3, 2, 1, 3),
    _Raid7ChannelTransactionRate_Type()
)
raid7ChannelTransactionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7ChannelTransactionRate.setStatus("mandatory")
_Raid7ChannelErrorMsgs_Type = Counter32
_Raid7ChannelErrorMsgs_Object = MibTableColumn
raid7ChannelErrorMsgs = _Raid7ChannelErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 3, 2, 1, 4),
    _Raid7ChannelErrorMsgs_Type()
)
raid7ChannelErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7ChannelErrorMsgs.setStatus("mandatory")


class _Raid7ChannelLastKey_Type(Integer32):
    """Custom type raid7ChannelLastKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              11,
              14)
        )
    )
    namedValues = NamedValues(
        *(("abortedCommand", 11),
          ("hardwareError", 4),
          ("illegalRequest", 5),
          ("mediumError", 3),
          ("miscompare", 14),
          ("noSense", 0),
          ("notReady", 2),
          ("recoveredError", 1),
          ("unitAttention", 6))
    )


_Raid7ChannelLastKey_Type.__name__ = "Integer32"
_Raid7ChannelLastKey_Object = MibTableColumn
raid7ChannelLastKey = _Raid7ChannelLastKey_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 3, 2, 1, 5),
    _Raid7ChannelLastKey_Type()
)
raid7ChannelLastKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7ChannelLastKey.setStatus("mandatory")


class _Raid7ChannelLastSense_Type(Integer32):
    """Custom type raid7ChannelLastSense based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              8,
              12,
              17,
              23,
              24,
              26,
              27,
              28,
              29,
              32,
              33,
              34,
              36,
              37,
              38,
              41,
              47,
              49,
              61,
              64,
              67,
              68,
              69,
              70,
              72,
              73)
        )
    )
    namedValues = NamedValues(
        *(("communicationFailure", 8),
          ("defectListNotFound", 28),
          ("diagnosticFailure", 64),
          ("driveNotReady", 4),
          ("illegalFunction", 34),
          ("illegalMessage", 73),
          ("initClearQ", 47),
          ("initiatorDetectedError", 72),
          ("internalFailure", 68),
          ("invalidBlockAddress", 33),
          ("invalidCommand", 32),
          ("invalidField", 38),
          ("invalidFieldCDB", 36),
          ("invalidIdentify", 61),
          ("invalidLUN", 37),
          ("listLengthError", 26),
          ("mediaFormat", 49),
          ("messageRejectError", 67),
          ("noAddSense", 0),
          ("noIndexSectSignal", 1),
          ("noSeekComplete", 2),
          ("parityError", 70),
          ("readError", 17),
          ("resetCondition", 41),
          ("retries", 23),
          ("retriesAndECC", 24),
          ("selectFailure", 69),
          ("syncError", 27),
          ("verifyMiscompare", 29),
          ("writeError", 12),
          ("writeFault", 3))
    )


_Raid7ChannelLastSense_Type.__name__ = "Integer32"
_Raid7ChannelLastSense_Object = MibTableColumn
raid7ChannelLastSense = _Raid7ChannelLastSense_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 3, 2, 1, 6),
    _Raid7ChannelLastSense_Type()
)
raid7ChannelLastSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7ChannelLastSense.setStatus("mandatory")
_Raid7Drive_ObjectIdentity = ObjectIdentity
raid7Drive = _Raid7Drive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 4)
)
_Raid7NumDrives_Type = Gauge32
_Raid7NumDrives_Object = MibScalar
raid7NumDrives = _Raid7NumDrives_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 4, 1),
    _Raid7NumDrives_Type()
)
raid7NumDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7NumDrives.setStatus("mandatory")
_Raid7NumDataDrives_Type = Gauge32
_Raid7NumDataDrives_Object = MibScalar
raid7NumDataDrives = _Raid7NumDataDrives_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 4, 2),
    _Raid7NumDataDrives_Type()
)
raid7NumDataDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7NumDataDrives.setStatus("mandatory")
_Raid7NumParityDrives_Type = Gauge32
_Raid7NumParityDrives_Object = MibScalar
raid7NumParityDrives = _Raid7NumParityDrives_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 4, 3),
    _Raid7NumParityDrives_Type()
)
raid7NumParityDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7NumParityDrives.setStatus("mandatory")
_Raid7NumStandbyDrives_Type = Gauge32
_Raid7NumStandbyDrives_Object = MibScalar
raid7NumStandbyDrives = _Raid7NumStandbyDrives_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 4, 4),
    _Raid7NumStandbyDrives_Type()
)
raid7NumStandbyDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7NumStandbyDrives.setStatus("mandatory")
_Raid7NumFailedDrives_Type = Gauge32
_Raid7NumFailedDrives_Object = MibScalar
raid7NumFailedDrives = _Raid7NumFailedDrives_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 4, 5),
    _Raid7NumFailedDrives_Type()
)
raid7NumFailedDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7NumFailedDrives.setStatus("mandatory")
_Raid7DriveTable_Object = MibTable
raid7DriveTable = _Raid7DriveTable_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 4, 6)
)
if mibBuilder.loadTexts:
    raid7DriveTable.setStatus("mandatory")
_Raid7DriveEntry_Object = MibTableRow
raid7DriveEntry = _Raid7DriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 4, 6, 1)
)
raid7DriveEntry.setIndexNames(
    (0, "SCC-RAID7-MIB", "raid7DriveNumber"),
)
if mibBuilder.loadTexts:
    raid7DriveEntry.setStatus("mandatory")


class _Raid7DriveNumber_Type(Integer32):
    """Custom type raid7DriveNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_Raid7DriveNumber_Type.__name__ = "Integer32"
_Raid7DriveNumber_Object = MibTableColumn
raid7DriveNumber = _Raid7DriveNumber_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 4, 6, 1, 1),
    _Raid7DriveNumber_Type()
)
raid7DriveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7DriveNumber.setStatus("mandatory")


class _Raid7DriveState_Type(Integer32):
    """Custom type raid7DriveState based on Integer32"""
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
        *(("data", 1),
          ("dataAndParity", 7),
          ("failed", 6),
          ("parity", 2),
          ("rebuilding", 4),
          ("reformatting", 5),
          ("standby", 3),
          ("unknown", 8))
    )


_Raid7DriveState_Type.__name__ = "Integer32"
_Raid7DriveState_Object = MibTableColumn
raid7DriveState = _Raid7DriveState_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 4, 6, 1, 2),
    _Raid7DriveState_Type()
)
raid7DriveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7DriveState.setStatus("mandatory")


class _Raid7DriveActivity_Type(DisplayString):
    """Custom type raid7DriveActivity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Raid7DriveActivity_Type.__name__ = "DisplayString"
_Raid7DriveActivity_Object = MibTableColumn
raid7DriveActivity = _Raid7DriveActivity_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 4, 6, 1, 3),
    _Raid7DriveActivity_Type()
)
raid7DriveActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7DriveActivity.setStatus("mandatory")
_Raid7DriveWrites_Type = Counter32
_Raid7DriveWrites_Object = MibTableColumn
raid7DriveWrites = _Raid7DriveWrites_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 4, 6, 1, 4),
    _Raid7DriveWrites_Type()
)
raid7DriveWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7DriveWrites.setStatus("mandatory")
_Raid7DriveReads_Type = Counter32
_Raid7DriveReads_Object = MibTableColumn
raid7DriveReads = _Raid7DriveReads_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 4, 6, 1, 5),
    _Raid7DriveReads_Type()
)
raid7DriveReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7DriveReads.setStatus("mandatory")
_Raid7DriveTimeOuts_Type = Counter32
_Raid7DriveTimeOuts_Object = MibTableColumn
raid7DriveTimeOuts = _Raid7DriveTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 4, 6, 1, 6),
    _Raid7DriveTimeOuts_Type()
)
raid7DriveTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7DriveTimeOuts.setStatus("mandatory")
_Raid7DriveErrors_Type = Counter32
_Raid7DriveErrors_Object = MibTableColumn
raid7DriveErrors = _Raid7DriveErrors_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 4, 6, 1, 7),
    _Raid7DriveErrors_Type()
)
raid7DriveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7DriveErrors.setStatus("mandatory")
_Raid7Env_ObjectIdentity = ObjectIdentity
raid7Env = _Raid7Env_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 5)
)


class _Raid7EnvironmentStatus_Type(Integer32):
    """Custom type raid7EnvironmentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("operational", 1))
    )


_Raid7EnvironmentStatus_Type.__name__ = "Integer32"
_Raid7EnvironmentStatus_Object = MibScalar
raid7EnvironmentStatus = _Raid7EnvironmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 5, 1),
    _Raid7EnvironmentStatus_Type()
)
raid7EnvironmentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raid7EnvironmentStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

raid7DriveUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 0, 1)
)
raid7DriveUp.setObjects(
      *(("SCC-RAID7-MIB", "raid7DriveNumber"),
        ("SCC-RAID7-MIB", "raid7DriveState"))
)
if mibBuilder.loadTexts:
    raid7DriveUp.setStatus(
        ""
    )

raid7DriveDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 0, 2)
)
raid7DriveDown.setObjects(
      *(("SCC-RAID7-MIB", "raid7DriveNumber"),
        ("SCC-RAID7-MIB", "raid7DriveState"))
)
if mibBuilder.loadTexts:
    raid7DriveDown.setStatus(
        ""
    )

raid7EnvironmentFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1386, 2, 1, 0, 3)
)
raid7EnvironmentFailure.setObjects(
    ("SCC-RAID7-MIB", "raid7EnvironmentStatus")
)
if mibBuilder.loadTexts:
    raid7EnvironmentFailure.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCC-RAID7-MIB",
    **{"raid7DriveUp": raid7DriveUp,
       "raid7DriveDown": raid7DriveDown,
       "raid7EnvironmentFailure": raid7EnvironmentFailure,
       "raid7Sys": raid7Sys,
       "raid7SysVersion": raid7SysVersion,
       "raid7Memory": raid7Memory,
       "raid7TotalMem": raid7TotalMem,
       "raid7GoodMem": raid7GoodMem,
       "raid7MemAvail": raid7MemAvail,
       "raid7CacheHitPercent": raid7CacheHitPercent,
       "raid7BlockTable": raid7BlockTable,
       "raid7BlockEntry": raid7BlockEntry,
       "raid7BlockSize": raid7BlockSize,
       "raid7NumBlocks": raid7NumBlocks,
       "raid7Host": raid7Host,
       "raid7NumHostChannels": raid7NumHostChannels,
       "raid7ChannelTable": raid7ChannelTable,
       "raid7ChannelEntry": raid7ChannelEntry,
       "raid7ChannelNumber": raid7ChannelNumber,
       "raid7ChannelTransferRate": raid7ChannelTransferRate,
       "raid7ChannelTransactionRate": raid7ChannelTransactionRate,
       "raid7ChannelErrorMsgs": raid7ChannelErrorMsgs,
       "raid7ChannelLastKey": raid7ChannelLastKey,
       "raid7ChannelLastSense": raid7ChannelLastSense,
       "raid7Drive": raid7Drive,
       "raid7NumDrives": raid7NumDrives,
       "raid7NumDataDrives": raid7NumDataDrives,
       "raid7NumParityDrives": raid7NumParityDrives,
       "raid7NumStandbyDrives": raid7NumStandbyDrives,
       "raid7NumFailedDrives": raid7NumFailedDrives,
       "raid7DriveTable": raid7DriveTable,
       "raid7DriveEntry": raid7DriveEntry,
       "raid7DriveNumber": raid7DriveNumber,
       "raid7DriveState": raid7DriveState,
       "raid7DriveActivity": raid7DriveActivity,
       "raid7DriveWrites": raid7DriveWrites,
       "raid7DriveReads": raid7DriveReads,
       "raid7DriveTimeOuts": raid7DriveTimeOuts,
       "raid7DriveErrors": raid7DriveErrors,
       "raid7Env": raid7Env,
       "raid7EnvironmentStatus": raid7EnvironmentStatus}
)
