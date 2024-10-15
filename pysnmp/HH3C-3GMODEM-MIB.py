# SNMP MIB module (HH3C-3GMODEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-3GMODEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:23 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

hh3c3GModem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98)
)
hh3c3GModem.setRevisions(
        ("2009-04-30 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cUIMStatusType(Integer32, TextualConvention):
    status = "current"
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
        *(("absent", 1),
          ("fault", 3),
          ("initial", 2),
          ("pinLocked", 6),
          ("protected", 5),
          ("pukLocked", 7),
          ("selfDestruct", 8),
          ("unprotected", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3c3GModemObjects_ObjectIdentity = ObjectIdentity
hh3c3GModemObjects = _Hh3c3GModemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1)
)
_Hh3cWirelessCard_ObjectIdentity = ObjectIdentity
hh3cWirelessCard = _Hh3cWirelessCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1)
)
_Hh3cWirelessCardTable_Object = MibTable
hh3cWirelessCardTable = _Hh3cWirelessCardTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cWirelessCardTable.setStatus("current")
_Hh3cWirelessCardEntry_Object = MibTableRow
hh3cWirelessCardEntry = _Hh3cWirelessCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1)
)
hh3cWirelessCardEntry.setIndexNames(
    (0, "HH3C-3GMODEM-MIB", "hh3cWirelessCardIndex"),
)
if mibBuilder.loadTexts:
    hh3cWirelessCardEntry.setStatus("current")


class _Hh3cWirelessCardIndex_Type(Integer32):
    """Custom type hh3cWirelessCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cWirelessCardIndex_Type.__name__ = "Integer32"
_Hh3cWirelessCardIndex_Object = MibTableColumn
hh3cWirelessCardIndex = _Hh3cWirelessCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 1),
    _Hh3cWirelessCardIndex_Type()
)
hh3cWirelessCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWirelessCardIndex.setStatus("current")
_Hh3cWirelessCardModelName_Type = SnmpAdminString
_Hh3cWirelessCardModelName_Object = MibTableColumn
hh3cWirelessCardModelName = _Hh3cWirelessCardModelName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 2),
    _Hh3cWirelessCardModelName_Type()
)
hh3cWirelessCardModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWirelessCardModelName.setStatus("current")
_Hh3cWirelessCardMfgName_Type = SnmpAdminString
_Hh3cWirelessCardMfgName_Object = MibTableColumn
hh3cWirelessCardMfgName = _Hh3cWirelessCardMfgName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 3),
    _Hh3cWirelessCardMfgName_Type()
)
hh3cWirelessCardMfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWirelessCardMfgName.setStatus("current")
_Hh3cWirelessCardDescription_Type = SnmpAdminString
_Hh3cWirelessCardDescription_Object = MibTableColumn
hh3cWirelessCardDescription = _Hh3cWirelessCardDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 4),
    _Hh3cWirelessCardDescription_Type()
)
hh3cWirelessCardDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWirelessCardDescription.setStatus("current")


class _Hh3cWirelessCardSerialNumber_Type(SnmpAdminString):
    """Custom type hh3cWirelessCardSerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cWirelessCardSerialNumber_Type.__name__ = "SnmpAdminString"
_Hh3cWirelessCardSerialNumber_Object = MibTableColumn
hh3cWirelessCardSerialNumber = _Hh3cWirelessCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 5),
    _Hh3cWirelessCardSerialNumber_Type()
)
hh3cWirelessCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWirelessCardSerialNumber.setStatus("current")


