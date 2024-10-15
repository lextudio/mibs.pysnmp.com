# SNMP MIB module (COM21-HCXALM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COM21-HCXALM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:33 2024
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

(com21,
 com21Hcx) = mibBuilder.importSymbols(
    "COM21-HCX-MIB",
    "com21",
    "com21Hcx")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

com21HcxAlm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 11)
)


# Types definitions



class EpochTime(Integer32):
    """Custom type EpochTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class AlarmSeverity(Integer32):
    """Custom type AlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("critical", 5),
          ("major", 4),
          ("minor", 3),
          ("warning", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Com21HcxCurrAlmGroup_ObjectIdentity = ObjectIdentity
com21HcxCurrAlmGroup = _Com21HcxCurrAlmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 15)
)
_Com21HcxCurrAlmTable_Object = MibTable
com21HcxCurrAlmTable = _Com21HcxCurrAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 15, 1)
)
if mibBuilder.loadTexts:
    com21HcxCurrAlmTable.setStatus("current")
_Com21HcxAlmEntry_Object = MibTableRow
com21HcxAlmEntry = _Com21HcxAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 15, 1, 1)
)
com21HcxAlmEntry.setIndexNames(
    (0, "COM21-HCXALM-MIB", "hcxAlmTrapId"),
    (0, "COM21-HCXALM-MIB", "hcxAlmShelfId"),
    (0, "COM21-HCXALM-MIB", "hcxAlmSlotId"),
    (0, "COM21-HCXALM-MIB", "hcxAlmPortId"),
)
if mibBuilder.loadTexts:
    com21HcxAlmEntry.setStatus("current")
_HcxAlmTrapId_Type = Integer32
_HcxAlmTrapId_Object = MibTableColumn
hcxAlmTrapId = _HcxAlmTrapId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 15, 1, 1, 1),
    _HcxAlmTrapId_Type()
)
hcxAlmTrapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxAlmTrapId.setStatus("current")
_HcxAlmSeverity_Type = AlarmSeverity
_HcxAlmSeverity_Object = MibTableColumn
hcxAlmSeverity = _HcxAlmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 15, 1, 1, 2),
    _HcxAlmSeverity_Type()
)
hcxAlmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxAlmSeverity.setStatus("current")
_HcxAlmTime_Type = EpochTime
_HcxAlmTime_Object = MibTableColumn
hcxAlmTime = _HcxAlmTime_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 15, 1, 1, 3),
    _HcxAlmTime_Type()
)
hcxAlmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxAlmTime.setStatus("current")


class _HcxAlmShelfId_Type(Integer32):
    """Custom type hcxAlmShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HcxAlmShelfId_Type.__name__ = "Integer32"
_HcxAlmShelfId_Object = MibTableColumn
hcxAlmShelfId = _HcxAlmShelfId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 15, 1, 1, 4),
    _HcxAlmShelfId_Type()
)
hcxAlmShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxAlmShelfId.setStatus("current")
_HcxAlmSlotId_Type = Integer32
_HcxAlmSlotId_Object = MibTableColumn
hcxAlmSlotId = _HcxAlmSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 15, 1, 1, 5),
    _HcxAlmSlotId_Type()
)
hcxAlmSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxAlmSlotId.setStatus("current")


class _HcxAlmPortId_Type(Integer32):
    """Custom type hcxAlmPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_HcxAlmPortId_Type.__name__ = "Integer32"
_HcxAlmPortId_Object = MibTableColumn
hcxAlmPortId = _HcxAlmPortId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 15, 1, 1, 6),
    _HcxAlmPortId_Type()
)
hcxAlmPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxAlmPortId.setStatus("current")
_HcxAlmMacAddr_Type = MacAddress
_HcxAlmMacAddr_Object = MibTableColumn
hcxAlmMacAddr = _HcxAlmMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 15, 1, 1, 7),
    _HcxAlmMacAddr_Type()
)
hcxAlmMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxAlmMacAddr.setStatus("current")


