# SNMP MIB module (HH3C-CFCARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-CFCARD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:35 2024
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

(hh3cCfCard,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCfCard")

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

hh3cCfCardMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cCfCardMIBObjects_ObjectIdentity = ObjectIdentity
hh3cCfCardMIBObjects = _Hh3cCfCardMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cCfCardMIBObjects.setStatus("current")
_Hh3cCfCardScalarObjects_ObjectIdentity = ObjectIdentity
hh3cCfCardScalarObjects = _Hh3cCfCardScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cCfCardScalarObjects.setStatus("current")


class _Hh3cCfCardNumber_Type(Integer32):
    """Custom type hh3cCfCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cCfCardNumber_Type.__name__ = "Integer32"
_Hh3cCfCardNumber_Object = MibScalar
hh3cCfCardNumber = _Hh3cCfCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1, 1, 1, 1),
    _Hh3cCfCardNumber_Type()
)
hh3cCfCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfCardNumber.setStatus("current")
_Hh3cCfCardInfoObjects_ObjectIdentity = ObjectIdentity
hh3cCfCardInfoObjects = _Hh3cCfCardInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cCfCardInfoObjects.setStatus("current")
_Hh3cCfCardInfoTable_Object = MibTable
hh3cCfCardInfoTable = _Hh3cCfCardInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cCfCardInfoTable.setStatus("current")
_Hh3cCfCardInfoEntry_Object = MibTableRow
hh3cCfCardInfoEntry = _Hh3cCfCardInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1, 1, 2, 2, 1)
)
hh3cCfCardInfoEntry.setIndexNames(
    (0, "HH3C-CFCARD-MIB", "hh3cCfCardIndex"),
)
if mibBuilder.loadTexts:
    hh3cCfCardInfoEntry.setStatus("current")


class _Hh3cCfCardIndex_Type(Integer32):
    """Custom type hh3cCfCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cCfCardIndex_Type.__name__ = "Integer32"
_Hh3cCfCardIndex_Object = MibTableColumn
hh3cCfCardIndex = _Hh3cCfCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1, 1, 2, 2, 1, 1),
    _Hh3cCfCardIndex_Type()
)
hh3cCfCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfCardIndex.setStatus("current")


class _Hh3cCfCardIsPresent_Type(Integer32):
    """Custom type hh3cCfCardIsPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Hh3cCfCardIsPresent_Type.__name__ = "Integer32"
_Hh3cCfCardIsPresent_Object = MibTableColumn
hh3cCfCardIsPresent = _Hh3cCfCardIsPresent_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1, 1, 2, 2, 1, 2),
    _Hh3cCfCardIsPresent_Type()
)
hh3cCfCardIsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfCardIsPresent.setStatus("current")


class _Hh3cCfCardContainedIn_Type(Integer32):
    """Custom type hh3cCfCardContainedIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cCfCardContainedIn_Type.__name__ = "Integer32"
_Hh3cCfCardContainedIn_Object = MibTableColumn
hh3cCfCardContainedIn = _Hh3cCfCardContainedIn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1, 1, 2, 2, 1, 3),
    _Hh3cCfCardContainedIn_Type()
)
hh3cCfCardContainedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfCardContainedIn.setStatus("current")


class _Hh3cCfCardParentRelPos_Type(Integer32):
    """Custom type hh3cCfCardParentRelPos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cCfCardParentRelPos_Type.__name__ = "Integer32"
_Hh3cCfCardParentRelPos_Object = MibTableColumn
hh3cCfCardParentRelPos = _Hh3cCfCardParentRelPos_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1, 1, 2, 2, 1, 4),
    _Hh3cCfCardParentRelPos_Type()
)
hh3cCfCardParentRelPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfCardParentRelPos.setStatus("current")


class _Hh3cCfCardDescription_Type(OctetString):
    """Custom type hh3cCfCardDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cCfCardDescription_Type.__name__ = "OctetString"
_Hh3cCfCardDescription_Object = MibTableColumn
hh3cCfCardDescription = _Hh3cCfCardDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1, 1, 2, 2, 1, 5),
    _Hh3cCfCardDescription_Type()
)
hh3cCfCardDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfCardDescription.setStatus("current")


class _Hh3cCfCardSerialNumber_Type(OctetString):
    """Custom type hh3cCfCardSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cCfCardSerialNumber_Type.__name__ = "OctetString"
_Hh3cCfCardSerialNumber_Object = MibTableColumn
hh3cCfCardSerialNumber = _Hh3cCfCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1, 1, 2, 2, 1, 6),
    _Hh3cCfCardSerialNumber_Type()
)
hh3cCfCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfCardSerialNumber.setStatus("current")


class _Hh3cCfCardFirewareVersion_Type(OctetString):
    """Custom type hh3cCfCardFirewareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cCfCardFirewareVersion_Type.__name__ = "OctetString"
