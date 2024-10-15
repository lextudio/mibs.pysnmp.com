# SNMP MIB module (DEC-ATM-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DEC-ATM-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:31 2024
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

_Dec_ObjectIdentity = ObjectIdentity
dec = _Dec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36)
)
_Ema_ObjectIdentity = ObjectIdentity
ema = _Ema_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2)
)
_DecMIBextension_ObjectIdentity = ObjectIdentity
decMIBextension = _DecMIBextension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18)
)
_DecAtmChassisMIB_ObjectIdentity = ObjectIdentity
decAtmChassisMIB = _DecAtmChassisMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30)
)
_DecAtmChassisMIBObjects_ObjectIdentity = ObjectIdentity
decAtmChassisMIBObjects = _DecAtmChassisMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1)
)
_DecAtmSysGroup_ObjectIdentity = ObjectIdentity
decAtmSysGroup = _DecAtmSysGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 1)
)


class _DecAtmSysType_Type(Integer32):
    """Custom type decAtmSysType based on Integer32"""
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
        *(("an2", 2),
          ("gigaswitchAtm", 3),
          ("hubSwitch", 4),
          ("other", 1))
    )


_DecAtmSysType_Type.__name__ = "Integer32"
_DecAtmSysType_Object = MibScalar
decAtmSysType = _DecAtmSysType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 1, 1),
    _DecAtmSysType_Type()
)
decAtmSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmSysType.setStatus("mandatory")


class _DecAtmKeyswitchPosition_Type(Integer32):
    """Custom type decAtmKeyswitchPosition based on Integer32"""
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
        *(("fault", 2),
          ("local", 4),
          ("noKeyswitch", 1),
          ("remote", 5),
          ("secure", 3),
          ("unknown", 7),
          ("worldAccess", 6))
    )


_DecAtmKeyswitchPosition_Type.__name__ = "Integer32"
_DecAtmKeyswitchPosition_Object = MibScalar
decAtmKeyswitchPosition = _DecAtmKeyswitchPosition_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 1, 2),
    _DecAtmKeyswitchPosition_Type()
)
decAtmKeyswitchPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmKeyswitchPosition.setStatus("mandatory")
_DecAtmSlot_ObjectIdentity = ObjectIdentity
decAtmSlot = _DecAtmSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 2)
)
_DecAtmSlotNumber_Type = Integer32
_DecAtmSlotNumber_Object = MibScalar
decAtmSlotNumber = _DecAtmSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 2, 1),
    _DecAtmSlotNumber_Type()
)
decAtmSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmSlotNumber.setStatus("mandatory")
_DecAtmMasterLinecardSlot_Type = Integer32
_DecAtmMasterLinecardSlot_Object = MibScalar
decAtmMasterLinecardSlot = _DecAtmMasterLinecardSlot_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 2, 2),
    _DecAtmMasterLinecardSlot_Type()
)
decAtmMasterLinecardSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmMasterLinecardSlot.setStatus("mandatory")
_DecAtmStandbyLinecardSlot_Type = Integer32
_DecAtmStandbyLinecardSlot_Object = MibScalar
decAtmStandbyLinecardSlot = _DecAtmStandbyLinecardSlot_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 2, 3),
    _DecAtmStandbyLinecardSlot_Type()
)
decAtmStandbyLinecardSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmStandbyLinecardSlot.setStatus("mandatory")
_DecAtmSlotTable_Object = MibTable
decAtmSlotTable = _DecAtmSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 2, 4)
)
if mibBuilder.loadTexts:
    decAtmSlotTable.setStatus("mandatory")
_DecAtmSlotEntry_Object = MibTableRow
decAtmSlotEntry = _DecAtmSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 2, 4, 1)
)
decAtmSlotEntry.setIndexNames(
    (0, "DEC-ATM-CHASSIS-MIB", "decAtmSlotIndex"),
)
if mibBuilder.loadTexts:
    decAtmSlotEntry.setStatus("mandatory")
_DecAtmSlotIndex_Type = Integer32
_DecAtmSlotIndex_Object = MibTableColumn
decAtmSlotIndex = _DecAtmSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 2, 4, 1, 1),
    _DecAtmSlotIndex_Type()
)
decAtmSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmSlotIndex.setStatus("mandatory")


class _DecAtmCardStatus_Type(Integer32):
    """Custom type decAtmCardStatus based on Integer32"""
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
        *(("fault", 5),
          ("notPresent", 1),
          ("powerDown", 2),
          ("powerDownThenUp", 4),
          ("powerUp", 3),
          ("revisionMismatch", 6),
          ("selfTestInProgress", 7))
    )


_DecAtmCardStatus_Type.__name__ = "Integer32"
_DecAtmCardStatus_Object = MibTableColumn
decAtmCardStatus = _DecAtmCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 2, 4, 1, 2),
    _DecAtmCardStatus_Type()
)
decAtmCardStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decAtmCardStatus.setStatus("mandatory")


class _DecAtmCardType_Type(Integer32):
    """Custom type decAtmCardType based on Integer32"""
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("clockCard", 3),
          ("hubSwitch", 9),
          ("none", 1),
          ("other", 2),
          ("qlc10", 4),
          ("qlc15", 5),
          ("qlc16", 6),
          ("qlc20", 7),
          ("qlc622", 8))
    )


_DecAtmCardType_Type.__name__ = "Integer32"
_DecAtmCardType_Object = MibTableColumn
decAtmCardType = _DecAtmCardType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 2, 4, 1, 3),
    _DecAtmCardType_Type()
)
decAtmCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmCardType.setStatus("mandatory")


