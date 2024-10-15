# SNMP MIB module (KYOCERA-Private-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/KYOCERA-Private-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:43 2024
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

(hrDeviceIndex,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "hrDeviceIndex")

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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Kyocera_ObjectIdentity = ObjectIdentity
kyocera = _Kyocera_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347)
)
_KcPrinter_ObjectIdentity = ObjectIdentity
kcPrinter = _KcPrinter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 43)
)
_KcprtGeneral_ObjectIdentity = ObjectIdentity
kcprtGeneral = _KcprtGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5)
)
_KcprtGeneralTable_Object = MibTable
kcprtGeneralTable = _KcprtGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1)
)
if mibBuilder.loadTexts:
    kcprtGeneralTable.setStatus("mandatory")
_KcprtGeneralEntry_Object = MibTableRow
kcprtGeneralEntry = _KcprtGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1)
)
kcprtGeneralEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    kcprtGeneralEntry.setStatus("mandatory")


class _KcprtGeneralModelName_Type(DisplayString):
    """Custom type kcprtGeneralModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_KcprtGeneralModelName_Type.__name__ = "DisplayString"
_KcprtGeneralModelName_Object = MibTableColumn
kcprtGeneralModelName = _KcprtGeneralModelName_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 1),
    _KcprtGeneralModelName_Type()
)
kcprtGeneralModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtGeneralModelName.setStatus("mandatory")


class _KcprtOptionDescription_Type(DisplayString):
    """Custom type kcprtOptionDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_KcprtOptionDescription_Type.__name__ = "DisplayString"
_KcprtOptionDescription_Object = MibScalar
kcprtOptionDescription = _KcprtOptionDescription_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 2),
    _KcprtOptionDescription_Type()
)
kcprtOptionDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtOptionDescription.setStatus("mandatory")


class _KcprtKpdlLevel_Type(Integer32):
    """Custom type kcprtKpdlLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_KcprtKpdlLevel_Type.__name__ = "Integer32"
_KcprtKpdlLevel_Object = MibTableColumn
kcprtKpdlLevel = _KcprtKpdlLevel_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 3),
    _KcprtKpdlLevel_Type()
)
kcprtKpdlLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtKpdlLevel.setStatus("mandatory")


class _KcprtSystemUpTime_Type(Integer32):
    """Custom type kcprtSystemUpTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KcprtSystemUpTime_Type.__name__ = "Integer32"
_KcprtSystemUpTime_Object = MibTableColumn
kcprtSystemUpTime = _KcprtSystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 4),
    _KcprtSystemUpTime_Type()
)
kcprtSystemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSystemUpTime.setStatus("mandatory")


class _KcprtBinNumber_Type(Integer32):
    """Custom type kcprtBinNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_KcprtBinNumber_Type.__name__ = "Integer32"
_KcprtBinNumber_Object = MibTableColumn
kcprtBinNumber = _KcprtBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 5),
    _KcprtBinNumber_Type()
)
kcprtBinNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtBinNumber.setStatus("mandatory")


class _KcprtCardSlotCapacity_Type(Integer32):
    """Custom type kcprtCardSlotCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_KcprtCardSlotCapacity_Type.__name__ = "Integer32"
_KcprtCardSlotCapacity_Object = MibTableColumn
kcprtCardSlotCapacity = _KcprtCardSlotCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 6),
    _KcprtCardSlotCapacity_Type()
)
kcprtCardSlotCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtCardSlotCapacity.setStatus("mandatory")


class _KcprtRomSlotCapacity_Type(Integer32):
    """Custom type kcprtRomSlotCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_KcprtRomSlotCapacity_Type.__name__ = "Integer32"
_KcprtRomSlotCapacity_Object = MibTableColumn
kcprtRomSlotCapacity = _KcprtRomSlotCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 7),
    _KcprtRomSlotCapacity_Type()
)
kcprtRomSlotCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtRomSlotCapacity.setStatus("mandatory")


class _KcprtSimmSlotCapacity_Type(Integer32):
    """Custom type kcprtSimmSlotCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_KcprtSimmSlotCapacity_Type.__name__ = "Integer32"
_KcprtSimmSlotCapacity_Object = MibTableColumn
kcprtSimmSlotCapacity = _KcprtSimmSlotCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 8),
    _KcprtSimmSlotCapacity_Type()
)
kcprtSimmSlotCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSimmSlotCapacity.setStatus("mandatory")


class _KcprtSimmSlotUsed_Type(Integer32):
    """Custom type kcprtSimmSlotUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_KcprtSimmSlotUsed_Type.__name__ = "Integer32"
_KcprtSimmSlotUsed_Object = MibTableColumn
kcprtSimmSlotUsed = _KcprtSimmSlotUsed_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 9),
    _KcprtSimmSlotUsed_Type()
)
kcprtSimmSlotUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSimmSlotUsed.setStatus("mandatory")


class _KcprtOriginalMemorySize_Type(Integer32):
    """Custom type kcprtOriginalMemorySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KcprtOriginalMemorySize_Type.__name__ = "Integer32"
_KcprtOriginalMemorySize_Object = MibTableColumn
kcprtOriginalMemorySize = _KcprtOriginalMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 10),
    _KcprtOriginalMemorySize_Type()
)
kcprtOriginalMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtOriginalMemorySize.setStatus("mandatory")


class _KcprtTotalMemorySize_Type(Integer32):
    """Custom type kcprtTotalMemorySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KcprtTotalMemorySize_Type.__name__ = "Integer32"
_KcprtTotalMemorySize_Object = MibTableColumn
kcprtTotalMemorySize = _KcprtTotalMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 11),
    _KcprtTotalMemorySize_Type()
)
kcprtTotalMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtTotalMemorySize.setStatus("mandatory")


class _KcprtUserMemorySize_Type(Integer32):
    """Custom type kcprtUserMemorySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KcprtUserMemorySize_Type.__name__ = "Integer32"
_KcprtUserMemorySize_Object = MibTableColumn
kcprtUserMemorySize = _KcprtUserMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 12),
    _KcprtUserMemorySize_Type()
)
kcprtUserMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtUserMemorySize.setStatus("mandatory")


class _KcprtVirtualMemory_Type(Integer32):
    """Custom type kcprtVirtualMemory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("support", 1))
    )


_KcprtVirtualMemory_Type.__name__ = "Integer32"
_KcprtVirtualMemory_Object = MibTableColumn
kcprtVirtualMemory = _KcprtVirtualMemory_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 13),
    _KcprtVirtualMemory_Type()
)
kcprtVirtualMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtVirtualMemory.setStatus("mandatory")


class _KcprtPageMemorySize_Type(Integer32):
    """Custom type kcprtPageMemorySize based on Integer32"""
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
        *(("size-128KB", 1),
          ("size-256KB", 2),
          ("size-512KB", 3),
          ("size-A4orLetter", 4),
          ("size-Legal", 5),
          ("size-doubleA4orLetter", 6),
          ("size-doubleLegal", 7))
    )


_KcprtPageMemorySize_Type.__name__ = "Integer32"
_KcprtPageMemorySize_Object = MibTableColumn
kcprtPageMemorySize = _KcprtPageMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 14),
    _KcprtPageMemorySize_Type()
)
kcprtPageMemorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtPageMemorySize.setStatus("mandatory")


class _KcprtHostBufferSize_Type(Integer32):
    """Custom type kcprtHostBufferSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_KcprtHostBufferSize_Type.__name__ = "Integer32"
