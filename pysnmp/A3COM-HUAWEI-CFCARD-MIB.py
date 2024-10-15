# SNMP MIB module (A3COM-HUAWEI-CFCARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-CFCARD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:24 2024
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

(h3cCfCard,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCfCard")

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

h3cCfCardMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cCfCardMIBObjects_ObjectIdentity = ObjectIdentity
h3cCfCardMIBObjects = _H3cCfCardMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1)
)
if mibBuilder.loadTexts:
    h3cCfCardMIBObjects.setStatus("current")
_H3cCfCardScalarObjects_ObjectIdentity = ObjectIdentity
h3cCfCardScalarObjects = _H3cCfCardScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cCfCardScalarObjects.setStatus("current")


class _H3cCfCardNumber_Type(Integer32):
    """Custom type h3cCfCardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cCfCardNumber_Type.__name__ = "Integer32"
_H3cCfCardNumber_Object = MibScalar
h3cCfCardNumber = _H3cCfCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 1, 1),
    _H3cCfCardNumber_Type()
)
h3cCfCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfCardNumber.setStatus("current")
_H3cCfCardInfoObjects_ObjectIdentity = ObjectIdentity
h3cCfCardInfoObjects = _H3cCfCardInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2)
)
if mibBuilder.loadTexts:
    h3cCfCardInfoObjects.setStatus("current")
_H3cCfCardInfoTable_Object = MibTable
h3cCfCardInfoTable = _H3cCfCardInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    h3cCfCardInfoTable.setStatus("current")
_H3CfCardInfoEntry_Object = MibTableRow
h3CfCardInfoEntry = _H3CfCardInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2, 2, 1)
)
h3CfCardInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardIndex"),
)
if mibBuilder.loadTexts:
    h3CfCardInfoEntry.setStatus("current")


class _H3cCfCardIndex_Type(Integer32):
    """Custom type h3cCfCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_H3cCfCardIndex_Type.__name__ = "Integer32"
_H3cCfCardIndex_Object = MibTableColumn
h3cCfCardIndex = _H3cCfCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2, 2, 1, 1),
    _H3cCfCardIndex_Type()
)
h3cCfCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfCardIndex.setStatus("current")


class _H3cCfCardIsPresent_Type(Integer32):
    """Custom type h3cCfCardIsPresent based on Integer32"""
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


_H3cCfCardIsPresent_Type.__name__ = "Integer32"
_H3cCfCardIsPresent_Object = MibTableColumn
h3cCfCardIsPresent = _H3cCfCardIsPresent_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2, 2, 1, 2),
    _H3cCfCardIsPresent_Type()
)
h3cCfCardIsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfCardIsPresent.setStatus("current")


class _H3cCfCardContainedIn_Type(Integer32):
    """Custom type h3cCfCardContainedIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cCfCardContainedIn_Type.__name__ = "Integer32"
_H3cCfCardContainedIn_Object = MibTableColumn
h3cCfCardContainedIn = _H3cCfCardContainedIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2, 2, 1, 3),
    _H3cCfCardContainedIn_Type()
)
h3cCfCardContainedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfCardContainedIn.setStatus("current")


class _H3cCfCardParentRelPos_Type(Integer32):
    """Custom type h3cCfCardParentRelPos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cCfCardParentRelPos_Type.__name__ = "Integer32"
_H3cCfCardParentRelPos_Object = MibTableColumn
h3cCfCardParentRelPos = _H3cCfCardParentRelPos_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2, 2, 1, 4),
    _H3cCfCardParentRelPos_Type()
)
h3cCfCardParentRelPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfCardParentRelPos.setStatus("current")


class _H3cCfCardDescription_Type(OctetString):
    """Custom type h3cCfCardDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cCfCardDescription_Type.__name__ = "OctetString"
_H3cCfCardDescription_Object = MibTableColumn
h3cCfCardDescription = _H3cCfCardDescription_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2, 2, 1, 5),
    _H3cCfCardDescription_Type()
)
h3cCfCardDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfCardDescription.setStatus("current")


class _H3cCfCardSerialNumber_Type(OctetString):
    """Custom type h3cCfCardSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cCfCardSerialNumber_Type.__name__ = "OctetString"
_H3cCfCardSerialNumber_Object = MibTableColumn
h3cCfCardSerialNumber = _H3cCfCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2, 2, 1, 6),
    _H3cCfCardSerialNumber_Type()
)
h3cCfCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfCardSerialNumber.setStatus("current")


class _H3cCfCardFirewareVersion_Type(OctetString):
    """Custom type h3cCfCardFirewareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cCfCardFirewareVersion_Type.__name__ = "OctetString"
_H3cCfCardFirewareVersion_Object = MibTableColumn
h3cCfCardFirewareVersion = _H3cCfCardFirewareVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2, 2, 1, 7),
    _H3cCfCardFirewareVersion_Type()
)
h3cCfCardFirewareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfCardFirewareVersion.setStatus("current")


class _H3cCfCardModelNumber_Type(OctetString):
    """Custom type h3cCfCardModelNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cCfCardModelNumber_Type.__name__ = "OctetString"
_H3cCfCardModelNumber_Object = MibTableColumn
h3cCfCardModelNumber = _H3cCfCardModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2, 2, 1, 8),
    _H3cCfCardModelNumber_Type()
)
h3cCfCardModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfCardModelNumber.setStatus("current")


class _H3cCfCardState_Type(Integer32):
    """Custom type h3cCfCardState based on Integer32"""
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


