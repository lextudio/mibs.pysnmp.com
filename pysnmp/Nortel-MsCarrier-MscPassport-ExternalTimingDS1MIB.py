# SNMP MIB module (Nortel-MsCarrier-MscPassport-ExternalTimingDS1MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-ExternalTimingDS1MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:19 2024
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

(mscLp,
 mscLpIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB",
    "mscLp",
    "mscLpIndex")

(DisplayString,
 Integer32,
 RowStatus,
 StorageType) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "DisplayString",
    "Integer32",
    "RowStatus",
    "StorageType")

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscPassportMIBs")

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

_MscLpEDS1_ObjectIdentity = ObjectIdentity
mscLpEDS1 = _MscLpEDS1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28)
)
_MscLpEDS1RowStatusTable_Object = MibTable
mscLpEDS1RowStatusTable = _MscLpEDS1RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28, 1)
)
if mibBuilder.loadTexts:
    mscLpEDS1RowStatusTable.setStatus("mandatory")
_MscLpEDS1RowStatusEntry_Object = MibTableRow
mscLpEDS1RowStatusEntry = _MscLpEDS1RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28, 1, 1)
)
mscLpEDS1RowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ExternalTimingDS1MIB", "mscLpEDS1Index"),
)
if mibBuilder.loadTexts:
    mscLpEDS1RowStatusEntry.setStatus("mandatory")
_MscLpEDS1RowStatus_Type = RowStatus
_MscLpEDS1RowStatus_Object = MibTableColumn
mscLpEDS1RowStatus = _MscLpEDS1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28, 1, 1, 1),
    _MscLpEDS1RowStatus_Type()
)
mscLpEDS1RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEDS1RowStatus.setStatus("mandatory")
_MscLpEDS1ComponentName_Type = DisplayString
_MscLpEDS1ComponentName_Object = MibTableColumn
mscLpEDS1ComponentName = _MscLpEDS1ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28, 1, 1, 2),
    _MscLpEDS1ComponentName_Type()
)
mscLpEDS1ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEDS1ComponentName.setStatus("mandatory")
_MscLpEDS1StorageType_Type = StorageType
_MscLpEDS1StorageType_Object = MibTableColumn
mscLpEDS1StorageType = _MscLpEDS1StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28, 1, 1, 4),
    _MscLpEDS1StorageType_Type()
)
mscLpEDS1StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEDS1StorageType.setStatus("mandatory")


class _MscLpEDS1Index_Type(Integer32):
    """Custom type mscLpEDS1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MscLpEDS1Index_Type.__name__ = "Integer32"
_MscLpEDS1Index_Object = MibTableColumn
mscLpEDS1Index = _MscLpEDS1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28, 1, 1, 10),
    _MscLpEDS1Index_Type()
)
mscLpEDS1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEDS1Index.setStatus("mandatory")
_MscLpEDS1ProvTable_Object = MibTable
mscLpEDS1ProvTable = _MscLpEDS1ProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28, 10)
)
if mibBuilder.loadTexts:
    mscLpEDS1ProvTable.setStatus("mandatory")
_MscLpEDS1ProvEntry_Object = MibTableRow
mscLpEDS1ProvEntry = _MscLpEDS1ProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28, 10, 1)
)
mscLpEDS1ProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ExternalTimingDS1MIB", "mscLpEDS1Index"),
)
if mibBuilder.loadTexts:
    mscLpEDS1ProvEntry.setStatus("mandatory")


class _MscLpEDS1LineType_Type(Integer32):
    """Custom type mscLpEDS1LineType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("d4", 0),
          ("esf", 1))
    )


_MscLpEDS1LineType_Type.__name__ = "Integer32"
_MscLpEDS1LineType_Object = MibTableColumn
mscLpEDS1LineType = _MscLpEDS1LineType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28, 10, 1, 1),
    _MscLpEDS1LineType_Type()
)
mscLpEDS1LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEDS1LineType.setStatus("mandatory")
_MscLpEDS1OperStatusTable_Object = MibTable
mscLpEDS1OperStatusTable = _MscLpEDS1OperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28, 14)
)
if mibBuilder.loadTexts:
    mscLpEDS1OperStatusTable.setStatus("mandatory")