_KcprtHostBufferSize_Object = MibTableColumn
kcprtHostBufferSize = _KcprtHostBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 15),
    _KcprtHostBufferSize_Type()
)
kcprtHostBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtHostBufferSize.setStatus("mandatory")


class _KcprtHostBuffer1stRate_Type(Integer32):
    """Custom type kcprtHostBuffer1stRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_KcprtHostBuffer1stRate_Type.__name__ = "Integer32"
_KcprtHostBuffer1stRate_Object = MibTableColumn
kcprtHostBuffer1stRate = _KcprtHostBuffer1stRate_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 16),
    _KcprtHostBuffer1stRate_Type()
)
kcprtHostBuffer1stRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtHostBuffer1stRate.setStatus("mandatory")


class _KcprtHostBuffer2ndRate_Type(Integer32):
    """Custom type kcprtHostBuffer2ndRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_KcprtHostBuffer2ndRate_Type.__name__ = "Integer32"
_KcprtHostBuffer2ndRate_Object = MibTableColumn
kcprtHostBuffer2ndRate = _KcprtHostBuffer2ndRate_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 17),
    _KcprtHostBuffer2ndRate_Type()
)
kcprtHostBuffer2ndRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtHostBuffer2ndRate.setStatus("mandatory")


class _KcprtHostBuffer3rdRate_Type(Integer32):
    """Custom type kcprtHostBuffer3rdRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_KcprtHostBuffer3rdRate_Type.__name__ = "Integer32"
_KcprtHostBuffer3rdRate_Object = MibTableColumn
kcprtHostBuffer3rdRate = _KcprtHostBuffer3rdRate_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 18),
    _KcprtHostBuffer3rdRate_Type()
)
kcprtHostBuffer3rdRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtHostBuffer3rdRate.setStatus("mandatory")


class _KcprtHostBufferOption_Type(Integer32):
    """Custom type kcprtHostBufferOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 0),
          ("fixed", 1))
    )


_KcprtHostBufferOption_Type.__name__ = "Integer32"
_KcprtHostBufferOption_Object = MibTableColumn
kcprtHostBufferOption = _KcprtHostBufferOption_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 19),
    _KcprtHostBufferOption_Type()
)
kcprtHostBufferOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtHostBufferOption.setStatus("mandatory")


class _KcprtBufferXoffLevel_Type(Integer32):
    """Custom type kcprtBufferXoffLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_KcprtBufferXoffLevel_Type.__name__ = "Integer32"
_KcprtBufferXoffLevel_Object = MibTableColumn
kcprtBufferXoffLevel = _KcprtBufferXoffLevel_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 20),
    _KcprtBufferXoffLevel_Type()
)
kcprtBufferXoffLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtBufferXoffLevel.setStatus("mandatory")


class _KcprtBufferXonLevel_Type(Integer32):
    """Custom type kcprtBufferXonLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_KcprtBufferXonLevel_Type.__name__ = "Integer32"
_KcprtBufferXonLevel_Object = MibTableColumn
kcprtBufferXonLevel = _KcprtBufferXonLevel_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 21),
    _KcprtBufferXonLevel_Type()
)
kcprtBufferXonLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtBufferXonLevel.setStatus("mandatory")


class _KcprtFFTimeout_Type(Integer32):
    """Custom type kcprtFFTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_KcprtFFTimeout_Type.__name__ = "Integer32"
_KcprtFFTimeout_Object = MibTableColumn
kcprtFFTimeout = _KcprtFFTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 22),
    _KcprtFFTimeout_Type()
)
kcprtFFTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtFFTimeout.setStatus("mandatory")


class _KcprtSleepTimer_Type(Integer32):
    """Custom type kcprtSleepTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_KcprtSleepTimer_Type.__name__ = "Integer32"
_KcprtSleepTimer_Object = MibTableColumn
kcprtSleepTimer = _KcprtSleepTimer_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 23),
    _KcprtSleepTimer_Type()
)
kcprtSleepTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtSleepTimer.setStatus("mandatory")


class _KcprtWakeupStatusPage_Type(Integer32):
    """Custom type kcprtWakeupStatusPage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_KcprtWakeupStatusPage_Type.__name__ = "Integer32"
_KcprtWakeupStatusPage_Object = MibTableColumn
kcprtWakeupStatusPage = _KcprtWakeupStatusPage_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 24),
    _KcprtWakeupStatusPage_Type()
)
kcprtWakeupStatusPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtWakeupStatusPage.setStatus("mandatory")


class _KcprtOnlineControl_Type(Integer32):
    """Custom type kcprtOnlineControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("offLine", 0),
          ("onLine", 1))
    )


_KcprtOnlineControl_Type.__name__ = "Integer32"
_KcprtOnlineControl_Object = MibTableColumn
kcprtOnlineControl = _KcprtOnlineControl_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 25),
    _KcprtOnlineControl_Type()
)
kcprtOnlineControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtOnlineControl.setStatus("mandatory")


class _KcprtCopyCount_Type(Integer32):
    """Custom type kcprtCopyCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_KcprtCopyCount_Type.__name__ = "Integer32"
_KcprtCopyCount_Object = MibTableColumn
kcprtCopyCount = _KcprtCopyCount_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 26),
    _KcprtCopyCount_Type()
)
kcprtCopyCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtCopyCount.setStatus("mandatory")
_KcprtCpuTable_Object = MibTable
kcprtCpuTable = _KcprtCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 4)
)
if mibBuilder.loadTexts:
    kcprtCpuTable.setStatus("mandatory")
_KcprtCpuEntry_Object = MibTableRow
kcprtCpuEntry = _KcprtCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 4, 1)
)
kcprtCpuEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-Private-MIB", "kcprtCpuIndex"),
)
if mibBuilder.loadTexts:
    kcprtCpuEntry.setStatus("mandatory")
_KcprtCpuIndex_Type = Integer32
_KcprtCpuIndex_Object = MibTableColumn
kcprtCpuIndex = _KcprtCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 4, 1, 1),
    _KcprtCpuIndex_Type()
)
kcprtCpuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtCpuIndex.setStatus("mandatory")


class _KcprtCpuName_Type(DisplayString):
    """Custom type kcprtCpuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_KcprtCpuName_Type.__name__ = "DisplayString"
_KcprtCpuName_Object = MibTableColumn
kcprtCpuName = _KcprtCpuName_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 4, 1, 2),
    _KcprtCpuName_Type()
)
kcprtCpuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtCpuName.setStatus("mandatory")
_KcprtCpuClock_Type = Integer32
_KcprtCpuClock_Object = MibTableColumn
kcprtCpuClock = _KcprtCpuClock_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 4, 1, 3),
    _KcprtCpuClock_Type()
)
kcprtCpuClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtCpuClock.setStatus("mandatory")


class _KcprtCpuRole_Type(Integer32):
    """Custom type kcprtCpuRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("controller", 1),
          ("engine", 0))
    )


_KcprtCpuRole_Type.__name__ = "Integer32"
_KcprtCpuRole_Object = MibTableColumn
kcprtCpuRole = _KcprtCpuRole_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 4, 1, 4),
    _KcprtCpuRole_Type()
)
kcprtCpuRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtCpuRole.setStatus("mandatory")


class _KcprtFirmwareVersion_Type(DisplayString):
    """Custom type kcprtFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_KcprtFirmwareVersion_Type.__name__ = "DisplayString"