class _DecAtmCardHasModPhys_Type(Integer32):
    """Custom type decAtmCardHasModPhys based on Integer32"""
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


_DecAtmCardHasModPhys_Type.__name__ = "Integer32"
_DecAtmCardHasModPhys_Object = MibTableColumn
decAtmCardHasModPhys = _DecAtmCardHasModPhys_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 2, 4, 1, 4),
    _DecAtmCardHasModPhys_Type()
)
decAtmCardHasModPhys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmCardHasModPhys.setStatus("mandatory")
_DecAtmCardHwRev_Type = DisplayString
_DecAtmCardHwRev_Object = MibTableColumn
decAtmCardHwRev = _DecAtmCardHwRev_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 2, 4, 1, 5),
    _DecAtmCardHwRev_Type()
)
decAtmCardHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmCardHwRev.setStatus("mandatory")
_DecAtmCardFwRev_Type = DisplayString
_DecAtmCardFwRev_Object = MibTableColumn
decAtmCardFwRev = _DecAtmCardFwRev_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 2, 4, 1, 6),
    _DecAtmCardFwRev_Type()
)
decAtmCardFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmCardFwRev.setStatus("mandatory")
_DecAtmCardFault_Type = Integer32
_DecAtmCardFault_Object = MibTableColumn
decAtmCardFault = _DecAtmCardFault_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 2, 4, 1, 7),
    _DecAtmCardFault_Type()
)
decAtmCardFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmCardFault.setStatus("mandatory")
_DecAtmPort_ObjectIdentity = ObjectIdentity
decAtmPort = _DecAtmPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 3)
)
_DecAtmPortTable_Object = MibTable
decAtmPortTable = _DecAtmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 3, 1)
)
if mibBuilder.loadTexts:
    decAtmPortTable.setStatus("mandatory")
_DecAtmPortEntry_Object = MibTableRow
decAtmPortEntry = _DecAtmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 3, 1, 1)
)
decAtmPortEntry.setIndexNames(
    (0, "DEC-ATM-CHASSIS-MIB", "decAtmSlotIndex"),
    (0, "DEC-ATM-CHASSIS-MIB", "decAtmPortIndex"),
)
if mibBuilder.loadTexts:
    decAtmPortEntry.setStatus("mandatory")
_DecAtmPortIndex_Type = Integer32
_DecAtmPortIndex_Object = MibTableColumn
decAtmPortIndex = _DecAtmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 3, 1, 1, 1),
    _DecAtmPortIndex_Type()
)
decAtmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmPortIndex.setStatus("mandatory")


class _DecAtmPortConnector_Type(Integer32):
    """Custom type decAtmPortConnector based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("e1", 8),
          ("e3", 7),
          ("e3Hdlc", 10),
          ("e3Proto", 11),
          ("notPresent", 2),
          ("other", 1),
          ("sts12cMultiModeFiber", 13),
          ("sts12cSingleModeFiber", 12),
          ("sts1TwistedPair", 9),
          ("sts3cMultiModeFiber", 4),
          ("sts3cSingleModeFiber", 3),
          ("sts3cTwistedPair", 5),
          ("t1", 14),
          ("t3", 6))
    )


_DecAtmPortConnector_Type.__name__ = "Integer32"
_DecAtmPortConnector_Object = MibTableColumn
decAtmPortConnector = _DecAtmPortConnector_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 3, 1, 1, 2),
    _DecAtmPortConnector_Type()
)
decAtmPortConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmPortConnector.setStatus("mandatory")
_DecAtmLed_ObjectIdentity = ObjectIdentity
decAtmLed = _DecAtmLed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 4)
)
_DecAtmSlotLedTable_Object = MibTable
decAtmSlotLedTable = _DecAtmSlotLedTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 4, 1)
)
if mibBuilder.loadTexts:
    decAtmSlotLedTable.setStatus("mandatory")
_DecAtmSlotLedEntry_Object = MibTableRow
decAtmSlotLedEntry = _DecAtmSlotLedEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 4, 1, 1)
)
decAtmSlotLedEntry.setIndexNames(
    (0, "DEC-ATM-CHASSIS-MIB", "decAtmSlotIndex"),
    (0, "DEC-ATM-CHASSIS-MIB", "decAtmSlotLedIndex"),
)
if mibBuilder.loadTexts:
    decAtmSlotLedEntry.setStatus("mandatory")


class _DecAtmSlotLedIndex_Type(Integer32):
    """Custom type decAtmSlotLedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DecAtmSlotLedIndex_Type.__name__ = "Integer32"
_DecAtmSlotLedIndex_Object = MibTableColumn
decAtmSlotLedIndex = _DecAtmSlotLedIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 4, 1, 1, 1),
    _DecAtmSlotLedIndex_Type()
)
decAtmSlotLedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmSlotLedIndex.setStatus("mandatory")


class _DecAtmSlotLedDescr_Type(DisplayString):
    """Custom type decAtmSlotLedDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DecAtmSlotLedDescr_Type.__name__ = "DisplayString"
_DecAtmSlotLedDescr_Object = MibTableColumn
decAtmSlotLedDescr = _DecAtmSlotLedDescr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 4, 1, 1, 2),
    _DecAtmSlotLedDescr_Type()
)
decAtmSlotLedDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmSlotLedDescr.setStatus("mandatory")


class _DecAtmSlotLedProgram_Type(OctetString):
    """Custom type decAtmSlotLedProgram based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_DecAtmSlotLedProgram_Type.__name__ = "OctetString"
