# SNMP MIB module (HPN-ICF-3GMODEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-3GMODEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:22 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpnicf3GModem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98)
)
hpnicf3GModem.setRevisions(
        ("2009-04-30 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfUIMStatusType(Integer32, TextualConvention):
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



class HpnicfSmsEncodeType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("ucs2", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Hpnicf3GModemObjects_ObjectIdentity = ObjectIdentity
hpnicf3GModemObjects = _Hpnicf3GModemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1)
)
_HpnicfWirelessCard_ObjectIdentity = ObjectIdentity
hpnicfWirelessCard = _HpnicfWirelessCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1)
)
_HpnicfWirelessCardTable_Object = MibTable
hpnicfWirelessCardTable = _HpnicfWirelessCardTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfWirelessCardTable.setStatus("current")
_HpnicfWirelessCardEntry_Object = MibTableRow
hpnicfWirelessCardEntry = _HpnicfWirelessCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1, 1, 1)
)
hpnicfWirelessCardEntry.setIndexNames(
    (0, "HPN-ICF-3GMODEM-MIB", "hpnicfWirelessCardIndex"),
)
if mibBuilder.loadTexts:
    hpnicfWirelessCardEntry.setStatus("current")


class _HpnicfWirelessCardIndex_Type(Integer32):
    """Custom type hpnicfWirelessCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfWirelessCardIndex_Type.__name__ = "Integer32"
_HpnicfWirelessCardIndex_Object = MibTableColumn
hpnicfWirelessCardIndex = _HpnicfWirelessCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1, 1, 1, 1),
    _HpnicfWirelessCardIndex_Type()
)
hpnicfWirelessCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWirelessCardIndex.setStatus("current")


class _HpnicfWirelessCardModelName_Type(SnmpAdminString):
    """Custom type hpnicfWirelessCardModelName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfWirelessCardModelName_Type.__name__ = "SnmpAdminString"
_HpnicfWirelessCardModelName_Object = MibTableColumn
hpnicfWirelessCardModelName = _HpnicfWirelessCardModelName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1, 1, 1, 2),
    _HpnicfWirelessCardModelName_Type()
)
hpnicfWirelessCardModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWirelessCardModelName.setStatus("current")


class _HpnicfWirelessCardMfgName_Type(SnmpAdminString):
    """Custom type hpnicfWirelessCardMfgName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfWirelessCardMfgName_Type.__name__ = "SnmpAdminString"
_HpnicfWirelessCardMfgName_Object = MibTableColumn
hpnicfWirelessCardMfgName = _HpnicfWirelessCardMfgName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1, 1, 1, 3),
    _HpnicfWirelessCardMfgName_Type()
)
hpnicfWirelessCardMfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWirelessCardMfgName.setStatus("current")


class _HpnicfWirelessCardDescription_Type(SnmpAdminString):
    """Custom type hpnicfWirelessCardDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfWirelessCardDescription_Type.__name__ = "SnmpAdminString"
_HpnicfWirelessCardDescription_Object = MibTableColumn
hpnicfWirelessCardDescription = _HpnicfWirelessCardDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1, 1, 1, 4),
    _HpnicfWirelessCardDescription_Type()
)
hpnicfWirelessCardDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWirelessCardDescription.setStatus("current")


class _HpnicfWirelessCardSerialNumber_Type(SnmpAdminString):
    """Custom type hpnicfWirelessCardSerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfWirelessCardSerialNumber_Type.__name__ = "SnmpAdminString"
_HpnicfWirelessCardSerialNumber_Object = MibTableColumn
hpnicfWirelessCardSerialNumber = _HpnicfWirelessCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1, 1, 1, 5),
    _HpnicfWirelessCardSerialNumber_Type()
)
hpnicfWirelessCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWirelessCardSerialNumber.setStatus("current")


class _HpnicfWirelessCardCMIIID_Type(SnmpAdminString):
    """Custom type hpnicfWirelessCardCMIIID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfWirelessCardCMIIID_Type.__name__ = "SnmpAdminString"
_HpnicfWirelessCardCMIIID_Object = MibTableColumn
hpnicfWirelessCardCMIIID = _HpnicfWirelessCardCMIIID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1, 1, 1, 6),
    _HpnicfWirelessCardCMIIID_Type()
)
hpnicfWirelessCardCMIIID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWirelessCardCMIIID.setStatus("current")


class _HpnicfWirelessCardHardwareVersion_Type(SnmpAdminString):
    """Custom type hpnicfWirelessCardHardwareVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfWirelessCardHardwareVersion_Type.__name__ = "SnmpAdminString"
_HpnicfWirelessCardHardwareVersion_Object = MibTableColumn
hpnicfWirelessCardHardwareVersion = _HpnicfWirelessCardHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1, 1, 1, 7),
    _HpnicfWirelessCardHardwareVersion_Type()
)
hpnicfWirelessCardHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWirelessCardHardwareVersion.setStatus("current")


class _HpnicfWirelessCardFirmwareVersion_Type(SnmpAdminString):
    """Custom type hpnicfWirelessCardFirmwareVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfWirelessCardFirmwareVersion_Type.__name__ = "SnmpAdminString"
_HpnicfWirelessCardFirmwareVersion_Object = MibTableColumn
hpnicfWirelessCardFirmwareVersion = _HpnicfWirelessCardFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1, 1, 1, 8),
    _HpnicfWirelessCardFirmwareVersion_Type()
)
hpnicfWirelessCardFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWirelessCardFirmwareVersion.setStatus("current")


class _HpnicfWirelessCardPRLVersion_Type(SnmpAdminString):
    """Custom type hpnicfWirelessCardPRLVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfWirelessCardPRLVersion_Type.__name__ = "SnmpAdminString"
_HpnicfWirelessCardPRLVersion_Object = MibTableColumn
hpnicfWirelessCardPRLVersion = _HpnicfWirelessCardPRLVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1, 1, 1, 9),
    _HpnicfWirelessCardPRLVersion_Type()
)
hpnicfWirelessCardPRLVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWirelessCardPRLVersion.setStatus("current")
_HpnicfWirelessCardInterfaceIndex_Type = InterfaceIndex
_HpnicfWirelessCardInterfaceIndex_Object = MibTableColumn
hpnicfWirelessCardInterfaceIndex = _HpnicfWirelessCardInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1, 1, 1, 10),
    _HpnicfWirelessCardInterfaceIndex_Type()
)
hpnicfWirelessCardInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWirelessCardInterfaceIndex.setStatus("current")


class _HpnicfWirelessCardModemStatus_Type(Integer32):
    """Custom type hpnicfWirelessCardModemStatus based on Integer32"""
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


_HpnicfWirelessCardModemStatus_Type.__name__ = "Integer32"
_HpnicfWirelessCardModemStatus_Object = MibTableColumn
hpnicfWirelessCardModemStatus = _HpnicfWirelessCardModemStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1, 1, 1, 11),
    _HpnicfWirelessCardModemStatus_Type()
)
hpnicfWirelessCardModemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWirelessCardModemStatus.setStatus("current")


class _HpnicfWirelessCardModemMode_Type(Integer32):
    """Custom type hpnicfWirelessCardModemMode based on Integer32"""
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
        *(("cdma", 4),
          ("tdscdma", 2),
          ("unknown", 1),
          ("wcdma", 3))
    )


_HpnicfWirelessCardModemMode_Type.__name__ = "Integer32"
_HpnicfWirelessCardModemMode_Object = MibTableColumn
hpnicfWirelessCardModemMode = _HpnicfWirelessCardModemMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1, 1, 1, 12),
    _HpnicfWirelessCardModemMode_Type()
)
hpnicfWirelessCardModemMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWirelessCardModemMode.setStatus("current")


class _HpnicfWirelessCardCurNetConn_Type(Integer32):
    """Custom type hpnicfWirelessCardCurNetConn based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("dchspaPlus", 11),
          ("edge", 5),
          ("evdo", 14),
          ("gprs", 4),
          ("gsm", 3),
          ("hsdpa", 6),
          ("hspaPlus", 9),
          ("hsupa", 7),
          ("hsupaAndhsdpa", 8),
          ("lte", 12),
          ("noService", 2),
          ("onexrtt", 13),
          ("onexrttAndevdo", 15),
          ("tdscdma", 16),
          ("umts", 10),
          ("unknown", 1))
    )