_KcprtFirmwareVersion_Object = MibTableColumn
kcprtFirmwareVersion = _KcprtFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 4, 1, 5),
    _KcprtFirmwareVersion_Type()
)
kcprtFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtFirmwareVersion.setStatus("mandatory")


class _KcprtFirmwareUpdata_Type(Integer32):
    """Custom type kcprtFirmwareUpdata based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 4),
          ("enabled", 3))
    )


_KcprtFirmwareUpdata_Type.__name__ = "Integer32"
_KcprtFirmwareUpdata_Object = MibScalar
kcprtFirmwareUpdata = _KcprtFirmwareUpdata_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 4, 1, 6),
    _KcprtFirmwareUpdata_Type()
)
kcprtFirmwareUpdata.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtFirmwareUpdata.setStatus("mandatory")
_KcprtOutput_ObjectIdentity = ObjectIdentity
kcprtOutput = _KcprtOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9)
)
_KcprtOutputTable_Object = MibTable
kcprtOutputTable = _KcprtOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 1)
)
if mibBuilder.loadTexts:
    kcprtOutputTable.setStatus("mandatory")
_KcprtOutputEntry_Object = MibTableRow
kcprtOutputEntry = _KcprtOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 1, 1)
)
kcprtOutputEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-Private-MIB", "kcprtOutputIndex"),
)
if mibBuilder.loadTexts:
    kcprtOutputEntry.setStatus("mandatory")
_KcprtOutputIndex_Type = Integer32
_KcprtOutputIndex_Object = MibTableColumn
kcprtOutputIndex = _KcprtOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 1, 1, 1),
    _KcprtOutputIndex_Type()
)
kcprtOutputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtOutputIndex.setStatus("mandatory")


class _KcprtOutputMode_Type(Integer32):
    """Custom type kcprtOutputMode based on Integer32"""
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
        *(("collator", 1),
          ("mailbox", 3),
          ("sorter", 0),
          ("stacker", 2))
    )


_KcprtOutputMode_Type.__name__ = "Integer32"
_KcprtOutputMode_Object = MibTableColumn
kcprtOutputMode = _KcprtOutputMode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 1, 1, 2),
    _KcprtOutputMode_Type()
)
kcprtOutputMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtOutputMode.setStatus("mandatory")


class _KcprtOutputMultiMode_Type(Integer32):
    """Custom type kcprtOutputMultiMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("id-specific", 1),
          ("if-specific", 2),
          ("off", 0))
    )


_KcprtOutputMultiMode_Type.__name__ = "Integer32"
_KcprtOutputMultiMode_Object = MibTableColumn
kcprtOutputMultiMode = _KcprtOutputMultiMode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 1, 1, 3),
    _KcprtOutputMultiMode_Type()
)
kcprtOutputMultiMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtOutputMultiMode.setStatus("mandatory")
_KcprtOutputGroupNumber_Type = Integer32
_KcprtOutputGroupNumber_Object = MibTableColumn
kcprtOutputGroupNumber = _KcprtOutputGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 1, 1, 4),
    _KcprtOutputGroupNumber_Type()
)
kcprtOutputGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtOutputGroupNumber.setStatus("mandatory")
_KcprtOutputDefaultGroup_Type = Integer32
_KcprtOutputDefaultGroup_Object = MibTableColumn
kcprtOutputDefaultGroup = _KcprtOutputDefaultGroup_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 1, 1, 5),
    _KcprtOutputDefaultGroup_Type()
)
kcprtOutputDefaultGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtOutputDefaultGroup.setStatus("mandatory")


