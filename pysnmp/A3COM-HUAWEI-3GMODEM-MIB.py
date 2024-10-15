# SNMP MIB module (A3COM-HUAWEI-3GMODEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-3GMODEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:13 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

h3c3GModem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98)
)
h3c3GModem.setRevisions(
        ("2009-04-30 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cUIMStatusType(Integer32, TextualConvention):
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

_H3c3GModemObjects_ObjectIdentity = ObjectIdentity
h3c3GModemObjects = _H3c3GModemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1)
)
_H3cWirelessCard_ObjectIdentity = ObjectIdentity
h3cWirelessCard = _H3cWirelessCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 1)
)
_H3cWirelessCardTable_Object = MibTable
h3cWirelessCardTable = _H3cWirelessCardTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cWirelessCardTable.setStatus("current")
_H3cWirelessCardEntry_Object = MibTableRow
h3cWirelessCardEntry = _H3cWirelessCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 1, 1, 1)
)
h3cWirelessCardEntry.setIndexNames(
    (0, "A3COM-HUAWEI-3GMODEM-MIB", "h3cWirelessCardIndex"),
)
if mibBuilder.loadTexts:
    h3cWirelessCardEntry.setStatus("current")


class _H3cWirelessCardIndex_Type(Integer32):
    """Custom type h3cWirelessCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cWirelessCardIndex_Type.__name__ = "Integer32"
_H3cWirelessCardIndex_Object = MibTableColumn
h3cWirelessCardIndex = _H3cWirelessCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 1, 1, 1, 1),
    _H3cWirelessCardIndex_Type()
)
h3cWirelessCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWirelessCardIndex.setStatus("current")


class _H3cWirelessCardModelName_Type(SnmpAdminString):
    """Custom type h3cWirelessCardModelName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cWirelessCardModelName_Type.__name__ = "SnmpAdminString"
_H3cWirelessCardModelName_Object = MibTableColumn
h3cWirelessCardModelName = _H3cWirelessCardModelName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 1, 1, 1, 2),
    _H3cWirelessCardModelName_Type()
)
h3cWirelessCardModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWirelessCardModelName.setStatus("current")


class _H3cWirelessCardMfgName_Type(SnmpAdminString):
    """Custom type h3cWirelessCardMfgName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cWirelessCardMfgName_Type.__name__ = "SnmpAdminString"
_H3cWirelessCardMfgName_Object = MibTableColumn
h3cWirelessCardMfgName = _H3cWirelessCardMfgName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 1, 1, 1, 3),
    _H3cWirelessCardMfgName_Type()
)
h3cWirelessCardMfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWirelessCardMfgName.setStatus("current")


class _H3cWirelessCardDescription_Type(SnmpAdminString):
    """Custom type h3cWirelessCardDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cWirelessCardDescription_Type.__name__ = "SnmpAdminString"
_H3cWirelessCardDescription_Object = MibTableColumn
h3cWirelessCardDescription = _H3cWirelessCardDescription_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 1, 1, 1, 4),
    _H3cWirelessCardDescription_Type()
)
h3cWirelessCardDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWirelessCardDescription.setStatus("current")


class _H3cWirelessCardSerialNumber_Type(SnmpAdminString):
    """Custom type h3cWirelessCardSerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cWirelessCardSerialNumber_Type.__name__ = "SnmpAdminString"
_H3cWirelessCardSerialNumber_Object = MibTableColumn
h3cWirelessCardSerialNumber = _H3cWirelessCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 1, 1, 1, 5),
    _H3cWirelessCardSerialNumber_Type()
)
h3cWirelessCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWirelessCardSerialNumber.setStatus("current")


class _H3cWirelessCardCMIIID_Type(SnmpAdminString):
    """Custom type h3cWirelessCardCMIIID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cWirelessCardCMIIID_Type.__name__ = "SnmpAdminString"
_H3cWirelessCardCMIIID_Object = MibTableColumn
h3cWirelessCardCMIIID = _H3cWirelessCardCMIIID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 1, 1, 1, 6),
    _H3cWirelessCardCMIIID_Type()
)
h3cWirelessCardCMIIID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWirelessCardCMIIID.setStatus("current")


class _H3cWirelessCardHardwareVersion_Type(SnmpAdminString):
    """Custom type h3cWirelessCardHardwareVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cWirelessCardHardwareVersion_Type.__name__ = "SnmpAdminString"
_H3cWirelessCardHardwareVersion_Object = MibTableColumn
h3cWirelessCardHardwareVersion = _H3cWirelessCardHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 1, 1, 1, 7),
    _H3cWirelessCardHardwareVersion_Type()
)
h3cWirelessCardHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWirelessCardHardwareVersion.setStatus("current")


class _H3cWirelessCardFirmwareVersion_Type(SnmpAdminString):
    """Custom type h3cWirelessCardFirmwareVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cWirelessCardFirmwareVersion_Type.__name__ = "SnmpAdminString"