class _HcxAlmDataAValid_Type(Integer32):
    """Custom type hcxAlmDataAValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxAlmDataAValid_Type.__name__ = "Integer32"
_HcxAlmDataAValid_Object = MibTableColumn
hcxAlmDataAValid = _HcxAlmDataAValid_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 15, 1, 1, 8),
    _HcxAlmDataAValid_Type()
)
hcxAlmDataAValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxAlmDataAValid.setStatus("current")
_HcxAlmDataA_Type = Integer32
_HcxAlmDataA_Object = MibTableColumn
hcxAlmDataA = _HcxAlmDataA_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 15, 1, 1, 9),
    _HcxAlmDataA_Type()
)
hcxAlmDataA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxAlmDataA.setStatus("current")


class _HcxAlmDataBValid_Type(Integer32):
    """Custom type hcxAlmDataBValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxAlmDataBValid_Type.__name__ = "Integer32"
_HcxAlmDataBValid_Object = MibTableColumn
hcxAlmDataBValid = _HcxAlmDataBValid_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 15, 1, 1, 10),
    _HcxAlmDataBValid_Type()
)
hcxAlmDataBValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxAlmDataBValid.setStatus("current")
_HcxAlmDataB_Type = Integer32
_HcxAlmDataB_Object = MibTableColumn
hcxAlmDataB = _HcxAlmDataB_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 15, 1, 1, 11),
    _HcxAlmDataB_Type()
)
hcxAlmDataB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxAlmDataB.setStatus("current")


class _HcxAlmStrDataValid_Type(Integer32):
    """Custom type hcxAlmStrDataValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxAlmStrDataValid_Type.__name__ = "Integer32"
_HcxAlmStrDataValid_Object = MibTableColumn
hcxAlmStrDataValid = _HcxAlmStrDataValid_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 15, 1, 1, 12),
    _HcxAlmStrDataValid_Type()
)
hcxAlmStrDataValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxAlmStrDataValid.setStatus("current")


class _HcxAlmStrData_Type(DisplayString):
    """Custom type hcxAlmStrData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxAlmStrData_Type.__name__ = "DisplayString"
_HcxAlmStrData_Object = MibTableColumn
hcxAlmStrData = _HcxAlmStrData_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 15, 1, 1, 13),
    _HcxAlmStrData_Type()
)
hcxAlmStrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxAlmStrData.setStatus("current")
_Com21HcxEventLogGroup_ObjectIdentity = ObjectIdentity
com21HcxEventLogGroup = _Com21HcxEventLogGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 16)
)
_Com21HcxEventLogTable_Object = MibTable
com21HcxEventLogTable = _Com21HcxEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 16, 1)
)
if mibBuilder.loadTexts:
    com21HcxEventLogTable.setStatus("current")
_Com21HcxEventLogEntry_Object = MibTableRow
com21HcxEventLogEntry = _Com21HcxEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1)
)
com21HcxEventLogEntry.setIndexNames(
    (0, "COM21-HCXALM-MIB", "hcxEventLogId"),
)
if mibBuilder.loadTexts:
    com21HcxEventLogEntry.setStatus("current")
_HcxEventLogId_Type = Integer32
_HcxEventLogId_Object = MibTableColumn
hcxEventLogId = _HcxEventLogId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1, 1),
    _HcxEventLogId_Type()
)
hcxEventLogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEventLogId.setStatus("current")
_HcxEventLogSeverity_Type = AlarmSeverity
_HcxEventLogSeverity_Object = MibTableColumn
hcxEventLogSeverity = _HcxEventLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1, 2),
    _HcxEventLogSeverity_Type()
)
hcxEventLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEventLogSeverity.setStatus("current")
_HcxEventLogTime_Type = EpochTime
_HcxEventLogTime_Object = MibTableColumn
hcxEventLogTime = _HcxEventLogTime_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1, 3),
    _HcxEventLogTime_Type()
)
hcxEventLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEventLogTime.setStatus("current")