_MscLpEDS1OperStatusEntry_Object = MibTableRow
mscLpEDS1OperStatusEntry = _MscLpEDS1OperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28, 14, 1)
)
mscLpEDS1OperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ExternalTimingDS1MIB", "mscLpEDS1Index"),
)
if mibBuilder.loadTexts:
    mscLpEDS1OperStatusEntry.setStatus("mandatory")


class _MscLpEDS1SnmpOperStatus_Type(Integer32):
    """Custom type mscLpEDS1SnmpOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscLpEDS1SnmpOperStatus_Type.__name__ = "Integer32"
_MscLpEDS1SnmpOperStatus_Object = MibTableColumn
mscLpEDS1SnmpOperStatus = _MscLpEDS1SnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28, 14, 1, 1),
    _MscLpEDS1SnmpOperStatus_Type()
)
mscLpEDS1SnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEDS1SnmpOperStatus.setStatus("mandatory")
_MscLpEDS1StateTable_Object = MibTable
mscLpEDS1StateTable = _MscLpEDS1StateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28, 15)
)
if mibBuilder.loadTexts:
    mscLpEDS1StateTable.setStatus("mandatory")
_MscLpEDS1StateEntry_Object = MibTableRow
mscLpEDS1StateEntry = _MscLpEDS1StateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28, 15, 1)
)
mscLpEDS1StateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ExternalTimingDS1MIB", "mscLpEDS1Index"),
)
if mibBuilder.loadTexts:
    mscLpEDS1StateEntry.setStatus("mandatory")


class _MscLpEDS1AdminState_Type(Integer32):
    """Custom type mscLpEDS1AdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_MscLpEDS1AdminState_Type.__name__ = "Integer32"
_MscLpEDS1AdminState_Object = MibTableColumn
mscLpEDS1AdminState = _MscLpEDS1AdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28, 15, 1, 1),
    _MscLpEDS1AdminState_Type()
)
mscLpEDS1AdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEDS1AdminState.setStatus("mandatory")


class _MscLpEDS1OperationalState_Type(Integer32):
    """Custom type mscLpEDS1OperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MscLpEDS1OperationalState_Type.__name__ = "Integer32"
_MscLpEDS1OperationalState_Object = MibTableColumn
mscLpEDS1OperationalState = _MscLpEDS1OperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28, 15, 1, 2),
    _MscLpEDS1OperationalState_Type()
)
mscLpEDS1OperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEDS1OperationalState.setStatus("mandatory")


class _MscLpEDS1UsageState_Type(Integer32):
    """Custom type mscLpEDS1UsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_MscLpEDS1UsageState_Type.__name__ = "Integer32"
_MscLpEDS1UsageState_Object = MibTableColumn
mscLpEDS1UsageState = _MscLpEDS1UsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28, 15, 1, 3),
    _MscLpEDS1UsageState_Type()
)
mscLpEDS1UsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEDS1UsageState.setStatus("mandatory")


class _MscLpEDS1AvailabilityStatus_Type(OctetString):
    """Custom type mscLpEDS1AvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscLpEDS1AvailabilityStatus_Type.__name__ = "OctetString"
_MscLpEDS1AvailabilityStatus_Object = MibTableColumn
mscLpEDS1AvailabilityStatus = _MscLpEDS1AvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28, 15, 1, 4),
    _MscLpEDS1AvailabilityStatus_Type()
)
mscLpEDS1AvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEDS1AvailabilityStatus.setStatus("mandatory")


class _MscLpEDS1ProceduralStatus_Type(OctetString):
    """Custom type mscLpEDS1ProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscLpEDS1ProceduralStatus_Type.__name__ = "OctetString"
_MscLpEDS1ProceduralStatus_Object = MibTableColumn
mscLpEDS1ProceduralStatus = _MscLpEDS1ProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28, 15, 1, 5),
    _MscLpEDS1ProceduralStatus_Type()
)
mscLpEDS1ProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEDS1ProceduralStatus.setStatus("mandatory")


class _MscLpEDS1ControlStatus_Type(OctetString):
    """Custom type mscLpEDS1ControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscLpEDS1ControlStatus_Type.__name__ = "OctetString"
_MscLpEDS1ControlStatus_Object = MibTableColumn
mscLpEDS1ControlStatus = _MscLpEDS1ControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28, 15, 1, 6),
    _MscLpEDS1ControlStatus_Type()
)
mscLpEDS1ControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEDS1ControlStatus.setStatus("mandatory")


class _MscLpEDS1AlarmStatus_Type(OctetString):
    """Custom type mscLpEDS1AlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscLpEDS1AlarmStatus_Type.__name__ = "OctetString"