class _Hh3cWirelessCardCMIIID_Type(SnmpAdminString):
    """Custom type hh3cWirelessCardCMIIID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cWirelessCardCMIIID_Type.__name__ = "SnmpAdminString"
_Hh3cWirelessCardCMIIID_Object = MibTableColumn
hh3cWirelessCardCMIIID = _Hh3cWirelessCardCMIIID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 6),
    _Hh3cWirelessCardCMIIID_Type()
)
hh3cWirelessCardCMIIID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWirelessCardCMIIID.setStatus("current")
_Hh3cWirelessCardHardwareVersion_Type = SnmpAdminString
_Hh3cWirelessCardHardwareVersion_Object = MibTableColumn
hh3cWirelessCardHardwareVersion = _Hh3cWirelessCardHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 7),
    _Hh3cWirelessCardHardwareVersion_Type()
)
hh3cWirelessCardHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWirelessCardHardwareVersion.setStatus("current")
_Hh3cWirelessCardFirmwareVersion_Type = SnmpAdminString
_Hh3cWirelessCardFirmwareVersion_Object = MibTableColumn
hh3cWirelessCardFirmwareVersion = _Hh3cWirelessCardFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 8),
    _Hh3cWirelessCardFirmwareVersion_Type()
)
hh3cWirelessCardFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWirelessCardFirmwareVersion.setStatus("current")
_Hh3cWirelessCardPRLVersion_Type = SnmpAdminString
_Hh3cWirelessCardPRLVersion_Object = MibTableColumn
hh3cWirelessCardPRLVersion = _Hh3cWirelessCardPRLVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 9),
    _Hh3cWirelessCardPRLVersion_Type()
)
hh3cWirelessCardPRLVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWirelessCardPRLVersion.setStatus("current")
_Hh3cUIM_ObjectIdentity = ObjectIdentity
hh3cUIM = _Hh3cUIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2)
)
_Hh3cUIMInfoTable_Object = MibTable
hh3cUIMInfoTable = _Hh3cUIMInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cUIMInfoTable.setStatus("current")
_Hh3cUIMInfoEntry_Object = MibTableRow
hh3cUIMInfoEntry = _Hh3cUIMInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1)
)
hh3cUIMInfoEntry.setIndexNames(
    (0, "HH3C-3GMODEM-MIB", "hh3cWirelessCardIndex"),
    (0, "HH3C-3GMODEM-MIB", "hh3cUIMIndex"),
)
if mibBuilder.loadTexts:
    hh3cUIMInfoEntry.setStatus("current")


class _Hh3cUIMIndex_Type(Integer32):
    """Custom type hh3cUIMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cUIMIndex_Type.__name__ = "Integer32"
_Hh3cUIMIndex_Object = MibTableColumn
hh3cUIMIndex = _Hh3cUIMIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1, 1),
    _Hh3cUIMIndex_Type()
)
hh3cUIMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cUIMIndex.setStatus("current")
_Hh3cUIMStatus_Type = Hh3cUIMStatusType
_Hh3cUIMStatus_Object = MibTableColumn
hh3cUIMStatus = _Hh3cUIMStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1, 2),
    _Hh3cUIMStatus_Type()
)
hh3cUIMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUIMStatus.setStatus("current")


class _Hh3cUIMImsi_Type(SnmpAdminString):
    """Custom type hh3cUIMImsi based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cUIMImsi_Type.__name__ = "SnmpAdminString"
_Hh3cUIMImsi_Object = MibTableColumn
hh3cUIMImsi = _Hh3cUIMImsi_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1, 3),
    _Hh3cUIMImsi_Type()
)
hh3cUIMImsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUIMImsi.setStatus("current")


class _Hh3cUIMPin_Type(SnmpAdminString):
    """Custom type hh3cUIMPin based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_Hh3cUIMPin_Type.__name__ = "SnmpAdminString"
_Hh3cUIMPin_Object = MibTableColumn
hh3cUIMPin = _Hh3cUIMPin_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1, 4),
    _Hh3cUIMPin_Type()
)
hh3cUIMPin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUIMPin.setStatus("current")


class _Hh3cUIMVoltage_Type(Unsigned32):
    """Custom type hh3cUIMVoltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hh3cUIMVoltage_Type.__name__ = "Unsigned32"
_Hh3cUIMVoltage_Object = MibTableColumn
hh3cUIMVoltage = _Hh3cUIMVoltage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1, 5),
    _Hh3cUIMVoltage_Type()
)
hh3cUIMVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUIMVoltage.setStatus("current")
if mibBuilder.loadTexts:
    hh3cUIMVoltage.setUnits("milli-volt")


class _Hh3cUIMProvider_Type(SnmpAdminString):
    """Custom type hh3cUIMProvider based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cUIMProvider_Type.__name__ = "SnmpAdminString"
_Hh3cUIMProvider_Object = MibTableColumn
hh3cUIMProvider = _Hh3cUIMProvider_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1, 6),
    _Hh3cUIMProvider_Type()
)
hh3cUIMProvider.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUIMProvider.setStatus("current")


class _Hh3cUIMSignal_Type(Integer32):
    """Custom type hh3cUIMSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
        ValueRangeConstraint(99, 99),
    )


_Hh3cUIMSignal_Type.__name__ = "Integer32"
_Hh3cUIMSignal_Object = MibTableColumn
hh3cUIMSignal = _Hh3cUIMSignal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1, 7),
    _Hh3cUIMSignal_Type()
)
hh3cUIMSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUIMSignal.setStatus("current")


class _Hh3cUIMTryPinPukTimes_Type(Unsigned32):
    """Custom type hh3cUIMTryPinPukTimes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hh3cUIMTryPinPukTimes_Type.__name__ = "Unsigned32"
