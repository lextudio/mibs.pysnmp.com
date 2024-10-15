# SNMP MIB module (ELTEX-MCCP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MCCP
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:19 2024
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

(elHardware,) = mibBuilder.importSymbols(
    "ELTEX-SMI",
    "elHardware")

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
 TextualConvention,
 TimeInterval,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp")


# MODULE-IDENTITY

mccp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MccpLogHumanState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleanUp", 2),
          ("turnOff", 0),
          ("turnOn", 1))
    )



class MccpCdrFileFlushStatusType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("active", 1)
    )



# MIB Managed Objects in the order of their OIDs



class _MccpDevName_Type(DisplayString):
    """Custom type mccpDevName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MccpDevName_Type.__name__ = "DisplayString"
_MccpDevName_Object = MibScalar
mccpDevName = _MccpDevName_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 1),
    _MccpDevName_Type()
)
mccpDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpDevName.setStatus("current")
_MccpDevType_Type = Integer32
_MccpDevType_Object = MibScalar
mccpDevType = _MccpDevType_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 2),
    _MccpDevType_Type()
)
mccpDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpDevType.setStatus("current")


class _MccpDevCfgBuild_Type(DisplayString):
    """Custom type mccpDevCfgBuild based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MccpDevCfgBuild_Type.__name__ = "DisplayString"
_MccpDevCfgBuild_Object = MibScalar
mccpDevCfgBuild = _MccpDevCfgBuild_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 3),
    _MccpDevCfgBuild_Type()
)
mccpDevCfgBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpDevCfgBuild.setStatus("current")


class _MccpDevCfgSyncSource_Type(DisplayString):
    """Custom type mccpDevCfgSyncSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MccpDevCfgSyncSource_Type.__name__ = "DisplayString"
_MccpDevCfgSyncSource_Object = MibScalar
mccpDevCfgSyncSource = _MccpDevCfgSyncSource_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 4),
    _MccpDevCfgSyncSource_Type()
)
mccpDevCfgSyncSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpDevCfgSyncSource.setStatus("current")
_MccpGlobalAlarm_Type = Integer32
_MccpGlobalAlarm_Object = MibScalar
mccpGlobalAlarm = _MccpGlobalAlarm_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 5),
    _MccpGlobalAlarm_Type()
)
mccpGlobalAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpGlobalAlarm.setStatus("current")
_MccpJournalQuery_Type = Integer32
_MccpJournalQuery_Object = MibScalar
mccpJournalQuery = _MccpJournalQuery_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 6),
    _MccpJournalQuery_Type()
)
mccpJournalQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpJournalQuery.setStatus("current")
_MccpMasterMode_Type = Integer32
_MccpMasterMode_Object = MibScalar
mccpMasterMode = _MccpMasterMode_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 7),
    _MccpMasterMode_Type()
)
mccpMasterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpMasterMode.setStatus("current")
_MccpFreeSpace_Type = Integer32
_MccpFreeSpace_Object = MibScalar
mccpFreeSpace = _MccpFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 8),
    _MccpFreeSpace_Type()
)
mccpFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpFreeSpace.setStatus("current")
_MccpFreeRam_Type = Integer32
_MccpFreeRam_Object = MibScalar
mccpFreeRam = _MccpFreeRam_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 9),
    _MccpFreeRam_Type()
)
mccpFreeRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpFreeRam.setStatus("current")
_MccpTgStatInTable_Object = MibTable
mccpTgStatInTable = _MccpTgStatInTable_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 10)
)
if mibBuilder.loadTexts:
    mccpTgStatInTable.setStatus("current")
_MccpTgStatInEntry_Object = MibTableRow
mccpTgStatInEntry = _MccpTgStatInEntry_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 10, 1)
)
mccpTgStatInEntry.setIndexNames(
    (0, "ELTEX-MCCP", "mccpTgInIndex"),
)
if mibBuilder.loadTexts:
    mccpTgStatInEntry.setStatus("current")


class _MccpTgInIndex_Type(Integer32):
    """Custom type mccpTgInIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MccpTgInIndex_Type.__name__ = "Integer32"
_MccpTgInIndex_Object = MibTableColumn
mccpTgInIndex = _MccpTgInIndex_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 10, 1, 1),
    _MccpTgInIndex_Type()
)
mccpTgInIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mccpTgInIndex.setStatus("current")


class _MccpTgInId_Type(Integer32):
    """Custom type mccpTgInId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MccpTgInId_Type.__name__ = "Integer32"
_MccpTgInId_Object = MibTableColumn
mccpTgInId = _MccpTgInId_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 10, 1, 2),
    _MccpTgInId_Type()
)
mccpTgInId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgInId.setStatus("current")


class _MccpTgInCounter0_Type(Integer32):
    """Custom type mccpTgInCounter0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgInCounter0_Type.__name__ = "Integer32"
_MccpTgInCounter0_Object = MibTableColumn
mccpTgInCounter0 = _MccpTgInCounter0_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 10, 1, 3),
    _MccpTgInCounter0_Type()
)
mccpTgInCounter0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgInCounter0.setStatus("current")


class _MccpTgInCounter1_Type(Integer32):
    """Custom type mccpTgInCounter1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgInCounter1_Type.__name__ = "Integer32"
_MccpTgInCounter1_Object = MibTableColumn
mccpTgInCounter1 = _MccpTgInCounter1_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 10, 1, 4),
    _MccpTgInCounter1_Type()
)
mccpTgInCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgInCounter1.setStatus("current")


class _MccpTgInCounter2_Type(Integer32):
    """Custom type mccpTgInCounter2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgInCounter2_Type.__name__ = "Integer32"
_MccpTgInCounter2_Object = MibTableColumn
mccpTgInCounter2 = _MccpTgInCounter2_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 10, 1, 5),
    _MccpTgInCounter2_Type()
)
mccpTgInCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgInCounter2.setStatus("current")


class _MccpTgInCounter3_Type(Integer32):
    """Custom type mccpTgInCounter3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgInCounter3_Type.__name__ = "Integer32"
_MccpTgInCounter3_Object = MibTableColumn
mccpTgInCounter3 = _MccpTgInCounter3_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 10, 1, 6),
    _MccpTgInCounter3_Type()
)
mccpTgInCounter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgInCounter3.setStatus("current")


class _MccpTgInCounter4_Type(Integer32):
    """Custom type mccpTgInCounter4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgInCounter4_Type.__name__ = "Integer32"
_MccpTgInCounter4_Object = MibTableColumn
mccpTgInCounter4 = _MccpTgInCounter4_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 10, 1, 7),
    _MccpTgInCounter4_Type()
)
mccpTgInCounter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgInCounter4.setStatus("current")


class _MccpTgInCounter5_Type(Integer32):
    """Custom type mccpTgInCounter5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgInCounter5_Type.__name__ = "Integer32"
_MccpTgInCounter5_Object = MibTableColumn
mccpTgInCounter5 = _MccpTgInCounter5_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 10, 1, 8),
    _MccpTgInCounter5_Type()
)
mccpTgInCounter5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgInCounter5.setStatus("current")


class _MccpTgInCounter6_Type(Integer32):
    """Custom type mccpTgInCounter6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgInCounter6_Type.__name__ = "Integer32"
_MccpTgInCounter6_Object = MibTableColumn
mccpTgInCounter6 = _MccpTgInCounter6_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 10, 1, 9),
    _MccpTgInCounter6_Type()
)
mccpTgInCounter6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgInCounter6.setStatus("current")


class _MccpTgInCounter7_Type(Integer32):
    """Custom type mccpTgInCounter7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgInCounter7_Type.__name__ = "Integer32"
_MccpTgInCounter7_Object = MibTableColumn
mccpTgInCounter7 = _MccpTgInCounter7_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 10, 1, 10),
    _MccpTgInCounter7_Type()
)
mccpTgInCounter7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgInCounter7.setStatus("current")


class _MccpTgInCounter8_Type(Integer32):
    """Custom type mccpTgInCounter8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgInCounter8_Type.__name__ = "Integer32"
_MccpTgInCounter8_Object = MibTableColumn
mccpTgInCounter8 = _MccpTgInCounter8_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 10, 1, 11),
    _MccpTgInCounter8_Type()
)
mccpTgInCounter8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgInCounter8.setStatus("current")


class _MccpTgInCounter9_Type(Integer32):
    """Custom type mccpTgInCounter9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgInCounter9_Type.__name__ = "Integer32"
_MccpTgInCounter9_Object = MibTableColumn
mccpTgInCounter9 = _MccpTgInCounter9_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 10, 1, 12),
    _MccpTgInCounter9_Type()
)
mccpTgInCounter9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgInCounter9.setStatus("current")


class _MccpTgInCounter10_Type(Integer32):
    """Custom type mccpTgInCounter10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgInCounter10_Type.__name__ = "Integer32"
_MccpTgInCounter10_Object = MibTableColumn
mccpTgInCounter10 = _MccpTgInCounter10_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 10, 1, 13),
    _MccpTgInCounter10_Type()
)
mccpTgInCounter10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgInCounter10.setStatus("current")
_MccpTgStatOutTable_Object = MibTable
mccpTgStatOutTable = _MccpTgStatOutTable_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 11)
)
if mibBuilder.loadTexts:
    mccpTgStatOutTable.setStatus("current")
_MccpTgStatOutEntry_Object = MibTableRow
mccpTgStatOutEntry = _MccpTgStatOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 11, 1)
)
mccpTgStatOutEntry.setIndexNames(
    (0, "ELTEX-MCCP", "mccpTgOutIndex"),
)
if mibBuilder.loadTexts:
    mccpTgStatOutEntry.setStatus("current")


class _MccpTgOutIndex_Type(Integer32):
    """Custom type mccpTgOutIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MccpTgOutIndex_Type.__name__ = "Integer32"
_MccpTgOutIndex_Object = MibTableColumn
mccpTgOutIndex = _MccpTgOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 11, 1, 1),
    _MccpTgOutIndex_Type()
)
mccpTgOutIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mccpTgOutIndex.setStatus("current")


class _MccpTgOutId_Type(Integer32):
    """Custom type mccpTgOutId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MccpTgOutId_Type.__name__ = "Integer32"
_MccpTgOutId_Object = MibTableColumn
mccpTgOutId = _MccpTgOutId_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 11, 1, 2),
    _MccpTgOutId_Type()
)
mccpTgOutId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgOutId.setStatus("current")


class _MccpTgOutCounter0_Type(Integer32):
    """Custom type mccpTgOutCounter0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgOutCounter0_Type.__name__ = "Integer32"
_MccpTgOutCounter0_Object = MibTableColumn
mccpTgOutCounter0 = _MccpTgOutCounter0_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 11, 1, 3),
    _MccpTgOutCounter0_Type()
)
mccpTgOutCounter0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgOutCounter0.setStatus("current")


class _MccpTgOutCounter1_Type(Integer32):
    """Custom type mccpTgOutCounter1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgOutCounter1_Type.__name__ = "Integer32"
_MccpTgOutCounter1_Object = MibTableColumn
mccpTgOutCounter1 = _MccpTgOutCounter1_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 11, 1, 4),
    _MccpTgOutCounter1_Type()
)
mccpTgOutCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgOutCounter1.setStatus("current")


class _MccpTgOutCounter2_Type(Integer32):
    """Custom type mccpTgOutCounter2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgOutCounter2_Type.__name__ = "Integer32"
_MccpTgOutCounter2_Object = MibTableColumn
mccpTgOutCounter2 = _MccpTgOutCounter2_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 11, 1, 5),
    _MccpTgOutCounter2_Type()
)
mccpTgOutCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgOutCounter2.setStatus("current")


class _MccpTgOutCounter3_Type(Integer32):
    """Custom type mccpTgOutCounter3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgOutCounter3_Type.__name__ = "Integer32"
_MccpTgOutCounter3_Object = MibTableColumn
mccpTgOutCounter3 = _MccpTgOutCounter3_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 11, 1, 6),
    _MccpTgOutCounter3_Type()
)
mccpTgOutCounter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgOutCounter3.setStatus("current")


class _MccpTgOutCounter4_Type(Integer32):
    """Custom type mccpTgOutCounter4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgOutCounter4_Type.__name__ = "Integer32"
_MccpTgOutCounter4_Object = MibTableColumn
mccpTgOutCounter4 = _MccpTgOutCounter4_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 11, 1, 7),
    _MccpTgOutCounter4_Type()
)
mccpTgOutCounter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgOutCounter4.setStatus("current")


class _MccpTgOutCounter5_Type(Integer32):
    """Custom type mccpTgOutCounter5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgOutCounter5_Type.__name__ = "Integer32"
_MccpTgOutCounter5_Object = MibTableColumn
mccpTgOutCounter5 = _MccpTgOutCounter5_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 11, 1, 8),
    _MccpTgOutCounter5_Type()
)
mccpTgOutCounter5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgOutCounter5.setStatus("current")


class _MccpTgOutCounter6_Type(Integer32):
    """Custom type mccpTgOutCounter6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgOutCounter6_Type.__name__ = "Integer32"
_MccpTgOutCounter6_Object = MibTableColumn
mccpTgOutCounter6 = _MccpTgOutCounter6_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 11, 1, 9),
    _MccpTgOutCounter6_Type()
)
mccpTgOutCounter6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgOutCounter6.setStatus("current")


class _MccpTgOutCounter7_Type(Integer32):
    """Custom type mccpTgOutCounter7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgOutCounter7_Type.__name__ = "Integer32"
_MccpTgOutCounter7_Object = MibTableColumn
mccpTgOutCounter7 = _MccpTgOutCounter7_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 11, 1, 10),
    _MccpTgOutCounter7_Type()
)
mccpTgOutCounter7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgOutCounter7.setStatus("current")


class _MccpTgOutCounter8_Type(Integer32):
    """Custom type mccpTgOutCounter8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgOutCounter8_Type.__name__ = "Integer32"
_MccpTgOutCounter8_Object = MibTableColumn
mccpTgOutCounter8 = _MccpTgOutCounter8_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 11, 1, 11),
    _MccpTgOutCounter8_Type()
)
mccpTgOutCounter8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgOutCounter8.setStatus("current")


class _MccpTgOutCounter9_Type(Integer32):
    """Custom type mccpTgOutCounter9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgOutCounter9_Type.__name__ = "Integer32"
_MccpTgOutCounter9_Object = MibTableColumn
mccpTgOutCounter9 = _MccpTgOutCounter9_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 11, 1, 12),
    _MccpTgOutCounter9_Type()
)
mccpTgOutCounter9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgOutCounter9.setStatus("current")


class _MccpTgOutCounter10_Type(Integer32):
    """Custom type mccpTgOutCounter10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgOutCounter10_Type.__name__ = "Integer32"
_MccpTgOutCounter10_Object = MibTableColumn
mccpTgOutCounter10 = _MccpTgOutCounter10_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 11, 1, 13),
    _MccpTgOutCounter10_Type()
)
mccpTgOutCounter10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgOutCounter10.setStatus("current")
_MccpTgStatTrInTable_Object = MibTable
mccpTgStatTrInTable = _MccpTgStatTrInTable_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 12)
)
if mibBuilder.loadTexts:
    mccpTgStatTrInTable.setStatus("current")
_MccpTgStatTrInEntry_Object = MibTableRow
mccpTgStatTrInEntry = _MccpTgStatTrInEntry_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 12, 1)
)
mccpTgStatTrInEntry.setIndexNames(
    (0, "ELTEX-MCCP", "mccpTgTrInIndex"),
)
if mibBuilder.loadTexts:
    mccpTgStatTrInEntry.setStatus("current")


class _MccpTgTrInIndex_Type(Integer32):
    """Custom type mccpTgTrInIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MccpTgTrInIndex_Type.__name__ = "Integer32"
_MccpTgTrInIndex_Object = MibTableColumn
mccpTgTrInIndex = _MccpTgTrInIndex_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 12, 1, 1),
    _MccpTgTrInIndex_Type()
)
mccpTgTrInIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mccpTgTrInIndex.setStatus("current")


class _MccpTgTrInId_Type(Integer32):
    """Custom type mccpTgTrInId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MccpTgTrInId_Type.__name__ = "Integer32"
_MccpTgTrInId_Object = MibTableColumn
mccpTgTrInId = _MccpTgTrInId_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 12, 1, 2),
    _MccpTgTrInId_Type()
)
mccpTgTrInId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgTrInId.setStatus("current")


class _MccpTgTrInCounter0_Type(Integer32):
    """Custom type mccpTgTrInCounter0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgTrInCounter0_Type.__name__ = "Integer32"
_MccpTgTrInCounter0_Object = MibTableColumn
mccpTgTrInCounter0 = _MccpTgTrInCounter0_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 12, 1, 3),
    _MccpTgTrInCounter0_Type()
)
mccpTgTrInCounter0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgTrInCounter0.setStatus("current")


class _MccpTgTrInCounter1_Type(Integer32):
    """Custom type mccpTgTrInCounter1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgTrInCounter1_Type.__name__ = "Integer32"
_MccpTgTrInCounter1_Object = MibTableColumn
mccpTgTrInCounter1 = _MccpTgTrInCounter1_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 12, 1, 4),
    _MccpTgTrInCounter1_Type()
)
mccpTgTrInCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgTrInCounter1.setStatus("current")


class _MccpTgTrInCounter2_Type(Integer32):
    """Custom type mccpTgTrInCounter2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgTrInCounter2_Type.__name__ = "Integer32"
_MccpTgTrInCounter2_Object = MibTableColumn
mccpTgTrInCounter2 = _MccpTgTrInCounter2_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 12, 1, 5),
    _MccpTgTrInCounter2_Type()
)
mccpTgTrInCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgTrInCounter2.setStatus("current")


class _MccpTgTrInCounter3_Type(Integer32):
    """Custom type mccpTgTrInCounter3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgTrInCounter3_Type.__name__ = "Integer32"
_MccpTgTrInCounter3_Object = MibTableColumn
mccpTgTrInCounter3 = _MccpTgTrInCounter3_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 12, 1, 6),
    _MccpTgTrInCounter3_Type()
)
mccpTgTrInCounter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgTrInCounter3.setStatus("current")


class _MccpTgTrInCounter4_Type(Integer32):
    """Custom type mccpTgTrInCounter4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgTrInCounter4_Type.__name__ = "Integer32"
_MccpTgTrInCounter4_Object = MibTableColumn
mccpTgTrInCounter4 = _MccpTgTrInCounter4_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 12, 1, 7),
    _MccpTgTrInCounter4_Type()
)
mccpTgTrInCounter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgTrInCounter4.setStatus("current")


class _MccpTgTrInCounter5_Type(Integer32):
    """Custom type mccpTgTrInCounter5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgTrInCounter5_Type.__name__ = "Integer32"
_MccpTgTrInCounter5_Object = MibTableColumn
mccpTgTrInCounter5 = _MccpTgTrInCounter5_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 12, 1, 8),
    _MccpTgTrInCounter5_Type()
)
mccpTgTrInCounter5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgTrInCounter5.setStatus("current")


class _MccpTgTrInCounter6_Type(Integer32):
    """Custom type mccpTgTrInCounter6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgTrInCounter6_Type.__name__ = "Integer32"
_MccpTgTrInCounter6_Object = MibTableColumn
mccpTgTrInCounter6 = _MccpTgTrInCounter6_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 12, 1, 9),
    _MccpTgTrInCounter6_Type()
)
mccpTgTrInCounter6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgTrInCounter6.setStatus("current")


class _MccpTgTrInCounter7_Type(Integer32):
    """Custom type mccpTgTrInCounter7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgTrInCounter7_Type.__name__ = "Integer32"
_MccpTgTrInCounter7_Object = MibTableColumn
mccpTgTrInCounter7 = _MccpTgTrInCounter7_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 12, 1, 10),
    _MccpTgTrInCounter7_Type()
)
mccpTgTrInCounter7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgTrInCounter7.setStatus("current")


class _MccpTgTrInCounter8_Type(Integer32):
    """Custom type mccpTgTrInCounter8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgTrInCounter8_Type.__name__ = "Integer32"
_MccpTgTrInCounter8_Object = MibTableColumn
mccpTgTrInCounter8 = _MccpTgTrInCounter8_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 12, 1, 11),
    _MccpTgTrInCounter8_Type()
)
mccpTgTrInCounter8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgTrInCounter8.setStatus("current")


class _MccpTgTrInCounter9_Type(Integer32):
    """Custom type mccpTgTrInCounter9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgTrInCounter9_Type.__name__ = "Integer32"
_MccpTgTrInCounter9_Object = MibTableColumn
mccpTgTrInCounter9 = _MccpTgTrInCounter9_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 12, 1, 12),
    _MccpTgTrInCounter9_Type()
)
mccpTgTrInCounter9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgTrInCounter9.setStatus("current")


class _MccpTgTrInCounter10_Type(Integer32):
    """Custom type mccpTgTrInCounter10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgTrInCounter10_Type.__name__ = "Integer32"
_MccpTgTrInCounter10_Object = MibTableColumn
mccpTgTrInCounter10 = _MccpTgTrInCounter10_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 12, 1, 13),
    _MccpTgTrInCounter10_Type()
)
mccpTgTrInCounter10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgTrInCounter10.setStatus("current")
_MccpTgStatTrOutTable_Object = MibTable
mccpTgStatTrOutTable = _MccpTgStatTrOutTable_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 13)
)
if mibBuilder.loadTexts:
    mccpTgStatTrOutTable.setStatus("current")
_MccpTgStatTrOutEntry_Object = MibTableRow
mccpTgStatTrOutEntry = _MccpTgStatTrOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 13, 1)
)
mccpTgStatTrOutEntry.setIndexNames(
    (0, "ELTEX-MCCP", "mccpTgTrOutIndex"),
)
if mibBuilder.loadTexts:
    mccpTgStatTrOutEntry.setStatus("current")


class _MccpTgTrOutIndex_Type(Integer32):
    """Custom type mccpTgTrOutIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MccpTgTrOutIndex_Type.__name__ = "Integer32"
_MccpTgTrOutIndex_Object = MibTableColumn
mccpTgTrOutIndex = _MccpTgTrOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 13, 1, 1),
    _MccpTgTrOutIndex_Type()
)
mccpTgTrOutIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mccpTgTrOutIndex.setStatus("current")


class _MccpTgTrOutId_Type(Integer32):
    """Custom type mccpTgTrOutId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MccpTgTrOutId_Type.__name__ = "Integer32"
_MccpTgTrOutId_Object = MibTableColumn
mccpTgTrOutId = _MccpTgTrOutId_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 13, 1, 2),
    _MccpTgTrOutId_Type()
)
mccpTgTrOutId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgTrOutId.setStatus("current")


class _MccpTgTrOutCounter0_Type(Integer32):
    """Custom type mccpTgTrOutCounter0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgTrOutCounter0_Type.__name__ = "Integer32"
_MccpTgTrOutCounter0_Object = MibTableColumn
mccpTgTrOutCounter0 = _MccpTgTrOutCounter0_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 13, 1, 3),
    _MccpTgTrOutCounter0_Type()
)
mccpTgTrOutCounter0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgTrOutCounter0.setStatus("current")


class _MccpTgTrOutCounter1_Type(Integer32):
    """Custom type mccpTgTrOutCounter1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgTrOutCounter1_Type.__name__ = "Integer32"
_MccpTgTrOutCounter1_Object = MibTableColumn
mccpTgTrOutCounter1 = _MccpTgTrOutCounter1_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 13, 1, 4),
    _MccpTgTrOutCounter1_Type()
)
mccpTgTrOutCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgTrOutCounter1.setStatus("current")


class _MccpTgTrOutCounter2_Type(Integer32):
    """Custom type mccpTgTrOutCounter2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgTrOutCounter2_Type.__name__ = "Integer32"
_MccpTgTrOutCounter2_Object = MibTableColumn
mccpTgTrOutCounter2 = _MccpTgTrOutCounter2_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 13, 1, 5),
    _MccpTgTrOutCounter2_Type()
)
mccpTgTrOutCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgTrOutCounter2.setStatus("current")


class _MccpTgTrOutCounter3_Type(Integer32):
    """Custom type mccpTgTrOutCounter3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgTrOutCounter3_Type.__name__ = "Integer32"
_MccpTgTrOutCounter3_Object = MibTableColumn
mccpTgTrOutCounter3 = _MccpTgTrOutCounter3_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 13, 1, 6),
    _MccpTgTrOutCounter3_Type()
)
mccpTgTrOutCounter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgTrOutCounter3.setStatus("current")


class _MccpTgTrOutCounter4_Type(Integer32):
    """Custom type mccpTgTrOutCounter4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgTrOutCounter4_Type.__name__ = "Integer32"
_MccpTgTrOutCounter4_Object = MibTableColumn
mccpTgTrOutCounter4 = _MccpTgTrOutCounter4_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 13, 1, 7),
    _MccpTgTrOutCounter4_Type()
)
mccpTgTrOutCounter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgTrOutCounter4.setStatus("current")


class _MccpTgTrOutCounter5_Type(Integer32):
    """Custom type mccpTgTrOutCounter5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgTrOutCounter5_Type.__name__ = "Integer32"
_MccpTgTrOutCounter5_Object = MibTableColumn
mccpTgTrOutCounter5 = _MccpTgTrOutCounter5_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 13, 1, 8),
    _MccpTgTrOutCounter5_Type()
)
mccpTgTrOutCounter5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgTrOutCounter5.setStatus("current")


class _MccpTgTrOutCounter6_Type(Integer32):
    """Custom type mccpTgTrOutCounter6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgTrOutCounter6_Type.__name__ = "Integer32"
_MccpTgTrOutCounter6_Object = MibTableColumn
mccpTgTrOutCounter6 = _MccpTgTrOutCounter6_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 13, 1, 9),
    _MccpTgTrOutCounter6_Type()
)
mccpTgTrOutCounter6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgTrOutCounter6.setStatus("current")


class _MccpTgTrOutCounter7_Type(Integer32):
    """Custom type mccpTgTrOutCounter7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgTrOutCounter7_Type.__name__ = "Integer32"
_MccpTgTrOutCounter7_Object = MibTableColumn
mccpTgTrOutCounter7 = _MccpTgTrOutCounter7_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 13, 1, 10),
    _MccpTgTrOutCounter7_Type()
)
mccpTgTrOutCounter7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgTrOutCounter7.setStatus("current")


class _MccpTgTrOutCounter8_Type(Integer32):
    """Custom type mccpTgTrOutCounter8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgTrOutCounter8_Type.__name__ = "Integer32"
_MccpTgTrOutCounter8_Object = MibTableColumn
mccpTgTrOutCounter8 = _MccpTgTrOutCounter8_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 13, 1, 11),
    _MccpTgTrOutCounter8_Type()
)
mccpTgTrOutCounter8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgTrOutCounter8.setStatus("current")


class _MccpTgTrOutCounter9_Type(Integer32):
    """Custom type mccpTgTrOutCounter9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgTrOutCounter9_Type.__name__ = "Integer32"
_MccpTgTrOutCounter9_Object = MibTableColumn
mccpTgTrOutCounter9 = _MccpTgTrOutCounter9_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 13, 1, 12),
    _MccpTgTrOutCounter9_Type()
)
mccpTgTrOutCounter9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgTrOutCounter9.setStatus("current")


class _MccpTgTrOutCounter10_Type(Integer32):
    """Custom type mccpTgTrOutCounter10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgTrOutCounter10_Type.__name__ = "Integer32"
_MccpTgTrOutCounter10_Object = MibTableColumn
mccpTgTrOutCounter10 = _MccpTgTrOutCounter10_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 13, 1, 13),
    _MccpTgTrOutCounter10_Type()
)
mccpTgTrOutCounter10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgTrOutCounter10.setStatus("current")
_MccpTgUsageTable_Object = MibTable
mccpTgUsageTable = _MccpTgUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 14)
)
if mibBuilder.loadTexts:
    mccpTgUsageTable.setStatus("current")
_MccpTgUsageEntry_Object = MibTableRow
mccpTgUsageEntry = _MccpTgUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 14, 1)
)
mccpTgUsageEntry.setIndexNames(
    (0, "ELTEX-MCCP", "mccpTgUsageIndex"),
)
if mibBuilder.loadTexts:
    mccpTgUsageEntry.setStatus("current")


class _MccpTgUsageIndex_Type(Integer32):
    """Custom type mccpTgUsageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MccpTgUsageIndex_Type.__name__ = "Integer32"
_MccpTgUsageIndex_Object = MibTableColumn
mccpTgUsageIndex = _MccpTgUsageIndex_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 14, 1, 1),
    _MccpTgUsageIndex_Type()
)
mccpTgUsageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mccpTgUsageIndex.setStatus("current")


class _MccpTgUsageId_Type(Integer32):
    """Custom type mccpTgUsageId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MccpTgUsageId_Type.__name__ = "Integer32"
_MccpTgUsageId_Object = MibTableColumn
mccpTgUsageId = _MccpTgUsageId_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 14, 1, 2),
    _MccpTgUsageId_Type()
)
mccpTgUsageId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgUsageId.setStatus("current")


class _MccpTgUsageCounter0_Type(Integer32):
    """Custom type mccpTgUsageCounter0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgUsageCounter0_Type.__name__ = "Integer32"
_MccpTgUsageCounter0_Object = MibTableColumn
mccpTgUsageCounter0 = _MccpTgUsageCounter0_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 14, 1, 3),
    _MccpTgUsageCounter0_Type()
)
mccpTgUsageCounter0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgUsageCounter0.setStatus("current")


class _MccpTgUsageCounter1_Type(Integer32):
    """Custom type mccpTgUsageCounter1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgUsageCounter1_Type.__name__ = "Integer32"
_MccpTgUsageCounter1_Object = MibTableColumn
mccpTgUsageCounter1 = _MccpTgUsageCounter1_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 14, 1, 4),
    _MccpTgUsageCounter1_Type()
)
mccpTgUsageCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgUsageCounter1.setStatus("current")


class _MccpTgUsageCounter2_Type(Integer32):
    """Custom type mccpTgUsageCounter2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgUsageCounter2_Type.__name__ = "Integer32"
_MccpTgUsageCounter2_Object = MibTableColumn
mccpTgUsageCounter2 = _MccpTgUsageCounter2_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 14, 1, 5),
    _MccpTgUsageCounter2_Type()
)
mccpTgUsageCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgUsageCounter2.setStatus("current")


class _MccpTgUsageCounter3_Type(Integer32):
    """Custom type mccpTgUsageCounter3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgUsageCounter3_Type.__name__ = "Integer32"
_MccpTgUsageCounter3_Object = MibTableColumn
mccpTgUsageCounter3 = _MccpTgUsageCounter3_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 14, 1, 6),
    _MccpTgUsageCounter3_Type()
)
mccpTgUsageCounter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgUsageCounter3.setStatus("current")


class _MccpTgUsageCounter4_Type(Integer32):
    """Custom type mccpTgUsageCounter4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpTgUsageCounter4_Type.__name__ = "Integer32"
_MccpTgUsageCounter4_Object = MibTableColumn
mccpTgUsageCounter4 = _MccpTgUsageCounter4_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 14, 1, 7),
    _MccpTgUsageCounter4_Type()
)
mccpTgUsageCounter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpTgUsageCounter4.setStatus("current")
_MccpPlanStatInTable_Object = MibTable
mccpPlanStatInTable = _MccpPlanStatInTable_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 15)
)
if mibBuilder.loadTexts:
    mccpPlanStatInTable.setStatus("current")
_MccpPlanStatInEntry_Object = MibTableRow
mccpPlanStatInEntry = _MccpPlanStatInEntry_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 15, 1)
)
mccpPlanStatInEntry.setIndexNames(
    (0, "ELTEX-MCCP", "mccpPlanInIndex"),
)
if mibBuilder.loadTexts:
    mccpPlanStatInEntry.setStatus("current")


class _MccpPlanInIndex_Type(Integer32):
    """Custom type mccpPlanInIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MccpPlanInIndex_Type.__name__ = "Integer32"
_MccpPlanInIndex_Object = MibTableColumn
mccpPlanInIndex = _MccpPlanInIndex_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 15, 1, 1),
    _MccpPlanInIndex_Type()
)
mccpPlanInIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mccpPlanInIndex.setStatus("current")


class _MccpPlanInCounter0_Type(Integer32):
    """Custom type mccpPlanInCounter0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpPlanInCounter0_Type.__name__ = "Integer32"
_MccpPlanInCounter0_Object = MibTableColumn
mccpPlanInCounter0 = _MccpPlanInCounter0_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 15, 1, 2),
    _MccpPlanInCounter0_Type()
)
mccpPlanInCounter0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpPlanInCounter0.setStatus("current")


class _MccpPlanInCounter1_Type(Integer32):
    """Custom type mccpPlanInCounter1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpPlanInCounter1_Type.__name__ = "Integer32"
_MccpPlanInCounter1_Object = MibTableColumn
mccpPlanInCounter1 = _MccpPlanInCounter1_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 15, 1, 3),
    _MccpPlanInCounter1_Type()
)
mccpPlanInCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpPlanInCounter1.setStatus("current")


class _MccpPlanInCounter2_Type(Integer32):
    """Custom type mccpPlanInCounter2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpPlanInCounter2_Type.__name__ = "Integer32"
_MccpPlanInCounter2_Object = MibTableColumn
mccpPlanInCounter2 = _MccpPlanInCounter2_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 15, 1, 4),
    _MccpPlanInCounter2_Type()
)
mccpPlanInCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpPlanInCounter2.setStatus("current")


class _MccpPlanInCounter3_Type(Integer32):
    """Custom type mccpPlanInCounter3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpPlanInCounter3_Type.__name__ = "Integer32"
_MccpPlanInCounter3_Object = MibTableColumn
mccpPlanInCounter3 = _MccpPlanInCounter3_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 15, 1, 5),
    _MccpPlanInCounter3_Type()
)
mccpPlanInCounter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpPlanInCounter3.setStatus("current")


class _MccpPlanInCounter4_Type(Integer32):
    """Custom type mccpPlanInCounter4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpPlanInCounter4_Type.__name__ = "Integer32"
_MccpPlanInCounter4_Object = MibTableColumn
mccpPlanInCounter4 = _MccpPlanInCounter4_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 15, 1, 6),
    _MccpPlanInCounter4_Type()
)
mccpPlanInCounter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpPlanInCounter4.setStatus("current")


class _MccpPlanInCounter5_Type(Integer32):
    """Custom type mccpPlanInCounter5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpPlanInCounter5_Type.__name__ = "Integer32"
_MccpPlanInCounter5_Object = MibTableColumn
mccpPlanInCounter5 = _MccpPlanInCounter5_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 15, 1, 7),
    _MccpPlanInCounter5_Type()
)
mccpPlanInCounter5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpPlanInCounter5.setStatus("current")


class _MccpPlanInCounter6_Type(Integer32):
    """Custom type mccpPlanInCounter6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpPlanInCounter6_Type.__name__ = "Integer32"
_MccpPlanInCounter6_Object = MibTableColumn
mccpPlanInCounter6 = _MccpPlanInCounter6_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 15, 1, 8),
    _MccpPlanInCounter6_Type()
)
mccpPlanInCounter6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpPlanInCounter6.setStatus("current")


class _MccpPlanInCounter7_Type(Integer32):
    """Custom type mccpPlanInCounter7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpPlanInCounter7_Type.__name__ = "Integer32"
_MccpPlanInCounter7_Object = MibTableColumn
mccpPlanInCounter7 = _MccpPlanInCounter7_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 15, 1, 9),
    _MccpPlanInCounter7_Type()
)
mccpPlanInCounter7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpPlanInCounter7.setStatus("current")


class _MccpPlanInCounter8_Type(Integer32):
    """Custom type mccpPlanInCounter8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpPlanInCounter8_Type.__name__ = "Integer32"
_MccpPlanInCounter8_Object = MibTableColumn
mccpPlanInCounter8 = _MccpPlanInCounter8_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 15, 1, 10),
    _MccpPlanInCounter8_Type()
)
mccpPlanInCounter8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpPlanInCounter8.setStatus("current")


class _MccpPlanInCounter9_Type(Integer32):
    """Custom type mccpPlanInCounter9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpPlanInCounter9_Type.__name__ = "Integer32"
_MccpPlanInCounter9_Object = MibTableColumn
mccpPlanInCounter9 = _MccpPlanInCounter9_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 15, 1, 11),
    _MccpPlanInCounter9_Type()
)
mccpPlanInCounter9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpPlanInCounter9.setStatus("current")


class _MccpPlanInCounter10_Type(Integer32):
    """Custom type mccpPlanInCounter10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpPlanInCounter10_Type.__name__ = "Integer32"
_MccpPlanInCounter10_Object = MibTableColumn
mccpPlanInCounter10 = _MccpPlanInCounter10_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 15, 1, 12),
    _MccpPlanInCounter10_Type()
)
mccpPlanInCounter10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpPlanInCounter10.setStatus("current")
_MccpPlanStatOutTable_Object = MibTable
mccpPlanStatOutTable = _MccpPlanStatOutTable_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 16)
)
if mibBuilder.loadTexts:
    mccpPlanStatOutTable.setStatus("current")
_MccpPlanStatOutEntry_Object = MibTableRow
mccpPlanStatOutEntry = _MccpPlanStatOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 16, 1)
)
mccpPlanStatOutEntry.setIndexNames(
    (0, "ELTEX-MCCP", "mccpPlanOutIndex"),
)
if mibBuilder.loadTexts:
    mccpPlanStatOutEntry.setStatus("current")


class _MccpPlanOutIndex_Type(Integer32):
    """Custom type mccpPlanOutIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MccpPlanOutIndex_Type.__name__ = "Integer32"
_MccpPlanOutIndex_Object = MibTableColumn
mccpPlanOutIndex = _MccpPlanOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 16, 1, 1),
    _MccpPlanOutIndex_Type()
)
mccpPlanOutIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mccpPlanOutIndex.setStatus("current")


class _MccpPlanOutCounter0_Type(Integer32):
    """Custom type mccpPlanOutCounter0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpPlanOutCounter0_Type.__name__ = "Integer32"
_MccpPlanOutCounter0_Object = MibTableColumn
mccpPlanOutCounter0 = _MccpPlanOutCounter0_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 16, 1, 2),
    _MccpPlanOutCounter0_Type()
)
mccpPlanOutCounter0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpPlanOutCounter0.setStatus("current")


class _MccpPlanOutCounter1_Type(Integer32):
    """Custom type mccpPlanOutCounter1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpPlanOutCounter1_Type.__name__ = "Integer32"
_MccpPlanOutCounter1_Object = MibTableColumn
mccpPlanOutCounter1 = _MccpPlanOutCounter1_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 16, 1, 3),
    _MccpPlanOutCounter1_Type()
)
mccpPlanOutCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpPlanOutCounter1.setStatus("current")


class _MccpPlanOutCounter2_Type(Integer32):
    """Custom type mccpPlanOutCounter2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpPlanOutCounter2_Type.__name__ = "Integer32"
_MccpPlanOutCounter2_Object = MibTableColumn
mccpPlanOutCounter2 = _MccpPlanOutCounter2_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 16, 1, 4),
    _MccpPlanOutCounter2_Type()
)
mccpPlanOutCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpPlanOutCounter2.setStatus("current")


class _MccpPlanOutCounter3_Type(Integer32):
    """Custom type mccpPlanOutCounter3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpPlanOutCounter3_Type.__name__ = "Integer32"
_MccpPlanOutCounter3_Object = MibTableColumn
mccpPlanOutCounter3 = _MccpPlanOutCounter3_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 16, 1, 5),
    _MccpPlanOutCounter3_Type()
)
mccpPlanOutCounter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpPlanOutCounter3.setStatus("current")


class _MccpPlanOutCounter4_Type(Integer32):
    """Custom type mccpPlanOutCounter4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpPlanOutCounter4_Type.__name__ = "Integer32"
_MccpPlanOutCounter4_Object = MibTableColumn
mccpPlanOutCounter4 = _MccpPlanOutCounter4_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 16, 1, 6),
    _MccpPlanOutCounter4_Type()
)
mccpPlanOutCounter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpPlanOutCounter4.setStatus("current")


class _MccpPlanOutCounter5_Type(Integer32):
    """Custom type mccpPlanOutCounter5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpPlanOutCounter5_Type.__name__ = "Integer32"
_MccpPlanOutCounter5_Object = MibTableColumn
mccpPlanOutCounter5 = _MccpPlanOutCounter5_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 16, 1, 7),
    _MccpPlanOutCounter5_Type()
)
mccpPlanOutCounter5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpPlanOutCounter5.setStatus("current")


class _MccpPlanOutCounter6_Type(Integer32):
    """Custom type mccpPlanOutCounter6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpPlanOutCounter6_Type.__name__ = "Integer32"
_MccpPlanOutCounter6_Object = MibTableColumn
mccpPlanOutCounter6 = _MccpPlanOutCounter6_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 16, 1, 8),
    _MccpPlanOutCounter6_Type()
)
mccpPlanOutCounter6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpPlanOutCounter6.setStatus("current")


class _MccpPlanOutCounter7_Type(Integer32):
    """Custom type mccpPlanOutCounter7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpPlanOutCounter7_Type.__name__ = "Integer32"
_MccpPlanOutCounter7_Object = MibTableColumn
mccpPlanOutCounter7 = _MccpPlanOutCounter7_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 16, 1, 9),
    _MccpPlanOutCounter7_Type()
)
mccpPlanOutCounter7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpPlanOutCounter7.setStatus("current")


class _MccpPlanOutCounter8_Type(Integer32):
    """Custom type mccpPlanOutCounter8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpPlanOutCounter8_Type.__name__ = "Integer32"
_MccpPlanOutCounter8_Object = MibTableColumn
mccpPlanOutCounter8 = _MccpPlanOutCounter8_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 16, 1, 10),
    _MccpPlanOutCounter8_Type()
)
mccpPlanOutCounter8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpPlanOutCounter8.setStatus("current")


class _MccpPlanOutCounter9_Type(Integer32):
    """Custom type mccpPlanOutCounter9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpPlanOutCounter9_Type.__name__ = "Integer32"
_MccpPlanOutCounter9_Object = MibTableColumn
mccpPlanOutCounter9 = _MccpPlanOutCounter9_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 16, 1, 11),
    _MccpPlanOutCounter9_Type()
)
mccpPlanOutCounter9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpPlanOutCounter9.setStatus("current")


class _MccpPlanOutCounter10_Type(Integer32):
    """Custom type mccpPlanOutCounter10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpPlanOutCounter10_Type.__name__ = "Integer32"
_MccpPlanOutCounter10_Object = MibTableColumn
mccpPlanOutCounter10 = _MccpPlanOutCounter10_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 16, 1, 12),
    _MccpPlanOutCounter10_Type()
)
mccpPlanOutCounter10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpPlanOutCounter10.setStatus("current")
_MccpPlanUsageTable_Object = MibTable
mccpPlanUsageTable = _MccpPlanUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 17)
)
if mibBuilder.loadTexts:
    mccpPlanUsageTable.setStatus("current")
_MccpPlanUsageEntry_Object = MibTableRow
mccpPlanUsageEntry = _MccpPlanUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 17, 1)
)
mccpPlanUsageEntry.setIndexNames(
    (0, "ELTEX-MCCP", "mccpPlanUsageIndex"),
)
if mibBuilder.loadTexts:
    mccpPlanUsageEntry.setStatus("current")


class _MccpPlanUsageIndex_Type(Integer32):
    """Custom type mccpPlanUsageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MccpPlanUsageIndex_Type.__name__ = "Integer32"
_MccpPlanUsageIndex_Object = MibTableColumn
mccpPlanUsageIndex = _MccpPlanUsageIndex_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 17, 1, 1),
    _MccpPlanUsageIndex_Type()
)
mccpPlanUsageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mccpPlanUsageIndex.setStatus("current")


class _MccpPlanUsageCounter0_Type(Integer32):
    """Custom type mccpPlanUsageCounter0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpPlanUsageCounter0_Type.__name__ = "Integer32"
_MccpPlanUsageCounter0_Object = MibTableColumn
mccpPlanUsageCounter0 = _MccpPlanUsageCounter0_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 17, 1, 2),
    _MccpPlanUsageCounter0_Type()
)
mccpPlanUsageCounter0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpPlanUsageCounter0.setStatus("current")


class _MccpPlanUsageCounter1_Type(Integer32):
    """Custom type mccpPlanUsageCounter1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpPlanUsageCounter1_Type.__name__ = "Integer32"
_MccpPlanUsageCounter1_Object = MibTableColumn
mccpPlanUsageCounter1 = _MccpPlanUsageCounter1_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 17, 1, 3),
    _MccpPlanUsageCounter1_Type()
)
mccpPlanUsageCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpPlanUsageCounter1.setStatus("current")


class _MccpPlanUsageCounter2_Type(Integer32):
    """Custom type mccpPlanUsageCounter2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpPlanUsageCounter2_Type.__name__ = "Integer32"
_MccpPlanUsageCounter2_Object = MibTableColumn
mccpPlanUsageCounter2 = _MccpPlanUsageCounter2_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 17, 1, 4),
    _MccpPlanUsageCounter2_Type()
)
mccpPlanUsageCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpPlanUsageCounter2.setStatus("current")


class _MccpPlanUsageCounter3_Type(Integer32):
    """Custom type mccpPlanUsageCounter3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpPlanUsageCounter3_Type.__name__ = "Integer32"
_MccpPlanUsageCounter3_Object = MibTableColumn
mccpPlanUsageCounter3 = _MccpPlanUsageCounter3_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 17, 1, 5),
    _MccpPlanUsageCounter3_Type()
)
mccpPlanUsageCounter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpPlanUsageCounter3.setStatus("current")


class _MccpPlanUsageCounter4_Type(Integer32):
    """Custom type mccpPlanUsageCounter4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpPlanUsageCounter4_Type.__name__ = "Integer32"
_MccpPlanUsageCounter4_Object = MibTableColumn
mccpPlanUsageCounter4 = _MccpPlanUsageCounter4_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 17, 1, 6),
    _MccpPlanUsageCounter4_Type()
)
mccpPlanUsageCounter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpPlanUsageCounter4.setStatus("current")
_MccpSubStatInTable_Object = MibTable
mccpSubStatInTable = _MccpSubStatInTable_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 18)
)
if mibBuilder.loadTexts:
    mccpSubStatInTable.setStatus("current")
_MccpSubStatInEntry_Object = MibTableRow
mccpSubStatInEntry = _MccpSubStatInEntry_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 18, 1)
)
mccpSubStatInEntry.setIndexNames(
    (0, "ELTEX-MCCP", "mccpSubInIndex"),
)
if mibBuilder.loadTexts:
    mccpSubStatInEntry.setStatus("current")


class _MccpSubInIndex_Type(Integer32):
    """Custom type mccpSubInIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubInIndex_Type.__name__ = "Integer32"
_MccpSubInIndex_Object = MibTableColumn
mccpSubInIndex = _MccpSubInIndex_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 18, 1, 1),
    _MccpSubInIndex_Type()
)
mccpSubInIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mccpSubInIndex.setStatus("current")


class _MccpSubInCounter0_Type(Integer32):
    """Custom type mccpSubInCounter0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubInCounter0_Type.__name__ = "Integer32"
_MccpSubInCounter0_Object = MibTableColumn
mccpSubInCounter0 = _MccpSubInCounter0_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 18, 1, 2),
    _MccpSubInCounter0_Type()
)
mccpSubInCounter0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpSubInCounter0.setStatus("current")


class _MccpSubInCounter1_Type(Integer32):
    """Custom type mccpSubInCounter1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubInCounter1_Type.__name__ = "Integer32"
_MccpSubInCounter1_Object = MibTableColumn
mccpSubInCounter1 = _MccpSubInCounter1_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 18, 1, 3),
    _MccpSubInCounter1_Type()
)
mccpSubInCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpSubInCounter1.setStatus("current")


class _MccpSubInCounter2_Type(Integer32):
    """Custom type mccpSubInCounter2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubInCounter2_Type.__name__ = "Integer32"
_MccpSubInCounter2_Object = MibTableColumn
mccpSubInCounter2 = _MccpSubInCounter2_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 18, 1, 4),
    _MccpSubInCounter2_Type()
)
mccpSubInCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpSubInCounter2.setStatus("current")


class _MccpSubInCounter3_Type(Integer32):
    """Custom type mccpSubInCounter3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubInCounter3_Type.__name__ = "Integer32"
_MccpSubInCounter3_Object = MibTableColumn
mccpSubInCounter3 = _MccpSubInCounter3_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 18, 1, 5),
    _MccpSubInCounter3_Type()
)
mccpSubInCounter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpSubInCounter3.setStatus("current")


class _MccpSubInCounter4_Type(Integer32):
    """Custom type mccpSubInCounter4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubInCounter4_Type.__name__ = "Integer32"
_MccpSubInCounter4_Object = MibTableColumn
mccpSubInCounter4 = _MccpSubInCounter4_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 18, 1, 6),
    _MccpSubInCounter4_Type()
)
mccpSubInCounter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpSubInCounter4.setStatus("current")


class _MccpSubInCounter5_Type(Integer32):
    """Custom type mccpSubInCounter5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubInCounter5_Type.__name__ = "Integer32"
_MccpSubInCounter5_Object = MibTableColumn
mccpSubInCounter5 = _MccpSubInCounter5_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 18, 1, 7),
    _MccpSubInCounter5_Type()
)
mccpSubInCounter5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpSubInCounter5.setStatus("current")


class _MccpSubInCounter6_Type(Integer32):
    """Custom type mccpSubInCounter6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubInCounter6_Type.__name__ = "Integer32"
_MccpSubInCounter6_Object = MibTableColumn
mccpSubInCounter6 = _MccpSubInCounter6_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 18, 1, 8),
    _MccpSubInCounter6_Type()
)
mccpSubInCounter6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpSubInCounter6.setStatus("current")


class _MccpSubInCounter7_Type(Integer32):
    """Custom type mccpSubInCounter7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubInCounter7_Type.__name__ = "Integer32"
_MccpSubInCounter7_Object = MibTableColumn
mccpSubInCounter7 = _MccpSubInCounter7_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 18, 1, 9),
    _MccpSubInCounter7_Type()
)
mccpSubInCounter7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpSubInCounter7.setStatus("current")


class _MccpSubInCounter8_Type(Integer32):
    """Custom type mccpSubInCounter8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubInCounter8_Type.__name__ = "Integer32"
_MccpSubInCounter8_Object = MibTableColumn
mccpSubInCounter8 = _MccpSubInCounter8_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 18, 1, 10),
    _MccpSubInCounter8_Type()
)
mccpSubInCounter8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpSubInCounter8.setStatus("current")


class _MccpSubInCounter9_Type(Integer32):
    """Custom type mccpSubInCounter9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubInCounter9_Type.__name__ = "Integer32"
_MccpSubInCounter9_Object = MibTableColumn
mccpSubInCounter9 = _MccpSubInCounter9_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 18, 1, 11),
    _MccpSubInCounter9_Type()
)
mccpSubInCounter9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpSubInCounter9.setStatus("current")


class _MccpSubInCounter10_Type(Integer32):
    """Custom type mccpSubInCounter10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubInCounter10_Type.__name__ = "Integer32"
_MccpSubInCounter10_Object = MibTableColumn
mccpSubInCounter10 = _MccpSubInCounter10_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 18, 1, 12),
    _MccpSubInCounter10_Type()
)
mccpSubInCounter10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpSubInCounter10.setStatus("current")
_MccpSubStatOutTable_Object = MibTable
mccpSubStatOutTable = _MccpSubStatOutTable_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 19)
)
if mibBuilder.loadTexts:
    mccpSubStatOutTable.setStatus("current")
_MccpSubStatOutEntry_Object = MibTableRow
mccpSubStatOutEntry = _MccpSubStatOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 19, 1)
)
mccpSubStatOutEntry.setIndexNames(
    (0, "ELTEX-MCCP", "mccpSubOutIndex"),
)
if mibBuilder.loadTexts:
    mccpSubStatOutEntry.setStatus("current")


class _MccpSubOutIndex_Type(Integer32):
    """Custom type mccpSubOutIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubOutIndex_Type.__name__ = "Integer32"
_MccpSubOutIndex_Object = MibTableColumn
mccpSubOutIndex = _MccpSubOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 19, 1, 1),
    _MccpSubOutIndex_Type()
)
mccpSubOutIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mccpSubOutIndex.setStatus("current")


class _MccpSubOutCounter0_Type(Integer32):
    """Custom type mccpSubOutCounter0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubOutCounter0_Type.__name__ = "Integer32"
_MccpSubOutCounter0_Object = MibTableColumn
mccpSubOutCounter0 = _MccpSubOutCounter0_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 19, 1, 2),
    _MccpSubOutCounter0_Type()
)
mccpSubOutCounter0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpSubOutCounter0.setStatus("current")


class _MccpSubOutCounter1_Type(Integer32):
    """Custom type mccpSubOutCounter1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubOutCounter1_Type.__name__ = "Integer32"
_MccpSubOutCounter1_Object = MibTableColumn
mccpSubOutCounter1 = _MccpSubOutCounter1_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 19, 1, 3),
    _MccpSubOutCounter1_Type()
)
mccpSubOutCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpSubOutCounter1.setStatus("current")


class _MccpSubOutCounter2_Type(Integer32):
    """Custom type mccpSubOutCounter2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubOutCounter2_Type.__name__ = "Integer32"
_MccpSubOutCounter2_Object = MibTableColumn
mccpSubOutCounter2 = _MccpSubOutCounter2_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 19, 1, 4),
    _MccpSubOutCounter2_Type()
)
mccpSubOutCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpSubOutCounter2.setStatus("current")


class _MccpSubOutCounter3_Type(Integer32):
    """Custom type mccpSubOutCounter3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubOutCounter3_Type.__name__ = "Integer32"
_MccpSubOutCounter3_Object = MibTableColumn
mccpSubOutCounter3 = _MccpSubOutCounter3_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 19, 1, 5),
    _MccpSubOutCounter3_Type()
)
mccpSubOutCounter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpSubOutCounter3.setStatus("current")


class _MccpSubOutCounter4_Type(Integer32):
    """Custom type mccpSubOutCounter4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubOutCounter4_Type.__name__ = "Integer32"
_MccpSubOutCounter4_Object = MibTableColumn
mccpSubOutCounter4 = _MccpSubOutCounter4_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 19, 1, 6),
    _MccpSubOutCounter4_Type()
)
mccpSubOutCounter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpSubOutCounter4.setStatus("current")


class _MccpSubOutCounter5_Type(Integer32):
    """Custom type mccpSubOutCounter5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubOutCounter5_Type.__name__ = "Integer32"
_MccpSubOutCounter5_Object = MibTableColumn
mccpSubOutCounter5 = _MccpSubOutCounter5_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 19, 1, 7),
    _MccpSubOutCounter5_Type()
)
mccpSubOutCounter5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpSubOutCounter5.setStatus("current")


class _MccpSubOutCounter6_Type(Integer32):
    """Custom type mccpSubOutCounter6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubOutCounter6_Type.__name__ = "Integer32"
_MccpSubOutCounter6_Object = MibTableColumn
mccpSubOutCounter6 = _MccpSubOutCounter6_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 19, 1, 8),
    _MccpSubOutCounter6_Type()
)
mccpSubOutCounter6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpSubOutCounter6.setStatus("current")


class _MccpSubOutCounter7_Type(Integer32):
    """Custom type mccpSubOutCounter7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubOutCounter7_Type.__name__ = "Integer32"
_MccpSubOutCounter7_Object = MibTableColumn
mccpSubOutCounter7 = _MccpSubOutCounter7_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 19, 1, 9),
    _MccpSubOutCounter7_Type()
)
mccpSubOutCounter7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpSubOutCounter7.setStatus("current")


class _MccpSubOutCounter8_Type(Integer32):
    """Custom type mccpSubOutCounter8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubOutCounter8_Type.__name__ = "Integer32"
_MccpSubOutCounter8_Object = MibTableColumn
mccpSubOutCounter8 = _MccpSubOutCounter8_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 19, 1, 10),
    _MccpSubOutCounter8_Type()
)
mccpSubOutCounter8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpSubOutCounter8.setStatus("current")


class _MccpSubOutCounter9_Type(Integer32):
    """Custom type mccpSubOutCounter9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubOutCounter9_Type.__name__ = "Integer32"
_MccpSubOutCounter9_Object = MibTableColumn
mccpSubOutCounter9 = _MccpSubOutCounter9_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 19, 1, 11),
    _MccpSubOutCounter9_Type()
)
mccpSubOutCounter9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpSubOutCounter9.setStatus("current")


class _MccpSubOutCounter10_Type(Integer32):
    """Custom type mccpSubOutCounter10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubOutCounter10_Type.__name__ = "Integer32"
_MccpSubOutCounter10_Object = MibTableColumn
mccpSubOutCounter10 = _MccpSubOutCounter10_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 19, 1, 12),
    _MccpSubOutCounter10_Type()
)
mccpSubOutCounter10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpSubOutCounter10.setStatus("current")
_MccpSubUsageTable_Object = MibTable
mccpSubUsageTable = _MccpSubUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 20)
)
if mibBuilder.loadTexts:
    mccpSubUsageTable.setStatus("current")
_MccpSubUsageEntry_Object = MibTableRow
mccpSubUsageEntry = _MccpSubUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 20, 1)
)
mccpSubUsageEntry.setIndexNames(
    (0, "ELTEX-MCCP", "mccpSubUsageIndex"),
)
if mibBuilder.loadTexts:
    mccpSubUsageEntry.setStatus("current")


class _MccpSubUsageIndex_Type(Integer32):
    """Custom type mccpSubUsageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MccpSubUsageIndex_Type.__name__ = "Integer32"
_MccpSubUsageIndex_Object = MibTableColumn
mccpSubUsageIndex = _MccpSubUsageIndex_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 20, 1, 1),
    _MccpSubUsageIndex_Type()
)
mccpSubUsageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mccpSubUsageIndex.setStatus("current")


class _MccpSubUsageCounter0_Type(Integer32):
    """Custom type mccpSubUsageCounter0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubUsageCounter0_Type.__name__ = "Integer32"
_MccpSubUsageCounter0_Object = MibTableColumn
mccpSubUsageCounter0 = _MccpSubUsageCounter0_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 20, 1, 2),
    _MccpSubUsageCounter0_Type()
)
mccpSubUsageCounter0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpSubUsageCounter0.setStatus("current")


class _MccpSubUsageCounter1_Type(Integer32):
    """Custom type mccpSubUsageCounter1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubUsageCounter1_Type.__name__ = "Integer32"
_MccpSubUsageCounter1_Object = MibTableColumn
mccpSubUsageCounter1 = _MccpSubUsageCounter1_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 20, 1, 3),
    _MccpSubUsageCounter1_Type()
)
mccpSubUsageCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpSubUsageCounter1.setStatus("current")


class _MccpSubUsageCounter2_Type(Integer32):
    """Custom type mccpSubUsageCounter2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubUsageCounter2_Type.__name__ = "Integer32"
_MccpSubUsageCounter2_Object = MibTableColumn
mccpSubUsageCounter2 = _MccpSubUsageCounter2_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 20, 1, 4),
    _MccpSubUsageCounter2_Type()
)
mccpSubUsageCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpSubUsageCounter2.setStatus("current")


class _MccpSubUsageCounter3_Type(Integer32):
    """Custom type mccpSubUsageCounter3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubUsageCounter3_Type.__name__ = "Integer32"
_MccpSubUsageCounter3_Object = MibTableColumn
mccpSubUsageCounter3 = _MccpSubUsageCounter3_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 20, 1, 5),
    _MccpSubUsageCounter3_Type()
)
mccpSubUsageCounter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpSubUsageCounter3.setStatus("current")


class _MccpSubUsageCounter4_Type(Integer32):
    """Custom type mccpSubUsageCounter4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpSubUsageCounter4_Type.__name__ = "Integer32"
_MccpSubUsageCounter4_Object = MibTableColumn
mccpSubUsageCounter4 = _MccpSubUsageCounter4_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 20, 1, 6),
    _MccpSubUsageCounter4_Type()
)
mccpSubUsageCounter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpSubUsageCounter4.setStatus("current")
_MccpRelcTgInTable_Object = MibTable
mccpRelcTgInTable = _MccpRelcTgInTable_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26)
)
if mibBuilder.loadTexts:
    mccpRelcTgInTable.setStatus("current")
_MccpRelcTgInEntry_Object = MibTableRow
mccpRelcTgInEntry = _MccpRelcTgInEntry_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1)
)
mccpRelcTgInEntry.setIndexNames(
    (0, "ELTEX-MCCP", "mccpRelcTgInIndex"),
)
if mibBuilder.loadTexts:
    mccpRelcTgInEntry.setStatus("current")


class _MccpRelcTgInIndex_Type(Integer32):
    """Custom type mccpRelcTgInIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MccpRelcTgInIndex_Type.__name__ = "Integer32"
_MccpRelcTgInIndex_Object = MibTableColumn
mccpRelcTgInIndex = _MccpRelcTgInIndex_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 1),
    _MccpRelcTgInIndex_Type()
)
mccpRelcTgInIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mccpRelcTgInIndex.setStatus("current")


class _MccpRelcTgInCounter0_Type(Integer32):
    """Custom type mccpRelcTgInCounter0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter0_Type.__name__ = "Integer32"
_MccpRelcTgInCounter0_Object = MibTableColumn
mccpRelcTgInCounter0 = _MccpRelcTgInCounter0_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 2),
    _MccpRelcTgInCounter0_Type()
)
mccpRelcTgInCounter0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter0.setStatus("current")


class _MccpRelcTgInCounter1_Type(Integer32):
    """Custom type mccpRelcTgInCounter1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter1_Type.__name__ = "Integer32"
_MccpRelcTgInCounter1_Object = MibTableColumn
mccpRelcTgInCounter1 = _MccpRelcTgInCounter1_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 3),
    _MccpRelcTgInCounter1_Type()
)
mccpRelcTgInCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter1.setStatus("current")


class _MccpRelcTgInCounter2_Type(Integer32):
    """Custom type mccpRelcTgInCounter2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter2_Type.__name__ = "Integer32"
_MccpRelcTgInCounter2_Object = MibTableColumn
mccpRelcTgInCounter2 = _MccpRelcTgInCounter2_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 4),
    _MccpRelcTgInCounter2_Type()
)
mccpRelcTgInCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter2.setStatus("current")


class _MccpRelcTgInCounter3_Type(Integer32):
    """Custom type mccpRelcTgInCounter3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter3_Type.__name__ = "Integer32"
_MccpRelcTgInCounter3_Object = MibTableColumn
mccpRelcTgInCounter3 = _MccpRelcTgInCounter3_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 5),
    _MccpRelcTgInCounter3_Type()
)
mccpRelcTgInCounter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter3.setStatus("current")


class _MccpRelcTgInCounter4_Type(Integer32):
    """Custom type mccpRelcTgInCounter4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter4_Type.__name__ = "Integer32"
_MccpRelcTgInCounter4_Object = MibTableColumn
mccpRelcTgInCounter4 = _MccpRelcTgInCounter4_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 6),
    _MccpRelcTgInCounter4_Type()
)
mccpRelcTgInCounter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter4.setStatus("current")


class _MccpRelcTgInCounter5_Type(Integer32):
    """Custom type mccpRelcTgInCounter5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter5_Type.__name__ = "Integer32"
_MccpRelcTgInCounter5_Object = MibTableColumn
mccpRelcTgInCounter5 = _MccpRelcTgInCounter5_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 7),
    _MccpRelcTgInCounter5_Type()
)
mccpRelcTgInCounter5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter5.setStatus("current")


class _MccpRelcTgInCounter6_Type(Integer32):
    """Custom type mccpRelcTgInCounter6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter6_Type.__name__ = "Integer32"
_MccpRelcTgInCounter6_Object = MibTableColumn
mccpRelcTgInCounter6 = _MccpRelcTgInCounter6_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 8),
    _MccpRelcTgInCounter6_Type()
)
mccpRelcTgInCounter6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter6.setStatus("current")


class _MccpRelcTgInCounter7_Type(Integer32):
    """Custom type mccpRelcTgInCounter7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter7_Type.__name__ = "Integer32"
_MccpRelcTgInCounter7_Object = MibTableColumn
mccpRelcTgInCounter7 = _MccpRelcTgInCounter7_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 9),
    _MccpRelcTgInCounter7_Type()
)
mccpRelcTgInCounter7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter7.setStatus("current")


class _MccpRelcTgInCounter8_Type(Integer32):
    """Custom type mccpRelcTgInCounter8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter8_Type.__name__ = "Integer32"
_MccpRelcTgInCounter8_Object = MibTableColumn
mccpRelcTgInCounter8 = _MccpRelcTgInCounter8_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 10),
    _MccpRelcTgInCounter8_Type()
)
mccpRelcTgInCounter8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter8.setStatus("current")


class _MccpRelcTgInCounter9_Type(Integer32):
    """Custom type mccpRelcTgInCounter9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter9_Type.__name__ = "Integer32"
_MccpRelcTgInCounter9_Object = MibTableColumn
mccpRelcTgInCounter9 = _MccpRelcTgInCounter9_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 11),
    _MccpRelcTgInCounter9_Type()
)
mccpRelcTgInCounter9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter9.setStatus("current")


class _MccpRelcTgInCounter10_Type(Integer32):
    """Custom type mccpRelcTgInCounter10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter10_Type.__name__ = "Integer32"
_MccpRelcTgInCounter10_Object = MibTableColumn
mccpRelcTgInCounter10 = _MccpRelcTgInCounter10_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 12),
    _MccpRelcTgInCounter10_Type()
)
mccpRelcTgInCounter10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter10.setStatus("current")


class _MccpRelcTgInCounter11_Type(Integer32):
    """Custom type mccpRelcTgInCounter11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter11_Type.__name__ = "Integer32"
_MccpRelcTgInCounter11_Object = MibTableColumn
mccpRelcTgInCounter11 = _MccpRelcTgInCounter11_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 13),
    _MccpRelcTgInCounter11_Type()
)
mccpRelcTgInCounter11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter11.setStatus("current")


class _MccpRelcTgInCounter12_Type(Integer32):
    """Custom type mccpRelcTgInCounter12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter12_Type.__name__ = "Integer32"
_MccpRelcTgInCounter12_Object = MibTableColumn
mccpRelcTgInCounter12 = _MccpRelcTgInCounter12_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 14),
    _MccpRelcTgInCounter12_Type()
)
mccpRelcTgInCounter12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter12.setStatus("current")


class _MccpRelcTgInCounter13_Type(Integer32):
    """Custom type mccpRelcTgInCounter13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter13_Type.__name__ = "Integer32"
_MccpRelcTgInCounter13_Object = MibTableColumn
mccpRelcTgInCounter13 = _MccpRelcTgInCounter13_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 15),
    _MccpRelcTgInCounter13_Type()
)
mccpRelcTgInCounter13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter13.setStatus("current")


class _MccpRelcTgInCounter14_Type(Integer32):
    """Custom type mccpRelcTgInCounter14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter14_Type.__name__ = "Integer32"
_MccpRelcTgInCounter14_Object = MibTableColumn
mccpRelcTgInCounter14 = _MccpRelcTgInCounter14_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 16),
    _MccpRelcTgInCounter14_Type()
)
mccpRelcTgInCounter14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter14.setStatus("current")


class _MccpRelcTgInCounter15_Type(Integer32):
    """Custom type mccpRelcTgInCounter15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter15_Type.__name__ = "Integer32"
_MccpRelcTgInCounter15_Object = MibTableColumn
mccpRelcTgInCounter15 = _MccpRelcTgInCounter15_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 17),
    _MccpRelcTgInCounter15_Type()
)
mccpRelcTgInCounter15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter15.setStatus("current")


class _MccpRelcTgInCounter16_Type(Integer32):
    """Custom type mccpRelcTgInCounter16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter16_Type.__name__ = "Integer32"
_MccpRelcTgInCounter16_Object = MibTableColumn
mccpRelcTgInCounter16 = _MccpRelcTgInCounter16_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 18),
    _MccpRelcTgInCounter16_Type()
)
mccpRelcTgInCounter16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter16.setStatus("current")


class _MccpRelcTgInCounter17_Type(Integer32):
    """Custom type mccpRelcTgInCounter17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter17_Type.__name__ = "Integer32"
_MccpRelcTgInCounter17_Object = MibTableColumn
mccpRelcTgInCounter17 = _MccpRelcTgInCounter17_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 19),
    _MccpRelcTgInCounter17_Type()
)
mccpRelcTgInCounter17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter17.setStatus("current")


class _MccpRelcTgInCounter18_Type(Integer32):
    """Custom type mccpRelcTgInCounter18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter18_Type.__name__ = "Integer32"
_MccpRelcTgInCounter18_Object = MibTableColumn
mccpRelcTgInCounter18 = _MccpRelcTgInCounter18_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 20),
    _MccpRelcTgInCounter18_Type()
)
mccpRelcTgInCounter18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter18.setStatus("current")


class _MccpRelcTgInCounter19_Type(Integer32):
    """Custom type mccpRelcTgInCounter19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter19_Type.__name__ = "Integer32"
_MccpRelcTgInCounter19_Object = MibTableColumn
mccpRelcTgInCounter19 = _MccpRelcTgInCounter19_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 21),
    _MccpRelcTgInCounter19_Type()
)
mccpRelcTgInCounter19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter19.setStatus("current")


class _MccpRelcTgInCounter20_Type(Integer32):
    """Custom type mccpRelcTgInCounter20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter20_Type.__name__ = "Integer32"
_MccpRelcTgInCounter20_Object = MibTableColumn
mccpRelcTgInCounter20 = _MccpRelcTgInCounter20_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 22),
    _MccpRelcTgInCounter20_Type()
)
mccpRelcTgInCounter20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter20.setStatus("current")


class _MccpRelcTgInCounter21_Type(Integer32):
    """Custom type mccpRelcTgInCounter21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter21_Type.__name__ = "Integer32"
_MccpRelcTgInCounter21_Object = MibTableColumn
mccpRelcTgInCounter21 = _MccpRelcTgInCounter21_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 23),
    _MccpRelcTgInCounter21_Type()
)
mccpRelcTgInCounter21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter21.setStatus("current")


class _MccpRelcTgInCounter22_Type(Integer32):
    """Custom type mccpRelcTgInCounter22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter22_Type.__name__ = "Integer32"
_MccpRelcTgInCounter22_Object = MibTableColumn
mccpRelcTgInCounter22 = _MccpRelcTgInCounter22_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 24),
    _MccpRelcTgInCounter22_Type()
)
mccpRelcTgInCounter22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter22.setStatus("current")


class _MccpRelcTgInCounter23_Type(Integer32):
    """Custom type mccpRelcTgInCounter23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter23_Type.__name__ = "Integer32"
_MccpRelcTgInCounter23_Object = MibTableColumn
mccpRelcTgInCounter23 = _MccpRelcTgInCounter23_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 25),
    _MccpRelcTgInCounter23_Type()
)
mccpRelcTgInCounter23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter23.setStatus("current")


class _MccpRelcTgInCounter24_Type(Integer32):
    """Custom type mccpRelcTgInCounter24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter24_Type.__name__ = "Integer32"
_MccpRelcTgInCounter24_Object = MibTableColumn
mccpRelcTgInCounter24 = _MccpRelcTgInCounter24_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 26),
    _MccpRelcTgInCounter24_Type()
)
mccpRelcTgInCounter24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter24.setStatus("current")


class _MccpRelcTgInCounter25_Type(Integer32):
    """Custom type mccpRelcTgInCounter25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter25_Type.__name__ = "Integer32"
_MccpRelcTgInCounter25_Object = MibTableColumn
mccpRelcTgInCounter25 = _MccpRelcTgInCounter25_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 27),
    _MccpRelcTgInCounter25_Type()
)
mccpRelcTgInCounter25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter25.setStatus("current")


class _MccpRelcTgInCounter26_Type(Integer32):
    """Custom type mccpRelcTgInCounter26 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter26_Type.__name__ = "Integer32"
_MccpRelcTgInCounter26_Object = MibTableColumn
mccpRelcTgInCounter26 = _MccpRelcTgInCounter26_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 28),
    _MccpRelcTgInCounter26_Type()
)
mccpRelcTgInCounter26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter26.setStatus("current")


class _MccpRelcTgInCounter27_Type(Integer32):
    """Custom type mccpRelcTgInCounter27 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter27_Type.__name__ = "Integer32"
_MccpRelcTgInCounter27_Object = MibTableColumn
mccpRelcTgInCounter27 = _MccpRelcTgInCounter27_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 29),
    _MccpRelcTgInCounter27_Type()
)
mccpRelcTgInCounter27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter27.setStatus("current")


class _MccpRelcTgInCounter28_Type(Integer32):
    """Custom type mccpRelcTgInCounter28 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter28_Type.__name__ = "Integer32"
_MccpRelcTgInCounter28_Object = MibTableColumn
mccpRelcTgInCounter28 = _MccpRelcTgInCounter28_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 30),
    _MccpRelcTgInCounter28_Type()
)
mccpRelcTgInCounter28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter28.setStatus("current")


class _MccpRelcTgInCounter29_Type(Integer32):
    """Custom type mccpRelcTgInCounter29 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter29_Type.__name__ = "Integer32"
_MccpRelcTgInCounter29_Object = MibTableColumn
mccpRelcTgInCounter29 = _MccpRelcTgInCounter29_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 31),
    _MccpRelcTgInCounter29_Type()
)
mccpRelcTgInCounter29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter29.setStatus("current")


class _MccpRelcTgInCounter30_Type(Integer32):
    """Custom type mccpRelcTgInCounter30 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter30_Type.__name__ = "Integer32"
_MccpRelcTgInCounter30_Object = MibTableColumn
mccpRelcTgInCounter30 = _MccpRelcTgInCounter30_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 32),
    _MccpRelcTgInCounter30_Type()
)
mccpRelcTgInCounter30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter30.setStatus("current")


class _MccpRelcTgInCounter31_Type(Integer32):
    """Custom type mccpRelcTgInCounter31 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter31_Type.__name__ = "Integer32"
_MccpRelcTgInCounter31_Object = MibTableColumn
mccpRelcTgInCounter31 = _MccpRelcTgInCounter31_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 33),
    _MccpRelcTgInCounter31_Type()
)
mccpRelcTgInCounter31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter31.setStatus("current")


class _MccpRelcTgInCounter32_Type(Integer32):
    """Custom type mccpRelcTgInCounter32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter32_Type.__name__ = "Integer32"
_MccpRelcTgInCounter32_Object = MibTableColumn
mccpRelcTgInCounter32 = _MccpRelcTgInCounter32_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 34),
    _MccpRelcTgInCounter32_Type()
)
mccpRelcTgInCounter32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter32.setStatus("current")


class _MccpRelcTgInCounter33_Type(Integer32):
    """Custom type mccpRelcTgInCounter33 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter33_Type.__name__ = "Integer32"
_MccpRelcTgInCounter33_Object = MibTableColumn
mccpRelcTgInCounter33 = _MccpRelcTgInCounter33_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 35),
    _MccpRelcTgInCounter33_Type()
)
mccpRelcTgInCounter33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter33.setStatus("current")


class _MccpRelcTgInCounter34_Type(Integer32):
    """Custom type mccpRelcTgInCounter34 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter34_Type.__name__ = "Integer32"
_MccpRelcTgInCounter34_Object = MibTableColumn
mccpRelcTgInCounter34 = _MccpRelcTgInCounter34_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 36),
    _MccpRelcTgInCounter34_Type()
)
mccpRelcTgInCounter34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter34.setStatus("current")


class _MccpRelcTgInCounter35_Type(Integer32):
    """Custom type mccpRelcTgInCounter35 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter35_Type.__name__ = "Integer32"
_MccpRelcTgInCounter35_Object = MibTableColumn
mccpRelcTgInCounter35 = _MccpRelcTgInCounter35_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 37),
    _MccpRelcTgInCounter35_Type()
)
mccpRelcTgInCounter35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter35.setStatus("current")


class _MccpRelcTgInCounter36_Type(Integer32):
    """Custom type mccpRelcTgInCounter36 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter36_Type.__name__ = "Integer32"
_MccpRelcTgInCounter36_Object = MibTableColumn
mccpRelcTgInCounter36 = _MccpRelcTgInCounter36_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 38),
    _MccpRelcTgInCounter36_Type()
)
mccpRelcTgInCounter36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter36.setStatus("current")


class _MccpRelcTgInCounter37_Type(Integer32):
    """Custom type mccpRelcTgInCounter37 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter37_Type.__name__ = "Integer32"
_MccpRelcTgInCounter37_Object = MibTableColumn
mccpRelcTgInCounter37 = _MccpRelcTgInCounter37_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 39),
    _MccpRelcTgInCounter37_Type()
)
mccpRelcTgInCounter37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter37.setStatus("current")


class _MccpRelcTgInCounter38_Type(Integer32):
    """Custom type mccpRelcTgInCounter38 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter38_Type.__name__ = "Integer32"
_MccpRelcTgInCounter38_Object = MibTableColumn
mccpRelcTgInCounter38 = _MccpRelcTgInCounter38_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 40),
    _MccpRelcTgInCounter38_Type()
)
mccpRelcTgInCounter38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter38.setStatus("current")


class _MccpRelcTgInCounter39_Type(Integer32):
    """Custom type mccpRelcTgInCounter39 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter39_Type.__name__ = "Integer32"
_MccpRelcTgInCounter39_Object = MibTableColumn
mccpRelcTgInCounter39 = _MccpRelcTgInCounter39_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 41),
    _MccpRelcTgInCounter39_Type()
)
mccpRelcTgInCounter39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter39.setStatus("current")


class _MccpRelcTgInCounter40_Type(Integer32):
    """Custom type mccpRelcTgInCounter40 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter40_Type.__name__ = "Integer32"
_MccpRelcTgInCounter40_Object = MibTableColumn
mccpRelcTgInCounter40 = _MccpRelcTgInCounter40_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 42),
    _MccpRelcTgInCounter40_Type()
)
mccpRelcTgInCounter40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter40.setStatus("current")


class _MccpRelcTgInCounter41_Type(Integer32):
    """Custom type mccpRelcTgInCounter41 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter41_Type.__name__ = "Integer32"
_MccpRelcTgInCounter41_Object = MibTableColumn
mccpRelcTgInCounter41 = _MccpRelcTgInCounter41_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 43),
    _MccpRelcTgInCounter41_Type()
)
mccpRelcTgInCounter41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter41.setStatus("current")


class _MccpRelcTgInCounter42_Type(Integer32):
    """Custom type mccpRelcTgInCounter42 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter42_Type.__name__ = "Integer32"
_MccpRelcTgInCounter42_Object = MibTableColumn
mccpRelcTgInCounter42 = _MccpRelcTgInCounter42_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 44),
    _MccpRelcTgInCounter42_Type()
)
mccpRelcTgInCounter42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter42.setStatus("current")


class _MccpRelcTgInCounter43_Type(Integer32):
    """Custom type mccpRelcTgInCounter43 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter43_Type.__name__ = "Integer32"
_MccpRelcTgInCounter43_Object = MibTableColumn
mccpRelcTgInCounter43 = _MccpRelcTgInCounter43_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 45),
    _MccpRelcTgInCounter43_Type()
)
mccpRelcTgInCounter43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter43.setStatus("current")


class _MccpRelcTgInCounter44_Type(Integer32):
    """Custom type mccpRelcTgInCounter44 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter44_Type.__name__ = "Integer32"
_MccpRelcTgInCounter44_Object = MibTableColumn
mccpRelcTgInCounter44 = _MccpRelcTgInCounter44_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 46),
    _MccpRelcTgInCounter44_Type()
)
mccpRelcTgInCounter44.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter44.setStatus("current")


class _MccpRelcTgInCounter45_Type(Integer32):
    """Custom type mccpRelcTgInCounter45 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter45_Type.__name__ = "Integer32"
_MccpRelcTgInCounter45_Object = MibTableColumn
mccpRelcTgInCounter45 = _MccpRelcTgInCounter45_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 47),
    _MccpRelcTgInCounter45_Type()
)
mccpRelcTgInCounter45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter45.setStatus("current")


class _MccpRelcTgInCounter46_Type(Integer32):
    """Custom type mccpRelcTgInCounter46 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter46_Type.__name__ = "Integer32"
_MccpRelcTgInCounter46_Object = MibTableColumn
mccpRelcTgInCounter46 = _MccpRelcTgInCounter46_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 48),
    _MccpRelcTgInCounter46_Type()
)
mccpRelcTgInCounter46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter46.setStatus("current")


class _MccpRelcTgInCounter47_Type(Integer32):
    """Custom type mccpRelcTgInCounter47 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter47_Type.__name__ = "Integer32"
_MccpRelcTgInCounter47_Object = MibTableColumn
mccpRelcTgInCounter47 = _MccpRelcTgInCounter47_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 49),
    _MccpRelcTgInCounter47_Type()
)
mccpRelcTgInCounter47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter47.setStatus("current")


class _MccpRelcTgInCounter48_Type(Integer32):
    """Custom type mccpRelcTgInCounter48 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter48_Type.__name__ = "Integer32"
_MccpRelcTgInCounter48_Object = MibTableColumn
mccpRelcTgInCounter48 = _MccpRelcTgInCounter48_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 50),
    _MccpRelcTgInCounter48_Type()
)
mccpRelcTgInCounter48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter48.setStatus("current")


class _MccpRelcTgInCounter49_Type(Integer32):
    """Custom type mccpRelcTgInCounter49 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter49_Type.__name__ = "Integer32"
_MccpRelcTgInCounter49_Object = MibTableColumn
mccpRelcTgInCounter49 = _MccpRelcTgInCounter49_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 51),
    _MccpRelcTgInCounter49_Type()
)
mccpRelcTgInCounter49.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter49.setStatus("current")


class _MccpRelcTgInCounter50_Type(Integer32):
    """Custom type mccpRelcTgInCounter50 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter50_Type.__name__ = "Integer32"
_MccpRelcTgInCounter50_Object = MibTableColumn
mccpRelcTgInCounter50 = _MccpRelcTgInCounter50_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 52),
    _MccpRelcTgInCounter50_Type()
)
mccpRelcTgInCounter50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter50.setStatus("current")


class _MccpRelcTgInCounter51_Type(Integer32):
    """Custom type mccpRelcTgInCounter51 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter51_Type.__name__ = "Integer32"
_MccpRelcTgInCounter51_Object = MibTableColumn
mccpRelcTgInCounter51 = _MccpRelcTgInCounter51_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 53),
    _MccpRelcTgInCounter51_Type()
)
mccpRelcTgInCounter51.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter51.setStatus("current")


class _MccpRelcTgInCounter52_Type(Integer32):
    """Custom type mccpRelcTgInCounter52 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter52_Type.__name__ = "Integer32"
_MccpRelcTgInCounter52_Object = MibTableColumn
mccpRelcTgInCounter52 = _MccpRelcTgInCounter52_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 54),
    _MccpRelcTgInCounter52_Type()
)
mccpRelcTgInCounter52.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter52.setStatus("current")


class _MccpRelcTgInCounter53_Type(Integer32):
    """Custom type mccpRelcTgInCounter53 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter53_Type.__name__ = "Integer32"
_MccpRelcTgInCounter53_Object = MibTableColumn
mccpRelcTgInCounter53 = _MccpRelcTgInCounter53_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 55),
    _MccpRelcTgInCounter53_Type()
)
mccpRelcTgInCounter53.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter53.setStatus("current")


class _MccpRelcTgInCounter54_Type(Integer32):
    """Custom type mccpRelcTgInCounter54 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter54_Type.__name__ = "Integer32"
_MccpRelcTgInCounter54_Object = MibTableColumn
mccpRelcTgInCounter54 = _MccpRelcTgInCounter54_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 56),
    _MccpRelcTgInCounter54_Type()
)
mccpRelcTgInCounter54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter54.setStatus("current")


class _MccpRelcTgInCounter55_Type(Integer32):
    """Custom type mccpRelcTgInCounter55 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter55_Type.__name__ = "Integer32"
_MccpRelcTgInCounter55_Object = MibTableColumn
mccpRelcTgInCounter55 = _MccpRelcTgInCounter55_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 57),
    _MccpRelcTgInCounter55_Type()
)
mccpRelcTgInCounter55.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter55.setStatus("current")


class _MccpRelcTgInCounter56_Type(Integer32):
    """Custom type mccpRelcTgInCounter56 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter56_Type.__name__ = "Integer32"
_MccpRelcTgInCounter56_Object = MibTableColumn
mccpRelcTgInCounter56 = _MccpRelcTgInCounter56_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 58),
    _MccpRelcTgInCounter56_Type()
)
mccpRelcTgInCounter56.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter56.setStatus("current")


class _MccpRelcTgInCounter57_Type(Integer32):
    """Custom type mccpRelcTgInCounter57 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter57_Type.__name__ = "Integer32"
_MccpRelcTgInCounter57_Object = MibTableColumn
mccpRelcTgInCounter57 = _MccpRelcTgInCounter57_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 59),
    _MccpRelcTgInCounter57_Type()
)
mccpRelcTgInCounter57.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter57.setStatus("current")


class _MccpRelcTgInCounter58_Type(Integer32):
    """Custom type mccpRelcTgInCounter58 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter58_Type.__name__ = "Integer32"
_MccpRelcTgInCounter58_Object = MibTableColumn
mccpRelcTgInCounter58 = _MccpRelcTgInCounter58_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 60),
    _MccpRelcTgInCounter58_Type()
)
mccpRelcTgInCounter58.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter58.setStatus("current")


class _MccpRelcTgInCounter59_Type(Integer32):
    """Custom type mccpRelcTgInCounter59 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter59_Type.__name__ = "Integer32"
_MccpRelcTgInCounter59_Object = MibTableColumn
mccpRelcTgInCounter59 = _MccpRelcTgInCounter59_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 61),
    _MccpRelcTgInCounter59_Type()
)
mccpRelcTgInCounter59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter59.setStatus("current")


class _MccpRelcTgInCounter60_Type(Integer32):
    """Custom type mccpRelcTgInCounter60 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter60_Type.__name__ = "Integer32"
_MccpRelcTgInCounter60_Object = MibTableColumn
mccpRelcTgInCounter60 = _MccpRelcTgInCounter60_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 62),
    _MccpRelcTgInCounter60_Type()
)
mccpRelcTgInCounter60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter60.setStatus("current")


class _MccpRelcTgInCounter61_Type(Integer32):
    """Custom type mccpRelcTgInCounter61 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter61_Type.__name__ = "Integer32"
_MccpRelcTgInCounter61_Object = MibTableColumn
mccpRelcTgInCounter61 = _MccpRelcTgInCounter61_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 63),
    _MccpRelcTgInCounter61_Type()
)
mccpRelcTgInCounter61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter61.setStatus("current")


class _MccpRelcTgInCounter62_Type(Integer32):
    """Custom type mccpRelcTgInCounter62 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter62_Type.__name__ = "Integer32"
_MccpRelcTgInCounter62_Object = MibTableColumn
mccpRelcTgInCounter62 = _MccpRelcTgInCounter62_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 64),
    _MccpRelcTgInCounter62_Type()
)
mccpRelcTgInCounter62.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter62.setStatus("current")


class _MccpRelcTgInCounter63_Type(Integer32):
    """Custom type mccpRelcTgInCounter63 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter63_Type.__name__ = "Integer32"
_MccpRelcTgInCounter63_Object = MibTableColumn
mccpRelcTgInCounter63 = _MccpRelcTgInCounter63_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 65),
    _MccpRelcTgInCounter63_Type()
)
mccpRelcTgInCounter63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter63.setStatus("current")


class _MccpRelcTgInCounter64_Type(Integer32):
    """Custom type mccpRelcTgInCounter64 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter64_Type.__name__ = "Integer32"
_MccpRelcTgInCounter64_Object = MibTableColumn
mccpRelcTgInCounter64 = _MccpRelcTgInCounter64_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 66),
    _MccpRelcTgInCounter64_Type()
)
mccpRelcTgInCounter64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter64.setStatus("current")


class _MccpRelcTgInCounter65_Type(Integer32):
    """Custom type mccpRelcTgInCounter65 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter65_Type.__name__ = "Integer32"
_MccpRelcTgInCounter65_Object = MibTableColumn
mccpRelcTgInCounter65 = _MccpRelcTgInCounter65_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 67),
    _MccpRelcTgInCounter65_Type()
)
mccpRelcTgInCounter65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter65.setStatus("current")


class _MccpRelcTgInCounter66_Type(Integer32):
    """Custom type mccpRelcTgInCounter66 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter66_Type.__name__ = "Integer32"
_MccpRelcTgInCounter66_Object = MibTableColumn
mccpRelcTgInCounter66 = _MccpRelcTgInCounter66_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 68),
    _MccpRelcTgInCounter66_Type()
)
mccpRelcTgInCounter66.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter66.setStatus("current")


class _MccpRelcTgInCounter67_Type(Integer32):
    """Custom type mccpRelcTgInCounter67 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter67_Type.__name__ = "Integer32"
_MccpRelcTgInCounter67_Object = MibTableColumn
mccpRelcTgInCounter67 = _MccpRelcTgInCounter67_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 69),
    _MccpRelcTgInCounter67_Type()
)
mccpRelcTgInCounter67.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter67.setStatus("current")


class _MccpRelcTgInCounter68_Type(Integer32):
    """Custom type mccpRelcTgInCounter68 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter68_Type.__name__ = "Integer32"
_MccpRelcTgInCounter68_Object = MibTableColumn
mccpRelcTgInCounter68 = _MccpRelcTgInCounter68_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 70),
    _MccpRelcTgInCounter68_Type()
)
mccpRelcTgInCounter68.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter68.setStatus("current")


class _MccpRelcTgInCounter69_Type(Integer32):
    """Custom type mccpRelcTgInCounter69 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter69_Type.__name__ = "Integer32"
_MccpRelcTgInCounter69_Object = MibTableColumn
mccpRelcTgInCounter69 = _MccpRelcTgInCounter69_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 71),
    _MccpRelcTgInCounter69_Type()
)
mccpRelcTgInCounter69.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter69.setStatus("current")


class _MccpRelcTgInCounter70_Type(Integer32):
    """Custom type mccpRelcTgInCounter70 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter70_Type.__name__ = "Integer32"
_MccpRelcTgInCounter70_Object = MibTableColumn
mccpRelcTgInCounter70 = _MccpRelcTgInCounter70_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 72),
    _MccpRelcTgInCounter70_Type()
)
mccpRelcTgInCounter70.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter70.setStatus("current")


class _MccpRelcTgInCounter71_Type(Integer32):
    """Custom type mccpRelcTgInCounter71 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter71_Type.__name__ = "Integer32"
_MccpRelcTgInCounter71_Object = MibTableColumn
mccpRelcTgInCounter71 = _MccpRelcTgInCounter71_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 73),
    _MccpRelcTgInCounter71_Type()
)
mccpRelcTgInCounter71.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter71.setStatus("current")


class _MccpRelcTgInCounter72_Type(Integer32):
    """Custom type mccpRelcTgInCounter72 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter72_Type.__name__ = "Integer32"
_MccpRelcTgInCounter72_Object = MibTableColumn
mccpRelcTgInCounter72 = _MccpRelcTgInCounter72_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 74),
    _MccpRelcTgInCounter72_Type()
)
mccpRelcTgInCounter72.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter72.setStatus("current")


class _MccpRelcTgInCounter73_Type(Integer32):
    """Custom type mccpRelcTgInCounter73 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter73_Type.__name__ = "Integer32"
_MccpRelcTgInCounter73_Object = MibTableColumn
mccpRelcTgInCounter73 = _MccpRelcTgInCounter73_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 75),
    _MccpRelcTgInCounter73_Type()
)
mccpRelcTgInCounter73.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter73.setStatus("current")


class _MccpRelcTgInCounter74_Type(Integer32):
    """Custom type mccpRelcTgInCounter74 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter74_Type.__name__ = "Integer32"
_MccpRelcTgInCounter74_Object = MibTableColumn
mccpRelcTgInCounter74 = _MccpRelcTgInCounter74_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 76),
    _MccpRelcTgInCounter74_Type()
)
mccpRelcTgInCounter74.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter74.setStatus("current")


class _MccpRelcTgInCounter75_Type(Integer32):
    """Custom type mccpRelcTgInCounter75 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter75_Type.__name__ = "Integer32"
_MccpRelcTgInCounter75_Object = MibTableColumn
mccpRelcTgInCounter75 = _MccpRelcTgInCounter75_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 77),
    _MccpRelcTgInCounter75_Type()
)
mccpRelcTgInCounter75.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter75.setStatus("current")


class _MccpRelcTgInCounter76_Type(Integer32):
    """Custom type mccpRelcTgInCounter76 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter76_Type.__name__ = "Integer32"
_MccpRelcTgInCounter76_Object = MibTableColumn
mccpRelcTgInCounter76 = _MccpRelcTgInCounter76_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 78),
    _MccpRelcTgInCounter76_Type()
)
mccpRelcTgInCounter76.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter76.setStatus("current")


class _MccpRelcTgInCounter77_Type(Integer32):
    """Custom type mccpRelcTgInCounter77 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter77_Type.__name__ = "Integer32"
_MccpRelcTgInCounter77_Object = MibTableColumn
mccpRelcTgInCounter77 = _MccpRelcTgInCounter77_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 79),
    _MccpRelcTgInCounter77_Type()
)
mccpRelcTgInCounter77.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter77.setStatus("current")


class _MccpRelcTgInCounter78_Type(Integer32):
    """Custom type mccpRelcTgInCounter78 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter78_Type.__name__ = "Integer32"
_MccpRelcTgInCounter78_Object = MibTableColumn
mccpRelcTgInCounter78 = _MccpRelcTgInCounter78_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 80),
    _MccpRelcTgInCounter78_Type()
)
mccpRelcTgInCounter78.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter78.setStatus("current")


class _MccpRelcTgInCounter79_Type(Integer32):
    """Custom type mccpRelcTgInCounter79 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter79_Type.__name__ = "Integer32"
_MccpRelcTgInCounter79_Object = MibTableColumn
mccpRelcTgInCounter79 = _MccpRelcTgInCounter79_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 81),
    _MccpRelcTgInCounter79_Type()
)
mccpRelcTgInCounter79.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter79.setStatus("current")


class _MccpRelcTgInCounter80_Type(Integer32):
    """Custom type mccpRelcTgInCounter80 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter80_Type.__name__ = "Integer32"
_MccpRelcTgInCounter80_Object = MibTableColumn
mccpRelcTgInCounter80 = _MccpRelcTgInCounter80_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 82),
    _MccpRelcTgInCounter80_Type()
)
mccpRelcTgInCounter80.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter80.setStatus("current")


class _MccpRelcTgInCounter81_Type(Integer32):
    """Custom type mccpRelcTgInCounter81 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter81_Type.__name__ = "Integer32"
_MccpRelcTgInCounter81_Object = MibTableColumn
mccpRelcTgInCounter81 = _MccpRelcTgInCounter81_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 83),
    _MccpRelcTgInCounter81_Type()
)
mccpRelcTgInCounter81.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter81.setStatus("current")


class _MccpRelcTgInCounter82_Type(Integer32):
    """Custom type mccpRelcTgInCounter82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter82_Type.__name__ = "Integer32"
_MccpRelcTgInCounter82_Object = MibTableColumn
mccpRelcTgInCounter82 = _MccpRelcTgInCounter82_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 84),
    _MccpRelcTgInCounter82_Type()
)
mccpRelcTgInCounter82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter82.setStatus("current")


class _MccpRelcTgInCounter83_Type(Integer32):
    """Custom type mccpRelcTgInCounter83 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter83_Type.__name__ = "Integer32"
_MccpRelcTgInCounter83_Object = MibTableColumn
mccpRelcTgInCounter83 = _MccpRelcTgInCounter83_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 85),
    _MccpRelcTgInCounter83_Type()
)
mccpRelcTgInCounter83.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter83.setStatus("current")


class _MccpRelcTgInCounter84_Type(Integer32):
    """Custom type mccpRelcTgInCounter84 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter84_Type.__name__ = "Integer32"
_MccpRelcTgInCounter84_Object = MibTableColumn
mccpRelcTgInCounter84 = _MccpRelcTgInCounter84_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 86),
    _MccpRelcTgInCounter84_Type()
)
mccpRelcTgInCounter84.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter84.setStatus("current")


class _MccpRelcTgInCounter85_Type(Integer32):
    """Custom type mccpRelcTgInCounter85 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter85_Type.__name__ = "Integer32"
_MccpRelcTgInCounter85_Object = MibTableColumn
mccpRelcTgInCounter85 = _MccpRelcTgInCounter85_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 87),
    _MccpRelcTgInCounter85_Type()
)
mccpRelcTgInCounter85.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter85.setStatus("current")


class _MccpRelcTgInCounter86_Type(Integer32):
    """Custom type mccpRelcTgInCounter86 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter86_Type.__name__ = "Integer32"
_MccpRelcTgInCounter86_Object = MibTableColumn
mccpRelcTgInCounter86 = _MccpRelcTgInCounter86_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 88),
    _MccpRelcTgInCounter86_Type()
)
mccpRelcTgInCounter86.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter86.setStatus("current")


class _MccpRelcTgInCounter87_Type(Integer32):
    """Custom type mccpRelcTgInCounter87 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter87_Type.__name__ = "Integer32"
_MccpRelcTgInCounter87_Object = MibTableColumn
mccpRelcTgInCounter87 = _MccpRelcTgInCounter87_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 89),
    _MccpRelcTgInCounter87_Type()
)
mccpRelcTgInCounter87.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter87.setStatus("current")


class _MccpRelcTgInCounter88_Type(Integer32):
    """Custom type mccpRelcTgInCounter88 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter88_Type.__name__ = "Integer32"
_MccpRelcTgInCounter88_Object = MibTableColumn
mccpRelcTgInCounter88 = _MccpRelcTgInCounter88_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 90),
    _MccpRelcTgInCounter88_Type()
)
mccpRelcTgInCounter88.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter88.setStatus("current")


class _MccpRelcTgInCounter89_Type(Integer32):
    """Custom type mccpRelcTgInCounter89 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter89_Type.__name__ = "Integer32"
_MccpRelcTgInCounter89_Object = MibTableColumn
mccpRelcTgInCounter89 = _MccpRelcTgInCounter89_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 91),
    _MccpRelcTgInCounter89_Type()
)
mccpRelcTgInCounter89.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter89.setStatus("current")


class _MccpRelcTgInCounter90_Type(Integer32):
    """Custom type mccpRelcTgInCounter90 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter90_Type.__name__ = "Integer32"
_MccpRelcTgInCounter90_Object = MibTableColumn
mccpRelcTgInCounter90 = _MccpRelcTgInCounter90_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 92),
    _MccpRelcTgInCounter90_Type()
)
mccpRelcTgInCounter90.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter90.setStatus("current")


class _MccpRelcTgInCounter91_Type(Integer32):
    """Custom type mccpRelcTgInCounter91 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter91_Type.__name__ = "Integer32"
_MccpRelcTgInCounter91_Object = MibTableColumn
mccpRelcTgInCounter91 = _MccpRelcTgInCounter91_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 93),
    _MccpRelcTgInCounter91_Type()
)
mccpRelcTgInCounter91.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter91.setStatus("current")


class _MccpRelcTgInCounter92_Type(Integer32):
    """Custom type mccpRelcTgInCounter92 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter92_Type.__name__ = "Integer32"
_MccpRelcTgInCounter92_Object = MibTableColumn
mccpRelcTgInCounter92 = _MccpRelcTgInCounter92_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 94),
    _MccpRelcTgInCounter92_Type()
)
mccpRelcTgInCounter92.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter92.setStatus("current")


class _MccpRelcTgInCounter93_Type(Integer32):
    """Custom type mccpRelcTgInCounter93 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter93_Type.__name__ = "Integer32"
_MccpRelcTgInCounter93_Object = MibTableColumn
mccpRelcTgInCounter93 = _MccpRelcTgInCounter93_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 95),
    _MccpRelcTgInCounter93_Type()
)
mccpRelcTgInCounter93.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter93.setStatus("current")


class _MccpRelcTgInCounter94_Type(Integer32):
    """Custom type mccpRelcTgInCounter94 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter94_Type.__name__ = "Integer32"
_MccpRelcTgInCounter94_Object = MibTableColumn
mccpRelcTgInCounter94 = _MccpRelcTgInCounter94_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 96),
    _MccpRelcTgInCounter94_Type()
)
mccpRelcTgInCounter94.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter94.setStatus("current")


class _MccpRelcTgInCounter95_Type(Integer32):
    """Custom type mccpRelcTgInCounter95 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter95_Type.__name__ = "Integer32"
_MccpRelcTgInCounter95_Object = MibTableColumn
mccpRelcTgInCounter95 = _MccpRelcTgInCounter95_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 97),
    _MccpRelcTgInCounter95_Type()
)
mccpRelcTgInCounter95.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter95.setStatus("current")


class _MccpRelcTgInCounter96_Type(Integer32):
    """Custom type mccpRelcTgInCounter96 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter96_Type.__name__ = "Integer32"
_MccpRelcTgInCounter96_Object = MibTableColumn
mccpRelcTgInCounter96 = _MccpRelcTgInCounter96_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 98),
    _MccpRelcTgInCounter96_Type()
)
mccpRelcTgInCounter96.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter96.setStatus("current")


class _MccpRelcTgInCounter97_Type(Integer32):
    """Custom type mccpRelcTgInCounter97 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter97_Type.__name__ = "Integer32"
_MccpRelcTgInCounter97_Object = MibTableColumn
mccpRelcTgInCounter97 = _MccpRelcTgInCounter97_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 99),
    _MccpRelcTgInCounter97_Type()
)
mccpRelcTgInCounter97.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter97.setStatus("current")


class _MccpRelcTgInCounter98_Type(Integer32):
    """Custom type mccpRelcTgInCounter98 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter98_Type.__name__ = "Integer32"
_MccpRelcTgInCounter98_Object = MibTableColumn
mccpRelcTgInCounter98 = _MccpRelcTgInCounter98_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 100),
    _MccpRelcTgInCounter98_Type()
)
mccpRelcTgInCounter98.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter98.setStatus("current")


class _MccpRelcTgInCounter99_Type(Integer32):
    """Custom type mccpRelcTgInCounter99 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter99_Type.__name__ = "Integer32"
_MccpRelcTgInCounter99_Object = MibTableColumn
mccpRelcTgInCounter99 = _MccpRelcTgInCounter99_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 101),
    _MccpRelcTgInCounter99_Type()
)
mccpRelcTgInCounter99.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter99.setStatus("current")


class _MccpRelcTgInCounter100_Type(Integer32):
    """Custom type mccpRelcTgInCounter100 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter100_Type.__name__ = "Integer32"
_MccpRelcTgInCounter100_Object = MibTableColumn
mccpRelcTgInCounter100 = _MccpRelcTgInCounter100_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 102),
    _MccpRelcTgInCounter100_Type()
)
mccpRelcTgInCounter100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter100.setStatus("current")


class _MccpRelcTgInCounter101_Type(Integer32):
    """Custom type mccpRelcTgInCounter101 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter101_Type.__name__ = "Integer32"
_MccpRelcTgInCounter101_Object = MibTableColumn
mccpRelcTgInCounter101 = _MccpRelcTgInCounter101_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 103),
    _MccpRelcTgInCounter101_Type()
)
mccpRelcTgInCounter101.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter101.setStatus("current")


class _MccpRelcTgInCounter102_Type(Integer32):
    """Custom type mccpRelcTgInCounter102 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter102_Type.__name__ = "Integer32"
_MccpRelcTgInCounter102_Object = MibTableColumn
mccpRelcTgInCounter102 = _MccpRelcTgInCounter102_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 104),
    _MccpRelcTgInCounter102_Type()
)
mccpRelcTgInCounter102.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter102.setStatus("current")


class _MccpRelcTgInCounter103_Type(Integer32):
    """Custom type mccpRelcTgInCounter103 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter103_Type.__name__ = "Integer32"
_MccpRelcTgInCounter103_Object = MibTableColumn
mccpRelcTgInCounter103 = _MccpRelcTgInCounter103_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 105),
    _MccpRelcTgInCounter103_Type()
)
mccpRelcTgInCounter103.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter103.setStatus("current")


class _MccpRelcTgInCounter104_Type(Integer32):
    """Custom type mccpRelcTgInCounter104 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter104_Type.__name__ = "Integer32"
_MccpRelcTgInCounter104_Object = MibTableColumn
mccpRelcTgInCounter104 = _MccpRelcTgInCounter104_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 106),
    _MccpRelcTgInCounter104_Type()
)
mccpRelcTgInCounter104.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter104.setStatus("current")


class _MccpRelcTgInCounter105_Type(Integer32):
    """Custom type mccpRelcTgInCounter105 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter105_Type.__name__ = "Integer32"
_MccpRelcTgInCounter105_Object = MibTableColumn
mccpRelcTgInCounter105 = _MccpRelcTgInCounter105_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 107),
    _MccpRelcTgInCounter105_Type()
)
mccpRelcTgInCounter105.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter105.setStatus("current")


class _MccpRelcTgInCounter106_Type(Integer32):
    """Custom type mccpRelcTgInCounter106 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter106_Type.__name__ = "Integer32"
_MccpRelcTgInCounter106_Object = MibTableColumn
mccpRelcTgInCounter106 = _MccpRelcTgInCounter106_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 108),
    _MccpRelcTgInCounter106_Type()
)
mccpRelcTgInCounter106.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter106.setStatus("current")


class _MccpRelcTgInCounter107_Type(Integer32):
    """Custom type mccpRelcTgInCounter107 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter107_Type.__name__ = "Integer32"
_MccpRelcTgInCounter107_Object = MibTableColumn
mccpRelcTgInCounter107 = _MccpRelcTgInCounter107_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 109),
    _MccpRelcTgInCounter107_Type()
)
mccpRelcTgInCounter107.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter107.setStatus("current")


class _MccpRelcTgInCounter108_Type(Integer32):
    """Custom type mccpRelcTgInCounter108 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter108_Type.__name__ = "Integer32"
_MccpRelcTgInCounter108_Object = MibTableColumn
mccpRelcTgInCounter108 = _MccpRelcTgInCounter108_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 110),
    _MccpRelcTgInCounter108_Type()
)
mccpRelcTgInCounter108.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter108.setStatus("current")


class _MccpRelcTgInCounter109_Type(Integer32):
    """Custom type mccpRelcTgInCounter109 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter109_Type.__name__ = "Integer32"
_MccpRelcTgInCounter109_Object = MibTableColumn
mccpRelcTgInCounter109 = _MccpRelcTgInCounter109_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 111),
    _MccpRelcTgInCounter109_Type()
)
mccpRelcTgInCounter109.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter109.setStatus("current")


class _MccpRelcTgInCounter110_Type(Integer32):
    """Custom type mccpRelcTgInCounter110 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter110_Type.__name__ = "Integer32"
_MccpRelcTgInCounter110_Object = MibTableColumn
mccpRelcTgInCounter110 = _MccpRelcTgInCounter110_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 112),
    _MccpRelcTgInCounter110_Type()
)
mccpRelcTgInCounter110.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter110.setStatus("current")


class _MccpRelcTgInCounter111_Type(Integer32):
    """Custom type mccpRelcTgInCounter111 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter111_Type.__name__ = "Integer32"
_MccpRelcTgInCounter111_Object = MibTableColumn
mccpRelcTgInCounter111 = _MccpRelcTgInCounter111_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 113),
    _MccpRelcTgInCounter111_Type()
)
mccpRelcTgInCounter111.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter111.setStatus("current")


class _MccpRelcTgInCounter112_Type(Integer32):
    """Custom type mccpRelcTgInCounter112 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter112_Type.__name__ = "Integer32"
_MccpRelcTgInCounter112_Object = MibTableColumn
mccpRelcTgInCounter112 = _MccpRelcTgInCounter112_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 114),
    _MccpRelcTgInCounter112_Type()
)
mccpRelcTgInCounter112.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter112.setStatus("current")


class _MccpRelcTgInCounter113_Type(Integer32):
    """Custom type mccpRelcTgInCounter113 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter113_Type.__name__ = "Integer32"
_MccpRelcTgInCounter113_Object = MibTableColumn
mccpRelcTgInCounter113 = _MccpRelcTgInCounter113_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 115),
    _MccpRelcTgInCounter113_Type()
)
mccpRelcTgInCounter113.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter113.setStatus("current")


class _MccpRelcTgInCounter114_Type(Integer32):
    """Custom type mccpRelcTgInCounter114 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter114_Type.__name__ = "Integer32"
_MccpRelcTgInCounter114_Object = MibTableColumn
mccpRelcTgInCounter114 = _MccpRelcTgInCounter114_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 116),
    _MccpRelcTgInCounter114_Type()
)
mccpRelcTgInCounter114.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter114.setStatus("current")


class _MccpRelcTgInCounter115_Type(Integer32):
    """Custom type mccpRelcTgInCounter115 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter115_Type.__name__ = "Integer32"
_MccpRelcTgInCounter115_Object = MibTableColumn
mccpRelcTgInCounter115 = _MccpRelcTgInCounter115_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 117),
    _MccpRelcTgInCounter115_Type()
)
mccpRelcTgInCounter115.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter115.setStatus("current")


class _MccpRelcTgInCounter116_Type(Integer32):
    """Custom type mccpRelcTgInCounter116 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter116_Type.__name__ = "Integer32"
_MccpRelcTgInCounter116_Object = MibTableColumn
mccpRelcTgInCounter116 = _MccpRelcTgInCounter116_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 118),
    _MccpRelcTgInCounter116_Type()
)
mccpRelcTgInCounter116.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter116.setStatus("current")


class _MccpRelcTgInCounter117_Type(Integer32):
    """Custom type mccpRelcTgInCounter117 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter117_Type.__name__ = "Integer32"
_MccpRelcTgInCounter117_Object = MibTableColumn
mccpRelcTgInCounter117 = _MccpRelcTgInCounter117_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 119),
    _MccpRelcTgInCounter117_Type()
)
mccpRelcTgInCounter117.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter117.setStatus("current")


class _MccpRelcTgInCounter118_Type(Integer32):
    """Custom type mccpRelcTgInCounter118 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter118_Type.__name__ = "Integer32"
_MccpRelcTgInCounter118_Object = MibTableColumn
mccpRelcTgInCounter118 = _MccpRelcTgInCounter118_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 120),
    _MccpRelcTgInCounter118_Type()
)
mccpRelcTgInCounter118.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter118.setStatus("current")


class _MccpRelcTgInCounter119_Type(Integer32):
    """Custom type mccpRelcTgInCounter119 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter119_Type.__name__ = "Integer32"
_MccpRelcTgInCounter119_Object = MibTableColumn
mccpRelcTgInCounter119 = _MccpRelcTgInCounter119_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 121),
    _MccpRelcTgInCounter119_Type()
)
mccpRelcTgInCounter119.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter119.setStatus("current")


class _MccpRelcTgInCounter120_Type(Integer32):
    """Custom type mccpRelcTgInCounter120 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter120_Type.__name__ = "Integer32"
_MccpRelcTgInCounter120_Object = MibTableColumn
mccpRelcTgInCounter120 = _MccpRelcTgInCounter120_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 122),
    _MccpRelcTgInCounter120_Type()
)
mccpRelcTgInCounter120.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter120.setStatus("current")


class _MccpRelcTgInCounter121_Type(Integer32):
    """Custom type mccpRelcTgInCounter121 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter121_Type.__name__ = "Integer32"
_MccpRelcTgInCounter121_Object = MibTableColumn
mccpRelcTgInCounter121 = _MccpRelcTgInCounter121_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 123),
    _MccpRelcTgInCounter121_Type()
)
mccpRelcTgInCounter121.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter121.setStatus("current")


class _MccpRelcTgInCounter122_Type(Integer32):
    """Custom type mccpRelcTgInCounter122 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter122_Type.__name__ = "Integer32"
_MccpRelcTgInCounter122_Object = MibTableColumn
mccpRelcTgInCounter122 = _MccpRelcTgInCounter122_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 124),
    _MccpRelcTgInCounter122_Type()
)
mccpRelcTgInCounter122.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter122.setStatus("current")


class _MccpRelcTgInCounter123_Type(Integer32):
    """Custom type mccpRelcTgInCounter123 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter123_Type.__name__ = "Integer32"
_MccpRelcTgInCounter123_Object = MibTableColumn
mccpRelcTgInCounter123 = _MccpRelcTgInCounter123_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 125),
    _MccpRelcTgInCounter123_Type()
)
mccpRelcTgInCounter123.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter123.setStatus("current")


class _MccpRelcTgInCounter124_Type(Integer32):
    """Custom type mccpRelcTgInCounter124 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter124_Type.__name__ = "Integer32"
_MccpRelcTgInCounter124_Object = MibTableColumn
mccpRelcTgInCounter124 = _MccpRelcTgInCounter124_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 126),
    _MccpRelcTgInCounter124_Type()
)
mccpRelcTgInCounter124.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter124.setStatus("current")


class _MccpRelcTgInCounter125_Type(Integer32):
    """Custom type mccpRelcTgInCounter125 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter125_Type.__name__ = "Integer32"
_MccpRelcTgInCounter125_Object = MibTableColumn
mccpRelcTgInCounter125 = _MccpRelcTgInCounter125_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 127),
    _MccpRelcTgInCounter125_Type()
)
mccpRelcTgInCounter125.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter125.setStatus("current")


class _MccpRelcTgInCounter126_Type(Integer32):
    """Custom type mccpRelcTgInCounter126 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter126_Type.__name__ = "Integer32"
_MccpRelcTgInCounter126_Object = MibTableColumn
mccpRelcTgInCounter126 = _MccpRelcTgInCounter126_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 128),
    _MccpRelcTgInCounter126_Type()
)
mccpRelcTgInCounter126.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter126.setStatus("current")


class _MccpRelcTgInCounter127_Type(Integer32):
    """Custom type mccpRelcTgInCounter127 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgInCounter127_Type.__name__ = "Integer32"
_MccpRelcTgInCounter127_Object = MibTableColumn
mccpRelcTgInCounter127 = _MccpRelcTgInCounter127_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 26, 1, 129),
    _MccpRelcTgInCounter127_Type()
)
mccpRelcTgInCounter127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgInCounter127.setStatus("current")
_MccpRelcTgOutTable_Object = MibTable
mccpRelcTgOutTable = _MccpRelcTgOutTable_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27)
)
if mibBuilder.loadTexts:
    mccpRelcTgOutTable.setStatus("current")
_MccpRelcTgOutEntry_Object = MibTableRow
mccpRelcTgOutEntry = _MccpRelcTgOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1)
)
mccpRelcTgOutEntry.setIndexNames(
    (0, "ELTEX-MCCP", "mccpRelcTgOutIndex"),
)
if mibBuilder.loadTexts:
    mccpRelcTgOutEntry.setStatus("current")


class _MccpRelcTgOutIndex_Type(Integer32):
    """Custom type mccpRelcTgOutIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MccpRelcTgOutIndex_Type.__name__ = "Integer32"
_MccpRelcTgOutIndex_Object = MibTableColumn
mccpRelcTgOutIndex = _MccpRelcTgOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 1),
    _MccpRelcTgOutIndex_Type()
)
mccpRelcTgOutIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mccpRelcTgOutIndex.setStatus("current")


class _MccpRelcTgOutCounter0_Type(Integer32):
    """Custom type mccpRelcTgOutCounter0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter0_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter0_Object = MibTableColumn
mccpRelcTgOutCounter0 = _MccpRelcTgOutCounter0_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 2),
    _MccpRelcTgOutCounter0_Type()
)
mccpRelcTgOutCounter0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter0.setStatus("current")


class _MccpRelcTgOutCounter1_Type(Integer32):
    """Custom type mccpRelcTgOutCounter1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter1_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter1_Object = MibTableColumn
mccpRelcTgOutCounter1 = _MccpRelcTgOutCounter1_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 3),
    _MccpRelcTgOutCounter1_Type()
)
mccpRelcTgOutCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter1.setStatus("current")


class _MccpRelcTgOutCounter2_Type(Integer32):
    """Custom type mccpRelcTgOutCounter2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter2_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter2_Object = MibTableColumn
mccpRelcTgOutCounter2 = _MccpRelcTgOutCounter2_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 4),
    _MccpRelcTgOutCounter2_Type()
)
mccpRelcTgOutCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter2.setStatus("current")


class _MccpRelcTgOutCounter3_Type(Integer32):
    """Custom type mccpRelcTgOutCounter3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter3_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter3_Object = MibTableColumn
mccpRelcTgOutCounter3 = _MccpRelcTgOutCounter3_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 5),
    _MccpRelcTgOutCounter3_Type()
)
mccpRelcTgOutCounter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter3.setStatus("current")


class _MccpRelcTgOutCounter4_Type(Integer32):
    """Custom type mccpRelcTgOutCounter4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter4_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter4_Object = MibTableColumn
mccpRelcTgOutCounter4 = _MccpRelcTgOutCounter4_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 6),
    _MccpRelcTgOutCounter4_Type()
)
mccpRelcTgOutCounter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter4.setStatus("current")


class _MccpRelcTgOutCounter5_Type(Integer32):
    """Custom type mccpRelcTgOutCounter5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter5_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter5_Object = MibTableColumn
mccpRelcTgOutCounter5 = _MccpRelcTgOutCounter5_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 7),
    _MccpRelcTgOutCounter5_Type()
)
mccpRelcTgOutCounter5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter5.setStatus("current")


class _MccpRelcTgOutCounter6_Type(Integer32):
    """Custom type mccpRelcTgOutCounter6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter6_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter6_Object = MibTableColumn
mccpRelcTgOutCounter6 = _MccpRelcTgOutCounter6_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 8),
    _MccpRelcTgOutCounter6_Type()
)
mccpRelcTgOutCounter6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter6.setStatus("current")


class _MccpRelcTgOutCounter7_Type(Integer32):
    """Custom type mccpRelcTgOutCounter7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter7_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter7_Object = MibTableColumn
mccpRelcTgOutCounter7 = _MccpRelcTgOutCounter7_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 9),
    _MccpRelcTgOutCounter7_Type()
)
mccpRelcTgOutCounter7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter7.setStatus("current")


class _MccpRelcTgOutCounter8_Type(Integer32):
    """Custom type mccpRelcTgOutCounter8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter8_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter8_Object = MibTableColumn
mccpRelcTgOutCounter8 = _MccpRelcTgOutCounter8_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 10),
    _MccpRelcTgOutCounter8_Type()
)
mccpRelcTgOutCounter8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter8.setStatus("current")


class _MccpRelcTgOutCounter9_Type(Integer32):
    """Custom type mccpRelcTgOutCounter9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter9_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter9_Object = MibTableColumn
mccpRelcTgOutCounter9 = _MccpRelcTgOutCounter9_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 11),
    _MccpRelcTgOutCounter9_Type()
)
mccpRelcTgOutCounter9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter9.setStatus("current")


class _MccpRelcTgOutCounter10_Type(Integer32):
    """Custom type mccpRelcTgOutCounter10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter10_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter10_Object = MibTableColumn
mccpRelcTgOutCounter10 = _MccpRelcTgOutCounter10_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 12),
    _MccpRelcTgOutCounter10_Type()
)
mccpRelcTgOutCounter10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter10.setStatus("current")


class _MccpRelcTgOutCounter11_Type(Integer32):
    """Custom type mccpRelcTgOutCounter11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter11_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter11_Object = MibTableColumn
mccpRelcTgOutCounter11 = _MccpRelcTgOutCounter11_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 13),
    _MccpRelcTgOutCounter11_Type()
)
mccpRelcTgOutCounter11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter11.setStatus("current")


class _MccpRelcTgOutCounter12_Type(Integer32):
    """Custom type mccpRelcTgOutCounter12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter12_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter12_Object = MibTableColumn
mccpRelcTgOutCounter12 = _MccpRelcTgOutCounter12_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 14),
    _MccpRelcTgOutCounter12_Type()
)
mccpRelcTgOutCounter12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter12.setStatus("current")


class _MccpRelcTgOutCounter13_Type(Integer32):
    """Custom type mccpRelcTgOutCounter13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter13_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter13_Object = MibTableColumn
mccpRelcTgOutCounter13 = _MccpRelcTgOutCounter13_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 15),
    _MccpRelcTgOutCounter13_Type()
)
mccpRelcTgOutCounter13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter13.setStatus("current")


class _MccpRelcTgOutCounter14_Type(Integer32):
    """Custom type mccpRelcTgOutCounter14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter14_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter14_Object = MibTableColumn
mccpRelcTgOutCounter14 = _MccpRelcTgOutCounter14_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 16),
    _MccpRelcTgOutCounter14_Type()
)
mccpRelcTgOutCounter14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter14.setStatus("current")


class _MccpRelcTgOutCounter15_Type(Integer32):
    """Custom type mccpRelcTgOutCounter15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter15_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter15_Object = MibTableColumn
mccpRelcTgOutCounter15 = _MccpRelcTgOutCounter15_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 17),
    _MccpRelcTgOutCounter15_Type()
)
mccpRelcTgOutCounter15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter15.setStatus("current")


class _MccpRelcTgOutCounter16_Type(Integer32):
    """Custom type mccpRelcTgOutCounter16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter16_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter16_Object = MibTableColumn
mccpRelcTgOutCounter16 = _MccpRelcTgOutCounter16_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 18),
    _MccpRelcTgOutCounter16_Type()
)
mccpRelcTgOutCounter16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter16.setStatus("current")


class _MccpRelcTgOutCounter17_Type(Integer32):
    """Custom type mccpRelcTgOutCounter17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter17_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter17_Object = MibTableColumn
mccpRelcTgOutCounter17 = _MccpRelcTgOutCounter17_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 19),
    _MccpRelcTgOutCounter17_Type()
)
mccpRelcTgOutCounter17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter17.setStatus("current")


class _MccpRelcTgOutCounter18_Type(Integer32):
    """Custom type mccpRelcTgOutCounter18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter18_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter18_Object = MibTableColumn
mccpRelcTgOutCounter18 = _MccpRelcTgOutCounter18_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 20),
    _MccpRelcTgOutCounter18_Type()
)
mccpRelcTgOutCounter18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter18.setStatus("current")


class _MccpRelcTgOutCounter19_Type(Integer32):
    """Custom type mccpRelcTgOutCounter19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter19_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter19_Object = MibTableColumn
mccpRelcTgOutCounter19 = _MccpRelcTgOutCounter19_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 21),
    _MccpRelcTgOutCounter19_Type()
)
mccpRelcTgOutCounter19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter19.setStatus("current")


class _MccpRelcTgOutCounter20_Type(Integer32):
    """Custom type mccpRelcTgOutCounter20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter20_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter20_Object = MibTableColumn
mccpRelcTgOutCounter20 = _MccpRelcTgOutCounter20_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 22),
    _MccpRelcTgOutCounter20_Type()
)
mccpRelcTgOutCounter20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter20.setStatus("current")


class _MccpRelcTgOutCounter21_Type(Integer32):
    """Custom type mccpRelcTgOutCounter21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter21_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter21_Object = MibTableColumn
mccpRelcTgOutCounter21 = _MccpRelcTgOutCounter21_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 23),
    _MccpRelcTgOutCounter21_Type()
)
mccpRelcTgOutCounter21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter21.setStatus("current")


class _MccpRelcTgOutCounter22_Type(Integer32):
    """Custom type mccpRelcTgOutCounter22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter22_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter22_Object = MibTableColumn
mccpRelcTgOutCounter22 = _MccpRelcTgOutCounter22_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 24),
    _MccpRelcTgOutCounter22_Type()
)
mccpRelcTgOutCounter22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter22.setStatus("current")


class _MccpRelcTgOutCounter23_Type(Integer32):
    """Custom type mccpRelcTgOutCounter23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter23_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter23_Object = MibTableColumn
mccpRelcTgOutCounter23 = _MccpRelcTgOutCounter23_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 25),
    _MccpRelcTgOutCounter23_Type()
)
mccpRelcTgOutCounter23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter23.setStatus("current")


class _MccpRelcTgOutCounter24_Type(Integer32):
    """Custom type mccpRelcTgOutCounter24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter24_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter24_Object = MibTableColumn
mccpRelcTgOutCounter24 = _MccpRelcTgOutCounter24_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 26),
    _MccpRelcTgOutCounter24_Type()
)
mccpRelcTgOutCounter24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter24.setStatus("current")


class _MccpRelcTgOutCounter25_Type(Integer32):
    """Custom type mccpRelcTgOutCounter25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter25_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter25_Object = MibTableColumn
mccpRelcTgOutCounter25 = _MccpRelcTgOutCounter25_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 27),
    _MccpRelcTgOutCounter25_Type()
)
mccpRelcTgOutCounter25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter25.setStatus("current")


class _MccpRelcTgOutCounter26_Type(Integer32):
    """Custom type mccpRelcTgOutCounter26 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter26_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter26_Object = MibTableColumn
mccpRelcTgOutCounter26 = _MccpRelcTgOutCounter26_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 28),
    _MccpRelcTgOutCounter26_Type()
)
mccpRelcTgOutCounter26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter26.setStatus("current")


class _MccpRelcTgOutCounter27_Type(Integer32):
    """Custom type mccpRelcTgOutCounter27 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter27_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter27_Object = MibTableColumn
mccpRelcTgOutCounter27 = _MccpRelcTgOutCounter27_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 29),
    _MccpRelcTgOutCounter27_Type()
)
mccpRelcTgOutCounter27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter27.setStatus("current")


class _MccpRelcTgOutCounter28_Type(Integer32):
    """Custom type mccpRelcTgOutCounter28 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter28_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter28_Object = MibTableColumn
mccpRelcTgOutCounter28 = _MccpRelcTgOutCounter28_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 30),
    _MccpRelcTgOutCounter28_Type()
)
mccpRelcTgOutCounter28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter28.setStatus("current")


class _MccpRelcTgOutCounter29_Type(Integer32):
    """Custom type mccpRelcTgOutCounter29 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter29_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter29_Object = MibTableColumn
mccpRelcTgOutCounter29 = _MccpRelcTgOutCounter29_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 31),
    _MccpRelcTgOutCounter29_Type()
)
mccpRelcTgOutCounter29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter29.setStatus("current")


class _MccpRelcTgOutCounter30_Type(Integer32):
    """Custom type mccpRelcTgOutCounter30 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter30_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter30_Object = MibTableColumn
mccpRelcTgOutCounter30 = _MccpRelcTgOutCounter30_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 32),
    _MccpRelcTgOutCounter30_Type()
)
mccpRelcTgOutCounter30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter30.setStatus("current")


class _MccpRelcTgOutCounter31_Type(Integer32):
    """Custom type mccpRelcTgOutCounter31 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter31_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter31_Object = MibTableColumn
mccpRelcTgOutCounter31 = _MccpRelcTgOutCounter31_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 33),
    _MccpRelcTgOutCounter31_Type()
)
mccpRelcTgOutCounter31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter31.setStatus("current")


class _MccpRelcTgOutCounter32_Type(Integer32):
    """Custom type mccpRelcTgOutCounter32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter32_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter32_Object = MibTableColumn
mccpRelcTgOutCounter32 = _MccpRelcTgOutCounter32_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 34),
    _MccpRelcTgOutCounter32_Type()
)
mccpRelcTgOutCounter32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter32.setStatus("current")


class _MccpRelcTgOutCounter33_Type(Integer32):
    """Custom type mccpRelcTgOutCounter33 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter33_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter33_Object = MibTableColumn
mccpRelcTgOutCounter33 = _MccpRelcTgOutCounter33_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 35),
    _MccpRelcTgOutCounter33_Type()
)
mccpRelcTgOutCounter33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter33.setStatus("current")


class _MccpRelcTgOutCounter34_Type(Integer32):
    """Custom type mccpRelcTgOutCounter34 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter34_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter34_Object = MibTableColumn
mccpRelcTgOutCounter34 = _MccpRelcTgOutCounter34_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 36),
    _MccpRelcTgOutCounter34_Type()
)
mccpRelcTgOutCounter34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter34.setStatus("current")


class _MccpRelcTgOutCounter35_Type(Integer32):
    """Custom type mccpRelcTgOutCounter35 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter35_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter35_Object = MibTableColumn
mccpRelcTgOutCounter35 = _MccpRelcTgOutCounter35_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 37),
    _MccpRelcTgOutCounter35_Type()
)
mccpRelcTgOutCounter35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter35.setStatus("current")


class _MccpRelcTgOutCounter36_Type(Integer32):
    """Custom type mccpRelcTgOutCounter36 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter36_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter36_Object = MibTableColumn
mccpRelcTgOutCounter36 = _MccpRelcTgOutCounter36_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 38),
    _MccpRelcTgOutCounter36_Type()
)
mccpRelcTgOutCounter36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter36.setStatus("current")


class _MccpRelcTgOutCounter37_Type(Integer32):
    """Custom type mccpRelcTgOutCounter37 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter37_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter37_Object = MibTableColumn
mccpRelcTgOutCounter37 = _MccpRelcTgOutCounter37_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 39),
    _MccpRelcTgOutCounter37_Type()
)
mccpRelcTgOutCounter37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter37.setStatus("current")


class _MccpRelcTgOutCounter38_Type(Integer32):
    """Custom type mccpRelcTgOutCounter38 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter38_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter38_Object = MibTableColumn
mccpRelcTgOutCounter38 = _MccpRelcTgOutCounter38_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 40),
    _MccpRelcTgOutCounter38_Type()
)
mccpRelcTgOutCounter38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter38.setStatus("current")


class _MccpRelcTgOutCounter39_Type(Integer32):
    """Custom type mccpRelcTgOutCounter39 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter39_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter39_Object = MibTableColumn
mccpRelcTgOutCounter39 = _MccpRelcTgOutCounter39_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 41),
    _MccpRelcTgOutCounter39_Type()
)
mccpRelcTgOutCounter39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter39.setStatus("current")


class _MccpRelcTgOutCounter40_Type(Integer32):
    """Custom type mccpRelcTgOutCounter40 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter40_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter40_Object = MibTableColumn
mccpRelcTgOutCounter40 = _MccpRelcTgOutCounter40_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 42),
    _MccpRelcTgOutCounter40_Type()
)
mccpRelcTgOutCounter40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter40.setStatus("current")


class _MccpRelcTgOutCounter41_Type(Integer32):
    """Custom type mccpRelcTgOutCounter41 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter41_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter41_Object = MibTableColumn
mccpRelcTgOutCounter41 = _MccpRelcTgOutCounter41_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 43),
    _MccpRelcTgOutCounter41_Type()
)
mccpRelcTgOutCounter41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter41.setStatus("current")


class _MccpRelcTgOutCounter42_Type(Integer32):
    """Custom type mccpRelcTgOutCounter42 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter42_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter42_Object = MibTableColumn
mccpRelcTgOutCounter42 = _MccpRelcTgOutCounter42_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 44),
    _MccpRelcTgOutCounter42_Type()
)
mccpRelcTgOutCounter42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter42.setStatus("current")


class _MccpRelcTgOutCounter43_Type(Integer32):
    """Custom type mccpRelcTgOutCounter43 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter43_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter43_Object = MibTableColumn
mccpRelcTgOutCounter43 = _MccpRelcTgOutCounter43_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 45),
    _MccpRelcTgOutCounter43_Type()
)
mccpRelcTgOutCounter43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter43.setStatus("current")


class _MccpRelcTgOutCounter44_Type(Integer32):
    """Custom type mccpRelcTgOutCounter44 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter44_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter44_Object = MibTableColumn
mccpRelcTgOutCounter44 = _MccpRelcTgOutCounter44_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 46),
    _MccpRelcTgOutCounter44_Type()
)
mccpRelcTgOutCounter44.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter44.setStatus("current")


class _MccpRelcTgOutCounter45_Type(Integer32):
    """Custom type mccpRelcTgOutCounter45 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter45_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter45_Object = MibTableColumn
mccpRelcTgOutCounter45 = _MccpRelcTgOutCounter45_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 47),
    _MccpRelcTgOutCounter45_Type()
)
mccpRelcTgOutCounter45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter45.setStatus("current")


class _MccpRelcTgOutCounter46_Type(Integer32):
    """Custom type mccpRelcTgOutCounter46 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter46_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter46_Object = MibTableColumn
mccpRelcTgOutCounter46 = _MccpRelcTgOutCounter46_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 48),
    _MccpRelcTgOutCounter46_Type()
)
mccpRelcTgOutCounter46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter46.setStatus("current")


class _MccpRelcTgOutCounter47_Type(Integer32):
    """Custom type mccpRelcTgOutCounter47 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter47_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter47_Object = MibTableColumn
mccpRelcTgOutCounter47 = _MccpRelcTgOutCounter47_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 49),
    _MccpRelcTgOutCounter47_Type()
)
mccpRelcTgOutCounter47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter47.setStatus("current")


class _MccpRelcTgOutCounter48_Type(Integer32):
    """Custom type mccpRelcTgOutCounter48 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter48_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter48_Object = MibTableColumn
mccpRelcTgOutCounter48 = _MccpRelcTgOutCounter48_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 50),
    _MccpRelcTgOutCounter48_Type()
)
mccpRelcTgOutCounter48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter48.setStatus("current")


class _MccpRelcTgOutCounter49_Type(Integer32):
    """Custom type mccpRelcTgOutCounter49 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter49_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter49_Object = MibTableColumn
mccpRelcTgOutCounter49 = _MccpRelcTgOutCounter49_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 51),
    _MccpRelcTgOutCounter49_Type()
)
mccpRelcTgOutCounter49.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter49.setStatus("current")


class _MccpRelcTgOutCounter50_Type(Integer32):
    """Custom type mccpRelcTgOutCounter50 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter50_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter50_Object = MibTableColumn
mccpRelcTgOutCounter50 = _MccpRelcTgOutCounter50_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 52),
    _MccpRelcTgOutCounter50_Type()
)
mccpRelcTgOutCounter50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter50.setStatus("current")


class _MccpRelcTgOutCounter51_Type(Integer32):
    """Custom type mccpRelcTgOutCounter51 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter51_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter51_Object = MibTableColumn
mccpRelcTgOutCounter51 = _MccpRelcTgOutCounter51_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 53),
    _MccpRelcTgOutCounter51_Type()
)
mccpRelcTgOutCounter51.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter51.setStatus("current")


class _MccpRelcTgOutCounter52_Type(Integer32):
    """Custom type mccpRelcTgOutCounter52 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter52_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter52_Object = MibTableColumn
mccpRelcTgOutCounter52 = _MccpRelcTgOutCounter52_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 54),
    _MccpRelcTgOutCounter52_Type()
)
mccpRelcTgOutCounter52.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter52.setStatus("current")


class _MccpRelcTgOutCounter53_Type(Integer32):
    """Custom type mccpRelcTgOutCounter53 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter53_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter53_Object = MibTableColumn
mccpRelcTgOutCounter53 = _MccpRelcTgOutCounter53_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 55),
    _MccpRelcTgOutCounter53_Type()
)
mccpRelcTgOutCounter53.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter53.setStatus("current")


class _MccpRelcTgOutCounter54_Type(Integer32):
    """Custom type mccpRelcTgOutCounter54 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter54_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter54_Object = MibTableColumn
mccpRelcTgOutCounter54 = _MccpRelcTgOutCounter54_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 56),
    _MccpRelcTgOutCounter54_Type()
)
mccpRelcTgOutCounter54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter54.setStatus("current")


class _MccpRelcTgOutCounter55_Type(Integer32):
    """Custom type mccpRelcTgOutCounter55 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter55_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter55_Object = MibTableColumn
mccpRelcTgOutCounter55 = _MccpRelcTgOutCounter55_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 57),
    _MccpRelcTgOutCounter55_Type()
)
mccpRelcTgOutCounter55.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter55.setStatus("current")


class _MccpRelcTgOutCounter56_Type(Integer32):
    """Custom type mccpRelcTgOutCounter56 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter56_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter56_Object = MibTableColumn
mccpRelcTgOutCounter56 = _MccpRelcTgOutCounter56_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 58),
    _MccpRelcTgOutCounter56_Type()
)
mccpRelcTgOutCounter56.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter56.setStatus("current")


class _MccpRelcTgOutCounter57_Type(Integer32):
    """Custom type mccpRelcTgOutCounter57 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter57_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter57_Object = MibTableColumn
mccpRelcTgOutCounter57 = _MccpRelcTgOutCounter57_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 59),
    _MccpRelcTgOutCounter57_Type()
)
mccpRelcTgOutCounter57.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter57.setStatus("current")


class _MccpRelcTgOutCounter58_Type(Integer32):
    """Custom type mccpRelcTgOutCounter58 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter58_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter58_Object = MibTableColumn
mccpRelcTgOutCounter58 = _MccpRelcTgOutCounter58_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 60),
    _MccpRelcTgOutCounter58_Type()
)
mccpRelcTgOutCounter58.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter58.setStatus("current")


class _MccpRelcTgOutCounter59_Type(Integer32):
    """Custom type mccpRelcTgOutCounter59 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter59_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter59_Object = MibTableColumn
mccpRelcTgOutCounter59 = _MccpRelcTgOutCounter59_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 61),
    _MccpRelcTgOutCounter59_Type()
)
mccpRelcTgOutCounter59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter59.setStatus("current")


class _MccpRelcTgOutCounter60_Type(Integer32):
    """Custom type mccpRelcTgOutCounter60 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter60_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter60_Object = MibTableColumn
mccpRelcTgOutCounter60 = _MccpRelcTgOutCounter60_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 62),
    _MccpRelcTgOutCounter60_Type()
)
mccpRelcTgOutCounter60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter60.setStatus("current")


class _MccpRelcTgOutCounter61_Type(Integer32):
    """Custom type mccpRelcTgOutCounter61 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter61_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter61_Object = MibTableColumn
mccpRelcTgOutCounter61 = _MccpRelcTgOutCounter61_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 63),
    _MccpRelcTgOutCounter61_Type()
)
mccpRelcTgOutCounter61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter61.setStatus("current")


class _MccpRelcTgOutCounter62_Type(Integer32):
    """Custom type mccpRelcTgOutCounter62 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter62_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter62_Object = MibTableColumn
mccpRelcTgOutCounter62 = _MccpRelcTgOutCounter62_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 64),
    _MccpRelcTgOutCounter62_Type()
)
mccpRelcTgOutCounter62.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter62.setStatus("current")


class _MccpRelcTgOutCounter63_Type(Integer32):
    """Custom type mccpRelcTgOutCounter63 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter63_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter63_Object = MibTableColumn
mccpRelcTgOutCounter63 = _MccpRelcTgOutCounter63_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 65),
    _MccpRelcTgOutCounter63_Type()
)
mccpRelcTgOutCounter63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter63.setStatus("current")


class _MccpRelcTgOutCounter64_Type(Integer32):
    """Custom type mccpRelcTgOutCounter64 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter64_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter64_Object = MibTableColumn
mccpRelcTgOutCounter64 = _MccpRelcTgOutCounter64_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 66),
    _MccpRelcTgOutCounter64_Type()
)
mccpRelcTgOutCounter64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter64.setStatus("current")


class _MccpRelcTgOutCounter65_Type(Integer32):
    """Custom type mccpRelcTgOutCounter65 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter65_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter65_Object = MibTableColumn
mccpRelcTgOutCounter65 = _MccpRelcTgOutCounter65_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 67),
    _MccpRelcTgOutCounter65_Type()
)
mccpRelcTgOutCounter65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter65.setStatus("current")


class _MccpRelcTgOutCounter66_Type(Integer32):
    """Custom type mccpRelcTgOutCounter66 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter66_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter66_Object = MibTableColumn
mccpRelcTgOutCounter66 = _MccpRelcTgOutCounter66_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 68),
    _MccpRelcTgOutCounter66_Type()
)
mccpRelcTgOutCounter66.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter66.setStatus("current")


class _MccpRelcTgOutCounter67_Type(Integer32):
    """Custom type mccpRelcTgOutCounter67 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter67_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter67_Object = MibTableColumn
mccpRelcTgOutCounter67 = _MccpRelcTgOutCounter67_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 69),
    _MccpRelcTgOutCounter67_Type()
)
mccpRelcTgOutCounter67.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter67.setStatus("current")


class _MccpRelcTgOutCounter68_Type(Integer32):
    """Custom type mccpRelcTgOutCounter68 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter68_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter68_Object = MibTableColumn
mccpRelcTgOutCounter68 = _MccpRelcTgOutCounter68_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 70),
    _MccpRelcTgOutCounter68_Type()
)
mccpRelcTgOutCounter68.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter68.setStatus("current")


class _MccpRelcTgOutCounter69_Type(Integer32):
    """Custom type mccpRelcTgOutCounter69 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter69_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter69_Object = MibTableColumn
mccpRelcTgOutCounter69 = _MccpRelcTgOutCounter69_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 71),
    _MccpRelcTgOutCounter69_Type()
)
mccpRelcTgOutCounter69.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter69.setStatus("current")


class _MccpRelcTgOutCounter70_Type(Integer32):
    """Custom type mccpRelcTgOutCounter70 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter70_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter70_Object = MibTableColumn
mccpRelcTgOutCounter70 = _MccpRelcTgOutCounter70_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 72),
    _MccpRelcTgOutCounter70_Type()
)
mccpRelcTgOutCounter70.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter70.setStatus("current")


class _MccpRelcTgOutCounter71_Type(Integer32):
    """Custom type mccpRelcTgOutCounter71 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter71_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter71_Object = MibTableColumn
mccpRelcTgOutCounter71 = _MccpRelcTgOutCounter71_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 73),
    _MccpRelcTgOutCounter71_Type()
)
mccpRelcTgOutCounter71.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter71.setStatus("current")


class _MccpRelcTgOutCounter72_Type(Integer32):
    """Custom type mccpRelcTgOutCounter72 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter72_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter72_Object = MibTableColumn
mccpRelcTgOutCounter72 = _MccpRelcTgOutCounter72_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 74),
    _MccpRelcTgOutCounter72_Type()
)
mccpRelcTgOutCounter72.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter72.setStatus("current")


class _MccpRelcTgOutCounter73_Type(Integer32):
    """Custom type mccpRelcTgOutCounter73 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter73_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter73_Object = MibTableColumn
mccpRelcTgOutCounter73 = _MccpRelcTgOutCounter73_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 75),
    _MccpRelcTgOutCounter73_Type()
)
mccpRelcTgOutCounter73.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter73.setStatus("current")


class _MccpRelcTgOutCounter74_Type(Integer32):
    """Custom type mccpRelcTgOutCounter74 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter74_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter74_Object = MibTableColumn
mccpRelcTgOutCounter74 = _MccpRelcTgOutCounter74_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 76),
    _MccpRelcTgOutCounter74_Type()
)
mccpRelcTgOutCounter74.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter74.setStatus("current")


class _MccpRelcTgOutCounter75_Type(Integer32):
    """Custom type mccpRelcTgOutCounter75 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter75_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter75_Object = MibTableColumn
mccpRelcTgOutCounter75 = _MccpRelcTgOutCounter75_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 77),
    _MccpRelcTgOutCounter75_Type()
)
mccpRelcTgOutCounter75.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter75.setStatus("current")


class _MccpRelcTgOutCounter76_Type(Integer32):
    """Custom type mccpRelcTgOutCounter76 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter76_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter76_Object = MibTableColumn
mccpRelcTgOutCounter76 = _MccpRelcTgOutCounter76_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 78),
    _MccpRelcTgOutCounter76_Type()
)
mccpRelcTgOutCounter76.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter76.setStatus("current")


class _MccpRelcTgOutCounter77_Type(Integer32):
    """Custom type mccpRelcTgOutCounter77 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter77_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter77_Object = MibTableColumn
mccpRelcTgOutCounter77 = _MccpRelcTgOutCounter77_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 79),
    _MccpRelcTgOutCounter77_Type()
)
mccpRelcTgOutCounter77.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter77.setStatus("current")


class _MccpRelcTgOutCounter78_Type(Integer32):
    """Custom type mccpRelcTgOutCounter78 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter78_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter78_Object = MibTableColumn
mccpRelcTgOutCounter78 = _MccpRelcTgOutCounter78_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 80),
    _MccpRelcTgOutCounter78_Type()
)
mccpRelcTgOutCounter78.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter78.setStatus("current")


class _MccpRelcTgOutCounter79_Type(Integer32):
    """Custom type mccpRelcTgOutCounter79 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter79_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter79_Object = MibTableColumn
mccpRelcTgOutCounter79 = _MccpRelcTgOutCounter79_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 81),
    _MccpRelcTgOutCounter79_Type()
)
mccpRelcTgOutCounter79.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter79.setStatus("current")


class _MccpRelcTgOutCounter80_Type(Integer32):
    """Custom type mccpRelcTgOutCounter80 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter80_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter80_Object = MibTableColumn
mccpRelcTgOutCounter80 = _MccpRelcTgOutCounter80_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 82),
    _MccpRelcTgOutCounter80_Type()
)
mccpRelcTgOutCounter80.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter80.setStatus("current")


class _MccpRelcTgOutCounter81_Type(Integer32):
    """Custom type mccpRelcTgOutCounter81 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter81_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter81_Object = MibTableColumn
mccpRelcTgOutCounter81 = _MccpRelcTgOutCounter81_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 83),
    _MccpRelcTgOutCounter81_Type()
)
mccpRelcTgOutCounter81.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter81.setStatus("current")


class _MccpRelcTgOutCounter82_Type(Integer32):
    """Custom type mccpRelcTgOutCounter82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter82_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter82_Object = MibTableColumn
mccpRelcTgOutCounter82 = _MccpRelcTgOutCounter82_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 84),
    _MccpRelcTgOutCounter82_Type()
)
mccpRelcTgOutCounter82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter82.setStatus("current")


class _MccpRelcTgOutCounter83_Type(Integer32):
    """Custom type mccpRelcTgOutCounter83 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter83_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter83_Object = MibTableColumn
mccpRelcTgOutCounter83 = _MccpRelcTgOutCounter83_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 85),
    _MccpRelcTgOutCounter83_Type()
)
mccpRelcTgOutCounter83.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter83.setStatus("current")


class _MccpRelcTgOutCounter84_Type(Integer32):
    """Custom type mccpRelcTgOutCounter84 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter84_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter84_Object = MibTableColumn
mccpRelcTgOutCounter84 = _MccpRelcTgOutCounter84_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 86),
    _MccpRelcTgOutCounter84_Type()
)
mccpRelcTgOutCounter84.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter84.setStatus("current")


class _MccpRelcTgOutCounter85_Type(Integer32):
    """Custom type mccpRelcTgOutCounter85 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter85_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter85_Object = MibTableColumn
mccpRelcTgOutCounter85 = _MccpRelcTgOutCounter85_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 87),
    _MccpRelcTgOutCounter85_Type()
)
mccpRelcTgOutCounter85.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter85.setStatus("current")


class _MccpRelcTgOutCounter86_Type(Integer32):
    """Custom type mccpRelcTgOutCounter86 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter86_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter86_Object = MibTableColumn
mccpRelcTgOutCounter86 = _MccpRelcTgOutCounter86_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 88),
    _MccpRelcTgOutCounter86_Type()
)
mccpRelcTgOutCounter86.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter86.setStatus("current")


class _MccpRelcTgOutCounter87_Type(Integer32):
    """Custom type mccpRelcTgOutCounter87 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter87_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter87_Object = MibTableColumn
mccpRelcTgOutCounter87 = _MccpRelcTgOutCounter87_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 89),
    _MccpRelcTgOutCounter87_Type()
)
mccpRelcTgOutCounter87.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter87.setStatus("current")


class _MccpRelcTgOutCounter88_Type(Integer32):
    """Custom type mccpRelcTgOutCounter88 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter88_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter88_Object = MibTableColumn
mccpRelcTgOutCounter88 = _MccpRelcTgOutCounter88_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 90),
    _MccpRelcTgOutCounter88_Type()
)
mccpRelcTgOutCounter88.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter88.setStatus("current")


class _MccpRelcTgOutCounter89_Type(Integer32):
    """Custom type mccpRelcTgOutCounter89 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter89_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter89_Object = MibTableColumn
mccpRelcTgOutCounter89 = _MccpRelcTgOutCounter89_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 91),
    _MccpRelcTgOutCounter89_Type()
)
mccpRelcTgOutCounter89.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter89.setStatus("current")


class _MccpRelcTgOutCounter90_Type(Integer32):
    """Custom type mccpRelcTgOutCounter90 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter90_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter90_Object = MibTableColumn
mccpRelcTgOutCounter90 = _MccpRelcTgOutCounter90_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 92),
    _MccpRelcTgOutCounter90_Type()
)
mccpRelcTgOutCounter90.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter90.setStatus("current")


class _MccpRelcTgOutCounter91_Type(Integer32):
    """Custom type mccpRelcTgOutCounter91 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter91_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter91_Object = MibTableColumn
mccpRelcTgOutCounter91 = _MccpRelcTgOutCounter91_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 93),
    _MccpRelcTgOutCounter91_Type()
)
mccpRelcTgOutCounter91.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter91.setStatus("current")


class _MccpRelcTgOutCounter92_Type(Integer32):
    """Custom type mccpRelcTgOutCounter92 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter92_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter92_Object = MibTableColumn
mccpRelcTgOutCounter92 = _MccpRelcTgOutCounter92_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 94),
    _MccpRelcTgOutCounter92_Type()
)
mccpRelcTgOutCounter92.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter92.setStatus("current")


class _MccpRelcTgOutCounter93_Type(Integer32):
    """Custom type mccpRelcTgOutCounter93 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter93_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter93_Object = MibTableColumn
mccpRelcTgOutCounter93 = _MccpRelcTgOutCounter93_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 95),
    _MccpRelcTgOutCounter93_Type()
)
mccpRelcTgOutCounter93.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter93.setStatus("current")


class _MccpRelcTgOutCounter94_Type(Integer32):
    """Custom type mccpRelcTgOutCounter94 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter94_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter94_Object = MibTableColumn
mccpRelcTgOutCounter94 = _MccpRelcTgOutCounter94_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 96),
    _MccpRelcTgOutCounter94_Type()
)
mccpRelcTgOutCounter94.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter94.setStatus("current")


class _MccpRelcTgOutCounter95_Type(Integer32):
    """Custom type mccpRelcTgOutCounter95 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter95_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter95_Object = MibTableColumn
mccpRelcTgOutCounter95 = _MccpRelcTgOutCounter95_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 97),
    _MccpRelcTgOutCounter95_Type()
)
mccpRelcTgOutCounter95.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter95.setStatus("current")


class _MccpRelcTgOutCounter96_Type(Integer32):
    """Custom type mccpRelcTgOutCounter96 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter96_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter96_Object = MibTableColumn
mccpRelcTgOutCounter96 = _MccpRelcTgOutCounter96_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 98),
    _MccpRelcTgOutCounter96_Type()
)
mccpRelcTgOutCounter96.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter96.setStatus("current")


class _MccpRelcTgOutCounter97_Type(Integer32):
    """Custom type mccpRelcTgOutCounter97 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter97_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter97_Object = MibTableColumn
mccpRelcTgOutCounter97 = _MccpRelcTgOutCounter97_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 99),
    _MccpRelcTgOutCounter97_Type()
)
mccpRelcTgOutCounter97.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter97.setStatus("current")


class _MccpRelcTgOutCounter98_Type(Integer32):
    """Custom type mccpRelcTgOutCounter98 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter98_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter98_Object = MibTableColumn
mccpRelcTgOutCounter98 = _MccpRelcTgOutCounter98_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 100),
    _MccpRelcTgOutCounter98_Type()
)
mccpRelcTgOutCounter98.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter98.setStatus("current")


class _MccpRelcTgOutCounter99_Type(Integer32):
    """Custom type mccpRelcTgOutCounter99 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter99_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter99_Object = MibTableColumn
mccpRelcTgOutCounter99 = _MccpRelcTgOutCounter99_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 101),
    _MccpRelcTgOutCounter99_Type()
)
mccpRelcTgOutCounter99.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter99.setStatus("current")


class _MccpRelcTgOutCounter100_Type(Integer32):
    """Custom type mccpRelcTgOutCounter100 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter100_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter100_Object = MibTableColumn
mccpRelcTgOutCounter100 = _MccpRelcTgOutCounter100_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 102),
    _MccpRelcTgOutCounter100_Type()
)
mccpRelcTgOutCounter100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter100.setStatus("current")


class _MccpRelcTgOutCounter101_Type(Integer32):
    """Custom type mccpRelcTgOutCounter101 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter101_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter101_Object = MibTableColumn
mccpRelcTgOutCounter101 = _MccpRelcTgOutCounter101_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 103),
    _MccpRelcTgOutCounter101_Type()
)
mccpRelcTgOutCounter101.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter101.setStatus("current")


class _MccpRelcTgOutCounter102_Type(Integer32):
    """Custom type mccpRelcTgOutCounter102 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter102_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter102_Object = MibTableColumn
mccpRelcTgOutCounter102 = _MccpRelcTgOutCounter102_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 104),
    _MccpRelcTgOutCounter102_Type()
)
mccpRelcTgOutCounter102.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter102.setStatus("current")


class _MccpRelcTgOutCounter103_Type(Integer32):
    """Custom type mccpRelcTgOutCounter103 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter103_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter103_Object = MibTableColumn
mccpRelcTgOutCounter103 = _MccpRelcTgOutCounter103_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 105),
    _MccpRelcTgOutCounter103_Type()
)
mccpRelcTgOutCounter103.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter103.setStatus("current")


class _MccpRelcTgOutCounter104_Type(Integer32):
    """Custom type mccpRelcTgOutCounter104 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter104_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter104_Object = MibTableColumn
mccpRelcTgOutCounter104 = _MccpRelcTgOutCounter104_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 106),
    _MccpRelcTgOutCounter104_Type()
)
mccpRelcTgOutCounter104.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter104.setStatus("current")


class _MccpRelcTgOutCounter105_Type(Integer32):
    """Custom type mccpRelcTgOutCounter105 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter105_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter105_Object = MibTableColumn
mccpRelcTgOutCounter105 = _MccpRelcTgOutCounter105_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 107),
    _MccpRelcTgOutCounter105_Type()
)
mccpRelcTgOutCounter105.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter105.setStatus("current")


class _MccpRelcTgOutCounter106_Type(Integer32):
    """Custom type mccpRelcTgOutCounter106 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter106_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter106_Object = MibTableColumn
mccpRelcTgOutCounter106 = _MccpRelcTgOutCounter106_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 108),
    _MccpRelcTgOutCounter106_Type()
)
mccpRelcTgOutCounter106.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter106.setStatus("current")


class _MccpRelcTgOutCounter107_Type(Integer32):
    """Custom type mccpRelcTgOutCounter107 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter107_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter107_Object = MibTableColumn
mccpRelcTgOutCounter107 = _MccpRelcTgOutCounter107_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 109),
    _MccpRelcTgOutCounter107_Type()
)
mccpRelcTgOutCounter107.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter107.setStatus("current")


class _MccpRelcTgOutCounter108_Type(Integer32):
    """Custom type mccpRelcTgOutCounter108 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter108_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter108_Object = MibTableColumn
mccpRelcTgOutCounter108 = _MccpRelcTgOutCounter108_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 110),
    _MccpRelcTgOutCounter108_Type()
)
mccpRelcTgOutCounter108.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter108.setStatus("current")


class _MccpRelcTgOutCounter109_Type(Integer32):
    """Custom type mccpRelcTgOutCounter109 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter109_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter109_Object = MibTableColumn
mccpRelcTgOutCounter109 = _MccpRelcTgOutCounter109_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 111),
    _MccpRelcTgOutCounter109_Type()
)
mccpRelcTgOutCounter109.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter109.setStatus("current")


class _MccpRelcTgOutCounter110_Type(Integer32):
    """Custom type mccpRelcTgOutCounter110 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter110_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter110_Object = MibTableColumn
mccpRelcTgOutCounter110 = _MccpRelcTgOutCounter110_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 112),
    _MccpRelcTgOutCounter110_Type()
)
mccpRelcTgOutCounter110.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter110.setStatus("current")


class _MccpRelcTgOutCounter111_Type(Integer32):
    """Custom type mccpRelcTgOutCounter111 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter111_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter111_Object = MibTableColumn
mccpRelcTgOutCounter111 = _MccpRelcTgOutCounter111_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 113),
    _MccpRelcTgOutCounter111_Type()
)
mccpRelcTgOutCounter111.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter111.setStatus("current")


class _MccpRelcTgOutCounter112_Type(Integer32):
    """Custom type mccpRelcTgOutCounter112 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter112_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter112_Object = MibTableColumn
mccpRelcTgOutCounter112 = _MccpRelcTgOutCounter112_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 114),
    _MccpRelcTgOutCounter112_Type()
)
mccpRelcTgOutCounter112.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter112.setStatus("current")


class _MccpRelcTgOutCounter113_Type(Integer32):
    """Custom type mccpRelcTgOutCounter113 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter113_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter113_Object = MibTableColumn
mccpRelcTgOutCounter113 = _MccpRelcTgOutCounter113_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 115),
    _MccpRelcTgOutCounter113_Type()
)
mccpRelcTgOutCounter113.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter113.setStatus("current")


class _MccpRelcTgOutCounter114_Type(Integer32):
    """Custom type mccpRelcTgOutCounter114 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter114_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter114_Object = MibTableColumn
mccpRelcTgOutCounter114 = _MccpRelcTgOutCounter114_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 116),
    _MccpRelcTgOutCounter114_Type()
)
mccpRelcTgOutCounter114.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter114.setStatus("current")


class _MccpRelcTgOutCounter115_Type(Integer32):
    """Custom type mccpRelcTgOutCounter115 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter115_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter115_Object = MibTableColumn
mccpRelcTgOutCounter115 = _MccpRelcTgOutCounter115_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 117),
    _MccpRelcTgOutCounter115_Type()
)
mccpRelcTgOutCounter115.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter115.setStatus("current")


class _MccpRelcTgOutCounter116_Type(Integer32):
    """Custom type mccpRelcTgOutCounter116 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter116_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter116_Object = MibTableColumn
mccpRelcTgOutCounter116 = _MccpRelcTgOutCounter116_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 118),
    _MccpRelcTgOutCounter116_Type()
)
mccpRelcTgOutCounter116.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter116.setStatus("current")


class _MccpRelcTgOutCounter117_Type(Integer32):
    """Custom type mccpRelcTgOutCounter117 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter117_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter117_Object = MibTableColumn
mccpRelcTgOutCounter117 = _MccpRelcTgOutCounter117_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 119),
    _MccpRelcTgOutCounter117_Type()
)
mccpRelcTgOutCounter117.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter117.setStatus("current")


class _MccpRelcTgOutCounter118_Type(Integer32):
    """Custom type mccpRelcTgOutCounter118 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter118_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter118_Object = MibTableColumn
mccpRelcTgOutCounter118 = _MccpRelcTgOutCounter118_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 120),
    _MccpRelcTgOutCounter118_Type()
)
mccpRelcTgOutCounter118.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter118.setStatus("current")


class _MccpRelcTgOutCounter119_Type(Integer32):
    """Custom type mccpRelcTgOutCounter119 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter119_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter119_Object = MibTableColumn
mccpRelcTgOutCounter119 = _MccpRelcTgOutCounter119_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 121),
    _MccpRelcTgOutCounter119_Type()
)
mccpRelcTgOutCounter119.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter119.setStatus("current")


class _MccpRelcTgOutCounter120_Type(Integer32):
    """Custom type mccpRelcTgOutCounter120 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter120_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter120_Object = MibTableColumn
mccpRelcTgOutCounter120 = _MccpRelcTgOutCounter120_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 122),
    _MccpRelcTgOutCounter120_Type()
)
mccpRelcTgOutCounter120.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter120.setStatus("current")


class _MccpRelcTgOutCounter121_Type(Integer32):
    """Custom type mccpRelcTgOutCounter121 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter121_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter121_Object = MibTableColumn
mccpRelcTgOutCounter121 = _MccpRelcTgOutCounter121_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 123),
    _MccpRelcTgOutCounter121_Type()
)
mccpRelcTgOutCounter121.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter121.setStatus("current")


class _MccpRelcTgOutCounter122_Type(Integer32):
    """Custom type mccpRelcTgOutCounter122 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter122_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter122_Object = MibTableColumn
mccpRelcTgOutCounter122 = _MccpRelcTgOutCounter122_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 124),
    _MccpRelcTgOutCounter122_Type()
)
mccpRelcTgOutCounter122.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter122.setStatus("current")


class _MccpRelcTgOutCounter123_Type(Integer32):
    """Custom type mccpRelcTgOutCounter123 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter123_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter123_Object = MibTableColumn
mccpRelcTgOutCounter123 = _MccpRelcTgOutCounter123_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 125),
    _MccpRelcTgOutCounter123_Type()
)
mccpRelcTgOutCounter123.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter123.setStatus("current")


class _MccpRelcTgOutCounter124_Type(Integer32):
    """Custom type mccpRelcTgOutCounter124 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter124_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter124_Object = MibTableColumn
mccpRelcTgOutCounter124 = _MccpRelcTgOutCounter124_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 126),
    _MccpRelcTgOutCounter124_Type()
)
mccpRelcTgOutCounter124.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter124.setStatus("current")


class _MccpRelcTgOutCounter125_Type(Integer32):
    """Custom type mccpRelcTgOutCounter125 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter125_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter125_Object = MibTableColumn
mccpRelcTgOutCounter125 = _MccpRelcTgOutCounter125_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 127),
    _MccpRelcTgOutCounter125_Type()
)
mccpRelcTgOutCounter125.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter125.setStatus("current")


class _MccpRelcTgOutCounter126_Type(Integer32):
    """Custom type mccpRelcTgOutCounter126 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter126_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter126_Object = MibTableColumn
mccpRelcTgOutCounter126 = _MccpRelcTgOutCounter126_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 128),
    _MccpRelcTgOutCounter126_Type()
)
mccpRelcTgOutCounter126.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter126.setStatus("current")


class _MccpRelcTgOutCounter127_Type(Integer32):
    """Custom type mccpRelcTgOutCounter127 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgOutCounter127_Type.__name__ = "Integer32"
_MccpRelcTgOutCounter127_Object = MibTableColumn
mccpRelcTgOutCounter127 = _MccpRelcTgOutCounter127_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 27, 1, 129),
    _MccpRelcTgOutCounter127_Type()
)
mccpRelcTgOutCounter127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgOutCounter127.setStatus("current")
_MccpRelcTgTrInTable_Object = MibTable
mccpRelcTgTrInTable = _MccpRelcTgTrInTable_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28)
)
if mibBuilder.loadTexts:
    mccpRelcTgTrInTable.setStatus("current")
_MccpRelcTgTrInEntry_Object = MibTableRow
mccpRelcTgTrInEntry = _MccpRelcTgTrInEntry_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1)
)
mccpRelcTgTrInEntry.setIndexNames(
    (0, "ELTEX-MCCP", "mccpRelcTgTrInIndex"),
)
if mibBuilder.loadTexts:
    mccpRelcTgTrInEntry.setStatus("current")


class _MccpRelcTgTrInIndex_Type(Integer32):
    """Custom type mccpRelcTgTrInIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MccpRelcTgTrInIndex_Type.__name__ = "Integer32"
_MccpRelcTgTrInIndex_Object = MibTableColumn
mccpRelcTgTrInIndex = _MccpRelcTgTrInIndex_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 1),
    _MccpRelcTgTrInIndex_Type()
)
mccpRelcTgTrInIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mccpRelcTgTrInIndex.setStatus("current")


class _MccpRelcTgTrInCounter0_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter0_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter0_Object = MibTableColumn
mccpRelcTgTrInCounter0 = _MccpRelcTgTrInCounter0_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 2),
    _MccpRelcTgTrInCounter0_Type()
)
mccpRelcTgTrInCounter0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter0.setStatus("current")


class _MccpRelcTgTrInCounter1_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter1_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter1_Object = MibTableColumn
mccpRelcTgTrInCounter1 = _MccpRelcTgTrInCounter1_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 3),
    _MccpRelcTgTrInCounter1_Type()
)
mccpRelcTgTrInCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter1.setStatus("current")


class _MccpRelcTgTrInCounter2_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter2_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter2_Object = MibTableColumn
mccpRelcTgTrInCounter2 = _MccpRelcTgTrInCounter2_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 4),
    _MccpRelcTgTrInCounter2_Type()
)
mccpRelcTgTrInCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter2.setStatus("current")


class _MccpRelcTgTrInCounter3_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter3_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter3_Object = MibTableColumn
mccpRelcTgTrInCounter3 = _MccpRelcTgTrInCounter3_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 5),
    _MccpRelcTgTrInCounter3_Type()
)
mccpRelcTgTrInCounter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter3.setStatus("current")


class _MccpRelcTgTrInCounter4_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter4_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter4_Object = MibTableColumn
mccpRelcTgTrInCounter4 = _MccpRelcTgTrInCounter4_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 6),
    _MccpRelcTgTrInCounter4_Type()
)
mccpRelcTgTrInCounter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter4.setStatus("current")


class _MccpRelcTgTrInCounter5_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter5_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter5_Object = MibTableColumn
mccpRelcTgTrInCounter5 = _MccpRelcTgTrInCounter5_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 7),
    _MccpRelcTgTrInCounter5_Type()
)
mccpRelcTgTrInCounter5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter5.setStatus("current")


class _MccpRelcTgTrInCounter6_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter6_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter6_Object = MibTableColumn
mccpRelcTgTrInCounter6 = _MccpRelcTgTrInCounter6_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 8),
    _MccpRelcTgTrInCounter6_Type()
)
mccpRelcTgTrInCounter6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter6.setStatus("current")


class _MccpRelcTgTrInCounter7_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter7_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter7_Object = MibTableColumn
mccpRelcTgTrInCounter7 = _MccpRelcTgTrInCounter7_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 9),
    _MccpRelcTgTrInCounter7_Type()
)
mccpRelcTgTrInCounter7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter7.setStatus("current")


class _MccpRelcTgTrInCounter8_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter8_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter8_Object = MibTableColumn
mccpRelcTgTrInCounter8 = _MccpRelcTgTrInCounter8_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 10),
    _MccpRelcTgTrInCounter8_Type()
)
mccpRelcTgTrInCounter8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter8.setStatus("current")


class _MccpRelcTgTrInCounter9_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter9_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter9_Object = MibTableColumn
mccpRelcTgTrInCounter9 = _MccpRelcTgTrInCounter9_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 11),
    _MccpRelcTgTrInCounter9_Type()
)
mccpRelcTgTrInCounter9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter9.setStatus("current")


class _MccpRelcTgTrInCounter10_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter10_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter10_Object = MibTableColumn
mccpRelcTgTrInCounter10 = _MccpRelcTgTrInCounter10_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 12),
    _MccpRelcTgTrInCounter10_Type()
)
mccpRelcTgTrInCounter10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter10.setStatus("current")


class _MccpRelcTgTrInCounter11_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter11_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter11_Object = MibTableColumn
mccpRelcTgTrInCounter11 = _MccpRelcTgTrInCounter11_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 13),
    _MccpRelcTgTrInCounter11_Type()
)
mccpRelcTgTrInCounter11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter11.setStatus("current")


class _MccpRelcTgTrInCounter12_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter12_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter12_Object = MibTableColumn
mccpRelcTgTrInCounter12 = _MccpRelcTgTrInCounter12_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 14),
    _MccpRelcTgTrInCounter12_Type()
)
mccpRelcTgTrInCounter12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter12.setStatus("current")


class _MccpRelcTgTrInCounter13_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter13_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter13_Object = MibTableColumn
mccpRelcTgTrInCounter13 = _MccpRelcTgTrInCounter13_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 15),
    _MccpRelcTgTrInCounter13_Type()
)
mccpRelcTgTrInCounter13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter13.setStatus("current")


class _MccpRelcTgTrInCounter14_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter14_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter14_Object = MibTableColumn
mccpRelcTgTrInCounter14 = _MccpRelcTgTrInCounter14_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 16),
    _MccpRelcTgTrInCounter14_Type()
)
mccpRelcTgTrInCounter14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter14.setStatus("current")


class _MccpRelcTgTrInCounter15_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter15_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter15_Object = MibTableColumn
mccpRelcTgTrInCounter15 = _MccpRelcTgTrInCounter15_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 17),
    _MccpRelcTgTrInCounter15_Type()
)
mccpRelcTgTrInCounter15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter15.setStatus("current")


class _MccpRelcTgTrInCounter16_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter16_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter16_Object = MibTableColumn
mccpRelcTgTrInCounter16 = _MccpRelcTgTrInCounter16_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 18),
    _MccpRelcTgTrInCounter16_Type()
)
mccpRelcTgTrInCounter16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter16.setStatus("current")


class _MccpRelcTgTrInCounter17_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter17_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter17_Object = MibTableColumn
mccpRelcTgTrInCounter17 = _MccpRelcTgTrInCounter17_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 19),
    _MccpRelcTgTrInCounter17_Type()
)
mccpRelcTgTrInCounter17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter17.setStatus("current")


class _MccpRelcTgTrInCounter18_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter18_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter18_Object = MibTableColumn
mccpRelcTgTrInCounter18 = _MccpRelcTgTrInCounter18_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 20),
    _MccpRelcTgTrInCounter18_Type()
)
mccpRelcTgTrInCounter18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter18.setStatus("current")


class _MccpRelcTgTrInCounter19_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter19_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter19_Object = MibTableColumn
mccpRelcTgTrInCounter19 = _MccpRelcTgTrInCounter19_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 21),
    _MccpRelcTgTrInCounter19_Type()
)
mccpRelcTgTrInCounter19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter19.setStatus("current")


class _MccpRelcTgTrInCounter20_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter20_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter20_Object = MibTableColumn
mccpRelcTgTrInCounter20 = _MccpRelcTgTrInCounter20_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 22),
    _MccpRelcTgTrInCounter20_Type()
)
mccpRelcTgTrInCounter20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter20.setStatus("current")


class _MccpRelcTgTrInCounter21_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter21_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter21_Object = MibTableColumn
mccpRelcTgTrInCounter21 = _MccpRelcTgTrInCounter21_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 23),
    _MccpRelcTgTrInCounter21_Type()
)
mccpRelcTgTrInCounter21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter21.setStatus("current")


class _MccpRelcTgTrInCounter22_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter22_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter22_Object = MibTableColumn
mccpRelcTgTrInCounter22 = _MccpRelcTgTrInCounter22_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 24),
    _MccpRelcTgTrInCounter22_Type()
)
mccpRelcTgTrInCounter22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter22.setStatus("current")


class _MccpRelcTgTrInCounter23_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter23_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter23_Object = MibTableColumn
mccpRelcTgTrInCounter23 = _MccpRelcTgTrInCounter23_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 25),
    _MccpRelcTgTrInCounter23_Type()
)
mccpRelcTgTrInCounter23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter23.setStatus("current")


class _MccpRelcTgTrInCounter24_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter24_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter24_Object = MibTableColumn
mccpRelcTgTrInCounter24 = _MccpRelcTgTrInCounter24_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 26),
    _MccpRelcTgTrInCounter24_Type()
)
mccpRelcTgTrInCounter24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter24.setStatus("current")


class _MccpRelcTgTrInCounter25_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter25_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter25_Object = MibTableColumn
mccpRelcTgTrInCounter25 = _MccpRelcTgTrInCounter25_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 27),
    _MccpRelcTgTrInCounter25_Type()
)
mccpRelcTgTrInCounter25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter25.setStatus("current")


class _MccpRelcTgTrInCounter26_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter26 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter26_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter26_Object = MibTableColumn
mccpRelcTgTrInCounter26 = _MccpRelcTgTrInCounter26_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 28),
    _MccpRelcTgTrInCounter26_Type()
)
mccpRelcTgTrInCounter26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter26.setStatus("current")


class _MccpRelcTgTrInCounter27_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter27 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter27_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter27_Object = MibTableColumn
mccpRelcTgTrInCounter27 = _MccpRelcTgTrInCounter27_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 29),
    _MccpRelcTgTrInCounter27_Type()
)
mccpRelcTgTrInCounter27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter27.setStatus("current")


class _MccpRelcTgTrInCounter28_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter28 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter28_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter28_Object = MibTableColumn
mccpRelcTgTrInCounter28 = _MccpRelcTgTrInCounter28_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 30),
    _MccpRelcTgTrInCounter28_Type()
)
mccpRelcTgTrInCounter28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter28.setStatus("current")


class _MccpRelcTgTrInCounter29_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter29 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter29_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter29_Object = MibTableColumn
mccpRelcTgTrInCounter29 = _MccpRelcTgTrInCounter29_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 31),
    _MccpRelcTgTrInCounter29_Type()
)
mccpRelcTgTrInCounter29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter29.setStatus("current")


class _MccpRelcTgTrInCounter30_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter30 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter30_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter30_Object = MibTableColumn
mccpRelcTgTrInCounter30 = _MccpRelcTgTrInCounter30_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 32),
    _MccpRelcTgTrInCounter30_Type()
)
mccpRelcTgTrInCounter30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter30.setStatus("current")


class _MccpRelcTgTrInCounter31_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter31 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter31_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter31_Object = MibTableColumn
mccpRelcTgTrInCounter31 = _MccpRelcTgTrInCounter31_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 33),
    _MccpRelcTgTrInCounter31_Type()
)
mccpRelcTgTrInCounter31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter31.setStatus("current")


class _MccpRelcTgTrInCounter32_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter32_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter32_Object = MibTableColumn
mccpRelcTgTrInCounter32 = _MccpRelcTgTrInCounter32_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 34),
    _MccpRelcTgTrInCounter32_Type()
)
mccpRelcTgTrInCounter32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter32.setStatus("current")


class _MccpRelcTgTrInCounter33_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter33 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter33_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter33_Object = MibTableColumn
mccpRelcTgTrInCounter33 = _MccpRelcTgTrInCounter33_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 35),
    _MccpRelcTgTrInCounter33_Type()
)
mccpRelcTgTrInCounter33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter33.setStatus("current")


class _MccpRelcTgTrInCounter34_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter34 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter34_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter34_Object = MibTableColumn
mccpRelcTgTrInCounter34 = _MccpRelcTgTrInCounter34_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 36),
    _MccpRelcTgTrInCounter34_Type()
)
mccpRelcTgTrInCounter34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter34.setStatus("current")


class _MccpRelcTgTrInCounter35_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter35 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter35_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter35_Object = MibTableColumn
mccpRelcTgTrInCounter35 = _MccpRelcTgTrInCounter35_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 37),
    _MccpRelcTgTrInCounter35_Type()
)
mccpRelcTgTrInCounter35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter35.setStatus("current")


class _MccpRelcTgTrInCounter36_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter36 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter36_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter36_Object = MibTableColumn
mccpRelcTgTrInCounter36 = _MccpRelcTgTrInCounter36_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 38),
    _MccpRelcTgTrInCounter36_Type()
)
mccpRelcTgTrInCounter36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter36.setStatus("current")


class _MccpRelcTgTrInCounter37_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter37 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter37_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter37_Object = MibTableColumn
mccpRelcTgTrInCounter37 = _MccpRelcTgTrInCounter37_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 39),
    _MccpRelcTgTrInCounter37_Type()
)
mccpRelcTgTrInCounter37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter37.setStatus("current")


class _MccpRelcTgTrInCounter38_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter38 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter38_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter38_Object = MibTableColumn
mccpRelcTgTrInCounter38 = _MccpRelcTgTrInCounter38_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 40),
    _MccpRelcTgTrInCounter38_Type()
)
mccpRelcTgTrInCounter38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter38.setStatus("current")


class _MccpRelcTgTrInCounter39_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter39 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter39_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter39_Object = MibTableColumn
mccpRelcTgTrInCounter39 = _MccpRelcTgTrInCounter39_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 41),
    _MccpRelcTgTrInCounter39_Type()
)
mccpRelcTgTrInCounter39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter39.setStatus("current")


class _MccpRelcTgTrInCounter40_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter40 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter40_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter40_Object = MibTableColumn
mccpRelcTgTrInCounter40 = _MccpRelcTgTrInCounter40_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 42),
    _MccpRelcTgTrInCounter40_Type()
)
mccpRelcTgTrInCounter40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter40.setStatus("current")


class _MccpRelcTgTrInCounter41_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter41 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter41_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter41_Object = MibTableColumn
mccpRelcTgTrInCounter41 = _MccpRelcTgTrInCounter41_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 43),
    _MccpRelcTgTrInCounter41_Type()
)
mccpRelcTgTrInCounter41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter41.setStatus("current")


class _MccpRelcTgTrInCounter42_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter42 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter42_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter42_Object = MibTableColumn
mccpRelcTgTrInCounter42 = _MccpRelcTgTrInCounter42_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 44),
    _MccpRelcTgTrInCounter42_Type()
)
mccpRelcTgTrInCounter42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter42.setStatus("current")


class _MccpRelcTgTrInCounter43_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter43 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter43_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter43_Object = MibTableColumn
mccpRelcTgTrInCounter43 = _MccpRelcTgTrInCounter43_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 45),
    _MccpRelcTgTrInCounter43_Type()
)
mccpRelcTgTrInCounter43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter43.setStatus("current")


class _MccpRelcTgTrInCounter44_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter44 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter44_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter44_Object = MibTableColumn
mccpRelcTgTrInCounter44 = _MccpRelcTgTrInCounter44_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 46),
    _MccpRelcTgTrInCounter44_Type()
)
mccpRelcTgTrInCounter44.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter44.setStatus("current")


class _MccpRelcTgTrInCounter45_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter45 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter45_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter45_Object = MibTableColumn
mccpRelcTgTrInCounter45 = _MccpRelcTgTrInCounter45_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 47),
    _MccpRelcTgTrInCounter45_Type()
)
mccpRelcTgTrInCounter45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter45.setStatus("current")


class _MccpRelcTgTrInCounter46_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter46 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter46_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter46_Object = MibTableColumn
mccpRelcTgTrInCounter46 = _MccpRelcTgTrInCounter46_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 48),
    _MccpRelcTgTrInCounter46_Type()
)
mccpRelcTgTrInCounter46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter46.setStatus("current")


class _MccpRelcTgTrInCounter47_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter47 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter47_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter47_Object = MibTableColumn
mccpRelcTgTrInCounter47 = _MccpRelcTgTrInCounter47_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 49),
    _MccpRelcTgTrInCounter47_Type()
)
mccpRelcTgTrInCounter47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter47.setStatus("current")


class _MccpRelcTgTrInCounter48_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter48 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter48_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter48_Object = MibTableColumn
mccpRelcTgTrInCounter48 = _MccpRelcTgTrInCounter48_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 50),
    _MccpRelcTgTrInCounter48_Type()
)
mccpRelcTgTrInCounter48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter48.setStatus("current")


class _MccpRelcTgTrInCounter49_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter49 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter49_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter49_Object = MibTableColumn
mccpRelcTgTrInCounter49 = _MccpRelcTgTrInCounter49_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 51),
    _MccpRelcTgTrInCounter49_Type()
)
mccpRelcTgTrInCounter49.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter49.setStatus("current")


class _MccpRelcTgTrInCounter50_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter50 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter50_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter50_Object = MibTableColumn
mccpRelcTgTrInCounter50 = _MccpRelcTgTrInCounter50_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 52),
    _MccpRelcTgTrInCounter50_Type()
)
mccpRelcTgTrInCounter50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter50.setStatus("current")


class _MccpRelcTgTrInCounter51_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter51 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter51_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter51_Object = MibTableColumn
mccpRelcTgTrInCounter51 = _MccpRelcTgTrInCounter51_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 53),
    _MccpRelcTgTrInCounter51_Type()
)
mccpRelcTgTrInCounter51.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter51.setStatus("current")


class _MccpRelcTgTrInCounter52_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter52 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter52_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter52_Object = MibTableColumn
mccpRelcTgTrInCounter52 = _MccpRelcTgTrInCounter52_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 54),
    _MccpRelcTgTrInCounter52_Type()
)
mccpRelcTgTrInCounter52.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter52.setStatus("current")


class _MccpRelcTgTrInCounter53_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter53 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter53_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter53_Object = MibTableColumn
mccpRelcTgTrInCounter53 = _MccpRelcTgTrInCounter53_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 55),
    _MccpRelcTgTrInCounter53_Type()
)
mccpRelcTgTrInCounter53.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter53.setStatus("current")


class _MccpRelcTgTrInCounter54_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter54 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter54_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter54_Object = MibTableColumn
mccpRelcTgTrInCounter54 = _MccpRelcTgTrInCounter54_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 56),
    _MccpRelcTgTrInCounter54_Type()
)
mccpRelcTgTrInCounter54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter54.setStatus("current")


class _MccpRelcTgTrInCounter55_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter55 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter55_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter55_Object = MibTableColumn
mccpRelcTgTrInCounter55 = _MccpRelcTgTrInCounter55_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 57),
    _MccpRelcTgTrInCounter55_Type()
)
mccpRelcTgTrInCounter55.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter55.setStatus("current")


class _MccpRelcTgTrInCounter56_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter56 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter56_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter56_Object = MibTableColumn
mccpRelcTgTrInCounter56 = _MccpRelcTgTrInCounter56_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 58),
    _MccpRelcTgTrInCounter56_Type()
)
mccpRelcTgTrInCounter56.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter56.setStatus("current")


class _MccpRelcTgTrInCounter57_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter57 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter57_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter57_Object = MibTableColumn
mccpRelcTgTrInCounter57 = _MccpRelcTgTrInCounter57_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 59),
    _MccpRelcTgTrInCounter57_Type()
)
mccpRelcTgTrInCounter57.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter57.setStatus("current")


class _MccpRelcTgTrInCounter58_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter58 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter58_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter58_Object = MibTableColumn
mccpRelcTgTrInCounter58 = _MccpRelcTgTrInCounter58_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 60),
    _MccpRelcTgTrInCounter58_Type()
)
mccpRelcTgTrInCounter58.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter58.setStatus("current")


class _MccpRelcTgTrInCounter59_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter59 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter59_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter59_Object = MibTableColumn
mccpRelcTgTrInCounter59 = _MccpRelcTgTrInCounter59_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 61),
    _MccpRelcTgTrInCounter59_Type()
)
mccpRelcTgTrInCounter59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter59.setStatus("current")


class _MccpRelcTgTrInCounter60_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter60 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter60_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter60_Object = MibTableColumn
mccpRelcTgTrInCounter60 = _MccpRelcTgTrInCounter60_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 62),
    _MccpRelcTgTrInCounter60_Type()
)
mccpRelcTgTrInCounter60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter60.setStatus("current")


class _MccpRelcTgTrInCounter61_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter61 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter61_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter61_Object = MibTableColumn
mccpRelcTgTrInCounter61 = _MccpRelcTgTrInCounter61_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 63),
    _MccpRelcTgTrInCounter61_Type()
)
mccpRelcTgTrInCounter61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter61.setStatus("current")


class _MccpRelcTgTrInCounter62_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter62 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter62_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter62_Object = MibTableColumn
mccpRelcTgTrInCounter62 = _MccpRelcTgTrInCounter62_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 64),
    _MccpRelcTgTrInCounter62_Type()
)
mccpRelcTgTrInCounter62.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter62.setStatus("current")


class _MccpRelcTgTrInCounter63_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter63 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter63_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter63_Object = MibTableColumn
mccpRelcTgTrInCounter63 = _MccpRelcTgTrInCounter63_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 65),
    _MccpRelcTgTrInCounter63_Type()
)
mccpRelcTgTrInCounter63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter63.setStatus("current")


class _MccpRelcTgTrInCounter64_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter64 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter64_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter64_Object = MibTableColumn
mccpRelcTgTrInCounter64 = _MccpRelcTgTrInCounter64_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 66),
    _MccpRelcTgTrInCounter64_Type()
)
mccpRelcTgTrInCounter64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter64.setStatus("current")


class _MccpRelcTgTrInCounter65_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter65 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter65_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter65_Object = MibTableColumn
mccpRelcTgTrInCounter65 = _MccpRelcTgTrInCounter65_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 67),
    _MccpRelcTgTrInCounter65_Type()
)
mccpRelcTgTrInCounter65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter65.setStatus("current")


class _MccpRelcTgTrInCounter66_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter66 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter66_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter66_Object = MibTableColumn
mccpRelcTgTrInCounter66 = _MccpRelcTgTrInCounter66_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 68),
    _MccpRelcTgTrInCounter66_Type()
)
mccpRelcTgTrInCounter66.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter66.setStatus("current")


class _MccpRelcTgTrInCounter67_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter67 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter67_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter67_Object = MibTableColumn
mccpRelcTgTrInCounter67 = _MccpRelcTgTrInCounter67_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 69),
    _MccpRelcTgTrInCounter67_Type()
)
mccpRelcTgTrInCounter67.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter67.setStatus("current")


class _MccpRelcTgTrInCounter68_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter68 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter68_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter68_Object = MibTableColumn
mccpRelcTgTrInCounter68 = _MccpRelcTgTrInCounter68_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 70),
    _MccpRelcTgTrInCounter68_Type()
)
mccpRelcTgTrInCounter68.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter68.setStatus("current")


class _MccpRelcTgTrInCounter69_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter69 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter69_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter69_Object = MibTableColumn
mccpRelcTgTrInCounter69 = _MccpRelcTgTrInCounter69_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 71),
    _MccpRelcTgTrInCounter69_Type()
)
mccpRelcTgTrInCounter69.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter69.setStatus("current")


class _MccpRelcTgTrInCounter70_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter70 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter70_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter70_Object = MibTableColumn
mccpRelcTgTrInCounter70 = _MccpRelcTgTrInCounter70_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 72),
    _MccpRelcTgTrInCounter70_Type()
)
mccpRelcTgTrInCounter70.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter70.setStatus("current")


class _MccpRelcTgTrInCounter71_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter71 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter71_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter71_Object = MibTableColumn
mccpRelcTgTrInCounter71 = _MccpRelcTgTrInCounter71_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 73),
    _MccpRelcTgTrInCounter71_Type()
)
mccpRelcTgTrInCounter71.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter71.setStatus("current")


class _MccpRelcTgTrInCounter72_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter72 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter72_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter72_Object = MibTableColumn
mccpRelcTgTrInCounter72 = _MccpRelcTgTrInCounter72_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 74),
    _MccpRelcTgTrInCounter72_Type()
)
mccpRelcTgTrInCounter72.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter72.setStatus("current")


class _MccpRelcTgTrInCounter73_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter73 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter73_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter73_Object = MibTableColumn
mccpRelcTgTrInCounter73 = _MccpRelcTgTrInCounter73_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 75),
    _MccpRelcTgTrInCounter73_Type()
)
mccpRelcTgTrInCounter73.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter73.setStatus("current")


class _MccpRelcTgTrInCounter74_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter74 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter74_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter74_Object = MibTableColumn
mccpRelcTgTrInCounter74 = _MccpRelcTgTrInCounter74_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 76),
    _MccpRelcTgTrInCounter74_Type()
)
mccpRelcTgTrInCounter74.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter74.setStatus("current")


class _MccpRelcTgTrInCounter75_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter75 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter75_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter75_Object = MibTableColumn
mccpRelcTgTrInCounter75 = _MccpRelcTgTrInCounter75_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 77),
    _MccpRelcTgTrInCounter75_Type()
)
mccpRelcTgTrInCounter75.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter75.setStatus("current")


class _MccpRelcTgTrInCounter76_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter76 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter76_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter76_Object = MibTableColumn
mccpRelcTgTrInCounter76 = _MccpRelcTgTrInCounter76_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 78),
    _MccpRelcTgTrInCounter76_Type()
)
mccpRelcTgTrInCounter76.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter76.setStatus("current")


class _MccpRelcTgTrInCounter77_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter77 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter77_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter77_Object = MibTableColumn
mccpRelcTgTrInCounter77 = _MccpRelcTgTrInCounter77_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 79),
    _MccpRelcTgTrInCounter77_Type()
)
mccpRelcTgTrInCounter77.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter77.setStatus("current")


class _MccpRelcTgTrInCounter78_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter78 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter78_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter78_Object = MibTableColumn
mccpRelcTgTrInCounter78 = _MccpRelcTgTrInCounter78_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 80),
    _MccpRelcTgTrInCounter78_Type()
)
mccpRelcTgTrInCounter78.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter78.setStatus("current")


class _MccpRelcTgTrInCounter79_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter79 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter79_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter79_Object = MibTableColumn
mccpRelcTgTrInCounter79 = _MccpRelcTgTrInCounter79_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 81),
    _MccpRelcTgTrInCounter79_Type()
)
mccpRelcTgTrInCounter79.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter79.setStatus("current")


class _MccpRelcTgTrInCounter80_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter80 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter80_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter80_Object = MibTableColumn
mccpRelcTgTrInCounter80 = _MccpRelcTgTrInCounter80_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 82),
    _MccpRelcTgTrInCounter80_Type()
)
mccpRelcTgTrInCounter80.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter80.setStatus("current")


class _MccpRelcTgTrInCounter81_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter81 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter81_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter81_Object = MibTableColumn
mccpRelcTgTrInCounter81 = _MccpRelcTgTrInCounter81_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 83),
    _MccpRelcTgTrInCounter81_Type()
)
mccpRelcTgTrInCounter81.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter81.setStatus("current")


class _MccpRelcTgTrInCounter82_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter82_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter82_Object = MibTableColumn
mccpRelcTgTrInCounter82 = _MccpRelcTgTrInCounter82_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 84),
    _MccpRelcTgTrInCounter82_Type()
)
mccpRelcTgTrInCounter82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter82.setStatus("current")


class _MccpRelcTgTrInCounter83_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter83 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter83_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter83_Object = MibTableColumn
mccpRelcTgTrInCounter83 = _MccpRelcTgTrInCounter83_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 85),
    _MccpRelcTgTrInCounter83_Type()
)
mccpRelcTgTrInCounter83.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter83.setStatus("current")


class _MccpRelcTgTrInCounter84_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter84 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter84_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter84_Object = MibTableColumn
mccpRelcTgTrInCounter84 = _MccpRelcTgTrInCounter84_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 86),
    _MccpRelcTgTrInCounter84_Type()
)
mccpRelcTgTrInCounter84.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter84.setStatus("current")


class _MccpRelcTgTrInCounter85_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter85 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter85_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter85_Object = MibTableColumn
mccpRelcTgTrInCounter85 = _MccpRelcTgTrInCounter85_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 87),
    _MccpRelcTgTrInCounter85_Type()
)
mccpRelcTgTrInCounter85.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter85.setStatus("current")


class _MccpRelcTgTrInCounter86_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter86 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter86_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter86_Object = MibTableColumn
mccpRelcTgTrInCounter86 = _MccpRelcTgTrInCounter86_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 88),
    _MccpRelcTgTrInCounter86_Type()
)
mccpRelcTgTrInCounter86.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter86.setStatus("current")


class _MccpRelcTgTrInCounter87_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter87 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter87_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter87_Object = MibTableColumn
mccpRelcTgTrInCounter87 = _MccpRelcTgTrInCounter87_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 89),
    _MccpRelcTgTrInCounter87_Type()
)
mccpRelcTgTrInCounter87.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter87.setStatus("current")


class _MccpRelcTgTrInCounter88_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter88 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter88_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter88_Object = MibTableColumn
mccpRelcTgTrInCounter88 = _MccpRelcTgTrInCounter88_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 90),
    _MccpRelcTgTrInCounter88_Type()
)
mccpRelcTgTrInCounter88.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter88.setStatus("current")


class _MccpRelcTgTrInCounter89_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter89 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter89_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter89_Object = MibTableColumn
mccpRelcTgTrInCounter89 = _MccpRelcTgTrInCounter89_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 91),
    _MccpRelcTgTrInCounter89_Type()
)
mccpRelcTgTrInCounter89.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter89.setStatus("current")


class _MccpRelcTgTrInCounter90_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter90 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter90_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter90_Object = MibTableColumn
mccpRelcTgTrInCounter90 = _MccpRelcTgTrInCounter90_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 92),
    _MccpRelcTgTrInCounter90_Type()
)
mccpRelcTgTrInCounter90.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter90.setStatus("current")


class _MccpRelcTgTrInCounter91_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter91 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter91_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter91_Object = MibTableColumn
mccpRelcTgTrInCounter91 = _MccpRelcTgTrInCounter91_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 93),
    _MccpRelcTgTrInCounter91_Type()
)
mccpRelcTgTrInCounter91.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter91.setStatus("current")


class _MccpRelcTgTrInCounter92_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter92 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter92_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter92_Object = MibTableColumn
mccpRelcTgTrInCounter92 = _MccpRelcTgTrInCounter92_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 94),
    _MccpRelcTgTrInCounter92_Type()
)
mccpRelcTgTrInCounter92.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter92.setStatus("current")


class _MccpRelcTgTrInCounter93_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter93 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter93_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter93_Object = MibTableColumn
mccpRelcTgTrInCounter93 = _MccpRelcTgTrInCounter93_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 95),
    _MccpRelcTgTrInCounter93_Type()
)
mccpRelcTgTrInCounter93.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter93.setStatus("current")


class _MccpRelcTgTrInCounter94_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter94 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter94_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter94_Object = MibTableColumn
mccpRelcTgTrInCounter94 = _MccpRelcTgTrInCounter94_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 96),
    _MccpRelcTgTrInCounter94_Type()
)
mccpRelcTgTrInCounter94.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter94.setStatus("current")


class _MccpRelcTgTrInCounter95_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter95 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter95_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter95_Object = MibTableColumn
mccpRelcTgTrInCounter95 = _MccpRelcTgTrInCounter95_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 97),
    _MccpRelcTgTrInCounter95_Type()
)
mccpRelcTgTrInCounter95.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter95.setStatus("current")


class _MccpRelcTgTrInCounter96_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter96 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter96_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter96_Object = MibTableColumn
mccpRelcTgTrInCounter96 = _MccpRelcTgTrInCounter96_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 98),
    _MccpRelcTgTrInCounter96_Type()
)
mccpRelcTgTrInCounter96.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter96.setStatus("current")


class _MccpRelcTgTrInCounter97_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter97 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter97_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter97_Object = MibTableColumn
mccpRelcTgTrInCounter97 = _MccpRelcTgTrInCounter97_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 99),
    _MccpRelcTgTrInCounter97_Type()
)
mccpRelcTgTrInCounter97.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter97.setStatus("current")


class _MccpRelcTgTrInCounter98_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter98 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter98_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter98_Object = MibTableColumn
mccpRelcTgTrInCounter98 = _MccpRelcTgTrInCounter98_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 100),
    _MccpRelcTgTrInCounter98_Type()
)
mccpRelcTgTrInCounter98.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter98.setStatus("current")


class _MccpRelcTgTrInCounter99_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter99 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter99_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter99_Object = MibTableColumn
mccpRelcTgTrInCounter99 = _MccpRelcTgTrInCounter99_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 101),
    _MccpRelcTgTrInCounter99_Type()
)
mccpRelcTgTrInCounter99.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter99.setStatus("current")


class _MccpRelcTgTrInCounter100_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter100 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter100_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter100_Object = MibTableColumn
mccpRelcTgTrInCounter100 = _MccpRelcTgTrInCounter100_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 102),
    _MccpRelcTgTrInCounter100_Type()
)
mccpRelcTgTrInCounter100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter100.setStatus("current")


class _MccpRelcTgTrInCounter101_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter101 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter101_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter101_Object = MibTableColumn
mccpRelcTgTrInCounter101 = _MccpRelcTgTrInCounter101_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 103),
    _MccpRelcTgTrInCounter101_Type()
)
mccpRelcTgTrInCounter101.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter101.setStatus("current")


class _MccpRelcTgTrInCounter102_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter102 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter102_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter102_Object = MibTableColumn
mccpRelcTgTrInCounter102 = _MccpRelcTgTrInCounter102_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 104),
    _MccpRelcTgTrInCounter102_Type()
)
mccpRelcTgTrInCounter102.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter102.setStatus("current")


class _MccpRelcTgTrInCounter103_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter103 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter103_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter103_Object = MibTableColumn
mccpRelcTgTrInCounter103 = _MccpRelcTgTrInCounter103_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 105),
    _MccpRelcTgTrInCounter103_Type()
)
mccpRelcTgTrInCounter103.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter103.setStatus("current")


class _MccpRelcTgTrInCounter104_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter104 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter104_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter104_Object = MibTableColumn
mccpRelcTgTrInCounter104 = _MccpRelcTgTrInCounter104_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 106),
    _MccpRelcTgTrInCounter104_Type()
)
mccpRelcTgTrInCounter104.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter104.setStatus("current")


class _MccpRelcTgTrInCounter105_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter105 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter105_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter105_Object = MibTableColumn
mccpRelcTgTrInCounter105 = _MccpRelcTgTrInCounter105_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 107),
    _MccpRelcTgTrInCounter105_Type()
)
mccpRelcTgTrInCounter105.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter105.setStatus("current")


class _MccpRelcTgTrInCounter106_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter106 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter106_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter106_Object = MibTableColumn
mccpRelcTgTrInCounter106 = _MccpRelcTgTrInCounter106_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 108),
    _MccpRelcTgTrInCounter106_Type()
)
mccpRelcTgTrInCounter106.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter106.setStatus("current")


class _MccpRelcTgTrInCounter107_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter107 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter107_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter107_Object = MibTableColumn
mccpRelcTgTrInCounter107 = _MccpRelcTgTrInCounter107_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 109),
    _MccpRelcTgTrInCounter107_Type()
)
mccpRelcTgTrInCounter107.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter107.setStatus("current")


class _MccpRelcTgTrInCounter108_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter108 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter108_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter108_Object = MibTableColumn
mccpRelcTgTrInCounter108 = _MccpRelcTgTrInCounter108_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 110),
    _MccpRelcTgTrInCounter108_Type()
)
mccpRelcTgTrInCounter108.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter108.setStatus("current")


class _MccpRelcTgTrInCounter109_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter109 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter109_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter109_Object = MibTableColumn
mccpRelcTgTrInCounter109 = _MccpRelcTgTrInCounter109_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 111),
    _MccpRelcTgTrInCounter109_Type()
)
mccpRelcTgTrInCounter109.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter109.setStatus("current")


class _MccpRelcTgTrInCounter110_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter110 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter110_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter110_Object = MibTableColumn
mccpRelcTgTrInCounter110 = _MccpRelcTgTrInCounter110_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 112),
    _MccpRelcTgTrInCounter110_Type()
)
mccpRelcTgTrInCounter110.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter110.setStatus("current")


class _MccpRelcTgTrInCounter111_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter111 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter111_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter111_Object = MibTableColumn
mccpRelcTgTrInCounter111 = _MccpRelcTgTrInCounter111_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 113),
    _MccpRelcTgTrInCounter111_Type()
)
mccpRelcTgTrInCounter111.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter111.setStatus("current")


class _MccpRelcTgTrInCounter112_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter112 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter112_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter112_Object = MibTableColumn
mccpRelcTgTrInCounter112 = _MccpRelcTgTrInCounter112_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 114),
    _MccpRelcTgTrInCounter112_Type()
)
mccpRelcTgTrInCounter112.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter112.setStatus("current")


class _MccpRelcTgTrInCounter113_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter113 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter113_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter113_Object = MibTableColumn
mccpRelcTgTrInCounter113 = _MccpRelcTgTrInCounter113_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 115),
    _MccpRelcTgTrInCounter113_Type()
)
mccpRelcTgTrInCounter113.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter113.setStatus("current")


class _MccpRelcTgTrInCounter114_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter114 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter114_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter114_Object = MibTableColumn
mccpRelcTgTrInCounter114 = _MccpRelcTgTrInCounter114_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 116),
    _MccpRelcTgTrInCounter114_Type()
)
mccpRelcTgTrInCounter114.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter114.setStatus("current")


class _MccpRelcTgTrInCounter115_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter115 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter115_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter115_Object = MibTableColumn
mccpRelcTgTrInCounter115 = _MccpRelcTgTrInCounter115_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 117),
    _MccpRelcTgTrInCounter115_Type()
)
mccpRelcTgTrInCounter115.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter115.setStatus("current")


class _MccpRelcTgTrInCounter116_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter116 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter116_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter116_Object = MibTableColumn
mccpRelcTgTrInCounter116 = _MccpRelcTgTrInCounter116_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 118),
    _MccpRelcTgTrInCounter116_Type()
)
mccpRelcTgTrInCounter116.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter116.setStatus("current")


class _MccpRelcTgTrInCounter117_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter117 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter117_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter117_Object = MibTableColumn
mccpRelcTgTrInCounter117 = _MccpRelcTgTrInCounter117_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 119),
    _MccpRelcTgTrInCounter117_Type()
)
mccpRelcTgTrInCounter117.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter117.setStatus("current")


class _MccpRelcTgTrInCounter118_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter118 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter118_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter118_Object = MibTableColumn
mccpRelcTgTrInCounter118 = _MccpRelcTgTrInCounter118_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 120),
    _MccpRelcTgTrInCounter118_Type()
)
mccpRelcTgTrInCounter118.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter118.setStatus("current")


class _MccpRelcTgTrInCounter119_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter119 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter119_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter119_Object = MibTableColumn
mccpRelcTgTrInCounter119 = _MccpRelcTgTrInCounter119_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 121),
    _MccpRelcTgTrInCounter119_Type()
)
mccpRelcTgTrInCounter119.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter119.setStatus("current")


class _MccpRelcTgTrInCounter120_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter120 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter120_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter120_Object = MibTableColumn
mccpRelcTgTrInCounter120 = _MccpRelcTgTrInCounter120_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 122),
    _MccpRelcTgTrInCounter120_Type()
)
mccpRelcTgTrInCounter120.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter120.setStatus("current")


class _MccpRelcTgTrInCounter121_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter121 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter121_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter121_Object = MibTableColumn
mccpRelcTgTrInCounter121 = _MccpRelcTgTrInCounter121_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 123),
    _MccpRelcTgTrInCounter121_Type()
)
mccpRelcTgTrInCounter121.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter121.setStatus("current")


class _MccpRelcTgTrInCounter122_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter122 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter122_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter122_Object = MibTableColumn
mccpRelcTgTrInCounter122 = _MccpRelcTgTrInCounter122_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 124),
    _MccpRelcTgTrInCounter122_Type()
)
mccpRelcTgTrInCounter122.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter122.setStatus("current")


class _MccpRelcTgTrInCounter123_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter123 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter123_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter123_Object = MibTableColumn
mccpRelcTgTrInCounter123 = _MccpRelcTgTrInCounter123_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 125),
    _MccpRelcTgTrInCounter123_Type()
)
mccpRelcTgTrInCounter123.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter123.setStatus("current")


class _MccpRelcTgTrInCounter124_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter124 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter124_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter124_Object = MibTableColumn
mccpRelcTgTrInCounter124 = _MccpRelcTgTrInCounter124_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 126),
    _MccpRelcTgTrInCounter124_Type()
)
mccpRelcTgTrInCounter124.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter124.setStatus("current")


class _MccpRelcTgTrInCounter125_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter125 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter125_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter125_Object = MibTableColumn
mccpRelcTgTrInCounter125 = _MccpRelcTgTrInCounter125_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 127),
    _MccpRelcTgTrInCounter125_Type()
)
mccpRelcTgTrInCounter125.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter125.setStatus("current")


class _MccpRelcTgTrInCounter126_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter126 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter126_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter126_Object = MibTableColumn
mccpRelcTgTrInCounter126 = _MccpRelcTgTrInCounter126_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 128),
    _MccpRelcTgTrInCounter126_Type()
)
mccpRelcTgTrInCounter126.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter126.setStatus("current")


class _MccpRelcTgTrInCounter127_Type(Integer32):
    """Custom type mccpRelcTgTrInCounter127 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrInCounter127_Type.__name__ = "Integer32"
_MccpRelcTgTrInCounter127_Object = MibTableColumn
mccpRelcTgTrInCounter127 = _MccpRelcTgTrInCounter127_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 28, 1, 129),
    _MccpRelcTgTrInCounter127_Type()
)
mccpRelcTgTrInCounter127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrInCounter127.setStatus("current")
_MccpRelcTgTrOutTable_Object = MibTable
mccpRelcTgTrOutTable = _MccpRelcTgTrOutTable_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29)
)
if mibBuilder.loadTexts:
    mccpRelcTgTrOutTable.setStatus("current")
_MccpRelcTgTrOutEntry_Object = MibTableRow
mccpRelcTgTrOutEntry = _MccpRelcTgTrOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1)
)
mccpRelcTgTrOutEntry.setIndexNames(
    (0, "ELTEX-MCCP", "mccpRelcTgTrOutIndex"),
)
if mibBuilder.loadTexts:
    mccpRelcTgTrOutEntry.setStatus("current")


class _MccpRelcTgTrOutIndex_Type(Integer32):
    """Custom type mccpRelcTgTrOutIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MccpRelcTgTrOutIndex_Type.__name__ = "Integer32"
_MccpRelcTgTrOutIndex_Object = MibTableColumn
mccpRelcTgTrOutIndex = _MccpRelcTgTrOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 1),
    _MccpRelcTgTrOutIndex_Type()
)
mccpRelcTgTrOutIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutIndex.setStatus("current")


class _MccpRelcTgTrOutCounter0_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter0_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter0_Object = MibTableColumn
mccpRelcTgTrOutCounter0 = _MccpRelcTgTrOutCounter0_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 2),
    _MccpRelcTgTrOutCounter0_Type()
)
mccpRelcTgTrOutCounter0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter0.setStatus("current")


class _MccpRelcTgTrOutCounter1_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter1_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter1_Object = MibTableColumn
mccpRelcTgTrOutCounter1 = _MccpRelcTgTrOutCounter1_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 3),
    _MccpRelcTgTrOutCounter1_Type()
)
mccpRelcTgTrOutCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter1.setStatus("current")


class _MccpRelcTgTrOutCounter2_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter2_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter2_Object = MibTableColumn
mccpRelcTgTrOutCounter2 = _MccpRelcTgTrOutCounter2_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 4),
    _MccpRelcTgTrOutCounter2_Type()
)
mccpRelcTgTrOutCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter2.setStatus("current")


class _MccpRelcTgTrOutCounter3_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter3_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter3_Object = MibTableColumn
mccpRelcTgTrOutCounter3 = _MccpRelcTgTrOutCounter3_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 5),
    _MccpRelcTgTrOutCounter3_Type()
)
mccpRelcTgTrOutCounter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter3.setStatus("current")


class _MccpRelcTgTrOutCounter4_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter4_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter4_Object = MibTableColumn
mccpRelcTgTrOutCounter4 = _MccpRelcTgTrOutCounter4_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 6),
    _MccpRelcTgTrOutCounter4_Type()
)
mccpRelcTgTrOutCounter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter4.setStatus("current")


class _MccpRelcTgTrOutCounter5_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter5_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter5_Object = MibTableColumn
mccpRelcTgTrOutCounter5 = _MccpRelcTgTrOutCounter5_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 7),
    _MccpRelcTgTrOutCounter5_Type()
)
mccpRelcTgTrOutCounter5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter5.setStatus("current")


class _MccpRelcTgTrOutCounter6_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter6_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter6_Object = MibTableColumn
mccpRelcTgTrOutCounter6 = _MccpRelcTgTrOutCounter6_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 8),
    _MccpRelcTgTrOutCounter6_Type()
)
mccpRelcTgTrOutCounter6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter6.setStatus("current")


class _MccpRelcTgTrOutCounter7_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter7_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter7_Object = MibTableColumn
mccpRelcTgTrOutCounter7 = _MccpRelcTgTrOutCounter7_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 9),
    _MccpRelcTgTrOutCounter7_Type()
)
mccpRelcTgTrOutCounter7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter7.setStatus("current")


class _MccpRelcTgTrOutCounter8_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter8_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter8_Object = MibTableColumn
mccpRelcTgTrOutCounter8 = _MccpRelcTgTrOutCounter8_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 10),
    _MccpRelcTgTrOutCounter8_Type()
)
mccpRelcTgTrOutCounter8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter8.setStatus("current")


class _MccpRelcTgTrOutCounter9_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter9_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter9_Object = MibTableColumn
mccpRelcTgTrOutCounter9 = _MccpRelcTgTrOutCounter9_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 11),
    _MccpRelcTgTrOutCounter9_Type()
)
mccpRelcTgTrOutCounter9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter9.setStatus("current")


class _MccpRelcTgTrOutCounter10_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter10_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter10_Object = MibTableColumn
mccpRelcTgTrOutCounter10 = _MccpRelcTgTrOutCounter10_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 12),
    _MccpRelcTgTrOutCounter10_Type()
)
mccpRelcTgTrOutCounter10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter10.setStatus("current")


class _MccpRelcTgTrOutCounter11_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter11_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter11_Object = MibTableColumn
mccpRelcTgTrOutCounter11 = _MccpRelcTgTrOutCounter11_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 13),
    _MccpRelcTgTrOutCounter11_Type()
)
mccpRelcTgTrOutCounter11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter11.setStatus("current")


class _MccpRelcTgTrOutCounter12_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter12_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter12_Object = MibTableColumn
mccpRelcTgTrOutCounter12 = _MccpRelcTgTrOutCounter12_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 14),
    _MccpRelcTgTrOutCounter12_Type()
)
mccpRelcTgTrOutCounter12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter12.setStatus("current")


class _MccpRelcTgTrOutCounter13_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter13_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter13_Object = MibTableColumn
mccpRelcTgTrOutCounter13 = _MccpRelcTgTrOutCounter13_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 15),
    _MccpRelcTgTrOutCounter13_Type()
)
mccpRelcTgTrOutCounter13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter13.setStatus("current")


class _MccpRelcTgTrOutCounter14_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter14_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter14_Object = MibTableColumn
mccpRelcTgTrOutCounter14 = _MccpRelcTgTrOutCounter14_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 16),
    _MccpRelcTgTrOutCounter14_Type()
)
mccpRelcTgTrOutCounter14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter14.setStatus("current")


class _MccpRelcTgTrOutCounter15_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter15_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter15_Object = MibTableColumn
mccpRelcTgTrOutCounter15 = _MccpRelcTgTrOutCounter15_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 17),
    _MccpRelcTgTrOutCounter15_Type()
)
mccpRelcTgTrOutCounter15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter15.setStatus("current")


class _MccpRelcTgTrOutCounter16_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter16_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter16_Object = MibTableColumn
mccpRelcTgTrOutCounter16 = _MccpRelcTgTrOutCounter16_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 18),
    _MccpRelcTgTrOutCounter16_Type()
)
mccpRelcTgTrOutCounter16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter16.setStatus("current")


class _MccpRelcTgTrOutCounter17_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter17_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter17_Object = MibTableColumn
mccpRelcTgTrOutCounter17 = _MccpRelcTgTrOutCounter17_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 19),
    _MccpRelcTgTrOutCounter17_Type()
)
mccpRelcTgTrOutCounter17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter17.setStatus("current")


class _MccpRelcTgTrOutCounter18_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter18_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter18_Object = MibTableColumn
mccpRelcTgTrOutCounter18 = _MccpRelcTgTrOutCounter18_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 20),
    _MccpRelcTgTrOutCounter18_Type()
)
mccpRelcTgTrOutCounter18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter18.setStatus("current")


class _MccpRelcTgTrOutCounter19_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter19_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter19_Object = MibTableColumn
mccpRelcTgTrOutCounter19 = _MccpRelcTgTrOutCounter19_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 21),
    _MccpRelcTgTrOutCounter19_Type()
)
mccpRelcTgTrOutCounter19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter19.setStatus("current")


class _MccpRelcTgTrOutCounter20_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter20_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter20_Object = MibTableColumn
mccpRelcTgTrOutCounter20 = _MccpRelcTgTrOutCounter20_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 22),
    _MccpRelcTgTrOutCounter20_Type()
)
mccpRelcTgTrOutCounter20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter20.setStatus("current")


class _MccpRelcTgTrOutCounter21_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter21_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter21_Object = MibTableColumn
mccpRelcTgTrOutCounter21 = _MccpRelcTgTrOutCounter21_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 23),
    _MccpRelcTgTrOutCounter21_Type()
)
mccpRelcTgTrOutCounter21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter21.setStatus("current")


class _MccpRelcTgTrOutCounter22_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter22_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter22_Object = MibTableColumn
mccpRelcTgTrOutCounter22 = _MccpRelcTgTrOutCounter22_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 24),
    _MccpRelcTgTrOutCounter22_Type()
)
mccpRelcTgTrOutCounter22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter22.setStatus("current")


class _MccpRelcTgTrOutCounter23_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter23_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter23_Object = MibTableColumn
mccpRelcTgTrOutCounter23 = _MccpRelcTgTrOutCounter23_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 25),
    _MccpRelcTgTrOutCounter23_Type()
)
mccpRelcTgTrOutCounter23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter23.setStatus("current")


class _MccpRelcTgTrOutCounter24_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter24_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter24_Object = MibTableColumn
mccpRelcTgTrOutCounter24 = _MccpRelcTgTrOutCounter24_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 26),
    _MccpRelcTgTrOutCounter24_Type()
)
mccpRelcTgTrOutCounter24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter24.setStatus("current")


class _MccpRelcTgTrOutCounter25_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter25_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter25_Object = MibTableColumn
mccpRelcTgTrOutCounter25 = _MccpRelcTgTrOutCounter25_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 27),
    _MccpRelcTgTrOutCounter25_Type()
)
mccpRelcTgTrOutCounter25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter25.setStatus("current")


class _MccpRelcTgTrOutCounter26_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter26 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter26_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter26_Object = MibTableColumn
mccpRelcTgTrOutCounter26 = _MccpRelcTgTrOutCounter26_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 28),
    _MccpRelcTgTrOutCounter26_Type()
)
mccpRelcTgTrOutCounter26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter26.setStatus("current")


class _MccpRelcTgTrOutCounter27_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter27 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter27_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter27_Object = MibTableColumn
mccpRelcTgTrOutCounter27 = _MccpRelcTgTrOutCounter27_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 29),
    _MccpRelcTgTrOutCounter27_Type()
)
mccpRelcTgTrOutCounter27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter27.setStatus("current")


class _MccpRelcTgTrOutCounter28_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter28 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter28_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter28_Object = MibTableColumn
mccpRelcTgTrOutCounter28 = _MccpRelcTgTrOutCounter28_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 30),
    _MccpRelcTgTrOutCounter28_Type()
)
mccpRelcTgTrOutCounter28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter28.setStatus("current")


class _MccpRelcTgTrOutCounter29_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter29 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter29_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter29_Object = MibTableColumn
mccpRelcTgTrOutCounter29 = _MccpRelcTgTrOutCounter29_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 31),
    _MccpRelcTgTrOutCounter29_Type()
)
mccpRelcTgTrOutCounter29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter29.setStatus("current")


class _MccpRelcTgTrOutCounter30_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter30 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter30_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter30_Object = MibTableColumn
mccpRelcTgTrOutCounter30 = _MccpRelcTgTrOutCounter30_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 32),
    _MccpRelcTgTrOutCounter30_Type()
)
mccpRelcTgTrOutCounter30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter30.setStatus("current")


class _MccpRelcTgTrOutCounter31_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter31 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter31_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter31_Object = MibTableColumn
mccpRelcTgTrOutCounter31 = _MccpRelcTgTrOutCounter31_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 33),
    _MccpRelcTgTrOutCounter31_Type()
)
mccpRelcTgTrOutCounter31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter31.setStatus("current")


class _MccpRelcTgTrOutCounter32_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter32_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter32_Object = MibTableColumn
mccpRelcTgTrOutCounter32 = _MccpRelcTgTrOutCounter32_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 34),
    _MccpRelcTgTrOutCounter32_Type()
)
mccpRelcTgTrOutCounter32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter32.setStatus("current")


class _MccpRelcTgTrOutCounter33_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter33 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter33_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter33_Object = MibTableColumn
mccpRelcTgTrOutCounter33 = _MccpRelcTgTrOutCounter33_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 35),
    _MccpRelcTgTrOutCounter33_Type()
)
mccpRelcTgTrOutCounter33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter33.setStatus("current")


class _MccpRelcTgTrOutCounter34_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter34 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter34_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter34_Object = MibTableColumn
mccpRelcTgTrOutCounter34 = _MccpRelcTgTrOutCounter34_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 36),
    _MccpRelcTgTrOutCounter34_Type()
)
mccpRelcTgTrOutCounter34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter34.setStatus("current")


class _MccpRelcTgTrOutCounter35_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter35 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter35_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter35_Object = MibTableColumn
mccpRelcTgTrOutCounter35 = _MccpRelcTgTrOutCounter35_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 37),
    _MccpRelcTgTrOutCounter35_Type()
)
mccpRelcTgTrOutCounter35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter35.setStatus("current")


class _MccpRelcTgTrOutCounter36_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter36 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter36_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter36_Object = MibTableColumn
mccpRelcTgTrOutCounter36 = _MccpRelcTgTrOutCounter36_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 38),
    _MccpRelcTgTrOutCounter36_Type()
)
mccpRelcTgTrOutCounter36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter36.setStatus("current")


class _MccpRelcTgTrOutCounter37_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter37 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter37_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter37_Object = MibTableColumn
mccpRelcTgTrOutCounter37 = _MccpRelcTgTrOutCounter37_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 39),
    _MccpRelcTgTrOutCounter37_Type()
)
mccpRelcTgTrOutCounter37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter37.setStatus("current")


class _MccpRelcTgTrOutCounter38_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter38 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter38_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter38_Object = MibTableColumn
mccpRelcTgTrOutCounter38 = _MccpRelcTgTrOutCounter38_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 40),
    _MccpRelcTgTrOutCounter38_Type()
)
mccpRelcTgTrOutCounter38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter38.setStatus("current")


class _MccpRelcTgTrOutCounter39_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter39 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter39_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter39_Object = MibTableColumn
mccpRelcTgTrOutCounter39 = _MccpRelcTgTrOutCounter39_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 41),
    _MccpRelcTgTrOutCounter39_Type()
)
mccpRelcTgTrOutCounter39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter39.setStatus("current")


class _MccpRelcTgTrOutCounter40_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter40 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter40_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter40_Object = MibTableColumn
mccpRelcTgTrOutCounter40 = _MccpRelcTgTrOutCounter40_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 42),
    _MccpRelcTgTrOutCounter40_Type()
)
mccpRelcTgTrOutCounter40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter40.setStatus("current")


class _MccpRelcTgTrOutCounter41_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter41 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter41_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter41_Object = MibTableColumn
mccpRelcTgTrOutCounter41 = _MccpRelcTgTrOutCounter41_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 43),
    _MccpRelcTgTrOutCounter41_Type()
)
mccpRelcTgTrOutCounter41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter41.setStatus("current")


class _MccpRelcTgTrOutCounter42_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter42 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter42_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter42_Object = MibTableColumn
mccpRelcTgTrOutCounter42 = _MccpRelcTgTrOutCounter42_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 44),
    _MccpRelcTgTrOutCounter42_Type()
)
mccpRelcTgTrOutCounter42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter42.setStatus("current")


class _MccpRelcTgTrOutCounter43_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter43 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter43_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter43_Object = MibTableColumn
mccpRelcTgTrOutCounter43 = _MccpRelcTgTrOutCounter43_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 45),
    _MccpRelcTgTrOutCounter43_Type()
)
mccpRelcTgTrOutCounter43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter43.setStatus("current")


class _MccpRelcTgTrOutCounter44_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter44 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter44_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter44_Object = MibTableColumn
mccpRelcTgTrOutCounter44 = _MccpRelcTgTrOutCounter44_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 46),
    _MccpRelcTgTrOutCounter44_Type()
)
mccpRelcTgTrOutCounter44.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter44.setStatus("current")


class _MccpRelcTgTrOutCounter45_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter45 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter45_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter45_Object = MibTableColumn
mccpRelcTgTrOutCounter45 = _MccpRelcTgTrOutCounter45_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 47),
    _MccpRelcTgTrOutCounter45_Type()
)
mccpRelcTgTrOutCounter45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter45.setStatus("current")


class _MccpRelcTgTrOutCounter46_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter46 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter46_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter46_Object = MibTableColumn
mccpRelcTgTrOutCounter46 = _MccpRelcTgTrOutCounter46_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 48),
    _MccpRelcTgTrOutCounter46_Type()
)
mccpRelcTgTrOutCounter46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter46.setStatus("current")


class _MccpRelcTgTrOutCounter47_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter47 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter47_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter47_Object = MibTableColumn
mccpRelcTgTrOutCounter47 = _MccpRelcTgTrOutCounter47_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 49),
    _MccpRelcTgTrOutCounter47_Type()
)
mccpRelcTgTrOutCounter47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter47.setStatus("current")


class _MccpRelcTgTrOutCounter48_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter48 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter48_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter48_Object = MibTableColumn
mccpRelcTgTrOutCounter48 = _MccpRelcTgTrOutCounter48_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 50),
    _MccpRelcTgTrOutCounter48_Type()
)
mccpRelcTgTrOutCounter48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter48.setStatus("current")


class _MccpRelcTgTrOutCounter49_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter49 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter49_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter49_Object = MibTableColumn
mccpRelcTgTrOutCounter49 = _MccpRelcTgTrOutCounter49_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 51),
    _MccpRelcTgTrOutCounter49_Type()
)
mccpRelcTgTrOutCounter49.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter49.setStatus("current")


class _MccpRelcTgTrOutCounter50_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter50 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter50_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter50_Object = MibTableColumn
mccpRelcTgTrOutCounter50 = _MccpRelcTgTrOutCounter50_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 52),
    _MccpRelcTgTrOutCounter50_Type()
)
mccpRelcTgTrOutCounter50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter50.setStatus("current")


class _MccpRelcTgTrOutCounter51_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter51 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter51_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter51_Object = MibTableColumn
mccpRelcTgTrOutCounter51 = _MccpRelcTgTrOutCounter51_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 53),
    _MccpRelcTgTrOutCounter51_Type()
)
mccpRelcTgTrOutCounter51.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter51.setStatus("current")


class _MccpRelcTgTrOutCounter52_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter52 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter52_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter52_Object = MibTableColumn
mccpRelcTgTrOutCounter52 = _MccpRelcTgTrOutCounter52_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 54),
    _MccpRelcTgTrOutCounter52_Type()
)
mccpRelcTgTrOutCounter52.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter52.setStatus("current")


class _MccpRelcTgTrOutCounter53_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter53 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter53_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter53_Object = MibTableColumn
mccpRelcTgTrOutCounter53 = _MccpRelcTgTrOutCounter53_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 55),
    _MccpRelcTgTrOutCounter53_Type()
)
mccpRelcTgTrOutCounter53.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter53.setStatus("current")


class _MccpRelcTgTrOutCounter54_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter54 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter54_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter54_Object = MibTableColumn
mccpRelcTgTrOutCounter54 = _MccpRelcTgTrOutCounter54_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 56),
    _MccpRelcTgTrOutCounter54_Type()
)
mccpRelcTgTrOutCounter54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter54.setStatus("current")


class _MccpRelcTgTrOutCounter55_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter55 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter55_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter55_Object = MibTableColumn
mccpRelcTgTrOutCounter55 = _MccpRelcTgTrOutCounter55_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 57),
    _MccpRelcTgTrOutCounter55_Type()
)
mccpRelcTgTrOutCounter55.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter55.setStatus("current")


class _MccpRelcTgTrOutCounter56_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter56 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter56_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter56_Object = MibTableColumn
mccpRelcTgTrOutCounter56 = _MccpRelcTgTrOutCounter56_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 58),
    _MccpRelcTgTrOutCounter56_Type()
)
mccpRelcTgTrOutCounter56.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter56.setStatus("current")


class _MccpRelcTgTrOutCounter57_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter57 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter57_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter57_Object = MibTableColumn
mccpRelcTgTrOutCounter57 = _MccpRelcTgTrOutCounter57_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 59),
    _MccpRelcTgTrOutCounter57_Type()
)
mccpRelcTgTrOutCounter57.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter57.setStatus("current")


class _MccpRelcTgTrOutCounter58_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter58 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter58_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter58_Object = MibTableColumn
mccpRelcTgTrOutCounter58 = _MccpRelcTgTrOutCounter58_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 60),
    _MccpRelcTgTrOutCounter58_Type()
)
mccpRelcTgTrOutCounter58.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter58.setStatus("current")


class _MccpRelcTgTrOutCounter59_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter59 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter59_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter59_Object = MibTableColumn
mccpRelcTgTrOutCounter59 = _MccpRelcTgTrOutCounter59_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 61),
    _MccpRelcTgTrOutCounter59_Type()
)
mccpRelcTgTrOutCounter59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter59.setStatus("current")


class _MccpRelcTgTrOutCounter60_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter60 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter60_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter60_Object = MibTableColumn
mccpRelcTgTrOutCounter60 = _MccpRelcTgTrOutCounter60_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 62),
    _MccpRelcTgTrOutCounter60_Type()
)
mccpRelcTgTrOutCounter60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter60.setStatus("current")


class _MccpRelcTgTrOutCounter61_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter61 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter61_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter61_Object = MibTableColumn
mccpRelcTgTrOutCounter61 = _MccpRelcTgTrOutCounter61_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 63),
    _MccpRelcTgTrOutCounter61_Type()
)
mccpRelcTgTrOutCounter61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter61.setStatus("current")


class _MccpRelcTgTrOutCounter62_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter62 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter62_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter62_Object = MibTableColumn
mccpRelcTgTrOutCounter62 = _MccpRelcTgTrOutCounter62_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 64),
    _MccpRelcTgTrOutCounter62_Type()
)
mccpRelcTgTrOutCounter62.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter62.setStatus("current")


class _MccpRelcTgTrOutCounter63_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter63 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter63_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter63_Object = MibTableColumn
mccpRelcTgTrOutCounter63 = _MccpRelcTgTrOutCounter63_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 65),
    _MccpRelcTgTrOutCounter63_Type()
)
mccpRelcTgTrOutCounter63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter63.setStatus("current")


class _MccpRelcTgTrOutCounter64_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter64 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter64_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter64_Object = MibTableColumn
mccpRelcTgTrOutCounter64 = _MccpRelcTgTrOutCounter64_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 66),
    _MccpRelcTgTrOutCounter64_Type()
)
mccpRelcTgTrOutCounter64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter64.setStatus("current")


class _MccpRelcTgTrOutCounter65_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter65 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter65_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter65_Object = MibTableColumn
mccpRelcTgTrOutCounter65 = _MccpRelcTgTrOutCounter65_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 67),
    _MccpRelcTgTrOutCounter65_Type()
)
mccpRelcTgTrOutCounter65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter65.setStatus("current")


class _MccpRelcTgTrOutCounter66_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter66 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter66_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter66_Object = MibTableColumn
mccpRelcTgTrOutCounter66 = _MccpRelcTgTrOutCounter66_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 68),
    _MccpRelcTgTrOutCounter66_Type()
)
mccpRelcTgTrOutCounter66.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter66.setStatus("current")


class _MccpRelcTgTrOutCounter67_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter67 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter67_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter67_Object = MibTableColumn
mccpRelcTgTrOutCounter67 = _MccpRelcTgTrOutCounter67_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 69),
    _MccpRelcTgTrOutCounter67_Type()
)
mccpRelcTgTrOutCounter67.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter67.setStatus("current")


class _MccpRelcTgTrOutCounter68_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter68 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter68_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter68_Object = MibTableColumn
mccpRelcTgTrOutCounter68 = _MccpRelcTgTrOutCounter68_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 70),
    _MccpRelcTgTrOutCounter68_Type()
)
mccpRelcTgTrOutCounter68.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter68.setStatus("current")


class _MccpRelcTgTrOutCounter69_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter69 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter69_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter69_Object = MibTableColumn
mccpRelcTgTrOutCounter69 = _MccpRelcTgTrOutCounter69_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 71),
    _MccpRelcTgTrOutCounter69_Type()
)
mccpRelcTgTrOutCounter69.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter69.setStatus("current")


class _MccpRelcTgTrOutCounter70_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter70 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter70_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter70_Object = MibTableColumn
mccpRelcTgTrOutCounter70 = _MccpRelcTgTrOutCounter70_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 72),
    _MccpRelcTgTrOutCounter70_Type()
)
mccpRelcTgTrOutCounter70.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter70.setStatus("current")


class _MccpRelcTgTrOutCounter71_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter71 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter71_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter71_Object = MibTableColumn
mccpRelcTgTrOutCounter71 = _MccpRelcTgTrOutCounter71_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 73),
    _MccpRelcTgTrOutCounter71_Type()
)
mccpRelcTgTrOutCounter71.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter71.setStatus("current")


class _MccpRelcTgTrOutCounter72_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter72 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter72_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter72_Object = MibTableColumn
mccpRelcTgTrOutCounter72 = _MccpRelcTgTrOutCounter72_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 74),
    _MccpRelcTgTrOutCounter72_Type()
)
mccpRelcTgTrOutCounter72.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter72.setStatus("current")


class _MccpRelcTgTrOutCounter73_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter73 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter73_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter73_Object = MibTableColumn
mccpRelcTgTrOutCounter73 = _MccpRelcTgTrOutCounter73_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 75),
    _MccpRelcTgTrOutCounter73_Type()
)
mccpRelcTgTrOutCounter73.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter73.setStatus("current")


class _MccpRelcTgTrOutCounter74_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter74 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter74_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter74_Object = MibTableColumn
mccpRelcTgTrOutCounter74 = _MccpRelcTgTrOutCounter74_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 76),
    _MccpRelcTgTrOutCounter74_Type()
)
mccpRelcTgTrOutCounter74.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter74.setStatus("current")


class _MccpRelcTgTrOutCounter75_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter75 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter75_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter75_Object = MibTableColumn
mccpRelcTgTrOutCounter75 = _MccpRelcTgTrOutCounter75_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 77),
    _MccpRelcTgTrOutCounter75_Type()
)
mccpRelcTgTrOutCounter75.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter75.setStatus("current")


class _MccpRelcTgTrOutCounter76_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter76 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter76_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter76_Object = MibTableColumn
mccpRelcTgTrOutCounter76 = _MccpRelcTgTrOutCounter76_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 78),
    _MccpRelcTgTrOutCounter76_Type()
)
mccpRelcTgTrOutCounter76.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter76.setStatus("current")


class _MccpRelcTgTrOutCounter77_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter77 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter77_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter77_Object = MibTableColumn
mccpRelcTgTrOutCounter77 = _MccpRelcTgTrOutCounter77_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 79),
    _MccpRelcTgTrOutCounter77_Type()
)
mccpRelcTgTrOutCounter77.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter77.setStatus("current")


class _MccpRelcTgTrOutCounter78_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter78 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter78_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter78_Object = MibTableColumn
mccpRelcTgTrOutCounter78 = _MccpRelcTgTrOutCounter78_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 80),
    _MccpRelcTgTrOutCounter78_Type()
)
mccpRelcTgTrOutCounter78.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter78.setStatus("current")


class _MccpRelcTgTrOutCounter79_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter79 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter79_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter79_Object = MibTableColumn
mccpRelcTgTrOutCounter79 = _MccpRelcTgTrOutCounter79_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 81),
    _MccpRelcTgTrOutCounter79_Type()
)
mccpRelcTgTrOutCounter79.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter79.setStatus("current")


class _MccpRelcTgTrOutCounter80_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter80 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter80_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter80_Object = MibTableColumn
mccpRelcTgTrOutCounter80 = _MccpRelcTgTrOutCounter80_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 82),
    _MccpRelcTgTrOutCounter80_Type()
)
mccpRelcTgTrOutCounter80.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter80.setStatus("current")


class _MccpRelcTgTrOutCounter81_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter81 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter81_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter81_Object = MibTableColumn
mccpRelcTgTrOutCounter81 = _MccpRelcTgTrOutCounter81_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 83),
    _MccpRelcTgTrOutCounter81_Type()
)
mccpRelcTgTrOutCounter81.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter81.setStatus("current")


class _MccpRelcTgTrOutCounter82_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter82_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter82_Object = MibTableColumn
mccpRelcTgTrOutCounter82 = _MccpRelcTgTrOutCounter82_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 84),
    _MccpRelcTgTrOutCounter82_Type()
)
mccpRelcTgTrOutCounter82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter82.setStatus("current")


class _MccpRelcTgTrOutCounter83_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter83 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter83_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter83_Object = MibTableColumn
mccpRelcTgTrOutCounter83 = _MccpRelcTgTrOutCounter83_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 85),
    _MccpRelcTgTrOutCounter83_Type()
)
mccpRelcTgTrOutCounter83.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter83.setStatus("current")


class _MccpRelcTgTrOutCounter84_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter84 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter84_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter84_Object = MibTableColumn
mccpRelcTgTrOutCounter84 = _MccpRelcTgTrOutCounter84_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 86),
    _MccpRelcTgTrOutCounter84_Type()
)
mccpRelcTgTrOutCounter84.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter84.setStatus("current")


class _MccpRelcTgTrOutCounter85_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter85 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter85_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter85_Object = MibTableColumn
mccpRelcTgTrOutCounter85 = _MccpRelcTgTrOutCounter85_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 87),
    _MccpRelcTgTrOutCounter85_Type()
)
mccpRelcTgTrOutCounter85.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter85.setStatus("current")


class _MccpRelcTgTrOutCounter86_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter86 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter86_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter86_Object = MibTableColumn
mccpRelcTgTrOutCounter86 = _MccpRelcTgTrOutCounter86_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 88),
    _MccpRelcTgTrOutCounter86_Type()
)
mccpRelcTgTrOutCounter86.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter86.setStatus("current")


class _MccpRelcTgTrOutCounter87_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter87 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter87_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter87_Object = MibTableColumn
mccpRelcTgTrOutCounter87 = _MccpRelcTgTrOutCounter87_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 89),
    _MccpRelcTgTrOutCounter87_Type()
)
mccpRelcTgTrOutCounter87.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter87.setStatus("current")


class _MccpRelcTgTrOutCounter88_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter88 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter88_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter88_Object = MibTableColumn
mccpRelcTgTrOutCounter88 = _MccpRelcTgTrOutCounter88_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 90),
    _MccpRelcTgTrOutCounter88_Type()
)
mccpRelcTgTrOutCounter88.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter88.setStatus("current")


class _MccpRelcTgTrOutCounter89_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter89 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter89_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter89_Object = MibTableColumn
mccpRelcTgTrOutCounter89 = _MccpRelcTgTrOutCounter89_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 91),
    _MccpRelcTgTrOutCounter89_Type()
)
mccpRelcTgTrOutCounter89.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter89.setStatus("current")


class _MccpRelcTgTrOutCounter90_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter90 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter90_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter90_Object = MibTableColumn
mccpRelcTgTrOutCounter90 = _MccpRelcTgTrOutCounter90_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 92),
    _MccpRelcTgTrOutCounter90_Type()
)
mccpRelcTgTrOutCounter90.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter90.setStatus("current")


class _MccpRelcTgTrOutCounter91_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter91 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter91_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter91_Object = MibTableColumn
mccpRelcTgTrOutCounter91 = _MccpRelcTgTrOutCounter91_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 93),
    _MccpRelcTgTrOutCounter91_Type()
)
mccpRelcTgTrOutCounter91.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter91.setStatus("current")


class _MccpRelcTgTrOutCounter92_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter92 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter92_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter92_Object = MibTableColumn
mccpRelcTgTrOutCounter92 = _MccpRelcTgTrOutCounter92_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 94),
    _MccpRelcTgTrOutCounter92_Type()
)
mccpRelcTgTrOutCounter92.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter92.setStatus("current")


class _MccpRelcTgTrOutCounter93_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter93 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter93_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter93_Object = MibTableColumn
mccpRelcTgTrOutCounter93 = _MccpRelcTgTrOutCounter93_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 95),
    _MccpRelcTgTrOutCounter93_Type()
)
mccpRelcTgTrOutCounter93.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter93.setStatus("current")


class _MccpRelcTgTrOutCounter94_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter94 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter94_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter94_Object = MibTableColumn
mccpRelcTgTrOutCounter94 = _MccpRelcTgTrOutCounter94_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 96),
    _MccpRelcTgTrOutCounter94_Type()
)
mccpRelcTgTrOutCounter94.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter94.setStatus("current")


class _MccpRelcTgTrOutCounter95_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter95 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter95_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter95_Object = MibTableColumn
mccpRelcTgTrOutCounter95 = _MccpRelcTgTrOutCounter95_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 97),
    _MccpRelcTgTrOutCounter95_Type()
)
mccpRelcTgTrOutCounter95.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter95.setStatus("current")


class _MccpRelcTgTrOutCounter96_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter96 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter96_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter96_Object = MibTableColumn
mccpRelcTgTrOutCounter96 = _MccpRelcTgTrOutCounter96_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 98),
    _MccpRelcTgTrOutCounter96_Type()
)
mccpRelcTgTrOutCounter96.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter96.setStatus("current")


class _MccpRelcTgTrOutCounter97_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter97 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter97_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter97_Object = MibTableColumn
mccpRelcTgTrOutCounter97 = _MccpRelcTgTrOutCounter97_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 99),
    _MccpRelcTgTrOutCounter97_Type()
)
mccpRelcTgTrOutCounter97.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter97.setStatus("current")


class _MccpRelcTgTrOutCounter98_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter98 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter98_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter98_Object = MibTableColumn
mccpRelcTgTrOutCounter98 = _MccpRelcTgTrOutCounter98_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 100),
    _MccpRelcTgTrOutCounter98_Type()
)
mccpRelcTgTrOutCounter98.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter98.setStatus("current")


class _MccpRelcTgTrOutCounter99_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter99 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter99_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter99_Object = MibTableColumn
mccpRelcTgTrOutCounter99 = _MccpRelcTgTrOutCounter99_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 101),
    _MccpRelcTgTrOutCounter99_Type()
)
mccpRelcTgTrOutCounter99.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter99.setStatus("current")


class _MccpRelcTgTrOutCounter100_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter100 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter100_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter100_Object = MibTableColumn
mccpRelcTgTrOutCounter100 = _MccpRelcTgTrOutCounter100_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 102),
    _MccpRelcTgTrOutCounter100_Type()
)
mccpRelcTgTrOutCounter100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter100.setStatus("current")


class _MccpRelcTgTrOutCounter101_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter101 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter101_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter101_Object = MibTableColumn
mccpRelcTgTrOutCounter101 = _MccpRelcTgTrOutCounter101_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 103),
    _MccpRelcTgTrOutCounter101_Type()
)
mccpRelcTgTrOutCounter101.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter101.setStatus("current")


class _MccpRelcTgTrOutCounter102_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter102 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter102_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter102_Object = MibTableColumn
mccpRelcTgTrOutCounter102 = _MccpRelcTgTrOutCounter102_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 104),
    _MccpRelcTgTrOutCounter102_Type()
)
mccpRelcTgTrOutCounter102.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter102.setStatus("current")


class _MccpRelcTgTrOutCounter103_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter103 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter103_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter103_Object = MibTableColumn
mccpRelcTgTrOutCounter103 = _MccpRelcTgTrOutCounter103_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 105),
    _MccpRelcTgTrOutCounter103_Type()
)
mccpRelcTgTrOutCounter103.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter103.setStatus("current")


class _MccpRelcTgTrOutCounter104_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter104 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter104_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter104_Object = MibTableColumn
mccpRelcTgTrOutCounter104 = _MccpRelcTgTrOutCounter104_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 106),
    _MccpRelcTgTrOutCounter104_Type()
)
mccpRelcTgTrOutCounter104.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter104.setStatus("current")


class _MccpRelcTgTrOutCounter105_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter105 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter105_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter105_Object = MibTableColumn
mccpRelcTgTrOutCounter105 = _MccpRelcTgTrOutCounter105_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 107),
    _MccpRelcTgTrOutCounter105_Type()
)
mccpRelcTgTrOutCounter105.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter105.setStatus("current")


class _MccpRelcTgTrOutCounter106_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter106 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter106_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter106_Object = MibTableColumn
mccpRelcTgTrOutCounter106 = _MccpRelcTgTrOutCounter106_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 108),
    _MccpRelcTgTrOutCounter106_Type()
)
mccpRelcTgTrOutCounter106.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter106.setStatus("current")


class _MccpRelcTgTrOutCounter107_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter107 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter107_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter107_Object = MibTableColumn
mccpRelcTgTrOutCounter107 = _MccpRelcTgTrOutCounter107_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 109),
    _MccpRelcTgTrOutCounter107_Type()
)
mccpRelcTgTrOutCounter107.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter107.setStatus("current")


class _MccpRelcTgTrOutCounter108_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter108 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter108_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter108_Object = MibTableColumn
mccpRelcTgTrOutCounter108 = _MccpRelcTgTrOutCounter108_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 110),
    _MccpRelcTgTrOutCounter108_Type()
)
mccpRelcTgTrOutCounter108.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter108.setStatus("current")


class _MccpRelcTgTrOutCounter109_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter109 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter109_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter109_Object = MibTableColumn
mccpRelcTgTrOutCounter109 = _MccpRelcTgTrOutCounter109_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 111),
    _MccpRelcTgTrOutCounter109_Type()
)
mccpRelcTgTrOutCounter109.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter109.setStatus("current")


class _MccpRelcTgTrOutCounter110_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter110 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter110_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter110_Object = MibTableColumn
mccpRelcTgTrOutCounter110 = _MccpRelcTgTrOutCounter110_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 112),
    _MccpRelcTgTrOutCounter110_Type()
)
mccpRelcTgTrOutCounter110.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter110.setStatus("current")


class _MccpRelcTgTrOutCounter111_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter111 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter111_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter111_Object = MibTableColumn
mccpRelcTgTrOutCounter111 = _MccpRelcTgTrOutCounter111_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 113),
    _MccpRelcTgTrOutCounter111_Type()
)
mccpRelcTgTrOutCounter111.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter111.setStatus("current")


class _MccpRelcTgTrOutCounter112_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter112 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter112_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter112_Object = MibTableColumn
mccpRelcTgTrOutCounter112 = _MccpRelcTgTrOutCounter112_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 114),
    _MccpRelcTgTrOutCounter112_Type()
)
mccpRelcTgTrOutCounter112.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter112.setStatus("current")


class _MccpRelcTgTrOutCounter113_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter113 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter113_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter113_Object = MibTableColumn
mccpRelcTgTrOutCounter113 = _MccpRelcTgTrOutCounter113_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 115),
    _MccpRelcTgTrOutCounter113_Type()
)
mccpRelcTgTrOutCounter113.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter113.setStatus("current")


class _MccpRelcTgTrOutCounter114_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter114 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter114_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter114_Object = MibTableColumn
mccpRelcTgTrOutCounter114 = _MccpRelcTgTrOutCounter114_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 116),
    _MccpRelcTgTrOutCounter114_Type()
)
mccpRelcTgTrOutCounter114.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter114.setStatus("current")


class _MccpRelcTgTrOutCounter115_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter115 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter115_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter115_Object = MibTableColumn
mccpRelcTgTrOutCounter115 = _MccpRelcTgTrOutCounter115_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 117),
    _MccpRelcTgTrOutCounter115_Type()
)
mccpRelcTgTrOutCounter115.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter115.setStatus("current")


class _MccpRelcTgTrOutCounter116_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter116 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter116_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter116_Object = MibTableColumn
mccpRelcTgTrOutCounter116 = _MccpRelcTgTrOutCounter116_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 118),
    _MccpRelcTgTrOutCounter116_Type()
)
mccpRelcTgTrOutCounter116.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter116.setStatus("current")


class _MccpRelcTgTrOutCounter117_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter117 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter117_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter117_Object = MibTableColumn
mccpRelcTgTrOutCounter117 = _MccpRelcTgTrOutCounter117_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 119),
    _MccpRelcTgTrOutCounter117_Type()
)
mccpRelcTgTrOutCounter117.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter117.setStatus("current")


class _MccpRelcTgTrOutCounter118_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter118 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter118_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter118_Object = MibTableColumn
mccpRelcTgTrOutCounter118 = _MccpRelcTgTrOutCounter118_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 120),
    _MccpRelcTgTrOutCounter118_Type()
)
mccpRelcTgTrOutCounter118.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter118.setStatus("current")


class _MccpRelcTgTrOutCounter119_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter119 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter119_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter119_Object = MibTableColumn
mccpRelcTgTrOutCounter119 = _MccpRelcTgTrOutCounter119_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 121),
    _MccpRelcTgTrOutCounter119_Type()
)
mccpRelcTgTrOutCounter119.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter119.setStatus("current")


class _MccpRelcTgTrOutCounter120_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter120 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter120_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter120_Object = MibTableColumn
mccpRelcTgTrOutCounter120 = _MccpRelcTgTrOutCounter120_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 122),
    _MccpRelcTgTrOutCounter120_Type()
)
mccpRelcTgTrOutCounter120.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter120.setStatus("current")


class _MccpRelcTgTrOutCounter121_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter121 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter121_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter121_Object = MibTableColumn
mccpRelcTgTrOutCounter121 = _MccpRelcTgTrOutCounter121_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 123),
    _MccpRelcTgTrOutCounter121_Type()
)
mccpRelcTgTrOutCounter121.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter121.setStatus("current")


class _MccpRelcTgTrOutCounter122_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter122 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter122_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter122_Object = MibTableColumn
mccpRelcTgTrOutCounter122 = _MccpRelcTgTrOutCounter122_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 124),
    _MccpRelcTgTrOutCounter122_Type()
)
mccpRelcTgTrOutCounter122.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter122.setStatus("current")


class _MccpRelcTgTrOutCounter123_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter123 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter123_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter123_Object = MibTableColumn
mccpRelcTgTrOutCounter123 = _MccpRelcTgTrOutCounter123_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 125),
    _MccpRelcTgTrOutCounter123_Type()
)
mccpRelcTgTrOutCounter123.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter123.setStatus("current")


class _MccpRelcTgTrOutCounter124_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter124 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter124_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter124_Object = MibTableColumn
mccpRelcTgTrOutCounter124 = _MccpRelcTgTrOutCounter124_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 126),
    _MccpRelcTgTrOutCounter124_Type()
)
mccpRelcTgTrOutCounter124.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter124.setStatus("current")


class _MccpRelcTgTrOutCounter125_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter125 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter125_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter125_Object = MibTableColumn
mccpRelcTgTrOutCounter125 = _MccpRelcTgTrOutCounter125_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 127),
    _MccpRelcTgTrOutCounter125_Type()
)
mccpRelcTgTrOutCounter125.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter125.setStatus("current")


class _MccpRelcTgTrOutCounter126_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter126 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter126_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter126_Object = MibTableColumn
mccpRelcTgTrOutCounter126 = _MccpRelcTgTrOutCounter126_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 128),
    _MccpRelcTgTrOutCounter126_Type()
)
mccpRelcTgTrOutCounter126.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter126.setStatus("current")


class _MccpRelcTgTrOutCounter127_Type(Integer32):
    """Custom type mccpRelcTgTrOutCounter127 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcTgTrOutCounter127_Type.__name__ = "Integer32"
_MccpRelcTgTrOutCounter127_Object = MibTableColumn
mccpRelcTgTrOutCounter127 = _MccpRelcTgTrOutCounter127_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 29, 1, 129),
    _MccpRelcTgTrOutCounter127_Type()
)
mccpRelcTgTrOutCounter127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcTgTrOutCounter127.setStatus("current")
_MccpRelcPlanInTable_Object = MibTable
mccpRelcPlanInTable = _MccpRelcPlanInTable_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30)
)
if mibBuilder.loadTexts:
    mccpRelcPlanInTable.setStatus("current")
_MccpRelcPlanInEntry_Object = MibTableRow
mccpRelcPlanInEntry = _MccpRelcPlanInEntry_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1)
)
mccpRelcPlanInEntry.setIndexNames(
    (0, "ELTEX-MCCP", "mccpRelcPlanInIndex"),
)
if mibBuilder.loadTexts:
    mccpRelcPlanInEntry.setStatus("current")


class _MccpRelcPlanInIndex_Type(Integer32):
    """Custom type mccpRelcPlanInIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MccpRelcPlanInIndex_Type.__name__ = "Integer32"
_MccpRelcPlanInIndex_Object = MibTableColumn
mccpRelcPlanInIndex = _MccpRelcPlanInIndex_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 1),
    _MccpRelcPlanInIndex_Type()
)
mccpRelcPlanInIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mccpRelcPlanInIndex.setStatus("current")


class _MccpRelcPlanInCounter0_Type(Integer32):
    """Custom type mccpRelcPlanInCounter0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter0_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter0_Object = MibTableColumn
mccpRelcPlanInCounter0 = _MccpRelcPlanInCounter0_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 2),
    _MccpRelcPlanInCounter0_Type()
)
mccpRelcPlanInCounter0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter0.setStatus("current")


class _MccpRelcPlanInCounter1_Type(Integer32):
    """Custom type mccpRelcPlanInCounter1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter1_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter1_Object = MibTableColumn
mccpRelcPlanInCounter1 = _MccpRelcPlanInCounter1_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 3),
    _MccpRelcPlanInCounter1_Type()
)
mccpRelcPlanInCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter1.setStatus("current")


class _MccpRelcPlanInCounter2_Type(Integer32):
    """Custom type mccpRelcPlanInCounter2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter2_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter2_Object = MibTableColumn
mccpRelcPlanInCounter2 = _MccpRelcPlanInCounter2_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 4),
    _MccpRelcPlanInCounter2_Type()
)
mccpRelcPlanInCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter2.setStatus("current")


class _MccpRelcPlanInCounter3_Type(Integer32):
    """Custom type mccpRelcPlanInCounter3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter3_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter3_Object = MibTableColumn
mccpRelcPlanInCounter3 = _MccpRelcPlanInCounter3_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 5),
    _MccpRelcPlanInCounter3_Type()
)
mccpRelcPlanInCounter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter3.setStatus("current")


class _MccpRelcPlanInCounter4_Type(Integer32):
    """Custom type mccpRelcPlanInCounter4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter4_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter4_Object = MibTableColumn
mccpRelcPlanInCounter4 = _MccpRelcPlanInCounter4_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 6),
    _MccpRelcPlanInCounter4_Type()
)
mccpRelcPlanInCounter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter4.setStatus("current")


class _MccpRelcPlanInCounter5_Type(Integer32):
    """Custom type mccpRelcPlanInCounter5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter5_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter5_Object = MibTableColumn
mccpRelcPlanInCounter5 = _MccpRelcPlanInCounter5_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 7),
    _MccpRelcPlanInCounter5_Type()
)
mccpRelcPlanInCounter5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter5.setStatus("current")


class _MccpRelcPlanInCounter6_Type(Integer32):
    """Custom type mccpRelcPlanInCounter6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter6_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter6_Object = MibTableColumn
mccpRelcPlanInCounter6 = _MccpRelcPlanInCounter6_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 8),
    _MccpRelcPlanInCounter6_Type()
)
mccpRelcPlanInCounter6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter6.setStatus("current")


class _MccpRelcPlanInCounter7_Type(Integer32):
    """Custom type mccpRelcPlanInCounter7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter7_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter7_Object = MibTableColumn
mccpRelcPlanInCounter7 = _MccpRelcPlanInCounter7_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 9),
    _MccpRelcPlanInCounter7_Type()
)
mccpRelcPlanInCounter7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter7.setStatus("current")


class _MccpRelcPlanInCounter8_Type(Integer32):
    """Custom type mccpRelcPlanInCounter8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter8_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter8_Object = MibTableColumn
mccpRelcPlanInCounter8 = _MccpRelcPlanInCounter8_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 10),
    _MccpRelcPlanInCounter8_Type()
)
mccpRelcPlanInCounter8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter8.setStatus("current")


class _MccpRelcPlanInCounter9_Type(Integer32):
    """Custom type mccpRelcPlanInCounter9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter9_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter9_Object = MibTableColumn
mccpRelcPlanInCounter9 = _MccpRelcPlanInCounter9_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 11),
    _MccpRelcPlanInCounter9_Type()
)
mccpRelcPlanInCounter9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter9.setStatus("current")


class _MccpRelcPlanInCounter10_Type(Integer32):
    """Custom type mccpRelcPlanInCounter10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter10_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter10_Object = MibTableColumn
mccpRelcPlanInCounter10 = _MccpRelcPlanInCounter10_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 12),
    _MccpRelcPlanInCounter10_Type()
)
mccpRelcPlanInCounter10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter10.setStatus("current")


class _MccpRelcPlanInCounter11_Type(Integer32):
    """Custom type mccpRelcPlanInCounter11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter11_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter11_Object = MibTableColumn
mccpRelcPlanInCounter11 = _MccpRelcPlanInCounter11_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 13),
    _MccpRelcPlanInCounter11_Type()
)
mccpRelcPlanInCounter11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter11.setStatus("current")


class _MccpRelcPlanInCounter12_Type(Integer32):
    """Custom type mccpRelcPlanInCounter12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter12_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter12_Object = MibTableColumn
mccpRelcPlanInCounter12 = _MccpRelcPlanInCounter12_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 14),
    _MccpRelcPlanInCounter12_Type()
)
mccpRelcPlanInCounter12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter12.setStatus("current")


class _MccpRelcPlanInCounter13_Type(Integer32):
    """Custom type mccpRelcPlanInCounter13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter13_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter13_Object = MibTableColumn
mccpRelcPlanInCounter13 = _MccpRelcPlanInCounter13_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 15),
    _MccpRelcPlanInCounter13_Type()
)
mccpRelcPlanInCounter13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter13.setStatus("current")


class _MccpRelcPlanInCounter14_Type(Integer32):
    """Custom type mccpRelcPlanInCounter14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter14_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter14_Object = MibTableColumn
mccpRelcPlanInCounter14 = _MccpRelcPlanInCounter14_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 16),
    _MccpRelcPlanInCounter14_Type()
)
mccpRelcPlanInCounter14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter14.setStatus("current")


class _MccpRelcPlanInCounter15_Type(Integer32):
    """Custom type mccpRelcPlanInCounter15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter15_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter15_Object = MibTableColumn
mccpRelcPlanInCounter15 = _MccpRelcPlanInCounter15_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 17),
    _MccpRelcPlanInCounter15_Type()
)
mccpRelcPlanInCounter15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter15.setStatus("current")


class _MccpRelcPlanInCounter16_Type(Integer32):
    """Custom type mccpRelcPlanInCounter16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter16_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter16_Object = MibTableColumn
mccpRelcPlanInCounter16 = _MccpRelcPlanInCounter16_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 18),
    _MccpRelcPlanInCounter16_Type()
)
mccpRelcPlanInCounter16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter16.setStatus("current")


class _MccpRelcPlanInCounter17_Type(Integer32):
    """Custom type mccpRelcPlanInCounter17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter17_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter17_Object = MibTableColumn
mccpRelcPlanInCounter17 = _MccpRelcPlanInCounter17_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 19),
    _MccpRelcPlanInCounter17_Type()
)
mccpRelcPlanInCounter17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter17.setStatus("current")


class _MccpRelcPlanInCounter18_Type(Integer32):
    """Custom type mccpRelcPlanInCounter18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter18_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter18_Object = MibTableColumn
mccpRelcPlanInCounter18 = _MccpRelcPlanInCounter18_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 20),
    _MccpRelcPlanInCounter18_Type()
)
mccpRelcPlanInCounter18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter18.setStatus("current")


class _MccpRelcPlanInCounter19_Type(Integer32):
    """Custom type mccpRelcPlanInCounter19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter19_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter19_Object = MibTableColumn
mccpRelcPlanInCounter19 = _MccpRelcPlanInCounter19_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 21),
    _MccpRelcPlanInCounter19_Type()
)
mccpRelcPlanInCounter19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter19.setStatus("current")


class _MccpRelcPlanInCounter20_Type(Integer32):
    """Custom type mccpRelcPlanInCounter20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter20_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter20_Object = MibTableColumn
mccpRelcPlanInCounter20 = _MccpRelcPlanInCounter20_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 22),
    _MccpRelcPlanInCounter20_Type()
)
mccpRelcPlanInCounter20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter20.setStatus("current")


class _MccpRelcPlanInCounter21_Type(Integer32):
    """Custom type mccpRelcPlanInCounter21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter21_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter21_Object = MibTableColumn
mccpRelcPlanInCounter21 = _MccpRelcPlanInCounter21_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 23),
    _MccpRelcPlanInCounter21_Type()
)
mccpRelcPlanInCounter21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter21.setStatus("current")


class _MccpRelcPlanInCounter22_Type(Integer32):
    """Custom type mccpRelcPlanInCounter22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter22_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter22_Object = MibTableColumn
mccpRelcPlanInCounter22 = _MccpRelcPlanInCounter22_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 24),
    _MccpRelcPlanInCounter22_Type()
)
mccpRelcPlanInCounter22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter22.setStatus("current")


class _MccpRelcPlanInCounter23_Type(Integer32):
    """Custom type mccpRelcPlanInCounter23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter23_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter23_Object = MibTableColumn
mccpRelcPlanInCounter23 = _MccpRelcPlanInCounter23_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 25),
    _MccpRelcPlanInCounter23_Type()
)
mccpRelcPlanInCounter23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter23.setStatus("current")


class _MccpRelcPlanInCounter24_Type(Integer32):
    """Custom type mccpRelcPlanInCounter24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter24_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter24_Object = MibTableColumn
mccpRelcPlanInCounter24 = _MccpRelcPlanInCounter24_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 26),
    _MccpRelcPlanInCounter24_Type()
)
mccpRelcPlanInCounter24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter24.setStatus("current")


class _MccpRelcPlanInCounter25_Type(Integer32):
    """Custom type mccpRelcPlanInCounter25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter25_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter25_Object = MibTableColumn
mccpRelcPlanInCounter25 = _MccpRelcPlanInCounter25_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 27),
    _MccpRelcPlanInCounter25_Type()
)
mccpRelcPlanInCounter25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter25.setStatus("current")


class _MccpRelcPlanInCounter26_Type(Integer32):
    """Custom type mccpRelcPlanInCounter26 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter26_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter26_Object = MibTableColumn
mccpRelcPlanInCounter26 = _MccpRelcPlanInCounter26_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 28),
    _MccpRelcPlanInCounter26_Type()
)
mccpRelcPlanInCounter26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter26.setStatus("current")


class _MccpRelcPlanInCounter27_Type(Integer32):
    """Custom type mccpRelcPlanInCounter27 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter27_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter27_Object = MibTableColumn
mccpRelcPlanInCounter27 = _MccpRelcPlanInCounter27_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 29),
    _MccpRelcPlanInCounter27_Type()
)
mccpRelcPlanInCounter27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter27.setStatus("current")


class _MccpRelcPlanInCounter28_Type(Integer32):
    """Custom type mccpRelcPlanInCounter28 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter28_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter28_Object = MibTableColumn
mccpRelcPlanInCounter28 = _MccpRelcPlanInCounter28_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 30),
    _MccpRelcPlanInCounter28_Type()
)
mccpRelcPlanInCounter28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter28.setStatus("current")


class _MccpRelcPlanInCounter29_Type(Integer32):
    """Custom type mccpRelcPlanInCounter29 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter29_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter29_Object = MibTableColumn
mccpRelcPlanInCounter29 = _MccpRelcPlanInCounter29_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 31),
    _MccpRelcPlanInCounter29_Type()
)
mccpRelcPlanInCounter29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter29.setStatus("current")


class _MccpRelcPlanInCounter30_Type(Integer32):
    """Custom type mccpRelcPlanInCounter30 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter30_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter30_Object = MibTableColumn
mccpRelcPlanInCounter30 = _MccpRelcPlanInCounter30_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 32),
    _MccpRelcPlanInCounter30_Type()
)
mccpRelcPlanInCounter30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter30.setStatus("current")


class _MccpRelcPlanInCounter31_Type(Integer32):
    """Custom type mccpRelcPlanInCounter31 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter31_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter31_Object = MibTableColumn
mccpRelcPlanInCounter31 = _MccpRelcPlanInCounter31_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 33),
    _MccpRelcPlanInCounter31_Type()
)
mccpRelcPlanInCounter31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter31.setStatus("current")


class _MccpRelcPlanInCounter32_Type(Integer32):
    """Custom type mccpRelcPlanInCounter32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter32_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter32_Object = MibTableColumn
mccpRelcPlanInCounter32 = _MccpRelcPlanInCounter32_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 34),
    _MccpRelcPlanInCounter32_Type()
)
mccpRelcPlanInCounter32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter32.setStatus("current")


class _MccpRelcPlanInCounter33_Type(Integer32):
    """Custom type mccpRelcPlanInCounter33 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter33_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter33_Object = MibTableColumn
mccpRelcPlanInCounter33 = _MccpRelcPlanInCounter33_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 35),
    _MccpRelcPlanInCounter33_Type()
)
mccpRelcPlanInCounter33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter33.setStatus("current")


class _MccpRelcPlanInCounter34_Type(Integer32):
    """Custom type mccpRelcPlanInCounter34 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter34_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter34_Object = MibTableColumn
mccpRelcPlanInCounter34 = _MccpRelcPlanInCounter34_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 36),
    _MccpRelcPlanInCounter34_Type()
)
mccpRelcPlanInCounter34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter34.setStatus("current")


class _MccpRelcPlanInCounter35_Type(Integer32):
    """Custom type mccpRelcPlanInCounter35 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter35_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter35_Object = MibTableColumn
mccpRelcPlanInCounter35 = _MccpRelcPlanInCounter35_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 37),
    _MccpRelcPlanInCounter35_Type()
)
mccpRelcPlanInCounter35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter35.setStatus("current")


class _MccpRelcPlanInCounter36_Type(Integer32):
    """Custom type mccpRelcPlanInCounter36 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter36_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter36_Object = MibTableColumn
mccpRelcPlanInCounter36 = _MccpRelcPlanInCounter36_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 38),
    _MccpRelcPlanInCounter36_Type()
)
mccpRelcPlanInCounter36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter36.setStatus("current")


class _MccpRelcPlanInCounter37_Type(Integer32):
    """Custom type mccpRelcPlanInCounter37 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter37_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter37_Object = MibTableColumn
mccpRelcPlanInCounter37 = _MccpRelcPlanInCounter37_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 39),
    _MccpRelcPlanInCounter37_Type()
)
mccpRelcPlanInCounter37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter37.setStatus("current")


class _MccpRelcPlanInCounter38_Type(Integer32):
    """Custom type mccpRelcPlanInCounter38 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter38_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter38_Object = MibTableColumn
mccpRelcPlanInCounter38 = _MccpRelcPlanInCounter38_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 40),
    _MccpRelcPlanInCounter38_Type()
)
mccpRelcPlanInCounter38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter38.setStatus("current")


class _MccpRelcPlanInCounter39_Type(Integer32):
    """Custom type mccpRelcPlanInCounter39 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter39_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter39_Object = MibTableColumn
mccpRelcPlanInCounter39 = _MccpRelcPlanInCounter39_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 41),
    _MccpRelcPlanInCounter39_Type()
)
mccpRelcPlanInCounter39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter39.setStatus("current")


class _MccpRelcPlanInCounter40_Type(Integer32):
    """Custom type mccpRelcPlanInCounter40 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter40_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter40_Object = MibTableColumn
mccpRelcPlanInCounter40 = _MccpRelcPlanInCounter40_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 42),
    _MccpRelcPlanInCounter40_Type()
)
mccpRelcPlanInCounter40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter40.setStatus("current")


class _MccpRelcPlanInCounter41_Type(Integer32):
    """Custom type mccpRelcPlanInCounter41 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter41_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter41_Object = MibTableColumn
mccpRelcPlanInCounter41 = _MccpRelcPlanInCounter41_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 43),
    _MccpRelcPlanInCounter41_Type()
)
mccpRelcPlanInCounter41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter41.setStatus("current")


class _MccpRelcPlanInCounter42_Type(Integer32):
    """Custom type mccpRelcPlanInCounter42 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter42_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter42_Object = MibTableColumn
mccpRelcPlanInCounter42 = _MccpRelcPlanInCounter42_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 44),
    _MccpRelcPlanInCounter42_Type()
)
mccpRelcPlanInCounter42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter42.setStatus("current")


class _MccpRelcPlanInCounter43_Type(Integer32):
    """Custom type mccpRelcPlanInCounter43 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter43_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter43_Object = MibTableColumn
mccpRelcPlanInCounter43 = _MccpRelcPlanInCounter43_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 45),
    _MccpRelcPlanInCounter43_Type()
)
mccpRelcPlanInCounter43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter43.setStatus("current")


class _MccpRelcPlanInCounter44_Type(Integer32):
    """Custom type mccpRelcPlanInCounter44 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter44_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter44_Object = MibTableColumn
mccpRelcPlanInCounter44 = _MccpRelcPlanInCounter44_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 46),
    _MccpRelcPlanInCounter44_Type()
)
mccpRelcPlanInCounter44.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter44.setStatus("current")


class _MccpRelcPlanInCounter45_Type(Integer32):
    """Custom type mccpRelcPlanInCounter45 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter45_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter45_Object = MibTableColumn
mccpRelcPlanInCounter45 = _MccpRelcPlanInCounter45_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 47),
    _MccpRelcPlanInCounter45_Type()
)
mccpRelcPlanInCounter45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter45.setStatus("current")


class _MccpRelcPlanInCounter46_Type(Integer32):
    """Custom type mccpRelcPlanInCounter46 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter46_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter46_Object = MibTableColumn
mccpRelcPlanInCounter46 = _MccpRelcPlanInCounter46_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 48),
    _MccpRelcPlanInCounter46_Type()
)
mccpRelcPlanInCounter46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter46.setStatus("current")


class _MccpRelcPlanInCounter47_Type(Integer32):
    """Custom type mccpRelcPlanInCounter47 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter47_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter47_Object = MibTableColumn
mccpRelcPlanInCounter47 = _MccpRelcPlanInCounter47_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 49),
    _MccpRelcPlanInCounter47_Type()
)
mccpRelcPlanInCounter47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter47.setStatus("current")


class _MccpRelcPlanInCounter48_Type(Integer32):
    """Custom type mccpRelcPlanInCounter48 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter48_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter48_Object = MibTableColumn
mccpRelcPlanInCounter48 = _MccpRelcPlanInCounter48_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 50),
    _MccpRelcPlanInCounter48_Type()
)
mccpRelcPlanInCounter48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter48.setStatus("current")


class _MccpRelcPlanInCounter49_Type(Integer32):
    """Custom type mccpRelcPlanInCounter49 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter49_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter49_Object = MibTableColumn
mccpRelcPlanInCounter49 = _MccpRelcPlanInCounter49_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 51),
    _MccpRelcPlanInCounter49_Type()
)
mccpRelcPlanInCounter49.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter49.setStatus("current")


class _MccpRelcPlanInCounter50_Type(Integer32):
    """Custom type mccpRelcPlanInCounter50 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter50_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter50_Object = MibTableColumn
mccpRelcPlanInCounter50 = _MccpRelcPlanInCounter50_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 52),
    _MccpRelcPlanInCounter50_Type()
)
mccpRelcPlanInCounter50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter50.setStatus("current")


class _MccpRelcPlanInCounter51_Type(Integer32):
    """Custom type mccpRelcPlanInCounter51 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter51_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter51_Object = MibTableColumn
mccpRelcPlanInCounter51 = _MccpRelcPlanInCounter51_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 53),
    _MccpRelcPlanInCounter51_Type()
)
mccpRelcPlanInCounter51.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter51.setStatus("current")


class _MccpRelcPlanInCounter52_Type(Integer32):
    """Custom type mccpRelcPlanInCounter52 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter52_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter52_Object = MibTableColumn
mccpRelcPlanInCounter52 = _MccpRelcPlanInCounter52_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 54),
    _MccpRelcPlanInCounter52_Type()
)
mccpRelcPlanInCounter52.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter52.setStatus("current")


class _MccpRelcPlanInCounter53_Type(Integer32):
    """Custom type mccpRelcPlanInCounter53 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter53_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter53_Object = MibTableColumn
mccpRelcPlanInCounter53 = _MccpRelcPlanInCounter53_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 55),
    _MccpRelcPlanInCounter53_Type()
)
mccpRelcPlanInCounter53.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter53.setStatus("current")


class _MccpRelcPlanInCounter54_Type(Integer32):
    """Custom type mccpRelcPlanInCounter54 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter54_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter54_Object = MibTableColumn
mccpRelcPlanInCounter54 = _MccpRelcPlanInCounter54_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 56),
    _MccpRelcPlanInCounter54_Type()
)
mccpRelcPlanInCounter54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter54.setStatus("current")


class _MccpRelcPlanInCounter55_Type(Integer32):
    """Custom type mccpRelcPlanInCounter55 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter55_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter55_Object = MibTableColumn
mccpRelcPlanInCounter55 = _MccpRelcPlanInCounter55_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 57),
    _MccpRelcPlanInCounter55_Type()
)
mccpRelcPlanInCounter55.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter55.setStatus("current")


class _MccpRelcPlanInCounter56_Type(Integer32):
    """Custom type mccpRelcPlanInCounter56 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter56_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter56_Object = MibTableColumn
mccpRelcPlanInCounter56 = _MccpRelcPlanInCounter56_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 58),
    _MccpRelcPlanInCounter56_Type()
)
mccpRelcPlanInCounter56.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter56.setStatus("current")


class _MccpRelcPlanInCounter57_Type(Integer32):
    """Custom type mccpRelcPlanInCounter57 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter57_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter57_Object = MibTableColumn
mccpRelcPlanInCounter57 = _MccpRelcPlanInCounter57_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 59),
    _MccpRelcPlanInCounter57_Type()
)
mccpRelcPlanInCounter57.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter57.setStatus("current")


class _MccpRelcPlanInCounter58_Type(Integer32):
    """Custom type mccpRelcPlanInCounter58 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter58_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter58_Object = MibTableColumn
mccpRelcPlanInCounter58 = _MccpRelcPlanInCounter58_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 60),
    _MccpRelcPlanInCounter58_Type()
)
mccpRelcPlanInCounter58.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter58.setStatus("current")


class _MccpRelcPlanInCounter59_Type(Integer32):
    """Custom type mccpRelcPlanInCounter59 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter59_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter59_Object = MibTableColumn
mccpRelcPlanInCounter59 = _MccpRelcPlanInCounter59_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 61),
    _MccpRelcPlanInCounter59_Type()
)
mccpRelcPlanInCounter59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter59.setStatus("current")


class _MccpRelcPlanInCounter60_Type(Integer32):
    """Custom type mccpRelcPlanInCounter60 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter60_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter60_Object = MibTableColumn
mccpRelcPlanInCounter60 = _MccpRelcPlanInCounter60_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 62),
    _MccpRelcPlanInCounter60_Type()
)
mccpRelcPlanInCounter60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter60.setStatus("current")


class _MccpRelcPlanInCounter61_Type(Integer32):
    """Custom type mccpRelcPlanInCounter61 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter61_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter61_Object = MibTableColumn
mccpRelcPlanInCounter61 = _MccpRelcPlanInCounter61_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 63),
    _MccpRelcPlanInCounter61_Type()
)
mccpRelcPlanInCounter61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter61.setStatus("current")


class _MccpRelcPlanInCounter62_Type(Integer32):
    """Custom type mccpRelcPlanInCounter62 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter62_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter62_Object = MibTableColumn
mccpRelcPlanInCounter62 = _MccpRelcPlanInCounter62_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 64),
    _MccpRelcPlanInCounter62_Type()
)
mccpRelcPlanInCounter62.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter62.setStatus("current")


class _MccpRelcPlanInCounter63_Type(Integer32):
    """Custom type mccpRelcPlanInCounter63 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter63_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter63_Object = MibTableColumn
mccpRelcPlanInCounter63 = _MccpRelcPlanInCounter63_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 65),
    _MccpRelcPlanInCounter63_Type()
)
mccpRelcPlanInCounter63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter63.setStatus("current")


class _MccpRelcPlanInCounter64_Type(Integer32):
    """Custom type mccpRelcPlanInCounter64 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter64_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter64_Object = MibTableColumn
mccpRelcPlanInCounter64 = _MccpRelcPlanInCounter64_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 66),
    _MccpRelcPlanInCounter64_Type()
)
mccpRelcPlanInCounter64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter64.setStatus("current")


class _MccpRelcPlanInCounter65_Type(Integer32):
    """Custom type mccpRelcPlanInCounter65 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter65_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter65_Object = MibTableColumn
mccpRelcPlanInCounter65 = _MccpRelcPlanInCounter65_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 67),
    _MccpRelcPlanInCounter65_Type()
)
mccpRelcPlanInCounter65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter65.setStatus("current")


class _MccpRelcPlanInCounter66_Type(Integer32):
    """Custom type mccpRelcPlanInCounter66 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter66_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter66_Object = MibTableColumn
mccpRelcPlanInCounter66 = _MccpRelcPlanInCounter66_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 68),
    _MccpRelcPlanInCounter66_Type()
)
mccpRelcPlanInCounter66.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter66.setStatus("current")


class _MccpRelcPlanInCounter67_Type(Integer32):
    """Custom type mccpRelcPlanInCounter67 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter67_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter67_Object = MibTableColumn
mccpRelcPlanInCounter67 = _MccpRelcPlanInCounter67_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 69),
    _MccpRelcPlanInCounter67_Type()
)
mccpRelcPlanInCounter67.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter67.setStatus("current")


class _MccpRelcPlanInCounter68_Type(Integer32):
    """Custom type mccpRelcPlanInCounter68 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter68_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter68_Object = MibTableColumn
mccpRelcPlanInCounter68 = _MccpRelcPlanInCounter68_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 70),
    _MccpRelcPlanInCounter68_Type()
)
mccpRelcPlanInCounter68.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter68.setStatus("current")


class _MccpRelcPlanInCounter69_Type(Integer32):
    """Custom type mccpRelcPlanInCounter69 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter69_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter69_Object = MibTableColumn
mccpRelcPlanInCounter69 = _MccpRelcPlanInCounter69_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 71),
    _MccpRelcPlanInCounter69_Type()
)
mccpRelcPlanInCounter69.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter69.setStatus("current")


class _MccpRelcPlanInCounter70_Type(Integer32):
    """Custom type mccpRelcPlanInCounter70 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter70_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter70_Object = MibTableColumn
mccpRelcPlanInCounter70 = _MccpRelcPlanInCounter70_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 72),
    _MccpRelcPlanInCounter70_Type()
)
mccpRelcPlanInCounter70.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter70.setStatus("current")


class _MccpRelcPlanInCounter71_Type(Integer32):
    """Custom type mccpRelcPlanInCounter71 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter71_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter71_Object = MibTableColumn
mccpRelcPlanInCounter71 = _MccpRelcPlanInCounter71_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 73),
    _MccpRelcPlanInCounter71_Type()
)
mccpRelcPlanInCounter71.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter71.setStatus("current")


class _MccpRelcPlanInCounter72_Type(Integer32):
    """Custom type mccpRelcPlanInCounter72 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter72_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter72_Object = MibTableColumn
mccpRelcPlanInCounter72 = _MccpRelcPlanInCounter72_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 74),
    _MccpRelcPlanInCounter72_Type()
)
mccpRelcPlanInCounter72.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter72.setStatus("current")


class _MccpRelcPlanInCounter73_Type(Integer32):
    """Custom type mccpRelcPlanInCounter73 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter73_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter73_Object = MibTableColumn
mccpRelcPlanInCounter73 = _MccpRelcPlanInCounter73_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 75),
    _MccpRelcPlanInCounter73_Type()
)
mccpRelcPlanInCounter73.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter73.setStatus("current")


class _MccpRelcPlanInCounter74_Type(Integer32):
    """Custom type mccpRelcPlanInCounter74 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter74_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter74_Object = MibTableColumn
mccpRelcPlanInCounter74 = _MccpRelcPlanInCounter74_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 76),
    _MccpRelcPlanInCounter74_Type()
)
mccpRelcPlanInCounter74.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter74.setStatus("current")


class _MccpRelcPlanInCounter75_Type(Integer32):
    """Custom type mccpRelcPlanInCounter75 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter75_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter75_Object = MibTableColumn
mccpRelcPlanInCounter75 = _MccpRelcPlanInCounter75_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 77),
    _MccpRelcPlanInCounter75_Type()
)
mccpRelcPlanInCounter75.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter75.setStatus("current")


class _MccpRelcPlanInCounter76_Type(Integer32):
    """Custom type mccpRelcPlanInCounter76 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter76_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter76_Object = MibTableColumn
mccpRelcPlanInCounter76 = _MccpRelcPlanInCounter76_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 78),
    _MccpRelcPlanInCounter76_Type()
)
mccpRelcPlanInCounter76.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter76.setStatus("current")


class _MccpRelcPlanInCounter77_Type(Integer32):
    """Custom type mccpRelcPlanInCounter77 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter77_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter77_Object = MibTableColumn
mccpRelcPlanInCounter77 = _MccpRelcPlanInCounter77_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 79),
    _MccpRelcPlanInCounter77_Type()
)
mccpRelcPlanInCounter77.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter77.setStatus("current")


class _MccpRelcPlanInCounter78_Type(Integer32):
    """Custom type mccpRelcPlanInCounter78 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter78_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter78_Object = MibTableColumn
mccpRelcPlanInCounter78 = _MccpRelcPlanInCounter78_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 80),
    _MccpRelcPlanInCounter78_Type()
)
mccpRelcPlanInCounter78.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter78.setStatus("current")


class _MccpRelcPlanInCounter79_Type(Integer32):
    """Custom type mccpRelcPlanInCounter79 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter79_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter79_Object = MibTableColumn
mccpRelcPlanInCounter79 = _MccpRelcPlanInCounter79_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 81),
    _MccpRelcPlanInCounter79_Type()
)
mccpRelcPlanInCounter79.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter79.setStatus("current")


class _MccpRelcPlanInCounter80_Type(Integer32):
    """Custom type mccpRelcPlanInCounter80 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter80_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter80_Object = MibTableColumn
mccpRelcPlanInCounter80 = _MccpRelcPlanInCounter80_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 82),
    _MccpRelcPlanInCounter80_Type()
)
mccpRelcPlanInCounter80.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter80.setStatus("current")


class _MccpRelcPlanInCounter81_Type(Integer32):
    """Custom type mccpRelcPlanInCounter81 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter81_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter81_Object = MibTableColumn
mccpRelcPlanInCounter81 = _MccpRelcPlanInCounter81_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 83),
    _MccpRelcPlanInCounter81_Type()
)
mccpRelcPlanInCounter81.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter81.setStatus("current")


class _MccpRelcPlanInCounter82_Type(Integer32):
    """Custom type mccpRelcPlanInCounter82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter82_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter82_Object = MibTableColumn
mccpRelcPlanInCounter82 = _MccpRelcPlanInCounter82_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 84),
    _MccpRelcPlanInCounter82_Type()
)
mccpRelcPlanInCounter82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter82.setStatus("current")


class _MccpRelcPlanInCounter83_Type(Integer32):
    """Custom type mccpRelcPlanInCounter83 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter83_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter83_Object = MibTableColumn
mccpRelcPlanInCounter83 = _MccpRelcPlanInCounter83_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 85),
    _MccpRelcPlanInCounter83_Type()
)
mccpRelcPlanInCounter83.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter83.setStatus("current")


class _MccpRelcPlanInCounter84_Type(Integer32):
    """Custom type mccpRelcPlanInCounter84 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter84_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter84_Object = MibTableColumn
mccpRelcPlanInCounter84 = _MccpRelcPlanInCounter84_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 86),
    _MccpRelcPlanInCounter84_Type()
)
mccpRelcPlanInCounter84.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter84.setStatus("current")


class _MccpRelcPlanInCounter85_Type(Integer32):
    """Custom type mccpRelcPlanInCounter85 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter85_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter85_Object = MibTableColumn
mccpRelcPlanInCounter85 = _MccpRelcPlanInCounter85_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 87),
    _MccpRelcPlanInCounter85_Type()
)
mccpRelcPlanInCounter85.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter85.setStatus("current")


class _MccpRelcPlanInCounter86_Type(Integer32):
    """Custom type mccpRelcPlanInCounter86 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter86_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter86_Object = MibTableColumn
mccpRelcPlanInCounter86 = _MccpRelcPlanInCounter86_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 88),
    _MccpRelcPlanInCounter86_Type()
)
mccpRelcPlanInCounter86.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter86.setStatus("current")


class _MccpRelcPlanInCounter87_Type(Integer32):
    """Custom type mccpRelcPlanInCounter87 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter87_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter87_Object = MibTableColumn
mccpRelcPlanInCounter87 = _MccpRelcPlanInCounter87_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 89),
    _MccpRelcPlanInCounter87_Type()
)
mccpRelcPlanInCounter87.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter87.setStatus("current")


class _MccpRelcPlanInCounter88_Type(Integer32):
    """Custom type mccpRelcPlanInCounter88 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter88_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter88_Object = MibTableColumn
mccpRelcPlanInCounter88 = _MccpRelcPlanInCounter88_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 90),
    _MccpRelcPlanInCounter88_Type()
)
mccpRelcPlanInCounter88.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter88.setStatus("current")


class _MccpRelcPlanInCounter89_Type(Integer32):
    """Custom type mccpRelcPlanInCounter89 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter89_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter89_Object = MibTableColumn
mccpRelcPlanInCounter89 = _MccpRelcPlanInCounter89_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 91),
    _MccpRelcPlanInCounter89_Type()
)
mccpRelcPlanInCounter89.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter89.setStatus("current")


class _MccpRelcPlanInCounter90_Type(Integer32):
    """Custom type mccpRelcPlanInCounter90 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter90_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter90_Object = MibTableColumn
mccpRelcPlanInCounter90 = _MccpRelcPlanInCounter90_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 92),
    _MccpRelcPlanInCounter90_Type()
)
mccpRelcPlanInCounter90.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter90.setStatus("current")


class _MccpRelcPlanInCounter91_Type(Integer32):
    """Custom type mccpRelcPlanInCounter91 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter91_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter91_Object = MibTableColumn
mccpRelcPlanInCounter91 = _MccpRelcPlanInCounter91_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 93),
    _MccpRelcPlanInCounter91_Type()
)
mccpRelcPlanInCounter91.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter91.setStatus("current")


class _MccpRelcPlanInCounter92_Type(Integer32):
    """Custom type mccpRelcPlanInCounter92 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter92_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter92_Object = MibTableColumn
mccpRelcPlanInCounter92 = _MccpRelcPlanInCounter92_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 94),
    _MccpRelcPlanInCounter92_Type()
)
mccpRelcPlanInCounter92.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter92.setStatus("current")


class _MccpRelcPlanInCounter93_Type(Integer32):
    """Custom type mccpRelcPlanInCounter93 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter93_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter93_Object = MibTableColumn
mccpRelcPlanInCounter93 = _MccpRelcPlanInCounter93_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 95),
    _MccpRelcPlanInCounter93_Type()
)
mccpRelcPlanInCounter93.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter93.setStatus("current")


class _MccpRelcPlanInCounter94_Type(Integer32):
    """Custom type mccpRelcPlanInCounter94 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter94_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter94_Object = MibTableColumn
mccpRelcPlanInCounter94 = _MccpRelcPlanInCounter94_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 96),
    _MccpRelcPlanInCounter94_Type()
)
mccpRelcPlanInCounter94.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter94.setStatus("current")


class _MccpRelcPlanInCounter95_Type(Integer32):
    """Custom type mccpRelcPlanInCounter95 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter95_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter95_Object = MibTableColumn
mccpRelcPlanInCounter95 = _MccpRelcPlanInCounter95_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 97),
    _MccpRelcPlanInCounter95_Type()
)
mccpRelcPlanInCounter95.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter95.setStatus("current")


class _MccpRelcPlanInCounter96_Type(Integer32):
    """Custom type mccpRelcPlanInCounter96 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter96_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter96_Object = MibTableColumn
mccpRelcPlanInCounter96 = _MccpRelcPlanInCounter96_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 98),
    _MccpRelcPlanInCounter96_Type()
)
mccpRelcPlanInCounter96.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter96.setStatus("current")


class _MccpRelcPlanInCounter97_Type(Integer32):
    """Custom type mccpRelcPlanInCounter97 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter97_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter97_Object = MibTableColumn
mccpRelcPlanInCounter97 = _MccpRelcPlanInCounter97_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 99),
    _MccpRelcPlanInCounter97_Type()
)
mccpRelcPlanInCounter97.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter97.setStatus("current")


class _MccpRelcPlanInCounter98_Type(Integer32):
    """Custom type mccpRelcPlanInCounter98 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter98_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter98_Object = MibTableColumn
mccpRelcPlanInCounter98 = _MccpRelcPlanInCounter98_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 100),
    _MccpRelcPlanInCounter98_Type()
)
mccpRelcPlanInCounter98.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter98.setStatus("current")


class _MccpRelcPlanInCounter99_Type(Integer32):
    """Custom type mccpRelcPlanInCounter99 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter99_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter99_Object = MibTableColumn
mccpRelcPlanInCounter99 = _MccpRelcPlanInCounter99_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 101),
    _MccpRelcPlanInCounter99_Type()
)
mccpRelcPlanInCounter99.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter99.setStatus("current")


class _MccpRelcPlanInCounter100_Type(Integer32):
    """Custom type mccpRelcPlanInCounter100 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter100_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter100_Object = MibTableColumn
mccpRelcPlanInCounter100 = _MccpRelcPlanInCounter100_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 102),
    _MccpRelcPlanInCounter100_Type()
)
mccpRelcPlanInCounter100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter100.setStatus("current")


class _MccpRelcPlanInCounter101_Type(Integer32):
    """Custom type mccpRelcPlanInCounter101 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter101_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter101_Object = MibTableColumn
mccpRelcPlanInCounter101 = _MccpRelcPlanInCounter101_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 103),
    _MccpRelcPlanInCounter101_Type()
)
mccpRelcPlanInCounter101.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter101.setStatus("current")


class _MccpRelcPlanInCounter102_Type(Integer32):
    """Custom type mccpRelcPlanInCounter102 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter102_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter102_Object = MibTableColumn
mccpRelcPlanInCounter102 = _MccpRelcPlanInCounter102_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 104),
    _MccpRelcPlanInCounter102_Type()
)
mccpRelcPlanInCounter102.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter102.setStatus("current")


class _MccpRelcPlanInCounter103_Type(Integer32):
    """Custom type mccpRelcPlanInCounter103 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter103_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter103_Object = MibTableColumn
mccpRelcPlanInCounter103 = _MccpRelcPlanInCounter103_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 105),
    _MccpRelcPlanInCounter103_Type()
)
mccpRelcPlanInCounter103.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter103.setStatus("current")


class _MccpRelcPlanInCounter104_Type(Integer32):
    """Custom type mccpRelcPlanInCounter104 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter104_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter104_Object = MibTableColumn
mccpRelcPlanInCounter104 = _MccpRelcPlanInCounter104_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 106),
    _MccpRelcPlanInCounter104_Type()
)
mccpRelcPlanInCounter104.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter104.setStatus("current")


class _MccpRelcPlanInCounter105_Type(Integer32):
    """Custom type mccpRelcPlanInCounter105 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter105_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter105_Object = MibTableColumn
mccpRelcPlanInCounter105 = _MccpRelcPlanInCounter105_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 107),
    _MccpRelcPlanInCounter105_Type()
)
mccpRelcPlanInCounter105.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter105.setStatus("current")


class _MccpRelcPlanInCounter106_Type(Integer32):
    """Custom type mccpRelcPlanInCounter106 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter106_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter106_Object = MibTableColumn
mccpRelcPlanInCounter106 = _MccpRelcPlanInCounter106_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 108),
    _MccpRelcPlanInCounter106_Type()
)
mccpRelcPlanInCounter106.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter106.setStatus("current")


class _MccpRelcPlanInCounter107_Type(Integer32):
    """Custom type mccpRelcPlanInCounter107 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter107_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter107_Object = MibTableColumn
mccpRelcPlanInCounter107 = _MccpRelcPlanInCounter107_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 109),
    _MccpRelcPlanInCounter107_Type()
)
mccpRelcPlanInCounter107.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter107.setStatus("current")


class _MccpRelcPlanInCounter108_Type(Integer32):
    """Custom type mccpRelcPlanInCounter108 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter108_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter108_Object = MibTableColumn
mccpRelcPlanInCounter108 = _MccpRelcPlanInCounter108_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 110),
    _MccpRelcPlanInCounter108_Type()
)
mccpRelcPlanInCounter108.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter108.setStatus("current")


class _MccpRelcPlanInCounter109_Type(Integer32):
    """Custom type mccpRelcPlanInCounter109 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter109_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter109_Object = MibTableColumn
mccpRelcPlanInCounter109 = _MccpRelcPlanInCounter109_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 111),
    _MccpRelcPlanInCounter109_Type()
)
mccpRelcPlanInCounter109.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter109.setStatus("current")


class _MccpRelcPlanInCounter110_Type(Integer32):
    """Custom type mccpRelcPlanInCounter110 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter110_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter110_Object = MibTableColumn
mccpRelcPlanInCounter110 = _MccpRelcPlanInCounter110_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 112),
    _MccpRelcPlanInCounter110_Type()
)
mccpRelcPlanInCounter110.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter110.setStatus("current")


class _MccpRelcPlanInCounter111_Type(Integer32):
    """Custom type mccpRelcPlanInCounter111 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter111_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter111_Object = MibTableColumn
mccpRelcPlanInCounter111 = _MccpRelcPlanInCounter111_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 113),
    _MccpRelcPlanInCounter111_Type()
)
mccpRelcPlanInCounter111.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter111.setStatus("current")


class _MccpRelcPlanInCounter112_Type(Integer32):
    """Custom type mccpRelcPlanInCounter112 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter112_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter112_Object = MibTableColumn
mccpRelcPlanInCounter112 = _MccpRelcPlanInCounter112_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 114),
    _MccpRelcPlanInCounter112_Type()
)
mccpRelcPlanInCounter112.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter112.setStatus("current")


class _MccpRelcPlanInCounter113_Type(Integer32):
    """Custom type mccpRelcPlanInCounter113 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter113_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter113_Object = MibTableColumn
mccpRelcPlanInCounter113 = _MccpRelcPlanInCounter113_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 115),
    _MccpRelcPlanInCounter113_Type()
)
mccpRelcPlanInCounter113.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter113.setStatus("current")


class _MccpRelcPlanInCounter114_Type(Integer32):
    """Custom type mccpRelcPlanInCounter114 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter114_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter114_Object = MibTableColumn
mccpRelcPlanInCounter114 = _MccpRelcPlanInCounter114_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 116),
    _MccpRelcPlanInCounter114_Type()
)
mccpRelcPlanInCounter114.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter114.setStatus("current")


class _MccpRelcPlanInCounter115_Type(Integer32):
    """Custom type mccpRelcPlanInCounter115 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter115_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter115_Object = MibTableColumn
mccpRelcPlanInCounter115 = _MccpRelcPlanInCounter115_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 117),
    _MccpRelcPlanInCounter115_Type()
)
mccpRelcPlanInCounter115.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter115.setStatus("current")


class _MccpRelcPlanInCounter116_Type(Integer32):
    """Custom type mccpRelcPlanInCounter116 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter116_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter116_Object = MibTableColumn
mccpRelcPlanInCounter116 = _MccpRelcPlanInCounter116_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 118),
    _MccpRelcPlanInCounter116_Type()
)
mccpRelcPlanInCounter116.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter116.setStatus("current")


class _MccpRelcPlanInCounter117_Type(Integer32):
    """Custom type mccpRelcPlanInCounter117 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter117_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter117_Object = MibTableColumn
mccpRelcPlanInCounter117 = _MccpRelcPlanInCounter117_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 119),
    _MccpRelcPlanInCounter117_Type()
)
mccpRelcPlanInCounter117.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter117.setStatus("current")


class _MccpRelcPlanInCounter118_Type(Integer32):
    """Custom type mccpRelcPlanInCounter118 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter118_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter118_Object = MibTableColumn
mccpRelcPlanInCounter118 = _MccpRelcPlanInCounter118_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 120),
    _MccpRelcPlanInCounter118_Type()
)
mccpRelcPlanInCounter118.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter118.setStatus("current")


class _MccpRelcPlanInCounter119_Type(Integer32):
    """Custom type mccpRelcPlanInCounter119 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter119_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter119_Object = MibTableColumn
mccpRelcPlanInCounter119 = _MccpRelcPlanInCounter119_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 121),
    _MccpRelcPlanInCounter119_Type()
)
mccpRelcPlanInCounter119.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter119.setStatus("current")


class _MccpRelcPlanInCounter120_Type(Integer32):
    """Custom type mccpRelcPlanInCounter120 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter120_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter120_Object = MibTableColumn
mccpRelcPlanInCounter120 = _MccpRelcPlanInCounter120_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 122),
    _MccpRelcPlanInCounter120_Type()
)
mccpRelcPlanInCounter120.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter120.setStatus("current")


class _MccpRelcPlanInCounter121_Type(Integer32):
    """Custom type mccpRelcPlanInCounter121 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter121_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter121_Object = MibTableColumn
mccpRelcPlanInCounter121 = _MccpRelcPlanInCounter121_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 123),
    _MccpRelcPlanInCounter121_Type()
)
mccpRelcPlanInCounter121.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter121.setStatus("current")


class _MccpRelcPlanInCounter122_Type(Integer32):
    """Custom type mccpRelcPlanInCounter122 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter122_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter122_Object = MibTableColumn
mccpRelcPlanInCounter122 = _MccpRelcPlanInCounter122_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 124),
    _MccpRelcPlanInCounter122_Type()
)
mccpRelcPlanInCounter122.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter122.setStatus("current")


class _MccpRelcPlanInCounter123_Type(Integer32):
    """Custom type mccpRelcPlanInCounter123 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter123_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter123_Object = MibTableColumn
mccpRelcPlanInCounter123 = _MccpRelcPlanInCounter123_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 125),
    _MccpRelcPlanInCounter123_Type()
)
mccpRelcPlanInCounter123.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter123.setStatus("current")


class _MccpRelcPlanInCounter124_Type(Integer32):
    """Custom type mccpRelcPlanInCounter124 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter124_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter124_Object = MibTableColumn
mccpRelcPlanInCounter124 = _MccpRelcPlanInCounter124_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 126),
    _MccpRelcPlanInCounter124_Type()
)
mccpRelcPlanInCounter124.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter124.setStatus("current")


class _MccpRelcPlanInCounter125_Type(Integer32):
    """Custom type mccpRelcPlanInCounter125 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter125_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter125_Object = MibTableColumn
mccpRelcPlanInCounter125 = _MccpRelcPlanInCounter125_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 127),
    _MccpRelcPlanInCounter125_Type()
)
mccpRelcPlanInCounter125.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter125.setStatus("current")


class _MccpRelcPlanInCounter126_Type(Integer32):
    """Custom type mccpRelcPlanInCounter126 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter126_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter126_Object = MibTableColumn
mccpRelcPlanInCounter126 = _MccpRelcPlanInCounter126_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 128),
    _MccpRelcPlanInCounter126_Type()
)
mccpRelcPlanInCounter126.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter126.setStatus("current")


class _MccpRelcPlanInCounter127_Type(Integer32):
    """Custom type mccpRelcPlanInCounter127 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanInCounter127_Type.__name__ = "Integer32"
_MccpRelcPlanInCounter127_Object = MibTableColumn
mccpRelcPlanInCounter127 = _MccpRelcPlanInCounter127_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 30, 1, 129),
    _MccpRelcPlanInCounter127_Type()
)
mccpRelcPlanInCounter127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanInCounter127.setStatus("current")
_MccpRelcPlanOutTable_Object = MibTable
mccpRelcPlanOutTable = _MccpRelcPlanOutTable_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31)
)
if mibBuilder.loadTexts:
    mccpRelcPlanOutTable.setStatus("current")
_MccpRelcPlanOutEntry_Object = MibTableRow
mccpRelcPlanOutEntry = _MccpRelcPlanOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1)
)
mccpRelcPlanOutEntry.setIndexNames(
    (0, "ELTEX-MCCP", "mccpRelcPlanOutIndex"),
)
if mibBuilder.loadTexts:
    mccpRelcPlanOutEntry.setStatus("current")


class _MccpRelcPlanOutIndex_Type(Integer32):
    """Custom type mccpRelcPlanOutIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MccpRelcPlanOutIndex_Type.__name__ = "Integer32"
_MccpRelcPlanOutIndex_Object = MibTableColumn
mccpRelcPlanOutIndex = _MccpRelcPlanOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 1),
    _MccpRelcPlanOutIndex_Type()
)
mccpRelcPlanOutIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mccpRelcPlanOutIndex.setStatus("current")


class _MccpRelcPlanOutCounter0_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter0_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter0_Object = MibTableColumn
mccpRelcPlanOutCounter0 = _MccpRelcPlanOutCounter0_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 2),
    _MccpRelcPlanOutCounter0_Type()
)
mccpRelcPlanOutCounter0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter0.setStatus("current")


class _MccpRelcPlanOutCounter1_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter1_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter1_Object = MibTableColumn
mccpRelcPlanOutCounter1 = _MccpRelcPlanOutCounter1_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 3),
    _MccpRelcPlanOutCounter1_Type()
)
mccpRelcPlanOutCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter1.setStatus("current")


class _MccpRelcPlanOutCounter2_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter2_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter2_Object = MibTableColumn
mccpRelcPlanOutCounter2 = _MccpRelcPlanOutCounter2_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 4),
    _MccpRelcPlanOutCounter2_Type()
)
mccpRelcPlanOutCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter2.setStatus("current")


class _MccpRelcPlanOutCounter3_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter3_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter3_Object = MibTableColumn
mccpRelcPlanOutCounter3 = _MccpRelcPlanOutCounter3_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 5),
    _MccpRelcPlanOutCounter3_Type()
)
mccpRelcPlanOutCounter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter3.setStatus("current")


class _MccpRelcPlanOutCounter4_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter4_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter4_Object = MibTableColumn
mccpRelcPlanOutCounter4 = _MccpRelcPlanOutCounter4_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 6),
    _MccpRelcPlanOutCounter4_Type()
)
mccpRelcPlanOutCounter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter4.setStatus("current")


class _MccpRelcPlanOutCounter5_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter5_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter5_Object = MibTableColumn
mccpRelcPlanOutCounter5 = _MccpRelcPlanOutCounter5_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 7),
    _MccpRelcPlanOutCounter5_Type()
)
mccpRelcPlanOutCounter5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter5.setStatus("current")


class _MccpRelcPlanOutCounter6_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter6_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter6_Object = MibTableColumn
mccpRelcPlanOutCounter6 = _MccpRelcPlanOutCounter6_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 8),
    _MccpRelcPlanOutCounter6_Type()
)
mccpRelcPlanOutCounter6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter6.setStatus("current")


class _MccpRelcPlanOutCounter7_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter7_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter7_Object = MibTableColumn
mccpRelcPlanOutCounter7 = _MccpRelcPlanOutCounter7_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 9),
    _MccpRelcPlanOutCounter7_Type()
)
mccpRelcPlanOutCounter7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter7.setStatus("current")


class _MccpRelcPlanOutCounter8_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter8_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter8_Object = MibTableColumn
mccpRelcPlanOutCounter8 = _MccpRelcPlanOutCounter8_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 10),
    _MccpRelcPlanOutCounter8_Type()
)
mccpRelcPlanOutCounter8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter8.setStatus("current")


class _MccpRelcPlanOutCounter9_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter9_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter9_Object = MibTableColumn
mccpRelcPlanOutCounter9 = _MccpRelcPlanOutCounter9_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 11),
    _MccpRelcPlanOutCounter9_Type()
)
mccpRelcPlanOutCounter9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter9.setStatus("current")


class _MccpRelcPlanOutCounter10_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter10_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter10_Object = MibTableColumn
mccpRelcPlanOutCounter10 = _MccpRelcPlanOutCounter10_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 12),
    _MccpRelcPlanOutCounter10_Type()
)
mccpRelcPlanOutCounter10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter10.setStatus("current")


class _MccpRelcPlanOutCounter11_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter11_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter11_Object = MibTableColumn
mccpRelcPlanOutCounter11 = _MccpRelcPlanOutCounter11_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 13),
    _MccpRelcPlanOutCounter11_Type()
)
mccpRelcPlanOutCounter11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter11.setStatus("current")


class _MccpRelcPlanOutCounter12_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter12_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter12_Object = MibTableColumn
mccpRelcPlanOutCounter12 = _MccpRelcPlanOutCounter12_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 14),
    _MccpRelcPlanOutCounter12_Type()
)
mccpRelcPlanOutCounter12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter12.setStatus("current")


class _MccpRelcPlanOutCounter13_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter13_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter13_Object = MibTableColumn
mccpRelcPlanOutCounter13 = _MccpRelcPlanOutCounter13_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 15),
    _MccpRelcPlanOutCounter13_Type()
)
mccpRelcPlanOutCounter13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter13.setStatus("current")


class _MccpRelcPlanOutCounter14_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter14_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter14_Object = MibTableColumn
mccpRelcPlanOutCounter14 = _MccpRelcPlanOutCounter14_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 16),
    _MccpRelcPlanOutCounter14_Type()
)
mccpRelcPlanOutCounter14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter14.setStatus("current")


class _MccpRelcPlanOutCounter15_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter15_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter15_Object = MibTableColumn
mccpRelcPlanOutCounter15 = _MccpRelcPlanOutCounter15_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 17),
    _MccpRelcPlanOutCounter15_Type()
)
mccpRelcPlanOutCounter15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter15.setStatus("current")


class _MccpRelcPlanOutCounter16_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter16_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter16_Object = MibTableColumn
mccpRelcPlanOutCounter16 = _MccpRelcPlanOutCounter16_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 18),
    _MccpRelcPlanOutCounter16_Type()
)
mccpRelcPlanOutCounter16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter16.setStatus("current")


class _MccpRelcPlanOutCounter17_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter17_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter17_Object = MibTableColumn
mccpRelcPlanOutCounter17 = _MccpRelcPlanOutCounter17_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 19),
    _MccpRelcPlanOutCounter17_Type()
)
mccpRelcPlanOutCounter17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter17.setStatus("current")


class _MccpRelcPlanOutCounter18_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter18_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter18_Object = MibTableColumn
mccpRelcPlanOutCounter18 = _MccpRelcPlanOutCounter18_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 20),
    _MccpRelcPlanOutCounter18_Type()
)
mccpRelcPlanOutCounter18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter18.setStatus("current")


class _MccpRelcPlanOutCounter19_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter19_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter19_Object = MibTableColumn
mccpRelcPlanOutCounter19 = _MccpRelcPlanOutCounter19_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 21),
    _MccpRelcPlanOutCounter19_Type()
)
mccpRelcPlanOutCounter19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter19.setStatus("current")


class _MccpRelcPlanOutCounter20_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter20_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter20_Object = MibTableColumn
mccpRelcPlanOutCounter20 = _MccpRelcPlanOutCounter20_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 22),
    _MccpRelcPlanOutCounter20_Type()
)
mccpRelcPlanOutCounter20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter20.setStatus("current")


class _MccpRelcPlanOutCounter21_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter21_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter21_Object = MibTableColumn
mccpRelcPlanOutCounter21 = _MccpRelcPlanOutCounter21_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 23),
    _MccpRelcPlanOutCounter21_Type()
)
mccpRelcPlanOutCounter21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter21.setStatus("current")


class _MccpRelcPlanOutCounter22_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter22_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter22_Object = MibTableColumn
mccpRelcPlanOutCounter22 = _MccpRelcPlanOutCounter22_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 24),
    _MccpRelcPlanOutCounter22_Type()
)
mccpRelcPlanOutCounter22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter22.setStatus("current")


class _MccpRelcPlanOutCounter23_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter23_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter23_Object = MibTableColumn
mccpRelcPlanOutCounter23 = _MccpRelcPlanOutCounter23_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 25),
    _MccpRelcPlanOutCounter23_Type()
)
mccpRelcPlanOutCounter23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter23.setStatus("current")


class _MccpRelcPlanOutCounter24_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter24_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter24_Object = MibTableColumn
mccpRelcPlanOutCounter24 = _MccpRelcPlanOutCounter24_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 26),
    _MccpRelcPlanOutCounter24_Type()
)
mccpRelcPlanOutCounter24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter24.setStatus("current")


class _MccpRelcPlanOutCounter25_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter25_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter25_Object = MibTableColumn
mccpRelcPlanOutCounter25 = _MccpRelcPlanOutCounter25_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 27),
    _MccpRelcPlanOutCounter25_Type()
)
mccpRelcPlanOutCounter25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter25.setStatus("current")


class _MccpRelcPlanOutCounter26_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter26 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter26_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter26_Object = MibTableColumn
mccpRelcPlanOutCounter26 = _MccpRelcPlanOutCounter26_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 28),
    _MccpRelcPlanOutCounter26_Type()
)
mccpRelcPlanOutCounter26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter26.setStatus("current")


class _MccpRelcPlanOutCounter27_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter27 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter27_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter27_Object = MibTableColumn
mccpRelcPlanOutCounter27 = _MccpRelcPlanOutCounter27_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 29),
    _MccpRelcPlanOutCounter27_Type()
)
mccpRelcPlanOutCounter27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter27.setStatus("current")


class _MccpRelcPlanOutCounter28_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter28 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter28_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter28_Object = MibTableColumn
mccpRelcPlanOutCounter28 = _MccpRelcPlanOutCounter28_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 30),
    _MccpRelcPlanOutCounter28_Type()
)
mccpRelcPlanOutCounter28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter28.setStatus("current")


class _MccpRelcPlanOutCounter29_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter29 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter29_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter29_Object = MibTableColumn
mccpRelcPlanOutCounter29 = _MccpRelcPlanOutCounter29_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 31),
    _MccpRelcPlanOutCounter29_Type()
)
mccpRelcPlanOutCounter29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter29.setStatus("current")


class _MccpRelcPlanOutCounter30_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter30 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter30_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter30_Object = MibTableColumn
mccpRelcPlanOutCounter30 = _MccpRelcPlanOutCounter30_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 32),
    _MccpRelcPlanOutCounter30_Type()
)
mccpRelcPlanOutCounter30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter30.setStatus("current")


class _MccpRelcPlanOutCounter31_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter31 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter31_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter31_Object = MibTableColumn
mccpRelcPlanOutCounter31 = _MccpRelcPlanOutCounter31_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 33),
    _MccpRelcPlanOutCounter31_Type()
)
mccpRelcPlanOutCounter31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter31.setStatus("current")


class _MccpRelcPlanOutCounter32_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter32_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter32_Object = MibTableColumn
mccpRelcPlanOutCounter32 = _MccpRelcPlanOutCounter32_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 34),
    _MccpRelcPlanOutCounter32_Type()
)
mccpRelcPlanOutCounter32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter32.setStatus("current")


class _MccpRelcPlanOutCounter33_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter33 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter33_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter33_Object = MibTableColumn
mccpRelcPlanOutCounter33 = _MccpRelcPlanOutCounter33_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 35),
    _MccpRelcPlanOutCounter33_Type()
)
mccpRelcPlanOutCounter33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter33.setStatus("current")


class _MccpRelcPlanOutCounter34_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter34 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter34_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter34_Object = MibTableColumn
mccpRelcPlanOutCounter34 = _MccpRelcPlanOutCounter34_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 36),
    _MccpRelcPlanOutCounter34_Type()
)
mccpRelcPlanOutCounter34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter34.setStatus("current")


class _MccpRelcPlanOutCounter35_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter35 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter35_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter35_Object = MibTableColumn
mccpRelcPlanOutCounter35 = _MccpRelcPlanOutCounter35_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 37),
    _MccpRelcPlanOutCounter35_Type()
)
mccpRelcPlanOutCounter35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter35.setStatus("current")


class _MccpRelcPlanOutCounter36_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter36 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter36_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter36_Object = MibTableColumn
mccpRelcPlanOutCounter36 = _MccpRelcPlanOutCounter36_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 38),
    _MccpRelcPlanOutCounter36_Type()
)
mccpRelcPlanOutCounter36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter36.setStatus("current")


class _MccpRelcPlanOutCounter37_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter37 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter37_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter37_Object = MibTableColumn
mccpRelcPlanOutCounter37 = _MccpRelcPlanOutCounter37_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 39),
    _MccpRelcPlanOutCounter37_Type()
)
mccpRelcPlanOutCounter37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter37.setStatus("current")


class _MccpRelcPlanOutCounter38_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter38 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter38_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter38_Object = MibTableColumn
mccpRelcPlanOutCounter38 = _MccpRelcPlanOutCounter38_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 40),
    _MccpRelcPlanOutCounter38_Type()
)
mccpRelcPlanOutCounter38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter38.setStatus("current")


class _MccpRelcPlanOutCounter39_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter39 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter39_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter39_Object = MibTableColumn
mccpRelcPlanOutCounter39 = _MccpRelcPlanOutCounter39_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 41),
    _MccpRelcPlanOutCounter39_Type()
)
mccpRelcPlanOutCounter39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter39.setStatus("current")


class _MccpRelcPlanOutCounter40_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter40 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter40_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter40_Object = MibTableColumn
mccpRelcPlanOutCounter40 = _MccpRelcPlanOutCounter40_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 42),
    _MccpRelcPlanOutCounter40_Type()
)
mccpRelcPlanOutCounter40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter40.setStatus("current")


class _MccpRelcPlanOutCounter41_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter41 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter41_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter41_Object = MibTableColumn
mccpRelcPlanOutCounter41 = _MccpRelcPlanOutCounter41_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 43),
    _MccpRelcPlanOutCounter41_Type()
)
mccpRelcPlanOutCounter41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter41.setStatus("current")


class _MccpRelcPlanOutCounter42_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter42 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter42_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter42_Object = MibTableColumn
mccpRelcPlanOutCounter42 = _MccpRelcPlanOutCounter42_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 44),
    _MccpRelcPlanOutCounter42_Type()
)
mccpRelcPlanOutCounter42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter42.setStatus("current")


class _MccpRelcPlanOutCounter43_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter43 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter43_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter43_Object = MibTableColumn
mccpRelcPlanOutCounter43 = _MccpRelcPlanOutCounter43_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 45),
    _MccpRelcPlanOutCounter43_Type()
)
mccpRelcPlanOutCounter43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter43.setStatus("current")


class _MccpRelcPlanOutCounter44_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter44 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter44_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter44_Object = MibTableColumn
mccpRelcPlanOutCounter44 = _MccpRelcPlanOutCounter44_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 46),
    _MccpRelcPlanOutCounter44_Type()
)
mccpRelcPlanOutCounter44.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter44.setStatus("current")


class _MccpRelcPlanOutCounter45_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter45 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter45_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter45_Object = MibTableColumn
mccpRelcPlanOutCounter45 = _MccpRelcPlanOutCounter45_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 47),
    _MccpRelcPlanOutCounter45_Type()
)
mccpRelcPlanOutCounter45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter45.setStatus("current")


class _MccpRelcPlanOutCounter46_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter46 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter46_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter46_Object = MibTableColumn
mccpRelcPlanOutCounter46 = _MccpRelcPlanOutCounter46_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 48),
    _MccpRelcPlanOutCounter46_Type()
)
mccpRelcPlanOutCounter46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter46.setStatus("current")


class _MccpRelcPlanOutCounter47_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter47 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter47_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter47_Object = MibTableColumn
mccpRelcPlanOutCounter47 = _MccpRelcPlanOutCounter47_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 49),
    _MccpRelcPlanOutCounter47_Type()
)
mccpRelcPlanOutCounter47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter47.setStatus("current")


class _MccpRelcPlanOutCounter48_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter48 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter48_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter48_Object = MibTableColumn
mccpRelcPlanOutCounter48 = _MccpRelcPlanOutCounter48_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 50),
    _MccpRelcPlanOutCounter48_Type()
)
mccpRelcPlanOutCounter48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter48.setStatus("current")


class _MccpRelcPlanOutCounter49_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter49 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter49_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter49_Object = MibTableColumn
mccpRelcPlanOutCounter49 = _MccpRelcPlanOutCounter49_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 51),
    _MccpRelcPlanOutCounter49_Type()
)
mccpRelcPlanOutCounter49.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter49.setStatus("current")


class _MccpRelcPlanOutCounter50_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter50 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter50_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter50_Object = MibTableColumn
mccpRelcPlanOutCounter50 = _MccpRelcPlanOutCounter50_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 52),
    _MccpRelcPlanOutCounter50_Type()
)
mccpRelcPlanOutCounter50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter50.setStatus("current")


class _MccpRelcPlanOutCounter51_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter51 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter51_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter51_Object = MibTableColumn
mccpRelcPlanOutCounter51 = _MccpRelcPlanOutCounter51_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 53),
    _MccpRelcPlanOutCounter51_Type()
)
mccpRelcPlanOutCounter51.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter51.setStatus("current")


class _MccpRelcPlanOutCounter52_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter52 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter52_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter52_Object = MibTableColumn
mccpRelcPlanOutCounter52 = _MccpRelcPlanOutCounter52_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 54),
    _MccpRelcPlanOutCounter52_Type()
)
mccpRelcPlanOutCounter52.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter52.setStatus("current")


class _MccpRelcPlanOutCounter53_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter53 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter53_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter53_Object = MibTableColumn
mccpRelcPlanOutCounter53 = _MccpRelcPlanOutCounter53_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 55),
    _MccpRelcPlanOutCounter53_Type()
)
mccpRelcPlanOutCounter53.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter53.setStatus("current")


class _MccpRelcPlanOutCounter54_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter54 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter54_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter54_Object = MibTableColumn
mccpRelcPlanOutCounter54 = _MccpRelcPlanOutCounter54_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 56),
    _MccpRelcPlanOutCounter54_Type()
)
mccpRelcPlanOutCounter54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter54.setStatus("current")


class _MccpRelcPlanOutCounter55_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter55 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter55_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter55_Object = MibTableColumn
mccpRelcPlanOutCounter55 = _MccpRelcPlanOutCounter55_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 57),
    _MccpRelcPlanOutCounter55_Type()
)
mccpRelcPlanOutCounter55.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter55.setStatus("current")


class _MccpRelcPlanOutCounter56_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter56 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter56_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter56_Object = MibTableColumn
mccpRelcPlanOutCounter56 = _MccpRelcPlanOutCounter56_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 58),
    _MccpRelcPlanOutCounter56_Type()
)
mccpRelcPlanOutCounter56.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter56.setStatus("current")


class _MccpRelcPlanOutCounter57_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter57 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter57_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter57_Object = MibTableColumn
mccpRelcPlanOutCounter57 = _MccpRelcPlanOutCounter57_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 59),
    _MccpRelcPlanOutCounter57_Type()
)
mccpRelcPlanOutCounter57.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter57.setStatus("current")


class _MccpRelcPlanOutCounter58_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter58 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter58_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter58_Object = MibTableColumn
mccpRelcPlanOutCounter58 = _MccpRelcPlanOutCounter58_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 60),
    _MccpRelcPlanOutCounter58_Type()
)
mccpRelcPlanOutCounter58.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter58.setStatus("current")


class _MccpRelcPlanOutCounter59_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter59 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter59_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter59_Object = MibTableColumn
mccpRelcPlanOutCounter59 = _MccpRelcPlanOutCounter59_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 61),
    _MccpRelcPlanOutCounter59_Type()
)
mccpRelcPlanOutCounter59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter59.setStatus("current")


class _MccpRelcPlanOutCounter60_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter60 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter60_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter60_Object = MibTableColumn
mccpRelcPlanOutCounter60 = _MccpRelcPlanOutCounter60_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 62),
    _MccpRelcPlanOutCounter60_Type()
)
mccpRelcPlanOutCounter60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter60.setStatus("current")


class _MccpRelcPlanOutCounter61_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter61 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter61_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter61_Object = MibTableColumn
mccpRelcPlanOutCounter61 = _MccpRelcPlanOutCounter61_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 63),
    _MccpRelcPlanOutCounter61_Type()
)
mccpRelcPlanOutCounter61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter61.setStatus("current")


class _MccpRelcPlanOutCounter62_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter62 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter62_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter62_Object = MibTableColumn
mccpRelcPlanOutCounter62 = _MccpRelcPlanOutCounter62_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 64),
    _MccpRelcPlanOutCounter62_Type()
)
mccpRelcPlanOutCounter62.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter62.setStatus("current")


class _MccpRelcPlanOutCounter63_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter63 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter63_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter63_Object = MibTableColumn
mccpRelcPlanOutCounter63 = _MccpRelcPlanOutCounter63_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 65),
    _MccpRelcPlanOutCounter63_Type()
)
mccpRelcPlanOutCounter63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter63.setStatus("current")


class _MccpRelcPlanOutCounter64_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter64 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter64_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter64_Object = MibTableColumn
mccpRelcPlanOutCounter64 = _MccpRelcPlanOutCounter64_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 66),
    _MccpRelcPlanOutCounter64_Type()
)
mccpRelcPlanOutCounter64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter64.setStatus("current")


class _MccpRelcPlanOutCounter65_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter65 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter65_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter65_Object = MibTableColumn
mccpRelcPlanOutCounter65 = _MccpRelcPlanOutCounter65_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 67),
    _MccpRelcPlanOutCounter65_Type()
)
mccpRelcPlanOutCounter65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter65.setStatus("current")


class _MccpRelcPlanOutCounter66_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter66 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter66_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter66_Object = MibTableColumn
mccpRelcPlanOutCounter66 = _MccpRelcPlanOutCounter66_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 68),
    _MccpRelcPlanOutCounter66_Type()
)
mccpRelcPlanOutCounter66.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter66.setStatus("current")


class _MccpRelcPlanOutCounter67_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter67 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter67_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter67_Object = MibTableColumn
mccpRelcPlanOutCounter67 = _MccpRelcPlanOutCounter67_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 69),
    _MccpRelcPlanOutCounter67_Type()
)
mccpRelcPlanOutCounter67.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter67.setStatus("current")


class _MccpRelcPlanOutCounter68_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter68 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter68_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter68_Object = MibTableColumn
mccpRelcPlanOutCounter68 = _MccpRelcPlanOutCounter68_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 70),
    _MccpRelcPlanOutCounter68_Type()
)
mccpRelcPlanOutCounter68.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter68.setStatus("current")


class _MccpRelcPlanOutCounter69_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter69 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter69_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter69_Object = MibTableColumn
mccpRelcPlanOutCounter69 = _MccpRelcPlanOutCounter69_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 71),
    _MccpRelcPlanOutCounter69_Type()
)
mccpRelcPlanOutCounter69.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter69.setStatus("current")


class _MccpRelcPlanOutCounter70_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter70 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter70_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter70_Object = MibTableColumn
mccpRelcPlanOutCounter70 = _MccpRelcPlanOutCounter70_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 72),
    _MccpRelcPlanOutCounter70_Type()
)
mccpRelcPlanOutCounter70.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter70.setStatus("current")


class _MccpRelcPlanOutCounter71_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter71 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter71_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter71_Object = MibTableColumn
mccpRelcPlanOutCounter71 = _MccpRelcPlanOutCounter71_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 73),
    _MccpRelcPlanOutCounter71_Type()
)
mccpRelcPlanOutCounter71.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter71.setStatus("current")


class _MccpRelcPlanOutCounter72_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter72 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter72_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter72_Object = MibTableColumn
mccpRelcPlanOutCounter72 = _MccpRelcPlanOutCounter72_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 74),
    _MccpRelcPlanOutCounter72_Type()
)
mccpRelcPlanOutCounter72.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter72.setStatus("current")


class _MccpRelcPlanOutCounter73_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter73 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter73_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter73_Object = MibTableColumn
mccpRelcPlanOutCounter73 = _MccpRelcPlanOutCounter73_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 75),
    _MccpRelcPlanOutCounter73_Type()
)
mccpRelcPlanOutCounter73.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter73.setStatus("current")


class _MccpRelcPlanOutCounter74_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter74 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter74_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter74_Object = MibTableColumn
mccpRelcPlanOutCounter74 = _MccpRelcPlanOutCounter74_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 76),
    _MccpRelcPlanOutCounter74_Type()
)
mccpRelcPlanOutCounter74.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter74.setStatus("current")


class _MccpRelcPlanOutCounter75_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter75 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter75_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter75_Object = MibTableColumn
mccpRelcPlanOutCounter75 = _MccpRelcPlanOutCounter75_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 77),
    _MccpRelcPlanOutCounter75_Type()
)
mccpRelcPlanOutCounter75.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter75.setStatus("current")


class _MccpRelcPlanOutCounter76_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter76 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter76_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter76_Object = MibTableColumn
mccpRelcPlanOutCounter76 = _MccpRelcPlanOutCounter76_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 78),
    _MccpRelcPlanOutCounter76_Type()
)
mccpRelcPlanOutCounter76.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter76.setStatus("current")


class _MccpRelcPlanOutCounter77_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter77 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter77_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter77_Object = MibTableColumn
mccpRelcPlanOutCounter77 = _MccpRelcPlanOutCounter77_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 79),
    _MccpRelcPlanOutCounter77_Type()
)
mccpRelcPlanOutCounter77.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter77.setStatus("current")


class _MccpRelcPlanOutCounter78_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter78 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter78_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter78_Object = MibTableColumn
mccpRelcPlanOutCounter78 = _MccpRelcPlanOutCounter78_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 80),
    _MccpRelcPlanOutCounter78_Type()
)
mccpRelcPlanOutCounter78.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter78.setStatus("current")


class _MccpRelcPlanOutCounter79_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter79 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter79_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter79_Object = MibTableColumn
mccpRelcPlanOutCounter79 = _MccpRelcPlanOutCounter79_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 81),
    _MccpRelcPlanOutCounter79_Type()
)
mccpRelcPlanOutCounter79.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter79.setStatus("current")


class _MccpRelcPlanOutCounter80_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter80 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter80_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter80_Object = MibTableColumn
mccpRelcPlanOutCounter80 = _MccpRelcPlanOutCounter80_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 82),
    _MccpRelcPlanOutCounter80_Type()
)
mccpRelcPlanOutCounter80.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter80.setStatus("current")


class _MccpRelcPlanOutCounter81_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter81 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter81_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter81_Object = MibTableColumn
mccpRelcPlanOutCounter81 = _MccpRelcPlanOutCounter81_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 83),
    _MccpRelcPlanOutCounter81_Type()
)
mccpRelcPlanOutCounter81.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter81.setStatus("current")


class _MccpRelcPlanOutCounter82_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter82_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter82_Object = MibTableColumn
mccpRelcPlanOutCounter82 = _MccpRelcPlanOutCounter82_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 84),
    _MccpRelcPlanOutCounter82_Type()
)
mccpRelcPlanOutCounter82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter82.setStatus("current")


class _MccpRelcPlanOutCounter83_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter83 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter83_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter83_Object = MibTableColumn
mccpRelcPlanOutCounter83 = _MccpRelcPlanOutCounter83_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 85),
    _MccpRelcPlanOutCounter83_Type()
)
mccpRelcPlanOutCounter83.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter83.setStatus("current")


class _MccpRelcPlanOutCounter84_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter84 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter84_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter84_Object = MibTableColumn
mccpRelcPlanOutCounter84 = _MccpRelcPlanOutCounter84_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 86),
    _MccpRelcPlanOutCounter84_Type()
)
mccpRelcPlanOutCounter84.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter84.setStatus("current")


class _MccpRelcPlanOutCounter85_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter85 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter85_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter85_Object = MibTableColumn
mccpRelcPlanOutCounter85 = _MccpRelcPlanOutCounter85_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 87),
    _MccpRelcPlanOutCounter85_Type()
)
mccpRelcPlanOutCounter85.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter85.setStatus("current")


class _MccpRelcPlanOutCounter86_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter86 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter86_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter86_Object = MibTableColumn
mccpRelcPlanOutCounter86 = _MccpRelcPlanOutCounter86_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 88),
    _MccpRelcPlanOutCounter86_Type()
)
mccpRelcPlanOutCounter86.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter86.setStatus("current")


class _MccpRelcPlanOutCounter87_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter87 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter87_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter87_Object = MibTableColumn
mccpRelcPlanOutCounter87 = _MccpRelcPlanOutCounter87_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 89),
    _MccpRelcPlanOutCounter87_Type()
)
mccpRelcPlanOutCounter87.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter87.setStatus("current")


class _MccpRelcPlanOutCounter88_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter88 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter88_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter88_Object = MibTableColumn
mccpRelcPlanOutCounter88 = _MccpRelcPlanOutCounter88_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 90),
    _MccpRelcPlanOutCounter88_Type()
)
mccpRelcPlanOutCounter88.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter88.setStatus("current")


class _MccpRelcPlanOutCounter89_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter89 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter89_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter89_Object = MibTableColumn
mccpRelcPlanOutCounter89 = _MccpRelcPlanOutCounter89_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 91),
    _MccpRelcPlanOutCounter89_Type()
)
mccpRelcPlanOutCounter89.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter89.setStatus("current")


class _MccpRelcPlanOutCounter90_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter90 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter90_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter90_Object = MibTableColumn
mccpRelcPlanOutCounter90 = _MccpRelcPlanOutCounter90_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 92),
    _MccpRelcPlanOutCounter90_Type()
)
mccpRelcPlanOutCounter90.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter90.setStatus("current")


class _MccpRelcPlanOutCounter91_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter91 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter91_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter91_Object = MibTableColumn
mccpRelcPlanOutCounter91 = _MccpRelcPlanOutCounter91_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 93),
    _MccpRelcPlanOutCounter91_Type()
)
mccpRelcPlanOutCounter91.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter91.setStatus("current")


class _MccpRelcPlanOutCounter92_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter92 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter92_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter92_Object = MibTableColumn
mccpRelcPlanOutCounter92 = _MccpRelcPlanOutCounter92_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 94),
    _MccpRelcPlanOutCounter92_Type()
)
mccpRelcPlanOutCounter92.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter92.setStatus("current")


class _MccpRelcPlanOutCounter93_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter93 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter93_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter93_Object = MibTableColumn
mccpRelcPlanOutCounter93 = _MccpRelcPlanOutCounter93_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 95),
    _MccpRelcPlanOutCounter93_Type()
)
mccpRelcPlanOutCounter93.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter93.setStatus("current")


class _MccpRelcPlanOutCounter94_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter94 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter94_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter94_Object = MibTableColumn
mccpRelcPlanOutCounter94 = _MccpRelcPlanOutCounter94_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 96),
    _MccpRelcPlanOutCounter94_Type()
)
mccpRelcPlanOutCounter94.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter94.setStatus("current")


class _MccpRelcPlanOutCounter95_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter95 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter95_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter95_Object = MibTableColumn
mccpRelcPlanOutCounter95 = _MccpRelcPlanOutCounter95_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 97),
    _MccpRelcPlanOutCounter95_Type()
)
mccpRelcPlanOutCounter95.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter95.setStatus("current")


class _MccpRelcPlanOutCounter96_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter96 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter96_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter96_Object = MibTableColumn
mccpRelcPlanOutCounter96 = _MccpRelcPlanOutCounter96_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 98),
    _MccpRelcPlanOutCounter96_Type()
)
mccpRelcPlanOutCounter96.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter96.setStatus("current")


class _MccpRelcPlanOutCounter97_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter97 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter97_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter97_Object = MibTableColumn
mccpRelcPlanOutCounter97 = _MccpRelcPlanOutCounter97_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 99),
    _MccpRelcPlanOutCounter97_Type()
)
mccpRelcPlanOutCounter97.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter97.setStatus("current")


class _MccpRelcPlanOutCounter98_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter98 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter98_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter98_Object = MibTableColumn
mccpRelcPlanOutCounter98 = _MccpRelcPlanOutCounter98_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 100),
    _MccpRelcPlanOutCounter98_Type()
)
mccpRelcPlanOutCounter98.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter98.setStatus("current")


class _MccpRelcPlanOutCounter99_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter99 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter99_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter99_Object = MibTableColumn
mccpRelcPlanOutCounter99 = _MccpRelcPlanOutCounter99_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 101),
    _MccpRelcPlanOutCounter99_Type()
)
mccpRelcPlanOutCounter99.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter99.setStatus("current")


class _MccpRelcPlanOutCounter100_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter100 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter100_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter100_Object = MibTableColumn
mccpRelcPlanOutCounter100 = _MccpRelcPlanOutCounter100_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 102),
    _MccpRelcPlanOutCounter100_Type()
)
mccpRelcPlanOutCounter100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter100.setStatus("current")


class _MccpRelcPlanOutCounter101_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter101 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter101_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter101_Object = MibTableColumn
mccpRelcPlanOutCounter101 = _MccpRelcPlanOutCounter101_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 103),
    _MccpRelcPlanOutCounter101_Type()
)
mccpRelcPlanOutCounter101.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter101.setStatus("current")


class _MccpRelcPlanOutCounter102_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter102 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter102_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter102_Object = MibTableColumn
mccpRelcPlanOutCounter102 = _MccpRelcPlanOutCounter102_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 104),
    _MccpRelcPlanOutCounter102_Type()
)
mccpRelcPlanOutCounter102.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter102.setStatus("current")


class _MccpRelcPlanOutCounter103_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter103 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter103_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter103_Object = MibTableColumn
mccpRelcPlanOutCounter103 = _MccpRelcPlanOutCounter103_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 105),
    _MccpRelcPlanOutCounter103_Type()
)
mccpRelcPlanOutCounter103.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter103.setStatus("current")


class _MccpRelcPlanOutCounter104_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter104 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter104_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter104_Object = MibTableColumn
mccpRelcPlanOutCounter104 = _MccpRelcPlanOutCounter104_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 106),
    _MccpRelcPlanOutCounter104_Type()
)
mccpRelcPlanOutCounter104.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter104.setStatus("current")


class _MccpRelcPlanOutCounter105_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter105 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter105_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter105_Object = MibTableColumn
mccpRelcPlanOutCounter105 = _MccpRelcPlanOutCounter105_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 107),
    _MccpRelcPlanOutCounter105_Type()
)
mccpRelcPlanOutCounter105.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter105.setStatus("current")


class _MccpRelcPlanOutCounter106_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter106 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter106_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter106_Object = MibTableColumn
mccpRelcPlanOutCounter106 = _MccpRelcPlanOutCounter106_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 108),
    _MccpRelcPlanOutCounter106_Type()
)
mccpRelcPlanOutCounter106.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter106.setStatus("current")


class _MccpRelcPlanOutCounter107_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter107 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter107_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter107_Object = MibTableColumn
mccpRelcPlanOutCounter107 = _MccpRelcPlanOutCounter107_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 109),
    _MccpRelcPlanOutCounter107_Type()
)
mccpRelcPlanOutCounter107.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter107.setStatus("current")


class _MccpRelcPlanOutCounter108_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter108 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter108_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter108_Object = MibTableColumn
mccpRelcPlanOutCounter108 = _MccpRelcPlanOutCounter108_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 110),
    _MccpRelcPlanOutCounter108_Type()
)
mccpRelcPlanOutCounter108.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter108.setStatus("current")


class _MccpRelcPlanOutCounter109_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter109 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter109_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter109_Object = MibTableColumn
mccpRelcPlanOutCounter109 = _MccpRelcPlanOutCounter109_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 111),
    _MccpRelcPlanOutCounter109_Type()
)
mccpRelcPlanOutCounter109.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter109.setStatus("current")


class _MccpRelcPlanOutCounter110_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter110 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter110_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter110_Object = MibTableColumn
mccpRelcPlanOutCounter110 = _MccpRelcPlanOutCounter110_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 112),
    _MccpRelcPlanOutCounter110_Type()
)
mccpRelcPlanOutCounter110.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter110.setStatus("current")


class _MccpRelcPlanOutCounter111_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter111 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter111_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter111_Object = MibTableColumn
mccpRelcPlanOutCounter111 = _MccpRelcPlanOutCounter111_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 113),
    _MccpRelcPlanOutCounter111_Type()
)
mccpRelcPlanOutCounter111.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter111.setStatus("current")


class _MccpRelcPlanOutCounter112_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter112 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter112_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter112_Object = MibTableColumn
mccpRelcPlanOutCounter112 = _MccpRelcPlanOutCounter112_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 114),
    _MccpRelcPlanOutCounter112_Type()
)
mccpRelcPlanOutCounter112.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter112.setStatus("current")


class _MccpRelcPlanOutCounter113_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter113 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter113_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter113_Object = MibTableColumn
mccpRelcPlanOutCounter113 = _MccpRelcPlanOutCounter113_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 115),
    _MccpRelcPlanOutCounter113_Type()
)
mccpRelcPlanOutCounter113.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter113.setStatus("current")


class _MccpRelcPlanOutCounter114_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter114 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter114_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter114_Object = MibTableColumn
mccpRelcPlanOutCounter114 = _MccpRelcPlanOutCounter114_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 116),
    _MccpRelcPlanOutCounter114_Type()
)
mccpRelcPlanOutCounter114.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter114.setStatus("current")


class _MccpRelcPlanOutCounter115_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter115 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter115_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter115_Object = MibTableColumn
mccpRelcPlanOutCounter115 = _MccpRelcPlanOutCounter115_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 117),
    _MccpRelcPlanOutCounter115_Type()
)
mccpRelcPlanOutCounter115.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter115.setStatus("current")


class _MccpRelcPlanOutCounter116_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter116 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter116_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter116_Object = MibTableColumn
mccpRelcPlanOutCounter116 = _MccpRelcPlanOutCounter116_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 118),
    _MccpRelcPlanOutCounter116_Type()
)
mccpRelcPlanOutCounter116.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter116.setStatus("current")


class _MccpRelcPlanOutCounter117_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter117 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter117_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter117_Object = MibTableColumn
mccpRelcPlanOutCounter117 = _MccpRelcPlanOutCounter117_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 119),
    _MccpRelcPlanOutCounter117_Type()
)
mccpRelcPlanOutCounter117.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter117.setStatus("current")


class _MccpRelcPlanOutCounter118_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter118 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter118_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter118_Object = MibTableColumn
mccpRelcPlanOutCounter118 = _MccpRelcPlanOutCounter118_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 120),
    _MccpRelcPlanOutCounter118_Type()
)
mccpRelcPlanOutCounter118.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter118.setStatus("current")


class _MccpRelcPlanOutCounter119_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter119 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter119_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter119_Object = MibTableColumn
mccpRelcPlanOutCounter119 = _MccpRelcPlanOutCounter119_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 121),
    _MccpRelcPlanOutCounter119_Type()
)
mccpRelcPlanOutCounter119.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter119.setStatus("current")


class _MccpRelcPlanOutCounter120_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter120 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter120_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter120_Object = MibTableColumn
mccpRelcPlanOutCounter120 = _MccpRelcPlanOutCounter120_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 122),
    _MccpRelcPlanOutCounter120_Type()
)
mccpRelcPlanOutCounter120.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter120.setStatus("current")


class _MccpRelcPlanOutCounter121_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter121 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter121_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter121_Object = MibTableColumn
mccpRelcPlanOutCounter121 = _MccpRelcPlanOutCounter121_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 123),
    _MccpRelcPlanOutCounter121_Type()
)
mccpRelcPlanOutCounter121.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter121.setStatus("current")


class _MccpRelcPlanOutCounter122_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter122 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter122_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter122_Object = MibTableColumn
mccpRelcPlanOutCounter122 = _MccpRelcPlanOutCounter122_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 124),
    _MccpRelcPlanOutCounter122_Type()
)
mccpRelcPlanOutCounter122.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter122.setStatus("current")


class _MccpRelcPlanOutCounter123_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter123 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter123_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter123_Object = MibTableColumn
mccpRelcPlanOutCounter123 = _MccpRelcPlanOutCounter123_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 125),
    _MccpRelcPlanOutCounter123_Type()
)
mccpRelcPlanOutCounter123.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter123.setStatus("current")


class _MccpRelcPlanOutCounter124_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter124 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter124_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter124_Object = MibTableColumn
mccpRelcPlanOutCounter124 = _MccpRelcPlanOutCounter124_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 126),
    _MccpRelcPlanOutCounter124_Type()
)
mccpRelcPlanOutCounter124.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter124.setStatus("current")


class _MccpRelcPlanOutCounter125_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter125 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter125_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter125_Object = MibTableColumn
mccpRelcPlanOutCounter125 = _MccpRelcPlanOutCounter125_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 127),
    _MccpRelcPlanOutCounter125_Type()
)
mccpRelcPlanOutCounter125.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter125.setStatus("current")


class _MccpRelcPlanOutCounter126_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter126 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter126_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter126_Object = MibTableColumn
mccpRelcPlanOutCounter126 = _MccpRelcPlanOutCounter126_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 128),
    _MccpRelcPlanOutCounter126_Type()
)
mccpRelcPlanOutCounter126.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter126.setStatus("current")


class _MccpRelcPlanOutCounter127_Type(Integer32):
    """Custom type mccpRelcPlanOutCounter127 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MccpRelcPlanOutCounter127_Type.__name__ = "Integer32"
_MccpRelcPlanOutCounter127_Object = MibTableColumn
mccpRelcPlanOutCounter127 = _MccpRelcPlanOutCounter127_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 31, 1, 129),
    _MccpRelcPlanOutCounter127_Type()
)
mccpRelcPlanOutCounter127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mccpRelcPlanOutCounter127.setStatus("current")
_MccpService_ObjectIdentity = ObjectIdentity
mccpService = _MccpService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 50)
)
_MccpHumanLogOnOff_Type = MccpLogHumanState
_MccpHumanLogOnOff_Object = MibScalar
mccpHumanLogOnOff = _MccpHumanLogOnOff_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 50, 1),
    _MccpHumanLogOnOff_Type()
)
mccpHumanLogOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mccpHumanLogOnOff.setStatus("current")
_MccpCdrFileFlushStatus_Type = MccpCdrFileFlushStatusType
_MccpCdrFileFlushStatus_Object = MibScalar
mccpCdrFileFlushStatus = _MccpCdrFileFlushStatus_Object(
    (1, 3, 6, 1, 4, 1, 34300, 1, 4, 51),
    _MccpCdrFileFlushStatus_Type()
)
mccpCdrFileFlushStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mccpCdrFileFlushStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MCCP",
    **{"MccpLogHumanState": MccpLogHumanState,
       "MccpCdrFileFlushStatusType": MccpCdrFileFlushStatusType,
       "mccp": mccp,
       "mccpDevName": mccpDevName,
       "mccpDevType": mccpDevType,
       "mccpDevCfgBuild": mccpDevCfgBuild,
       "mccpDevCfgSyncSource": mccpDevCfgSyncSource,
       "mccpGlobalAlarm": mccpGlobalAlarm,
       "mccpJournalQuery": mccpJournalQuery,
       "mccpMasterMode": mccpMasterMode,
       "mccpFreeSpace": mccpFreeSpace,
       "mccpFreeRam": mccpFreeRam,
       "mccpTgStatInTable": mccpTgStatInTable,
       "mccpTgStatInEntry": mccpTgStatInEntry,
       "mccpTgInIndex": mccpTgInIndex,
       "mccpTgInId": mccpTgInId,
       "mccpTgInCounter0": mccpTgInCounter0,
       "mccpTgInCounter1": mccpTgInCounter1,
       "mccpTgInCounter2": mccpTgInCounter2,
       "mccpTgInCounter3": mccpTgInCounter3,
       "mccpTgInCounter4": mccpTgInCounter4,
       "mccpTgInCounter5": mccpTgInCounter5,
       "mccpTgInCounter6": mccpTgInCounter6,
       "mccpTgInCounter7": mccpTgInCounter7,
       "mccpTgInCounter8": mccpTgInCounter8,
       "mccpTgInCounter9": mccpTgInCounter9,
       "mccpTgInCounter10": mccpTgInCounter10,
       "mccpTgStatOutTable": mccpTgStatOutTable,
       "mccpTgStatOutEntry": mccpTgStatOutEntry,
       "mccpTgOutIndex": mccpTgOutIndex,
       "mccpTgOutId": mccpTgOutId,
       "mccpTgOutCounter0": mccpTgOutCounter0,
       "mccpTgOutCounter1": mccpTgOutCounter1,
       "mccpTgOutCounter2": mccpTgOutCounter2,
       "mccpTgOutCounter3": mccpTgOutCounter3,
       "mccpTgOutCounter4": mccpTgOutCounter4,
       "mccpTgOutCounter5": mccpTgOutCounter5,
       "mccpTgOutCounter6": mccpTgOutCounter6,
       "mccpTgOutCounter7": mccpTgOutCounter7,
       "mccpTgOutCounter8": mccpTgOutCounter8,
       "mccpTgOutCounter9": mccpTgOutCounter9,
       "mccpTgOutCounter10": mccpTgOutCounter10,
       "mccpTgStatTrInTable": mccpTgStatTrInTable,
       "mccpTgStatTrInEntry": mccpTgStatTrInEntry,
       "mccpTgTrInIndex": mccpTgTrInIndex,
       "mccpTgTrInId": mccpTgTrInId,
       "mccpTgTrInCounter0": mccpTgTrInCounter0,
       "mccpTgTrInCounter1": mccpTgTrInCounter1,
       "mccpTgTrInCounter2": mccpTgTrInCounter2,
       "mccpTgTrInCounter3": mccpTgTrInCounter3,
       "mccpTgTrInCounter4": mccpTgTrInCounter4,
       "mccpTgTrInCounter5": mccpTgTrInCounter5,
       "mccpTgTrInCounter6": mccpTgTrInCounter6,
       "mccpTgTrInCounter7": mccpTgTrInCounter7,
       "mccpTgTrInCounter8": mccpTgTrInCounter8,
       "mccpTgTrInCounter9": mccpTgTrInCounter9,
       "mccpTgTrInCounter10": mccpTgTrInCounter10,
       "mccpTgStatTrOutTable": mccpTgStatTrOutTable,
       "mccpTgStatTrOutEntry": mccpTgStatTrOutEntry,
       "mccpTgTrOutIndex": mccpTgTrOutIndex,
       "mccpTgTrOutId": mccpTgTrOutId,
       "mccpTgTrOutCounter0": mccpTgTrOutCounter0,
       "mccpTgTrOutCounter1": mccpTgTrOutCounter1,
       "mccpTgTrOutCounter2": mccpTgTrOutCounter2,
       "mccpTgTrOutCounter3": mccpTgTrOutCounter3,
       "mccpTgTrOutCounter4": mccpTgTrOutCounter4,
       "mccpTgTrOutCounter5": mccpTgTrOutCounter5,
       "mccpTgTrOutCounter6": mccpTgTrOutCounter6,
       "mccpTgTrOutCounter7": mccpTgTrOutCounter7,
       "mccpTgTrOutCounter8": mccpTgTrOutCounter8,
       "mccpTgTrOutCounter9": mccpTgTrOutCounter9,
       "mccpTgTrOutCounter10": mccpTgTrOutCounter10,
       "mccpTgUsageTable": mccpTgUsageTable,
       "mccpTgUsageEntry": mccpTgUsageEntry,
       "mccpTgUsageIndex": mccpTgUsageIndex,
       "mccpTgUsageId": mccpTgUsageId,
       "mccpTgUsageCounter0": mccpTgUsageCounter0,
       "mccpTgUsageCounter1": mccpTgUsageCounter1,
       "mccpTgUsageCounter2": mccpTgUsageCounter2,
       "mccpTgUsageCounter3": mccpTgUsageCounter3,
       "mccpTgUsageCounter4": mccpTgUsageCounter4,
       "mccpPlanStatInTable": mccpPlanStatInTable,
       "mccpPlanStatInEntry": mccpPlanStatInEntry,
       "mccpPlanInIndex": mccpPlanInIndex,
       "mccpPlanInCounter0": mccpPlanInCounter0,
       "mccpPlanInCounter1": mccpPlanInCounter1,
       "mccpPlanInCounter2": mccpPlanInCounter2,
       "mccpPlanInCounter3": mccpPlanInCounter3,
       "mccpPlanInCounter4": mccpPlanInCounter4,
       "mccpPlanInCounter5": mccpPlanInCounter5,
       "mccpPlanInCounter6": mccpPlanInCounter6,
       "mccpPlanInCounter7": mccpPlanInCounter7,
       "mccpPlanInCounter8": mccpPlanInCounter8,
       "mccpPlanInCounter9": mccpPlanInCounter9,
       "mccpPlanInCounter10": mccpPlanInCounter10,
       "mccpPlanStatOutTable": mccpPlanStatOutTable,
       "mccpPlanStatOutEntry": mccpPlanStatOutEntry,
       "mccpPlanOutIndex": mccpPlanOutIndex,
       "mccpPlanOutCounter0": mccpPlanOutCounter0,
       "mccpPlanOutCounter1": mccpPlanOutCounter1,
       "mccpPlanOutCounter2": mccpPlanOutCounter2,
       "mccpPlanOutCounter3": mccpPlanOutCounter3,
       "mccpPlanOutCounter4": mccpPlanOutCounter4,
       "mccpPlanOutCounter5": mccpPlanOutCounter5,
       "mccpPlanOutCounter6": mccpPlanOutCounter6,
       "mccpPlanOutCounter7": mccpPlanOutCounter7,
       "mccpPlanOutCounter8": mccpPlanOutCounter8,
       "mccpPlanOutCounter9": mccpPlanOutCounter9,
       "mccpPlanOutCounter10": mccpPlanOutCounter10,
       "mccpPlanUsageTable": mccpPlanUsageTable,
       "mccpPlanUsageEntry": mccpPlanUsageEntry,
       "mccpPlanUsageIndex": mccpPlanUsageIndex,
       "mccpPlanUsageCounter0": mccpPlanUsageCounter0,
       "mccpPlanUsageCounter1": mccpPlanUsageCounter1,
       "mccpPlanUsageCounter2": mccpPlanUsageCounter2,
       "mccpPlanUsageCounter3": mccpPlanUsageCounter3,
       "mccpPlanUsageCounter4": mccpPlanUsageCounter4,
       "mccpSubStatInTable": mccpSubStatInTable,
       "mccpSubStatInEntry": mccpSubStatInEntry,
       "mccpSubInIndex": mccpSubInIndex,
       "mccpSubInCounter0": mccpSubInCounter0,
       "mccpSubInCounter1": mccpSubInCounter1,
       "mccpSubInCounter2": mccpSubInCounter2,
       "mccpSubInCounter3": mccpSubInCounter3,
       "mccpSubInCounter4": mccpSubInCounter4,
       "mccpSubInCounter5": mccpSubInCounter5,
       "mccpSubInCounter6": mccpSubInCounter6,
       "mccpSubInCounter7": mccpSubInCounter7,
       "mccpSubInCounter8": mccpSubInCounter8,
       "mccpSubInCounter9": mccpSubInCounter9,
       "mccpSubInCounter10": mccpSubInCounter10,
       "mccpSubStatOutTable": mccpSubStatOutTable,
       "mccpSubStatOutEntry": mccpSubStatOutEntry,
       "mccpSubOutIndex": mccpSubOutIndex,
       "mccpSubOutCounter0": mccpSubOutCounter0,
       "mccpSubOutCounter1": mccpSubOutCounter1,
       "mccpSubOutCounter2": mccpSubOutCounter2,
       "mccpSubOutCounter3": mccpSubOutCounter3,
       "mccpSubOutCounter4": mccpSubOutCounter4,
       "mccpSubOutCounter5": mccpSubOutCounter5,
       "mccpSubOutCounter6": mccpSubOutCounter6,
       "mccpSubOutCounter7": mccpSubOutCounter7,
       "mccpSubOutCounter8": mccpSubOutCounter8,
       "mccpSubOutCounter9": mccpSubOutCounter9,
       "mccpSubOutCounter10": mccpSubOutCounter10,
       "mccpSubUsageTable": mccpSubUsageTable,
       "mccpSubUsageEntry": mccpSubUsageEntry,
       "mccpSubUsageIndex": mccpSubUsageIndex,
       "mccpSubUsageCounter0": mccpSubUsageCounter0,
       "mccpSubUsageCounter1": mccpSubUsageCounter1,
       "mccpSubUsageCounter2": mccpSubUsageCounter2,
       "mccpSubUsageCounter3": mccpSubUsageCounter3,
       "mccpSubUsageCounter4": mccpSubUsageCounter4,
       "mccpRelcTgInTable": mccpRelcTgInTable,
       "mccpRelcTgInEntry": mccpRelcTgInEntry,
       "mccpRelcTgInIndex": mccpRelcTgInIndex,
       "mccpRelcTgInCounter0": mccpRelcTgInCounter0,
       "mccpRelcTgInCounter1": mccpRelcTgInCounter1,
       "mccpRelcTgInCounter2": mccpRelcTgInCounter2,
       "mccpRelcTgInCounter3": mccpRelcTgInCounter3,
       "mccpRelcTgInCounter4": mccpRelcTgInCounter4,
       "mccpRelcTgInCounter5": mccpRelcTgInCounter5,
       "mccpRelcTgInCounter6": mccpRelcTgInCounter6,
       "mccpRelcTgInCounter7": mccpRelcTgInCounter7,
       "mccpRelcTgInCounter8": mccpRelcTgInCounter8,
       "mccpRelcTgInCounter9": mccpRelcTgInCounter9,
       "mccpRelcTgInCounter10": mccpRelcTgInCounter10,
       "mccpRelcTgInCounter11": mccpRelcTgInCounter11,
       "mccpRelcTgInCounter12": mccpRelcTgInCounter12,
       "mccpRelcTgInCounter13": mccpRelcTgInCounter13,
       "mccpRelcTgInCounter14": mccpRelcTgInCounter14,
       "mccpRelcTgInCounter15": mccpRelcTgInCounter15,
       "mccpRelcTgInCounter16": mccpRelcTgInCounter16,
       "mccpRelcTgInCounter17": mccpRelcTgInCounter17,
       "mccpRelcTgInCounter18": mccpRelcTgInCounter18,
       "mccpRelcTgInCounter19": mccpRelcTgInCounter19,
       "mccpRelcTgInCounter20": mccpRelcTgInCounter20,
       "mccpRelcTgInCounter21": mccpRelcTgInCounter21,
       "mccpRelcTgInCounter22": mccpRelcTgInCounter22,
       "mccpRelcTgInCounter23": mccpRelcTgInCounter23,
       "mccpRelcTgInCounter24": mccpRelcTgInCounter24,
       "mccpRelcTgInCounter25": mccpRelcTgInCounter25,
       "mccpRelcTgInCounter26": mccpRelcTgInCounter26,
       "mccpRelcTgInCounter27": mccpRelcTgInCounter27,
       "mccpRelcTgInCounter28": mccpRelcTgInCounter28,
       "mccpRelcTgInCounter29": mccpRelcTgInCounter29,
       "mccpRelcTgInCounter30": mccpRelcTgInCounter30,
       "mccpRelcTgInCounter31": mccpRelcTgInCounter31,
       "mccpRelcTgInCounter32": mccpRelcTgInCounter32,
       "mccpRelcTgInCounter33": mccpRelcTgInCounter33,
       "mccpRelcTgInCounter34": mccpRelcTgInCounter34,
       "mccpRelcTgInCounter35": mccpRelcTgInCounter35,
       "mccpRelcTgInCounter36": mccpRelcTgInCounter36,
       "mccpRelcTgInCounter37": mccpRelcTgInCounter37,
       "mccpRelcTgInCounter38": mccpRelcTgInCounter38,
       "mccpRelcTgInCounter39": mccpRelcTgInCounter39,
       "mccpRelcTgInCounter40": mccpRelcTgInCounter40,
       "mccpRelcTgInCounter41": mccpRelcTgInCounter41,
       "mccpRelcTgInCounter42": mccpRelcTgInCounter42,
       "mccpRelcTgInCounter43": mccpRelcTgInCounter43,
       "mccpRelcTgInCounter44": mccpRelcTgInCounter44,
       "mccpRelcTgInCounter45": mccpRelcTgInCounter45,
       "mccpRelcTgInCounter46": mccpRelcTgInCounter46,
       "mccpRelcTgInCounter47": mccpRelcTgInCounter47,
       "mccpRelcTgInCounter48": mccpRelcTgInCounter48,
       "mccpRelcTgInCounter49": mccpRelcTgInCounter49,
       "mccpRelcTgInCounter50": mccpRelcTgInCounter50,
       "mccpRelcTgInCounter51": mccpRelcTgInCounter51,
       "mccpRelcTgInCounter52": mccpRelcTgInCounter52,
       "mccpRelcTgInCounter53": mccpRelcTgInCounter53,
       "mccpRelcTgInCounter54": mccpRelcTgInCounter54,
       "mccpRelcTgInCounter55": mccpRelcTgInCounter55,
       "mccpRelcTgInCounter56": mccpRelcTgInCounter56,
       "mccpRelcTgInCounter57": mccpRelcTgInCounter57,
       "mccpRelcTgInCounter58": mccpRelcTgInCounter58,
       "mccpRelcTgInCounter59": mccpRelcTgInCounter59,
       "mccpRelcTgInCounter60": mccpRelcTgInCounter60,
       "mccpRelcTgInCounter61": mccpRelcTgInCounter61,
       "mccpRelcTgInCounter62": mccpRelcTgInCounter62,
       "mccpRelcTgInCounter63": mccpRelcTgInCounter63,
       "mccpRelcTgInCounter64": mccpRelcTgInCounter64,
       "mccpRelcTgInCounter65": mccpRelcTgInCounter65,
       "mccpRelcTgInCounter66": mccpRelcTgInCounter66,
       "mccpRelcTgInCounter67": mccpRelcTgInCounter67,
       "mccpRelcTgInCounter68": mccpRelcTgInCounter68,
       "mccpRelcTgInCounter69": mccpRelcTgInCounter69,
       "mccpRelcTgInCounter70": mccpRelcTgInCounter70,
       "mccpRelcTgInCounter71": mccpRelcTgInCounter71,
       "mccpRelcTgInCounter72": mccpRelcTgInCounter72,
       "mccpRelcTgInCounter73": mccpRelcTgInCounter73,
       "mccpRelcTgInCounter74": mccpRelcTgInCounter74,
       "mccpRelcTgInCounter75": mccpRelcTgInCounter75,
       "mccpRelcTgInCounter76": mccpRelcTgInCounter76,
       "mccpRelcTgInCounter77": mccpRelcTgInCounter77,
       "mccpRelcTgInCounter78": mccpRelcTgInCounter78,
       "mccpRelcTgInCounter79": mccpRelcTgInCounter79,
       "mccpRelcTgInCounter80": mccpRelcTgInCounter80,
       "mccpRelcTgInCounter81": mccpRelcTgInCounter81,
       "mccpRelcTgInCounter82": mccpRelcTgInCounter82,
       "mccpRelcTgInCounter83": mccpRelcTgInCounter83,
       "mccpRelcTgInCounter84": mccpRelcTgInCounter84,
       "mccpRelcTgInCounter85": mccpRelcTgInCounter85,
       "mccpRelcTgInCounter86": mccpRelcTgInCounter86,
       "mccpRelcTgInCounter87": mccpRelcTgInCounter87,
       "mccpRelcTgInCounter88": mccpRelcTgInCounter88,
       "mccpRelcTgInCounter89": mccpRelcTgInCounter89,
       "mccpRelcTgInCounter90": mccpRelcTgInCounter90,
       "mccpRelcTgInCounter91": mccpRelcTgInCounter91,
       "mccpRelcTgInCounter92": mccpRelcTgInCounter92,
       "mccpRelcTgInCounter93": mccpRelcTgInCounter93,
       "mccpRelcTgInCounter94": mccpRelcTgInCounter94,
       "mccpRelcTgInCounter95": mccpRelcTgInCounter95,
       "mccpRelcTgInCounter96": mccpRelcTgInCounter96,
       "mccpRelcTgInCounter97": mccpRelcTgInCounter97,
       "mccpRelcTgInCounter98": mccpRelcTgInCounter98,
       "mccpRelcTgInCounter99": mccpRelcTgInCounter99,
       "mccpRelcTgInCounter100": mccpRelcTgInCounter100,
       "mccpRelcTgInCounter101": mccpRelcTgInCounter101,
       "mccpRelcTgInCounter102": mccpRelcTgInCounter102,
       "mccpRelcTgInCounter103": mccpRelcTgInCounter103,
       "mccpRelcTgInCounter104": mccpRelcTgInCounter104,
       "mccpRelcTgInCounter105": mccpRelcTgInCounter105,
       "mccpRelcTgInCounter106": mccpRelcTgInCounter106,
       "mccpRelcTgInCounter107": mccpRelcTgInCounter107,
       "mccpRelcTgInCounter108": mccpRelcTgInCounter108,
       "mccpRelcTgInCounter109": mccpRelcTgInCounter109,
       "mccpRelcTgInCounter110": mccpRelcTgInCounter110,
       "mccpRelcTgInCounter111": mccpRelcTgInCounter111,
       "mccpRelcTgInCounter112": mccpRelcTgInCounter112,
       "mccpRelcTgInCounter113": mccpRelcTgInCounter113,
       "mccpRelcTgInCounter114": mccpRelcTgInCounter114,
       "mccpRelcTgInCounter115": mccpRelcTgInCounter115,
       "mccpRelcTgInCounter116": mccpRelcTgInCounter116,
       "mccpRelcTgInCounter117": mccpRelcTgInCounter117,
       "mccpRelcTgInCounter118": mccpRelcTgInCounter118,
       "mccpRelcTgInCounter119": mccpRelcTgInCounter119,
       "mccpRelcTgInCounter120": mccpRelcTgInCounter120,
       "mccpRelcTgInCounter121": mccpRelcTgInCounter121,
       "mccpRelcTgInCounter122": mccpRelcTgInCounter122,
       "mccpRelcTgInCounter123": mccpRelcTgInCounter123,
       "mccpRelcTgInCounter124": mccpRelcTgInCounter124,
       "mccpRelcTgInCounter125": mccpRelcTgInCounter125,
       "mccpRelcTgInCounter126": mccpRelcTgInCounter126,
       "mccpRelcTgInCounter127": mccpRelcTgInCounter127,
       "mccpRelcTgOutTable": mccpRelcTgOutTable,
       "mccpRelcTgOutEntry": mccpRelcTgOutEntry,
       "mccpRelcTgOutIndex": mccpRelcTgOutIndex,
       "mccpRelcTgOutCounter0": mccpRelcTgOutCounter0,
       "mccpRelcTgOutCounter1": mccpRelcTgOutCounter1,
       "mccpRelcTgOutCounter2": mccpRelcTgOutCounter2,
       "mccpRelcTgOutCounter3": mccpRelcTgOutCounter3,
       "mccpRelcTgOutCounter4": mccpRelcTgOutCounter4,
       "mccpRelcTgOutCounter5": mccpRelcTgOutCounter5,
       "mccpRelcTgOutCounter6": mccpRelcTgOutCounter6,
       "mccpRelcTgOutCounter7": mccpRelcTgOutCounter7,
       "mccpRelcTgOutCounter8": mccpRelcTgOutCounter8,
       "mccpRelcTgOutCounter9": mccpRelcTgOutCounter9,
       "mccpRelcTgOutCounter10": mccpRelcTgOutCounter10,
       "mccpRelcTgOutCounter11": mccpRelcTgOutCounter11,
       "mccpRelcTgOutCounter12": mccpRelcTgOutCounter12,
       "mccpRelcTgOutCounter13": mccpRelcTgOutCounter13,
       "mccpRelcTgOutCounter14": mccpRelcTgOutCounter14,
       "mccpRelcTgOutCounter15": mccpRelcTgOutCounter15,
       "mccpRelcTgOutCounter16": mccpRelcTgOutCounter16,
       "mccpRelcTgOutCounter17": mccpRelcTgOutCounter17,
       "mccpRelcTgOutCounter18": mccpRelcTgOutCounter18,
       "mccpRelcTgOutCounter19": mccpRelcTgOutCounter19,
       "mccpRelcTgOutCounter20": mccpRelcTgOutCounter20,
       "mccpRelcTgOutCounter21": mccpRelcTgOutCounter21,
       "mccpRelcTgOutCounter22": mccpRelcTgOutCounter22,
       "mccpRelcTgOutCounter23": mccpRelcTgOutCounter23,
       "mccpRelcTgOutCounter24": mccpRelcTgOutCounter24,
       "mccpRelcTgOutCounter25": mccpRelcTgOutCounter25,
       "mccpRelcTgOutCounter26": mccpRelcTgOutCounter26,
       "mccpRelcTgOutCounter27": mccpRelcTgOutCounter27,
       "mccpRelcTgOutCounter28": mccpRelcTgOutCounter28,
       "mccpRelcTgOutCounter29": mccpRelcTgOutCounter29,
       "mccpRelcTgOutCounter30": mccpRelcTgOutCounter30,
       "mccpRelcTgOutCounter31": mccpRelcTgOutCounter31,
       "mccpRelcTgOutCounter32": mccpRelcTgOutCounter32,
       "mccpRelcTgOutCounter33": mccpRelcTgOutCounter33,
       "mccpRelcTgOutCounter34": mccpRelcTgOutCounter34,
       "mccpRelcTgOutCounter35": mccpRelcTgOutCounter35,
       "mccpRelcTgOutCounter36": mccpRelcTgOutCounter36,
       "mccpRelcTgOutCounter37": mccpRelcTgOutCounter37,
       "mccpRelcTgOutCounter38": mccpRelcTgOutCounter38,
       "mccpRelcTgOutCounter39": mccpRelcTgOutCounter39,
       "mccpRelcTgOutCounter40": mccpRelcTgOutCounter40,
       "mccpRelcTgOutCounter41": mccpRelcTgOutCounter41,
       "mccpRelcTgOutCounter42": mccpRelcTgOutCounter42,
       "mccpRelcTgOutCounter43": mccpRelcTgOutCounter43,
       "mccpRelcTgOutCounter44": mccpRelcTgOutCounter44,
       "mccpRelcTgOutCounter45": mccpRelcTgOutCounter45,
       "mccpRelcTgOutCounter46": mccpRelcTgOutCounter46,
       "mccpRelcTgOutCounter47": mccpRelcTgOutCounter47,
       "mccpRelcTgOutCounter48": mccpRelcTgOutCounter48,
       "mccpRelcTgOutCounter49": mccpRelcTgOutCounter49,
       "mccpRelcTgOutCounter50": mccpRelcTgOutCounter50,
       "mccpRelcTgOutCounter51": mccpRelcTgOutCounter51,
       "mccpRelcTgOutCounter52": mccpRelcTgOutCounter52,
       "mccpRelcTgOutCounter53": mccpRelcTgOutCounter53,
       "mccpRelcTgOutCounter54": mccpRelcTgOutCounter54,
       "mccpRelcTgOutCounter55": mccpRelcTgOutCounter55,
       "mccpRelcTgOutCounter56": mccpRelcTgOutCounter56,
       "mccpRelcTgOutCounter57": mccpRelcTgOutCounter57,
       "mccpRelcTgOutCounter58": mccpRelcTgOutCounter58,
       "mccpRelcTgOutCounter59": mccpRelcTgOutCounter59,
       "mccpRelcTgOutCounter60": mccpRelcTgOutCounter60,
       "mccpRelcTgOutCounter61": mccpRelcTgOutCounter61,
       "mccpRelcTgOutCounter62": mccpRelcTgOutCounter62,
       "mccpRelcTgOutCounter63": mccpRelcTgOutCounter63,
       "mccpRelcTgOutCounter64": mccpRelcTgOutCounter64,
       "mccpRelcTgOutCounter65": mccpRelcTgOutCounter65,
       "mccpRelcTgOutCounter66": mccpRelcTgOutCounter66,
       "mccpRelcTgOutCounter67": mccpRelcTgOutCounter67,
       "mccpRelcTgOutCounter68": mccpRelcTgOutCounter68,
       "mccpRelcTgOutCounter69": mccpRelcTgOutCounter69,
       "mccpRelcTgOutCounter70": mccpRelcTgOutCounter70,
       "mccpRelcTgOutCounter71": mccpRelcTgOutCounter71,
       "mccpRelcTgOutCounter72": mccpRelcTgOutCounter72,
       "mccpRelcTgOutCounter73": mccpRelcTgOutCounter73,
       "mccpRelcTgOutCounter74": mccpRelcTgOutCounter74,
       "mccpRelcTgOutCounter75": mccpRelcTgOutCounter75,
       "mccpRelcTgOutCounter76": mccpRelcTgOutCounter76,
       "mccpRelcTgOutCounter77": mccpRelcTgOutCounter77,
       "mccpRelcTgOutCounter78": mccpRelcTgOutCounter78,
       "mccpRelcTgOutCounter79": mccpRelcTgOutCounter79,
       "mccpRelcTgOutCounter80": mccpRelcTgOutCounter80,
       "mccpRelcTgOutCounter81": mccpRelcTgOutCounter81,
       "mccpRelcTgOutCounter82": mccpRelcTgOutCounter82,
       "mccpRelcTgOutCounter83": mccpRelcTgOutCounter83,
       "mccpRelcTgOutCounter84": mccpRelcTgOutCounter84,
       "mccpRelcTgOutCounter85": mccpRelcTgOutCounter85,
       "mccpRelcTgOutCounter86": mccpRelcTgOutCounter86,
       "mccpRelcTgOutCounter87": mccpRelcTgOutCounter87,
       "mccpRelcTgOutCounter88": mccpRelcTgOutCounter88,
       "mccpRelcTgOutCounter89": mccpRelcTgOutCounter89,
       "mccpRelcTgOutCounter90": mccpRelcTgOutCounter90,
       "mccpRelcTgOutCounter91": mccpRelcTgOutCounter91,
       "mccpRelcTgOutCounter92": mccpRelcTgOutCounter92,
       "mccpRelcTgOutCounter93": mccpRelcTgOutCounter93,
       "mccpRelcTgOutCounter94": mccpRelcTgOutCounter94,
       "mccpRelcTgOutCounter95": mccpRelcTgOutCounter95,
       "mccpRelcTgOutCounter96": mccpRelcTgOutCounter96,
       "mccpRelcTgOutCounter97": mccpRelcTgOutCounter97,
       "mccpRelcTgOutCounter98": mccpRelcTgOutCounter98,
       "mccpRelcTgOutCounter99": mccpRelcTgOutCounter99,
       "mccpRelcTgOutCounter100": mccpRelcTgOutCounter100,
       "mccpRelcTgOutCounter101": mccpRelcTgOutCounter101,
       "mccpRelcTgOutCounter102": mccpRelcTgOutCounter102,
       "mccpRelcTgOutCounter103": mccpRelcTgOutCounter103,
       "mccpRelcTgOutCounter104": mccpRelcTgOutCounter104,
       "mccpRelcTgOutCounter105": mccpRelcTgOutCounter105,
       "mccpRelcTgOutCounter106": mccpRelcTgOutCounter106,
       "mccpRelcTgOutCounter107": mccpRelcTgOutCounter107,
       "mccpRelcTgOutCounter108": mccpRelcTgOutCounter108,
       "mccpRelcTgOutCounter109": mccpRelcTgOutCounter109,
       "mccpRelcTgOutCounter110": mccpRelcTgOutCounter110,
       "mccpRelcTgOutCounter111": mccpRelcTgOutCounter111,
       "mccpRelcTgOutCounter112": mccpRelcTgOutCounter112,
       "mccpRelcTgOutCounter113": mccpRelcTgOutCounter113,
       "mccpRelcTgOutCounter114": mccpRelcTgOutCounter114,
       "mccpRelcTgOutCounter115": mccpRelcTgOutCounter115,
       "mccpRelcTgOutCounter116": mccpRelcTgOutCounter116,
       "mccpRelcTgOutCounter117": mccpRelcTgOutCounter117,
       "mccpRelcTgOutCounter118": mccpRelcTgOutCounter118,
       "mccpRelcTgOutCounter119": mccpRelcTgOutCounter119,
       "mccpRelcTgOutCounter120": mccpRelcTgOutCounter120,
       "mccpRelcTgOutCounter121": mccpRelcTgOutCounter121,
       "mccpRelcTgOutCounter122": mccpRelcTgOutCounter122,
       "mccpRelcTgOutCounter123": mccpRelcTgOutCounter123,
       "mccpRelcTgOutCounter124": mccpRelcTgOutCounter124,
       "mccpRelcTgOutCounter125": mccpRelcTgOutCounter125,
       "mccpRelcTgOutCounter126": mccpRelcTgOutCounter126,
       "mccpRelcTgOutCounter127": mccpRelcTgOutCounter127,
       "mccpRelcTgTrInTable": mccpRelcTgTrInTable,
       "mccpRelcTgTrInEntry": mccpRelcTgTrInEntry,
       "mccpRelcTgTrInIndex": mccpRelcTgTrInIndex,
       "mccpRelcTgTrInCounter0": mccpRelcTgTrInCounter0,
       "mccpRelcTgTrInCounter1": mccpRelcTgTrInCounter1,
       "mccpRelcTgTrInCounter2": mccpRelcTgTrInCounter2,
       "mccpRelcTgTrInCounter3": mccpRelcTgTrInCounter3,
       "mccpRelcTgTrInCounter4": mccpRelcTgTrInCounter4,
       "mccpRelcTgTrInCounter5": mccpRelcTgTrInCounter5,
       "mccpRelcTgTrInCounter6": mccpRelcTgTrInCounter6,
       "mccpRelcTgTrInCounter7": mccpRelcTgTrInCounter7,
       "mccpRelcTgTrInCounter8": mccpRelcTgTrInCounter8,
       "mccpRelcTgTrInCounter9": mccpRelcTgTrInCounter9,
       "mccpRelcTgTrInCounter10": mccpRelcTgTrInCounter10,
       "mccpRelcTgTrInCounter11": mccpRelcTgTrInCounter11,
       "mccpRelcTgTrInCounter12": mccpRelcTgTrInCounter12,
       "mccpRelcTgTrInCounter13": mccpRelcTgTrInCounter13,
       "mccpRelcTgTrInCounter14": mccpRelcTgTrInCounter14,
       "mccpRelcTgTrInCounter15": mccpRelcTgTrInCounter15,
       "mccpRelcTgTrInCounter16": mccpRelcTgTrInCounter16,
       "mccpRelcTgTrInCounter17": mccpRelcTgTrInCounter17,
       "mccpRelcTgTrInCounter18": mccpRelcTgTrInCounter18,
       "mccpRelcTgTrInCounter19": mccpRelcTgTrInCounter19,
       "mccpRelcTgTrInCounter20": mccpRelcTgTrInCounter20,
       "mccpRelcTgTrInCounter21": mccpRelcTgTrInCounter21,
       "mccpRelcTgTrInCounter22": mccpRelcTgTrInCounter22,
       "mccpRelcTgTrInCounter23": mccpRelcTgTrInCounter23,
       "mccpRelcTgTrInCounter24": mccpRelcTgTrInCounter24,
       "mccpRelcTgTrInCounter25": mccpRelcTgTrInCounter25,
       "mccpRelcTgTrInCounter26": mccpRelcTgTrInCounter26,
       "mccpRelcTgTrInCounter27": mccpRelcTgTrInCounter27,
       "mccpRelcTgTrInCounter28": mccpRelcTgTrInCounter28,
       "mccpRelcTgTrInCounter29": mccpRelcTgTrInCounter29,
       "mccpRelcTgTrInCounter30": mccpRelcTgTrInCounter30,
       "mccpRelcTgTrInCounter31": mccpRelcTgTrInCounter31,
       "mccpRelcTgTrInCounter32": mccpRelcTgTrInCounter32,
       "mccpRelcTgTrInCounter33": mccpRelcTgTrInCounter33,
       "mccpRelcTgTrInCounter34": mccpRelcTgTrInCounter34,
       "mccpRelcTgTrInCounter35": mccpRelcTgTrInCounter35,
       "mccpRelcTgTrInCounter36": mccpRelcTgTrInCounter36,
       "mccpRelcTgTrInCounter37": mccpRelcTgTrInCounter37,
       "mccpRelcTgTrInCounter38": mccpRelcTgTrInCounter38,
       "mccpRelcTgTrInCounter39": mccpRelcTgTrInCounter39,
       "mccpRelcTgTrInCounter40": mccpRelcTgTrInCounter40,
       "mccpRelcTgTrInCounter41": mccpRelcTgTrInCounter41,
       "mccpRelcTgTrInCounter42": mccpRelcTgTrInCounter42,
       "mccpRelcTgTrInCounter43": mccpRelcTgTrInCounter43,
       "mccpRelcTgTrInCounter44": mccpRelcTgTrInCounter44,
       "mccpRelcTgTrInCounter45": mccpRelcTgTrInCounter45,
       "mccpRelcTgTrInCounter46": mccpRelcTgTrInCounter46,
       "mccpRelcTgTrInCounter47": mccpRelcTgTrInCounter47,
       "mccpRelcTgTrInCounter48": mccpRelcTgTrInCounter48,
       "mccpRelcTgTrInCounter49": mccpRelcTgTrInCounter49,
       "mccpRelcTgTrInCounter50": mccpRelcTgTrInCounter50,
       "mccpRelcTgTrInCounter51": mccpRelcTgTrInCounter51,
       "mccpRelcTgTrInCounter52": mccpRelcTgTrInCounter52,
       "mccpRelcTgTrInCounter53": mccpRelcTgTrInCounter53,
       "mccpRelcTgTrInCounter54": mccpRelcTgTrInCounter54,
       "mccpRelcTgTrInCounter55": mccpRelcTgTrInCounter55,
       "mccpRelcTgTrInCounter56": mccpRelcTgTrInCounter56,
       "mccpRelcTgTrInCounter57": mccpRelcTgTrInCounter57,
       "mccpRelcTgTrInCounter58": mccpRelcTgTrInCounter58,
       "mccpRelcTgTrInCounter59": mccpRelcTgTrInCounter59,
       "mccpRelcTgTrInCounter60": mccpRelcTgTrInCounter60,
       "mccpRelcTgTrInCounter61": mccpRelcTgTrInCounter61,
       "mccpRelcTgTrInCounter62": mccpRelcTgTrInCounter62,
       "mccpRelcTgTrInCounter63": mccpRelcTgTrInCounter63,
       "mccpRelcTgTrInCounter64": mccpRelcTgTrInCounter64,
       "mccpRelcTgTrInCounter65": mccpRelcTgTrInCounter65,
       "mccpRelcTgTrInCounter66": mccpRelcTgTrInCounter66,
       "mccpRelcTgTrInCounter67": mccpRelcTgTrInCounter67,
       "mccpRelcTgTrInCounter68": mccpRelcTgTrInCounter68,
       "mccpRelcTgTrInCounter69": mccpRelcTgTrInCounter69,
       "mccpRelcTgTrInCounter70": mccpRelcTgTrInCounter70,
       "mccpRelcTgTrInCounter71": mccpRelcTgTrInCounter71,
       "mccpRelcTgTrInCounter72": mccpRelcTgTrInCounter72,
       "mccpRelcTgTrInCounter73": mccpRelcTgTrInCounter73,
       "mccpRelcTgTrInCounter74": mccpRelcTgTrInCounter74,
       "mccpRelcTgTrInCounter75": mccpRelcTgTrInCounter75,
       "mccpRelcTgTrInCounter76": mccpRelcTgTrInCounter76,
       "mccpRelcTgTrInCounter77": mccpRelcTgTrInCounter77,
       "mccpRelcTgTrInCounter78": mccpRelcTgTrInCounter78,
       "mccpRelcTgTrInCounter79": mccpRelcTgTrInCounter79,
       "mccpRelcTgTrInCounter80": mccpRelcTgTrInCounter80,
       "mccpRelcTgTrInCounter81": mccpRelcTgTrInCounter81,
       "mccpRelcTgTrInCounter82": mccpRelcTgTrInCounter82,
       "mccpRelcTgTrInCounter83": mccpRelcTgTrInCounter83,
       "mccpRelcTgTrInCounter84": mccpRelcTgTrInCounter84,
       "mccpRelcTgTrInCounter85": mccpRelcTgTrInCounter85,
       "mccpRelcTgTrInCounter86": mccpRelcTgTrInCounter86,
       "mccpRelcTgTrInCounter87": mccpRelcTgTrInCounter87,
       "mccpRelcTgTrInCounter88": mccpRelcTgTrInCounter88,
       "mccpRelcTgTrInCounter89": mccpRelcTgTrInCounter89,
       "mccpRelcTgTrInCounter90": mccpRelcTgTrInCounter90,
       "mccpRelcTgTrInCounter91": mccpRelcTgTrInCounter91,
       "mccpRelcTgTrInCounter92": mccpRelcTgTrInCounter92,
       "mccpRelcTgTrInCounter93": mccpRelcTgTrInCounter93,
       "mccpRelcTgTrInCounter94": mccpRelcTgTrInCounter94,
       "mccpRelcTgTrInCounter95": mccpRelcTgTrInCounter95,
       "mccpRelcTgTrInCounter96": mccpRelcTgTrInCounter96,
       "mccpRelcTgTrInCounter97": mccpRelcTgTrInCounter97,
       "mccpRelcTgTrInCounter98": mccpRelcTgTrInCounter98,
       "mccpRelcTgTrInCounter99": mccpRelcTgTrInCounter99,
       "mccpRelcTgTrInCounter100": mccpRelcTgTrInCounter100,
       "mccpRelcTgTrInCounter101": mccpRelcTgTrInCounter101,
       "mccpRelcTgTrInCounter102": mccpRelcTgTrInCounter102,
       "mccpRelcTgTrInCounter103": mccpRelcTgTrInCounter103,
       "mccpRelcTgTrInCounter104": mccpRelcTgTrInCounter104,
       "mccpRelcTgTrInCounter105": mccpRelcTgTrInCounter105,
       "mccpRelcTgTrInCounter106": mccpRelcTgTrInCounter106,
       "mccpRelcTgTrInCounter107": mccpRelcTgTrInCounter107,
       "mccpRelcTgTrInCounter108": mccpRelcTgTrInCounter108,
       "mccpRelcTgTrInCounter109": mccpRelcTgTrInCounter109,
       "mccpRelcTgTrInCounter110": mccpRelcTgTrInCounter110,
       "mccpRelcTgTrInCounter111": mccpRelcTgTrInCounter111,
       "mccpRelcTgTrInCounter112": mccpRelcTgTrInCounter112,
       "mccpRelcTgTrInCounter113": mccpRelcTgTrInCounter113,
       "mccpRelcTgTrInCounter114": mccpRelcTgTrInCounter114,
       "mccpRelcTgTrInCounter115": mccpRelcTgTrInCounter115,
       "mccpRelcTgTrInCounter116": mccpRelcTgTrInCounter116,
       "mccpRelcTgTrInCounter117": mccpRelcTgTrInCounter117,
       "mccpRelcTgTrInCounter118": mccpRelcTgTrInCounter118,
       "mccpRelcTgTrInCounter119": mccpRelcTgTrInCounter119,
       "mccpRelcTgTrInCounter120": mccpRelcTgTrInCounter120,
       "mccpRelcTgTrInCounter121": mccpRelcTgTrInCounter121,
       "mccpRelcTgTrInCounter122": mccpRelcTgTrInCounter122,
       "mccpRelcTgTrInCounter123": mccpRelcTgTrInCounter123,
       "mccpRelcTgTrInCounter124": mccpRelcTgTrInCounter124,
       "mccpRelcTgTrInCounter125": mccpRelcTgTrInCounter125,
       "mccpRelcTgTrInCounter126": mccpRelcTgTrInCounter126,
       "mccpRelcTgTrInCounter127": mccpRelcTgTrInCounter127,
       "mccpRelcTgTrOutTable": mccpRelcTgTrOutTable,
       "mccpRelcTgTrOutEntry": mccpRelcTgTrOutEntry,
       "mccpRelcTgTrOutIndex": mccpRelcTgTrOutIndex,
       "mccpRelcTgTrOutCounter0": mccpRelcTgTrOutCounter0,
       "mccpRelcTgTrOutCounter1": mccpRelcTgTrOutCounter1,
       "mccpRelcTgTrOutCounter2": mccpRelcTgTrOutCounter2,
       "mccpRelcTgTrOutCounter3": mccpRelcTgTrOutCounter3,
       "mccpRelcTgTrOutCounter4": mccpRelcTgTrOutCounter4,
       "mccpRelcTgTrOutCounter5": mccpRelcTgTrOutCounter5,
       "mccpRelcTgTrOutCounter6": mccpRelcTgTrOutCounter6,
       "mccpRelcTgTrOutCounter7": mccpRelcTgTrOutCounter7,
       "mccpRelcTgTrOutCounter8": mccpRelcTgTrOutCounter8,
       "mccpRelcTgTrOutCounter9": mccpRelcTgTrOutCounter9,
       "mccpRelcTgTrOutCounter10": mccpRelcTgTrOutCounter10,
       "mccpRelcTgTrOutCounter11": mccpRelcTgTrOutCounter11,
       "mccpRelcTgTrOutCounter12": mccpRelcTgTrOutCounter12,
       "mccpRelcTgTrOutCounter13": mccpRelcTgTrOutCounter13,
       "mccpRelcTgTrOutCounter14": mccpRelcTgTrOutCounter14,
       "mccpRelcTgTrOutCounter15": mccpRelcTgTrOutCounter15,
       "mccpRelcTgTrOutCounter16": mccpRelcTgTrOutCounter16,
       "mccpRelcTgTrOutCounter17": mccpRelcTgTrOutCounter17,
       "mccpRelcTgTrOutCounter18": mccpRelcTgTrOutCounter18,
       "mccpRelcTgTrOutCounter19": mccpRelcTgTrOutCounter19,
       "mccpRelcTgTrOutCounter20": mccpRelcTgTrOutCounter20,
       "mccpRelcTgTrOutCounter21": mccpRelcTgTrOutCounter21,
       "mccpRelcTgTrOutCounter22": mccpRelcTgTrOutCounter22,
       "mccpRelcTgTrOutCounter23": mccpRelcTgTrOutCounter23,
       "mccpRelcTgTrOutCounter24": mccpRelcTgTrOutCounter24,
       "mccpRelcTgTrOutCounter25": mccpRelcTgTrOutCounter25,
       "mccpRelcTgTrOutCounter26": mccpRelcTgTrOutCounter26,
       "mccpRelcTgTrOutCounter27": mccpRelcTgTrOutCounter27,
       "mccpRelcTgTrOutCounter28": mccpRelcTgTrOutCounter28,
       "mccpRelcTgTrOutCounter29": mccpRelcTgTrOutCounter29,
       "mccpRelcTgTrOutCounter30": mccpRelcTgTrOutCounter30,
       "mccpRelcTgTrOutCounter31": mccpRelcTgTrOutCounter31,
       "mccpRelcTgTrOutCounter32": mccpRelcTgTrOutCounter32,
       "mccpRelcTgTrOutCounter33": mccpRelcTgTrOutCounter33,
       "mccpRelcTgTrOutCounter34": mccpRelcTgTrOutCounter34,
       "mccpRelcTgTrOutCounter35": mccpRelcTgTrOutCounter35,
       "mccpRelcTgTrOutCounter36": mccpRelcTgTrOutCounter36,
       "mccpRelcTgTrOutCounter37": mccpRelcTgTrOutCounter37,
       "mccpRelcTgTrOutCounter38": mccpRelcTgTrOutCounter38,
       "mccpRelcTgTrOutCounter39": mccpRelcTgTrOutCounter39,
       "mccpRelcTgTrOutCounter40": mccpRelcTgTrOutCounter40,
       "mccpRelcTgTrOutCounter41": mccpRelcTgTrOutCounter41,
       "mccpRelcTgTrOutCounter42": mccpRelcTgTrOutCounter42,
       "mccpRelcTgTrOutCounter43": mccpRelcTgTrOutCounter43,
       "mccpRelcTgTrOutCounter44": mccpRelcTgTrOutCounter44,
       "mccpRelcTgTrOutCounter45": mccpRelcTgTrOutCounter45,
       "mccpRelcTgTrOutCounter46": mccpRelcTgTrOutCounter46,
       "mccpRelcTgTrOutCounter47": mccpRelcTgTrOutCounter47,
       "mccpRelcTgTrOutCounter48": mccpRelcTgTrOutCounter48,
       "mccpRelcTgTrOutCounter49": mccpRelcTgTrOutCounter49,
       "mccpRelcTgTrOutCounter50": mccpRelcTgTrOutCounter50,
       "mccpRelcTgTrOutCounter51": mccpRelcTgTrOutCounter51,
       "mccpRelcTgTrOutCounter52": mccpRelcTgTrOutCounter52,
       "mccpRelcTgTrOutCounter53": mccpRelcTgTrOutCounter53,
       "mccpRelcTgTrOutCounter54": mccpRelcTgTrOutCounter54,
       "mccpRelcTgTrOutCounter55": mccpRelcTgTrOutCounter55,
       "mccpRelcTgTrOutCounter56": mccpRelcTgTrOutCounter56,
       "mccpRelcTgTrOutCounter57": mccpRelcTgTrOutCounter57,
       "mccpRelcTgTrOutCounter58": mccpRelcTgTrOutCounter58,
       "mccpRelcTgTrOutCounter59": mccpRelcTgTrOutCounter59,
       "mccpRelcTgTrOutCounter60": mccpRelcTgTrOutCounter60,
       "mccpRelcTgTrOutCounter61": mccpRelcTgTrOutCounter61,
       "mccpRelcTgTrOutCounter62": mccpRelcTgTrOutCounter62,
       "mccpRelcTgTrOutCounter63": mccpRelcTgTrOutCounter63,
       "mccpRelcTgTrOutCounter64": mccpRelcTgTrOutCounter64,
       "mccpRelcTgTrOutCounter65": mccpRelcTgTrOutCounter65,
       "mccpRelcTgTrOutCounter66": mccpRelcTgTrOutCounter66,
       "mccpRelcTgTrOutCounter67": mccpRelcTgTrOutCounter67,
       "mccpRelcTgTrOutCounter68": mccpRelcTgTrOutCounter68,
       "mccpRelcTgTrOutCounter69": mccpRelcTgTrOutCounter69,
       "mccpRelcTgTrOutCounter70": mccpRelcTgTrOutCounter70,
       "mccpRelcTgTrOutCounter71": mccpRelcTgTrOutCounter71,
       "mccpRelcTgTrOutCounter72": mccpRelcTgTrOutCounter72,
       "mccpRelcTgTrOutCounter73": mccpRelcTgTrOutCounter73,
       "mccpRelcTgTrOutCounter74": mccpRelcTgTrOutCounter74,
       "mccpRelcTgTrOutCounter75": mccpRelcTgTrOutCounter75,
       "mccpRelcTgTrOutCounter76": mccpRelcTgTrOutCounter76,
       "mccpRelcTgTrOutCounter77": mccpRelcTgTrOutCounter77,
       "mccpRelcTgTrOutCounter78": mccpRelcTgTrOutCounter78,
       "mccpRelcTgTrOutCounter79": mccpRelcTgTrOutCounter79,
       "mccpRelcTgTrOutCounter80": mccpRelcTgTrOutCounter80,
       "mccpRelcTgTrOutCounter81": mccpRelcTgTrOutCounter81,
       "mccpRelcTgTrOutCounter82": mccpRelcTgTrOutCounter82,
       "mccpRelcTgTrOutCounter83": mccpRelcTgTrOutCounter83,
       "mccpRelcTgTrOutCounter84": mccpRelcTgTrOutCounter84,
       "mccpRelcTgTrOutCounter85": mccpRelcTgTrOutCounter85,
       "mccpRelcTgTrOutCounter86": mccpRelcTgTrOutCounter86,
       "mccpRelcTgTrOutCounter87": mccpRelcTgTrOutCounter87,
       "mccpRelcTgTrOutCounter88": mccpRelcTgTrOutCounter88,
       "mccpRelcTgTrOutCounter89": mccpRelcTgTrOutCounter89,
       "mccpRelcTgTrOutCounter90": mccpRelcTgTrOutCounter90,
       "mccpRelcTgTrOutCounter91": mccpRelcTgTrOutCounter91,
       "mccpRelcTgTrOutCounter92": mccpRelcTgTrOutCounter92,
       "mccpRelcTgTrOutCounter93": mccpRelcTgTrOutCounter93,
       "mccpRelcTgTrOutCounter94": mccpRelcTgTrOutCounter94,
       "mccpRelcTgTrOutCounter95": mccpRelcTgTrOutCounter95,
       "mccpRelcTgTrOutCounter96": mccpRelcTgTrOutCounter96,
       "mccpRelcTgTrOutCounter97": mccpRelcTgTrOutCounter97,
       "mccpRelcTgTrOutCounter98": mccpRelcTgTrOutCounter98,
       "mccpRelcTgTrOutCounter99": mccpRelcTgTrOutCounter99,
       "mccpRelcTgTrOutCounter100": mccpRelcTgTrOutCounter100,
       "mccpRelcTgTrOutCounter101": mccpRelcTgTrOutCounter101,
       "mccpRelcTgTrOutCounter102": mccpRelcTgTrOutCounter102,
       "mccpRelcTgTrOutCounter103": mccpRelcTgTrOutCounter103,
       "mccpRelcTgTrOutCounter104": mccpRelcTgTrOutCounter104,
       "mccpRelcTgTrOutCounter105": mccpRelcTgTrOutCounter105,
       "mccpRelcTgTrOutCounter106": mccpRelcTgTrOutCounter106,
       "mccpRelcTgTrOutCounter107": mccpRelcTgTrOutCounter107,
       "mccpRelcTgTrOutCounter108": mccpRelcTgTrOutCounter108,
       "mccpRelcTgTrOutCounter109": mccpRelcTgTrOutCounter109,
       "mccpRelcTgTrOutCounter110": mccpRelcTgTrOutCounter110,
       "mccpRelcTgTrOutCounter111": mccpRelcTgTrOutCounter111,
       "mccpRelcTgTrOutCounter112": mccpRelcTgTrOutCounter112,
       "mccpRelcTgTrOutCounter113": mccpRelcTgTrOutCounter113,
       "mccpRelcTgTrOutCounter114": mccpRelcTgTrOutCounter114,
       "mccpRelcTgTrOutCounter115": mccpRelcTgTrOutCounter115,
       "mccpRelcTgTrOutCounter116": mccpRelcTgTrOutCounter116,
       "mccpRelcTgTrOutCounter117": mccpRelcTgTrOutCounter117,
       "mccpRelcTgTrOutCounter118": mccpRelcTgTrOutCounter118,
       "mccpRelcTgTrOutCounter119": mccpRelcTgTrOutCounter119,
       "mccpRelcTgTrOutCounter120": mccpRelcTgTrOutCounter120,
       "mccpRelcTgTrOutCounter121": mccpRelcTgTrOutCounter121,
       "mccpRelcTgTrOutCounter122": mccpRelcTgTrOutCounter122,
       "mccpRelcTgTrOutCounter123": mccpRelcTgTrOutCounter123,
       "mccpRelcTgTrOutCounter124": mccpRelcTgTrOutCounter124,
       "mccpRelcTgTrOutCounter125": mccpRelcTgTrOutCounter125,
       "mccpRelcTgTrOutCounter126": mccpRelcTgTrOutCounter126,
       "mccpRelcTgTrOutCounter127": mccpRelcTgTrOutCounter127,
       "mccpRelcPlanInTable": mccpRelcPlanInTable,
       "mccpRelcPlanInEntry": mccpRelcPlanInEntry,
       "mccpRelcPlanInIndex": mccpRelcPlanInIndex,
       "mccpRelcPlanInCounter0": mccpRelcPlanInCounter0,
       "mccpRelcPlanInCounter1": mccpRelcPlanInCounter1,
       "mccpRelcPlanInCounter2": mccpRelcPlanInCounter2,
       "mccpRelcPlanInCounter3": mccpRelcPlanInCounter3,
       "mccpRelcPlanInCounter4": mccpRelcPlanInCounter4,
       "mccpRelcPlanInCounter5": mccpRelcPlanInCounter5,
       "mccpRelcPlanInCounter6": mccpRelcPlanInCounter6,
       "mccpRelcPlanInCounter7": mccpRelcPlanInCounter7,
       "mccpRelcPlanInCounter8": mccpRelcPlanInCounter8,
       "mccpRelcPlanInCounter9": mccpRelcPlanInCounter9,
       "mccpRelcPlanInCounter10": mccpRelcPlanInCounter10,
       "mccpRelcPlanInCounter11": mccpRelcPlanInCounter11,
       "mccpRelcPlanInCounter12": mccpRelcPlanInCounter12,
       "mccpRelcPlanInCounter13": mccpRelcPlanInCounter13,
       "mccpRelcPlanInCounter14": mccpRelcPlanInCounter14,
       "mccpRelcPlanInCounter15": mccpRelcPlanInCounter15,
       "mccpRelcPlanInCounter16": mccpRelcPlanInCounter16,
       "mccpRelcPlanInCounter17": mccpRelcPlanInCounter17,
       "mccpRelcPlanInCounter18": mccpRelcPlanInCounter18,
       "mccpRelcPlanInCounter19": mccpRelcPlanInCounter19,
       "mccpRelcPlanInCounter20": mccpRelcPlanInCounter20,
       "mccpRelcPlanInCounter21": mccpRelcPlanInCounter21,
       "mccpRelcPlanInCounter22": mccpRelcPlanInCounter22,
       "mccpRelcPlanInCounter23": mccpRelcPlanInCounter23,
       "mccpRelcPlanInCounter24": mccpRelcPlanInCounter24,
       "mccpRelcPlanInCounter25": mccpRelcPlanInCounter25,
       "mccpRelcPlanInCounter26": mccpRelcPlanInCounter26,
       "mccpRelcPlanInCounter27": mccpRelcPlanInCounter27,
       "mccpRelcPlanInCounter28": mccpRelcPlanInCounter28,
       "mccpRelcPlanInCounter29": mccpRelcPlanInCounter29,
       "mccpRelcPlanInCounter30": mccpRelcPlanInCounter30,
       "mccpRelcPlanInCounter31": mccpRelcPlanInCounter31,
       "mccpRelcPlanInCounter32": mccpRelcPlanInCounter32,
       "mccpRelcPlanInCounter33": mccpRelcPlanInCounter33,
       "mccpRelcPlanInCounter34": mccpRelcPlanInCounter34,
       "mccpRelcPlanInCounter35": mccpRelcPlanInCounter35,
       "mccpRelcPlanInCounter36": mccpRelcPlanInCounter36,
       "mccpRelcPlanInCounter37": mccpRelcPlanInCounter37,
       "mccpRelcPlanInCounter38": mccpRelcPlanInCounter38,
       "mccpRelcPlanInCounter39": mccpRelcPlanInCounter39,
       "mccpRelcPlanInCounter40": mccpRelcPlanInCounter40,
       "mccpRelcPlanInCounter41": mccpRelcPlanInCounter41,
       "mccpRelcPlanInCounter42": mccpRelcPlanInCounter42,
       "mccpRelcPlanInCounter43": mccpRelcPlanInCounter43,
       "mccpRelcPlanInCounter44": mccpRelcPlanInCounter44,
       "mccpRelcPlanInCounter45": mccpRelcPlanInCounter45,
       "mccpRelcPlanInCounter46": mccpRelcPlanInCounter46,
       "mccpRelcPlanInCounter47": mccpRelcPlanInCounter47,
       "mccpRelcPlanInCounter48": mccpRelcPlanInCounter48,
       "mccpRelcPlanInCounter49": mccpRelcPlanInCounter49,
       "mccpRelcPlanInCounter50": mccpRelcPlanInCounter50,
       "mccpRelcPlanInCounter51": mccpRelcPlanInCounter51,
       "mccpRelcPlanInCounter52": mccpRelcPlanInCounter52,
       "mccpRelcPlanInCounter53": mccpRelcPlanInCounter53,
       "mccpRelcPlanInCounter54": mccpRelcPlanInCounter54,
       "mccpRelcPlanInCounter55": mccpRelcPlanInCounter55,
       "mccpRelcPlanInCounter56": mccpRelcPlanInCounter56,
       "mccpRelcPlanInCounter57": mccpRelcPlanInCounter57,
       "mccpRelcPlanInCounter58": mccpRelcPlanInCounter58,
       "mccpRelcPlanInCounter59": mccpRelcPlanInCounter59,
       "mccpRelcPlanInCounter60": mccpRelcPlanInCounter60,
       "mccpRelcPlanInCounter61": mccpRelcPlanInCounter61,
       "mccpRelcPlanInCounter62": mccpRelcPlanInCounter62,
       "mccpRelcPlanInCounter63": mccpRelcPlanInCounter63,
       "mccpRelcPlanInCounter64": mccpRelcPlanInCounter64,
       "mccpRelcPlanInCounter65": mccpRelcPlanInCounter65,
       "mccpRelcPlanInCounter66": mccpRelcPlanInCounter66,
       "mccpRelcPlanInCounter67": mccpRelcPlanInCounter67,
       "mccpRelcPlanInCounter68": mccpRelcPlanInCounter68,
       "mccpRelcPlanInCounter69": mccpRelcPlanInCounter69,
       "mccpRelcPlanInCounter70": mccpRelcPlanInCounter70,
       "mccpRelcPlanInCounter71": mccpRelcPlanInCounter71,
       "mccpRelcPlanInCounter72": mccpRelcPlanInCounter72,
       "mccpRelcPlanInCounter73": mccpRelcPlanInCounter73,
       "mccpRelcPlanInCounter74": mccpRelcPlanInCounter74,
       "mccpRelcPlanInCounter75": mccpRelcPlanInCounter75,
       "mccpRelcPlanInCounter76": mccpRelcPlanInCounter76,
       "mccpRelcPlanInCounter77": mccpRelcPlanInCounter77,
       "mccpRelcPlanInCounter78": mccpRelcPlanInCounter78,
       "mccpRelcPlanInCounter79": mccpRelcPlanInCounter79,
       "mccpRelcPlanInCounter80": mccpRelcPlanInCounter80,
       "mccpRelcPlanInCounter81": mccpRelcPlanInCounter81,
       "mccpRelcPlanInCounter82": mccpRelcPlanInCounter82,
       "mccpRelcPlanInCounter83": mccpRelcPlanInCounter83,
       "mccpRelcPlanInCounter84": mccpRelcPlanInCounter84,
       "mccpRelcPlanInCounter85": mccpRelcPlanInCounter85,
       "mccpRelcPlanInCounter86": mccpRelcPlanInCounter86,
       "mccpRelcPlanInCounter87": mccpRelcPlanInCounter87,
       "mccpRelcPlanInCounter88": mccpRelcPlanInCounter88,
       "mccpRelcPlanInCounter89": mccpRelcPlanInCounter89,
       "mccpRelcPlanInCounter90": mccpRelcPlanInCounter90,
       "mccpRelcPlanInCounter91": mccpRelcPlanInCounter91,
       "mccpRelcPlanInCounter92": mccpRelcPlanInCounter92,
       "mccpRelcPlanInCounter93": mccpRelcPlanInCounter93,
       "mccpRelcPlanInCounter94": mccpRelcPlanInCounter94,
       "mccpRelcPlanInCounter95": mccpRelcPlanInCounter95,
       "mccpRelcPlanInCounter96": mccpRelcPlanInCounter96,
       "mccpRelcPlanInCounter97": mccpRelcPlanInCounter97,
       "mccpRelcPlanInCounter98": mccpRelcPlanInCounter98,
       "mccpRelcPlanInCounter99": mccpRelcPlanInCounter99,
       "mccpRelcPlanInCounter100": mccpRelcPlanInCounter100,
       "mccpRelcPlanInCounter101": mccpRelcPlanInCounter101,
       "mccpRelcPlanInCounter102": mccpRelcPlanInCounter102,
       "mccpRelcPlanInCounter103": mccpRelcPlanInCounter103,
       "mccpRelcPlanInCounter104": mccpRelcPlanInCounter104,
       "mccpRelcPlanInCounter105": mccpRelcPlanInCounter105,
       "mccpRelcPlanInCounter106": mccpRelcPlanInCounter106,
       "mccpRelcPlanInCounter107": mccpRelcPlanInCounter107,
       "mccpRelcPlanInCounter108": mccpRelcPlanInCounter108,
       "mccpRelcPlanInCounter109": mccpRelcPlanInCounter109,
       "mccpRelcPlanInCounter110": mccpRelcPlanInCounter110,
       "mccpRelcPlanInCounter111": mccpRelcPlanInCounter111,
       "mccpRelcPlanInCounter112": mccpRelcPlanInCounter112,
       "mccpRelcPlanInCounter113": mccpRelcPlanInCounter113,
       "mccpRelcPlanInCounter114": mccpRelcPlanInCounter114,
       "mccpRelcPlanInCounter115": mccpRelcPlanInCounter115,
       "mccpRelcPlanInCounter116": mccpRelcPlanInCounter116,
       "mccpRelcPlanInCounter117": mccpRelcPlanInCounter117,
       "mccpRelcPlanInCounter118": mccpRelcPlanInCounter118,
       "mccpRelcPlanInCounter119": mccpRelcPlanInCounter119,
       "mccpRelcPlanInCounter120": mccpRelcPlanInCounter120,
       "mccpRelcPlanInCounter121": mccpRelcPlanInCounter121,
       "mccpRelcPlanInCounter122": mccpRelcPlanInCounter122,
       "mccpRelcPlanInCounter123": mccpRelcPlanInCounter123,
       "mccpRelcPlanInCounter124": mccpRelcPlanInCounter124,
       "mccpRelcPlanInCounter125": mccpRelcPlanInCounter125,
       "mccpRelcPlanInCounter126": mccpRelcPlanInCounter126,
       "mccpRelcPlanInCounter127": mccpRelcPlanInCounter127,
       "mccpRelcPlanOutTable": mccpRelcPlanOutTable,
       "mccpRelcPlanOutEntry": mccpRelcPlanOutEntry,
       "mccpRelcPlanOutIndex": mccpRelcPlanOutIndex,
       "mccpRelcPlanOutCounter0": mccpRelcPlanOutCounter0,
       "mccpRelcPlanOutCounter1": mccpRelcPlanOutCounter1,
       "mccpRelcPlanOutCounter2": mccpRelcPlanOutCounter2,
       "mccpRelcPlanOutCounter3": mccpRelcPlanOutCounter3,
       "mccpRelcPlanOutCounter4": mccpRelcPlanOutCounter4,
       "mccpRelcPlanOutCounter5": mccpRelcPlanOutCounter5,
       "mccpRelcPlanOutCounter6": mccpRelcPlanOutCounter6,
       "mccpRelcPlanOutCounter7": mccpRelcPlanOutCounter7,
       "mccpRelcPlanOutCounter8": mccpRelcPlanOutCounter8,
       "mccpRelcPlanOutCounter9": mccpRelcPlanOutCounter9,
       "mccpRelcPlanOutCounter10": mccpRelcPlanOutCounter10,
       "mccpRelcPlanOutCounter11": mccpRelcPlanOutCounter11,
       "mccpRelcPlanOutCounter12": mccpRelcPlanOutCounter12,
       "mccpRelcPlanOutCounter13": mccpRelcPlanOutCounter13,
       "mccpRelcPlanOutCounter14": mccpRelcPlanOutCounter14,
       "mccpRelcPlanOutCounter15": mccpRelcPlanOutCounter15,
       "mccpRelcPlanOutCounter16": mccpRelcPlanOutCounter16,
       "mccpRelcPlanOutCounter17": mccpRelcPlanOutCounter17,
       "mccpRelcPlanOutCounter18": mccpRelcPlanOutCounter18,
       "mccpRelcPlanOutCounter19": mccpRelcPlanOutCounter19,
       "mccpRelcPlanOutCounter20": mccpRelcPlanOutCounter20,
       "mccpRelcPlanOutCounter21": mccpRelcPlanOutCounter21,
       "mccpRelcPlanOutCounter22": mccpRelcPlanOutCounter22,
       "mccpRelcPlanOutCounter23": mccpRelcPlanOutCounter23,
       "mccpRelcPlanOutCounter24": mccpRelcPlanOutCounter24,
       "mccpRelcPlanOutCounter25": mccpRelcPlanOutCounter25,
       "mccpRelcPlanOutCounter26": mccpRelcPlanOutCounter26,
       "mccpRelcPlanOutCounter27": mccpRelcPlanOutCounter27,
       "mccpRelcPlanOutCounter28": mccpRelcPlanOutCounter28,
       "mccpRelcPlanOutCounter29": mccpRelcPlanOutCounter29,
       "mccpRelcPlanOutCounter30": mccpRelcPlanOutCounter30,
       "mccpRelcPlanOutCounter31": mccpRelcPlanOutCounter31,
       "mccpRelcPlanOutCounter32": mccpRelcPlanOutCounter32,
       "mccpRelcPlanOutCounter33": mccpRelcPlanOutCounter33,
       "mccpRelcPlanOutCounter34": mccpRelcPlanOutCounter34,
       "mccpRelcPlanOutCounter35": mccpRelcPlanOutCounter35,
       "mccpRelcPlanOutCounter36": mccpRelcPlanOutCounter36,
       "mccpRelcPlanOutCounter37": mccpRelcPlanOutCounter37,
       "mccpRelcPlanOutCounter38": mccpRelcPlanOutCounter38,
       "mccpRelcPlanOutCounter39": mccpRelcPlanOutCounter39,
       "mccpRelcPlanOutCounter40": mccpRelcPlanOutCounter40,
       "mccpRelcPlanOutCounter41": mccpRelcPlanOutCounter41,
       "mccpRelcPlanOutCounter42": mccpRelcPlanOutCounter42,
       "mccpRelcPlanOutCounter43": mccpRelcPlanOutCounter43,
       "mccpRelcPlanOutCounter44": mccpRelcPlanOutCounter44,
       "mccpRelcPlanOutCounter45": mccpRelcPlanOutCounter45,
       "mccpRelcPlanOutCounter46": mccpRelcPlanOutCounter46,
       "mccpRelcPlanOutCounter47": mccpRelcPlanOutCounter47,
       "mccpRelcPlanOutCounter48": mccpRelcPlanOutCounter48,
       "mccpRelcPlanOutCounter49": mccpRelcPlanOutCounter49,
       "mccpRelcPlanOutCounter50": mccpRelcPlanOutCounter50,
       "mccpRelcPlanOutCounter51": mccpRelcPlanOutCounter51,
       "mccpRelcPlanOutCounter52": mccpRelcPlanOutCounter52,
       "mccpRelcPlanOutCounter53": mccpRelcPlanOutCounter53,
       "mccpRelcPlanOutCounter54": mccpRelcPlanOutCounter54,
       "mccpRelcPlanOutCounter55": mccpRelcPlanOutCounter55,
       "mccpRelcPlanOutCounter56": mccpRelcPlanOutCounter56,
       "mccpRelcPlanOutCounter57": mccpRelcPlanOutCounter57,
       "mccpRelcPlanOutCounter58": mccpRelcPlanOutCounter58,
       "mccpRelcPlanOutCounter59": mccpRelcPlanOutCounter59,
       "mccpRelcPlanOutCounter60": mccpRelcPlanOutCounter60,
       "mccpRelcPlanOutCounter61": mccpRelcPlanOutCounter61,
       "mccpRelcPlanOutCounter62": mccpRelcPlanOutCounter62,
       "mccpRelcPlanOutCounter63": mccpRelcPlanOutCounter63,
       "mccpRelcPlanOutCounter64": mccpRelcPlanOutCounter64,
       "mccpRelcPlanOutCounter65": mccpRelcPlanOutCounter65,
       "mccpRelcPlanOutCounter66": mccpRelcPlanOutCounter66,
       "mccpRelcPlanOutCounter67": mccpRelcPlanOutCounter67,
       "mccpRelcPlanOutCounter68": mccpRelcPlanOutCounter68,
       "mccpRelcPlanOutCounter69": mccpRelcPlanOutCounter69,
       "mccpRelcPlanOutCounter70": mccpRelcPlanOutCounter70,
       "mccpRelcPlanOutCounter71": mccpRelcPlanOutCounter71,
       "mccpRelcPlanOutCounter72": mccpRelcPlanOutCounter72,
       "mccpRelcPlanOutCounter73": mccpRelcPlanOutCounter73,
       "mccpRelcPlanOutCounter74": mccpRelcPlanOutCounter74,
       "mccpRelcPlanOutCounter75": mccpRelcPlanOutCounter75,
       "mccpRelcPlanOutCounter76": mccpRelcPlanOutCounter76,
       "mccpRelcPlanOutCounter77": mccpRelcPlanOutCounter77,
       "mccpRelcPlanOutCounter78": mccpRelcPlanOutCounter78,
       "mccpRelcPlanOutCounter79": mccpRelcPlanOutCounter79,
       "mccpRelcPlanOutCounter80": mccpRelcPlanOutCounter80,
       "mccpRelcPlanOutCounter81": mccpRelcPlanOutCounter81,
       "mccpRelcPlanOutCounter82": mccpRelcPlanOutCounter82,
       "mccpRelcPlanOutCounter83": mccpRelcPlanOutCounter83,
       "mccpRelcPlanOutCounter84": mccpRelcPlanOutCounter84,
       "mccpRelcPlanOutCounter85": mccpRelcPlanOutCounter85,
       "mccpRelcPlanOutCounter86": mccpRelcPlanOutCounter86,
       "mccpRelcPlanOutCounter87": mccpRelcPlanOutCounter87,
       "mccpRelcPlanOutCounter88": mccpRelcPlanOutCounter88,
       "mccpRelcPlanOutCounter89": mccpRelcPlanOutCounter89,
       "mccpRelcPlanOutCounter90": mccpRelcPlanOutCounter90,
       "mccpRelcPlanOutCounter91": mccpRelcPlanOutCounter91,
       "mccpRelcPlanOutCounter92": mccpRelcPlanOutCounter92,
       "mccpRelcPlanOutCounter93": mccpRelcPlanOutCounter93,
       "mccpRelcPlanOutCounter94": mccpRelcPlanOutCounter94,
       "mccpRelcPlanOutCounter95": mccpRelcPlanOutCounter95,
       "mccpRelcPlanOutCounter96": mccpRelcPlanOutCounter96,
       "mccpRelcPlanOutCounter97": mccpRelcPlanOutCounter97,
       "mccpRelcPlanOutCounter98": mccpRelcPlanOutCounter98,
       "mccpRelcPlanOutCounter99": mccpRelcPlanOutCounter99,
       "mccpRelcPlanOutCounter100": mccpRelcPlanOutCounter100,
       "mccpRelcPlanOutCounter101": mccpRelcPlanOutCounter101,
       "mccpRelcPlanOutCounter102": mccpRelcPlanOutCounter102,
       "mccpRelcPlanOutCounter103": mccpRelcPlanOutCounter103,
       "mccpRelcPlanOutCounter104": mccpRelcPlanOutCounter104,
       "mccpRelcPlanOutCounter105": mccpRelcPlanOutCounter105,
       "mccpRelcPlanOutCounter106": mccpRelcPlanOutCounter106,
       "mccpRelcPlanOutCounter107": mccpRelcPlanOutCounter107,
       "mccpRelcPlanOutCounter108": mccpRelcPlanOutCounter108,
       "mccpRelcPlanOutCounter109": mccpRelcPlanOutCounter109,
       "mccpRelcPlanOutCounter110": mccpRelcPlanOutCounter110,
       "mccpRelcPlanOutCounter111": mccpRelcPlanOutCounter111,
       "mccpRelcPlanOutCounter112": mccpRelcPlanOutCounter112,
       "mccpRelcPlanOutCounter113": mccpRelcPlanOutCounter113,
       "mccpRelcPlanOutCounter114": mccpRelcPlanOutCounter114,
       "mccpRelcPlanOutCounter115": mccpRelcPlanOutCounter115,
       "mccpRelcPlanOutCounter116": mccpRelcPlanOutCounter116,
       "mccpRelcPlanOutCounter117": mccpRelcPlanOutCounter117,
       "mccpRelcPlanOutCounter118": mccpRelcPlanOutCounter118,
       "mccpRelcPlanOutCounter119": mccpRelcPlanOutCounter119,
       "mccpRelcPlanOutCounter120": mccpRelcPlanOutCounter120,
       "mccpRelcPlanOutCounter121": mccpRelcPlanOutCounter121,
       "mccpRelcPlanOutCounter122": mccpRelcPlanOutCounter122,
       "mccpRelcPlanOutCounter123": mccpRelcPlanOutCounter123,
       "mccpRelcPlanOutCounter124": mccpRelcPlanOutCounter124,
       "mccpRelcPlanOutCounter125": mccpRelcPlanOutCounter125,
       "mccpRelcPlanOutCounter126": mccpRelcPlanOutCounter126,
       "mccpRelcPlanOutCounter127": mccpRelcPlanOutCounter127,
       "mccpService": mccpService,
       "mccpHumanLogOnOff": mccpHumanLogOnOff,
       "mccpCdrFileFlushStatus": mccpCdrFileFlushStatus}
)
