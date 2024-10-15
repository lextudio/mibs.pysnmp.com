# SNMP MIB module (NBS-PRBS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBS-PRBS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:57 2024
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

(nbs,
 nbsCmmcChassisIndex,
 nbsCmmcPortIndex,
 nbsCmmcPortName,
 nbsCmmcSlotIndex) = mibBuilder.importSymbols(
    "NBS-CMMC-MIB",
    "nbs",
    "nbsCmmcChassisIndex",
    "nbsCmmcPortIndex",
    "nbsCmmcPortName",
    "nbsCmmcSlotIndex")

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

nbsPrbsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 212)
)


# Types definitions



class InterfaceIndex(Integer32):
    """Custom type InterfaceIndex based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsPrbsPatternGrp_ObjectIdentity = ObjectIdentity
nbsPrbsPatternGrp = _NbsPrbsPatternGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 212, 1)
)
if mibBuilder.loadTexts:
    nbsPrbsPatternGrp.setStatus("current")
_NbsPrbsPatternTableSize_Type = Unsigned32
_NbsPrbsPatternTableSize_Object = MibScalar
nbsPrbsPatternTableSize = _NbsPrbsPatternTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 1, 1),
    _NbsPrbsPatternTableSize_Type()
)
nbsPrbsPatternTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPrbsPatternTableSize.setStatus("current")
_NbsPrbsPatternTable_Object = MibTable
nbsPrbsPatternTable = _NbsPrbsPatternTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 1, 2)
)
if mibBuilder.loadTexts:
    nbsPrbsPatternTable.setStatus("current")
_NbsPrbsPatternEntry_Object = MibTableRow
nbsPrbsPatternEntry = _NbsPrbsPatternEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 1, 2, 1)
)
nbsPrbsPatternEntry.setIndexNames(
    (0, "NBS-PRBS-MIB", "nbsPrbsPatternIndex"),
)
if mibBuilder.loadTexts:
    nbsPrbsPatternEntry.setStatus("current")
_NbsPrbsPatternIndex_Type = Integer32
_NbsPrbsPatternIndex_Object = MibTableColumn
nbsPrbsPatternIndex = _NbsPrbsPatternIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 1, 2, 1, 1),
    _NbsPrbsPatternIndex_Type()
)
nbsPrbsPatternIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsPrbsPatternIndex.setStatus("current")
_NbsPrbsPatternName_Type = DisplayString
_NbsPrbsPatternName_Object = MibTableColumn
nbsPrbsPatternName = _NbsPrbsPatternName_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 1, 2, 1, 2),
    _NbsPrbsPatternName_Type()
)
nbsPrbsPatternName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPrbsPatternName.setStatus("current")
_NbsPrbsPatternDesc_Type = DisplayString
_NbsPrbsPatternDesc_Object = MibTableColumn
nbsPrbsPatternDesc = _NbsPrbsPatternDesc_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 1, 2, 1, 3),
    _NbsPrbsPatternDesc_Type()
)
nbsPrbsPatternDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPrbsPatternDesc.setStatus("current")
_NbsPrbsGenGrp_ObjectIdentity = ObjectIdentity
nbsPrbsGenGrp = _NbsPrbsGenGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 212, 2)
)
if mibBuilder.loadTexts:
    nbsPrbsGenGrp.setStatus("current")
_NbsPrbsGenTableSize_Type = Unsigned32
_NbsPrbsGenTableSize_Object = MibScalar
nbsPrbsGenTableSize = _NbsPrbsGenTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 2, 1),
    _NbsPrbsGenTableSize_Type()
)
nbsPrbsGenTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPrbsGenTableSize.setStatus("current")
_NbsPrbsGenTable_Object = MibTable
nbsPrbsGenTable = _NbsPrbsGenTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 2, 2)
)
if mibBuilder.loadTexts:
    nbsPrbsGenTable.setStatus("current")
_NbsPrbsGenEntry_Object = MibTableRow
nbsPrbsGenEntry = _NbsPrbsGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 2, 2, 1)
)
nbsPrbsGenEntry.setIndexNames(
    (0, "NBS-PRBS-MIB", "nbsPrbsGenIfIndex"),
)
if mibBuilder.loadTexts:
    nbsPrbsGenEntry.setStatus("current")
_NbsPrbsGenIfIndex_Type = InterfaceIndex
_NbsPrbsGenIfIndex_Object = MibTableColumn
nbsPrbsGenIfIndex = _NbsPrbsGenIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 2, 2, 1, 1),
    _NbsPrbsGenIfIndex_Type()
)
nbsPrbsGenIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsPrbsGenIfIndex.setStatus("current")
_NbsPrbsGenPatternCaps_Type = OctetString
_NbsPrbsGenPatternCaps_Object = MibTableColumn
nbsPrbsGenPatternCaps = _NbsPrbsGenPatternCaps_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 2, 2, 1, 2),
    _NbsPrbsGenPatternCaps_Type()
)
nbsPrbsGenPatternCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPrbsGenPatternCaps.setStatus("current")
_NbsPrbsGenPatternIndex_Type = Integer32
_NbsPrbsGenPatternIndex_Object = MibTableColumn
nbsPrbsGenPatternIndex = _NbsPrbsGenPatternIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 2, 2, 1, 3),
    _NbsPrbsGenPatternIndex_Type()
)
nbsPrbsGenPatternIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsPrbsGenPatternIndex.setStatus("current")


class _NbsPrbsGenDurationMax_Type(Integer32):
    """Custom type nbsPrbsGenDurationMax based on Integer32"""
    defaultValue = 0


_NbsPrbsGenDurationMax_Object = MibTableColumn
nbsPrbsGenDurationMax = _NbsPrbsGenDurationMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 2, 2, 1, 4),
    _NbsPrbsGenDurationMax_Type()
)
nbsPrbsGenDurationMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPrbsGenDurationMax.setStatus("current")


class _NbsPrbsGenDuration_Type(Integer32):
    """Custom type nbsPrbsGenDuration based on Integer32"""
    defaultValue = 60


_NbsPrbsGenDuration_Object = MibTableColumn
nbsPrbsGenDuration = _NbsPrbsGenDuration_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 2, 2, 1, 5),
    _NbsPrbsGenDuration_Type()
)
nbsPrbsGenDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsPrbsGenDuration.setStatus("current")


class _NbsPrbsGenAction_Type(Integer32):
    """Custom type nbsPrbsGenAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("start", 3),
          ("stop", 2))
    )