_DecAtmSlotLedProgram_Object = MibTableColumn
decAtmSlotLedProgram = _DecAtmSlotLedProgram_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 4, 1, 1, 3),
    _DecAtmSlotLedProgram_Type()
)
decAtmSlotLedProgram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmSlotLedProgram.setStatus("mandatory")
_DecAtmPortLedTable_Object = MibTable
decAtmPortLedTable = _DecAtmPortLedTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 4, 2)
)
if mibBuilder.loadTexts:
    decAtmPortLedTable.setStatus("mandatory")
_DecAtmPortLedEntry_Object = MibTableRow
decAtmPortLedEntry = _DecAtmPortLedEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 4, 2, 1)
)
decAtmPortLedEntry.setIndexNames(
    (0, "DEC-ATM-CHASSIS-MIB", "decAtmSlotIndex"),
    (0, "DEC-ATM-CHASSIS-MIB", "decAtmPortIndex"),
    (0, "DEC-ATM-CHASSIS-MIB", "decAtmPortLedIndex"),
)
if mibBuilder.loadTexts:
    decAtmPortLedEntry.setStatus("mandatory")


class _DecAtmPortLedIndex_Type(Integer32):
    """Custom type decAtmPortLedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DecAtmPortLedIndex_Type.__name__ = "Integer32"
_DecAtmPortLedIndex_Object = MibTableColumn
decAtmPortLedIndex = _DecAtmPortLedIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 4, 2, 1, 1),
    _DecAtmPortLedIndex_Type()
)
decAtmPortLedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmPortLedIndex.setStatus("mandatory")


class _DecAtmPortLedDescr_Type(DisplayString):
    """Custom type decAtmPortLedDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DecAtmPortLedDescr_Type.__name__ = "DisplayString"
_DecAtmPortLedDescr_Object = MibTableColumn
decAtmPortLedDescr = _DecAtmPortLedDescr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 4, 2, 1, 2),
    _DecAtmPortLedDescr_Type()
)
decAtmPortLedDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmPortLedDescr.setStatus("mandatory")


class _DecAtmPortLedProgram_Type(OctetString):
    """Custom type decAtmPortLedProgram based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_DecAtmPortLedProgram_Type.__name__ = "OctetString"
_DecAtmPortLedProgram_Object = MibTableColumn
decAtmPortLedProgram = _DecAtmPortLedProgram_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 4, 2, 1, 3),
    _DecAtmPortLedProgram_Type()
)
decAtmPortLedProgram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmPortLedProgram.setStatus("mandatory")
_DecAtmLedInterestingChanges_Type = Counter32
_DecAtmLedInterestingChanges_Object = MibScalar
decAtmLedInterestingChanges = _DecAtmLedInterestingChanges_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 4, 3),
    _DecAtmLedInterestingChanges_Type()
)
decAtmLedInterestingChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmLedInterestingChanges.setStatus("mandatory")
_DecAtmClockCard_ObjectIdentity = ObjectIdentity
decAtmClockCard = _DecAtmClockCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 5)
)
_DecAtmMgmtMemoryAvail_Type = Integer32
_DecAtmMgmtMemoryAvail_Object = MibScalar
decAtmMgmtMemoryAvail = _DecAtmMgmtMemoryAvail_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 5, 1),
    _DecAtmMgmtMemoryAvail_Type()
)
decAtmMgmtMemoryAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmMgmtMemoryAvail.setStatus("mandatory")


class _DecAtmMgmtMemoryAction_Type(Integer32):
    """Custom type decAtmMgmtMemoryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("rewrite", 2),
          ("rewriting", 3))
    )


_DecAtmMgmtMemoryAction_Type.__name__ = "Integer32"
_DecAtmMgmtMemoryAction_Object = MibScalar
decAtmMgmtMemoryAction = _DecAtmMgmtMemoryAction_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 5, 2),
    _DecAtmMgmtMemoryAction_Type()
)
decAtmMgmtMemoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decAtmMgmtMemoryAction.setStatus("mandatory")
_DecGigaAtmIntEthPktsSent_Type = Counter32
_DecGigaAtmIntEthPktsSent_Object = MibScalar
decGigaAtmIntEthPktsSent = _DecGigaAtmIntEthPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 5, 3),
    _DecGigaAtmIntEthPktsSent_Type()
)
decGigaAtmIntEthPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decGigaAtmIntEthPktsSent.setStatus("mandatory")
_DecGigaAtmIntEthPktsRcvd_Type = Counter32
_DecGigaAtmIntEthPktsRcvd_Object = MibScalar
decGigaAtmIntEthPktsRcvd = _DecGigaAtmIntEthPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 5, 4),
    _DecGigaAtmIntEthPktsRcvd_Type()
)
decGigaAtmIntEthPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decGigaAtmIntEthPktsRcvd.setStatus("mandatory")
_DecGigaAtmExtEthPktsSent_Type = Counter32
_DecGigaAtmExtEthPktsSent_Object = MibScalar
decGigaAtmExtEthPktsSent = _DecGigaAtmExtEthPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 5, 5),
    _DecGigaAtmExtEthPktsSent_Type()
)
decGigaAtmExtEthPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decGigaAtmExtEthPktsSent.setStatus("mandatory")
_DecGigaAtmExtEthPktsRcvd_Type = Counter32
_DecGigaAtmExtEthPktsRcvd_Object = MibScalar
decGigaAtmExtEthPktsRcvd = _DecGigaAtmExtEthPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 5, 6),
    _DecGigaAtmExtEthPktsRcvd_Type()
)
decGigaAtmExtEthPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decGigaAtmExtEthPktsRcvd.setStatus("mandatory")
_DecAtmPsc_ObjectIdentity = ObjectIdentity
decAtmPsc = _DecAtmPsc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 6)
)


