# SNMP MIB module (AIILINKTABLE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AIILINKTABLE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:10 2024
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

aiLink = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 16, 2)
)


# Types definitions



class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class IfIndexType(Integer32):
    """Custom type IfIndexType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )




# TEXTUAL-CONVENTIONS



class AIIifType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              18,
              19,
              22,
              23,
              28,
              32,
              37,
              38,
              40,
              48,
              1024,
              1025,
              1026,
              1027,
              1028,
              1029,
              1030,
              1031,
              1032,
              1033)
        )
    )
    namedValues = NamedValues(
        *(("asyncTl1", 1029),
          ("atm", 37),
          ("bridge", 1030),
          ("ds1", 18),
          ("e1", 19),
          ("e2a", 1026),
          ("ethernet-csmacd", 6),
          ("frameRelay", 32),
          ("gasp", 1032),
          ("miox25", 38),
          ("modem", 48),
          ("other", 1),
          ("ppp", 23),
          ("pppAsynchronous", 1033),
          ("propPointToPointSerial", 22),
          ("slip", 28),
          ("sm100BaseFX", 1031),
          ("tabs", 1028),
          ("tbos", 1027),
          ("tl1", 1024),
          ("ttl1", 1025),
          ("x25ple", 40))
    )



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)
_AiSLC2_ObjectIdentity = ObjectIdentity
aiSLC2 = _AiSLC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 16)
)
_AiLinkTable_Object = MibTable
aiLinkTable = _AiLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 1)
)
if mibBuilder.loadTexts:
    aiLinkTable.setStatus("current")
_AiLinkEntry_Object = MibTableRow
aiLinkEntry = _AiLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 1, 1)
)
aiLinkEntry.setIndexNames(
    (0, "AIILINKTABLE-MIB", "aiLinkIndex"),
)
if mibBuilder.loadTexts:
    aiLinkEntry.setStatus("current")
_AiLinkIndex_Type = PositiveInteger
_AiLinkIndex_Object = MibTableColumn
aiLinkIndex = _AiLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 1, 1, 1),
    _AiLinkIndex_Type()
)
aiLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiLinkIndex.setStatus("current")
_AiLinkType_Type = AIIifType
_AiLinkType_Object = MibTableColumn
aiLinkType = _AiLinkType_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 1, 1, 2),
    _AiLinkType_Type()
)
aiLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiLinkType.setStatus("current")


class _AiLinkDescr_Type(DisplayString):
    """Custom type aiLinkDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AiLinkDescr_Type.__name__ = "DisplayString"
_AiLinkDescr_Object = MibTableColumn
aiLinkDescr = _AiLinkDescr_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 1, 1, 3),
    _AiLinkDescr_Type()
)
aiLinkDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiLinkDescr.setStatus("current")
_AiLinkIfIndex_Type = IfIndexType
_AiLinkIfIndex_Object = MibTableColumn
aiLinkIfIndex = _AiLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 1, 1, 4),
    _AiLinkIfIndex_Type()
)
aiLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiLinkIfIndex.setStatus("current")
_AiLinkIfIndex1_Type = IfIndexType
_AiLinkIfIndex1_Object = MibTableColumn
aiLinkIfIndex1 = _AiLinkIfIndex1_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 1, 1, 5),
    _AiLinkIfIndex1_Type()
)
aiLinkIfIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiLinkIfIndex1.setStatus("current")
_AiLinkIfIndex2_Type = IfIndexType
_AiLinkIfIndex2_Object = MibTableColumn
aiLinkIfIndex2 = _AiLinkIfIndex2_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 1, 1, 6),
    _AiLinkIfIndex2_Type()
)
aiLinkIfIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiLinkIfIndex2.setStatus("current")
_AiLinkIfIndex3_Type = IfIndexType
_AiLinkIfIndex3_Object = MibTableColumn
aiLinkIfIndex3 = _AiLinkIfIndex3_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 1, 1, 7),
    _AiLinkIfIndex3_Type()
)
aiLinkIfIndex3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiLinkIfIndex3.setStatus("current")
_AiLinkIfIndex4_Type = IfIndexType
_AiLinkIfIndex4_Object = MibTableColumn
aiLinkIfIndex4 = _AiLinkIfIndex4_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 1, 1, 8),
    _AiLinkIfIndex4_Type()
)
aiLinkIfIndex4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiLinkIfIndex4.setStatus("current")


