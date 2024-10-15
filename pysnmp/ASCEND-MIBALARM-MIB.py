# SNMP MIB module (ASCEND-MIBALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBALARM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:02 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibalarmProfile_ObjectIdentity = ObjectIdentity
mibalarmProfile = _MibalarmProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 33)
)
_MibalarmProfileTable_Object = MibTable
mibalarmProfileTable = _MibalarmProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 33, 1)
)
if mibBuilder.loadTexts:
    mibalarmProfileTable.setStatus("mandatory")
_MibalarmProfileEntry_Object = MibTableRow
mibalarmProfileEntry = _MibalarmProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 33, 1, 1)
)
mibalarmProfileEntry.setIndexNames(
    (0, "ASCEND-MIBALARM-MIB", "alarmProfile-Name"),
)
if mibBuilder.loadTexts:
    mibalarmProfileEntry.setStatus("mandatory")
_AlarmProfile_Name_Type = DisplayString
_AlarmProfile_Name_Object = MibScalar
alarmProfile_Name = _AlarmProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 33, 1, 1, 1),
    _AlarmProfile_Name_Type()
)
alarmProfile_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmProfile_Name.setStatus("mandatory")


class _AlarmProfile_Enabled_Type(Integer32):
    """Custom type alarmProfile_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AlarmProfile_Enabled_Type.__name__ = "Integer32"
_AlarmProfile_Enabled_Object = MibScalar
alarmProfile_Enabled = _AlarmProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 33, 1, 1, 2),
    _AlarmProfile_Enabled_Type()
)
alarmProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmProfile_Enabled.setStatus("mandatory")


class _AlarmProfile_Event_Type(Integer32):
    """Custom type alarmProfile_Event based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("dpramCbusFailure", 11),
          ("fanFailure", 5),
          ("highTemperatureTrigger", 10),
          ("inputRelayClosed", 7),
          ("inputRelayOpen", 8),
          ("lineStateChange", 1),
          ("lowTemperatureTrigger", 9),
          ("powerFailure", 4),
          ("primarySwitchover", 3),
          ("secondaryControllerStateChange", 6),
          ("slotStateChange", 2))
    )


_AlarmProfile_Event_Type.__name__ = "Integer32"
_AlarmProfile_Event_Object = MibScalar
alarmProfile_Event = _AlarmProfile_Event_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 33, 1, 1, 3),
    _AlarmProfile_Event_Type()
)
alarmProfile_Event.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmProfile_Event.setStatus("mandatory")