_HpnicfWirelessCardCurNetConn_Type.__name__ = "Integer32"
_HpnicfWirelessCardCurNetConn_Object = MibTableColumn
hpnicfWirelessCardCurNetConn = _HpnicfWirelessCardCurNetConn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1, 1, 1, 13),
    _HpnicfWirelessCardCurNetConn_Type()
)
hpnicfWirelessCardCurNetConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWirelessCardCurNetConn.setStatus("current")
_HpnicfSmsGroup_ObjectIdentity = ObjectIdentity
hpnicfSmsGroup = _HpnicfSmsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1, 2)
)
_HpnicfSmsScalarObjects_ObjectIdentity = ObjectIdentity
hpnicfSmsScalarObjects = _HpnicfSmsScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1, 2, 1)
)
_HpnicfSmsRxNotifSwitch_Type = TruthValue
_HpnicfSmsRxNotifSwitch_Object = MibScalar
hpnicfSmsRxNotifSwitch = _HpnicfSmsRxNotifSwitch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1, 2, 1, 1),
    _HpnicfSmsRxNotifSwitch_Type()
)
hpnicfSmsRxNotifSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSmsRxNotifSwitch.setStatus("current")
_HpnicfSmsOperationTable_Object = MibTable
hpnicfSmsOperationTable = _HpnicfSmsOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfSmsOperationTable.setStatus("current")
_HpnicfSmsOperationEntry_Object = MibTableRow
hpnicfSmsOperationEntry = _HpnicfSmsOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1, 2, 2, 1)
)
hpnicfSmsOperationEntry.setIndexNames(
    (0, "HPN-ICF-3GMODEM-MIB", "hpnicfWirelessCardIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSmsOperationEntry.setStatus("current")


class _HpnicfSmsDestNumber_Type(SnmpAdminString):
    """Custom type hpnicfSmsDestNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HpnicfSmsDestNumber_Type.__name__ = "SnmpAdminString"
_HpnicfSmsDestNumber_Object = MibTableColumn
hpnicfSmsDestNumber = _HpnicfSmsDestNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1, 2, 2, 1, 1),
    _HpnicfSmsDestNumber_Type()
)
hpnicfSmsDestNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSmsDestNumber.setStatus("current")


class _HpnicfSmsEncode_Type(HpnicfSmsEncodeType):
    """Custom type hpnicfSmsEncode based on HpnicfSmsEncodeType"""
    defaultValue = 1


_HpnicfSmsEncode_Object = MibTableColumn
hpnicfSmsEncode = _HpnicfSmsEncode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1, 2, 2, 1, 2),
    _HpnicfSmsEncode_Type()
)
hpnicfSmsEncode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSmsEncode.setStatus("current")


class _HpnicfSmsContent_Type(OctetString):
    """Custom type hpnicfSmsContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfSmsContent_Type.__name__ = "OctetString"
_HpnicfSmsContent_Object = MibTableColumn
hpnicfSmsContent = _HpnicfSmsContent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1, 2, 2, 1, 3),
    _HpnicfSmsContent_Type()
)
hpnicfSmsContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSmsContent.setStatus("current")


class _HpnicfSmsSendStatus_Type(Integer32):
    """Custom type hpnicfSmsSendStatus based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("busy", 10),
          ("codeError", 8),
          ("contentTooLong", 7),
          ("initializing", 13),
          ("noCenterNum", 14),
          ("noSim", 15),
          ("notPresent", 11),
          ("notSupport", 12),
          ("paramInvalid", 6),
          ("ready2Send", 2),
          ("sendAtFailed", 17),
          ("sendDisable", 18),
          ("sending", 3),
          ("sentAlready", 4),
          ("set2Send", 1),
          ("simNotReady", 16),
          ("telnumberInvalid", 5),
          ("unknown", 9))
    )


_HpnicfSmsSendStatus_Type.__name__ = "Integer32"
_HpnicfSmsSendStatus_Object = MibTableColumn
hpnicfSmsSendStatus = _HpnicfSmsSendStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1, 2, 2, 1, 4),
    _HpnicfSmsSendStatus_Type()
)
hpnicfSmsSendStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSmsSendStatus.setStatus("current")
_HpnicfWirelessCardOnlineTable_Object = MibTable
hpnicfWirelessCardOnlineTable = _HpnicfWirelessCardOnlineTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfWirelessCardOnlineTable.setStatus("current")
_HpnicfWirelessCardOnlineEntry_Object = MibTableRow
hpnicfWirelessCardOnlineEntry = _HpnicfWirelessCardOnlineEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1, 3, 1)
)
hpnicfWirelessCardOnlineEntry.setIndexNames(
    (0, "HPN-ICF-3GMODEM-MIB", "hpnicfWirelessCardIndex"),
    (0, "HPN-ICF-3GMODEM-MIB", "hpnicfWirelessCardOnlineTime"),
)
if mibBuilder.loadTexts:
    hpnicfWirelessCardOnlineEntry.setStatus("current")
_HpnicfWirelessCardOnlineTime_Type = Unsigned32
_HpnicfWirelessCardOnlineTime_Object = MibTableColumn
hpnicfWirelessCardOnlineTime = _HpnicfWirelessCardOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1, 3, 1, 1),
    _HpnicfWirelessCardOnlineTime_Type()
)
hpnicfWirelessCardOnlineTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfWirelessCardOnlineTime.setStatus("current")


class _HpnicfWirelessCardOnlineType_Type(Integer32):
    """Custom type hpnicfWirelessCardOnlineType based on Integer32"""
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


_HpnicfWirelessCardOnlineType_Type.__name__ = "Integer32"
_HpnicfWirelessCardOnlineType_Object = MibTableColumn
hpnicfWirelessCardOnlineType = _HpnicfWirelessCardOnlineType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 1, 3, 1, 2),
    _HpnicfWirelessCardOnlineType_Type()
)
hpnicfWirelessCardOnlineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWirelessCardOnlineType.setStatus("current")
_HpnicfUIM_ObjectIdentity = ObjectIdentity
hpnicfUIM = _HpnicfUIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 2)
)
_HpnicfUIMInfoTable_Object = MibTable
hpnicfUIMInfoTable = _HpnicfUIMInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfUIMInfoTable.setStatus("current")
_HpnicfUIMInfoEntry_Object = MibTableRow
hpnicfUIMInfoEntry = _HpnicfUIMInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 2, 1, 1)
)
hpnicfUIMInfoEntry.setIndexNames(
    (0, "HPN-ICF-3GMODEM-MIB", "hpnicfWirelessCardIndex"),
    (0, "HPN-ICF-3GMODEM-MIB", "hpnicfUIMIndex"),
)
if mibBuilder.loadTexts:
    hpnicfUIMInfoEntry.setStatus("current")


class _HpnicfUIMIndex_Type(Integer32):
    """Custom type hpnicfUIMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfUIMIndex_Type.__name__ = "Integer32"
_HpnicfUIMIndex_Object = MibTableColumn
hpnicfUIMIndex = _HpnicfUIMIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 2, 1, 1, 1),
    _HpnicfUIMIndex_Type()
)
hpnicfUIMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfUIMIndex.setStatus("current")
_HpnicfUIMStatus_Type = HpnicfUIMStatusType
_HpnicfUIMStatus_Object = MibTableColumn
hpnicfUIMStatus = _HpnicfUIMStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 2, 1, 1, 2),
    _HpnicfUIMStatus_Type()
)
hpnicfUIMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUIMStatus.setStatus("current")


