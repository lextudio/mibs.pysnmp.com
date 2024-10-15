# SNMP MIB module (NNCGNI00X8-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NNCGNI00X8-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:29 2024
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

(nncExtRptr,) = mibBuilder.importSymbols(
    "NNCGNI00X1-SMI",
    "nncExtRptr")

(PositionIndex,) = mibBuilder.importSymbols(
    "NNCGNI00X4-MIB",
    "PositionIndex")

(PortIndex,) = mibBuilder.importSymbols(
    "NNCGNI00X7-MIB",
    "PortIndex")

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



class RptrPortStatus(Integer32):
    """Custom type RptrPortStatus based on Integer32"""
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
        *(("autoIsolate", 4),
          ("busyOut", 3),
          ("forcedIsolate", 2),
          ("inService", 1),
          ("linkDown", 5))
    )





class RptrIsolationStatus(Integer32):
    """Custom type RptrIsolationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPartitioning", 1),
          ("partitionedPort", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NncExtRptrModuleTable_Object = MibTable
nncExtRptrModuleTable = _NncExtRptrModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 11, 1)
)
if mibBuilder.loadTexts:
    nncExtRptrModuleTable.setStatus("mandatory")
_NncExtRptrModuleEntry_Object = MibTableRow
nncExtRptrModuleEntry = _NncExtRptrModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 11, 1, 1)
)
nncExtRptrModuleEntry.setIndexNames(
    (0, "NNCGNI00X8-MIB", "nncExtRptrModulePositionIndex"),
)
if mibBuilder.loadTexts:
    nncExtRptrModuleEntry.setStatus("mandatory")
_NncExtRptrModulePositionIndex_Type = PositionIndex
_NncExtRptrModulePositionIndex_Object = MibTableColumn
nncExtRptrModulePositionIndex = _NncExtRptrModulePositionIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 11, 1, 1, 1),
    _NncExtRptrModulePositionIndex_Type()
)
nncExtRptrModulePositionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtRptrModulePositionIndex.setStatus("mandatory")


class _NncExtRptrModuleAdminMode_Type(Integer32):
    """Custom type nncExtRptrModuleAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cascade", 2),
          ("repeater", 1))
    )


_NncExtRptrModuleAdminMode_Type.__name__ = "Integer32"
_NncExtRptrModuleAdminMode_Object = MibTableColumn
nncExtRptrModuleAdminMode = _NncExtRptrModuleAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 11, 1, 1, 2),
    _NncExtRptrModuleAdminMode_Type()
)
nncExtRptrModuleAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtRptrModuleAdminMode.setStatus("mandatory")


class _NncExtRptrModuleOperMode_Type(Integer32):
    """Custom type nncExtRptrModuleOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cascade", 2),
          ("notPresent", 3),
          ("repeater", 1))
    )


_NncExtRptrModuleOperMode_Type.__name__ = "Integer32"
_NncExtRptrModuleOperMode_Object = MibTableColumn
nncExtRptrModuleOperMode = _NncExtRptrModuleOperMode_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 11, 1, 1, 3),
    _NncExtRptrModuleOperMode_Type()
)
nncExtRptrModuleOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtRptrModuleOperMode.setStatus("mandatory")


class _NncExtRptrModuleStatisticsMask_Type(Integer32):
    """Custom type nncExtRptrModuleStatisticsMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NncExtRptrModuleStatisticsMask_Type.__name__ = "Integer32"
_NncExtRptrModuleStatisticsMask_Object = MibTableColumn
nncExtRptrModuleStatisticsMask = _NncExtRptrModuleStatisticsMask_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 11, 1, 1, 4),
    _NncExtRptrModuleStatisticsMask_Type()
)
nncExtRptrModuleStatisticsMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtRptrModuleStatisticsMask.setStatus("mandatory")
_NncExtRptrPortTable_Object = MibTable
nncExtRptrPortTable = _NncExtRptrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 11, 2)
)
if mibBuilder.loadTexts:
    nncExtRptrPortTable.setStatus("mandatory")
_NncExtRptrPortEntry_Object = MibTableRow
nncExtRptrPortEntry = _NncExtRptrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 11, 2, 1)
)
nncExtRptrPortEntry.setIndexNames(
    (0, "NNCGNI00X8-MIB", "nncExtRptrPortPositionIndex"),
    (0, "NNCGNI00X8-MIB", "nncExtRptrPortIndex"),
)
if mibBuilder.loadTexts:
    nncExtRptrPortEntry.setStatus("mandatory")
_NncExtRptrPortPositionIndex_Type = PositionIndex
_NncExtRptrPortPositionIndex_Object = MibTableColumn
nncExtRptrPortPositionIndex = _NncExtRptrPortPositionIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 11, 2, 1, 1),
    _NncExtRptrPortPositionIndex_Type()
)
nncExtRptrPortPositionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtRptrPortPositionIndex.setStatus("mandatory")
_NncExtRptrPortIndex_Type = PortIndex
_NncExtRptrPortIndex_Object = MibTableColumn
nncExtRptrPortIndex = _NncExtRptrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 11, 2, 1, 2),
    _NncExtRptrPortIndex_Type()
)
nncExtRptrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtRptrPortIndex.setStatus("mandatory")