class _AlarmProfile_PhysicalAddress_Shelf_Type(Integer32):
    """Custom type alarmProfile_PhysicalAddress_Shelf based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("anyShelf", 1),
          ("shelf1", 2),
          ("shelf2", 3),
          ("shelf3", 4),
          ("shelf4", 5),
          ("shelf5", 6),
          ("shelf6", 7),
          ("shelf7", 8),
          ("shelf8", 9),
          ("shelf9", 10))
    )


_AlarmProfile_PhysicalAddress_Shelf_Type.__name__ = "Integer32"
_AlarmProfile_PhysicalAddress_Shelf_Object = MibScalar
alarmProfile_PhysicalAddress_Shelf = _AlarmProfile_PhysicalAddress_Shelf_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 33, 1, 1, 4),
    _AlarmProfile_PhysicalAddress_Shelf_Type()
)
alarmProfile_PhysicalAddress_Shelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmProfile_PhysicalAddress_Shelf.setStatus("mandatory")


class _AlarmProfile_PhysicalAddress_Slot_Type(Integer32):
    """Custom type alarmProfile_PhysicalAddress_Slot based on Integer32"""
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
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              45,
              46,
              49,
              50,
              51,
              53,
              54,
              55,
              56,
              57,
              58,
              59)
        )
    )
    namedValues = NamedValues(
        *(("aLim", 55),
          ("anySlot", 1),
          ("bLim", 56),
          ("cLim", 57),
          ("controlModule", 51),
          ("controller", 42),
          ("dLim", 58),
          ("firstControlModule", 53),
          ("leftController", 49),
          ("rightController", 50),
          ("secondControlModule", 54),
          ("slot1", 2),
          ("slot10", 11),
          ("slot11", 12),
          ("slot12", 13),
          ("slot13", 14),
          ("slot14", 15),
          ("slot15", 16),
          ("slot16", 17),
          ("slot17", 18),
          ("slot18", 19),
          ("slot19", 20),
          ("slot2", 3),
          ("slot20", 21),
          ("slot21", 22),
          ("slot22", 23),
          ("slot23", 24),
          ("slot24", 25),
          ("slot25", 26),
          ("slot26", 27),
          ("slot27", 28),
          ("slot28", 29),
          ("slot29", 30),
          ("slot3", 4),
          ("slot30", 31),
          ("slot31", 32),
          ("slot32", 33),
          ("slot33", 34),
          ("slot34", 35),
          ("slot35", 36),
          ("slot36", 37),
          ("slot37", 38),
          ("slot38", 39),
          ("slot39", 40),
          ("slot4", 5),
          ("slot40", 41),
          ("slot5", 6),
          ("slot6", 7),
          ("slot7", 8),
          ("slot8", 9),
          ("slot9", 10),
          ("slotPrimary", 59),
          ("trunkModule1", 45),
          ("trunkModule2", 46))
    )


_AlarmProfile_PhysicalAddress_Slot_Type.__name__ = "Integer32"
_AlarmProfile_PhysicalAddress_Slot_Object = MibScalar
alarmProfile_PhysicalAddress_Slot = _AlarmProfile_PhysicalAddress_Slot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 33, 1, 1, 5),
    _AlarmProfile_PhysicalAddress_Slot_Type()
)
alarmProfile_PhysicalAddress_Slot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmProfile_PhysicalAddress_Slot.setStatus("mandatory")
_AlarmProfile_PhysicalAddress_ItemNumber_Type = Integer32
_AlarmProfile_PhysicalAddress_ItemNumber_Object = MibScalar
alarmProfile_PhysicalAddress_ItemNumber = _AlarmProfile_PhysicalAddress_ItemNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 33, 1, 1, 6),
    _AlarmProfile_PhysicalAddress_ItemNumber_Type()
)
alarmProfile_PhysicalAddress_ItemNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmProfile_PhysicalAddress_ItemNumber.setStatus("mandatory")


class _AlarmProfile_Action_AlarmLedMinor_Type(Integer32):
    """Custom type alarmProfile_Action_AlarmLedMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AlarmProfile_Action_AlarmLedMinor_Type.__name__ = "Integer32"
_AlarmProfile_Action_AlarmLedMinor_Object = MibScalar
alarmProfile_Action_AlarmLedMinor = _AlarmProfile_Action_AlarmLedMinor_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 33, 1, 1, 7),
    _AlarmProfile_Action_AlarmLedMinor_Type()
)
alarmProfile_Action_AlarmLedMinor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmProfile_Action_AlarmLedMinor.setStatus("mandatory")


class _AlarmProfile_Action_AlarmLedMajor_Type(Integer32):
    """Custom type alarmProfile_Action_AlarmLedMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AlarmProfile_Action_AlarmLedMajor_Type.__name__ = "Integer32"
_AlarmProfile_Action_AlarmLedMajor_Object = MibScalar
alarmProfile_Action_AlarmLedMajor = _AlarmProfile_Action_AlarmLedMajor_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 33, 1, 1, 8),
    _AlarmProfile_Action_AlarmLedMajor_Type()
)
alarmProfile_Action_AlarmLedMajor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmProfile_Action_AlarmLedMajor.setStatus("mandatory")


class _AlarmProfile_Action_AlarmRelayMinor_Type(Integer32):
    """Custom type alarmProfile_Action_AlarmRelayMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AlarmProfile_Action_AlarmRelayMinor_Type.__name__ = "Integer32"