_Hh3cUIMTryPinPukTimes_Object = MibTableColumn
hh3cUIMTryPinPukTimes = _Hh3cUIMTryPinPukTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1, 8),
    _Hh3cUIMTryPinPukTimes_Type()
)
hh3cUIMTryPinPukTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUIMTryPinPukTimes.setStatus("current")


class _Hh3cUIMOldPin_Type(SnmpAdminString):
    """Custom type hh3cUIMOldPin based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_Hh3cUIMOldPin_Type.__name__ = "SnmpAdminString"
_Hh3cUIMOldPin_Object = MibTableColumn
hh3cUIMOldPin = _Hh3cUIMOldPin_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1, 9),
    _Hh3cUIMOldPin_Type()
)
hh3cUIMOldPin.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cUIMOldPin.setStatus("current")
_Hh3c3GModemTrap_ObjectIdentity = ObjectIdentity
hh3c3GModemTrap = _Hh3c3GModemTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 2)
)


class _Hh3cDevSerialNumber_Type(SnmpAdminString):
    """Custom type hh3cDevSerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cDevSerialNumber_Type.__name__ = "SnmpAdminString"
_Hh3cDevSerialNumber_Object = MibScalar
hh3cDevSerialNumber = _Hh3cDevSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 2, 1),
    _Hh3cDevSerialNumber_Type()
)
hh3cDevSerialNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDevSerialNumber.setStatus("current")


class _Hh3cDeviceOUI_Type(SnmpAdminString):
    """Custom type hh3cDeviceOUI based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cDeviceOUI_Type.__name__ = "SnmpAdminString"
_Hh3cDeviceOUI_Object = MibScalar
hh3cDeviceOUI = _Hh3cDeviceOUI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 2, 2),
    _Hh3cDeviceOUI_Type()
)
hh3cDeviceOUI.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDeviceOUI.setStatus("current")


class _Hh3cAccessMedia_Type(Integer32):
    """Custom type hh3cAccessMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("air", 2),
          ("cable", 3),
          ("unknown", 1))
    )


_Hh3cAccessMedia_Type.__name__ = "Integer32"
_Hh3cAccessMedia_Object = MibScalar
hh3cAccessMedia = _Hh3cAccessMedia_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 2, 3),
    _Hh3cAccessMedia_Type()
)
hh3cAccessMedia.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAccessMedia.setStatus("current")
_Hh3c3GModemTraps_ObjectIdentity = ObjectIdentity
hh3c3GModemTraps = _Hh3c3GModemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 3)
)
_Hh3c3GModemTrapPrefix_ObjectIdentity = ObjectIdentity
hh3c3GModemTrapPrefix = _Hh3c3GModemTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 3, 0)
)

# Managed Objects groups


# Notification objects

hh3cWirelessCardInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 3, 0, 1)
)
hh3cWirelessCardInserted.setObjects(
      *(("HH3C-3GMODEM-MIB", "hh3cDeviceOUI"),
        ("HH3C-3GMODEM-MIB", "hh3cDevSerialNumber"),
        ("HH3C-3GMODEM-MIB", "hh3cWirelessCardSerialNumber"),
        ("HH3C-3GMODEM-MIB", "hh3cUIMImsi"))
)
if mibBuilder.loadTexts:
    hh3cWirelessCardInserted.setStatus(
        "current"
    )

hh3cWirelessCardPulledOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 3, 0, 2)
)
hh3cWirelessCardPulledOut.setObjects(
      *(("HH3C-3GMODEM-MIB", "hh3cDeviceOUI"),
        ("HH3C-3GMODEM-MIB", "hh3cDevSerialNumber"),
        ("HH3C-3GMODEM-MIB", "hh3cWirelessCardSerialNumber"),
        ("HH3C-3GMODEM-MIB", "hh3cUIMImsi"))
)
if mibBuilder.loadTexts:
    hh3cWirelessCardPulledOut.setStatus(
        "current"
    )

hh3cUIMPinInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 3, 0, 3)
)
hh3cUIMPinInvalid.setObjects(
      *(("HH3C-3GMODEM-MIB", "hh3cDeviceOUI"),
        ("HH3C-3GMODEM-MIB", "hh3cDevSerialNumber"),
        ("HH3C-3GMODEM-MIB", "hh3cWirelessCardSerialNumber"),
        ("HH3C-3GMODEM-MIB", "hh3cUIMImsi"))
)
if mibBuilder.loadTexts:
    hh3cUIMPinInvalid.setStatus(
        "current"
    )