_H3cWirelessCardFirmwareVersion_Object = MibTableColumn
h3cWirelessCardFirmwareVersion = _H3cWirelessCardFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 1, 1, 1, 8),
    _H3cWirelessCardFirmwareVersion_Type()
)
h3cWirelessCardFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWirelessCardFirmwareVersion.setStatus("current")


class _H3cWirelessCardPRLVersion_Type(SnmpAdminString):
    """Custom type h3cWirelessCardPRLVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cWirelessCardPRLVersion_Type.__name__ = "SnmpAdminString"
_H3cWirelessCardPRLVersion_Object = MibTableColumn
h3cWirelessCardPRLVersion = _H3cWirelessCardPRLVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 1, 1, 1, 9),
    _H3cWirelessCardPRLVersion_Type()
)
h3cWirelessCardPRLVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWirelessCardPRLVersion.setStatus("current")
_H3cWirelessCardInterfaceIndex_Type = InterfaceIndex
_H3cWirelessCardInterfaceIndex_Object = MibTableColumn
h3cWirelessCardInterfaceIndex = _H3cWirelessCardInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 1, 1, 1, 10),
    _H3cWirelessCardInterfaceIndex_Type()
)
h3cWirelessCardInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWirelessCardInterfaceIndex.setStatus("current")


class _H3cWirelessCardModemStatus_Type(Integer32):
    """Custom type h3cWirelessCardModemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("offLine", 3),
          ("onLine", 2),
          ("unknown", 1))
    )


_H3cWirelessCardModemStatus_Type.__name__ = "Integer32"
_H3cWirelessCardModemStatus_Object = MibTableColumn
h3cWirelessCardModemStatus = _H3cWirelessCardModemStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 1, 1, 1, 11),
    _H3cWirelessCardModemStatus_Type()
)
h3cWirelessCardModemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWirelessCardModemStatus.setStatus("current")


class _H3cWirelessCardCurServiceStatus_Type(Integer32):
    """Custom type h3cWirelessCardCurServiceStatus based on Integer32"""
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
        *(("available", 2),
          ("emergency", 3),
          ("lowPower", 4),
          ("noService", 5),
          ("unknown", 1))
    )


_H3cWirelessCardCurServiceStatus_Type.__name__ = "Integer32"
_H3cWirelessCardCurServiceStatus_Object = MibTableColumn
h3cWirelessCardCurServiceStatus = _H3cWirelessCardCurServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 1, 1, 1, 12),
    _H3cWirelessCardCurServiceStatus_Type()
)
h3cWirelessCardCurServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWirelessCardCurServiceStatus.setStatus("current")


class _H3cWirelessCardCurRoamingStatus_Type(Integer32):
    """Custom type h3cWirelessCardCurRoamingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("home", 3),
          ("roaming", 2),
          ("unknown", 1))
    )


_H3cWirelessCardCurRoamingStatus_Type.__name__ = "Integer32"
_H3cWirelessCardCurRoamingStatus_Object = MibTableColumn
h3cWirelessCardCurRoamingStatus = _H3cWirelessCardCurRoamingStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 1, 1, 1, 13),
    _H3cWirelessCardCurRoamingStatus_Type()
)
h3cWirelessCardCurRoamingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cWirelessCardCurRoamingStatus.setStatus("current")
_H3cUIM_ObjectIdentity = ObjectIdentity
h3cUIM = _H3cUIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 2)
)
_H3cUIMInfoTable_Object = MibTable
h3cUIMInfoTable = _H3cUIMInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cUIMInfoTable.setStatus("current")
_H3cUIMInfoEntry_Object = MibTableRow
h3cUIMInfoEntry = _H3cUIMInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 2, 1, 1)
)
h3cUIMInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-3GMODEM-MIB", "h3cWirelessCardIndex"),
    (0, "A3COM-HUAWEI-3GMODEM-MIB", "h3cUIMIndex"),
)
if mibBuilder.loadTexts:
    h3cUIMInfoEntry.setStatus("current")


class _H3cUIMIndex_Type(Integer32):
    """Custom type h3cUIMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cUIMIndex_Type.__name__ = "Integer32"
_H3cUIMIndex_Object = MibTableColumn
h3cUIMIndex = _H3cUIMIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 2, 1, 1, 1),
    _H3cUIMIndex_Type()
)
h3cUIMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cUIMIndex.setStatus("current")
_H3cUIMStatus_Type = H3cUIMStatusType
_H3cUIMStatus_Object = MibTableColumn
h3cUIMStatus = _H3cUIMStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 2, 1, 1, 2),
    _H3cUIMStatus_Type()
)
h3cUIMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cUIMStatus.setStatus("current")


class _H3cUIMImsi_Type(SnmpAdminString):
    """Custom type h3cUIMImsi based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cUIMImsi_Type.__name__ = "SnmpAdminString"
_H3cUIMImsi_Object = MibTableColumn
h3cUIMImsi = _H3cUIMImsi_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 2, 1, 1, 3),
    _H3cUIMImsi_Type()
)
h3cUIMImsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cUIMImsi.setStatus("current")


class _H3cUIMPin_Type(SnmpAdminString):
    """Custom type h3cUIMPin based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_H3cUIMPin_Type.__name__ = "SnmpAdminString"