_AlarmProfile_Action_AlarmRelayMinor_Object = MibScalar
alarmProfile_Action_AlarmRelayMinor = _AlarmProfile_Action_AlarmRelayMinor_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 33, 1, 1, 9),
    _AlarmProfile_Action_AlarmRelayMinor_Type()
)
alarmProfile_Action_AlarmRelayMinor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmProfile_Action_AlarmRelayMinor.setStatus("mandatory")
_AlarmProfile_Action_AlarmRelayMinorDuration_Type = Integer32
_AlarmProfile_Action_AlarmRelayMinorDuration_Object = MibScalar
alarmProfile_Action_AlarmRelayMinorDuration = _AlarmProfile_Action_AlarmRelayMinorDuration_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 33, 1, 1, 10),
    _AlarmProfile_Action_AlarmRelayMinorDuration_Type()
)
alarmProfile_Action_AlarmRelayMinorDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmProfile_Action_AlarmRelayMinorDuration.setStatus("mandatory")


class _AlarmProfile_Action_AlarmRelayMajor_Type(Integer32):
    """Custom type alarmProfile_Action_AlarmRelayMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AlarmProfile_Action_AlarmRelayMajor_Type.__name__ = "Integer32"
_AlarmProfile_Action_AlarmRelayMajor_Object = MibScalar
alarmProfile_Action_AlarmRelayMajor = _AlarmProfile_Action_AlarmRelayMajor_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 33, 1, 1, 11),
    _AlarmProfile_Action_AlarmRelayMajor_Type()
)
alarmProfile_Action_AlarmRelayMajor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmProfile_Action_AlarmRelayMajor.setStatus("mandatory")
_AlarmProfile_Action_AlarmRelayMajorDuration_Type = Integer32
_AlarmProfile_Action_AlarmRelayMajorDuration_Object = MibScalar
alarmProfile_Action_AlarmRelayMajorDuration = _AlarmProfile_Action_AlarmRelayMajorDuration_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 33, 1, 1, 12),
    _AlarmProfile_Action_AlarmRelayMajorDuration_Type()
)
alarmProfile_Action_AlarmRelayMajorDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmProfile_Action_AlarmRelayMajorDuration.setStatus("mandatory")


class _AlarmProfile_Action_o_Type(Integer32):
    """Custom type alarmProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_AlarmProfile_Action_o_Type.__name__ = "Integer32"
_AlarmProfile_Action_o_Object = MibScalar
alarmProfile_Action_o = _AlarmProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 33, 1, 1, 13),
    _AlarmProfile_Action_o_Type()
)
alarmProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBALARM-MIB",
    **{"DisplayString": DisplayString,
       "mibalarmProfile": mibalarmProfile,
       "mibalarmProfileTable": mibalarmProfileTable,
       "mibalarmProfileEntry": mibalarmProfileEntry,
       "alarmProfile-Name": alarmProfile_Name,
       "alarmProfile-Enabled": alarmProfile_Enabled,
       "alarmProfile-Event": alarmProfile_Event,
       "alarmProfile-PhysicalAddress-Shelf": alarmProfile_PhysicalAddress_Shelf,
       "alarmProfile-PhysicalAddress-Slot": alarmProfile_PhysicalAddress_Slot,
       "alarmProfile-PhysicalAddress-ItemNumber": alarmProfile_PhysicalAddress_ItemNumber,
       "alarmProfile-Action-AlarmLedMinor": alarmProfile_Action_AlarmLedMinor,
       "alarmProfile-Action-AlarmLedMajor": alarmProfile_Action_AlarmLedMajor,
       "alarmProfile-Action-AlarmRelayMinor": alarmProfile_Action_AlarmRelayMinor,
       "alarmProfile-Action-AlarmRelayMinorDuration": alarmProfile_Action_AlarmRelayMinorDuration,
       "alarmProfile-Action-AlarmRelayMajor": alarmProfile_Action_AlarmRelayMajor,
       "alarmProfile-Action-AlarmRelayMajorDuration": alarmProfile_Action_AlarmRelayMajorDuration,
       "alarmProfile-Action-o": alarmProfile_Action_o}
)
