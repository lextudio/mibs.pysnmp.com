# SNMP MIB module (ADTRAN-ATLASIQ-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-ATLASIQ-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:29 2024
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

(adMgmt,
 adProdPhysAddress,
 adProducts) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adMgmt",
    "adProdPhysAddress",
    "adProducts")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(frCircuitDlci,
 frCircuitIfIndex) = mibBuilder.importSymbols(
    "RFC1315-MIB",
    "frCircuitDlci",
    "frCircuitIfIndex")

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
    "NotificationType",
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

_AdATLASIQ_ObjectIdentity = ObjectIdentity
adATLASIQ = _AdATLASIQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 1, 155)
)
_AdATLASmg_ObjectIdentity = ObjectIdentity
adATLASmg = _AdATLASmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 154)
)
_AdATLASIQmg_ObjectIdentity = ObjectIdentity
adATLASIQmg = _AdATLASIQmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 155)
)
_AdATLASIQSystemConfig_ObjectIdentity = ObjectIdentity
adATLASIQSystemConfig = _AdATLASIQSystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 155, 1)
)
_AdATLASIQTOD_Type = DisplayString
_AdATLASIQTOD_Object = MibScalar
adATLASIQTOD = _AdATLASIQTOD_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 155, 1, 1),
    _AdATLASIQTOD_Type()
)
adATLASIQTOD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLASIQTOD.setStatus("mandatory")
_AdATLASIQDate_Type = DisplayString
_AdATLASIQDate_Object = MibScalar
adATLASIQDate = _AdATLASIQDate_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 155, 1, 2),
    _AdATLASIQDate_Type()
)
adATLASIQDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLASIQDate.setStatus("mandatory")
_AdATLASIQNetPortConfig_ObjectIdentity = ObjectIdentity
adATLASIQNetPortConfig = _AdATLASIQNetPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 155, 2)
)