class _KcprtOutputBulkStatus_Type(Integer32):
    """Custom type kcprtOutputBulkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("notFull", 0))
    )


_KcprtOutputBulkStatus_Type.__name__ = "Integer32"
_KcprtOutputBulkStatus_Object = MibTableColumn
kcprtOutputBulkStatus = _KcprtOutputBulkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 1, 1, 6),
    _KcprtOutputBulkStatus_Type()
)
kcprtOutputBulkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtOutputBulkStatus.setStatus("mandatory")
_KcprtOutputTrayMaxCapacity_Type = Integer32
_KcprtOutputTrayMaxCapacity_Object = MibTableColumn
kcprtOutputTrayMaxCapacity = _KcprtOutputTrayMaxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 1, 1, 7),
    _KcprtOutputTrayMaxCapacity_Type()
)
kcprtOutputTrayMaxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtOutputTrayMaxCapacity.setStatus("mandatory")
_KcprtTrayGroupTable_Object = MibTable
kcprtTrayGroupTable = _KcprtTrayGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 2)
)
if mibBuilder.loadTexts:
    kcprtTrayGroupTable.setStatus("mandatory")
_KcprtTrayGroupEntry_Object = MibTableRow
kcprtTrayGroupEntry = _KcprtTrayGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 2, 1)
)
kcprtTrayGroupEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-Private-MIB", "kcprtOutputIndex"),
    (0, "KYOCERA-Private-MIB", "kcprtTrayGroupIndex"),
)
if mibBuilder.loadTexts:
    kcprtTrayGroupEntry.setStatus("mandatory")
_KcprtTrayGroupIndex_Type = Integer32
_KcprtTrayGroupIndex_Object = MibTableColumn
kcprtTrayGroupIndex = _KcprtTrayGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 2, 1, 1),
    _KcprtTrayGroupIndex_Type()
)
kcprtTrayGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtTrayGroupIndex.setStatus("mandatory")
_KcprtTrayGroupBeginIndex_Type = Integer32
_KcprtTrayGroupBeginIndex_Object = MibTableColumn
kcprtTrayGroupBeginIndex = _KcprtTrayGroupBeginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 2, 1, 2),
    _KcprtTrayGroupBeginIndex_Type()
)
kcprtTrayGroupBeginIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtTrayGroupBeginIndex.setStatus("mandatory")
_KcprtTrayGroupEndIndex_Type = Integer32
_KcprtTrayGroupEndIndex_Object = MibTableColumn
kcprtTrayGroupEndIndex = _KcprtTrayGroupEndIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 2, 1, 3),
    _KcprtTrayGroupEndIndex_Type()
)
kcprtTrayGroupEndIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtTrayGroupEndIndex.setStatus("mandatory")
_KcprtOutputTrayTable_Object = MibTable
kcprtOutputTrayTable = _KcprtOutputTrayTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 3)
)
if mibBuilder.loadTexts:
    kcprtOutputTrayTable.setStatus("mandatory")
_KcprtOutputTrayEntry_Object = MibTableRow
kcprtOutputTrayEntry = _KcprtOutputTrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 3, 1)
)
kcprtOutputTrayEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-Private-MIB", "kcprtOutputIndex"),
    (0, "KYOCERA-Private-MIB", "kcprtOutputTrayIndex"),
)
if mibBuilder.loadTexts:
    kcprtOutputTrayEntry.setStatus("mandatory")
_KcprtOutputTrayIndex_Type = Integer32
_KcprtOutputTrayIndex_Object = MibTableColumn
kcprtOutputTrayIndex = _KcprtOutputTrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 3, 1, 1),
    _KcprtOutputTrayIndex_Type()
)
kcprtOutputTrayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtOutputTrayIndex.setStatus("mandatory")
_KcprtOutputTrayOrder_Type = Integer32
_KcprtOutputTrayOrder_Object = MibTableColumn
kcprtOutputTrayOrder = _KcprtOutputTrayOrder_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 3, 1, 2),
    _KcprtOutputTrayOrder_Type()
)
kcprtOutputTrayOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtOutputTrayOrder.setStatus("mandatory")
_KcprtOutputTrayGroup_Type = Integer32
_KcprtOutputTrayGroup_Object = MibTableColumn
kcprtOutputTrayGroup = _KcprtOutputTrayGroup_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 3, 1, 3),
    _KcprtOutputTrayGroup_Type()
)
kcprtOutputTrayGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtOutputTrayGroup.setStatus("mandatory")
_KcprtOutputTrayCount_Type = Integer32
_KcprtOutputTrayCount_Object = MibTableColumn
kcprtOutputTrayCount = _KcprtOutputTrayCount_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 3, 1, 4),
    _KcprtOutputTrayCount_Type()
)
kcprtOutputTrayCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtOutputTrayCount.setStatus("mandatory")
_KcprtMarker_ObjectIdentity = ObjectIdentity
kcprtMarker = _KcprtMarker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 43, 10)
)
_KcprtMarkerTable_Object = MibTable
kcprtMarkerTable = _KcprtMarkerTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 10, 1)
)
if mibBuilder.loadTexts:
    kcprtMarkerTable.setStatus("mandatory")
_KcprtMarkerEntry_Object = MibTableRow
kcprtMarkerEntry = _KcprtMarkerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 10, 1, 1)
)
kcprtMarkerEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-Private-MIB", "prtMarkerIndex"),
)
if mibBuilder.loadTexts:
    kcprtMarkerEntry.setStatus("mandatory")
_KcprtMarkerIndex_Type = Integer32
_KcprtMarkerIndex_Object = MibTableColumn
kcprtMarkerIndex = _KcprtMarkerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 10, 1, 1, 1),
    _KcprtMarkerIndex_Type()
)
kcprtMarkerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtMarkerIndex.setStatus("mandatory")


class _KcprtMarkerKirLevel_Type(Integer32):
    """Custom type kcprtMarkerKirLevel based on Integer32"""
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
        *(("dark", 3),
          ("light", 1),
          ("medium", 2),
          ("offOrNotSupport", 0))
    )


_KcprtMarkerKirLevel_Type.__name__ = "Integer32"
_KcprtMarkerKirLevel_Object = MibTableColumn
kcprtMarkerKirLevel = _KcprtMarkerKirLevel_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 10, 1, 1, 2),
    _KcprtMarkerKirLevel_Type()
)
kcprtMarkerKirLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtMarkerKirLevel.setStatus("mandatory")


class _KcprtMarkerEcoprintLevel_Type(Integer32):
    """Custom type kcprtMarkerEcoprintLevel based on Integer32"""
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
        *(("dark", 3),
          ("light", 1),
          ("medium", 2),
          ("offOrNotSupport", 0))
    )


_KcprtMarkerEcoprintLevel_Type.__name__ = "Integer32"
_KcprtMarkerEcoprintLevel_Object = MibTableColumn
kcprtMarkerEcoprintLevel = _KcprtMarkerEcoprintLevel_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 10, 1, 1, 3),
    _KcprtMarkerEcoprintLevel_Type()
)
kcprtMarkerEcoprintLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtMarkerEcoprintLevel.setStatus("mandatory")
_KcprtMarkerAddressabilityFeedDirDeclared_Type = Integer32
_KcprtMarkerAddressabilityFeedDirDeclared_Object = MibTableColumn
kcprtMarkerAddressabilityFeedDirDeclared = _KcprtMarkerAddressabilityFeedDirDeclared_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 10, 1, 1, 4),
    _KcprtMarkerAddressabilityFeedDirDeclared_Type()
)
kcprtMarkerAddressabilityFeedDirDeclared.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtMarkerAddressabilityFeedDirDeclared.setStatus("mandatory")
_KcprtMarkerAddressabilityXFeedDirDeclared_Type = Integer32
_KcprtMarkerAddressabilityXFeedDirDeclared_Object = MibTableColumn
kcprtMarkerAddressabilityXFeedDirDeclared = _KcprtMarkerAddressabilityXFeedDirDeclared_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 10, 1, 1, 5),
    _KcprtMarkerAddressabilityXFeedDirDeclared_Type()
)
kcprtMarkerAddressabilityXFeedDirDeclared.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtMarkerAddressabilityXFeedDirDeclared.setStatus("mandatory")
_KcprtMarkerAddressablilityFeedDirChosen_Type = Integer32
_KcprtMarkerAddressablilityFeedDirChosen_Object = MibScalar
kcprtMarkerAddressablilityFeedDirChosen = _KcprtMarkerAddressablilityFeedDirChosen_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 10, 1, 1, 6),
    _KcprtMarkerAddressablilityFeedDirChosen_Type()
)
kcprtMarkerAddressablilityFeedDirChosen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMarkerAddressablilityFeedDirChosen.setStatus("mandatory")
_KcprtMarkerAddressablilityXFeedDirChosen_Type = Integer32
_KcprtMarkerAddressablilityXFeedDirChosen_Object = MibScalar
kcprtMarkerAddressablilityXFeedDirChosen = _KcprtMarkerAddressablilityXFeedDirChosen_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 10, 1, 1, 7),
    _KcprtMarkerAddressablilityXFeedDirChosen_Type()
)
kcprtMarkerAddressablilityXFeedDirChosen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMarkerAddressablilityXFeedDirChosen.setStatus("mandatory")
_KcprtChannel_ObjectIdentity = ObjectIdentity
kcprtChannel = _KcprtChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 43, 14)
)
_KcprtChannelTable_Object = MibTable
kcprtChannelTable = _KcprtChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 14, 1)
)
if mibBuilder.loadTexts:
    kcprtChannelTable.setStatus("mandatory")
_KcprtChannelEntry_Object = MibTableRow
kcprtChannelEntry = _KcprtChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 14, 1, 1)
)
kcprtChannelEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-Private-MIB", "kcprtChannelIndex"),
)
if mibBuilder.loadTexts:
    kcprtChannelEntry.setStatus("mandatory")
_KcprtChannelIndex_Type = Integer32
_KcprtChannelIndex_Object = MibTableColumn
kcprtChannelIndex = _KcprtChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 14, 1, 1, 1),
    _KcprtChannelIndex_Type()
)
kcprtChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtChannelIndex.setStatus("mandatory")


class _KcprtChannelFunction_Type(Integer32):
    """Custom type kcprtChannelFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hexDump", 1),
          ("through", 0))
    )


_KcprtChannelFunction_Type.__name__ = "Integer32"
_KcprtChannelFunction_Object = MibTableColumn
kcprtChannelFunction = _KcprtChannelFunction_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 14, 1, 1, 2),
    _KcprtChannelFunction_Type()
)
kcprtChannelFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtChannelFunction.setStatus("mandatory")
_KcprtMemoryResource_ObjectIdentity = ObjectIdentity
kcprtMemoryResource = _KcprtMemoryResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20)
)
_KcprtMemoryDeviceTable_Object = MibTable
kcprtMemoryDeviceTable = _KcprtMemoryDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 1)
)
if mibBuilder.loadTexts:
    kcprtMemoryDeviceTable.setStatus("mandatory")