class _HpnicfUIMImsi_Type(SnmpAdminString):
    """Custom type hpnicfUIMImsi based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfUIMImsi_Type.__name__ = "SnmpAdminString"
_HpnicfUIMImsi_Object = MibTableColumn
hpnicfUIMImsi = _HpnicfUIMImsi_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 2, 1, 1, 3),
    _HpnicfUIMImsi_Type()
)
hpnicfUIMImsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUIMImsi.setStatus("current")


class _HpnicfUIMPin_Type(SnmpAdminString):
    """Custom type hpnicfUIMPin based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_HpnicfUIMPin_Type.__name__ = "SnmpAdminString"
_HpnicfUIMPin_Object = MibTableColumn
hpnicfUIMPin = _HpnicfUIMPin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 2, 1, 1, 4),
    _HpnicfUIMPin_Type()
)
hpnicfUIMPin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUIMPin.setStatus("current")


class _HpnicfUIMVoltage_Type(Unsigned32):
    """Custom type hpnicfUIMVoltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpnicfUIMVoltage_Type.__name__ = "Unsigned32"
_HpnicfUIMVoltage_Object = MibTableColumn
hpnicfUIMVoltage = _HpnicfUIMVoltage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 2, 1, 1, 5),
    _HpnicfUIMVoltage_Type()
)
hpnicfUIMVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUIMVoltage.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfUIMVoltage.setUnits("milli-volt")


class _HpnicfUIMProvider_Type(SnmpAdminString):
    """Custom type hpnicfUIMProvider based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfUIMProvider_Type.__name__ = "SnmpAdminString"
_HpnicfUIMProvider_Object = MibTableColumn
hpnicfUIMProvider = _HpnicfUIMProvider_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 2, 1, 1, 6),
    _HpnicfUIMProvider_Type()
)
hpnicfUIMProvider.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUIMProvider.setStatus("current")


class _HpnicfUIMSignal_Type(Integer32):
    """Custom type hpnicfUIMSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
        ValueRangeConstraint(99, 99),
    )


_HpnicfUIMSignal_Type.__name__ = "Integer32"
_HpnicfUIMSignal_Object = MibTableColumn
hpnicfUIMSignal = _HpnicfUIMSignal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 2, 1, 1, 7),
    _HpnicfUIMSignal_Type()
)
hpnicfUIMSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUIMSignal.setStatus("current")


class _HpnicfUIMTryPinPukTimes_Type(Unsigned32):
    """Custom type hpnicfUIMTryPinPukTimes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpnicfUIMTryPinPukTimes_Type.__name__ = "Unsigned32"
_HpnicfUIMTryPinPukTimes_Object = MibTableColumn
hpnicfUIMTryPinPukTimes = _HpnicfUIMTryPinPukTimes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 2, 1, 1, 8),
    _HpnicfUIMTryPinPukTimes_Type()
)
hpnicfUIMTryPinPukTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfUIMTryPinPukTimes.setStatus("current")


class _HpnicfUIMOldPin_Type(SnmpAdminString):
    """Custom type hpnicfUIMOldPin based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_HpnicfUIMOldPin_Type.__name__ = "SnmpAdminString"
_HpnicfUIMOldPin_Object = MibTableColumn
hpnicfUIMOldPin = _HpnicfUIMOldPin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 2, 1, 1, 9),
    _HpnicfUIMOldPin_Type()
)
hpnicfUIMOldPin.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfUIMOldPin.setStatus("current")
_Hpnicf3GCdma_ObjectIdentity = ObjectIdentity
hpnicf3GCdma = _Hpnicf3GCdma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 3)
)
_Hpnicf3GCdma1xRttTable_Object = MibTable
hpnicf3GCdma1xRttTable = _Hpnicf3GCdma1xRttTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpnicf3GCdma1xRttTable.setStatus("current")
_Hpnicf3GCdma1xRttEntry_Object = MibTableRow
hpnicf3GCdma1xRttEntry = _Hpnicf3GCdma1xRttEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 3, 1, 1)
)
hpnicf3GCdma1xRttEntry.setIndexNames(
    (0, "HPN-ICF-3GMODEM-MIB", "hpnicfWirelessCardIndex"),
)
if mibBuilder.loadTexts:
    hpnicf3GCdma1xRttEntry.setStatus("current")


class _Hpnicf3GCdma1xRttCurrentRssi_Type(Integer32):
    """Custom type hpnicf3GCdma1xRttCurrentRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, -2147483648),
        ValueRangeConstraint(-150, 0),
    )


_Hpnicf3GCdma1xRttCurrentRssi_Type.__name__ = "Integer32"
_Hpnicf3GCdma1xRttCurrentRssi_Object = MibTableColumn
hpnicf3GCdma1xRttCurrentRssi = _Hpnicf3GCdma1xRttCurrentRssi_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 3, 1, 1, 1),
    _Hpnicf3GCdma1xRttCurrentRssi_Type()
)
hpnicf3GCdma1xRttCurrentRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicf3GCdma1xRttCurrentRssi.setStatus("current")
if mibBuilder.loadTexts:
    hpnicf3GCdma1xRttCurrentRssi.setUnits("dBm")


class _Hpnicf3GCdma1xRttRssiMediumThreshold_Type(Integer32):
    """Custom type hpnicf3GCdma1xRttRssiMediumThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_Hpnicf3GCdma1xRttRssiMediumThreshold_Type.__name__ = "Integer32"
_Hpnicf3GCdma1xRttRssiMediumThreshold_Object = MibTableColumn
hpnicf3GCdma1xRttRssiMediumThreshold = _Hpnicf3GCdma1xRttRssiMediumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 3, 1, 1, 2),
    _Hpnicf3GCdma1xRttRssiMediumThreshold_Type()
)
hpnicf3GCdma1xRttRssiMediumThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicf3GCdma1xRttRssiMediumThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hpnicf3GCdma1xRttRssiMediumThreshold.setUnits("dBm")


class _Hpnicf3GCdma1xRttRssiWeakThreshold_Type(Integer32):
    """Custom type hpnicf3GCdma1xRttRssiWeakThreshold based on Integer32"""
    defaultValue = -150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_Hpnicf3GCdma1xRttRssiWeakThreshold_Type.__name__ = "Integer32"
_Hpnicf3GCdma1xRttRssiWeakThreshold_Object = MibTableColumn
hpnicf3GCdma1xRttRssiWeakThreshold = _Hpnicf3GCdma1xRttRssiWeakThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 3, 1, 1, 3),
    _Hpnicf3GCdma1xRttRssiWeakThreshold_Type()
)
hpnicf3GCdma1xRttRssiWeakThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicf3GCdma1xRttRssiWeakThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hpnicf3GCdma1xRttRssiWeakThreshold.setUnits("dBm")


class _Hpnicf3GCdma1xRttCurServiceStatus_Type(Integer32):
    """Custom type hpnicf3GCdma1xRttCurServiceStatus based on Integer32"""
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


_Hpnicf3GCdma1xRttCurServiceStatus_Type.__name__ = "Integer32"
_Hpnicf3GCdma1xRttCurServiceStatus_Object = MibTableColumn
hpnicf3GCdma1xRttCurServiceStatus = _Hpnicf3GCdma1xRttCurServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 3, 1, 1, 4),
    _Hpnicf3GCdma1xRttCurServiceStatus_Type()
)
hpnicf3GCdma1xRttCurServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicf3GCdma1xRttCurServiceStatus.setStatus("current")


class _Hpnicf3GCdma1xRttCurRoamingStatus_Type(Integer32):
    """Custom type hpnicf3GCdma1xRttCurRoamingStatus based on Integer32"""
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


_Hpnicf3GCdma1xRttCurRoamingStatus_Type.__name__ = "Integer32"
_Hpnicf3GCdma1xRttCurRoamingStatus_Object = MibTableColumn
hpnicf3GCdma1xRttCurRoamingStatus = _Hpnicf3GCdma1xRttCurRoamingStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 3, 1, 1, 5),
    _Hpnicf3GCdma1xRttCurRoamingStatus_Type()
)
hpnicf3GCdma1xRttCurRoamingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicf3GCdma1xRttCurRoamingStatus.setStatus("current")
_Hpnicf3GCdmaEvDoTable_Object = MibTable
hpnicf3GCdmaEvDoTable = _Hpnicf3GCdmaEvDoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hpnicf3GCdmaEvDoTable.setStatus("current")
_Hpnicf3GCdmaEvDoEntry_Object = MibTableRow
hpnicf3GCdmaEvDoEntry = _Hpnicf3GCdmaEvDoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 3, 2, 1)
)
hpnicf3GCdmaEvDoEntry.setIndexNames(
    (0, "HPN-ICF-3GMODEM-MIB", "hpnicfWirelessCardIndex"),
)
if mibBuilder.loadTexts:
    hpnicf3GCdmaEvDoEntry.setStatus("current")


class _Hpnicf3GCdmaEvDoCurrentRssi_Type(Integer32):
    """Custom type hpnicf3GCdmaEvDoCurrentRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, -2147483648),
        ValueRangeConstraint(-150, 0),
    )