_NbsPrbsGenAction_Type.__name__ = "Integer32"
_NbsPrbsGenAction_Object = MibTableColumn
nbsPrbsGenAction = _NbsPrbsGenAction_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 2, 2, 1, 6),
    _NbsPrbsGenAction_Type()
)
nbsPrbsGenAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsPrbsGenAction.setStatus("current")


class _NbsPrbsGenStatus_Type(Integer32):
    """Custom type nbsPrbsGenStatus based on Integer32"""
    defaultValue = 3

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
        *(("generating", 4),
          ("idle", 3),
          ("notSupported", 1),
          ("unknown", 2))
    )


_NbsPrbsGenStatus_Type.__name__ = "Integer32"
_NbsPrbsGenStatus_Object = MibTableColumn
nbsPrbsGenStatus = _NbsPrbsGenStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 2, 2, 1, 7),
    _NbsPrbsGenStatus_Type()
)
nbsPrbsGenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPrbsGenStatus.setStatus("current")
_NbsPrbsGenProgress_Type = Counter32
_NbsPrbsGenProgress_Object = MibTableColumn
nbsPrbsGenProgress = _NbsPrbsGenProgress_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 2, 2, 1, 8),
    _NbsPrbsGenProgress_Type()
)
nbsPrbsGenProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPrbsGenProgress.setStatus("current")
_NbsPrbsCheckGrp_ObjectIdentity = ObjectIdentity
nbsPrbsCheckGrp = _NbsPrbsCheckGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 212, 3)
)
if mibBuilder.loadTexts:
    nbsPrbsCheckGrp.setStatus("current")
_NbsPrbsCheckTableSize_Type = Unsigned32
_NbsPrbsCheckTableSize_Object = MibScalar
nbsPrbsCheckTableSize = _NbsPrbsCheckTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 3, 1),
    _NbsPrbsCheckTableSize_Type()
)
nbsPrbsCheckTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPrbsCheckTableSize.setStatus("current")
_NbsPrbsCheckTable_Object = MibTable
nbsPrbsCheckTable = _NbsPrbsCheckTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 3, 2)
)
if mibBuilder.loadTexts:
    nbsPrbsCheckTable.setStatus("current")
