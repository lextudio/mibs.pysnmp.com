# SNMP MIB module (DLGR4DEV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLGR4DEV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:38 2024
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

(dlgR4Resources,) = mibBuilder.importSymbols(
    "DLGC-GLOBAL-REG",
    "dlgR4Resources")

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
 NotificationType,
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
    "NotificationType",
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DlgR4ResObj_ObjectIdentity = ObjectIdentity
dlgR4ResObj = _DlgR4ResObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1)
)
_DlgR4MibRev_ObjectIdentity = ObjectIdentity
dlgR4MibRev = _DlgR4MibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 1)
)


class _DlgR4MibRevMajor_Type(Integer32):
    """Custom type dlgR4MibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DlgR4MibRevMajor_Type.__name__ = "Integer32"
_DlgR4MibRevMajor_Object = MibScalar
dlgR4MibRevMajor = _DlgR4MibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 1, 1),
    _DlgR4MibRevMajor_Type()
)
dlgR4MibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4MibRevMajor.setStatus("mandatory")


class _DlgR4MibRevMinor_Type(Integer32):
    """Custom type dlgR4MibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DlgR4MibRevMinor_Type.__name__ = "Integer32"
_DlgR4MibRevMinor_Object = MibScalar
dlgR4MibRevMinor = _DlgR4MibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 1, 2),
    _DlgR4MibRevMinor_Type()
)
dlgR4MibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4MibRevMinor.setStatus("mandatory")
_DlgR4DeviceInfo_ObjectIdentity = ObjectIdentity
dlgR4DeviceInfo = _DlgR4DeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2)
)
_DlgR4DeviceTable_Object = MibTable
dlgR4DeviceTable = _DlgR4DeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dlgR4DeviceTable.setStatus("mandatory")
_DlgR4DeviceEntry_Object = MibTableRow
dlgR4DeviceEntry = _DlgR4DeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 1, 1)
)
dlgR4DeviceEntry.setIndexNames(
    (0, "DLGR4DEV-MIB", "dlgR4DeviceIndex"),
)
if mibBuilder.loadTexts:
    dlgR4DeviceEntry.setStatus("mandatory")