_KcprtMemoryDeviceEntry_Object = MibTableRow
kcprtMemoryDeviceEntry = _KcprtMemoryDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 1, 1)
)
kcprtMemoryDeviceEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-Private-MIB", "kcprtMemoryDeviceIndex"),
)
if mibBuilder.loadTexts:
    kcprtMemoryDeviceEntry.setStatus("mandatory")
_KcprtMemoryDeviceIndex_Type = Integer32
_KcprtMemoryDeviceIndex_Object = MibTableColumn
kcprtMemoryDeviceIndex = _KcprtMemoryDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 1, 1, 1),
    _KcprtMemoryDeviceIndex_Type()
)
kcprtMemoryDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtMemoryDeviceIndex.setStatus("mandatory")


class _KcprtMemoryDeviceLocation_Type(Integer32):
    """Custom type kcprtMemoryDeviceLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("downloadArea", 4),
          ("icCardSlot-A", 0),
          ("icCardslot-B", 1),
          ("optionROMsocket", 2),
          ("others", 255),
          ("residentFont", 3))
    )


_KcprtMemoryDeviceLocation_Type.__name__ = "Integer32"
_KcprtMemoryDeviceLocation_Object = MibTableColumn
kcprtMemoryDeviceLocation = _KcprtMemoryDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 1, 1, 2),
    _KcprtMemoryDeviceLocation_Type()
)
kcprtMemoryDeviceLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMemoryDeviceLocation.setStatus("mandatory")


class _KcprtMemoryDeviceType_Type(Integer32):
    """Custom type kcprtMemoryDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("dram", 3),
          ("flash", 1),
          ("others", 255),
          ("rom", 0),
          ("sram", 2))
    )


_KcprtMemoryDeviceType_Type.__name__ = "Integer32"
_KcprtMemoryDeviceType_Object = MibTableColumn
kcprtMemoryDeviceType = _KcprtMemoryDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 1, 1, 3),
    _KcprtMemoryDeviceType_Type()
)
kcprtMemoryDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMemoryDeviceType.setStatus("mandatory")
_KcprtMemoryDeviceTotalSize_Type = Integer32
_KcprtMemoryDeviceTotalSize_Object = MibTableColumn
kcprtMemoryDeviceTotalSize = _KcprtMemoryDeviceTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 1, 1, 4),
    _KcprtMemoryDeviceTotalSize_Type()
)
kcprtMemoryDeviceTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMemoryDeviceTotalSize.setStatus("mandatory")
_KcprtMemoryDeviceUsedSize_Type = Integer32
_KcprtMemoryDeviceUsedSize_Object = MibTableColumn
kcprtMemoryDeviceUsedSize = _KcprtMemoryDeviceUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 1, 1, 5),
    _KcprtMemoryDeviceUsedSize_Type()
)
kcprtMemoryDeviceUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMemoryDeviceUsedSize.setStatus("mandatory")


class _KcprtMemoryDeviceStatus_Type(Integer32):
    """Custom type kcprtMemoryDeviceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("lowBattery", 4),
          ("notAccessible", 2),
          ("readyReadOnly", 1),
          ("readyReadWrite", 0))
    )


_KcprtMemoryDeviceStatus_Type.__name__ = "Integer32"
_KcprtMemoryDeviceStatus_Object = MibTableColumn
kcprtMemoryDeviceStatus = _KcprtMemoryDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 1, 1, 6),
    _KcprtMemoryDeviceStatus_Type()
)
kcprtMemoryDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMemoryDeviceStatus.setStatus("mandatory")
_KcprtPartitionTable_Object = MibTable
kcprtPartitionTable = _KcprtPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 2)
)
if mibBuilder.loadTexts:
    kcprtPartitionTable.setStatus("mandatory")
_KcprtPartitionEntry_Object = MibTableRow
kcprtPartitionEntry = _KcprtPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 2, 1)
)
kcprtPartitionEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-Private-MIB", "kcprtPartitionIndex"),
)
if mibBuilder.loadTexts:
    kcprtPartitionEntry.setStatus("mandatory")
_KcprtPartitionIndex_Type = Integer32
_KcprtPartitionIndex_Object = MibTableColumn
kcprtPartitionIndex = _KcprtPartitionIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 2, 1, 1),
    _KcprtPartitionIndex_Type()
)
kcprtPartitionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtPartitionIndex.setStatus("mandatory")
_KcprtPartitionSize_Type = Integer32
_KcprtPartitionSize_Object = MibTableColumn
kcprtPartitionSize = _KcprtPartitionSize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 2, 1, 2),
    _KcprtPartitionSize_Type()
)
kcprtPartitionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtPartitionSize.setStatus("mandatory")
_KcprtPartitionLocation_Type = Integer32
_KcprtPartitionLocation_Object = MibTableColumn
kcprtPartitionLocation = _KcprtPartitionLocation_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 2, 1, 3),
    _KcprtPartitionLocation_Type()
)
kcprtPartitionLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtPartitionLocation.setStatus("mandatory")


class _KcprtPartitionResourceType_Type(Integer32):
    """Custom type kcprtPartitionResourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("fontData", 7),
          ("hostData", 4),
          ("macro", 3),
          ("messageData", 6),
          ("programData", 5),
          ("void", 0))
    )


_KcprtPartitionResourceType_Type.__name__ = "Integer32"
_KcprtPartitionResourceType_Object = MibTableColumn
kcprtPartitionResourceType = _KcprtPartitionResourceType_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 2, 1, 4),
    _KcprtPartitionResourceType_Type()
)
kcprtPartitionResourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtPartitionResourceType.setStatus("mandatory")


class _KcprtPartitionName_Type(DisplayString):
    """Custom type kcprtPartitionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_KcprtPartitionName_Type.__name__ = "DisplayString"
_KcprtPartitionName_Object = MibTableColumn
kcprtPartitionName = _KcprtPartitionName_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 2, 1, 5),
    _KcprtPartitionName_Type()
)
kcprtPartitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtPartitionName.setStatus("mandatory")


class _KcprtPartitionLoad_Type(Integer32):
    """Custom type kcprtPartitionLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 1),
          ("notLoaded", 0))
    )


_KcprtPartitionLoad_Type.__name__ = "Integer32"
_KcprtPartitionLoad_Object = MibTableColumn
kcprtPartitionLoad = _KcprtPartitionLoad_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 2, 1, 6),
    _KcprtPartitionLoad_Type()
)
kcprtPartitionLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtPartitionLoad.setStatus("mandatory")
_KcprtMacroDataTable_Object = MibTable
kcprtMacroDataTable = _KcprtMacroDataTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 3)
)
if mibBuilder.loadTexts:
    kcprtMacroDataTable.setStatus("mandatory")
_KcprtMacroDataEntry_Object = MibTableRow
kcprtMacroDataEntry = _KcprtMacroDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 3, 1)
)
kcprtMacroDataEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-Private-MIB", "kcprtMacroDataIndex"),
)
if mibBuilder.loadTexts:
    kcprtMacroDataEntry.setStatus("mandatory")
