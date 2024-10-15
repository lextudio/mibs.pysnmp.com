# SNMP MIB module (HPN-ICF-CFCARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-CFCARD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:34 2024
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

(hpnicfCfCard,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCfCard")

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

hpnicfCfCardMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfCfCardMIBObjects_ObjectIdentity = ObjectIdentity
hpnicfCfCardMIBObjects = _HpnicfCfCardMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfCfCardMIBObjects.setStatus("current")
_HpnicfCfCardScalarObjects_ObjectIdentity = ObjectIdentity
hpnicfCfCardScalarObjects = _HpnicfCfCardScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfCfCardScalarObjects.setStatus("current")


class _HpnicfCfCardNumber_Type(Integer32):
    """Custom type hpnicfCfCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfCfCardNumber_Type.__name__ = "Integer32"
_HpnicfCfCardNumber_Object = MibScalar
hpnicfCfCardNumber = _HpnicfCfCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1, 1, 1, 1),
    _HpnicfCfCardNumber_Type()
)
hpnicfCfCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfCardNumber.setStatus("current")
_HpnicfCfCardInfoObjects_ObjectIdentity = ObjectIdentity
hpnicfCfCardInfoObjects = _HpnicfCfCardInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfCfCardInfoObjects.setStatus("current")
_HpnicfCfCardInfoTable_Object = MibTable
hpnicfCfCardInfoTable = _HpnicfCfCardInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfCfCardInfoTable.setStatus("current")
_HpnicfCfCardInfoEntry_Object = MibTableRow
hpnicfCfCardInfoEntry = _HpnicfCfCardInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1, 1, 2, 2, 1)
)
hpnicfCfCardInfoEntry.setIndexNames(
    (0, "HPN-ICF-CFCARD-MIB", "hpnicfCfCardIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCfCardInfoEntry.setStatus("current")


class _HpnicfCfCardIndex_Type(Integer32):
    """Custom type hpnicfCfCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpnicfCfCardIndex_Type.__name__ = "Integer32"
_HpnicfCfCardIndex_Object = MibTableColumn
hpnicfCfCardIndex = _HpnicfCfCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1, 1, 2, 2, 1, 1),
    _HpnicfCfCardIndex_Type()
)
hpnicfCfCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfCardIndex.setStatus("current")


class _HpnicfCfCardIsPresent_Type(Integer32):
    """Custom type hpnicfCfCardIsPresent based on Integer32"""
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


_HpnicfCfCardIsPresent_Type.__name__ = "Integer32"
_HpnicfCfCardIsPresent_Object = MibTableColumn
hpnicfCfCardIsPresent = _HpnicfCfCardIsPresent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1, 1, 2, 2, 1, 2),
    _HpnicfCfCardIsPresent_Type()
)
hpnicfCfCardIsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfCardIsPresent.setStatus("current")


class _HpnicfCfCardContainedIn_Type(Integer32):
    """Custom type hpnicfCfCardContainedIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfCfCardContainedIn_Type.__name__ = "Integer32"
_HpnicfCfCardContainedIn_Object = MibTableColumn
hpnicfCfCardContainedIn = _HpnicfCfCardContainedIn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1, 1, 2, 2, 1, 3),
    _HpnicfCfCardContainedIn_Type()
)
hpnicfCfCardContainedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfCardContainedIn.setStatus("current")


class _HpnicfCfCardParentRelPos_Type(Integer32):
    """Custom type hpnicfCfCardParentRelPos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfCfCardParentRelPos_Type.__name__ = "Integer32"
_HpnicfCfCardParentRelPos_Object = MibTableColumn
hpnicfCfCardParentRelPos = _HpnicfCfCardParentRelPos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1, 1, 2, 2, 1, 4),
    _HpnicfCfCardParentRelPos_Type()
)
hpnicfCfCardParentRelPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfCardParentRelPos.setStatus("current")


class _HpnicfCfCardDescription_Type(OctetString):
    """Custom type hpnicfCfCardDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfCfCardDescription_Type.__name__ = "OctetString"
_HpnicfCfCardDescription_Object = MibTableColumn
hpnicfCfCardDescription = _HpnicfCfCardDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1, 1, 2, 2, 1, 5),
    _HpnicfCfCardDescription_Type()
)
hpnicfCfCardDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfCardDescription.setStatus("current")


class _HpnicfCfCardSerialNumber_Type(OctetString):
    """Custom type hpnicfCfCardSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfCfCardSerialNumber_Type.__name__ = "OctetString"
_HpnicfCfCardSerialNumber_Object = MibTableColumn
hpnicfCfCardSerialNumber = _HpnicfCfCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1, 1, 2, 2, 1, 6),
    _HpnicfCfCardSerialNumber_Type()
)
hpnicfCfCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfCardSerialNumber.setStatus("current")