_MscLpEDS1AlarmStatus_Object = MibTableColumn
mscLpEDS1AlarmStatus = _MscLpEDS1AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28, 15, 1, 7),
    _MscLpEDS1AlarmStatus_Type()
)
mscLpEDS1AlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEDS1AlarmStatus.setStatus("mandatory")


class _MscLpEDS1StandbyStatus_Type(Integer32):
    """Custom type mscLpEDS1StandbyStatus based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              15)
        )
    )
    namedValues = NamedValues(
        *(("coldStandby", 1),
          ("hotStandby", 0),
          ("notSet", 15),
          ("providingService", 2))
    )


_MscLpEDS1StandbyStatus_Type.__name__ = "Integer32"
_MscLpEDS1StandbyStatus_Object = MibTableColumn
mscLpEDS1StandbyStatus = _MscLpEDS1StandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28, 15, 1, 8),
    _MscLpEDS1StandbyStatus_Type()
)
mscLpEDS1StandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEDS1StandbyStatus.setStatus("mandatory")


class _MscLpEDS1UnknownStatus_Type(Integer32):
    """Custom type mscLpEDS1UnknownStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_MscLpEDS1UnknownStatus_Type.__name__ = "Integer32"
_MscLpEDS1UnknownStatus_Object = MibTableColumn
mscLpEDS1UnknownStatus = _MscLpEDS1UnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28, 15, 1, 9),
    _MscLpEDS1UnknownStatus_Type()
)
mscLpEDS1UnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEDS1UnknownStatus.setStatus("mandatory")
_MscLpEDS1OperTable_Object = MibTable
mscLpEDS1OperTable = _MscLpEDS1OperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28, 16)
)
if mibBuilder.loadTexts:
    mscLpEDS1OperTable.setStatus("mandatory")
_MscLpEDS1OperEntry_Object = MibTableRow
mscLpEDS1OperEntry = _MscLpEDS1OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28, 16, 1)
)
mscLpEDS1OperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ExternalTimingDS1MIB", "mscLpEDS1Index"),
)
if mibBuilder.loadTexts:
    mscLpEDS1OperEntry.setStatus("mandatory")


class _MscLpEDS1LosAlarm_Type(Integer32):
    """Custom type mscLpEDS1LosAlarm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_MscLpEDS1LosAlarm_Type.__name__ = "Integer32"
_MscLpEDS1LosAlarm_Object = MibTableColumn
mscLpEDS1LosAlarm = _MscLpEDS1LosAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28, 16, 1, 1),
    _MscLpEDS1LosAlarm_Type()
)
mscLpEDS1LosAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEDS1LosAlarm.setStatus("mandatory")


class _MscLpEDS1LofAlarm_Type(Integer32):
    """Custom type mscLpEDS1LofAlarm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_MscLpEDS1LofAlarm_Type.__name__ = "Integer32"
_MscLpEDS1LofAlarm_Object = MibTableColumn
mscLpEDS1LofAlarm = _MscLpEDS1LofAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28, 16, 1, 2),
    _MscLpEDS1LofAlarm_Type()
)
mscLpEDS1LofAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEDS1LofAlarm.setStatus("mandatory")