class _DlgR4DeviceIndex_Type(Integer32):
    """Custom type dlgR4DeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DlgR4DeviceIndex_Type.__name__ = "Integer32"
_DlgR4DeviceIndex_Object = MibTableColumn
dlgR4DeviceIndex = _DlgR4DeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 1, 1, 1),
    _DlgR4DeviceIndex_Type()
)
dlgR4DeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4DeviceIndex.setStatus("mandatory")
_DlgR4DeviceName_Type = DisplayString
_DlgR4DeviceName_Object = MibTableColumn
dlgR4DeviceName = _DlgR4DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 1, 1, 2),
    _DlgR4DeviceName_Type()
)
dlgR4DeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4DeviceName.setStatus("mandatory")


class _DlgR4DeviceType_Type(Integer32):
    """Custom type dlgR4DeviceType based on Integer32"""
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
        *(("dti", 3),
          ("isdn", 4),
          ("msi", 5),
          ("unknown", 1),
          ("voice", 2))
    )


_DlgR4DeviceType_Type.__name__ = "Integer32"
_DlgR4DeviceType_Object = MibTableColumn
dlgR4DeviceType = _DlgR4DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 1, 1, 3),
    _DlgR4DeviceType_Type()
)
dlgR4DeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4DeviceType.setStatus("mandatory")
_DlgR4DeviceHiIdentIndex_Type = Integer32
_DlgR4DeviceHiIdentIndex_Object = MibTableColumn
dlgR4DeviceHiIdentIndex = _DlgR4DeviceHiIdentIndex_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 1, 1, 4),
    _DlgR4DeviceHiIdentIndex_Type()
)
dlgR4DeviceHiIdentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4DeviceHiIdentIndex.setStatus("mandatory")
_DlgR4DeviceOpenCount_Type = Gauge32
_DlgR4DeviceOpenCount_Object = MibTableColumn
dlgR4DeviceOpenCount = _DlgR4DeviceOpenCount_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 1, 1, 5),
    _DlgR4DeviceOpenCount_Type()
)
dlgR4DeviceOpenCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4DeviceOpenCount.setStatus("mandatory")
_DlgR4DeviceXmitCTbusSlot_Type = Integer32
_DlgR4DeviceXmitCTbusSlot_Object = MibTableColumn
dlgR4DeviceXmitCTbusSlot = _DlgR4DeviceXmitCTbusSlot_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 1, 1, 6),
    _DlgR4DeviceXmitCTbusSlot_Type()
)
dlgR4DeviceXmitCTbusSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4DeviceXmitCTbusSlot.setStatus("mandatory")
_DlgR4DeviceRcvrCTbusSlot_Type = Integer32
_DlgR4DeviceRcvrCTbusSlot_Object = MibTableColumn
dlgR4DeviceRcvrCTbusSlot = _DlgR4DeviceRcvrCTbusSlot_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 1, 1, 7),
    _DlgR4DeviceRcvrCTbusSlot_Type()
)
dlgR4DeviceRcvrCTbusSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4DeviceRcvrCTbusSlot.setStatus("mandatory")
_DlgR4VoiceTable_Object = MibTable
dlgR4VoiceTable = _DlgR4VoiceTable_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dlgR4VoiceTable.setStatus("mandatory")
_DlgR4VoiceEntry_Object = MibTableRow
dlgR4VoiceEntry = _DlgR4VoiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 2, 1)
)
dlgR4VoiceEntry.setIndexNames(
    (0, "DLGR4DEV-MIB", "dlgR4VoiceChannelIndex"),
)
if mibBuilder.loadTexts:
    dlgR4VoiceEntry.setStatus("mandatory")


class _DlgR4VoiceChannelIndex_Type(Integer32):
    """Custom type dlgR4VoiceChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DlgR4VoiceChannelIndex_Type.__name__ = "Integer32"
_DlgR4VoiceChannelIndex_Object = MibTableColumn
dlgR4VoiceChannelIndex = _DlgR4VoiceChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 2, 1, 1),
    _DlgR4VoiceChannelIndex_Type()
)
dlgR4VoiceChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4VoiceChannelIndex.setStatus("mandatory")


class _DlgR4VoiceChannelStatus_Type(Integer32):
    """Custom type dlgR4VoiceChannelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              16)
        )
    )
    namedValues = NamedValues(
        *(("betweenFAXPages", 10),
          ("blocked", 16),
          ("callProgess", 13),
          ("dialing", 4),
          ("gettingDigits", 5),
          ("gettingR2MF", 14),
          ("hookState", 11),
          ("idle", 1),
          ("playTone", 6),
          ("playing", 2),
          ("receivingFax", 9),
          ("recording", 3),
          ("sendingFax", 8),
          ("winking", 12))
    )


_DlgR4VoiceChannelStatus_Type.__name__ = "Integer32"
_DlgR4VoiceChannelStatus_Object = MibTableColumn
dlgR4VoiceChannelStatus = _DlgR4VoiceChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 2, 1, 2),
    _DlgR4VoiceChannelStatus_Type()
)
dlgR4VoiceChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4VoiceChannelStatus.setStatus("mandatory")


class _DlgR4VoiceLineStatus_Type(Integer32):
    """Custom type dlgR4VoiceLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lcDetected", 3),
          ("offhook", 2),
          ("onhook", 1),
          ("unknown", 0))
    )