_KcprtMacroDataIndex_Type = Integer32
_KcprtMacroDataIndex_Object = MibTableColumn
kcprtMacroDataIndex = _KcprtMacroDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 3, 1, 1),
    _KcprtMacroDataIndex_Type()
)
kcprtMacroDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtMacroDataIndex.setStatus("mandatory")


class _KcprtMacroDataName_Type(DisplayString):
    """Custom type kcprtMacroDataName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_KcprtMacroDataName_Type.__name__ = "DisplayString"
_KcprtMacroDataName_Object = MibTableColumn
kcprtMacroDataName = _KcprtMacroDataName_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 3, 1, 2),
    _KcprtMacroDataName_Type()
)
kcprtMacroDataName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMacroDataName.setStatus("mandatory")
_KcprtMacroDataID_Type = Integer32
_KcprtMacroDataID_Object = MibTableColumn
kcprtMacroDataID = _KcprtMacroDataID_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 3, 1, 3),
    _KcprtMacroDataID_Type()
)
kcprtMacroDataID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMacroDataID.setStatus("mandatory")


class _KcprtMacroDataType_Type(Integer32):
    """Custom type kcprtMacroDataType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("others", 255),
          ("pcl", 2),
          ("prescribe", 1))
    )


_KcprtMacroDataType_Type.__name__ = "Integer32"
_KcprtMacroDataType_Object = MibTableColumn
kcprtMacroDataType = _KcprtMacroDataType_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 3, 1, 4),
    _KcprtMacroDataType_Type()
)
kcprtMacroDataType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMacroDataType.setStatus("mandatory")


class _KcprtMacroDataAutoLoad_Type(Integer32):
    """Custom type kcprtMacroDataAutoLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("onWithInitialize", 1),
          ("onWithoutInitialize", 2))
    )


_KcprtMacroDataAutoLoad_Type.__name__ = "Integer32"
_KcprtMacroDataAutoLoad_Object = MibTableColumn
kcprtMacroDataAutoLoad = _KcprtMacroDataAutoLoad_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 3, 1, 5),
    _KcprtMacroDataAutoLoad_Type()
)
kcprtMacroDataAutoLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMacroDataAutoLoad.setStatus("mandatory")
_KcprtMacroDataLocation_Type = Integer32
_KcprtMacroDataLocation_Object = MibTableColumn
kcprtMacroDataLocation = _KcprtMacroDataLocation_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 3, 1, 6),
    _KcprtMacroDataLocation_Type()
)
kcprtMacroDataLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMacroDataLocation.setStatus("mandatory")


class _KcprtMacroDataAttribute_Type(Integer32):
    """Custom type kcprtMacroDataAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notRegistered", 0),
          ("registered", 1))
    )


_KcprtMacroDataAttribute_Type.__name__ = "Integer32"
_KcprtMacroDataAttribute_Object = MibTableColumn
kcprtMacroDataAttribute = _KcprtMacroDataAttribute_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 3, 1, 7),
    _KcprtMacroDataAttribute_Type()
)
kcprtMacroDataAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMacroDataAttribute.setStatus("mandatory")
_KcprtHostDataTable_Object = MibTable
kcprtHostDataTable = _KcprtHostDataTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 4)
)
if mibBuilder.loadTexts:
    kcprtHostDataTable.setStatus("mandatory")
_KcprtHostDataEntry_Object = MibTableRow
kcprtHostDataEntry = _KcprtHostDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 4, 1)
)
kcprtHostDataEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-Private-MIB", "kcprtHostDataIndex"),
)
if mibBuilder.loadTexts:
    kcprtHostDataEntry.setStatus("mandatory")
_KcprtHostDataIndex_Type = Integer32
_KcprtHostDataIndex_Object = MibTableColumn
kcprtHostDataIndex = _KcprtHostDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 4, 1, 1),
    _KcprtHostDataIndex_Type()
)
kcprtHostDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtHostDataIndex.setStatus("mandatory")


class _KcprtHostDataName_Type(DisplayString):
    """Custom type kcprtHostDataName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_KcprtHostDataName_Type.__name__ = "DisplayString"
_KcprtHostDataName_Object = MibScalar
kcprtHostDataName = _KcprtHostDataName_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 4, 1, 2),
    _KcprtHostDataName_Type()
)
kcprtHostDataName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtHostDataName.setStatus("mandatory")
_KcprtHostDataLocation_Type = Integer32
_KcprtHostDataLocation_Object = MibTableColumn
kcprtHostDataLocation = _KcprtHostDataLocation_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 4, 1, 3),
    _KcprtHostDataLocation_Type()
)
kcprtHostDataLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtHostDataLocation.setStatus("mandatory")


class _KcprtHostDataAttribute_Type(Integer32):
    """Custom type kcprtHostDataAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notRegistered", 0),
          ("registered", 1))
    )


_KcprtHostDataAttribute_Type.__name__ = "Integer32"
_KcprtHostDataAttribute_Object = MibTableColumn
kcprtHostDataAttribute = _KcprtHostDataAttribute_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 4, 1, 4),
    _KcprtHostDataAttribute_Type()
)
kcprtHostDataAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtHostDataAttribute.setStatus("mandatory")
_KcprtProgramDataTable_Object = MibTable
kcprtProgramDataTable = _KcprtProgramDataTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 5)
)
if mibBuilder.loadTexts:
    kcprtProgramDataTable.setStatus("mandatory")
_KcprtProgramDataEntry_Object = MibTableRow
kcprtProgramDataEntry = _KcprtProgramDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 5, 1)
)
kcprtProgramDataEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-Private-MIB", "kcprtProgramDataIndex"),
)
if mibBuilder.loadTexts:
    kcprtProgramDataEntry.setStatus("mandatory")
_KcprtProgramDataIndex_Type = Integer32
_KcprtProgramDataIndex_Object = MibTableColumn
kcprtProgramDataIndex = _KcprtProgramDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 5, 1, 1),
    _KcprtProgramDataIndex_Type()
)
kcprtProgramDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtProgramDataIndex.setStatus("mandatory")


class _KcprtProgramDataName_Type(DisplayString):
    """Custom type kcprtProgramDataName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_KcprtProgramDataName_Type.__name__ = "DisplayString"
_KcprtProgramDataName_Object = MibTableColumn
kcprtProgramDataName = _KcprtProgramDataName_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 5, 1, 2),
    _KcprtProgramDataName_Type()
)
kcprtProgramDataName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtProgramDataName.setStatus("mandatory")


class _KcprtProgramDataType_Type(Integer32):
    """Custom type kcprtProgramDataType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("emulation", 0),
          ("others", 255),
          ("prescribe", 1))
    )


_KcprtProgramDataType_Type.__name__ = "Integer32"
_KcprtProgramDataType_Object = MibTableColumn
kcprtProgramDataType = _KcprtProgramDataType_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 5, 1, 3),
    _KcprtProgramDataType_Type()
)
kcprtProgramDataType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtProgramDataType.setStatus("mandatory")
_KcprtProgramDataLocation_Type = Integer32
_KcprtProgramDataLocation_Object = MibTableColumn
kcprtProgramDataLocation = _KcprtProgramDataLocation_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 5, 1, 4),
    _KcprtProgramDataLocation_Type()
)
kcprtProgramDataLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtProgramDataLocation.setStatus("mandatory")