_H3cUIMPin_Object = MibTableColumn
h3cUIMPin = _H3cUIMPin_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 2, 1, 1, 4),
    _H3cUIMPin_Type()
)
h3cUIMPin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cUIMPin.setStatus("current")


class _H3cUIMVoltage_Type(Unsigned32):
    """Custom type h3cUIMVoltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_H3cUIMVoltage_Type.__name__ = "Unsigned32"
_H3cUIMVoltage_Object = MibTableColumn
h3cUIMVoltage = _H3cUIMVoltage_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 2, 1, 1, 5),
    _H3cUIMVoltage_Type()
)
h3cUIMVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cUIMVoltage.setStatus("current")
if mibBuilder.loadTexts:
    h3cUIMVoltage.setUnits("milli-volt")


class _H3cUIMProvider_Type(SnmpAdminString):
    """Custom type h3cUIMProvider based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cUIMProvider_Type.__name__ = "SnmpAdminString"
_H3cUIMProvider_Object = MibTableColumn
h3cUIMProvider = _H3cUIMProvider_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 2, 1, 1, 6),
    _H3cUIMProvider_Type()
)
h3cUIMProvider.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cUIMProvider.setStatus("current")


class _H3cUIMSignal_Type(Integer32):
    """Custom type h3cUIMSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
        ValueRangeConstraint(99, 99),
    )


_H3cUIMSignal_Type.__name__ = "Integer32"
_H3cUIMSignal_Object = MibTableColumn
h3cUIMSignal = _H3cUIMSignal_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 2, 1, 1, 7),
    _H3cUIMSignal_Type()
)
h3cUIMSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cUIMSignal.setStatus("current")


class _H3cUIMTryPinPukTimes_Type(Unsigned32):
    """Custom type h3cUIMTryPinPukTimes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_H3cUIMTryPinPukTimes_Type.__name__ = "Unsigned32"
_H3cUIMTryPinPukTimes_Object = MibTableColumn
h3cUIMTryPinPukTimes = _H3cUIMTryPinPukTimes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 2, 1, 1, 8),
    _H3cUIMTryPinPukTimes_Type()
)
h3cUIMTryPinPukTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cUIMTryPinPukTimes.setStatus("current")


class _H3cUIMOldPin_Type(SnmpAdminString):
    """Custom type h3cUIMOldPin based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_H3cUIMOldPin_Type.__name__ = "SnmpAdminString"
_H3cUIMOldPin_Object = MibTableColumn
h3cUIMOldPin = _H3cUIMOldPin_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 2, 1, 1, 9),
    _H3cUIMOldPin_Type()
)
h3cUIMOldPin.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cUIMOldPin.setStatus("current")
_H3c3GCdma_ObjectIdentity = ObjectIdentity
h3c3GCdma = _H3c3GCdma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 3)
)
_H3c3GCdma1xRttTable_Object = MibTable
h3c3GCdma1xRttTable = _H3c3GCdma1xRttTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 3, 1)
)
if mibBuilder.loadTexts:
    h3c3GCdma1xRttTable.setStatus("current")
_H3c3GCdma1xRttEntry_Object = MibTableRow
h3c3GCdma1xRttEntry = _H3c3GCdma1xRttEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 3, 1, 1)
)
h3c3GCdma1xRttEntry.setIndexNames(
    (0, "A3COM-HUAWEI-3GMODEM-MIB", "h3cWirelessCardIndex"),
)
if mibBuilder.loadTexts:
    h3c3GCdma1xRttEntry.setStatus("current")


class _H3c3GCdma1xRttCurrentRssi_Type(Integer32):
    """Custom type h3c3GCdma1xRttCurrentRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_H3c3GCdma1xRttCurrentRssi_Type.__name__ = "Integer32"
_H3c3GCdma1xRttCurrentRssi_Object = MibTableColumn
h3c3GCdma1xRttCurrentRssi = _H3c3GCdma1xRttCurrentRssi_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 3, 1, 1, 1),
    _H3c3GCdma1xRttCurrentRssi_Type()
)
h3c3GCdma1xRttCurrentRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GCdma1xRttCurrentRssi.setStatus("current")
if mibBuilder.loadTexts:
    h3c3GCdma1xRttCurrentRssi.setUnits("dBm")