_H3cCfCardState_Type.__name__ = "Integer32"
_H3cCfCardState_Object = MibTableColumn
h3cCfCardState = _H3cCfCardState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2, 2, 1, 9),
    _H3cCfCardState_Type()
)
h3cCfCardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfCardState.setStatus("current")
_H3cCfCardSize_Type = Unsigned32
_H3cCfCardSize_Object = MibTableColumn
h3cCfCardSize = _H3cCfCardSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2, 2, 1, 10),
    _H3cCfCardSize_Type()
)
h3cCfCardSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfCardSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cCfCardSize.setUnits("byte")
_H3cCfCardUsedSize_Type = Unsigned32
_H3cCfCardUsedSize_Object = MibTableColumn
h3cCfCardUsedSize = _H3cCfCardUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2, 2, 1, 11),
    _H3cCfCardUsedSize_Type()
)
h3cCfCardUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfCardUsedSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cCfCardUsedSize.setUnits("byte")
_H3cCfCardFreeSize_Type = Unsigned32
_H3cCfCardFreeSize_Object = MibTableColumn
h3cCfCardFreeSize = _H3cCfCardFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 1, 2, 2, 1, 12),
    _H3cCfCardFreeSize_Type()
)
h3cCfCardFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cCfCardFreeSize.setStatus("current")
if mibBuilder.loadTexts:
    h3cCfCardFreeSize.setUnits("byte")
_H3cCfCardNotifications_ObjectIdentity = ObjectIdentity
h3cCfCardNotifications = _H3cCfCardNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 2)
)
if mibBuilder.loadTexts:
    h3cCfCardNotifications.setStatus("current")
_H3cCfCardNotificationsV2_ObjectIdentity = ObjectIdentity
h3cCfCardNotificationsV2 = _H3cCfCardNotificationsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 2, 0)
)
if mibBuilder.loadTexts:
    h3cCfCardNotificationsV2.setStatus("current")
_H3cCfCardMIBConformance_ObjectIdentity = ObjectIdentity
h3cCfCardMIBConformance = _H3cCfCardMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 4)
)
_H3cCfCardMIBGroups_ObjectIdentity = ObjectIdentity
h3cCfCardMIBGroups = _H3cCfCardMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 4, 1)
)
_H3cCfCardMIBCompliances_ObjectIdentity = ObjectIdentity
h3cCfCardMIBCompliances = _H3cCfCardMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 4, 2)
)

# Managed Objects groups

currentObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 4, 1, 1)
)
currentObjectGroup.setObjects(
      *(("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardNumber"),
        ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardIndex"),
        ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardIsPresent"),
        ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardContainedIn"),
        ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardParentRelPos"),
        ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardDescription"),
        ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardSerialNumber"),
        ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardFirewareVersion"),
        ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardModelNumber"),
        ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardState"),
        ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardSize"),
        ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardUsedSize"),
        ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardFreeSize"))
)
if mibBuilder.loadTexts:
    currentObjectGroup.setStatus("current")


# Notification objects

h3cCfCardHotSwapOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 2, 0, 1)
)
h3cCfCardHotSwapOn.setObjects(
      *(("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardContainedIn"),
        ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardParentRelPos"),
        ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardDescription"))
)
if mibBuilder.loadTexts:
    h3cCfCardHotSwapOn.setStatus(
        "current"
    )

h3cCfCardHotSwapOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 2, 0, 2)
)
h3cCfCardHotSwapOff.setObjects(
      *(("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardContainedIn"),
        ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardParentRelPos"),
        ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardDescription"))
)
if mibBuilder.loadTexts:
    h3cCfCardHotSwapOff.setStatus(
        "current"
    )


# Notifications groups

currentNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 4, 1, 2)
)
currentNotificationGroup.setObjects(
      *(("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardHotSwapOn"),
        ("A3COM-HUAWEI-CFCARD-MIB", "h3cCfCardHotSwapOff"))
)
if mibBuilder.loadTexts:
    currentNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

basicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 41, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    basicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-CFCARD-MIB",
    **{"h3cCfCardMIB": h3cCfCardMIB,
       "h3cCfCardMIBObjects": h3cCfCardMIBObjects,
       "h3cCfCardScalarObjects": h3cCfCardScalarObjects,
       "h3cCfCardNumber": h3cCfCardNumber,
       "h3cCfCardInfoObjects": h3cCfCardInfoObjects,
       "h3cCfCardInfoTable": h3cCfCardInfoTable,
       "h3CfCardInfoEntry": h3CfCardInfoEntry,
       "h3cCfCardIndex": h3cCfCardIndex,
       "h3cCfCardIsPresent": h3cCfCardIsPresent,
       "h3cCfCardContainedIn": h3cCfCardContainedIn,
       "h3cCfCardParentRelPos": h3cCfCardParentRelPos,
       "h3cCfCardDescription": h3cCfCardDescription,
       "h3cCfCardSerialNumber": h3cCfCardSerialNumber,
       "h3cCfCardFirewareVersion": h3cCfCardFirewareVersion,
       "h3cCfCardModelNumber": h3cCfCardModelNumber,
       "h3cCfCardState": h3cCfCardState,
       "h3cCfCardSize": h3cCfCardSize,
       "h3cCfCardUsedSize": h3cCfCardUsedSize,
       "h3cCfCardFreeSize": h3cCfCardFreeSize,
       "h3cCfCardNotifications": h3cCfCardNotifications,
       "h3cCfCardNotificationsV2": h3cCfCardNotificationsV2,
       "h3cCfCardHotSwapOn": h3cCfCardHotSwapOn,
       "h3cCfCardHotSwapOff": h3cCfCardHotSwapOff,
       "h3cCfCardMIBConformance": h3cCfCardMIBConformance,
       "h3cCfCardMIBGroups": h3cCfCardMIBGroups,
       "currentObjectGroup": currentObjectGroup,
       "currentNotificationGroup": currentNotificationGroup,
       "h3cCfCardMIBCompliances": h3cCfCardMIBCompliances,
       "basicCompliance": basicCompliance}
)
