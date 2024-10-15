# SNMP MIB module (Nortel-MsCarrier-MscPassport-ExternalTimingE1MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-ExternalTimingE1MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:20 2024
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

_MscLpEE1_ObjectIdentity = ObjectIdentity
mscLpEE1 = _MscLpEE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 29)
)
_MscLpEE1RowStatusTable_Object = MibTable
mscLpEE1RowStatusTable = _MscLpEE1RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 29, 1)
)
if mibBuilder.loadTexts:
    mscLpEE1RowStatusTable.setStatus("mandatory")
_MscLpEE1RowStatusEntry_Object = MibTableRow
mscLpEE1RowStatusEntry = _MscLpEE1RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 29, 1, 1)
)
mscLpEE1RowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ExternalTimingE1MIB", "mscLpEE1Index"),
)
if mibBuilder.loadTexts:
    mscLpEE1RowStatusEntry.setStatus("mandatory")
_MscLpEE1RowStatus_Type = RowStatus
_MscLpEE1RowStatus_Object = MibTableColumn
mscLpEE1RowStatus = _MscLpEE1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 29, 1, 1, 1),
    _MscLpEE1RowStatus_Type()
)
mscLpEE1RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEE1RowStatus.setStatus("mandatory")
_MscLpEE1ComponentName_Type = DisplayString
_MscLpEE1ComponentName_Object = MibTableColumn
mscLpEE1ComponentName = _MscLpEE1ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 29, 1, 1, 2),
    _MscLpEE1ComponentName_Type()
)
mscLpEE1ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEE1ComponentName.setStatus("mandatory")
_MscLpEE1StorageType_Type = StorageType
_MscLpEE1StorageType_Object = MibTableColumn
mscLpEE1StorageType = _MscLpEE1StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 29, 1, 1, 4),
    _MscLpEE1StorageType_Type()
)
mscLpEE1StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEE1StorageType.setStatus("mandatory")


class _MscLpEE1Index_Type(Integer32):
    """Custom type mscLpEE1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MscLpEE1Index_Type.__name__ = "Integer32"
_MscLpEE1Index_Object = MibTableColumn
mscLpEE1Index = _MscLpEE1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 29, 1, 1, 10),
    _MscLpEE1Index_Type()
)
mscLpEE1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEE1Index.setStatus("mandatory")
_MscLpEE1OperStatusTable_Object = MibTable
mscLpEE1OperStatusTable = _MscLpEE1OperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 29, 14)
)
if mibBuilder.loadTexts:
    mscLpEE1OperStatusTable.setStatus("mandatory")
_MscLpEE1OperStatusEntry_Object = MibTableRow
mscLpEE1OperStatusEntry = _MscLpEE1OperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 29, 14, 1)
)
mscLpEE1OperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ExternalTimingE1MIB", "mscLpEE1Index"),
)
if mibBuilder.loadTexts:
    mscLpEE1OperStatusEntry.setStatus("mandatory")


class _MscLpEE1SnmpOperStatus_Type(Integer32):
    """Custom type mscLpEE1SnmpOperStatus based on Integer32"""
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


_MscLpEE1SnmpOperStatus_Type.__name__ = "Integer32"
_MscLpEE1SnmpOperStatus_Object = MibTableColumn
mscLpEE1SnmpOperStatus = _MscLpEE1SnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 29, 14, 1, 1),
    _MscLpEE1SnmpOperStatus_Type()
)
mscLpEE1SnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEE1SnmpOperStatus.setStatus("mandatory")
_MscLpEE1StateTable_Object = MibTable
mscLpEE1StateTable = _MscLpEE1StateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 29, 15)
)
if mibBuilder.loadTexts:
    mscLpEE1StateTable.setStatus("mandatory")
_MscLpEE1StateEntry_Object = MibTableRow
mscLpEE1StateEntry = _MscLpEE1StateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 29, 15, 1)
)
mscLpEE1StateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ExternalTimingE1MIB", "mscLpEE1Index"),
)
if mibBuilder.loadTexts:
    mscLpEE1StateEntry.setStatus("mandatory")


class _MscLpEE1AdminState_Type(Integer32):
    """Custom type mscLpEE1AdminState based on Integer32"""
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


_MscLpEE1AdminState_Type.__name__ = "Integer32"
_MscLpEE1AdminState_Object = MibTableColumn
mscLpEE1AdminState = _MscLpEE1AdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 29, 15, 1, 1),
    _MscLpEE1AdminState_Type()
)
mscLpEE1AdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEE1AdminState.setStatus("mandatory")


class _MscLpEE1OperationalState_Type(Integer32):
    """Custom type mscLpEE1OperationalState based on Integer32"""
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


_MscLpEE1OperationalState_Type.__name__ = "Integer32"
_MscLpEE1OperationalState_Object = MibTableColumn
mscLpEE1OperationalState = _MscLpEE1OperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 29, 15, 1, 2),
    _MscLpEE1OperationalState_Type()
)
mscLpEE1OperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEE1OperationalState.setStatus("mandatory")


class _MscLpEE1UsageState_Type(Integer32):
    """Custom type mscLpEE1UsageState based on Integer32"""
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


_MscLpEE1UsageState_Type.__name__ = "Integer32"
_MscLpEE1UsageState_Object = MibTableColumn
mscLpEE1UsageState = _MscLpEE1UsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 29, 15, 1, 3),
    _MscLpEE1UsageState_Type()
)
mscLpEE1UsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEE1UsageState.setStatus("mandatory")


class _MscLpEE1AvailabilityStatus_Type(OctetString):
    """Custom type mscLpEE1AvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscLpEE1AvailabilityStatus_Type.__name__ = "OctetString"