class _H3c3GCdma1xRttRssiMediumThreshold_Type(Integer32):
    """Custom type h3c3GCdma1xRttRssiMediumThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_H3c3GCdma1xRttRssiMediumThreshold_Type.__name__ = "Integer32"
_H3c3GCdma1xRttRssiMediumThreshold_Object = MibTableColumn
h3c3GCdma1xRttRssiMediumThreshold = _H3c3GCdma1xRttRssiMediumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 3, 1, 1, 2),
    _H3c3GCdma1xRttRssiMediumThreshold_Type()
)
h3c3GCdma1xRttRssiMediumThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3c3GCdma1xRttRssiMediumThreshold.setStatus("current")
if mibBuilder.loadTexts:
    h3c3GCdma1xRttRssiMediumThreshold.setUnits("dBm")


class _H3c3GCdma1xRttRssiWeakThreshold_Type(Integer32):
    """Custom type h3c3GCdma1xRttRssiWeakThreshold based on Integer32"""
    defaultValue = -150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_H3c3GCdma1xRttRssiWeakThreshold_Type.__name__ = "Integer32"
_H3c3GCdma1xRttRssiWeakThreshold_Object = MibTableColumn
h3c3GCdma1xRttRssiWeakThreshold = _H3c3GCdma1xRttRssiWeakThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 3, 1, 1, 3),
    _H3c3GCdma1xRttRssiWeakThreshold_Type()
)
h3c3GCdma1xRttRssiWeakThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3c3GCdma1xRttRssiWeakThreshold.setStatus("current")
if mibBuilder.loadTexts:
    h3c3GCdma1xRttRssiWeakThreshold.setUnits("dBm")
_H3c3GCdmaEvDoTable_Object = MibTable
h3c3GCdmaEvDoTable = _H3c3GCdmaEvDoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 3, 2)
)
if mibBuilder.loadTexts:
    h3c3GCdmaEvDoTable.setStatus("current")
_H3c3GCdmaEvDoEntry_Object = MibTableRow
h3c3GCdmaEvDoEntry = _H3c3GCdmaEvDoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 3, 2, 1)
)
h3c3GCdmaEvDoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-3GMODEM-MIB", "h3cWirelessCardIndex"),
)
if mibBuilder.loadTexts:
    h3c3GCdmaEvDoEntry.setStatus("current")


class _H3c3GCdmaEvDoCurrentRssi_Type(Integer32):
    """Custom type h3c3GCdmaEvDoCurrentRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_H3c3GCdmaEvDoCurrentRssi_Type.__name__ = "Integer32"
_H3c3GCdmaEvDoCurrentRssi_Object = MibTableColumn
h3c3GCdmaEvDoCurrentRssi = _H3c3GCdmaEvDoCurrentRssi_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 3, 2, 1, 1),
    _H3c3GCdmaEvDoCurrentRssi_Type()
)
h3c3GCdmaEvDoCurrentRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GCdmaEvDoCurrentRssi.setStatus("current")
if mibBuilder.loadTexts:
    h3c3GCdmaEvDoCurrentRssi.setUnits("dBm")


class _H3c3GCdmaEvDoRssiMediumThreshold_Type(Integer32):
    """Custom type h3c3GCdmaEvDoRssiMediumThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_H3c3GCdmaEvDoRssiMediumThreshold_Type.__name__ = "Integer32"
_H3c3GCdmaEvDoRssiMediumThreshold_Object = MibTableColumn
h3c3GCdmaEvDoRssiMediumThreshold = _H3c3GCdmaEvDoRssiMediumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 3, 2, 1, 2),
    _H3c3GCdmaEvDoRssiMediumThreshold_Type()
)
h3c3GCdmaEvDoRssiMediumThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3c3GCdmaEvDoRssiMediumThreshold.setStatus("current")
if mibBuilder.loadTexts:
    h3c3GCdmaEvDoRssiMediumThreshold.setUnits("dBm")


class _H3c3GCdmaEvDoRssiWeakThreshold_Type(Integer32):
    """Custom type h3c3GCdmaEvDoRssiWeakThreshold based on Integer32"""
    defaultValue = -150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_H3c3GCdmaEvDoRssiWeakThreshold_Type.__name__ = "Integer32"
_H3c3GCdmaEvDoRssiWeakThreshold_Object = MibTableColumn
h3c3GCdmaEvDoRssiWeakThreshold = _H3c3GCdmaEvDoRssiWeakThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 3, 2, 1, 3),
    _H3c3GCdmaEvDoRssiWeakThreshold_Type()
)
h3c3GCdmaEvDoRssiWeakThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3c3GCdmaEvDoRssiWeakThreshold.setStatus("current")
if mibBuilder.loadTexts:
    h3c3GCdmaEvDoRssiWeakThreshold.setUnits("dBm")
_H3c3GGsm_ObjectIdentity = ObjectIdentity
h3c3GGsm = _H3c3GGsm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 4)
)
_H3c3GGsmInfoTable_Object = MibTable
h3c3GGsmInfoTable = _H3c3GGsmInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 4, 1)
)
if mibBuilder.loadTexts:
    h3c3GGsmInfoTable.setStatus("current")
_H3c3GGsmInfoEntry_Object = MibTableRow
h3c3GGsmInfoEntry = _H3c3GGsmInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 4, 1, 1)
)
h3c3GGsmInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-3GMODEM-MIB", "h3cWirelessCardIndex"),
)
if mibBuilder.loadTexts:
    h3c3GGsmInfoEntry.setStatus("current")


class _H3c3GGsmCurrentRssi_Type(Integer32):
    """Custom type h3c3GGsmCurrentRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_H3c3GGsmCurrentRssi_Type.__name__ = "Integer32"