class _KcprtProgramDataAttribute_Type(Integer32):
    """Custom type kcprtProgramDataAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRegistered", 0),
          ("registered", 1),
          ("running", 2))
    )


_KcprtProgramDataAttribute_Type.__name__ = "Integer32"
_KcprtProgramDataAttribute_Object = MibTableColumn
kcprtProgramDataAttribute = _KcprtProgramDataAttribute_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 5, 1, 5),
    _KcprtProgramDataAttribute_Type()
)
kcprtProgramDataAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtProgramDataAttribute.setStatus("mandatory")
_KcprtMessageDataTable_Object = MibTable
kcprtMessageDataTable = _KcprtMessageDataTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 6)
)
if mibBuilder.loadTexts:
    kcprtMessageDataTable.setStatus("mandatory")
_KcprtMessageDataEntry_Object = MibTableRow
kcprtMessageDataEntry = _KcprtMessageDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 6, 1)
)
kcprtMessageDataEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-Private-MIB", "kcprtMessageDataIndex"),
)
if mibBuilder.loadTexts:
    kcprtMessageDataEntry.setStatus("mandatory")
_KcprtMessageDataIndex_Type = Integer32
_KcprtMessageDataIndex_Object = MibTableColumn
kcprtMessageDataIndex = _KcprtMessageDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 6, 1, 1),
    _KcprtMessageDataIndex_Type()
)
kcprtMessageDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtMessageDataIndex.setStatus("mandatory")


class _KcprtMessageDataName_Type(DisplayString):
    """Custom type kcprtMessageDataName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_KcprtMessageDataName_Type.__name__ = "DisplayString"
_KcprtMessageDataName_Object = MibTableColumn
kcprtMessageDataName = _KcprtMessageDataName_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 6, 1, 2),
    _KcprtMessageDataName_Type()
)
kcprtMessageDataName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMessageDataName.setStatus("mandatory")
_KcprtMessageDataLocation_Type = Integer32
_KcprtMessageDataLocation_Object = MibTableColumn
kcprtMessageDataLocation = _KcprtMessageDataLocation_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 6, 1, 3),
    _KcprtMessageDataLocation_Type()
)
kcprtMessageDataLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMessageDataLocation.setStatus("mandatory")


class _KcprtMessageDataAttribute_Type(Integer32):
    """Custom type kcprtMessageDataAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notRegistered", 0),
          ("registered", 1))
    )


_KcprtMessageDataAttribute_Type.__name__ = "Integer32"
_KcprtMessageDataAttribute_Object = MibTableColumn
kcprtMessageDataAttribute = _KcprtMessageDataAttribute_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 6, 1, 4),
    _KcprtMessageDataAttribute_Type()
)
kcprtMessageDataAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMessageDataAttribute.setStatus("mandatory")
_KcprtFontDataTable_Object = MibTable
kcprtFontDataTable = _KcprtFontDataTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 7)
)
if mibBuilder.loadTexts:
    kcprtFontDataTable.setStatus("mandatory")
_KcprtFontDataEntry_Object = MibTableRow
kcprtFontDataEntry = _KcprtFontDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 7, 1)
)
kcprtFontDataEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-Private-MIB", "kcprtFontDataIndex"),
)
if mibBuilder.loadTexts:
    kcprtFontDataEntry.setStatus("mandatory")
_KcprtFontDataIndex_Type = Integer32
_KcprtFontDataIndex_Object = MibTableColumn
kcprtFontDataIndex = _KcprtFontDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 7, 1, 1),
    _KcprtFontDataIndex_Type()
)
kcprtFontDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtFontDataIndex.setStatus("mandatory")


class _KcprtTypeFaceName_Type(DisplayString):
    """Custom type kcprtTypeFaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_KcprtTypeFaceName_Type.__name__ = "DisplayString"
_KcprtTypeFaceName_Object = MibTableColumn
kcprtTypeFaceName = _KcprtTypeFaceName_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 7, 1, 2),
    _KcprtTypeFaceName_Type()
)
kcprtTypeFaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtTypeFaceName.setStatus("mandatory")
_KcprtFontID_Type = Integer32
_KcprtFontID_Object = MibTableColumn
kcprtFontID = _KcprtFontID_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 7, 1, 3),
    _KcprtFontID_Type()
)
kcprtFontID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtFontID.setStatus("mandatory")


class _KcprtFontType_Type(Integer32):
    """Custom type kcprtFontType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("bitmap", 0),
          ("others", 255),
          ("scalable", 1))
    )


_KcprtFontType_Type.__name__ = "Integer32"
_KcprtFontType_Object = MibTableColumn
kcprtFontType = _KcprtFontType_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 7, 1, 4),
    _KcprtFontType_Type()
)
kcprtFontType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtFontType.setStatus("mandatory")
_KcprtFontLocation_Type = Integer32
_KcprtFontLocation_Object = MibTableColumn
kcprtFontLocation = _KcprtFontLocation_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 7, 1, 5),
    _KcprtFontLocation_Type()
)
kcprtFontLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtFontLocation.setStatus("mandatory")


class _KcprtFontAttribute_Type(Integer32):
    """Custom type kcprtFontAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notRegistered", 0),
          ("registered", 1))
    )