class _AiLinkPhysIf_Type(Integer32):
    """Custom type aiLinkPhysIf based on Integer32"""
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
        *(("ds1", 5),
          ("e1", 6),
          ("ethernet-csmacd", 4),
          ("fiber", 7),
          ("rs232", 1),
          ("rs530", 2),
          ("rs530m", 8),
          ("v35", 3))
    )


_AiLinkPhysIf_Type.__name__ = "Integer32"
_AiLinkPhysIf_Object = MibTableColumn
aiLinkPhysIf = _AiLinkPhysIf_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 1, 1, 9),
    _AiLinkPhysIf_Type()
)
aiLinkPhysIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiLinkPhysIf.setStatus("current")
_AiLinkX25Table_Object = MibTable
aiLinkX25Table = _AiLinkX25Table_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 2)
)
if mibBuilder.loadTexts:
    aiLinkX25Table.setStatus("current")
_AiLinkX25Entry_Object = MibTableRow
aiLinkX25Entry = _AiLinkX25Entry_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 2, 1)
)
aiLinkX25Entry.setIndexNames(
    (0, "AIILINKTABLE-MIB", "aiLinkX25Index"),
)
if mibBuilder.loadTexts:
    aiLinkX25Entry.setStatus("current")
_AiLinkX25Index_Type = PositiveInteger
_AiLinkX25Index_Object = MibTableColumn
aiLinkX25Index = _AiLinkX25Index_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 2, 1, 1),
    _AiLinkX25Index_Type()
)
aiLinkX25Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiLinkX25Index.setStatus("current")


class _AiLinkX25Negotiation_Type(Integer32):
    """Custom type aiLinkX25Negotiation based on Integer32"""
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


_AiLinkX25Negotiation_Type.__name__ = "Integer32"
_AiLinkX25Negotiation_Object = MibTableColumn
aiLinkX25Negotiation = _AiLinkX25Negotiation_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 2, 1, 2),
    _AiLinkX25Negotiation_Type()
)
aiLinkX25Negotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiLinkX25Negotiation.setStatus("current")


class _AiLinkX25LinkMode_Type(Integer32):
    """Custom type aiLinkX25LinkMode based on Integer32"""
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
        *(("extended", 3),
          ("normal", 1),
          ("passive", 2))
    )


_AiLinkX25LinkMode_Type.__name__ = "Integer32"
_AiLinkX25LinkMode_Object = MibTableColumn
aiLinkX25LinkMode = _AiLinkX25LinkMode_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 2, 1, 3),
    _AiLinkX25LinkMode_Type()
)
aiLinkX25LinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiLinkX25LinkMode.setStatus("current")
_AiLinkConformance_ObjectIdentity = ObjectIdentity
aiLinkConformance = _AiLinkConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 3)
)
_AiLinkGroups_ObjectIdentity = ObjectIdentity
aiLinkGroups = _AiLinkGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 3, 1)
)
_AiLinkCompliances_ObjectIdentity = ObjectIdentity
aiLinkCompliances = _AiLinkCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 3, 2)
)
_AiLinkT1Table_Object = MibTable
aiLinkT1Table = _AiLinkT1Table_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 4)
)
if mibBuilder.loadTexts:
    aiLinkT1Table.setStatus("current")
_AiLinkT1Entry_Object = MibTableRow
aiLinkT1Entry = _AiLinkT1Entry_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 4, 1)
)
aiLinkT1Entry.setIndexNames(
    (0, "AIILINKTABLE-MIB", "aiLinkT1Index"),
)
if mibBuilder.loadTexts:
    aiLinkT1Entry.setStatus("current")