_Hpnicf3GCdmaEvDoCurrentRssi_Type.__name__ = "Integer32"
_Hpnicf3GCdmaEvDoCurrentRssi_Object = MibTableColumn
hpnicf3GCdmaEvDoCurrentRssi = _Hpnicf3GCdmaEvDoCurrentRssi_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 3, 2, 1, 1),
    _Hpnicf3GCdmaEvDoCurrentRssi_Type()
)
hpnicf3GCdmaEvDoCurrentRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicf3GCdmaEvDoCurrentRssi.setStatus("current")
if mibBuilder.loadTexts:
    hpnicf3GCdmaEvDoCurrentRssi.setUnits("dBm")


class _Hpnicf3GCdmaEvDoRssiMediumThreshold_Type(Integer32):
    """Custom type hpnicf3GCdmaEvDoRssiMediumThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_Hpnicf3GCdmaEvDoRssiMediumThreshold_Type.__name__ = "Integer32"
_Hpnicf3GCdmaEvDoRssiMediumThreshold_Object = MibTableColumn
hpnicf3GCdmaEvDoRssiMediumThreshold = _Hpnicf3GCdmaEvDoRssiMediumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 3, 2, 1, 2),
    _Hpnicf3GCdmaEvDoRssiMediumThreshold_Type()
)
hpnicf3GCdmaEvDoRssiMediumThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicf3GCdmaEvDoRssiMediumThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hpnicf3GCdmaEvDoRssiMediumThreshold.setUnits("dBm")


class _Hpnicf3GCdmaEvDoRssiWeakThreshold_Type(Integer32):
    """Custom type hpnicf3GCdmaEvDoRssiWeakThreshold based on Integer32"""
    defaultValue = -150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_Hpnicf3GCdmaEvDoRssiWeakThreshold_Type.__name__ = "Integer32"
_Hpnicf3GCdmaEvDoRssiWeakThreshold_Object = MibTableColumn
hpnicf3GCdmaEvDoRssiWeakThreshold = _Hpnicf3GCdmaEvDoRssiWeakThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 3, 2, 1, 3),
    _Hpnicf3GCdmaEvDoRssiWeakThreshold_Type()
)
hpnicf3GCdmaEvDoRssiWeakThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicf3GCdmaEvDoRssiWeakThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hpnicf3GCdmaEvDoRssiWeakThreshold.setUnits("dBm")


class _Hpnicf3GCdmaEvDoCurServiceStatus_Type(Integer32):
    """Custom type hpnicf3GCdmaEvDoCurServiceStatus based on Integer32"""
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


_Hpnicf3GCdmaEvDoCurServiceStatus_Type.__name__ = "Integer32"
_Hpnicf3GCdmaEvDoCurServiceStatus_Object = MibTableColumn
hpnicf3GCdmaEvDoCurServiceStatus = _Hpnicf3GCdmaEvDoCurServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 3, 2, 1, 4),
    _Hpnicf3GCdmaEvDoCurServiceStatus_Type()
)
hpnicf3GCdmaEvDoCurServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicf3GCdmaEvDoCurServiceStatus.setStatus("current")


class _Hpnicf3GCdmaEvDoCurRoamingStatus_Type(Integer32):
    """Custom type hpnicf3GCdmaEvDoCurRoamingStatus based on Integer32"""
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


_Hpnicf3GCdmaEvDoCurRoamingStatus_Type.__name__ = "Integer32"
_Hpnicf3GCdmaEvDoCurRoamingStatus_Object = MibTableColumn
hpnicf3GCdmaEvDoCurRoamingStatus = _Hpnicf3GCdmaEvDoCurRoamingStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 3, 2, 1, 5),
    _Hpnicf3GCdmaEvDoCurRoamingStatus_Type()
)
hpnicf3GCdmaEvDoCurRoamingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicf3GCdmaEvDoCurRoamingStatus.setStatus("current")
_Hpnicf3GGsm_ObjectIdentity = ObjectIdentity
hpnicf3GGsm = _Hpnicf3GGsm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 4)
)
_Hpnicf3GGsmInfoTable_Object = MibTable
hpnicf3GGsmInfoTable = _Hpnicf3GGsmInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hpnicf3GGsmInfoTable.setStatus("current")
_Hpnicf3GGsmInfoEntry_Object = MibTableRow
hpnicf3GGsmInfoEntry = _Hpnicf3GGsmInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 4, 1, 1)
)
hpnicf3GGsmInfoEntry.setIndexNames(
    (0, "HPN-ICF-3GMODEM-MIB", "hpnicfWirelessCardIndex"),
)
if mibBuilder.loadTexts:
    hpnicf3GGsmInfoEntry.setStatus("current")


class _Hpnicf3GGsmCurrentRssi_Type(Integer32):
    """Custom type hpnicf3GGsmCurrentRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, -2147483648),
        ValueRangeConstraint(-150, 0),
    )


_Hpnicf3GGsmCurrentRssi_Type.__name__ = "Integer32"
_Hpnicf3GGsmCurrentRssi_Object = MibTableColumn
hpnicf3GGsmCurrentRssi = _Hpnicf3GGsmCurrentRssi_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 4, 1, 1, 1),
    _Hpnicf3GGsmCurrentRssi_Type()
)
hpnicf3GGsmCurrentRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicf3GGsmCurrentRssi.setStatus("current")
if mibBuilder.loadTexts:
    hpnicf3GGsmCurrentRssi.setUnits("dBm")


class _Hpnicf3GGsmRssiMediumThreshold_Type(Integer32):
    """Custom type hpnicf3GGsmRssiMediumThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_Hpnicf3GGsmRssiMediumThreshold_Type.__name__ = "Integer32"
_Hpnicf3GGsmRssiMediumThreshold_Object = MibTableColumn
hpnicf3GGsmRssiMediumThreshold = _Hpnicf3GGsmRssiMediumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 4, 1, 1, 2),
    _Hpnicf3GGsmRssiMediumThreshold_Type()
)
hpnicf3GGsmRssiMediumThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicf3GGsmRssiMediumThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hpnicf3GGsmRssiMediumThreshold.setUnits("dBm")


class _Hpnicf3GGsmRssiWeakThreshold_Type(Integer32):
    """Custom type hpnicf3GGsmRssiWeakThreshold based on Integer32"""
    defaultValue = -150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_Hpnicf3GGsmRssiWeakThreshold_Type.__name__ = "Integer32"
_Hpnicf3GGsmRssiWeakThreshold_Object = MibTableColumn
hpnicf3GGsmRssiWeakThreshold = _Hpnicf3GGsmRssiWeakThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 4, 1, 1, 3),
    _Hpnicf3GGsmRssiWeakThreshold_Type()
)
hpnicf3GGsmRssiWeakThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicf3GGsmRssiWeakThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hpnicf3GGsmRssiWeakThreshold.setUnits("dBm")


class _Hpnicf3GGsmImsi_Type(SnmpAdminString):
    """Custom type hpnicf3GGsmImsi based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hpnicf3GGsmImsi_Type.__name__ = "SnmpAdminString"