class _HpnicfCfCardFirewareVersion_Type(OctetString):
    """Custom type hpnicfCfCardFirewareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfCfCardFirewareVersion_Type.__name__ = "OctetString"
_HpnicfCfCardFirewareVersion_Object = MibTableColumn
hpnicfCfCardFirewareVersion = _HpnicfCfCardFirewareVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1, 1, 2, 2, 1, 7),
    _HpnicfCfCardFirewareVersion_Type()
)
hpnicfCfCardFirewareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfCardFirewareVersion.setStatus("current")


class _HpnicfCfCardModelNumber_Type(OctetString):
    """Custom type hpnicfCfCardModelNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfCfCardModelNumber_Type.__name__ = "OctetString"
_HpnicfCfCardModelNumber_Object = MibTableColumn
hpnicfCfCardModelNumber = _HpnicfCfCardModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1, 1, 2, 2, 1, 8),
    _HpnicfCfCardModelNumber_Type()
)
hpnicfCfCardModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfCardModelNumber.setStatus("current")


class _HpnicfCfCardState_Type(Integer32):
    """Custom type hpnicfCfCardState based on Integer32"""
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


_HpnicfCfCardState_Type.__name__ = "Integer32"
_HpnicfCfCardState_Object = MibTableColumn
hpnicfCfCardState = _HpnicfCfCardState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1, 1, 2, 2, 1, 9),
    _HpnicfCfCardState_Type()
)
hpnicfCfCardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfCardState.setStatus("current")
_HpnicfCfCardSize_Type = Unsigned32
_HpnicfCfCardSize_Object = MibTableColumn
hpnicfCfCardSize = _HpnicfCfCardSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1, 1, 2, 2, 1, 10),
    _HpnicfCfCardSize_Type()
)
hpnicfCfCardSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfCardSize.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfCfCardSize.setUnits("byte")
_HpnicfCfCardUsedSize_Type = Unsigned32
_HpnicfCfCardUsedSize_Object = MibTableColumn
hpnicfCfCardUsedSize = _HpnicfCfCardUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1, 1, 2, 2, 1, 11),
    _HpnicfCfCardUsedSize_Type()
)
hpnicfCfCardUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfCardUsedSize.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfCfCardUsedSize.setUnits("byte")
_HpnicfCfCardFreeSize_Type = Unsigned32
_HpnicfCfCardFreeSize_Object = MibTableColumn
hpnicfCfCardFreeSize = _HpnicfCfCardFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1, 1, 2, 2, 1, 12),
    _HpnicfCfCardFreeSize_Type()
)
hpnicfCfCardFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCfCardFreeSize.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfCfCardFreeSize.setUnits("byte")
_HpnicfCfCardNotifications_ObjectIdentity = ObjectIdentity
hpnicfCfCardNotifications = _HpnicfCfCardNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfCfCardNotifications.setStatus("current")
_HpnicfCfCardNotificationsV2_ObjectIdentity = ObjectIdentity
hpnicfCfCardNotificationsV2 = _HpnicfCfCardNotificationsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1, 2, 0)
)
if mibBuilder.loadTexts:
    hpnicfCfCardNotificationsV2.setStatus("current")
_HpnicfCfCardMIBConformance_ObjectIdentity = ObjectIdentity
hpnicfCfCardMIBConformance = _HpnicfCfCardMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1, 4)
)
_HpnicfCfCardMIBGroups_ObjectIdentity = ObjectIdentity
hpnicfCfCardMIBGroups = _HpnicfCfCardMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1, 4, 1)
)
_HpnicfCfCardMIBCompliances_ObjectIdentity = ObjectIdentity
hpnicfCfCardMIBCompliances = _HpnicfCfCardMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1, 4, 2)
)

# Managed Objects groups

hpnicfcurrentObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1, 4, 1, 1)
)
hpnicfcurrentObjectGroup.setObjects(
      *(("HPN-ICF-CFCARD-MIB", "hpnicfCfCardNumber"),
        ("HPN-ICF-CFCARD-MIB", "hpnicfCfCardIndex"),
        ("HPN-ICF-CFCARD-MIB", "hpnicfCfCardIsPresent"),
        ("HPN-ICF-CFCARD-MIB", "hpnicfCfCardContainedIn"),
        ("HPN-ICF-CFCARD-MIB", "hpnicfCfCardParentRelPos"),
        ("HPN-ICF-CFCARD-MIB", "hpnicfCfCardDescription"),
        ("HPN-ICF-CFCARD-MIB", "hpnicfCfCardSerialNumber"),
        ("HPN-ICF-CFCARD-MIB", "hpnicfCfCardFirewareVersion"),
        ("HPN-ICF-CFCARD-MIB", "hpnicfCfCardModelNumber"),
        ("HPN-ICF-CFCARD-MIB", "hpnicfCfCardState"),
        ("HPN-ICF-CFCARD-MIB", "hpnicfCfCardSize"),
        ("HPN-ICF-CFCARD-MIB", "hpnicfCfCardUsedSize"),
        ("HPN-ICF-CFCARD-MIB", "hpnicfCfCardFreeSize"))
)
if mibBuilder.loadTexts:
    hpnicfcurrentObjectGroup.setStatus("current")