class _MscLpEDS1RxAisAlarm_Type(Integer32):
    """Custom type mscLpEDS1RxAisAlarm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_MscLpEDS1RxAisAlarm_Type.__name__ = "Integer32"
_MscLpEDS1RxAisAlarm_Object = MibTableColumn
mscLpEDS1RxAisAlarm = _MscLpEDS1RxAisAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 28, 16, 1, 3),
    _MscLpEDS1RxAisAlarm_Type()
)
mscLpEDS1RxAisAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEDS1RxAisAlarm.setStatus("mandatory")
_ExternalTimingDS1MIB_ObjectIdentity = ObjectIdentity
externalTimingDS1MIB = _ExternalTimingDS1MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 151)
)
_ExternalTimingDS1Group_ObjectIdentity = ObjectIdentity
externalTimingDS1Group = _ExternalTimingDS1Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 151, 1)
)
_ExternalTimingDS1GroupCA_ObjectIdentity = ObjectIdentity
externalTimingDS1GroupCA = _ExternalTimingDS1GroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 151, 1, 1)
)
_ExternalTimingDS1GroupCA02_ObjectIdentity = ObjectIdentity
externalTimingDS1GroupCA02 = _ExternalTimingDS1GroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 151, 1, 1, 3)
)
_ExternalTimingDS1GroupCA02A_ObjectIdentity = ObjectIdentity
externalTimingDS1GroupCA02A = _ExternalTimingDS1GroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 151, 1, 1, 3, 2)
)
_ExternalTimingDS1Capabilities_ObjectIdentity = ObjectIdentity
externalTimingDS1Capabilities = _ExternalTimingDS1Capabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 151, 3)
)
_ExternalTimingDS1CapabilitiesCA_ObjectIdentity = ObjectIdentity
externalTimingDS1CapabilitiesCA = _ExternalTimingDS1CapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 151, 3, 1)
)
_ExternalTimingDS1CapabilitiesCA02_ObjectIdentity = ObjectIdentity
externalTimingDS1CapabilitiesCA02 = _ExternalTimingDS1CapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 151, 3, 1, 3)
)
_ExternalTimingDS1CapabilitiesCA02A_ObjectIdentity = ObjectIdentity
externalTimingDS1CapabilitiesCA02A = _ExternalTimingDS1CapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 151, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-ExternalTimingDS1MIB",
    **{"mscLpEDS1": mscLpEDS1,
       "mscLpEDS1RowStatusTable": mscLpEDS1RowStatusTable,
       "mscLpEDS1RowStatusEntry": mscLpEDS1RowStatusEntry,
       "mscLpEDS1RowStatus": mscLpEDS1RowStatus,
       "mscLpEDS1ComponentName": mscLpEDS1ComponentName,
       "mscLpEDS1StorageType": mscLpEDS1StorageType,
       "mscLpEDS1Index": mscLpEDS1Index,
       "mscLpEDS1ProvTable": mscLpEDS1ProvTable,
       "mscLpEDS1ProvEntry": mscLpEDS1ProvEntry,
       "mscLpEDS1LineType": mscLpEDS1LineType,
       "mscLpEDS1OperStatusTable": mscLpEDS1OperStatusTable,
       "mscLpEDS1OperStatusEntry": mscLpEDS1OperStatusEntry,
       "mscLpEDS1SnmpOperStatus": mscLpEDS1SnmpOperStatus,
       "mscLpEDS1StateTable": mscLpEDS1StateTable,
       "mscLpEDS1StateEntry": mscLpEDS1StateEntry,
       "mscLpEDS1AdminState": mscLpEDS1AdminState,
       "mscLpEDS1OperationalState": mscLpEDS1OperationalState,
       "mscLpEDS1UsageState": mscLpEDS1UsageState,
       "mscLpEDS1AvailabilityStatus": mscLpEDS1AvailabilityStatus,
       "mscLpEDS1ProceduralStatus": mscLpEDS1ProceduralStatus,
       "mscLpEDS1ControlStatus": mscLpEDS1ControlStatus,
       "mscLpEDS1AlarmStatus": mscLpEDS1AlarmStatus,
       "mscLpEDS1StandbyStatus": mscLpEDS1StandbyStatus,
       "mscLpEDS1UnknownStatus": mscLpEDS1UnknownStatus,
       "mscLpEDS1OperTable": mscLpEDS1OperTable,
       "mscLpEDS1OperEntry": mscLpEDS1OperEntry,
       "mscLpEDS1LosAlarm": mscLpEDS1LosAlarm,
       "mscLpEDS1LofAlarm": mscLpEDS1LofAlarm,
       "mscLpEDS1RxAisAlarm": mscLpEDS1RxAisAlarm,
       "externalTimingDS1MIB": externalTimingDS1MIB,
       "externalTimingDS1Group": externalTimingDS1Group,
       "externalTimingDS1GroupCA": externalTimingDS1GroupCA,
       "externalTimingDS1GroupCA02": externalTimingDS1GroupCA02,
       "externalTimingDS1GroupCA02A": externalTimingDS1GroupCA02A,
       "externalTimingDS1Capabilities": externalTimingDS1Capabilities,
       "externalTimingDS1CapabilitiesCA": externalTimingDS1CapabilitiesCA,
       "externalTimingDS1CapabilitiesCA02": externalTimingDS1CapabilitiesCA02,
       "externalTimingDS1CapabilitiesCA02A": externalTimingDS1CapabilitiesCA02A}
)