class _AdATLASIQNetPortMaxPVCs_Type(Integer32):
    """Custom type adATLASIQNetPortMaxPVCs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AdATLASIQNetPortMaxPVCs_Type.__name__ = "Integer32"
_AdATLASIQNetPortMaxPVCs_Object = MibScalar
adATLASIQNetPortMaxPVCs = _AdATLASIQNetPortMaxPVCs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 155, 2, 20),
    _AdATLASIQNetPortMaxPVCs_Type()
)
adATLASIQNetPortMaxPVCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLASIQNetPortMaxPVCs.setStatus("mandatory")
_AdATLASIQNetPortHistIntervals_Type = Integer32
_AdATLASIQNetPortHistIntervals_Object = MibScalar
adATLASIQNetPortHistIntervals = _AdATLASIQNetPortHistIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 155, 2, 21),
    _AdATLASIQNetPortHistIntervals_Type()
)
adATLASIQNetPortHistIntervals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLASIQNetPortHistIntervals.setStatus("mandatory")
_AdATLASIQNetPortHistIntervalsAvailable_Type = Integer32
_AdATLASIQNetPortHistIntervalsAvailable_Object = MibScalar
adATLASIQNetPortHistIntervalsAvailable = _AdATLASIQNetPortHistIntervalsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 155, 2, 22),
    _AdATLASIQNetPortHistIntervalsAvailable_Type()
)
adATLASIQNetPortHistIntervalsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASIQNetPortHistIntervalsAvailable.setStatus("mandatory")
_AdATLASIQDtePortConfig_ObjectIdentity = ObjectIdentity
adATLASIQDtePortConfig = _AdATLASIQDtePortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 155, 3)
)
_AdATLASIQPvcConfig_ObjectIdentity = ObjectIdentity
adATLASIQPvcConfig = _AdATLASIQPvcConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 155, 4)
)
_AdATLASIQCurrentStatus_ObjectIdentity = ObjectIdentity
adATLASIQCurrentStatus = _AdATLASIQCurrentStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 155, 5)
)
_AdATLASIQIntT1Status_ObjectIdentity = ObjectIdentity
adATLASIQIntT1Status = _AdATLASIQIntT1Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 155, 6)
)
_AdATLASIQDayT1Status_ObjectIdentity = ObjectIdentity
adATLASIQDayT1Status = _AdATLASIQDayT1Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 155, 7)
)
_AdATLASIQDiagnostic_ObjectIdentity = ObjectIdentity
adATLASIQDiagnostic = _AdATLASIQDiagnostic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 155, 8)
)
_AdATLASIQ1406Time_ObjectIdentity = ObjectIdentity
adATLASIQ1406Time = _AdATLASIQ1406Time_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 155, 9)
)
_AdATLASIQ1406TimeTable_Object = MibTable
adATLASIQ1406TimeTable = _AdATLASIQ1406TimeTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 155, 9, 1)
)
if mibBuilder.loadTexts:
    adATLASIQ1406TimeTable.setStatus("mandatory")
_AdATLASIQ1406TimeEntry_Object = MibTableRow
adATLASIQ1406TimeEntry = _AdATLASIQ1406TimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 155, 9, 1, 1)
)
adATLASIQ1406TimeEntry.setIndexNames(
    (0, "ADTRAN-ATLASIQ-MIB", "adATLASIQ1406TimeSlotIndex"),
)
if mibBuilder.loadTexts:
    adATLASIQ1406TimeEntry.setStatus("mandatory")
_AdATLASIQ1406TimeSlotIndex_Type = Integer32
_AdATLASIQ1406TimeSlotIndex_Object = MibTableColumn
adATLASIQ1406TimeSlotIndex = _AdATLASIQ1406TimeSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 155, 9, 1, 1, 1),
    _AdATLASIQ1406TimeSlotIndex_Type()
)
adATLASIQ1406TimeSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASIQ1406TimeSlotIndex.setStatus("mandatory")
_AdATLASIQ1406TimeStamp_Type = DisplayString
_AdATLASIQ1406TimeStamp_Object = MibTableColumn
adATLASIQ1406TimeStamp = _AdATLASIQ1406TimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 155, 9, 1, 1, 2),
    _AdATLASIQ1406TimeStamp_Type()
)
adATLASIQ1406TimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASIQ1406TimeStamp.setStatus("mandatory")
_AdATLASIQDBUConfig_ObjectIdentity = ObjectIdentity
adATLASIQDBUConfig = _AdATLASIQDBUConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 155, 10)
)
_AdATLASIQIntDBUStatus_ObjectIdentity = ObjectIdentity
adATLASIQIntDBUStatus = _AdATLASIQIntDBUStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 155, 11)
)
_AdATLASIQDayDBUStatus_ObjectIdentity = ObjectIdentity
adATLASIQDayDBUStatus = _AdATLASIQDayDBUStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 155, 12)
)
_AdATLASIQTrapManager_ObjectIdentity = ObjectIdentity
adATLASIQTrapManager = _AdATLASIQTrapManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 155, 13)
)

# Managed Objects groups


# Notification objects

adATLASFrSwToBkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15440)
)
adATLASFrSwToBkup.setObjects(
      *(("RFC1315-MIB", "frCircuitIfIndex"),
        ("RFC1315-MIB", "frCircuitDlci"))
)
if mibBuilder.loadTexts:
    adATLASFrSwToBkup.setStatus(
        ""
    )

adATLASFrSwToPrimary = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15441)
)
adATLASFrSwToPrimary.setObjects(
      *(("RFC1315-MIB", "frCircuitIfIndex"),
        ("RFC1315-MIB", "frCircuitDlci"))
)
if mibBuilder.loadTexts:
    adATLASFrSwToPrimary.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-ATLASIQ-MIB",
    **{"adATLASIQ": adATLASIQ,
       "adATLASmg": adATLASmg,
       "adATLASFrSwToBkup": adATLASFrSwToBkup,
       "adATLASFrSwToPrimary": adATLASFrSwToPrimary,
       "adATLASIQmg": adATLASIQmg,
       "adATLASIQSystemConfig": adATLASIQSystemConfig,
       "adATLASIQTOD": adATLASIQTOD,
       "adATLASIQDate": adATLASIQDate,
       "adATLASIQNetPortConfig": adATLASIQNetPortConfig,
       "adATLASIQNetPortMaxPVCs": adATLASIQNetPortMaxPVCs,
       "adATLASIQNetPortHistIntervals": adATLASIQNetPortHistIntervals,
       "adATLASIQNetPortHistIntervalsAvailable": adATLASIQNetPortHistIntervalsAvailable,
       "adATLASIQDtePortConfig": adATLASIQDtePortConfig,
       "adATLASIQPvcConfig": adATLASIQPvcConfig,
       "adATLASIQCurrentStatus": adATLASIQCurrentStatus,
       "adATLASIQIntT1Status": adATLASIQIntT1Status,
       "adATLASIQDayT1Status": adATLASIQDayT1Status,
       "adATLASIQDiagnostic": adATLASIQDiagnostic,
       "adATLASIQ1406Time": adATLASIQ1406Time,
       "adATLASIQ1406TimeTable": adATLASIQ1406TimeTable,
       "adATLASIQ1406TimeEntry": adATLASIQ1406TimeEntry,
       "adATLASIQ1406TimeSlotIndex": adATLASIQ1406TimeSlotIndex,
       "adATLASIQ1406TimeStamp": adATLASIQ1406TimeStamp,
       "adATLASIQDBUConfig": adATLASIQDBUConfig,
       "adATLASIQIntDBUStatus": adATLASIQIntDBUStatus,
       "adATLASIQDayDBUStatus": adATLASIQDayDBUStatus,
       "adATLASIQTrapManager": adATLASIQTrapManager}
)
