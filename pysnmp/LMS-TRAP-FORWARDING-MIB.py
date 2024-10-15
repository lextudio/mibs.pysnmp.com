# SNMP MIB module (LMS-TRAP-FORWARDING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LMS-TRAP-FORWARDING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:17 2024
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



class TimeInterval(Integer32):
    """Custom type TimeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lotus_ObjectIdentity = ObjectIdentity
lotus = _Lotus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334)
)
_Notes_ObjectIdentity = ObjectIdentity
notes = _Notes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 1)
)
_Lcs_ObjectIdentity = ObjectIdentity
lcs = _Lcs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 2)
)
_Softswitch_ObjectIdentity = ObjectIdentity
softswitch = _Softswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 3)
)
_Common_mibs_ObjectIdentity = ObjectIdentity
common_mibs = _Common_mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 3, 1)
)
_Lms_ObjectIdentity = ObjectIdentity
lms = _Lms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 3, 2)
)
_LmsTrap_ObjectIdentity = ObjectIdentity
lmsTrap = _LmsTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 2)
)


class _EventFwdTableModificationStatus_Type(Integer32):
    """Custom type eventFwdTableModificationStatus based on Integer32"""
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
        *(("no-access", 2),
          ("read-create", 5),
          ("read-modify", 4),
          ("read-only", 3),
          ("unknown", 1))
    )


_EventFwdTableModificationStatus_Type.__name__ = "Integer32"
_EventFwdTableModificationStatus_Object = MibScalar
eventFwdTableModificationStatus = _EventFwdTableModificationStatus_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 1),
    _EventFwdTableModificationStatus_Type()
)
eventFwdTableModificationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventFwdTableModificationStatus.setStatus("mandatory")
_NextFwdEntryIndex_Type = Integer32
_NextFwdEntryIndex_Object = MibScalar
nextFwdEntryIndex = _NextFwdEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 2),
    _NextFwdEntryIndex_Type()
)
nextFwdEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextFwdEntryIndex.setStatus("mandatory")
_TrapWindowTime_Type = TimeInterval
_TrapWindowTime_Object = MibScalar
trapWindowTime = _TrapWindowTime_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 3),
    _TrapWindowTime_Type()
)
trapWindowTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapWindowTime.setStatus("mandatory")
_MaxTrapsPerWindow_Type = Integer32
_MaxTrapsPerWindow_Object = MibScalar
maxTrapsPerWindow = _MaxTrapsPerWindow_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 4),
    _MaxTrapsPerWindow_Type()
)
maxTrapsPerWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxTrapsPerWindow.setStatus("mandatory")
_NumDroppedMaxPerWindowTraps_Type = Counter32
_NumDroppedMaxPerWindowTraps_Object = MibScalar
numDroppedMaxPerWindowTraps = _NumDroppedMaxPerWindowTraps_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 5),
    _NumDroppedMaxPerWindowTraps_Type()
)
numDroppedMaxPerWindowTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numDroppedMaxPerWindowTraps.setStatus("mandatory")
_LmsEventFwdTable_Object = MibTable
lmsEventFwdTable = _LmsEventFwdTable_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 6)
)
if mibBuilder.loadTexts:
    lmsEventFwdTable.setStatus("mandatory")
_LmsEventFwdEntry_Object = MibTableRow
lmsEventFwdEntry = _LmsEventFwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 6, 1)
)
lmsEventFwdEntry.setIndexNames(
    (0, "LMS-TRAP-FORWARDING-MIB", "fwdEntryIndex"),
)
if mibBuilder.loadTexts:
    lmsEventFwdEntry.setStatus("mandatory")
_FwdEntryIndex_Type = Integer32
_FwdEntryIndex_Object = MibTableColumn
fwdEntryIndex = _FwdEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 6, 1, 1),
    _FwdEntryIndex_Type()
)
fwdEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwdEntryIndex.setStatus("mandatory")


class _RowStatus_Type(Integer32):
    """Custom type rowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_RowStatus_Type.__name__ = "Integer32"
_RowStatus_Object = MibTableColumn
rowStatus = _RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 6, 1, 2),
    _RowStatus_Type()
)
rowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rowStatus.setStatus("mandatory")
_DestinationNetAddr_Type = IpAddress
_DestinationNetAddr_Object = MibTableColumn
destinationNetAddr = _DestinationNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 6, 1, 3),
    _DestinationNetAddr_Type()
)
destinationNetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destinationNetAddr.setStatus("mandatory")
_DestinationCommunity_Type = DisplayString
_DestinationCommunity_Object = MibTableColumn
destinationCommunity = _DestinationCommunity_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 6, 1, 4),
    _DestinationCommunity_Type()
)
destinationCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destinationCommunity.setStatus("mandatory")
_DestinationPort_Type = Integer32
_DestinationPort_Object = MibTableColumn
destinationPort = _DestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 6, 1, 5),
    _DestinationPort_Type()
)
destinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destinationPort.setStatus("mandatory")