_KcprtFontAttribute_Type.__name__ = "Integer32"
_KcprtFontAttribute_Object = MibTableColumn
kcprtFontAttribute = _KcprtFontAttribute_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 7, 1, 6),
    _KcprtFontAttribute_Type()
)
kcprtFontAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtFontAttribute.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KYOCERA-Private-MIB",
    **{"kyocera": kyocera,
       "kcPrinter": kcPrinter,
       "kcprtGeneral": kcprtGeneral,
       "kcprtGeneralTable": kcprtGeneralTable,
       "kcprtGeneralEntry": kcprtGeneralEntry,
       "kcprtGeneralModelName": kcprtGeneralModelName,
       "kcprtOptionDescription": kcprtOptionDescription,
       "kcprtKpdlLevel": kcprtKpdlLevel,
       "kcprtSystemUpTime": kcprtSystemUpTime,
       "kcprtBinNumber": kcprtBinNumber,
       "kcprtCardSlotCapacity": kcprtCardSlotCapacity,
       "kcprtRomSlotCapacity": kcprtRomSlotCapacity,
       "kcprtSimmSlotCapacity": kcprtSimmSlotCapacity,
       "kcprtSimmSlotUsed": kcprtSimmSlotUsed,
       "kcprtOriginalMemorySize": kcprtOriginalMemorySize,
       "kcprtTotalMemorySize": kcprtTotalMemorySize,
       "kcprtUserMemorySize": kcprtUserMemorySize,
       "kcprtVirtualMemory": kcprtVirtualMemory,
       "kcprtPageMemorySize": kcprtPageMemorySize,
       "kcprtHostBufferSize": kcprtHostBufferSize,
       "kcprtHostBuffer1stRate": kcprtHostBuffer1stRate,
       "kcprtHostBuffer2ndRate": kcprtHostBuffer2ndRate,
       "kcprtHostBuffer3rdRate": kcprtHostBuffer3rdRate,
       "kcprtHostBufferOption": kcprtHostBufferOption,
       "kcprtBufferXoffLevel": kcprtBufferXoffLevel,
       "kcprtBufferXonLevel": kcprtBufferXonLevel,
       "kcprtFFTimeout": kcprtFFTimeout,
       "kcprtSleepTimer": kcprtSleepTimer,
       "kcprtWakeupStatusPage": kcprtWakeupStatusPage,
       "kcprtOnlineControl": kcprtOnlineControl,
       "kcprtCopyCount": kcprtCopyCount,
       "kcprtCpuTable": kcprtCpuTable,
       "kcprtCpuEntry": kcprtCpuEntry,
       "kcprtCpuIndex": kcprtCpuIndex,
       "kcprtCpuName": kcprtCpuName,
       "kcprtCpuClock": kcprtCpuClock,
       "kcprtCpuRole": kcprtCpuRole,
       "kcprtFirmwareVersion": kcprtFirmwareVersion,
       "kcprtFirmwareUpdata": kcprtFirmwareUpdata,
       "kcprtOutput": kcprtOutput,
       "kcprtOutputTable": kcprtOutputTable,
       "kcprtOutputEntry": kcprtOutputEntry,
       "kcprtOutputIndex": kcprtOutputIndex,
       "kcprtOutputMode": kcprtOutputMode,
       "kcprtOutputMultiMode": kcprtOutputMultiMode,
       "kcprtOutputGroupNumber": kcprtOutputGroupNumber,
       "kcprtOutputDefaultGroup": kcprtOutputDefaultGroup,
       "kcprtOutputBulkStatus": kcprtOutputBulkStatus,
       "kcprtOutputTrayMaxCapacity": kcprtOutputTrayMaxCapacity,
       "kcprtTrayGroupTable": kcprtTrayGroupTable,
       "kcprtTrayGroupEntry": kcprtTrayGroupEntry,
       "kcprtTrayGroupIndex": kcprtTrayGroupIndex,
       "kcprtTrayGroupBeginIndex": kcprtTrayGroupBeginIndex,
       "kcprtTrayGroupEndIndex": kcprtTrayGroupEndIndex,
       "kcprtOutputTrayTable": kcprtOutputTrayTable,
       "kcprtOutputTrayEntry": kcprtOutputTrayEntry,
       "kcprtOutputTrayIndex": kcprtOutputTrayIndex,
       "kcprtOutputTrayOrder": kcprtOutputTrayOrder,
       "kcprtOutputTrayGroup": kcprtOutputTrayGroup,
       "kcprtOutputTrayCount": kcprtOutputTrayCount,
       "kcprtMarker": kcprtMarker,
       "kcprtMarkerTable": kcprtMarkerTable,
       "kcprtMarkerEntry": kcprtMarkerEntry,
       "kcprtMarkerIndex": kcprtMarkerIndex,
       "kcprtMarkerKirLevel": kcprtMarkerKirLevel,
       "kcprtMarkerEcoprintLevel": kcprtMarkerEcoprintLevel,
       "kcprtMarkerAddressabilityFeedDirDeclared": kcprtMarkerAddressabilityFeedDirDeclared,
       "kcprtMarkerAddressabilityXFeedDirDeclared": kcprtMarkerAddressabilityXFeedDirDeclared,
       "kcprtMarkerAddressablilityFeedDirChosen": kcprtMarkerAddressablilityFeedDirChosen,
       "kcprtMarkerAddressablilityXFeedDirChosen": kcprtMarkerAddressablilityXFeedDirChosen,
       "kcprtChannel": kcprtChannel,
       "kcprtChannelTable": kcprtChannelTable,
       "kcprtChannelEntry": kcprtChannelEntry,
       "kcprtChannelIndex": kcprtChannelIndex,
       "kcprtChannelFunction": kcprtChannelFunction,
       "kcprtMemoryResource": kcprtMemoryResource,
       "kcprtMemoryDeviceTable": kcprtMemoryDeviceTable,
       "kcprtMemoryDeviceEntry": kcprtMemoryDeviceEntry,
       "kcprtMemoryDeviceIndex": kcprtMemoryDeviceIndex,
       "kcprtMemoryDeviceLocation": kcprtMemoryDeviceLocation,
       "kcprtMemoryDeviceType": kcprtMemoryDeviceType,
       "kcprtMemoryDeviceTotalSize": kcprtMemoryDeviceTotalSize,
       "kcprtMemoryDeviceUsedSize": kcprtMemoryDeviceUsedSize,
       "kcprtMemoryDeviceStatus": kcprtMemoryDeviceStatus,
       "kcprtPartitionTable": kcprtPartitionTable,
       "kcprtPartitionEntry": kcprtPartitionEntry,
       "kcprtPartitionIndex": kcprtPartitionIndex,
       "kcprtPartitionSize": kcprtPartitionSize,
       "kcprtPartitionLocation": kcprtPartitionLocation,
       "kcprtPartitionResourceType": kcprtPartitionResourceType,
       "kcprtPartitionName": kcprtPartitionName,
       "kcprtPartitionLoad": kcprtPartitionLoad,
       "kcprtMacroDataTable": kcprtMacroDataTable,
       "kcprtMacroDataEntry": kcprtMacroDataEntry,
       "kcprtMacroDataIndex": kcprtMacroDataIndex,
       "kcprtMacroDataName": kcprtMacroDataName,
       "kcprtMacroDataID": kcprtMacroDataID,
       "kcprtMacroDataType": kcprtMacroDataType,
       "kcprtMacroDataAutoLoad": kcprtMacroDataAutoLoad,
       "kcprtMacroDataLocation": kcprtMacroDataLocation,
       "kcprtMacroDataAttribute": kcprtMacroDataAttribute,
       "kcprtHostDataTable": kcprtHostDataTable,
       "kcprtHostDataEntry": kcprtHostDataEntry,
       "kcprtHostDataIndex": kcprtHostDataIndex,
       "kcprtHostDataName": kcprtHostDataName,
       "kcprtHostDataLocation": kcprtHostDataLocation,
       "kcprtHostDataAttribute": kcprtHostDataAttribute,
       "kcprtProgramDataTable": kcprtProgramDataTable,
       "kcprtProgramDataEntry": kcprtProgramDataEntry,
       "kcprtProgramDataIndex": kcprtProgramDataIndex,
       "kcprtProgramDataName": kcprtProgramDataName,
       "kcprtProgramDataType": kcprtProgramDataType,
       "kcprtProgramDataLocation": kcprtProgramDataLocation,
       "kcprtProgramDataAttribute": kcprtProgramDataAttribute,
       "kcprtMessageDataTable": kcprtMessageDataTable,
       "kcprtMessageDataEntry": kcprtMessageDataEntry,
       "kcprtMessageDataIndex": kcprtMessageDataIndex,
       "kcprtMessageDataName": kcprtMessageDataName,
       "kcprtMessageDataLocation": kcprtMessageDataLocation,
       "kcprtMessageDataAttribute": kcprtMessageDataAttribute,
       "kcprtFontDataTable": kcprtFontDataTable,
       "kcprtFontDataEntry": kcprtFontDataEntry,
       "kcprtFontDataIndex": kcprtFontDataIndex,
       "kcprtTypeFaceName": kcprtTypeFaceName,
       "kcprtFontID": kcprtFontID,
       "kcprtFontType": kcprtFontType,
       "kcprtFontLocation": kcprtFontLocation,
       "kcprtFontAttribute": kcprtFontAttribute}
)