_MscLpEE1AvailabilityStatus_Object = MibTableColumn
mscLpEE1AvailabilityStatus = _MscLpEE1AvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 29, 15, 1, 4),
    _MscLpEE1AvailabilityStatus_Type()
)
mscLpEE1AvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEE1AvailabilityStatus.setStatus("mandatory")


class _MscLpEE1ProceduralStatus_Type(OctetString):
    """Custom type mscLpEE1ProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscLpEE1ProceduralStatus_Type.__name__ = "OctetString"
_MscLpEE1ProceduralStatus_Object = MibTableColumn
mscLpEE1ProceduralStatus = _MscLpEE1ProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 29, 15, 1, 5),
    _MscLpEE1ProceduralStatus_Type()
)
mscLpEE1ProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEE1ProceduralStatus.setStatus("mandatory")


class _MscLpEE1ControlStatus_Type(OctetString):
    """Custom type mscLpEE1ControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscLpEE1ControlStatus_Type.__name__ = "OctetString"
_MscLpEE1ControlStatus_Object = MibTableColumn
mscLpEE1ControlStatus = _MscLpEE1ControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 29, 15, 1, 6),
    _MscLpEE1ControlStatus_Type()
)
mscLpEE1ControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEE1ControlStatus.setStatus("mandatory")


