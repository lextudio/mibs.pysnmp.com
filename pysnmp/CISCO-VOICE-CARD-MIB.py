# SNMP MIB module (CISCO-VOICE-CARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VOICE-CARD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:18 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoVoiceCard = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300576)
)
ciscoVoiceCard.setRevisions(
        ("2002-02-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoVoiceCardNotifications_ObjectIdentity = ObjectIdentity
ciscoVoiceCardNotifications = _CiscoVoiceCardNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300576, 0)
)
_CiscoVoiceCardObjects_ObjectIdentity = ObjectIdentity
ciscoVoiceCardObjects = _CiscoVoiceCardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300576, 1)
)
_CVoiceCardTable_Object = MibTable
cVoiceCardTable = _CVoiceCardTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300576, 1, 1)
)
if mibBuilder.loadTexts:
    cVoiceCardTable.setStatus("current")
_CVoiceCardEntry_Object = MibTableRow
cVoiceCardEntry = _CVoiceCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300576, 1, 1, 1)
)
cVoiceCardEntry.setIndexNames(
    (0, "CISCO-VOICE-CARD-MIB", "cVoiceCardIndex"),
)
if mibBuilder.loadTexts:
    cVoiceCardEntry.setStatus("current")


class _CVoiceCardIndex_Type(Unsigned32):
    """Custom type cVoiceCardIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CVoiceCardIndex_Type.__name__ = "Unsigned32"
_CVoiceCardIndex_Object = MibTableColumn
cVoiceCardIndex = _CVoiceCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300576, 1, 1, 1, 1),
    _CVoiceCardIndex_Type()
)
cVoiceCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cVoiceCardIndex.setStatus("current")


class _CVoiceCardSlotNumber_Type(Unsigned32):
    """Custom type cVoiceCardSlotNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CVoiceCardSlotNumber_Type.__name__ = "Unsigned32"
_CVoiceCardSlotNumber_Object = MibTableColumn
cVoiceCardSlotNumber = _CVoiceCardSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300576, 1, 1, 1, 2),
    _CVoiceCardSlotNumber_Type()
)
cVoiceCardSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVoiceCardSlotNumber.setStatus("current")


class _CVoiceCardCodecComplexity_Type(Integer32):
    """Custom type cVoiceCardCodecComplexity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("hc", 2),
          ("mc", 4))
    )


_CVoiceCardCodecComplexity_Type.__name__ = "Integer32"
_CVoiceCardCodecComplexity_Object = MibTableColumn
cVoiceCardCodecComplexity = _CVoiceCardCodecComplexity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300576, 1, 1, 1, 3),
    _CVoiceCardCodecComplexity_Type()
)
cVoiceCardCodecComplexity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cVoiceCardCodecComplexity.setStatus("current")


class _CVoiceCardAdminStatus_Type(Integer32):
    """Custom type cVoiceCardAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CVoiceCardAdminStatus_Type.__name__ = "Integer32"
_CVoiceCardAdminStatus_Object = MibTableColumn
cVoiceCardAdminStatus = _CVoiceCardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 300576, 1, 1, 1, 4),
    _CVoiceCardAdminStatus_Type()
)
cVoiceCardAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cVoiceCardAdminStatus.setStatus("current")
_CiscoVoiceCardConformance_ObjectIdentity = ObjectIdentity
ciscoVoiceCardConformance = _CiscoVoiceCardConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300576, 2)
)
_CiscoVoiceCardMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVoiceCardMIBCompliances = _CiscoVoiceCardMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300576, 2, 1)
)
_CiscoVoiceCardMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVoiceCardMIBGroups = _CiscoVoiceCardMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 300576, 2, 2)
)

# Managed Objects groups

ciscoVoiceCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 300576, 2, 2, 1)
)
ciscoVoiceCardGroup.setObjects(
      *(("CISCO-VOICE-CARD-MIB", "cVoiceCardSlotNumber"),
        ("CISCO-VOICE-CARD-MIB", "cVoiceCardCodecComplexity"),
        ("CISCO-VOICE-CARD-MIB", "cVoiceCardAdminStatus"))
)
if mibBuilder.loadTexts:
    ciscoVoiceCardGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoVoiceCardMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 300576, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoVoiceCardMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VOICE-CARD-MIB",
    **{"ciscoVoiceCard": ciscoVoiceCard,
       "ciscoVoiceCardNotifications": ciscoVoiceCardNotifications,
       "ciscoVoiceCardObjects": ciscoVoiceCardObjects,
       "cVoiceCardTable": cVoiceCardTable,
       "cVoiceCardEntry": cVoiceCardEntry,
       "cVoiceCardIndex": cVoiceCardIndex,
       "cVoiceCardSlotNumber": cVoiceCardSlotNumber,
       "cVoiceCardCodecComplexity": cVoiceCardCodecComplexity,
       "cVoiceCardAdminStatus": cVoiceCardAdminStatus,
       "ciscoVoiceCardConformance": ciscoVoiceCardConformance,
       "ciscoVoiceCardMIBCompliances": ciscoVoiceCardMIBCompliances,
       "ciscoVoiceCardMIBCompliance": ciscoVoiceCardMIBCompliance,
       "ciscoVoiceCardMIBGroups": ciscoVoiceCardMIBGroups,
       "ciscoVoiceCardGroup": ciscoVoiceCardGroup}
)