class _DecAtmPscStatus_Type(Integer32):
    """Custom type decAtmPscStatus based on Integer32"""
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
        *(("fault", 3),
          ("notPresent", 1),
          ("okay", 2),
          ("unknown", 4))
    )


_DecAtmPscStatus_Type.__name__ = "Integer32"
_DecAtmPscStatus_Object = MibScalar
decAtmPscStatus = _DecAtmPscStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 6, 1),
    _DecAtmPscStatus_Type()
)
decAtmPscStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmPscStatus.setStatus("mandatory")
_DecAtmPscFwRev_Type = DisplayString
_DecAtmPscFwRev_Object = MibScalar
decAtmPscFwRev = _DecAtmPscFwRev_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 6, 2),
    _DecAtmPscFwRev_Type()
)
decAtmPscFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmPscFwRev.setStatus("mandatory")
_DecAtmPscHwRev_Type = DisplayString
_DecAtmPscHwRev_Object = MibScalar
decAtmPscHwRev = _DecAtmPscHwRev_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 6, 3),
    _DecAtmPscHwRev_Type()
)
decAtmPscHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmPscHwRev.setStatus("mandatory")


class _DecAtmPscFwImageStatus_Type(Integer32):
    """Custom type decAtmPscFwImageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("downloadRequired", 2),
          ("okay", 1),
          ("unknown", 3))
    )


_DecAtmPscFwImageStatus_Type.__name__ = "Integer32"
_DecAtmPscFwImageStatus_Object = MibScalar
decAtmPscFwImageStatus = _DecAtmPscFwImageStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 6, 4),
    _DecAtmPscFwImageStatus_Type()
)
decAtmPscFwImageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmPscFwImageStatus.setStatus("mandatory")


class _DecAtmPscBackplaneStatus_Type(Integer32):
    """Custom type decAtmPscBackplaneStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("okay", 1),
          ("unknown", 3))
    )


_DecAtmPscBackplaneStatus_Type.__name__ = "Integer32"
_DecAtmPscBackplaneStatus_Object = MibScalar
decAtmPscBackplaneStatus = _DecAtmPscBackplaneStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 6, 5),
    _DecAtmPscBackplaneStatus_Type()
)
decAtmPscBackplaneStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmPscBackplaneStatus.setStatus("mandatory")


class _DecAtmPscFaultLedProgram_Type(OctetString):
    """Custom type decAtmPscFaultLedProgram based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_DecAtmPscFaultLedProgram_Type.__name__ = "OctetString"
_DecAtmPscFaultLedProgram_Object = MibScalar
decAtmPscFaultLedProgram = _DecAtmPscFaultLedProgram_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 6, 6),
    _DecAtmPscFaultLedProgram_Type()
)
decAtmPscFaultLedProgram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmPscFaultLedProgram.setStatus("mandatory")
_DecAtmPowerSupply_ObjectIdentity = ObjectIdentity
decAtmPowerSupply = _DecAtmPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 7)
)
_DecAtmPowerSupplyTable_Object = MibTable
decAtmPowerSupplyTable = _DecAtmPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 7, 1)
)
if mibBuilder.loadTexts:
    decAtmPowerSupplyTable.setStatus("mandatory")
_DecAtmPowerSupplyEntry_Object = MibTableRow
decAtmPowerSupplyEntry = _DecAtmPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 7, 1, 1)
)
decAtmPowerSupplyEntry.setIndexNames(
    (0, "DEC-ATM-CHASSIS-MIB", "decAtmPowerIndex"),
)
if mibBuilder.loadTexts:
    decAtmPowerSupplyEntry.setStatus("mandatory")
_DecAtmPowerIndex_Type = Integer32
_DecAtmPowerIndex_Object = MibTableColumn
decAtmPowerIndex = _DecAtmPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 7, 1, 1, 1),
    _DecAtmPowerIndex_Type()
)
decAtmPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmPowerIndex.setStatus("mandatory")


class _DecAtmPowerStatus_Type(Integer32):
    """Custom type decAtmPowerStatus based on Integer32"""
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
        *(("fault", 3),
          ("notPresent", 1),
          ("okay", 2),
          ("unknown", 4))
    )


_DecAtmPowerStatus_Type.__name__ = "Integer32"
_DecAtmPowerStatus_Object = MibTableColumn
decAtmPowerStatus = _DecAtmPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 7, 1, 1, 2),
    _DecAtmPowerStatus_Type()
)
decAtmPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmPowerStatus.setStatus("mandatory")


class _DecAtmPowerInputSource_Type(Integer32):
    """Custom type decAtmPowerInputSource based on Integer32"""
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
        *(("acLine", 1),
          ("dc48V", 2),
          ("decHub", 3),
          ("none", 4),
          ("unknown", 5))
    )


_DecAtmPowerInputSource_Type.__name__ = "Integer32"
_DecAtmPowerInputSource_Object = MibTableColumn
decAtmPowerInputSource = _DecAtmPowerInputSource_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 7, 1, 1, 3),
    _DecAtmPowerInputSource_Type()
)
decAtmPowerInputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmPowerInputSource.setStatus("mandatory")
_DecAtmPowerVoltage_Type = Integer32
_DecAtmPowerVoltage_Object = MibTableColumn
decAtmPowerVoltage = _DecAtmPowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 7, 1, 1, 4),
    _DecAtmPowerVoltage_Type()
)
decAtmPowerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmPowerVoltage.setStatus("mandatory")
_DecAtmPowerOutputInWatts_Type = Integer32
_DecAtmPowerOutputInWatts_Object = MibTableColumn
decAtmPowerOutputInWatts = _DecAtmPowerOutputInWatts_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 7, 1, 1, 5),
    _DecAtmPowerOutputInWatts_Type()
)
decAtmPowerOutputInWatts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decAtmPowerOutputInWatts.setStatus("mandatory")


class _DecAtmPowerFaultLedProgram_Type(OctetString):
    """Custom type decAtmPowerFaultLedProgram based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_DecAtmPowerFaultLedProgram_Type.__name__ = "OctetString"