_DlgR4VoiceLineStatus_Type.__name__ = "Integer32"
_DlgR4VoiceLineStatus_Object = MibTableColumn
dlgR4VoiceLineStatus = _DlgR4VoiceLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 2, 1, 3),
    _DlgR4VoiceLineStatus_Type()
)
dlgR4VoiceLineStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlgR4VoiceLineStatus.setStatus("mandatory")
_DlgR4VoiceNumberOfDigits_Type = Integer32
_DlgR4VoiceNumberOfDigits_Object = MibTableColumn
dlgR4VoiceNumberOfDigits = _DlgR4VoiceNumberOfDigits_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 2, 1, 4),
    _DlgR4VoiceNumberOfDigits_Type()
)
dlgR4VoiceNumberOfDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4VoiceNumberOfDigits.setStatus("mandatory")
_DlgR4VoiceE2PROMFeatures_Type = Integer32
_DlgR4VoiceE2PROMFeatures_Object = MibTableColumn
dlgR4VoiceE2PROMFeatures = _DlgR4VoiceE2PROMFeatures_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 2, 1, 5),
    _DlgR4VoiceE2PROMFeatures_Type()
)
dlgR4VoiceE2PROMFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4VoiceE2PROMFeatures.setStatus("mandatory")
_DlgR4DTITable_Object = MibTable
dlgR4DTITable = _DlgR4DTITable_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    dlgR4DTITable.setStatus("mandatory")
_DlgR4DTIEntry_Object = MibTableRow
dlgR4DTIEntry = _DlgR4DTIEntry_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 3, 1)
)
dlgR4DTIEntry.setIndexNames(
    (0, "DLGR4DEV-MIB", "d"),
)
if mibBuilder.loadTexts:
    dlgR4DTIEntry.setStatus("mandatory")


class _DlgR4DTITimeslotIndex_Type(Integer32):
    """Custom type dlgR4DTITimeslotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DlgR4DTITimeslotIndex_Type.__name__ = "Integer32"
_DlgR4DTITimeslotIndex_Object = MibTableColumn
dlgR4DTITimeslotIndex = _DlgR4DTITimeslotIndex_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 3, 1, 1),
    _DlgR4DTITimeslotIndex_Type()
)
dlgR4DTITimeslotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4DTITimeslotIndex.setStatus("mandatory")
_DlgR4DTIProtocol_Type = DisplayString
_DlgR4DTIProtocol_Object = MibTableColumn
dlgR4DTIProtocol = _DlgR4DTIProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 3, 1, 2),
    _DlgR4DTIProtocol_Type()
)
dlgR4DTIProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4DTIProtocol.setStatus("mandatory")


class _DlgR4DTITimeslotStatus_Type(Integer32):
    """Custom type dlgR4DTITimeslotStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dialing", 1),
          ("idle", 0),
          ("waitingForCall", 3),
          ("winking", 2))
    )


_DlgR4DTITimeslotStatus_Type.__name__ = "Integer32"
_DlgR4DTITimeslotStatus_Object = MibTableColumn
dlgR4DTITimeslotStatus = _DlgR4DTITimeslotStatus_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 3, 1, 3),
    _DlgR4DTITimeslotStatus_Type()
)
dlgR4DTITimeslotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4DTITimeslotStatus.setStatus("mandatory")
_DlgR4DTIRcvSigBits_Type = Integer32
_DlgR4DTIRcvSigBits_Object = MibTableColumn
dlgR4DTIRcvSigBits = _DlgR4DTIRcvSigBits_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 3, 1, 4),
    _DlgR4DTIRcvSigBits_Type()
)
dlgR4DTIRcvSigBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4DTIRcvSigBits.setStatus("mandatory")
_DlgR4DTIXmitSigBits_Type = Integer32
_DlgR4DTIXmitSigBits_Object = MibTableColumn
dlgR4DTIXmitSigBits = _DlgR4DTIXmitSigBits_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 3, 1, 5),
    _DlgR4DTIXmitSigBits_Type()
)
dlgR4DTIXmitSigBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlgR4DTIXmitSigBits.setStatus("mandatory")
_DlgR4ISDNTable_Object = MibTable
dlgR4ISDNTable = _DlgR4ISDNTable_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    dlgR4ISDNTable.setStatus("mandatory")
_DlgR4ISDNEntry_Object = MibTableRow
dlgR4ISDNEntry = _DlgR4ISDNEntry_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 4, 1)
)
dlgR4ISDNEntry.setIndexNames(
    (0, "DLGR4DEV-MIB", "dlgR4ISDNBChannelIndex"),
)
if mibBuilder.loadTexts:
    dlgR4ISDNEntry.setStatus("mandatory")