_AiLinkT1Index_Type = PositiveInteger
_AiLinkT1Index_Object = MibTableColumn
aiLinkT1Index = _AiLinkT1Index_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 4, 1, 1),
    _AiLinkT1Index_Type()
)
aiLinkT1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiLinkT1Index.setStatus("current")


class _AiLinkT1LineBuildOut_Type(Integer32):
    """Custom type aiLinkT1LineBuildOut based on Integer32"""
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
        *(("lbo0to133ft", 1),
          ("lbo133to266ft", 2),
          ("lbo266to399ft", 3),
          ("lbo399to533ft", 4),
          ("lbo533to655ft", 5))
    )


_AiLinkT1LineBuildOut_Type.__name__ = "Integer32"
_AiLinkT1LineBuildOut_Object = MibTableColumn
aiLinkT1LineBuildOut = _AiLinkT1LineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 4, 1, 2),
    _AiLinkT1LineBuildOut_Type()
)
aiLinkT1LineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiLinkT1LineBuildOut.setStatus("current")


class _AiLinkT1TimeslotSpeed_Type(Integer32):
    """Custom type aiLinkT1TimeslotSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tss56K", 1),
          ("tss64K", 2))
    )


_AiLinkT1TimeslotSpeed_Type.__name__ = "Integer32"
_AiLinkT1TimeslotSpeed_Object = MibTableColumn
aiLinkT1TimeslotSpeed = _AiLinkT1TimeslotSpeed_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 4, 1, 3),
    _AiLinkT1TimeslotSpeed_Type()
)
aiLinkT1TimeslotSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiLinkT1TimeslotSpeed.setStatus("current")


class _AiLinkT1TimeslotsString_Type(DisplayString):
    """Custom type aiLinkT1TimeslotsString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_AiLinkT1TimeslotsString_Type.__name__ = "DisplayString"
_AiLinkT1TimeslotsString_Object = MibTableColumn
aiLinkT1TimeslotsString = _AiLinkT1TimeslotsString_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 4, 1, 4),
    _AiLinkT1TimeslotsString_Type()
)
aiLinkT1TimeslotsString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiLinkT1TimeslotsString.setStatus("current")
_AiLinkT1Timeslots_Type = PositiveInteger
_AiLinkT1Timeslots_Object = MibTableColumn
aiLinkT1Timeslots = _AiLinkT1Timeslots_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 4, 1, 5),
    _AiLinkT1Timeslots_Type()
)
aiLinkT1Timeslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiLinkT1Timeslots.setStatus("current")
_AiLinkE1Table_Object = MibTable
aiLinkE1Table = _AiLinkE1Table_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 5)
)
if mibBuilder.loadTexts:
    aiLinkE1Table.setStatus("current")
_AiLinkE1Entry_Object = MibTableRow
aiLinkE1Entry = _AiLinkE1Entry_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 5, 1)
)
aiLinkE1Entry.setIndexNames(
    (0, "AIILINKTABLE-MIB", "aiLinkE1Index"),
)
if mibBuilder.loadTexts:
    aiLinkE1Entry.setStatus("current")
_AiLinkE1Index_Type = PositiveInteger
_AiLinkE1Index_Object = MibTableColumn
aiLinkE1Index = _AiLinkE1Index_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 5, 1, 1),
    _AiLinkE1Index_Type()
)
aiLinkE1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiLinkE1Index.setStatus("current")


class _AiLinkE1TimeslotSpeed_Type(Integer32):
    """Custom type aiLinkE1TimeslotSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tss56K", 1),
          ("tss64K", 2))
    )


_AiLinkE1TimeslotSpeed_Type.__name__ = "Integer32"
_AiLinkE1TimeslotSpeed_Object = MibTableColumn
aiLinkE1TimeslotSpeed = _AiLinkE1TimeslotSpeed_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 5, 1, 2),
    _AiLinkE1TimeslotSpeed_Type()
)
aiLinkE1TimeslotSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiLinkE1TimeslotSpeed.setStatus("current")


class _AiLinkE1TimeslotsString_Type(DisplayString):
    """Custom type aiLinkE1TimeslotsString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_AiLinkE1TimeslotsString_Type.__name__ = "DisplayString"