_DecAtmPowerFaultLedProgram_Object = MibTableColumn
decAtmPowerFaultLedProgram = _DecAtmPowerFaultLedProgram_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 7, 1, 1, 6),
    _DecAtmPowerFaultLedProgram_Type()
)
decAtmPowerFaultLedProgram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmPowerFaultLedProgram.setStatus("mandatory")


class _DecAtmPowerOkLedProgram_Type(OctetString):
    """Custom type decAtmPowerOkLedProgram based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_DecAtmPowerOkLedProgram_Type.__name__ = "OctetString"
_DecAtmPowerOkLedProgram_Object = MibTableColumn
decAtmPowerOkLedProgram = _DecAtmPowerOkLedProgram_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 7, 1, 1, 7),
    _DecAtmPowerOkLedProgram_Type()
)
decAtmPowerOkLedProgram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmPowerOkLedProgram.setStatus("mandatory")
_DecAtmBattery_ObjectIdentity = ObjectIdentity
decAtmBattery = _DecAtmBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 8)
)


class _DecAtmBatteryStatus_Type(Integer32):
    """Custom type decAtmBatteryStatus based on Integer32"""
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
        *(("fault", 3),
          ("notPresent", 1),
          ("okay", 2),
          ("unknown", 4))
    )


_DecAtmBatteryStatus_Type.__name__ = "Integer32"
_DecAtmBatteryStatus_Object = MibScalar
decAtmBatteryStatus = _DecAtmBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 8, 1),
    _DecAtmBatteryStatus_Type()
)
decAtmBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmBatteryStatus.setStatus("mandatory")


class _DecAtmBatteryUsing_Type(Integer32):
    """Custom type decAtmBatteryUsing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("batteryPower", 1),
          ("externalPower", 2),
          ("unknown", 3))
    )


_DecAtmBatteryUsing_Type.__name__ = "Integer32"
_DecAtmBatteryUsing_Object = MibScalar
decAtmBatteryUsing = _DecAtmBatteryUsing_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 8, 2),
    _DecAtmBatteryUsing_Type()
)
decAtmBatteryUsing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmBatteryUsing.setStatus("mandatory")


class _DecAtmBatteryCharge_Type(Integer32):
    """Custom type decAtmBatteryCharge based on Integer32"""
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
        *(("fullyCharged", 1),
          ("low", 3),
          ("okay", 2),
          ("unknown", 4))
    )


_DecAtmBatteryCharge_Type.__name__ = "Integer32"
_DecAtmBatteryCharge_Object = MibScalar
decAtmBatteryCharge = _DecAtmBatteryCharge_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 8, 3),
    _DecAtmBatteryCharge_Type()
)
decAtmBatteryCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmBatteryCharge.setStatus("mandatory")


class _DecAtmBatteryTest_Type(Integer32):
    """Custom type decAtmBatteryTest based on Integer32"""
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
        *(("fail", 2),
          ("notTested", 4),
          ("pass", 1),
          ("test", 3))
    )


_DecAtmBatteryTest_Type.__name__ = "Integer32"
_DecAtmBatteryTest_Object = MibScalar
decAtmBatteryTest = _DecAtmBatteryTest_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 8, 4),
    _DecAtmBatteryTest_Type()
)
decAtmBatteryTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decAtmBatteryTest.setStatus("mandatory")
_DecAtmTemperature_ObjectIdentity = ObjectIdentity
decAtmTemperature = _DecAtmTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 9)
)


class _DecAtmCabinetTemperature_Type(Integer32):
    """Custom type decAtmCabinetTemperature based on Integer32"""
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
        *(("excessivelyHigh", 3),
          ("excessivelyLow", 5),
          ("high", 2),
          ("low", 4),
          ("noSensor", 6),
          ("normal", 1),
          ("unknown", 7))
    )


_DecAtmCabinetTemperature_Type.__name__ = "Integer32"
_DecAtmCabinetTemperature_Object = MibScalar
decAtmCabinetTemperature = _DecAtmCabinetTemperature_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 9, 1),
    _DecAtmCabinetTemperature_Type()
)
decAtmCabinetTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmCabinetTemperature.setStatus("mandatory")