# Notification objects

hpnicfCfCardHotSwapOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1, 2, 0, 1)
)
hpnicfCfCardHotSwapOn.setObjects(
      *(("HPN-ICF-CFCARD-MIB", "hpnicfCfCardContainedIn"),
        ("HPN-ICF-CFCARD-MIB", "hpnicfCfCardParentRelPos"),
        ("HPN-ICF-CFCARD-MIB", "hpnicfCfCardDescription"))
)
if mibBuilder.loadTexts:
    hpnicfCfCardHotSwapOn.setStatus(
        "current"
    )

hpnicfCfCardHotSwapOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1, 2, 0, 2)
)
hpnicfCfCardHotSwapOff.setObjects(
      *(("HPN-ICF-CFCARD-MIB", "hpnicfCfCardContainedIn"),
        ("HPN-ICF-CFCARD-MIB", "hpnicfCfCardParentRelPos"),
        ("HPN-ICF-CFCARD-MIB", "hpnicfCfCardDescription"))
)
if mibBuilder.loadTexts:
    hpnicfCfCardHotSwapOff.setStatus(
        "current"
    )


# Notifications groups

hpnicfcurrentNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1, 4, 1, 2)
)
hpnicfcurrentNotificationGroup.setObjects(
      *(("HPN-ICF-CFCARD-MIB", "hpnicfCfCardHotSwapOn"),
        ("HPN-ICF-CFCARD-MIB", "hpnicfCfCardHotSwapOff"))
)
if mibBuilder.loadTexts:
    hpnicfcurrentNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpnicfbasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfbasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-CFCARD-MIB",
    **{"hpnicfCfCardMIB": hpnicfCfCardMIB,
       "hpnicfCfCardMIBObjects": hpnicfCfCardMIBObjects,
       "hpnicfCfCardScalarObjects": hpnicfCfCardScalarObjects,
       "hpnicfCfCardNumber": hpnicfCfCardNumber,
       "hpnicfCfCardInfoObjects": hpnicfCfCardInfoObjects,
       "hpnicfCfCardInfoTable": hpnicfCfCardInfoTable,
       "hpnicfCfCardInfoEntry": hpnicfCfCardInfoEntry,
       "hpnicfCfCardIndex": hpnicfCfCardIndex,
       "hpnicfCfCardIsPresent": hpnicfCfCardIsPresent,
       "hpnicfCfCardContainedIn": hpnicfCfCardContainedIn,
       "hpnicfCfCardParentRelPos": hpnicfCfCardParentRelPos,
       "hpnicfCfCardDescription": hpnicfCfCardDescription,
       "hpnicfCfCardSerialNumber": hpnicfCfCardSerialNumber,
       "hpnicfCfCardFirewareVersion": hpnicfCfCardFirewareVersion,
       "hpnicfCfCardModelNumber": hpnicfCfCardModelNumber,
       "hpnicfCfCardState": hpnicfCfCardState,
       "hpnicfCfCardSize": hpnicfCfCardSize,
       "hpnicfCfCardUsedSize": hpnicfCfCardUsedSize,
       "hpnicfCfCardFreeSize": hpnicfCfCardFreeSize,
       "hpnicfCfCardNotifications": hpnicfCfCardNotifications,
       "hpnicfCfCardNotificationsV2": hpnicfCfCardNotificationsV2,
       "hpnicfCfCardHotSwapOn": hpnicfCfCardHotSwapOn,
       "hpnicfCfCardHotSwapOff": hpnicfCfCardHotSwapOff,
       "hpnicfCfCardMIBConformance": hpnicfCfCardMIBConformance,
       "hpnicfCfCardMIBGroups": hpnicfCfCardMIBGroups,
       "hpnicfcurrentObjectGroup": hpnicfcurrentObjectGroup,
       "hpnicfcurrentNotificationGroup": hpnicfcurrentNotificationGroup,
       "hpnicfCfCardMIBCompliances": hpnicfCfCardMIBCompliances,
       "hpnicfbasicCompliance": hpnicfbasicCompliance}
)