_AiLinkE1TimeslotsString_Object = MibTableColumn
aiLinkE1TimeslotsString = _AiLinkE1TimeslotsString_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 5, 1, 3),
    _AiLinkE1TimeslotsString_Type()
)
aiLinkE1TimeslotsString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiLinkE1TimeslotsString.setStatus("current")
_AiLinkE1Timeslots_Type = PositiveInteger
_AiLinkE1Timeslots_Object = MibTableColumn
aiLinkE1Timeslots = _AiLinkE1Timeslots_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 5, 1, 4),
    _AiLinkE1Timeslots_Type()
)
aiLinkE1Timeslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiLinkE1Timeslots.setStatus("current")

# Managed Objects groups

aiLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 3, 1, 1)
)
aiLinkGroup.setObjects(
      *(("AIILINKTABLE-MIB", "aiLinkIndex"),
        ("AIILINKTABLE-MIB", "aiLinkType"),
        ("AIILINKTABLE-MIB", "aiLinkDescr"),
        ("AIILINKTABLE-MIB", "aiLinkIfIndex"),
        ("AIILINKTABLE-MIB", "aiLinkIfIndex1"),
        ("AIILINKTABLE-MIB", "aiLinkIfIndex2"),
        ("AIILINKTABLE-MIB", "aiLinkIfIndex3"),
        ("AIILINKTABLE-MIB", "aiLinkIfIndex4"))
)
if mibBuilder.loadTexts:
    aiLinkGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aiLinkCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 539, 16, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    aiLinkCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AIILINKTABLE-MIB",
    **{"PositiveInteger": PositiveInteger,
       "IfIndexType": IfIndexType,
       "AIIifType": AIIifType,
       "aii": aii,
       "aiSLC2": aiSLC2,
       "aiLink": aiLink,
       "aiLinkTable": aiLinkTable,
       "aiLinkEntry": aiLinkEntry,
       "aiLinkIndex": aiLinkIndex,
       "aiLinkType": aiLinkType,
       "aiLinkDescr": aiLinkDescr,
       "aiLinkIfIndex": aiLinkIfIndex,
       "aiLinkIfIndex1": aiLinkIfIndex1,
       "aiLinkIfIndex2": aiLinkIfIndex2,
       "aiLinkIfIndex3": aiLinkIfIndex3,
       "aiLinkIfIndex4": aiLinkIfIndex4,
       "aiLinkPhysIf": aiLinkPhysIf,
       "aiLinkX25Table": aiLinkX25Table,
       "aiLinkX25Entry": aiLinkX25Entry,
       "aiLinkX25Index": aiLinkX25Index,
       "aiLinkX25Negotiation": aiLinkX25Negotiation,
       "aiLinkX25LinkMode": aiLinkX25LinkMode,
       "aiLinkConformance": aiLinkConformance,
       "aiLinkGroups": aiLinkGroups,
       "aiLinkGroup": aiLinkGroup,
       "aiLinkCompliances": aiLinkCompliances,
       "aiLinkCompliance": aiLinkCompliance,
       "aiLinkT1Table": aiLinkT1Table,
       "aiLinkT1Entry": aiLinkT1Entry,
       "aiLinkT1Index": aiLinkT1Index,
       "aiLinkT1LineBuildOut": aiLinkT1LineBuildOut,
       "aiLinkT1TimeslotSpeed": aiLinkT1TimeslotSpeed,
       "aiLinkT1TimeslotsString": aiLinkT1TimeslotsString,
       "aiLinkT1Timeslots": aiLinkT1Timeslots,
       "aiLinkE1Table": aiLinkE1Table,
       "aiLinkE1Entry": aiLinkE1Entry,
       "aiLinkE1Index": aiLinkE1Index,
       "aiLinkE1TimeslotSpeed": aiLinkE1TimeslotSpeed,
       "aiLinkE1TimeslotsString": aiLinkE1TimeslotsString,
       "aiLinkE1Timeslots": aiLinkE1Timeslots}
)