_Hpnicf3GGsmImsi_Object = MibTableColumn
hpnicf3GGsmImsi = _Hpnicf3GGsmImsi_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 4, 1, 1, 4),
    _Hpnicf3GGsmImsi_Type()
)
hpnicf3GGsmImsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicf3GGsmImsi.setStatus("current")


class _Hpnicf3GGsmImei_Type(SnmpAdminString):
    """Custom type hpnicf3GGsmImei based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hpnicf3GGsmImei_Type.__name__ = "SnmpAdminString"
_Hpnicf3GGsmImei_Object = MibTableColumn
hpnicf3GGsmImei = _Hpnicf3GGsmImei_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 4, 1, 1, 5),
    _Hpnicf3GGsmImei_Type()
)
hpnicf3GGsmImei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicf3GGsmImei.setStatus("current")


class _Hpnicf3GGsmApn_Type(SnmpAdminString):
    """Custom type hpnicf3GGsmApn based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_Hpnicf3GGsmApn_Type.__name__ = "SnmpAdminString"
_Hpnicf3GGsmApn_Object = MibTableColumn
hpnicf3GGsmApn = _Hpnicf3GGsmApn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 4, 1, 1, 6),
    _Hpnicf3GGsmApn_Type()
)
hpnicf3GGsmApn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicf3GGsmApn.setStatus("current")


class _Hpnicf3GGsmPacketSessionStatus_Type(Integer32):
    """Custom type hpnicf3GGsmPacketSessionStatus based on Integer32"""
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


_Hpnicf3GGsmPacketSessionStatus_Type.__name__ = "Integer32"
_Hpnicf3GGsmPacketSessionStatus_Object = MibTableColumn
hpnicf3GGsmPacketSessionStatus = _Hpnicf3GGsmPacketSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 4, 1, 1, 7),
    _Hpnicf3GGsmPacketSessionStatus_Type()
)
hpnicf3GGsmPacketSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicf3GGsmPacketSessionStatus.setStatus("current")


class _Hpnicf3GGsmNetworkSelectionMode_Type(Integer32):
    """Custom type hpnicf3GGsmNetworkSelectionMode based on Integer32"""
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


_Hpnicf3GGsmNetworkSelectionMode_Type.__name__ = "Integer32"
_Hpnicf3GGsmNetworkSelectionMode_Object = MibTableColumn
hpnicf3GGsmNetworkSelectionMode = _Hpnicf3GGsmNetworkSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 4, 1, 1, 8),
    _Hpnicf3GGsmNetworkSelectionMode_Type()
)
hpnicf3GGsmNetworkSelectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicf3GGsmNetworkSelectionMode.setStatus("current")


class _Hpnicf3GGsmMobileNetworkName_Type(SnmpAdminString):
    """Custom type hpnicf3GGsmMobileNetworkName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hpnicf3GGsmMobileNetworkName_Type.__name__ = "SnmpAdminString"
_Hpnicf3GGsmMobileNetworkName_Object = MibTableColumn
hpnicf3GGsmMobileNetworkName = _Hpnicf3GGsmMobileNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 4, 1, 1, 9),
    _Hpnicf3GGsmMobileNetworkName_Type()
)
hpnicf3GGsmMobileNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicf3GGsmMobileNetworkName.setStatus("current")


class _Hpnicf3GGsmLac_Type(SnmpAdminString):
    """Custom type hpnicf3GGsmLac based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hpnicf3GGsmLac_Type.__name__ = "SnmpAdminString"
_Hpnicf3GGsmLac_Object = MibTableColumn
hpnicf3GGsmLac = _Hpnicf3GGsmLac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 4, 1, 1, 10),
    _Hpnicf3GGsmLac_Type()
)
hpnicf3GGsmLac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicf3GGsmLac.setStatus("current")


class _Hpnicf3GGsmCellId_Type(SnmpAdminString):
    """Custom type hpnicf3GGsmCellId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hpnicf3GGsmCellId_Type.__name__ = "SnmpAdminString"
_Hpnicf3GGsmCellId_Object = MibTableColumn
hpnicf3GGsmCellId = _Hpnicf3GGsmCellId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 4, 1, 1, 11),
    _Hpnicf3GGsmCellId_Type()
)
hpnicf3GGsmCellId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicf3GGsmCellId.setStatus("current")


class _Hpnicf3GGsmSimStatus_Type(Integer32):
    """Custom type hpnicf3GGsmSimStatus based on Integer32"""
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


_Hpnicf3GGsmSimStatus_Type.__name__ = "Integer32"
_Hpnicf3GGsmSimStatus_Object = MibTableColumn
hpnicf3GGsmSimStatus = _Hpnicf3GGsmSimStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 4, 1, 1, 12),
    _Hpnicf3GGsmSimStatus_Type()
)
hpnicf3GGsmSimStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicf3GGsmSimStatus.setStatus("current")


class _Hpnicf3GGsmCurServiceStatus_Type(Integer32):
    """Custom type hpnicf3GGsmCurServiceStatus based on Integer32"""
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


_Hpnicf3GGsmCurServiceStatus_Type.__name__ = "Integer32"
_Hpnicf3GGsmCurServiceStatus_Object = MibTableColumn
hpnicf3GGsmCurServiceStatus = _Hpnicf3GGsmCurServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 4, 1, 1, 13),
    _Hpnicf3GGsmCurServiceStatus_Type()
)
hpnicf3GGsmCurServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicf3GGsmCurServiceStatus.setStatus("current")


class _Hpnicf3GGsmCurRoamingStatus_Type(Integer32):
    """Custom type hpnicf3GGsmCurRoamingStatus based on Integer32"""
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


_Hpnicf3GGsmCurRoamingStatus_Type.__name__ = "Integer32"
_Hpnicf3GGsmCurRoamingStatus_Object = MibTableColumn
hpnicf3GGsmCurRoamingStatus = _Hpnicf3GGsmCurRoamingStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 4, 1, 1, 14),
    _Hpnicf3GGsmCurRoamingStatus_Type()
)
hpnicf3GGsmCurRoamingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicf3GGsmCurRoamingStatus.setStatus("current")


class _Hpnicf3GGsmMcc_Type(SnmpAdminString):
    """Custom type hpnicf3GGsmMcc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hpnicf3GGsmMcc_Type.__name__ = "SnmpAdminString"
_Hpnicf3GGsmMcc_Object = MibTableColumn
hpnicf3GGsmMcc = _Hpnicf3GGsmMcc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 4, 1, 1, 15),
    _Hpnicf3GGsmMcc_Type()
)
hpnicf3GGsmMcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicf3GGsmMcc.setStatus("current")