class _ForwardingEnabled_Type(Integer32):
    """Custom type forwardingEnabled based on Integer32"""
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


_ForwardingEnabled_Type.__name__ = "Integer32"
_ForwardingEnabled_Object = MibTableColumn
forwardingEnabled = _ForwardingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 6, 1, 6),
    _ForwardingEnabled_Type()
)
forwardingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forwardingEnabled.setStatus("mandatory")
_ForwardingFilterName_Type = DisplayString
_ForwardingFilterName_Object = MibTableColumn
forwardingFilterName = _ForwardingFilterName_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 6, 1, 7),
    _ForwardingFilterName_Type()
)
forwardingFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forwardingFilterName.setStatus("mandatory")
_LastTrapSequenceNumber_Type = Integer32
_LastTrapSequenceNumber_Object = MibTableColumn
lastTrapSequenceNumber = _LastTrapSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 6, 1, 8),
    _LastTrapSequenceNumber_Type()
)
lastTrapSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastTrapSequenceNumber.setStatus("mandatory")
_LastTrapTime_Type = TimeTicks
_LastTrapTime_Object = MibTableColumn
lastTrapTime = _LastTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 6, 1, 9),
    _LastTrapTime_Type()
)
lastTrapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastTrapTime.setStatus("mandatory")
_NumDroppedDisabledTraps_Type = Counter32
_NumDroppedDisabledTraps_Object = MibTableColumn
numDroppedDisabledTraps = _NumDroppedDisabledTraps_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 2, 6, 1, 10),
    _NumDroppedDisabledTraps_Type()
)
numDroppedDisabledTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numDroppedDisabledTraps.setStatus("mandatory")
_LmsTrapData_ObjectIdentity = ObjectIdentity
lmsTrapData = _LmsTrapData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 3)
)


class _LmsEvComponentType_Type(Integer32):
    """Custom type lmsEvComponentType based on Integer32"""
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
        *(("core", 3),
          ("global", 1),
          ("mea", 7),
          ("mta", 4),
          ("mta-group", 5),
          ("other", 8),
          ("queue", 6),
          ("switch", 2))
    )


_LmsEvComponentType_Type.__name__ = "Integer32"
_LmsEvComponentType_Object = MibScalar
lmsEvComponentType = _LmsEvComponentType_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 3, 1),
    _LmsEvComponentType_Type()
)
lmsEvComponentType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lmsEvComponentType.setStatus("mandatory")
_LmsEvComponentDN_Type = DisplayString
_LmsEvComponentDN_Object = MibScalar
lmsEvComponentDN = _LmsEvComponentDN_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 3, 2),
    _LmsEvComponentDN_Type()
)
lmsEvComponentDN.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lmsEvComponentDN.setStatus("mandatory")
_LmsEvDbId_Type = Integer32
_LmsEvDbId_Object = MibScalar
lmsEvDbId = _LmsEvDbId_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 3, 3),
    _LmsEvDbId_Type()
)
lmsEvDbId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lmsEvDbId.setStatus("mandatory")
_LmsEvOID_Type = Integer32
_LmsEvOID_Object = MibScalar
lmsEvOID = _LmsEvOID_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 3, 4),
    _LmsEvOID_Type()
)
lmsEvOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lmsEvOID.setStatus("mandatory")
_NumLmsEvSequences_Type = Counter32
_NumLmsEvSequences_Object = MibScalar
numLmsEvSequences = _NumLmsEvSequences_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 3, 5),
    _NumLmsEvSequences_Type()
)
numLmsEvSequences.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    numLmsEvSequences.setStatus("mandatory")
_LmsEvSeverity_Type = Integer32
_LmsEvSeverity_Object = MibScalar
lmsEvSeverity = _LmsEvSeverity_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 3, 6),
    _LmsEvSeverity_Type()
)
lmsEvSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lmsEvSeverity.setStatus("mandatory")
_LmsEvSupportingText_Type = DisplayString
_LmsEvSupportingText_Object = MibScalar
lmsEvSupportingText = _LmsEvSupportingText_Object(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 3, 7),
    _LmsEvSupportingText_Type()
)
lmsEvSupportingText.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lmsEvSupportingText.setStatus("mandatory")

# Managed Objects groups


# Notification objects

lmsCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 0, 1)
)
lmsCritical.setObjects(
      *(("LMS-TRAP-FORWARDING-MIB", "lmsEvComponentType"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvComponentDN"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvDbId"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvOID"),
        ("LMS-TRAP-FORWARDING-MIB", "numLmsEvSequences"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvSeverity"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvSupportingText"))
)
if mibBuilder.loadTexts:
    lmsCritical.setStatus(
        ""
    )

lmsMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 0, 2)
)
lmsMajor.setObjects(
      *(("LMS-TRAP-FORWARDING-MIB", "lmsEvComponentType"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvComponentDN"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvDbId"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvOID"),
        ("LMS-TRAP-FORWARDING-MIB", "numLmsEvSequences"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvSeverity"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvSupportingText"))
)
if mibBuilder.loadTexts:
    lmsMajor.setStatus(
        ""
    )

lmsMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 0, 3)
)
lmsMinor.setObjects(
      *(("LMS-TRAP-FORWARDING-MIB", "lmsEvComponentType"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvComponentDN"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvDbId"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvOID"),
        ("LMS-TRAP-FORWARDING-MIB", "numLmsEvSequences"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvSeverity"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvSupportingText"))
)
if mibBuilder.loadTexts:
    lmsMinor.setStatus(
        ""
    )

lmsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 0, 4)
)
lmsWarning.setObjects(
      *(("LMS-TRAP-FORWARDING-MIB", "lmsEvComponentType"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvComponentDN"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvDbId"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvOID"),
        ("LMS-TRAP-FORWARDING-MIB", "numLmsEvSequences"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvSeverity"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvSupportingText"))
)
if mibBuilder.loadTexts:
    lmsWarning.setStatus(
        ""
    )

lmsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 0, 5)
)
lmsCleared.setObjects(
      *(("LMS-TRAP-FORWARDING-MIB", "lmsEvComponentType"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvComponentDN"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvDbId"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvOID"),
        ("LMS-TRAP-FORWARDING-MIB", "numLmsEvSequences"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvSeverity"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvSupportingText"))
)
if mibBuilder.loadTexts:
    lmsCleared.setStatus(
        ""
    )

lmsInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 334, 3, 2, 0, 6)
)
lmsInformational.setObjects(
      *(("LMS-TRAP-FORWARDING-MIB", "lmsEvComponentType"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvComponentDN"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvDbId"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvOID"),
        ("LMS-TRAP-FORWARDING-MIB", "numLmsEvSequences"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvSeverity"),
        ("LMS-TRAP-FORWARDING-MIB", "lmsEvSupportingText"))
)
if mibBuilder.loadTexts:
    lmsInformational.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LMS-TRAP-FORWARDING-MIB",
    **{"TimeInterval": TimeInterval,
       "lotus": lotus,
       "notes": notes,
       "lcs": lcs,
       "softswitch": softswitch,
       "common-mibs": common_mibs,
       "lms": lms,
       "lmsCritical": lmsCritical,
       "lmsMajor": lmsMajor,
       "lmsMinor": lmsMinor,
       "lmsWarning": lmsWarning,
       "lmsCleared": lmsCleared,
       "lmsInformational": lmsInformational,
       "lmsTrap": lmsTrap,
       "eventFwdTableModificationStatus": eventFwdTableModificationStatus,
       "nextFwdEntryIndex": nextFwdEntryIndex,
       "trapWindowTime": trapWindowTime,
       "maxTrapsPerWindow": maxTrapsPerWindow,
       "numDroppedMaxPerWindowTraps": numDroppedMaxPerWindowTraps,
       "lmsEventFwdTable": lmsEventFwdTable,
       "lmsEventFwdEntry": lmsEventFwdEntry,
       "fwdEntryIndex": fwdEntryIndex,
       "rowStatus": rowStatus,
       "destinationNetAddr": destinationNetAddr,
       "destinationCommunity": destinationCommunity,
       "destinationPort": destinationPort,
       "forwardingEnabled": forwardingEnabled,
       "forwardingFilterName": forwardingFilterName,
       "lastTrapSequenceNumber": lastTrapSequenceNumber,
       "lastTrapTime": lastTrapTime,
       "numDroppedDisabledTraps": numDroppedDisabledTraps,
       "lmsTrapData": lmsTrapData,
       "lmsEvComponentType": lmsEvComponentType,
       "lmsEvComponentDN": lmsEvComponentDN,
       "lmsEvDbId": lmsEvDbId,
       "lmsEvOID": lmsEvOID,
       "numLmsEvSequences": numLmsEvSequences,
       "lmsEvSeverity": lmsEvSeverity,
       "lmsEvSupportingText": lmsEvSupportingText}
)