class _DecAtmTemperatureWarning_Type(Integer32):
    """Custom type decAtmTemperatureWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("heedWarning", 1),
          ("ignoreWarning", 2),
          ("noWarningFeature", 3))
    )


_DecAtmTemperatureWarning_Type.__name__ = "Integer32"
_DecAtmTemperatureWarning_Object = MibScalar
decAtmTemperatureWarning = _DecAtmTemperatureWarning_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 9, 2),
    _DecAtmTemperatureWarning_Type()
)
decAtmTemperatureWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decAtmTemperatureWarning.setStatus("mandatory")


class _DecAtmTemperatureLedProgram_Type(OctetString):
    """Custom type decAtmTemperatureLedProgram based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_DecAtmTemperatureLedProgram_Type.__name__ = "OctetString"
_DecAtmTemperatureLedProgram_Object = MibScalar
decAtmTemperatureLedProgram = _DecAtmTemperatureLedProgram_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 9, 3),
    _DecAtmTemperatureLedProgram_Type()
)
decAtmTemperatureLedProgram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmTemperatureLedProgram.setStatus("mandatory")
_DecAtmFan_ObjectIdentity = ObjectIdentity
decAtmFan = _DecAtmFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 10)
)


class _DecAtmFanSpeed_Type(Integer32):
    """Custom type decAtmFanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 1),
          ("normal", 2),
          ("unknown", 3))
    )


_DecAtmFanSpeed_Type.__name__ = "Integer32"
_DecAtmFanSpeed_Object = MibScalar
decAtmFanSpeed = _DecAtmFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 10, 1),
    _DecAtmFanSpeed_Type()
)
decAtmFanSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decAtmFanSpeed.setStatus("mandatory")
_DecAtmFanTable_Object = MibTable
decAtmFanTable = _DecAtmFanTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 10, 2)
)
if mibBuilder.loadTexts:
    decAtmFanTable.setStatus("mandatory")
_DecAtmFanEntry_Object = MibTableRow
decAtmFanEntry = _DecAtmFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 10, 2, 1)
)
decAtmFanEntry.setIndexNames(
    (0, "DEC-ATM-CHASSIS-MIB", "decAtmFanIndex"),
)
if mibBuilder.loadTexts:
    decAtmFanEntry.setStatus("mandatory")
_DecAtmFanIndex_Type = Integer32
_DecAtmFanIndex_Object = MibTableColumn
decAtmFanIndex = _DecAtmFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 10, 2, 1, 1),
    _DecAtmFanIndex_Type()
)
decAtmFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmFanIndex.setStatus("mandatory")


class _DecAtmFanStatus_Type(Integer32):
    """Custom type decAtmFanStatus based on Integer32"""
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
        *(("fault", 3),
          ("notPresent", 1),
          ("okay", 2),
          ("unknown", 4))
    )


_DecAtmFanStatus_Type.__name__ = "Integer32"
_DecAtmFanStatus_Object = MibTableColumn
decAtmFanStatus = _DecAtmFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 10, 2, 1, 2),
    _DecAtmFanStatus_Type()
)
decAtmFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmFanStatus.setStatus("mandatory")


class _DecAtmFanFaultLedProgram_Type(OctetString):
    """Custom type decAtmFanFaultLedProgram based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_DecAtmFanFaultLedProgram_Type.__name__ = "OctetString"
_DecAtmFanFaultLedProgram_Object = MibTableColumn
decAtmFanFaultLedProgram = _DecAtmFanFaultLedProgram_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 10, 2, 1, 3),
    _DecAtmFanFaultLedProgram_Type()
)
decAtmFanFaultLedProgram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmFanFaultLedProgram.setStatus("mandatory")
_DecAtmFppnTable_Object = MibTable
decAtmFppnTable = _DecAtmFppnTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 11)
)
if mibBuilder.loadTexts:
    decAtmFppnTable.setStatus("mandatory")
_DecAtmFppnEntry_Object = MibTableRow
decAtmFppnEntry = _DecAtmFppnEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 11, 1)
)
decAtmFppnEntry.setIndexNames(
    (0, "DEC-ATM-CHASSIS-MIB", "decAtmFppnSlotNumber"),
    (0, "DEC-ATM-CHASSIS-MIB", "decAtmFppnPortOfThatSlot"),
)
if mibBuilder.loadTexts:
    decAtmFppnEntry.setStatus("mandatory")
_DecAtmFppnSlotNumber_Type = Integer32
_DecAtmFppnSlotNumber_Object = MibTableColumn
decAtmFppnSlotNumber = _DecAtmFppnSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 11, 1, 1),
    _DecAtmFppnSlotNumber_Type()
)
decAtmFppnSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmFppnSlotNumber.setStatus("mandatory")
_DecAtmFppnPortOfThatSlot_Type = Integer32
_DecAtmFppnPortOfThatSlot_Object = MibTableColumn
decAtmFppnPortOfThatSlot = _DecAtmFppnPortOfThatSlot_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 11, 1, 2),
    _DecAtmFppnPortOfThatSlot_Type()
)
decAtmFppnPortOfThatSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmFppnPortOfThatSlot.setStatus("mandatory")
_DecAtmFppnIfIndex_Type = Integer32
_DecAtmFppnIfIndex_Object = MibTableColumn
decAtmFppnIfIndex = _DecAtmFppnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 11, 1, 3),
    _DecAtmFppnIfIndex_Type()
)
decAtmFppnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmFppnIfIndex.setStatus("mandatory")
_DecAtmUpgradeSoftware_ObjectIdentity = ObjectIdentity
decAtmUpgradeSoftware = _DecAtmUpgradeSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 12)
)
_DecAtmLoad_ObjectIdentity = ObjectIdentity
decAtmLoad = _DecAtmLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 12, 1)
)