class _Hpnicf3GGsmMnc_Type(SnmpAdminString):
    """Custom type hpnicf3GGsmMnc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hpnicf3GGsmMnc_Type.__name__ = "SnmpAdminString"
_Hpnicf3GGsmMnc_Object = MibTableColumn
hpnicf3GGsmMnc = _Hpnicf3GGsmMnc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 4, 1, 1, 16),
    _Hpnicf3GGsmMnc_Type()
)
hpnicf3GGsmMnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicf3GGsmMnc.setStatus("current")
_HpnicfLte_ObjectIdentity = ObjectIdentity
hpnicfLte = _HpnicfLte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 5)
)
_HpnicfLteInfoTable_Object = MibTable
hpnicfLteInfoTable = _HpnicfLteInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hpnicfLteInfoTable.setStatus("current")
_HpnicfLteInfoEntry_Object = MibTableRow
hpnicfLteInfoEntry = _HpnicfLteInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 5, 1, 1)
)
hpnicfLteInfoEntry.setIndexNames(
    (0, "HPN-ICF-3GMODEM-MIB", "hpnicfWirelessCardIndex"),
)
if mibBuilder.loadTexts:
    hpnicfLteInfoEntry.setStatus("current")
_HpnicfLteCurrentRsrp_Type = Integer32
_HpnicfLteCurrentRsrp_Object = MibTableColumn
hpnicfLteCurrentRsrp = _HpnicfLteCurrentRsrp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 5, 1, 1, 1),
    _HpnicfLteCurrentRsrp_Type()
)
hpnicfLteCurrentRsrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLteCurrentRsrp.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfLteCurrentRsrp.setUnits("dBm")
_HpnicfLteCurrentRsrq_Type = Integer32
_HpnicfLteCurrentRsrq_Object = MibTableColumn
hpnicfLteCurrentRsrq = _HpnicfLteCurrentRsrq_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 5, 1, 1, 2),
    _HpnicfLteCurrentRsrq_Type()
)
hpnicfLteCurrentRsrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLteCurrentRsrq.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfLteCurrentRsrq.setUnits("dB")
_HpnicfLteCurrentSinr_Type = Integer32
_HpnicfLteCurrentSinr_Object = MibTableColumn
hpnicfLteCurrentSinr = _HpnicfLteCurrentSinr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 5, 1, 1, 3),
    _HpnicfLteCurrentSinr_Type()
)
hpnicfLteCurrentSinr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLteCurrentSinr.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfLteCurrentSinr.setUnits("dB")
_HpnicfLteTxPower_Type = Integer32
_HpnicfLteTxPower_Object = MibTableColumn
hpnicfLteTxPower = _HpnicfLteTxPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 5, 1, 1, 4),
    _HpnicfLteTxPower_Type()
)
hpnicfLteTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLteTxPower.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfLteTxPower.setUnits("dB")


class _HpnicfLteCurrentRssi_Type(Integer32):
    """Custom type hpnicfLteCurrentRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, -2147483648),
        ValueRangeConstraint(-150, 0),
    )


_HpnicfLteCurrentRssi_Type.__name__ = "Integer32"
_HpnicfLteCurrentRssi_Object = MibTableColumn
hpnicfLteCurrentRssi = _HpnicfLteCurrentRssi_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 5, 1, 1, 5),
    _HpnicfLteCurrentRssi_Type()
)
hpnicfLteCurrentRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLteCurrentRssi.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfLteCurrentRssi.setUnits("dBm")


class _HpnicfLteRssiMediumThreshold_Type(Integer32):
    """Custom type hpnicfLteRssiMediumThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_HpnicfLteRssiMediumThreshold_Type.__name__ = "Integer32"
_HpnicfLteRssiMediumThreshold_Object = MibTableColumn
hpnicfLteRssiMediumThreshold = _HpnicfLteRssiMediumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 5, 1, 1, 6),
    _HpnicfLteRssiMediumThreshold_Type()
)
hpnicfLteRssiMediumThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLteRssiMediumThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfLteRssiMediumThreshold.setUnits("dBm")


class _HpnicfLteRssiWeakThreshold_Type(Integer32):
    """Custom type hpnicfLteRssiWeakThreshold based on Integer32"""
    defaultValue = -150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_HpnicfLteRssiWeakThreshold_Type.__name__ = "Integer32"
_HpnicfLteRssiWeakThreshold_Object = MibTableColumn
hpnicfLteRssiWeakThreshold = _HpnicfLteRssiWeakThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 1, 5, 1, 1, 7),
    _HpnicfLteRssiWeakThreshold_Type()
)
hpnicfLteRssiWeakThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLteRssiWeakThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfLteRssiWeakThreshold.setUnits("dBm")
_Hpnicf3GModemTrap_ObjectIdentity = ObjectIdentity
hpnicf3GModemTrap = _Hpnicf3GModemTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 2)
)


class _HpnicfDevSerialNumber_Type(SnmpAdminString):
    """Custom type hpnicfDevSerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfDevSerialNumber_Type.__name__ = "SnmpAdminString"
_HpnicfDevSerialNumber_Object = MibScalar
hpnicfDevSerialNumber = _HpnicfDevSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 2, 1),
    _HpnicfDevSerialNumber_Type()
)
hpnicfDevSerialNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDevSerialNumber.setStatus("current")


class _HpnicfDeviceOUI_Type(SnmpAdminString):
    """Custom type hpnicfDeviceOUI based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpnicfDeviceOUI_Type.__name__ = "SnmpAdminString"
_HpnicfDeviceOUI_Object = MibScalar
hpnicfDeviceOUI = _HpnicfDeviceOUI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 2, 2),
    _HpnicfDeviceOUI_Type()
)
hpnicfDeviceOUI.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDeviceOUI.setStatus("current")


class _HpnicfAccessMedia_Type(Integer32):
    """Custom type hpnicfAccessMedia based on Integer32"""
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


_HpnicfAccessMedia_Type.__name__ = "Integer32"
_HpnicfAccessMedia_Object = MibScalar
hpnicfAccessMedia = _HpnicfAccessMedia_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 2, 3),
    _HpnicfAccessMedia_Type()
)
hpnicfAccessMedia.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfAccessMedia.setStatus("current")


class _Hpnicf3GCurrentService_Type(Integer32):
    """Custom type hpnicf3GCurrentService based on Integer32"""
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
        *(("evDo", 3),
          ("gsm", 4),
          ("lte", 5),
          ("oneXRtt", 2),
          ("unknown", 1))
    )


_Hpnicf3GCurrentService_Type.__name__ = "Integer32"
_Hpnicf3GCurrentService_Object = MibScalar
hpnicf3GCurrentService = _Hpnicf3GCurrentService_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 2, 4),
    _Hpnicf3GCurrentService_Type()
)
hpnicf3GCurrentService.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicf3GCurrentService.setStatus("current")


class _Hpnicf3GCurrentRssiBind_Type(Integer32):
    """Custom type hpnicf3GCurrentRssiBind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, -2147483648),
        ValueRangeConstraint(-150, 0),
    )


_Hpnicf3GCurrentRssiBind_Type.__name__ = "Integer32"
_Hpnicf3GCurrentRssiBind_Object = MibScalar
hpnicf3GCurrentRssiBind = _Hpnicf3GCurrentRssiBind_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 2, 5),
    _Hpnicf3GCurrentRssiBind_Type()
)
hpnicf3GCurrentRssiBind.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicf3GCurrentRssiBind.setStatus("current")
if mibBuilder.loadTexts:
    hpnicf3GCurrentRssiBind.setUnits("dBm")


class _Hpnicf3GImsiBind_Type(SnmpAdminString):
    """Custom type hpnicf3GImsiBind based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hpnicf3GImsiBind_Type.__name__ = "SnmpAdminString"
_Hpnicf3GImsiBind_Object = MibScalar
hpnicf3GImsiBind = _Hpnicf3GImsiBind_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 2, 6),
    _Hpnicf3GImsiBind_Type()
)
hpnicf3GImsiBind.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicf3GImsiBind.setStatus("current")


class _HpnicfSmsSrcNumberBind_Type(SnmpAdminString):
    """Custom type hpnicfSmsSrcNumberBind based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HpnicfSmsSrcNumberBind_Type.__name__ = "SnmpAdminString"
_HpnicfSmsSrcNumberBind_Object = MibScalar
hpnicfSmsSrcNumberBind = _HpnicfSmsSrcNumberBind_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 2, 7),
    _HpnicfSmsSrcNumberBind_Type()
)
hpnicfSmsSrcNumberBind.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfSmsSrcNumberBind.setStatus("current")