class _DlgR4ISDNBChannelIndex_Type(Integer32):
    """Custom type dlgR4ISDNBChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DlgR4ISDNBChannelIndex_Type.__name__ = "Integer32"
_DlgR4ISDNBChannelIndex_Object = MibTableColumn
dlgR4ISDNBChannelIndex = _DlgR4ISDNBChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 4, 1, 1),
    _DlgR4ISDNBChannelIndex_Type()
)
dlgR4ISDNBChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4ISDNBChannelIndex.setStatus("mandatory")
_DlgR4ISDNProtocol_Type = DisplayString
_DlgR4ISDNProtocol_Object = MibTableColumn
dlgR4ISDNProtocol = _DlgR4ISDNProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 4, 1, 2),
    _DlgR4ISDNProtocol_Type()
)
dlgR4ISDNProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlgR4ISDNProtocol.setStatus("mandatory")


class _DlgR4ISDNBChannelStatus_Type(Integer32):
    """Custom type dlgR4ISDNBChannelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 0),
          ("maintenance", 1),
          ("outOfService", 2))
    )


_DlgR4ISDNBChannelStatus_Type.__name__ = "Integer32"
_DlgR4ISDNBChannelStatus_Object = MibTableColumn
dlgR4ISDNBChannelStatus = _DlgR4ISDNBChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 4, 1, 3),
    _DlgR4ISDNBChannelStatus_Type()
)
dlgR4ISDNBChannelStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlgR4ISDNBChannelStatus.setStatus("mandatory")
_DlgR4MSITable_Object = MibTable
dlgR4MSITable = _DlgR4MSITable_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    dlgR4MSITable.setStatus("mandatory")
_DlgR4MSIEntry_Object = MibTableRow
dlgR4MSIEntry = _DlgR4MSIEntry_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 5, 1)
)
dlgR4MSIEntry.setIndexNames(
    (0, "DLGR4DEV-MIB", "dlgR4MSIStationIndex"),
)
if mibBuilder.loadTexts:
    dlgR4MSIEntry.setStatus("mandatory")


class _DlgR4MSIStationIndex_Type(Integer32):
    """Custom type dlgR4MSIStationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DlgR4MSIStationIndex_Type.__name__ = "Integer32"
_DlgR4MSIStationIndex_Object = MibTableColumn
dlgR4MSIStationIndex = _DlgR4MSIStationIndex_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 5, 1, 1),
    _DlgR4MSIStationIndex_Type()
)
dlgR4MSIStationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4MSIStationIndex.setStatus("mandatory")


class _DlgR4MSIStationLineStatus_Type(Integer32):
    """Custom type dlgR4MSIStationLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              16)
        )
    )
    namedValues = NamedValues(
        *(("offhook", 16),
          ("onhook", 0))
    )


_DlgR4MSIStationLineStatus_Type.__name__ = "Integer32"
_DlgR4MSIStationLineStatus_Object = MibTableColumn
dlgR4MSIStationLineStatus = _DlgR4MSIStationLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 2, 5, 1, 2),
    _DlgR4MSIStationLineStatus_Type()
)
dlgR4MSIStationLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4MSIStationLineStatus.setStatus("mandatory")
_DlgR4SrlInfo_ObjectIdentity = ObjectIdentity
dlgR4SrlInfo = _DlgR4SrlInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 3)
)
_DlgR4SrlTable_Object = MibTable
dlgR4SrlTable = _DlgR4SrlTable_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dlgR4SrlTable.setStatus("mandatory")
_DlgR4SrlEntry_Object = MibTableRow
dlgR4SrlEntry = _DlgR4SrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 3, 1, 1)
)
dlgR4SrlEntry.setIndexNames(
    (0, "DLGR4DEV-MIB", "dlgR4SrlIndex"),
)
if mibBuilder.loadTexts:
    dlgR4SrlEntry.setStatus("mandatory")