class _HcxEventLogShelfId_Type(Integer32):
    """Custom type hcxEventLogShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HcxEventLogShelfId_Type.__name__ = "Integer32"
_HcxEventLogShelfId_Object = MibTableColumn
hcxEventLogShelfId = _HcxEventLogShelfId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1, 4),
    _HcxEventLogShelfId_Type()
)
hcxEventLogShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEventLogShelfId.setStatus("current")
_HcxEventLogSlotId_Type = Integer32
_HcxEventLogSlotId_Object = MibTableColumn
hcxEventLogSlotId = _HcxEventLogSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1, 5),
    _HcxEventLogSlotId_Type()
)
hcxEventLogSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEventLogSlotId.setStatus("current")


class _HcxEventLogPortId_Type(Integer32):
    """Custom type hcxEventLogPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_HcxEventLogPortId_Type.__name__ = "Integer32"
_HcxEventLogPortId_Object = MibTableColumn
hcxEventLogPortId = _HcxEventLogPortId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1, 6),
    _HcxEventLogPortId_Type()
)
hcxEventLogPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEventLogPortId.setStatus("current")
_HcxEventLogMacAddr_Type = MacAddress
_HcxEventLogMacAddr_Object = MibTableColumn
hcxEventLogMacAddr = _HcxEventLogMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1, 7),
    _HcxEventLogMacAddr_Type()
)
hcxEventLogMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEventLogMacAddr.setStatus("current")
_HcxEventLogTrapId_Type = Integer32
_HcxEventLogTrapId_Object = MibTableColumn
hcxEventLogTrapId = _HcxEventLogTrapId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1, 8),
    _HcxEventLogTrapId_Type()
)
hcxEventLogTrapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEventLogTrapId.setStatus("current")


class _HcxEventLogDataAValid_Type(Integer32):
    """Custom type hcxEventLogDataAValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxEventLogDataAValid_Type.__name__ = "Integer32"
_HcxEventLogDataAValid_Object = MibTableColumn
hcxEventLogDataAValid = _HcxEventLogDataAValid_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1, 9),
    _HcxEventLogDataAValid_Type()
)
hcxEventLogDataAValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEventLogDataAValid.setStatus("current")
_HcxEventLogDataA_Type = Integer32
_HcxEventLogDataA_Object = MibTableColumn
hcxEventLogDataA = _HcxEventLogDataA_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1, 10),
    _HcxEventLogDataA_Type()
)
hcxEventLogDataA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEventLogDataA.setStatus("current")


class _HcxEventLogDataBValid_Type(Integer32):
    """Custom type hcxEventLogDataBValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxEventLogDataBValid_Type.__name__ = "Integer32"
_HcxEventLogDataBValid_Object = MibTableColumn
hcxEventLogDataBValid = _HcxEventLogDataBValid_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1, 11),
    _HcxEventLogDataBValid_Type()
)
hcxEventLogDataBValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEventLogDataBValid.setStatus("current")
_HcxEventLogDataB_Type = Integer32
_HcxEventLogDataB_Object = MibTableColumn
hcxEventLogDataB = _HcxEventLogDataB_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1, 12),
    _HcxEventLogDataB_Type()
)
hcxEventLogDataB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEventLogDataB.setStatus("current")


class _HcxEventStrDataValid_Type(Integer32):
    """Custom type hcxEventStrDataValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxEventStrDataValid_Type.__name__ = "Integer32"
_HcxEventStrDataValid_Object = MibTableColumn
hcxEventStrDataValid = _HcxEventStrDataValid_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1, 13),
    _HcxEventStrDataValid_Type()
)
hcxEventStrDataValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEventStrDataValid.setStatus("current")


class _HcxEventStrData_Type(DisplayString):
    """Custom type hcxEventStrData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxEventStrData_Type.__name__ = "DisplayString"
_HcxEventStrData_Object = MibTableColumn
hcxEventStrData = _HcxEventStrData_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1, 14),
    _HcxEventStrData_Type()
)
hcxEventStrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxEventStrData.setStatus("current")
_Com21HcxAlmSeverityGroup_ObjectIdentity = ObjectIdentity
com21HcxAlmSeverityGroup = _Com21HcxAlmSeverityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 17)
)
_Com21HcxAlmSeverityTable_Object = MibTable
com21HcxAlmSeverityTable = _Com21HcxAlmSeverityTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 17, 1)
)
if mibBuilder.loadTexts:
    com21HcxAlmSeverityTable.setStatus("current")