_H3c3GGsmCurrentRssi_Object = MibTableColumn
h3c3GGsmCurrentRssi = _H3c3GGsmCurrentRssi_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 4, 1, 1, 1),
    _H3c3GGsmCurrentRssi_Type()
)
h3c3GGsmCurrentRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GGsmCurrentRssi.setStatus("current")
if mibBuilder.loadTexts:
    h3c3GGsmCurrentRssi.setUnits("dBm")


class _H3c3GGsmRssiMediumThreshold_Type(Integer32):
    """Custom type h3c3GGsmRssiMediumThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_H3c3GGsmRssiMediumThreshold_Type.__name__ = "Integer32"
_H3c3GGsmRssiMediumThreshold_Object = MibTableColumn
h3c3GGsmRssiMediumThreshold = _H3c3GGsmRssiMediumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 4, 1, 1, 2),
    _H3c3GGsmRssiMediumThreshold_Type()
)
h3c3GGsmRssiMediumThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3c3GGsmRssiMediumThreshold.setStatus("current")
if mibBuilder.loadTexts:
    h3c3GGsmRssiMediumThreshold.setUnits("dBm")


class _H3c3GGsmRssiWeakThreshold_Type(Integer32):
    """Custom type h3c3GGsmRssiWeakThreshold based on Integer32"""
    defaultValue = -150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_H3c3GGsmRssiWeakThreshold_Type.__name__ = "Integer32"
_H3c3GGsmRssiWeakThreshold_Object = MibTableColumn
h3c3GGsmRssiWeakThreshold = _H3c3GGsmRssiWeakThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 4, 1, 1, 3),
    _H3c3GGsmRssiWeakThreshold_Type()
)
h3c3GGsmRssiWeakThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3c3GGsmRssiWeakThreshold.setStatus("current")
if mibBuilder.loadTexts:
    h3c3GGsmRssiWeakThreshold.setUnits("dBm")


class _H3c3GGsmImsi_Type(SnmpAdminString):
    """Custom type h3c3GGsmImsi based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3c3GGsmImsi_Type.__name__ = "SnmpAdminString"
_H3c3GGsmImsi_Object = MibTableColumn
h3c3GGsmImsi = _H3c3GGsmImsi_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 4, 1, 1, 4),
    _H3c3GGsmImsi_Type()
)
h3c3GGsmImsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GGsmImsi.setStatus("current")


class _H3c3GGsmImei_Type(SnmpAdminString):
    """Custom type h3c3GGsmImei based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3c3GGsmImei_Type.__name__ = "SnmpAdminString"
_H3c3GGsmImei_Object = MibTableColumn
h3c3GGsmImei = _H3c3GGsmImei_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 4, 1, 1, 5),
    _H3c3GGsmImei_Type()
)
h3c3GGsmImei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GGsmImei.setStatus("current")


class _H3c3GGsmApn_Type(SnmpAdminString):
    """Custom type h3c3GGsmApn based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_H3c3GGsmApn_Type.__name__ = "SnmpAdminString"
_H3c3GGsmApn_Object = MibTableColumn
h3c3GGsmApn = _H3c3GGsmApn_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 4, 1, 1, 6),
    _H3c3GGsmApn_Type()
)
h3c3GGsmApn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3c3GGsmApn.setStatus("current")


class _H3c3GGsmPacketSessionStatus_Type(Integer32):
    """Custom type h3c3GGsmPacketSessionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("unknown", 1))
    )


_H3c3GGsmPacketSessionStatus_Type.__name__ = "Integer32"
_H3c3GGsmPacketSessionStatus_Object = MibTableColumn
h3c3GGsmPacketSessionStatus = _H3c3GGsmPacketSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 4, 1, 1, 7),
    _H3c3GGsmPacketSessionStatus_Type()
)
h3c3GGsmPacketSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GGsmPacketSessionStatus.setStatus("current")


class _H3c3GGsmNetworkSelectionMode_Type(Integer32):
    """Custom type h3c3GGsmNetworkSelectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 2),
          ("manual", 3),
          ("unknown", 1))
    )


_H3c3GGsmNetworkSelectionMode_Type.__name__ = "Integer32"
_H3c3GGsmNetworkSelectionMode_Object = MibTableColumn
h3c3GGsmNetworkSelectionMode = _H3c3GGsmNetworkSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 4, 1, 1, 8),
    _H3c3GGsmNetworkSelectionMode_Type()
)
h3c3GGsmNetworkSelectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GGsmNetworkSelectionMode.setStatus("current")