_NbsPrbsCheckEntry_Object = MibTableRow
nbsPrbsCheckEntry = _NbsPrbsCheckEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 3, 2, 1)
)
nbsPrbsCheckEntry.setIndexNames(
    (0, "NBS-PRBS-MIB", "nbsPrbsCheckIfIndex"),
)
if mibBuilder.loadTexts:
    nbsPrbsCheckEntry.setStatus("current")
_NbsPrbsCheckIfIndex_Type = InterfaceIndex
_NbsPrbsCheckIfIndex_Object = MibTableColumn
nbsPrbsCheckIfIndex = _NbsPrbsCheckIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 3, 2, 1, 1),
    _NbsPrbsCheckIfIndex_Type()
)
nbsPrbsCheckIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsPrbsCheckIfIndex.setStatus("current")
_NbsPrbsCheckPatternCaps_Type = OctetString
_NbsPrbsCheckPatternCaps_Object = MibTableColumn
nbsPrbsCheckPatternCaps = _NbsPrbsCheckPatternCaps_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 3, 2, 1, 2),
    _NbsPrbsCheckPatternCaps_Type()
)
nbsPrbsCheckPatternCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPrbsCheckPatternCaps.setStatus("current")
_NbsPrbsCheckPatternIndex_Type = Integer32
_NbsPrbsCheckPatternIndex_Object = MibTableColumn
nbsPrbsCheckPatternIndex = _NbsPrbsCheckPatternIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 3, 2, 1, 3),
    _NbsPrbsCheckPatternIndex_Type()
)
nbsPrbsCheckPatternIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsPrbsCheckPatternIndex.setStatus("current")


class _NbsPrbsCheckDurationMax_Type(Integer32):
    """Custom type nbsPrbsCheckDurationMax based on Integer32"""
    defaultValue = 0


_NbsPrbsCheckDurationMax_Object = MibTableColumn
nbsPrbsCheckDurationMax = _NbsPrbsCheckDurationMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 3, 2, 1, 4),
    _NbsPrbsCheckDurationMax_Type()
)
nbsPrbsCheckDurationMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPrbsCheckDurationMax.setStatus("current")


class _NbsPrbsCheckDuration_Type(Integer32):
    """Custom type nbsPrbsCheckDuration based on Integer32"""
    defaultValue = 60


_NbsPrbsCheckDuration_Object = MibTableColumn
nbsPrbsCheckDuration = _NbsPrbsCheckDuration_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 3, 2, 1, 5),
    _NbsPrbsCheckDuration_Type()
)
nbsPrbsCheckDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsPrbsCheckDuration.setStatus("current")