class _HpnicfSmsTimeBind_Type(SnmpAdminString):
    """Custom type hpnicfSmsTimeBind based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HpnicfSmsTimeBind_Type.__name__ = "SnmpAdminString"
_HpnicfSmsTimeBind_Object = MibScalar
hpnicfSmsTimeBind = _HpnicfSmsTimeBind_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 2, 8),
    _HpnicfSmsTimeBind_Type()
)
hpnicfSmsTimeBind.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfSmsTimeBind.setStatus("current")
_HpnicfSmsEncodeBind_Type = HpnicfSmsEncodeType
_HpnicfSmsEncodeBind_Object = MibScalar
hpnicfSmsEncodeBind = _HpnicfSmsEncodeBind_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 2, 9),
    _HpnicfSmsEncodeBind_Type()
)
hpnicfSmsEncodeBind.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfSmsEncodeBind.setStatus("current")


class _HpnicfSmsContentBind_Type(OctetString):
    """Custom type hpnicfSmsContentBind based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_HpnicfSmsContentBind_Type.__name__ = "OctetString"
_HpnicfSmsContentBind_Object = MibScalar
hpnicfSmsContentBind = _HpnicfSmsContentBind_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 2, 10),
    _HpnicfSmsContentBind_Type()
)
hpnicfSmsContentBind.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfSmsContentBind.setStatus("current")
_Hpnicf3GModemTraps_ObjectIdentity = ObjectIdentity
hpnicf3GModemTraps = _Hpnicf3GModemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 3)
)
_Hpnicf3GModemTrapPrefix_ObjectIdentity = ObjectIdentity
hpnicf3GModemTrapPrefix = _Hpnicf3GModemTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 3, 0)
)

# Managed Objects groups


# Notification objects

hpnicfWirelessCardInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 3, 0, 1)
)
hpnicfWirelessCardInserted.setObjects(
      *(("HPN-ICF-3GMODEM-MIB", "hpnicfDeviceOUI"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfDevSerialNumber"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfWirelessCardSerialNumber"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfUIMImsi"))
)
if mibBuilder.loadTexts:
    hpnicfWirelessCardInserted.setStatus(
        "current"
    )

hpnicfWirelessCardPulledOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 3, 0, 2)
)
hpnicfWirelessCardPulledOut.setObjects(
      *(("HPN-ICF-3GMODEM-MIB", "hpnicfDeviceOUI"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfDevSerialNumber"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfWirelessCardSerialNumber"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfUIMImsi"))
)
if mibBuilder.loadTexts:
    hpnicfWirelessCardPulledOut.setStatus(
        "current"
    )

hpnicfUIMPinInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 3, 0, 3)
)
hpnicfUIMPinInvalid.setObjects(
      *(("HPN-ICF-3GMODEM-MIB", "hpnicfDeviceOUI"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfDevSerialNumber"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfWirelessCardSerialNumber"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfUIMImsi"))
)
if mibBuilder.loadTexts:
    hpnicfUIMPinInvalid.setStatus(
        "current"
    )

hpnicfUIMPinChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 3, 0, 4)
)
hpnicfUIMPinChanged.setObjects(
      *(("HPN-ICF-3GMODEM-MIB", "hpnicfDeviceOUI"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfDevSerialNumber"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfWirelessCardSerialNumber"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfUIMImsi"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfUIMOldPin"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfUIMPin"))
)
if mibBuilder.loadTexts:
    hpnicfUIMPinChanged.setStatus(
        "current"
    )

hpnicfAccessMediaChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 3, 0, 5)
)
hpnicfAccessMediaChanged.setObjects(
      *(("HPN-ICF-3GMODEM-MIB", "hpnicfDeviceOUI"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfDevSerialNumber"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfWirelessCardSerialNumber"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfUIMImsi"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfAccessMedia"))
)
if mibBuilder.loadTexts:
    hpnicfAccessMediaChanged.setStatus(
        "current"
    )

hpnicf3GRssiStrongSignalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 3, 0, 6)
)
hpnicf3GRssiStrongSignalTrap.setObjects(
      *(("HPN-ICF-3GMODEM-MIB", "hpnicfWirelessCardIndex"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfDeviceOUI"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfDevSerialNumber"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfWirelessCardSerialNumber"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicf3GCurrentService"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicf3GCurrentRssiBind"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicf3GImsiBind"))
)
if mibBuilder.loadTexts:
    hpnicf3GRssiStrongSignalTrap.setStatus(
        "current"
    )

hpnicf3GRssiMediumSignalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 3, 0, 7)
)
hpnicf3GRssiMediumSignalTrap.setObjects(
      *(("HPN-ICF-3GMODEM-MIB", "hpnicfWirelessCardIndex"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfDeviceOUI"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfDevSerialNumber"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfWirelessCardSerialNumber"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicf3GCurrentService"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicf3GCurrentRssiBind"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicf3GImsiBind"))
)
if mibBuilder.loadTexts:
    hpnicf3GRssiMediumSignalTrap.setStatus(
        "current"
    )

hpnicf3GRssiWeakSignalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 3, 0, 8)
)
hpnicf3GRssiWeakSignalTrap.setObjects(
      *(("HPN-ICF-3GMODEM-MIB", "hpnicfWirelessCardIndex"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfDeviceOUI"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfDevSerialNumber"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfWirelessCardSerialNumber"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicf3GCurrentService"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicf3GCurrentRssiBind"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicf3GImsiBind"))
)
if mibBuilder.loadTexts:
    hpnicf3GRssiWeakSignalTrap.setStatus(
        "current"
    )

hpnicfSmsTxNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 3, 0, 9)
)
hpnicfSmsTxNotification.setObjects(
      *(("HPN-ICF-3GMODEM-MIB", "hpnicfWirelessCardIndex"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfSmsSendStatus"))
)
if mibBuilder.loadTexts:
    hpnicfSmsTxNotification.setStatus(
        "current"
    )

hpnicfSmsRxNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98, 3, 0, 10)
)
hpnicfSmsRxNotification.setObjects(
      *(("HPN-ICF-3GMODEM-MIB", "hpnicfWirelessCardIndex"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfSmsSrcNumberBind"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfSmsTimeBind"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfSmsEncodeBind"),
        ("HPN-ICF-3GMODEM-MIB", "hpnicfSmsContentBind"))
)
if mibBuilder.loadTexts:
    hpnicfSmsRxNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-3GMODEM-MIB",
    **{"HpnicfUIMStatusType": HpnicfUIMStatusType,
       "HpnicfSmsEncodeType": HpnicfSmsEncodeType,
       "hpnicf3GModem": hpnicf3GModem,
       "hpnicf3GModemObjects": hpnicf3GModemObjects,
       "hpnicfWirelessCard": hpnicfWirelessCard,
       "hpnicfWirelessCardTable": hpnicfWirelessCardTable,
       "hpnicfWirelessCardEntry": hpnicfWirelessCardEntry,
       "hpnicfWirelessCardIndex": hpnicfWirelessCardIndex,
       "hpnicfWirelessCardModelName": hpnicfWirelessCardModelName,
       "hpnicfWirelessCardMfgName": hpnicfWirelessCardMfgName,
       "hpnicfWirelessCardDescription": hpnicfWirelessCardDescription,
       "hpnicfWirelessCardSerialNumber": hpnicfWirelessCardSerialNumber,
       "hpnicfWirelessCardCMIIID": hpnicfWirelessCardCMIIID,
       "hpnicfWirelessCardHardwareVersion": hpnicfWirelessCardHardwareVersion,
       "hpnicfWirelessCardFirmwareVersion": hpnicfWirelessCardFirmwareVersion,
       "hpnicfWirelessCardPRLVersion": hpnicfWirelessCardPRLVersion,
       "hpnicfWirelessCardInterfaceIndex": hpnicfWirelessCardInterfaceIndex,
       "hpnicfWirelessCardModemStatus": hpnicfWirelessCardModemStatus,
       "hpnicfWirelessCardModemMode": hpnicfWirelessCardModemMode,
       "hpnicfWirelessCardCurNetConn": hpnicfWirelessCardCurNetConn,
       "hpnicfSmsGroup": hpnicfSmsGroup,
       "hpnicfSmsScalarObjects": hpnicfSmsScalarObjects,
       "hpnicfSmsRxNotifSwitch": hpnicfSmsRxNotifSwitch,
       "hpnicfSmsOperationTable": hpnicfSmsOperationTable,
       "hpnicfSmsOperationEntry": hpnicfSmsOperationEntry,
       "hpnicfSmsDestNumber": hpnicfSmsDestNumber,
       "hpnicfSmsEncode": hpnicfSmsEncode,
       "hpnicfSmsContent": hpnicfSmsContent,
       "hpnicfSmsSendStatus": hpnicfSmsSendStatus,
       "hpnicfWirelessCardOnlineTable": hpnicfWirelessCardOnlineTable,
       "hpnicfWirelessCardOnlineEntry": hpnicfWirelessCardOnlineEntry,
       "hpnicfWirelessCardOnlineTime": hpnicfWirelessCardOnlineTime,
       "hpnicfWirelessCardOnlineType": hpnicfWirelessCardOnlineType,
       "hpnicfUIM": hpnicfUIM,
       "hpnicfUIMInfoTable": hpnicfUIMInfoTable,
       "hpnicfUIMInfoEntry": hpnicfUIMInfoEntry,
       "hpnicfUIMIndex": hpnicfUIMIndex,
       "hpnicfUIMStatus": hpnicfUIMStatus,
       "hpnicfUIMImsi": hpnicfUIMImsi,
       "hpnicfUIMPin": hpnicfUIMPin,
       "hpnicfUIMVoltage": hpnicfUIMVoltage,
       "hpnicfUIMProvider": hpnicfUIMProvider,
       "hpnicfUIMSignal": hpnicfUIMSignal,
       "hpnicfUIMTryPinPukTimes": hpnicfUIMTryPinPukTimes,
       "hpnicfUIMOldPin": hpnicfUIMOldPin,
       "hpnicf3GCdma": hpnicf3GCdma,
       "hpnicf3GCdma1xRttTable": hpnicf3GCdma1xRttTable,
       "hpnicf3GCdma1xRttEntry": hpnicf3GCdma1xRttEntry,
       "hpnicf3GCdma1xRttCurrentRssi": hpnicf3GCdma1xRttCurrentRssi,
       "hpnicf3GCdma1xRttRssiMediumThreshold": hpnicf3GCdma1xRttRssiMediumThreshold,
       "hpnicf3GCdma1xRttRssiWeakThreshold": hpnicf3GCdma1xRttRssiWeakThreshold,
       "hpnicf3GCdma1xRttCurServiceStatus": hpnicf3GCdma1xRttCurServiceStatus,
       "hpnicf3GCdma1xRttCurRoamingStatus": hpnicf3GCdma1xRttCurRoamingStatus,
       "hpnicf3GCdmaEvDoTable": hpnicf3GCdmaEvDoTable,
       "hpnicf3GCdmaEvDoEntry": hpnicf3GCdmaEvDoEntry,
       "hpnicf3GCdmaEvDoCurrentRssi": hpnicf3GCdmaEvDoCurrentRssi,
       "hpnicf3GCdmaEvDoRssiMediumThreshold": hpnicf3GCdmaEvDoRssiMediumThreshold,
       "hpnicf3GCdmaEvDoRssiWeakThreshold": hpnicf3GCdmaEvDoRssiWeakThreshold,
       "hpnicf3GCdmaEvDoCurServiceStatus": hpnicf3GCdmaEvDoCurServiceStatus,
       "hpnicf3GCdmaEvDoCurRoamingStatus": hpnicf3GCdmaEvDoCurRoamingStatus,
       "hpnicf3GGsm": hpnicf3GGsm,
       "hpnicf3GGsmInfoTable": hpnicf3GGsmInfoTable,
       "hpnicf3GGsmInfoEntry": hpnicf3GGsmInfoEntry,
       "hpnicf3GGsmCurrentRssi": hpnicf3GGsmCurrentRssi,
       "hpnicf3GGsmRssiMediumThreshold": hpnicf3GGsmRssiMediumThreshold,
       "hpnicf3GGsmRssiWeakThreshold": hpnicf3GGsmRssiWeakThreshold,
       "hpnicf3GGsmImsi": hpnicf3GGsmImsi,
       "hpnicf3GGsmImei": hpnicf3GGsmImei,
       "hpnicf3GGsmApn": hpnicf3GGsmApn,
       "hpnicf3GGsmPacketSessionStatus": hpnicf3GGsmPacketSessionStatus,
       "hpnicf3GGsmNetworkSelectionMode": hpnicf3GGsmNetworkSelectionMode,
       "hpnicf3GGsmMobileNetworkName": hpnicf3GGsmMobileNetworkName,
       "hpnicf3GGsmLac": hpnicf3GGsmLac,
       "hpnicf3GGsmCellId": hpnicf3GGsmCellId,
       "hpnicf3GGsmSimStatus": hpnicf3GGsmSimStatus,
       "hpnicf3GGsmCurServiceStatus": hpnicf3GGsmCurServiceStatus,
       "hpnicf3GGsmCurRoamingStatus": hpnicf3GGsmCurRoamingStatus,
       "hpnicf3GGsmMcc": hpnicf3GGsmMcc,
       "hpnicf3GGsmMnc": hpnicf3GGsmMnc,
       "hpnicfLte": hpnicfLte,
       "hpnicfLteInfoTable": hpnicfLteInfoTable,
       "hpnicfLteInfoEntry": hpnicfLteInfoEntry,
       "hpnicfLteCurrentRsrp": hpnicfLteCurrentRsrp,
       "hpnicfLteCurrentRsrq": hpnicfLteCurrentRsrq,
       "hpnicfLteCurrentSinr": hpnicfLteCurrentSinr,
       "hpnicfLteTxPower": hpnicfLteTxPower,
       "hpnicfLteCurrentRssi": hpnicfLteCurrentRssi,
       "hpnicfLteRssiMediumThreshold": hpnicfLteRssiMediumThreshold,
       "hpnicfLteRssiWeakThreshold": hpnicfLteRssiWeakThreshold,
       "hpnicf3GModemTrap": hpnicf3GModemTrap,
       "hpnicfDevSerialNumber": hpnicfDevSerialNumber,
       "hpnicfDeviceOUI": hpnicfDeviceOUI,
       "hpnicfAccessMedia": hpnicfAccessMedia,
       "hpnicf3GCurrentService": hpnicf3GCurrentService,
       "hpnicf3GCurrentRssiBind": hpnicf3GCurrentRssiBind,
       "hpnicf3GImsiBind": hpnicf3GImsiBind,
       "hpnicfSmsSrcNumberBind": hpnicfSmsSrcNumberBind,
       "hpnicfSmsTimeBind": hpnicfSmsTimeBind,
       "hpnicfSmsEncodeBind": hpnicfSmsEncodeBind,
       "hpnicfSmsContentBind": hpnicfSmsContentBind,
       "hpnicf3GModemTraps": hpnicf3GModemTraps,
       "hpnicf3GModemTrapPrefix": hpnicf3GModemTrapPrefix,
       "hpnicfWirelessCardInserted": hpnicfWirelessCardInserted,
       "hpnicfWirelessCardPulledOut": hpnicfWirelessCardPulledOut,
       "hpnicfUIMPinInvalid": hpnicfUIMPinInvalid,
       "hpnicfUIMPinChanged": hpnicfUIMPinChanged,
       "hpnicfAccessMediaChanged": hpnicfAccessMediaChanged,
       "hpnicf3GRssiStrongSignalTrap": hpnicf3GRssiStrongSignalTrap,
       "hpnicf3GRssiMediumSignalTrap": hpnicf3GRssiMediumSignalTrap,
       "hpnicf3GRssiWeakSignalTrap": hpnicf3GRssiWeakSignalTrap,
       "hpnicfSmsTxNotification": hpnicfSmsTxNotification,
       "hpnicfSmsRxNotification": hpnicfSmsRxNotification}
)