class _H3c3GGsmMobileNetworkName_Type(SnmpAdminString):
    """Custom type h3c3GGsmMobileNetworkName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3c3GGsmMobileNetworkName_Type.__name__ = "SnmpAdminString"
_H3c3GGsmMobileNetworkName_Object = MibTableColumn
h3c3GGsmMobileNetworkName = _H3c3GGsmMobileNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 4, 1, 1, 9),
    _H3c3GGsmMobileNetworkName_Type()
)
h3c3GGsmMobileNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GGsmMobileNetworkName.setStatus("current")


class _H3c3GGsmLac_Type(SnmpAdminString):
    """Custom type h3c3GGsmLac based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3c3GGsmLac_Type.__name__ = "SnmpAdminString"
_H3c3GGsmLac_Object = MibTableColumn
h3c3GGsmLac = _H3c3GGsmLac_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 4, 1, 1, 10),
    _H3c3GGsmLac_Type()
)
h3c3GGsmLac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GGsmLac.setStatus("current")


class _H3c3GGsmCellId_Type(SnmpAdminString):
    """Custom type h3c3GGsmCellId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3c3GGsmCellId_Type.__name__ = "SnmpAdminString"
_H3c3GGsmCellId_Object = MibTableColumn
h3c3GGsmCellId = _H3c3GGsmCellId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 4, 1, 1, 11),
    _H3c3GGsmCellId_Type()
)
h3c3GGsmCellId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GGsmCellId.setStatus("current")


class _H3c3GGsmSimStatus_Type(Integer32):
    """Custom type h3c3GGsmSimStatus based on Integer32"""
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
        *(("blocked", 5),
          ("networkReject", 4),
          ("notInsert", 3),
          ("ok", 2),
          ("unknown", 1))
    )


_H3c3GGsmSimStatus_Type.__name__ = "Integer32"
_H3c3GGsmSimStatus_Object = MibTableColumn
h3c3GGsmSimStatus = _H3c3GGsmSimStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 1, 4, 1, 1, 12),
    _H3c3GGsmSimStatus_Type()
)
h3c3GGsmSimStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c3GGsmSimStatus.setStatus("current")
_H3c3GModemTrap_ObjectIdentity = ObjectIdentity
h3c3GModemTrap = _H3c3GModemTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 2)
)


class _H3cDevSerialNumber_Type(SnmpAdminString):
    """Custom type h3cDevSerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cDevSerialNumber_Type.__name__ = "SnmpAdminString"
_H3cDevSerialNumber_Object = MibScalar
h3cDevSerialNumber = _H3cDevSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 2, 1),
    _H3cDevSerialNumber_Type()
)
h3cDevSerialNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDevSerialNumber.setStatus("current")


class _H3cDeviceOUI_Type(SnmpAdminString):
    """Custom type h3cDeviceOUI based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_H3cDeviceOUI_Type.__name__ = "SnmpAdminString"
_H3cDeviceOUI_Object = MibScalar
h3cDeviceOUI = _H3cDeviceOUI_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 2, 2),
    _H3cDeviceOUI_Type()
)
h3cDeviceOUI.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDeviceOUI.setStatus("current")


class _H3cAccessMedia_Type(Integer32):
    """Custom type h3cAccessMedia based on Integer32"""
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


_H3cAccessMedia_Type.__name__ = "Integer32"
_H3cAccessMedia_Object = MibScalar
h3cAccessMedia = _H3cAccessMedia_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 2, 3),
    _H3cAccessMedia_Type()
)
h3cAccessMedia.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cAccessMedia.setStatus("current")


class _H3c3GCurrentService_Type(Integer32):
    """Custom type h3c3GCurrentService based on Integer32"""
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
        *(("evDo", 3),
          ("gsm", 4),
          ("oneXRtt", 2),
          ("unknown", 1))
    )


_H3c3GCurrentService_Type.__name__ = "Integer32"
_H3c3GCurrentService_Object = MibScalar
h3c3GCurrentService = _H3c3GCurrentService_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 2, 4),
    _H3c3GCurrentService_Type()
)
h3c3GCurrentService.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3c3GCurrentService.setStatus("current")


class _H3c3GCurrentRssiBind_Type(Integer32):
    """Custom type h3c3GCurrentRssiBind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_H3c3GCurrentRssiBind_Type.__name__ = "Integer32"
_H3c3GCurrentRssiBind_Object = MibScalar
h3c3GCurrentRssiBind = _H3c3GCurrentRssiBind_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 2, 5),
    _H3c3GCurrentRssiBind_Type()
)
h3c3GCurrentRssiBind.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3c3GCurrentRssiBind.setStatus("current")
if mibBuilder.loadTexts:
    h3c3GCurrentRssiBind.setUnits("dBm")