class _DecAtmLoadAdminStatus_Type(Integer32):
    """Custom type decAtmLoadAdminStatus based on Integer32"""
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
        *(("other", 1),
          ("start-read-BootP", 3),
          ("start-read-TFTP", 4),
          ("start-reboot", 2))
    )


_DecAtmLoadAdminStatus_Type.__name__ = "Integer32"
_DecAtmLoadAdminStatus_Object = MibScalar
decAtmLoadAdminStatus = _DecAtmLoadAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 12, 1, 1),
    _DecAtmLoadAdminStatus_Type()
)
decAtmLoadAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decAtmLoadAdminStatus.setStatus("mandatory")


class _DecAtmLoadOperStatus_Type(Integer32):
    """Custom type decAtmLoadOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 3),
          ("none", 1),
          ("success", 2))
    )


_DecAtmLoadOperStatus_Type.__name__ = "Integer32"
_DecAtmLoadOperStatus_Object = MibScalar
decAtmLoadOperStatus = _DecAtmLoadOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 12, 1, 2),
    _DecAtmLoadOperStatus_Type()
)
decAtmLoadOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmLoadOperStatus.setStatus("mandatory")


class _DecAtmLoadFilename_Type(DisplayString):
    """Custom type decAtmLoadFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DecAtmLoadFilename_Type.__name__ = "DisplayString"
_DecAtmLoadFilename_Object = MibScalar
decAtmLoadFilename = _DecAtmLoadFilename_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 12, 1, 3),
    _DecAtmLoadFilename_Type()
)
decAtmLoadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decAtmLoadFilename.setStatus("mandatory")
_DecAtmLoadIpHostAddr_Type = IpAddress
_DecAtmLoadIpHostAddr_Object = MibScalar
decAtmLoadIpHostAddr = _DecAtmLoadIpHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 12, 1, 4),
    _DecAtmLoadIpHostAddr_Type()
)
decAtmLoadIpHostAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decAtmLoadIpHostAddr.setStatus("mandatory")


class _DecAtmLoadDevSpecific_Type(DisplayString):
    """Custom type decAtmLoadDevSpecific based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DecAtmLoadDevSpecific_Type.__name__ = "DisplayString"
_DecAtmLoadDevSpecific_Object = MibScalar
decAtmLoadDevSpecific = _DecAtmLoadDevSpecific_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 12, 1, 5),
    _DecAtmLoadDevSpecific_Type()
)
decAtmLoadDevSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    decAtmLoadDevSpecific.setStatus("mandatory")
_DecAtmConfigIpHostAddr_Type = IpAddress
_DecAtmConfigIpHostAddr_Object = MibScalar
decAtmConfigIpHostAddr = _DecAtmConfigIpHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 12, 1, 6),
    _DecAtmConfigIpHostAddr_Type()
)
decAtmConfigIpHostAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decAtmConfigIpHostAddr.setStatus("mandatory")
_DecAtmConfigDefaultGateway_Type = IpAddress
_DecAtmConfigDefaultGateway_Object = MibScalar
decAtmConfigDefaultGateway = _DecAtmConfigDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 12, 1, 7),
    _DecAtmConfigDefaultGateway_Type()
)
decAtmConfigDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decAtmConfigDefaultGateway.setStatus("mandatory")


class _DecAtmConfigFilename_Type(DisplayString):
    """Custom type decAtmConfigFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DecAtmConfigFilename_Type.__name__ = "DisplayString"
_DecAtmConfigFilename_Object = MibScalar
decAtmConfigFilename = _DecAtmConfigFilename_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 12, 1, 8),
    _DecAtmConfigFilename_Type()
)
decAtmConfigFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decAtmConfigFilename.setStatus("mandatory")


class _DecAtmConfigStatus_Type(Integer32):
    """Custom type decAtmConfigStatus based on Integer32"""
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("read-error", 8),
          ("start-read", 2),
          ("start-read-complete", 5),
          ("start-read-inprogress", 4),
          ("start-write", 3),
          ("start-write-complete", 7),
          ("start-write-inprogress", 6),
          ("write-error", 9))
    )