_DlgR4SrlIndex_Type = Integer32
_DlgR4SrlIndex_Object = MibTableColumn
dlgR4SrlIndex = _DlgR4SrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 3, 1, 1, 1),
    _DlgR4SrlIndex_Type()
)
dlgR4SrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4SrlIndex.setStatus("mandatory")
_DlgR4SrlApplicationName_Type = DisplayString
_DlgR4SrlApplicationName_Object = MibTableColumn
dlgR4SrlApplicationName = _DlgR4SrlApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 3, 1, 1, 2),
    _DlgR4SrlApplicationName_Type()
)
dlgR4SrlApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4SrlApplicationName.setStatus("mandatory")
_DlgR4SrlNumberOfOpens_Type = Counter32
_DlgR4SrlNumberOfOpens_Object = MibTableColumn
dlgR4SrlNumberOfOpens = _DlgR4SrlNumberOfOpens_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 3, 1, 1, 3),
    _DlgR4SrlNumberOfOpens_Type()
)
dlgR4SrlNumberOfOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4SrlNumberOfOpens.setStatus("mandatory")
_DlgR4SrlNumberOfCloses_Type = Counter32
_DlgR4SrlNumberOfCloses_Object = MibTableColumn
dlgR4SrlNumberOfCloses = _DlgR4SrlNumberOfCloses_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 3, 1, 1, 4),
    _DlgR4SrlNumberOfCloses_Type()
)
dlgR4SrlNumberOfCloses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4SrlNumberOfCloses.setStatus("mandatory")
_DlgR4SrlEventQSize_Type = Integer32
_DlgR4SrlEventQSize_Object = MibTableColumn
dlgR4SrlEventQSize = _DlgR4SrlEventQSize_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 3, 1, 1, 5),
    _DlgR4SrlEventQSize_Type()
)
dlgR4SrlEventQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4SrlEventQSize.setStatus("mandatory")
_DlgR4SrlCurrentEventsOnQ_Type = Gauge32
_DlgR4SrlCurrentEventsOnQ_Object = MibTableColumn
dlgR4SrlCurrentEventsOnQ = _DlgR4SrlCurrentEventsOnQ_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 3, 1, 1, 6),
    _DlgR4SrlCurrentEventsOnQ_Type()
)
dlgR4SrlCurrentEventsOnQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4SrlCurrentEventsOnQ.setStatus("mandatory")
_DlgR4SrlMaxEventsOnQ_Type = Gauge32
_DlgR4SrlMaxEventsOnQ_Object = MibTableColumn
dlgR4SrlMaxEventsOnQ = _DlgR4SrlMaxEventsOnQ_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 3, 1, 1, 7),
    _DlgR4SrlMaxEventsOnQ_Type()
)
dlgR4SrlMaxEventsOnQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4SrlMaxEventsOnQ.setStatus("mandatory")
_DlgR4SrlTotalQueuedEvents_Type = Counter32
_DlgR4SrlTotalQueuedEvents_Object = MibTableColumn
dlgR4SrlTotalQueuedEvents = _DlgR4SrlTotalQueuedEvents_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 3, 1, 1, 8),
    _DlgR4SrlTotalQueuedEvents_Type()
)
dlgR4SrlTotalQueuedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4SrlTotalQueuedEvents.setStatus("mandatory")
_DlgR4SrlNumberOfHandlers_Type = Gauge32
_DlgR4SrlNumberOfHandlers_Object = MibTableColumn
dlgR4SrlNumberOfHandlers = _DlgR4SrlNumberOfHandlers_Object(
    (1, 3, 6, 1, 4, 1, 3028, 2, 1, 1, 3, 1, 1, 9),
    _DlgR4SrlNumberOfHandlers_Type()
)
dlgR4SrlNumberOfHandlers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlgR4SrlNumberOfHandlers.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLGR4DEV-MIB",
    **{"dlgR4ResObj": dlgR4ResObj,
       "dlgR4MibRev": dlgR4MibRev,
       "dlgR4MibRevMajor": dlgR4MibRevMajor,
       "dlgR4MibRevMinor": dlgR4MibRevMinor,
       "dlgR4DeviceInfo": dlgR4DeviceInfo,
       "dlgR4DeviceTable": dlgR4DeviceTable,
       "dlgR4DeviceEntry": dlgR4DeviceEntry,
       "dlgR4DeviceIndex": dlgR4DeviceIndex,
       "dlgR4DeviceName": dlgR4DeviceName,
       "dlgR4DeviceType": dlgR4DeviceType,
       "dlgR4DeviceHiIdentIndex": dlgR4DeviceHiIdentIndex,
       "dlgR4DeviceOpenCount": dlgR4DeviceOpenCount,
       "dlgR4DeviceXmitCTbusSlot": dlgR4DeviceXmitCTbusSlot,
       "dlgR4DeviceRcvrCTbusSlot": dlgR4DeviceRcvrCTbusSlot,
       "dlgR4VoiceTable": dlgR4VoiceTable,
       "dlgR4VoiceEntry": dlgR4VoiceEntry,
       "dlgR4VoiceChannelIndex": dlgR4VoiceChannelIndex,
       "dlgR4VoiceChannelStatus": dlgR4VoiceChannelStatus,
       "dlgR4VoiceLineStatus": dlgR4VoiceLineStatus,
       "dlgR4VoiceNumberOfDigits": dlgR4VoiceNumberOfDigits,
       "dlgR4VoiceE2PROMFeatures": dlgR4VoiceE2PROMFeatures,
       "dlgR4DTITable": dlgR4DTITable,
       "dlgR4DTIEntry": dlgR4DTIEntry,
       "dlgR4DTITimeslotIndex": dlgR4DTITimeslotIndex,
       "dlgR4DTIProtocol": dlgR4DTIProtocol,
       "dlgR4DTITimeslotStatus": dlgR4DTITimeslotStatus,
       "dlgR4DTIRcvSigBits": dlgR4DTIRcvSigBits,
       "dlgR4DTIXmitSigBits": dlgR4DTIXmitSigBits,
       "dlgR4ISDNTable": dlgR4ISDNTable,
       "dlgR4ISDNEntry": dlgR4ISDNEntry,
       "dlgR4ISDNBChannelIndex": dlgR4ISDNBChannelIndex,
       "dlgR4ISDNProtocol": dlgR4ISDNProtocol,
       "dlgR4ISDNBChannelStatus": dlgR4ISDNBChannelStatus,
       "dlgR4MSITable": dlgR4MSITable,
       "dlgR4MSIEntry": dlgR4MSIEntry,
       "dlgR4MSIStationIndex": dlgR4MSIStationIndex,
       "dlgR4MSIStationLineStatus": dlgR4MSIStationLineStatus,
       "dlgR4SrlInfo": dlgR4SrlInfo,
       "dlgR4SrlTable": dlgR4SrlTable,
       "dlgR4SrlEntry": dlgR4SrlEntry,
       "dlgR4SrlIndex": dlgR4SrlIndex,
       "dlgR4SrlApplicationName": dlgR4SrlApplicationName,
       "dlgR4SrlNumberOfOpens": dlgR4SrlNumberOfOpens,
       "dlgR4SrlNumberOfCloses": dlgR4SrlNumberOfCloses,
       "dlgR4SrlEventQSize": dlgR4SrlEventQSize,
       "dlgR4SrlCurrentEventsOnQ": dlgR4SrlCurrentEventsOnQ,
       "dlgR4SrlMaxEventsOnQ": dlgR4SrlMaxEventsOnQ,
       "dlgR4SrlTotalQueuedEvents": dlgR4SrlTotalQueuedEvents,
       "dlgR4SrlNumberOfHandlers": dlgR4SrlNumberOfHandlers}
)