class _H3c3GImsiBind_Type(SnmpAdminString):
    """Custom type h3c3GImsiBind based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3c3GImsiBind_Type.__name__ = "SnmpAdminString"
_H3c3GImsiBind_Object = MibScalar
h3c3GImsiBind = _H3c3GImsiBind_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 2, 6),
    _H3c3GImsiBind_Type()
)
h3c3GImsiBind.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3c3GImsiBind.setStatus("current")
_H3c3GModemTraps_ObjectIdentity = ObjectIdentity
h3c3GModemTraps = _H3c3GModemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 3)
)
_H3c3GModemTrapPrefix_ObjectIdentity = ObjectIdentity
h3c3GModemTrapPrefix = _H3c3GModemTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 3, 0)
)

# Managed Objects groups


# Notification objects

h3cWirelessCardInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 3, 0, 1)
)
h3cWirelessCardInserted.setObjects(
      *(("A3COM-HUAWEI-3GMODEM-MIB", "h3cDeviceOUI"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3cDevSerialNumber"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3cWirelessCardSerialNumber"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3cUIMImsi"))
)
if mibBuilder.loadTexts:
    h3cWirelessCardInserted.setStatus(
        "current"
    )

h3cWirelessCardPulledOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 3, 0, 2)
)
h3cWirelessCardPulledOut.setObjects(
      *(("A3COM-HUAWEI-3GMODEM-MIB", "h3cDeviceOUI"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3cDevSerialNumber"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3cWirelessCardSerialNumber"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3cUIMImsi"))
)
if mibBuilder.loadTexts:
    h3cWirelessCardPulledOut.setStatus(
        "current"
    )

h3cUIMPinInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 3, 0, 3)
)
h3cUIMPinInvalid.setObjects(
      *(("A3COM-HUAWEI-3GMODEM-MIB", "h3cDeviceOUI"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3cDevSerialNumber"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3cWirelessCardSerialNumber"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3cUIMImsi"))
)
if mibBuilder.loadTexts:
    h3cUIMPinInvalid.setStatus(
        "current"
    )

h3cUIMPinChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 3, 0, 4)
)
h3cUIMPinChanged.setObjects(
      *(("A3COM-HUAWEI-3GMODEM-MIB", "h3cDeviceOUI"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3cDevSerialNumber"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3cWirelessCardSerialNumber"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3cUIMImsi"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3cUIMOldPin"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3cUIMPin"))
)
if mibBuilder.loadTexts:
    h3cUIMPinChanged.setStatus(
        "current"
    )

h3cAccessMediaChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 3, 0, 5)
)
h3cAccessMediaChanged.setObjects(
      *(("A3COM-HUAWEI-3GMODEM-MIB", "h3cDeviceOUI"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3cDevSerialNumber"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3cWirelessCardSerialNumber"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3cUIMImsi"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3cAccessMedia"))
)
if mibBuilder.loadTexts:
    h3cAccessMediaChanged.setStatus(
        "current"
    )

h3c3GRssiStrongSignalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 3, 0, 6)
)
h3c3GRssiStrongSignalTrap.setObjects(
      *(("A3COM-HUAWEI-3GMODEM-MIB", "h3cWirelessCardIndex"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3cDeviceOUI"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3cDevSerialNumber"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3cWirelessCardSerialNumber"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3c3GCurrentService"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3c3GCurrentRssiBind"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3c3GImsiBind"))
)
if mibBuilder.loadTexts:
    h3c3GRssiStrongSignalTrap.setStatus(
        "current"
    )

h3c3GRssiMediumSignalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 3, 0, 7)
)
h3c3GRssiMediumSignalTrap.setObjects(
      *(("A3COM-HUAWEI-3GMODEM-MIB", "h3cWirelessCardIndex"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3cDeviceOUI"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3cDevSerialNumber"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3cWirelessCardSerialNumber"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3c3GCurrentService"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3c3GCurrentRssiBind"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3c3GImsiBind"))
)
if mibBuilder.loadTexts:
    h3c3GRssiMediumSignalTrap.setStatus(
        "current"
    )

h3c3GRssiWeakSignalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 98, 3, 0, 8)
)
h3c3GRssiWeakSignalTrap.setObjects(
      *(("A3COM-HUAWEI-3GMODEM-MIB", "h3cWirelessCardIndex"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3cDeviceOUI"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3cDevSerialNumber"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3cWirelessCardSerialNumber"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3c3GCurrentService"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3c3GCurrentRssiBind"),
        ("A3COM-HUAWEI-3GMODEM-MIB", "h3c3GImsiBind"))
)
if mibBuilder.loadTexts:
    h3c3GRssiWeakSignalTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-3GMODEM-MIB",
    **{"H3cUIMStatusType": H3cUIMStatusType,
       "h3c3GModem": h3c3GModem,
       "h3c3GModemObjects": h3c3GModemObjects,
       "h3cWirelessCard": h3cWirelessCard,
       "h3cWirelessCardTable": h3cWirelessCardTable,
       "h3cWirelessCardEntry": h3cWirelessCardEntry,
       "h3cWirelessCardIndex": h3cWirelessCardIndex,
       "h3cWirelessCardModelName": h3cWirelessCardModelName,
       "h3cWirelessCardMfgName": h3cWirelessCardMfgName,
       "h3cWirelessCardDescription": h3cWirelessCardDescription,
       "h3cWirelessCardSerialNumber": h3cWirelessCardSerialNumber,
       "h3cWirelessCardCMIIID": h3cWirelessCardCMIIID,
       "h3cWirelessCardHardwareVersion": h3cWirelessCardHardwareVersion,
       "h3cWirelessCardFirmwareVersion": h3cWirelessCardFirmwareVersion,
       "h3cWirelessCardPRLVersion": h3cWirelessCardPRLVersion,
       "h3cWirelessCardInterfaceIndex": h3cWirelessCardInterfaceIndex,
       "h3cWirelessCardModemStatus": h3cWirelessCardModemStatus,
       "h3cWirelessCardCurServiceStatus": h3cWirelessCardCurServiceStatus,
       "h3cWirelessCardCurRoamingStatus": h3cWirelessCardCurRoamingStatus,
       "h3cUIM": h3cUIM,
       "h3cUIMInfoTable": h3cUIMInfoTable,
       "h3cUIMInfoEntry": h3cUIMInfoEntry,
       "h3cUIMIndex": h3cUIMIndex,
       "h3cUIMStatus": h3cUIMStatus,
       "h3cUIMImsi": h3cUIMImsi,
       "h3cUIMPin": h3cUIMPin,
       "h3cUIMVoltage": h3cUIMVoltage,
       "h3cUIMProvider": h3cUIMProvider,
       "h3cUIMSignal": h3cUIMSignal,
       "h3cUIMTryPinPukTimes": h3cUIMTryPinPukTimes,
       "h3cUIMOldPin": h3cUIMOldPin,
       "h3c3GCdma": h3c3GCdma,
       "h3c3GCdma1xRttTable": h3c3GCdma1xRttTable,
       "h3c3GCdma1xRttEntry": h3c3GCdma1xRttEntry,
       "h3c3GCdma1xRttCurrentRssi": h3c3GCdma1xRttCurrentRssi,
       "h3c3GCdma1xRttRssiMediumThreshold": h3c3GCdma1xRttRssiMediumThreshold,
       "h3c3GCdma1xRttRssiWeakThreshold": h3c3GCdma1xRttRssiWeakThreshold,
       "h3c3GCdmaEvDoTable": h3c3GCdmaEvDoTable,
       "h3c3GCdmaEvDoEntry": h3c3GCdmaEvDoEntry,
       "h3c3GCdmaEvDoCurrentRssi": h3c3GCdmaEvDoCurrentRssi,
       "h3c3GCdmaEvDoRssiMediumThreshold": h3c3GCdmaEvDoRssiMediumThreshold,
       "h3c3GCdmaEvDoRssiWeakThreshold": h3c3GCdmaEvDoRssiWeakThreshold,
       "h3c3GGsm": h3c3GGsm,
       "h3c3GGsmInfoTable": h3c3GGsmInfoTable,
       "h3c3GGsmInfoEntry": h3c3GGsmInfoEntry,
       "h3c3GGsmCurrentRssi": h3c3GGsmCurrentRssi,
       "h3c3GGsmRssiMediumThreshold": h3c3GGsmRssiMediumThreshold,
       "h3c3GGsmRssiWeakThreshold": h3c3GGsmRssiWeakThreshold,
       "h3c3GGsmImsi": h3c3GGsmImsi,
       "h3c3GGsmImei": h3c3GGsmImei,
       "h3c3GGsmApn": h3c3GGsmApn,
       "h3c3GGsmPacketSessionStatus": h3c3GGsmPacketSessionStatus,
       "h3c3GGsmNetworkSelectionMode": h3c3GGsmNetworkSelectionMode,
       "h3c3GGsmMobileNetworkName": h3c3GGsmMobileNetworkName,
       "h3c3GGsmLac": h3c3GGsmLac,
       "h3c3GGsmCellId": h3c3GGsmCellId,
       "h3c3GGsmSimStatus": h3c3GGsmSimStatus,
       "h3c3GModemTrap": h3c3GModemTrap,
       "h3cDevSerialNumber": h3cDevSerialNumber,
       "h3cDeviceOUI": h3cDeviceOUI,
       "h3cAccessMedia": h3cAccessMedia,
       "h3c3GCurrentService": h3c3GCurrentService,
       "h3c3GCurrentRssiBind": h3c3GCurrentRssiBind,
       "h3c3GImsiBind": h3c3GImsiBind,
       "h3c3GModemTraps": h3c3GModemTraps,
       "h3c3GModemTrapPrefix": h3c3GModemTrapPrefix,
       "h3cWirelessCardInserted": h3cWirelessCardInserted,
       "h3cWirelessCardPulledOut": h3cWirelessCardPulledOut,
       "h3cUIMPinInvalid": h3cUIMPinInvalid,
       "h3cUIMPinChanged": h3cUIMPinChanged,
       "h3cAccessMediaChanged": h3cAccessMediaChanged,
       "h3c3GRssiStrongSignalTrap": h3c3GRssiStrongSignalTrap,
       "h3c3GRssiMediumSignalTrap": h3c3GRssiMediumSignalTrap,
       "h3c3GRssiWeakSignalTrap": h3c3GRssiWeakSignalTrap}
)