_Hh3cCfCardFirewareVersion_Object = MibTableColumn
hh3cCfCardFirewareVersion = _Hh3cCfCardFirewareVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1, 1, 2, 2, 1, 7),
    _Hh3cCfCardFirewareVersion_Type()
)
hh3cCfCardFirewareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfCardFirewareVersion.setStatus("current")


class _Hh3cCfCardModelNumber_Type(OctetString):
    """Custom type hh3cCfCardModelNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cCfCardModelNumber_Type.__name__ = "OctetString"
_Hh3cCfCardModelNumber_Object = MibTableColumn
hh3cCfCardModelNumber = _Hh3cCfCardModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1, 1, 2, 2, 1, 8),
    _Hh3cCfCardModelNumber_Type()
)
hh3cCfCardModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfCardModelNumber.setStatus("current")


class _Hh3cCfCardState_Type(Integer32):
    """Custom type hh3cCfCardState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              128,
              240,
              255)
        )
    )
    namedValues = NamedValues(
        *(("sCMPError", 5),
          ("sECCError", 4),
          ("sFormatError", 2),
          ("sIOError", 240),
          ("sNoError", 1),
          ("sOther", 255),
          ("sSectorBufferError", 3),
          ("sSlaveError", 128))
    )


_Hh3cCfCardState_Type.__name__ = "Integer32"
_Hh3cCfCardState_Object = MibTableColumn
hh3cCfCardState = _Hh3cCfCardState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1, 1, 2, 2, 1, 9),
    _Hh3cCfCardState_Type()
)
hh3cCfCardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfCardState.setStatus("current")
_Hh3cCfCardSize_Type = Unsigned32
_Hh3cCfCardSize_Object = MibTableColumn
hh3cCfCardSize = _Hh3cCfCardSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1, 1, 2, 2, 1, 10),
    _Hh3cCfCardSize_Type()
)
hh3cCfCardSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfCardSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cCfCardSize.setUnits("byte")
_Hh3cCfCardUsedSize_Type = Unsigned32
_Hh3cCfCardUsedSize_Object = MibTableColumn
hh3cCfCardUsedSize = _Hh3cCfCardUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1, 1, 2, 2, 1, 11),
    _Hh3cCfCardUsedSize_Type()
)
hh3cCfCardUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfCardUsedSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cCfCardUsedSize.setUnits("byte")
_Hh3cCfCardFreeSize_Type = Unsigned32
_Hh3cCfCardFreeSize_Object = MibTableColumn
hh3cCfCardFreeSize = _Hh3cCfCardFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1, 1, 2, 2, 1, 12),
    _Hh3cCfCardFreeSize_Type()
)
hh3cCfCardFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCfCardFreeSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cCfCardFreeSize.setUnits("byte")
_Hh3cCfCardNotifications_ObjectIdentity = ObjectIdentity
hh3cCfCardNotifications = _Hh3cCfCardNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cCfCardNotifications.setStatus("current")
_Hh3cCfCardNotificationsV2_ObjectIdentity = ObjectIdentity
hh3cCfCardNotificationsV2 = _Hh3cCfCardNotificationsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1, 2, 0)
)
if mibBuilder.loadTexts:
    hh3cCfCardNotificationsV2.setStatus("current")
_Hh3cCfCardMIBConformance_ObjectIdentity = ObjectIdentity
hh3cCfCardMIBConformance = _Hh3cCfCardMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1, 4)
)
_Hh3cCfCardMIBGroups_ObjectIdentity = ObjectIdentity
hh3cCfCardMIBGroups = _Hh3cCfCardMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1, 4, 1)
)
_Hh3cCfCardMIBCompliances_ObjectIdentity = ObjectIdentity
hh3cCfCardMIBCompliances = _Hh3cCfCardMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1, 4, 2)
)

# Managed Objects groups