class _MscLpEE1AlarmStatus_Type(OctetString):
    """Custom type mscLpEE1AlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscLpEE1AlarmStatus_Type.__name__ = "OctetString"
_MscLpEE1AlarmStatus_Object = MibTableColumn
mscLpEE1AlarmStatus = _MscLpEE1AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 29, 15, 1, 7),
    _MscLpEE1AlarmStatus_Type()
)
mscLpEE1AlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEE1AlarmStatus.setStatus("mandatory")


class _MscLpEE1StandbyStatus_Type(Integer32):
    """Custom type mscLpEE1StandbyStatus based on Integer32"""
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


_MscLpEE1StandbyStatus_Type.__name__ = "Integer32"
_MscLpEE1StandbyStatus_Object = MibTableColumn
mscLpEE1StandbyStatus = _MscLpEE1StandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 29, 15, 1, 8),
    _MscLpEE1StandbyStatus_Type()
)
mscLpEE1StandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEE1StandbyStatus.setStatus("mandatory")


class _MscLpEE1UnknownStatus_Type(Integer32):
    """Custom type mscLpEE1UnknownStatus based on Integer32"""
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


_MscLpEE1UnknownStatus_Type.__name__ = "Integer32"
_MscLpEE1UnknownStatus_Object = MibTableColumn
mscLpEE1UnknownStatus = _MscLpEE1UnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 29, 15, 1, 9),
    _MscLpEE1UnknownStatus_Type()
)
mscLpEE1UnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEE1UnknownStatus.setStatus("mandatory")
_MscLpEE1OperTable_Object = MibTable
mscLpEE1OperTable = _MscLpEE1OperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 29, 16)
)
if mibBuilder.loadTexts:
    mscLpEE1OperTable.setStatus("mandatory")
_MscLpEE1OperEntry_Object = MibTableRow
mscLpEE1OperEntry = _MscLpEE1OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 29, 16, 1)
)
mscLpEE1OperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ExternalTimingE1MIB", "mscLpEE1Index"),
)
if mibBuilder.loadTexts:
    mscLpEE1OperEntry.setStatus("mandatory")


class _MscLpEE1LosAlarm_Type(Integer32):
    """Custom type mscLpEE1LosAlarm based on Integer32"""
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


_MscLpEE1LosAlarm_Type.__name__ = "Integer32"
_MscLpEE1LosAlarm_Object = MibTableColumn
mscLpEE1LosAlarm = _MscLpEE1LosAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 29, 16, 1, 1),
    _MscLpEE1LosAlarm_Type()
)
mscLpEE1LosAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEE1LosAlarm.setStatus("mandatory")


class _MscLpEE1LofAlarm_Type(Integer32):
    """Custom type mscLpEE1LofAlarm based on Integer32"""
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


_MscLpEE1LofAlarm_Type.__name__ = "Integer32"
_MscLpEE1LofAlarm_Object = MibTableColumn
mscLpEE1LofAlarm = _MscLpEE1LofAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 29, 16, 1, 2),
    _MscLpEE1LofAlarm_Type()
)
mscLpEE1LofAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEE1LofAlarm.setStatus("mandatory")


class _MscLpEE1RxAisAlarm_Type(Integer32):
    """Custom type mscLpEE1RxAisAlarm based on Integer32"""
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


_MscLpEE1RxAisAlarm_Type.__name__ = "Integer32"
_MscLpEE1RxAisAlarm_Object = MibTableColumn
mscLpEE1RxAisAlarm = _MscLpEE1RxAisAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 29, 16, 1, 3),
    _MscLpEE1RxAisAlarm_Type()
)
mscLpEE1RxAisAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEE1RxAisAlarm.setStatus("mandatory")
_ExternalTimingE1MIB_ObjectIdentity = ObjectIdentity
externalTimingE1MIB = _ExternalTimingE1MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 152)
)
_ExternalTimingE1Group_ObjectIdentity = ObjectIdentity
externalTimingE1Group = _ExternalTimingE1Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 152, 1)
)
_ExternalTimingE1GroupCA_ObjectIdentity = ObjectIdentity
externalTimingE1GroupCA = _ExternalTimingE1GroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 152, 1, 1)
)
_ExternalTimingE1GroupCA02_ObjectIdentity = ObjectIdentity
externalTimingE1GroupCA02 = _ExternalTimingE1GroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 152, 1, 1, 3)
)
_ExternalTimingE1GroupCA02A_ObjectIdentity = ObjectIdentity
externalTimingE1GroupCA02A = _ExternalTimingE1GroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 152, 1, 1, 3, 2)
)
_ExternalTimingE1Capabilities_ObjectIdentity = ObjectIdentity
externalTimingE1Capabilities = _ExternalTimingE1Capabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 152, 3)
)
_ExternalTimingE1CapabilitiesCA_ObjectIdentity = ObjectIdentity
externalTimingE1CapabilitiesCA = _ExternalTimingE1CapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 152, 3, 1)
)
_ExternalTimingE1CapabilitiesCA02_ObjectIdentity = ObjectIdentity
externalTimingE1CapabilitiesCA02 = _ExternalTimingE1CapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 152, 3, 1, 3)
)
_ExternalTimingE1CapabilitiesCA02A_ObjectIdentity = ObjectIdentity
externalTimingE1CapabilitiesCA02A = _ExternalTimingE1CapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 152, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-ExternalTimingE1MIB",
    **{"mscLpEE1": mscLpEE1,
       "mscLpEE1RowStatusTable": mscLpEE1RowStatusTable,
       "mscLpEE1RowStatusEntry": mscLpEE1RowStatusEntry,
       "mscLpEE1RowStatus": mscLpEE1RowStatus,
       "mscLpEE1ComponentName": mscLpEE1ComponentName,
       "mscLpEE1StorageType": mscLpEE1StorageType,
       "mscLpEE1Index": mscLpEE1Index,
       "mscLpEE1OperStatusTable": mscLpEE1OperStatusTable,
       "mscLpEE1OperStatusEntry": mscLpEE1OperStatusEntry,
       "mscLpEE1SnmpOperStatus": mscLpEE1SnmpOperStatus,
       "mscLpEE1StateTable": mscLpEE1StateTable,
       "mscLpEE1StateEntry": mscLpEE1StateEntry,
       "mscLpEE1AdminState": mscLpEE1AdminState,
       "mscLpEE1OperationalState": mscLpEE1OperationalState,
       "mscLpEE1UsageState": mscLpEE1UsageState,
       "mscLpEE1AvailabilityStatus": mscLpEE1AvailabilityStatus,
       "mscLpEE1ProceduralStatus": mscLpEE1ProceduralStatus,
       "mscLpEE1ControlStatus": mscLpEE1ControlStatus,
       "mscLpEE1AlarmStatus": mscLpEE1AlarmStatus,
       "mscLpEE1StandbyStatus": mscLpEE1StandbyStatus,
       "mscLpEE1UnknownStatus": mscLpEE1UnknownStatus,
       "mscLpEE1OperTable": mscLpEE1OperTable,
       "mscLpEE1OperEntry": mscLpEE1OperEntry,
       "mscLpEE1LosAlarm": mscLpEE1LosAlarm,
       "mscLpEE1LofAlarm": mscLpEE1LofAlarm,
       "mscLpEE1RxAisAlarm": mscLpEE1RxAisAlarm,
       "externalTimingE1MIB": externalTimingE1MIB,
       "externalTimingE1Group": externalTimingE1Group,
       "externalTimingE1GroupCA": externalTimingE1GroupCA,
       "externalTimingE1GroupCA02": externalTimingE1GroupCA02,
       "externalTimingE1GroupCA02A": externalTimingE1GroupCA02A,
       "externalTimingE1Capabilities": externalTimingE1Capabilities,
       "externalTimingE1CapabilitiesCA": externalTimingE1CapabilitiesCA,
       "externalTimingE1CapabilitiesCA02": externalTimingE1CapabilitiesCA02,
       "externalTimingE1CapabilitiesCA02A": externalTimingE1CapabilitiesCA02A}
)