class _NbsPrbsCheckAction_Type(Integer32):
    """Custom type nbsPrbsCheckAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("start", 3),
          ("stop", 2))
    )


_NbsPrbsCheckAction_Type.__name__ = "Integer32"
_NbsPrbsCheckAction_Object = MibTableColumn
nbsPrbsCheckAction = _NbsPrbsCheckAction_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 3, 2, 1, 6),
    _NbsPrbsCheckAction_Type()
)
nbsPrbsCheckAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsPrbsCheckAction.setStatus("current")


class _NbsPrbsCheckStatus_Type(Integer32):
    """Custom type nbsPrbsCheckStatus based on Integer32"""
    defaultValue = 2

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
        *(("errOverflow", 6),
          ("error", 5),
          ("gaveUp", 7),
          ("idle", 2),
          ("notSupported", 1),
          ("syncIn", 3),
          ("syncOut", 4))
    )


_NbsPrbsCheckStatus_Type.__name__ = "Integer32"
_NbsPrbsCheckStatus_Object = MibTableColumn
nbsPrbsCheckStatus = _NbsPrbsCheckStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 3, 2, 1, 7),
    _NbsPrbsCheckStatus_Type()
)
nbsPrbsCheckStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPrbsCheckStatus.setStatus("current")
_NbsPrbsCheckProgress_Type = Counter32
_NbsPrbsCheckProgress_Object = MibTableColumn
nbsPrbsCheckProgress = _NbsPrbsCheckProgress_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 3, 2, 1, 8),
    _NbsPrbsCheckProgress_Type()
)
nbsPrbsCheckProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPrbsCheckProgress.setStatus("current")
_NbsPrbsCheckErrors_Type = Counter32
_NbsPrbsCheckErrors_Object = MibTableColumn
nbsPrbsCheckErrors = _NbsPrbsCheckErrors_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 3, 2, 1, 9),
    _NbsPrbsCheckErrors_Type()
)
nbsPrbsCheckErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPrbsCheckErrors.setStatus("current")


class _NbsPrbsCheckUpdateFreq_Type(Integer32):
    """Custom type nbsPrbsCheckUpdateFreq based on Integer32"""
    defaultValue = 0


_NbsPrbsCheckUpdateFreq_Object = MibTableColumn
nbsPrbsCheckUpdateFreq = _NbsPrbsCheckUpdateFreq_Object(
    (1, 3, 6, 1, 4, 1, 629, 212, 3, 2, 1, 10),
    _NbsPrbsCheckUpdateFreq_Type()
)
nbsPrbsCheckUpdateFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsPrbsCheckUpdateFreq.setStatus("current")
_NbsPrbsTrapGrp_ObjectIdentity = ObjectIdentity
nbsPrbsTrapGrp = _NbsPrbsTrapGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 212, 200)
)
if mibBuilder.loadTexts:
    nbsPrbsTrapGrp.setStatus("current")
_NbsPrbsTraps0_ObjectIdentity = ObjectIdentity
nbsPrbsTraps0 = _NbsPrbsTraps0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 212, 200, 0)
)
if mibBuilder.loadTexts:
    nbsPrbsTraps0.setStatus("current")

# Managed Objects groups


# Notification objects

nbsPrbsTrapGeneratorStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 212, 200, 0, 10)
)
nbsPrbsTrapGeneratorStarted.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"))
)
if mibBuilder.loadTexts:
    nbsPrbsTrapGeneratorStarted.setStatus(
        "current"
    )

nbsPrbsTrapGeneratorStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 212, 200, 0, 11)
)
nbsPrbsTrapGeneratorStopped.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"))
)
if mibBuilder.loadTexts:
    nbsPrbsTrapGeneratorStopped.setStatus(
        "current"
    )

nbsPrbsTrapCheckerStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 212, 200, 0, 20)
)
nbsPrbsTrapCheckerStarted.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"))
)
if mibBuilder.loadTexts:
    nbsPrbsTrapCheckerStarted.setStatus(
        "current"
    )

nbsPrbsTrapCheckerStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 212, 200, 0, 21)
)
nbsPrbsTrapCheckerStopped.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"),
        ("NBS-PRBS-MIB", "nbsPrbsCheckStatus"))
)
if mibBuilder.loadTexts:
    nbsPrbsTrapCheckerStopped.setStatus(
        "current"
    )

nbsPrbsTrapCheckerOverflowed = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 212, 200, 0, 22)
)
nbsPrbsTrapCheckerOverflowed.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"))
)
if mibBuilder.loadTexts:
    nbsPrbsTrapCheckerOverflowed.setStatus(
        "current"
    )

nbsPrbsTrapCheckerErrorDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 212, 200, 0, 23)
)
nbsPrbsTrapCheckerErrorDetected.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"),
        ("NBS-PRBS-MIB", "nbsPrbsCheckStatus"))
)
if mibBuilder.loadTexts:
    nbsPrbsTrapCheckerErrorDetected.setStatus(
        "current"
    )

nbsPrbsTrapCheckerStatusUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 212, 200, 0, 24)
)
nbsPrbsTrapCheckerStatusUpdate.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"),
        ("NBS-PRBS-MIB", "nbsPrbsCheckStatus"),
        ("NBS-PRBS-MIB", "nbsPrbsCheckErrors"),
        ("NBS-PRBS-MIB", "nbsPrbsCheckProgress"))
)
if mibBuilder.loadTexts:
    nbsPrbsTrapCheckerStatusUpdate.setStatus(
        "current"
    )

nbsPrbsTrapCheckerSyncIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 212, 200, 0, 25)
)
nbsPrbsTrapCheckerSyncIn.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"),
        ("NBS-PRBS-MIB", "nbsPrbsCheckStatus"))
)
if mibBuilder.loadTexts:
    nbsPrbsTrapCheckerSyncIn.setStatus(
        "current"
    )

nbsPrbsTrapCheckerSyncOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 212, 200, 0, 26)
)
nbsPrbsTrapCheckerSyncOut.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"),
        ("NBS-PRBS-MIB", "nbsPrbsCheckStatus"))
)
if mibBuilder.loadTexts:
    nbsPrbsTrapCheckerSyncOut.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-PRBS-MIB",
    **{"InterfaceIndex": InterfaceIndex,
       "nbsPrbsMib": nbsPrbsMib,
       "nbsPrbsPatternGrp": nbsPrbsPatternGrp,
       "nbsPrbsPatternTableSize": nbsPrbsPatternTableSize,
       "nbsPrbsPatternTable": nbsPrbsPatternTable,
       "nbsPrbsPatternEntry": nbsPrbsPatternEntry,
       "nbsPrbsPatternIndex": nbsPrbsPatternIndex,
       "nbsPrbsPatternName": nbsPrbsPatternName,
       "nbsPrbsPatternDesc": nbsPrbsPatternDesc,
       "nbsPrbsGenGrp": nbsPrbsGenGrp,
       "nbsPrbsGenTableSize": nbsPrbsGenTableSize,
       "nbsPrbsGenTable": nbsPrbsGenTable,
       "nbsPrbsGenEntry": nbsPrbsGenEntry,
       "nbsPrbsGenIfIndex": nbsPrbsGenIfIndex,
       "nbsPrbsGenPatternCaps": nbsPrbsGenPatternCaps,
       "nbsPrbsGenPatternIndex": nbsPrbsGenPatternIndex,
       "nbsPrbsGenDurationMax": nbsPrbsGenDurationMax,
       "nbsPrbsGenDuration": nbsPrbsGenDuration,
       "nbsPrbsGenAction": nbsPrbsGenAction,
       "nbsPrbsGenStatus": nbsPrbsGenStatus,
       "nbsPrbsGenProgress": nbsPrbsGenProgress,
       "nbsPrbsCheckGrp": nbsPrbsCheckGrp,
       "nbsPrbsCheckTableSize": nbsPrbsCheckTableSize,
       "nbsPrbsCheckTable": nbsPrbsCheckTable,
       "nbsPrbsCheckEntry": nbsPrbsCheckEntry,
       "nbsPrbsCheckIfIndex": nbsPrbsCheckIfIndex,
       "nbsPrbsCheckPatternCaps": nbsPrbsCheckPatternCaps,
       "nbsPrbsCheckPatternIndex": nbsPrbsCheckPatternIndex,
       "nbsPrbsCheckDurationMax": nbsPrbsCheckDurationMax,
       "nbsPrbsCheckDuration": nbsPrbsCheckDuration,
       "nbsPrbsCheckAction": nbsPrbsCheckAction,
       "nbsPrbsCheckStatus": nbsPrbsCheckStatus,
       "nbsPrbsCheckProgress": nbsPrbsCheckProgress,
       "nbsPrbsCheckErrors": nbsPrbsCheckErrors,
       "nbsPrbsCheckUpdateFreq": nbsPrbsCheckUpdateFreq,
       "nbsPrbsTrapGrp": nbsPrbsTrapGrp,
       "nbsPrbsTraps0": nbsPrbsTraps0,
       "nbsPrbsTrapGeneratorStarted": nbsPrbsTrapGeneratorStarted,
       "nbsPrbsTrapGeneratorStopped": nbsPrbsTrapGeneratorStopped,
       "nbsPrbsTrapCheckerStarted": nbsPrbsTrapCheckerStarted,
       "nbsPrbsTrapCheckerStopped": nbsPrbsTrapCheckerStopped,
       "nbsPrbsTrapCheckerOverflowed": nbsPrbsTrapCheckerOverflowed,
       "nbsPrbsTrapCheckerErrorDetected": nbsPrbsTrapCheckerErrorDetected,
       "nbsPrbsTrapCheckerStatusUpdate": nbsPrbsTrapCheckerStatusUpdate,
       "nbsPrbsTrapCheckerSyncIn": nbsPrbsTrapCheckerSyncIn,
       "nbsPrbsTrapCheckerSyncOut": nbsPrbsTrapCheckerSyncOut}
)