_Com21HcxAlmSeverityEntry_Object = MibTableRow
com21HcxAlmSeverityEntry = _Com21HcxAlmSeverityEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 17, 1, 1)
)
com21HcxAlmSeverityEntry.setIndexNames(
    (0, "COM21-HCXALM-MIB", "hcxAlmSevTrapId"),
)
if mibBuilder.loadTexts:
    com21HcxAlmSeverityEntry.setStatus("current")
_HcxAlmSevTrapId_Type = Integer32
_HcxAlmSevTrapId_Object = MibTableColumn
hcxAlmSevTrapId = _HcxAlmSevTrapId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 17, 1, 1, 1),
    _HcxAlmSevTrapId_Type()
)
hcxAlmSevTrapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxAlmSevTrapId.setStatus("current")
_HcxSetAlmSeverity_Type = AlarmSeverity
_HcxSetAlmSeverity_Object = MibTableColumn
hcxSetAlmSeverity = _HcxSetAlmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 17, 1, 1, 2),
    _HcxSetAlmSeverity_Type()
)
hcxSetAlmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxSetAlmSeverity.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COM21-HCXALM-MIB",
    **{"EpochTime": EpochTime,
       "AlarmSeverity": AlarmSeverity,
       "com21HcxAlm": com21HcxAlm,
       "com21HcxCurrAlmGroup": com21HcxCurrAlmGroup,
       "com21HcxCurrAlmTable": com21HcxCurrAlmTable,
       "com21HcxAlmEntry": com21HcxAlmEntry,
       "hcxAlmTrapId": hcxAlmTrapId,
       "hcxAlmSeverity": hcxAlmSeverity,
       "hcxAlmTime": hcxAlmTime,
       "hcxAlmShelfId": hcxAlmShelfId,
       "hcxAlmSlotId": hcxAlmSlotId,
       "hcxAlmPortId": hcxAlmPortId,
       "hcxAlmMacAddr": hcxAlmMacAddr,
       "hcxAlmDataAValid": hcxAlmDataAValid,
       "hcxAlmDataA": hcxAlmDataA,
       "hcxAlmDataBValid": hcxAlmDataBValid,
       "hcxAlmDataB": hcxAlmDataB,
       "hcxAlmStrDataValid": hcxAlmStrDataValid,
       "hcxAlmStrData": hcxAlmStrData,
       "com21HcxEventLogGroup": com21HcxEventLogGroup,
       "com21HcxEventLogTable": com21HcxEventLogTable,
       "com21HcxEventLogEntry": com21HcxEventLogEntry,
       "hcxEventLogId": hcxEventLogId,
       "hcxEventLogSeverity": hcxEventLogSeverity,
       "hcxEventLogTime": hcxEventLogTime,
       "hcxEventLogShelfId": hcxEventLogShelfId,
       "hcxEventLogSlotId": hcxEventLogSlotId,
       "hcxEventLogPortId": hcxEventLogPortId,
       "hcxEventLogMacAddr": hcxEventLogMacAddr,
       "hcxEventLogTrapId": hcxEventLogTrapId,
       "hcxEventLogDataAValid": hcxEventLogDataAValid,
       "hcxEventLogDataA": hcxEventLogDataA,
       "hcxEventLogDataBValid": hcxEventLogDataBValid,
       "hcxEventLogDataB": hcxEventLogDataB,
       "hcxEventStrDataValid": hcxEventStrDataValid,
       "hcxEventStrData": hcxEventStrData,
       "com21HcxAlmSeverityGroup": com21HcxAlmSeverityGroup,
       "com21HcxAlmSeverityTable": com21HcxAlmSeverityTable,
       "com21HcxAlmSeverityEntry": com21HcxAlmSeverityEntry,
       "hcxAlmSevTrapId": hcxAlmSevTrapId,
       "hcxSetAlmSeverity": hcxSetAlmSeverity}
)