_DecAtmConfigStatus_Type.__name__ = "Integer32"
_DecAtmConfigStatus_Object = MibScalar
decAtmConfigStatus = _DecAtmConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 30, 1, 12, 1, 9),
    _DecAtmConfigStatus_Type()
)
decAtmConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    decAtmConfigStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DEC-ATM-CHASSIS-MIB",
    **{"dec": dec,
       "ema": ema,
       "decMIBextension": decMIBextension,
       "decAtmChassisMIB": decAtmChassisMIB,
       "decAtmChassisMIBObjects": decAtmChassisMIBObjects,
       "decAtmSysGroup": decAtmSysGroup,
       "decAtmSysType": decAtmSysType,
       "decAtmKeyswitchPosition": decAtmKeyswitchPosition,
       "decAtmSlot": decAtmSlot,
       "decAtmSlotNumber": decAtmSlotNumber,
       "decAtmMasterLinecardSlot": decAtmMasterLinecardSlot,
       "decAtmStandbyLinecardSlot": decAtmStandbyLinecardSlot,
       "decAtmSlotTable": decAtmSlotTable,
       "decAtmSlotEntry": decAtmSlotEntry,
       "decAtmSlotIndex": decAtmSlotIndex,
       "decAtmCardStatus": decAtmCardStatus,
       "decAtmCardType": decAtmCardType,
       "decAtmCardHasModPhys": decAtmCardHasModPhys,
       "decAtmCardHwRev": decAtmCardHwRev,
       "decAtmCardFwRev": decAtmCardFwRev,
       "decAtmCardFault": decAtmCardFault,
       "decAtmPort": decAtmPort,
       "decAtmPortTable": decAtmPortTable,
       "decAtmPortEntry": decAtmPortEntry,
       "decAtmPortIndex": decAtmPortIndex,
       "decAtmPortConnector": decAtmPortConnector,
       "decAtmLed": decAtmLed,
       "decAtmSlotLedTable": decAtmSlotLedTable,
       "decAtmSlotLedEntry": decAtmSlotLedEntry,
       "decAtmSlotLedIndex": decAtmSlotLedIndex,
       "decAtmSlotLedDescr": decAtmSlotLedDescr,
       "decAtmSlotLedProgram": decAtmSlotLedProgram,
       "decAtmPortLedTable": decAtmPortLedTable,
       "decAtmPortLedEntry": decAtmPortLedEntry,
       "decAtmPortLedIndex": decAtmPortLedIndex,
       "decAtmPortLedDescr": decAtmPortLedDescr,
       "decAtmPortLedProgram": decAtmPortLedProgram,
       "decAtmLedInterestingChanges": decAtmLedInterestingChanges,
       "decAtmClockCard": decAtmClockCard,
       "decAtmMgmtMemoryAvail": decAtmMgmtMemoryAvail,
       "decAtmMgmtMemoryAction": decAtmMgmtMemoryAction,
       "decGigaAtmIntEthPktsSent": decGigaAtmIntEthPktsSent,
       "decGigaAtmIntEthPktsRcvd": decGigaAtmIntEthPktsRcvd,
       "decGigaAtmExtEthPktsSent": decGigaAtmExtEthPktsSent,
       "decGigaAtmExtEthPktsRcvd": decGigaAtmExtEthPktsRcvd,
       "decAtmPsc": decAtmPsc,
       "decAtmPscStatus": decAtmPscStatus,
       "decAtmPscFwRev": decAtmPscFwRev,
       "decAtmPscHwRev": decAtmPscHwRev,
       "decAtmPscFwImageStatus": decAtmPscFwImageStatus,
       "decAtmPscBackplaneStatus": decAtmPscBackplaneStatus,
       "decAtmPscFaultLedProgram": decAtmPscFaultLedProgram,
       "decAtmPowerSupply": decAtmPowerSupply,
       "decAtmPowerSupplyTable": decAtmPowerSupplyTable,
       "decAtmPowerSupplyEntry": decAtmPowerSupplyEntry,
       "decAtmPowerIndex": decAtmPowerIndex,
       "decAtmPowerStatus": decAtmPowerStatus,
       "decAtmPowerInputSource": decAtmPowerInputSource,
       "decAtmPowerVoltage": decAtmPowerVoltage,
       "decAtmPowerOutputInWatts": decAtmPowerOutputInWatts,
       "decAtmPowerFaultLedProgram": decAtmPowerFaultLedProgram,
       "decAtmPowerOkLedProgram": decAtmPowerOkLedProgram,
       "decAtmBattery": decAtmBattery,
       "decAtmBatteryStatus": decAtmBatteryStatus,
       "decAtmBatteryUsing": decAtmBatteryUsing,
       "decAtmBatteryCharge": decAtmBatteryCharge,
       "decAtmBatteryTest": decAtmBatteryTest,
       "decAtmTemperature": decAtmTemperature,
       "decAtmCabinetTemperature": decAtmCabinetTemperature,
       "decAtmTemperatureWarning": decAtmTemperatureWarning,
       "decAtmTemperatureLedProgram": decAtmTemperatureLedProgram,
       "decAtmFan": decAtmFan,
       "decAtmFanSpeed": decAtmFanSpeed,
       "decAtmFanTable": decAtmFanTable,
       "decAtmFanEntry": decAtmFanEntry,
       "decAtmFanIndex": decAtmFanIndex,
       "decAtmFanStatus": decAtmFanStatus,
       "decAtmFanFaultLedProgram": decAtmFanFaultLedProgram,
       "decAtmFppnTable": decAtmFppnTable,
       "decAtmFppnEntry": decAtmFppnEntry,
       "decAtmFppnSlotNumber": decAtmFppnSlotNumber,
       "decAtmFppnPortOfThatSlot": decAtmFppnPortOfThatSlot,
       "decAtmFppnIfIndex": decAtmFppnIfIndex,
       "decAtmUpgradeSoftware": decAtmUpgradeSoftware,
       "decAtmLoad": decAtmLoad,
       "decAtmLoadAdminStatus": decAtmLoadAdminStatus,
       "decAtmLoadOperStatus": decAtmLoadOperStatus,
       "decAtmLoadFilename": decAtmLoadFilename,
       "decAtmLoadIpHostAddr": decAtmLoadIpHostAddr,
       "decAtmLoadDevSpecific": decAtmLoadDevSpecific,
       "decAtmConfigIpHostAddr": decAtmConfigIpHostAddr,
       "decAtmConfigDefaultGateway": decAtmConfigDefaultGateway,
       "decAtmConfigFilename": decAtmConfigFilename,
       "decAtmConfigStatus": decAtmConfigStatus}
)