hh3ccurrentObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1, 4, 1, 1)
)
hh3ccurrentObjectGroup.setObjects(
      *(("HH3C-CFCARD-MIB", "hh3cCfCardNumber"),
        ("HH3C-CFCARD-MIB", "hh3cCfCardIndex"),
        ("HH3C-CFCARD-MIB", "hh3cCfCardIsPresent"),
        ("HH3C-CFCARD-MIB", "hh3cCfCardContainedIn"),
        ("HH3C-CFCARD-MIB", "hh3cCfCardParentRelPos"),
        ("HH3C-CFCARD-MIB", "hh3cCfCardDescription"),
        ("HH3C-CFCARD-MIB", "hh3cCfCardSerialNumber"),
        ("HH3C-CFCARD-MIB", "hh3cCfCardFirewareVersion"),
        ("HH3C-CFCARD-MIB", "hh3cCfCardModelNumber"),
        ("HH3C-CFCARD-MIB", "hh3cCfCardState"),
        ("HH3C-CFCARD-MIB", "hh3cCfCardSize"),
        ("HH3C-CFCARD-MIB", "hh3cCfCardUsedSize"),
        ("HH3C-CFCARD-MIB", "hh3cCfCardFreeSize"))
)
if mibBuilder.loadTexts:
    hh3ccurrentObjectGroup.setStatus("current")


# Notification objects

hh3cCfCardHotSwapOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1, 2, 0, 1)
)
hh3cCfCardHotSwapOn.setObjects(
      *(("HH3C-CFCARD-MIB", "hh3cCfCardContainedIn"),
        ("HH3C-CFCARD-MIB", "hh3cCfCardParentRelPos"),
        ("HH3C-CFCARD-MIB", "hh3cCfCardDescription"))
)
if mibBuilder.loadTexts:
    hh3cCfCardHotSwapOn.setStatus(
        "current"
    )

hh3cCfCardHotSwapOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1, 2, 0, 2)
)
hh3cCfCardHotSwapOff.setObjects(
      *(("HH3C-CFCARD-MIB", "hh3cCfCardContainedIn"),
        ("HH3C-CFCARD-MIB", "hh3cCfCardParentRelPos"),
        ("HH3C-CFCARD-MIB", "hh3cCfCardDescription"))
)
if mibBuilder.loadTexts:
    hh3cCfCardHotSwapOff.setStatus(
        "current"
    )


# Notifications groups

hh3ccurrentNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1, 4, 1, 2)
)
hh3ccurrentNotificationGroup.setObjects(
      *(("HH3C-CFCARD-MIB", "hh3cCfCardHotSwapOn"),
        ("HH3C-CFCARD-MIB", "hh3cCfCardHotSwapOff"))
)
if mibBuilder.loadTexts:
    hh3ccurrentNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hh3cbasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cbasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-CFCARD-MIB",
    **{"hh3cCfCardMIB": hh3cCfCardMIB,
       "hh3cCfCardMIBObjects": hh3cCfCardMIBObjects,
       "hh3cCfCardScalarObjects": hh3cCfCardScalarObjects,
       "hh3cCfCardNumber": hh3cCfCardNumber,
       "hh3cCfCardInfoObjects": hh3cCfCardInfoObjects,
       "hh3cCfCardInfoTable": hh3cCfCardInfoTable,
       "hh3cCfCardInfoEntry": hh3cCfCardInfoEntry,
       "hh3cCfCardIndex": hh3cCfCardIndex,
       "hh3cCfCardIsPresent": hh3cCfCardIsPresent,
       "hh3cCfCardContainedIn": hh3cCfCardContainedIn,
       "hh3cCfCardParentRelPos": hh3cCfCardParentRelPos,
       "hh3cCfCardDescription": hh3cCfCardDescription,
       "hh3cCfCardSerialNumber": hh3cCfCardSerialNumber,
       "hh3cCfCardFirewareVersion": hh3cCfCardFirewareVersion,
       "hh3cCfCardModelNumber": hh3cCfCardModelNumber,
       "hh3cCfCardState": hh3cCfCardState,
       "hh3cCfCardSize": hh3cCfCardSize,
       "hh3cCfCardUsedSize": hh3cCfCardUsedSize,
       "hh3cCfCardFreeSize": hh3cCfCardFreeSize,
       "hh3cCfCardNotifications": hh3cCfCardNotifications,
       "hh3cCfCardNotificationsV2": hh3cCfCardNotificationsV2,
       "hh3cCfCardHotSwapOn": hh3cCfCardHotSwapOn,
       "hh3cCfCardHotSwapOff": hh3cCfCardHotSwapOff,
       "hh3cCfCardMIBConformance": hh3cCfCardMIBConformance,
       "hh3cCfCardMIBGroups": hh3cCfCardMIBGroups,
       "hh3ccurrentObjectGroup": hh3ccurrentObjectGroup,
       "hh3ccurrentNotificationGroup": hh3ccurrentNotificationGroup,
       "hh3cCfCardMIBCompliances": hh3cCfCardMIBCompliances,
       "hh3cbasicCompliance": hh3cbasicCompliance}
)