hh3cUIMPinChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 3, 0, 4)
)
hh3cUIMPinChanged.setObjects(
      *(("HH3C-3GMODEM-MIB", "hh3cDeviceOUI"),
        ("HH3C-3GMODEM-MIB", "hh3cDevSerialNumber"),
        ("HH3C-3GMODEM-MIB", "hh3cWirelessCardSerialNumber"),
        ("HH3C-3GMODEM-MIB", "hh3cUIMImsi"),
        ("HH3C-3GMODEM-MIB", "hh3cUIMOldPin"),
        ("HH3C-3GMODEM-MIB", "hh3cUIMPin"))
)
if mibBuilder.loadTexts:
    hh3cUIMPinChanged.setStatus(
        "current"
    )

hh3cAccessMediaChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 3, 0, 5)
)
hh3cAccessMediaChanged.setObjects(
      *(("HH3C-3GMODEM-MIB", "hh3cDeviceOUI"),
        ("HH3C-3GMODEM-MIB", "hh3cDevSerialNumber"),
        ("HH3C-3GMODEM-MIB", "hh3cWirelessCardSerialNumber"),
        ("HH3C-3GMODEM-MIB", "hh3cUIMImsi"),
        ("HH3C-3GMODEM-MIB", "hh3cAccessMedia"))
)
if mibBuilder.loadTexts:
    hh3cAccessMediaChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-3GMODEM-MIB",
    **{"Hh3cUIMStatusType": Hh3cUIMStatusType,
       "hh3c3GModem": hh3c3GModem,
       "hh3c3GModemObjects": hh3c3GModemObjects,
       "hh3cWirelessCard": hh3cWirelessCard,
       "hh3cWirelessCardTable": hh3cWirelessCardTable,
       "hh3cWirelessCardEntry": hh3cWirelessCardEntry,
       "hh3cWirelessCardIndex": hh3cWirelessCardIndex,
       "hh3cWirelessCardModelName": hh3cWirelessCardModelName,
       "hh3cWirelessCardMfgName": hh3cWirelessCardMfgName,
       "hh3cWirelessCardDescription": hh3cWirelessCardDescription,
       "hh3cWirelessCardSerialNumber": hh3cWirelessCardSerialNumber,
       "hh3cWirelessCardCMIIID": hh3cWirelessCardCMIIID,
       "hh3cWirelessCardHardwareVersion": hh3cWirelessCardHardwareVersion,
       "hh3cWirelessCardFirmwareVersion": hh3cWirelessCardFirmwareVersion,
       "hh3cWirelessCardPRLVersion": hh3cWirelessCardPRLVersion,
       "hh3cUIM": hh3cUIM,
       "hh3cUIMInfoTable": hh3cUIMInfoTable,
       "hh3cUIMInfoEntry": hh3cUIMInfoEntry,
       "hh3cUIMIndex": hh3cUIMIndex,
       "hh3cUIMStatus": hh3cUIMStatus,
       "hh3cUIMImsi": hh3cUIMImsi,
       "hh3cUIMPin": hh3cUIMPin,
       "hh3cUIMVoltage": hh3cUIMVoltage,
       "hh3cUIMProvider": hh3cUIMProvider,
       "hh3cUIMSignal": hh3cUIMSignal,
       "hh3cUIMTryPinPukTimes": hh3cUIMTryPinPukTimes,
       "hh3cUIMOldPin": hh3cUIMOldPin,
       "hh3c3GModemTrap": hh3c3GModemTrap,
       "hh3cDevSerialNumber": hh3cDevSerialNumber,
       "hh3cDeviceOUI": hh3cDeviceOUI,
       "hh3cAccessMedia": hh3cAccessMedia,
       "hh3c3GModemTraps": hh3c3GModemTraps,
       "hh3c3GModemTrapPrefix": hh3c3GModemTrapPrefix,
       "hh3cWirelessCardInserted": hh3cWirelessCardInserted,
       "hh3cWirelessCardPulledOut": hh3cWirelessCardPulledOut,
       "hh3cUIMPinInvalid": hh3cUIMPinInvalid,
       "hh3cUIMPinChanged": hh3cUIMPinChanged,
       "hh3cAccessMediaChanged": hh3cAccessMediaChanged}
)