class _NncExtRptrPortAlarmEnable_Type(Integer32):
    """Custom type nncExtRptrPortAlarmEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_NncExtRptrPortAlarmEnable_Type.__name__ = "Integer32"
_NncExtRptrPortAlarmEnable_Object = MibTableColumn
nncExtRptrPortAlarmEnable = _NncExtRptrPortAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 11, 2, 1, 3),
    _NncExtRptrPortAlarmEnable_Type()
)
nncExtRptrPortAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtRptrPortAlarmEnable.setStatus("mandatory")
_NncExtRptrPortLinkIntegrityLosses_Type = Counter32
_NncExtRptrPortLinkIntegrityLosses_Object = MibTableColumn
nncExtRptrPortLinkIntegrityLosses = _NncExtRptrPortLinkIntegrityLosses_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 11, 2, 1, 4),
    _NncExtRptrPortLinkIntegrityLosses_Type()
)
nncExtRptrPortLinkIntegrityLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtRptrPortLinkIntegrityLosses.setStatus("mandatory")
_NncExtRptrPortAutoPartitions_Type = Counter32
_NncExtRptrPortAutoPartitions_Object = MibTableColumn
nncExtRptrPortAutoPartitions = _NncExtRptrPortAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 11, 2, 1, 5),
    _NncExtRptrPortAutoPartitions_Type()
)
nncExtRptrPortAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtRptrPortAutoPartitions.setStatus("mandatory")
_NncExtRptrPortAdminDisables_Type = Counter32
_NncExtRptrPortAdminDisables_Object = MibTableColumn
nncExtRptrPortAdminDisables = _NncExtRptrPortAdminDisables_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 11, 2, 1, 6),
    _NncExtRptrPortAdminDisables_Type()
)
nncExtRptrPortAdminDisables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtRptrPortAdminDisables.setStatus("mandatory")
_NncExtRptrPortEvents_Type = Counter32
_NncExtRptrPortEvents_Object = MibTableColumn
nncExtRptrPortEvents = _NncExtRptrPortEvents_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 11, 2, 1, 7),
    _NncExtRptrPortEvents_Type()
)
nncExtRptrPortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtRptrPortEvents.setStatus("mandatory")
_NncExtRptrPortLastChange_Type = TimeTicks
_NncExtRptrPortLastChange_Object = MibTableColumn
nncExtRptrPortLastChange = _NncExtRptrPortLastChange_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 11, 2, 1, 8),
    _NncExtRptrPortLastChange_Type()
)
nncExtRptrPortLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtRptrPortLastChange.setStatus("mandatory")


class _NncExtRptrPortOperStatus_Type(Integer32):
    """Custom type nncExtRptrPortOperStatus based on Integer32"""
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
        *(("autoIsolate", 4),
          ("busyOut", 3),
          ("forcedIsolate", 2),
          ("inService", 1),
          ("linkDown", 5))
    )


_NncExtRptrPortOperStatus_Type.__name__ = "Integer32"
_NncExtRptrPortOperStatus_Object = MibTableColumn
nncExtRptrPortOperStatus = _NncExtRptrPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 11, 2, 1, 9),
    _NncExtRptrPortOperStatus_Type()
)
nncExtRptrPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtRptrPortOperStatus.setStatus("mandatory")


class _NncExtRptrPortIsolation_Type(Integer32):
    """Custom type nncExtRptrPortIsolation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPartitioning", 1),
          ("partitionedPort", 2))
    )


_NncExtRptrPortIsolation_Type.__name__ = "Integer32"
_NncExtRptrPortIsolation_Object = MibTableColumn
nncExtRptrPortIsolation = _NncExtRptrPortIsolation_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 11, 2, 1, 10),
    _NncExtRptrPortIsolation_Type()
)
nncExtRptrPortIsolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtRptrPortIsolation.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NNCGNI00X8-MIB",
    **{"RptrPortStatus": RptrPortStatus,
       "RptrIsolationStatus": RptrIsolationStatus,
       "nncExtRptrModuleTable": nncExtRptrModuleTable,
       "nncExtRptrModuleEntry": nncExtRptrModuleEntry,
       "nncExtRptrModulePositionIndex": nncExtRptrModulePositionIndex,
       "nncExtRptrModuleAdminMode": nncExtRptrModuleAdminMode,
       "nncExtRptrModuleOperMode": nncExtRptrModuleOperMode,
       "nncExtRptrModuleStatisticsMask": nncExtRptrModuleStatisticsMask,
       "nncExtRptrPortTable": nncExtRptrPortTable,
       "nncExtRptrPortEntry": nncExtRptrPortEntry,
       "nncExtRptrPortPositionIndex": nncExtRptrPortPositionIndex,
       "nncExtRptrPortIndex": nncExtRptrPortIndex,
       "nncExtRptrPortAlarmEnable": nncExtRptrPortAlarmEnable,
       "nncExtRptrPortLinkIntegrityLosses": nncExtRptrPortLinkIntegrityLosses,
       "nncExtRptrPortAutoPartitions": nncExtRptrPortAutoPartitions,
       "nncExtRptrPortAdminDisables": nncExtRptrPortAdminDisables,
       "nncExtRptrPortEvents": nncExtRptrPortEvents,
       "nncExtRptrPortLastChange": nncExtRptrPortLastChange,
       "nncExtRptrPortOperStatus": nncExtRptrPortOperStatus,
       "nncExtRptrPortIsolation": nncExtRptrPortIsolation}
)
