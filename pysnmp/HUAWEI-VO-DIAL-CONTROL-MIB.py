# SNMP MIB module (HUAWEI-VO-DIAL-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-VO-DIAL-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:29 2024
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

(voice,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "voice")

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

hwVoiceDialControlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5)
)
hwVoiceDialControlMIB.setRevisions(
        ("2004-04-08 13:45",)
)


# Types definitions



class EntryStatus(Integer32):
    """Custom type EntryStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwVoPeerObjects_ObjectIdentity = ObjectIdentity
hwVoPeerObjects = _HwVoPeerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1)
)
_HwVoPeerCommonConfigTable_Object = MibTable
hwVoPeerCommonConfigTable = _HwVoPeerCommonConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    hwVoPeerCommonConfigTable.setStatus("current")
_HwVoPeerCommonConfigEntry_Object = MibTableRow
hwVoPeerCommonConfigEntry = _HwVoPeerCommonConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1)
)
hwVoPeerCommonConfigEntry.setIndexNames(
    (0, "HUAWEI-VO-DIAL-CONTROL-MIB", "hwVoPeerConfigIndex"),
)
if mibBuilder.loadTexts:
    hwVoPeerCommonConfigEntry.setStatus("current")


class _HwVoPeerConfigIndex_Type(Integer32):
    """Custom type hwVoPeerConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwVoPeerConfigIndex_Type.__name__ = "Integer32"
_HwVoPeerConfigIndex_Object = MibTableColumn
hwVoPeerConfigIndex = _HwVoPeerConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 1),
    _HwVoPeerConfigIndex_Type()
)
hwVoPeerConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoPeerConfigIndex.setStatus("current")


class _HwVoPeerConfigType_Type(Integer32):
    """Custom type hwVoPeerConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pots", 1),
          ("vofr", 3),
          ("voip", 2))
    )


_HwVoPeerConfigType_Type.__name__ = "Integer32"
_HwVoPeerConfigType_Object = MibTableColumn
hwVoPeerConfigType = _HwVoPeerConfigType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 2),
    _HwVoPeerConfigType_Type()
)
hwVoPeerConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigType.setStatus("current")


class _HwVoPeerConfigDesPattern_Type(OctetString):
    """Custom type hwVoPeerConfigDesPattern based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwVoPeerConfigDesPattern_Type.__name__ = "OctetString"
_HwVoPeerConfigDesPattern_Object = MibTableColumn
hwVoPeerConfigDesPattern = _HwVoPeerConfigDesPattern_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 3),
    _HwVoPeerConfigDesPattern_Type()
)
hwVoPeerConfigDesPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigDesPattern.setStatus("current")


class _HwVoPeerConfigCodec1st_Type(Integer32):
    """Custom type hwVoPeerConfigCodec1st based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("default", 7),
          ("g711a", 1),
          ("g711u", 2),
          ("g723r53", 3),
          ("g723r63", 4),
          ("g729", 5),
          ("g729a", 6))
    )


_HwVoPeerConfigCodec1st_Type.__name__ = "Integer32"
_HwVoPeerConfigCodec1st_Object = MibTableColumn
hwVoPeerConfigCodec1st = _HwVoPeerConfigCodec1st_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 4),
    _HwVoPeerConfigCodec1st_Type()
)
hwVoPeerConfigCodec1st.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigCodec1st.setStatus("current")


class _HwVoPeerConfigCodec2st_Type(Integer32):
    """Custom type hwVoPeerConfigCodec2st based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("default", 7),
          ("g711a", 1),
          ("g711u", 2),
          ("g723r53", 3),
          ("g723r63", 4),
          ("g729", 5),
          ("g729a", 6))
    )


_HwVoPeerConfigCodec2st_Type.__name__ = "Integer32"
_HwVoPeerConfigCodec2st_Object = MibTableColumn
hwVoPeerConfigCodec2st = _HwVoPeerConfigCodec2st_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 5),
    _HwVoPeerConfigCodec2st_Type()
)
hwVoPeerConfigCodec2st.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigCodec2st.setStatus("current")


class _HwVoPeerConfigCodec3st_Type(Integer32):
    """Custom type hwVoPeerConfigCodec3st based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("default", 7),
          ("g711a", 1),
          ("g711u", 2),
          ("g723r53", 3),
          ("g723r63", 4),
          ("g729", 5),
          ("g729a", 6))
    )


_HwVoPeerConfigCodec3st_Type.__name__ = "Integer32"
_HwVoPeerConfigCodec3st_Object = MibTableColumn
hwVoPeerConfigCodec3st = _HwVoPeerConfigCodec3st_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 6),
    _HwVoPeerConfigCodec3st_Type()
)
hwVoPeerConfigCodec3st.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigCodec3st.setStatus("current")


class _HwVoPeerConfigCodec4st_Type(Integer32):
    """Custom type hwVoPeerConfigCodec4st based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("default", 7),
          ("g711a", 1),
          ("g711u", 2),
          ("g723r53", 3),
          ("g723r63", 4),
          ("g729", 5),
          ("g729a", 6))
    )


_HwVoPeerConfigCodec4st_Type.__name__ = "Integer32"
_HwVoPeerConfigCodec4st_Object = MibTableColumn
hwVoPeerConfigCodec4st = _HwVoPeerConfigCodec4st_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 7),
    _HwVoPeerConfigCodec4st_Type()
)
hwVoPeerConfigCodec4st.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigCodec4st.setStatus("current")


class _HwVoPeerConfigIpPreced_Type(Integer32):
    """Custom type hwVoPeerConfigIpPreced based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwVoPeerConfigIpPreced_Type.__name__ = "Integer32"
_HwVoPeerConfigIpPreced_Object = MibTableColumn
hwVoPeerConfigIpPreced = _HwVoPeerConfigIpPreced_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 8),
    _HwVoPeerConfigIpPreced_Type()
)
hwVoPeerConfigIpPreced.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigIpPreced.setStatus("current")


class _HwVoPeerConfigShutDown_Type(Integer32):
    """Custom type hwVoPeerConfigShutDown based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwVoPeerConfigShutDown_Type.__name__ = "Integer32"
_HwVoPeerConfigShutDown_Object = MibTableColumn
hwVoPeerConfigShutDown = _HwVoPeerConfigShutDown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 9),
    _HwVoPeerConfigShutDown_Type()
)
hwVoPeerConfigShutDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigShutDown.setStatus("current")


class _HwVoPeerConfigVADSwitch_Type(Integer32):
    """Custom type hwVoPeerConfigVADSwitch based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwVoPeerConfigVADSwitch_Type.__name__ = "Integer32"
_HwVoPeerConfigVADSwitch_Object = MibTableColumn
hwVoPeerConfigVADSwitch = _HwVoPeerConfigVADSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 10),
    _HwVoPeerConfigVADSwitch_Type()
)
hwVoPeerConfigVADSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigVADSwitch.setStatus("current")


class _HwVoPeerConfigDtmfRelay_Type(Integer32):
    """Custom type hwVoPeerConfigDtmfRelay based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              12)
        )
    )
    namedValues = NamedValues(
        *(("h245Alphanumeric", 1),
          ("sip", 12),
          ("voice", 2))
    )


_HwVoPeerConfigDtmfRelay_Type.__name__ = "Integer32"
_HwVoPeerConfigDtmfRelay_Object = MibTableColumn
hwVoPeerConfigDtmfRelay = _HwVoPeerConfigDtmfRelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 11),
    _HwVoPeerConfigDtmfRelay_Type()
)
hwVoPeerConfigDtmfRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigDtmfRelay.setStatus("current")


class _HwVoPeerConfigFaxLevel_Type(Integer32):
    """Custom type hwVoPeerConfigFaxLevel based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 60),
    )


_HwVoPeerConfigFaxLevel_Type.__name__ = "Integer32"
_HwVoPeerConfigFaxLevel_Object = MibTableColumn
hwVoPeerConfigFaxLevel = _HwVoPeerConfigFaxLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 12),
    _HwVoPeerConfigFaxLevel_Type()
)
hwVoPeerConfigFaxLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigFaxLevel.setStatus("current")


class _HwVoPeerConfigFaxRate_Type(Integer32):
    """Custom type hwVoPeerConfigFaxRate based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disable", 5),
          ("r14400", 1),
          ("r2400", 2),
          ("r4800", 3),
          ("r9600", 4),
          ("voice", 6))
    )


_HwVoPeerConfigFaxRate_Type.__name__ = "Integer32"
_HwVoPeerConfigFaxRate_Object = MibTableColumn
hwVoPeerConfigFaxRate = _HwVoPeerConfigFaxRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 13),
    _HwVoPeerConfigFaxRate_Type()
)
hwVoPeerConfigFaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigFaxRate.setStatus("current")


class _HwVoPeerConfigFaxLocalTrainParam_Type(Integer32):
    """Custom type hwVoPeerConfigFaxLocalTrainParam based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwVoPeerConfigFaxLocalTrainParam_Type.__name__ = "Integer32"
_HwVoPeerConfigFaxLocalTrainParam_Object = MibTableColumn
hwVoPeerConfigFaxLocalTrainParam = _HwVoPeerConfigFaxLocalTrainParam_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 14),
    _HwVoPeerConfigFaxLocalTrainParam_Type()
)
hwVoPeerConfigFaxLocalTrainParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigFaxLocalTrainParam.setStatus("current")


class _HwVoPeerConfigFaxProtocol_Type(Integer32):
    """Custom type hwVoPeerConfigFaxProtocol based on Integer32"""
    defaultValue = 2

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
        *(("h323-t38", 5),
          ("nonstandard-compatible", 1),
          ("pcm", 3),
          ("sip-t38", 4),
          ("t38", 2))
    )


_HwVoPeerConfigFaxProtocol_Type.__name__ = "Integer32"
_HwVoPeerConfigFaxProtocol_Object = MibTableColumn
hwVoPeerConfigFaxProtocol = _HwVoPeerConfigFaxProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 15),
    _HwVoPeerConfigFaxProtocol_Type()
)
hwVoPeerConfigFaxProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigFaxProtocol.setStatus("current")


class _HwVoPeerConfigFaxT38HighRedunPackNumber_Type(Integer32):
    """Custom type hwVoPeerConfigFaxT38HighRedunPackNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HwVoPeerConfigFaxT38HighRedunPackNumber_Type.__name__ = "Integer32"
_HwVoPeerConfigFaxT38HighRedunPackNumber_Object = MibTableColumn
hwVoPeerConfigFaxT38HighRedunPackNumber = _HwVoPeerConfigFaxT38HighRedunPackNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 16),
    _HwVoPeerConfigFaxT38HighRedunPackNumber_Type()
)
hwVoPeerConfigFaxT38HighRedunPackNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigFaxT38HighRedunPackNumber.setStatus("current")


class _HwVoPeerConfigFaxT38LowRedunPackNumber_Type(Integer32):
    """Custom type hwVoPeerConfigFaxT38LowRedunPackNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_HwVoPeerConfigFaxT38LowRedunPackNumber_Type.__name__ = "Integer32"
_HwVoPeerConfigFaxT38LowRedunPackNumber_Object = MibTableColumn
hwVoPeerConfigFaxT38LowRedunPackNumber = _HwVoPeerConfigFaxT38LowRedunPackNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 17),
    _HwVoPeerConfigFaxT38LowRedunPackNumber_Type()
)
hwVoPeerConfigFaxT38LowRedunPackNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigFaxT38LowRedunPackNumber.setStatus("current")


class _HwVoPeerConfigFaxSendNSFSwitch_Type(Integer32):
    """Custom type hwVoPeerConfigFaxSendNSFSwitch based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwVoPeerConfigFaxSendNSFSwitch_Type.__name__ = "Integer32"
_HwVoPeerConfigFaxSendNSFSwitch_Object = MibTableColumn
hwVoPeerConfigFaxSendNSFSwitch = _HwVoPeerConfigFaxSendNSFSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 18),
    _HwVoPeerConfigFaxSendNSFSwitch_Type()
)
hwVoPeerConfigFaxSendNSFSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigFaxSendNSFSwitch.setStatus("current")


class _HwVoPeerConfigFaxSupportMode_Type(Integer32):
    """Custom type hwVoPeerConfigFaxSupportMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("rtp", 1),
          ("sip-udp", 4),
          ("vt", 2))
    )


_HwVoPeerConfigFaxSupportMode_Type.__name__ = "Integer32"
_HwVoPeerConfigFaxSupportMode_Object = MibTableColumn
hwVoPeerConfigFaxSupportMode = _HwVoPeerConfigFaxSupportMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 19),
    _HwVoPeerConfigFaxSupportMode_Type()
)
hwVoPeerConfigFaxSupportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigFaxSupportMode.setStatus("current")


class _HwVoPeerConfigFaxTrainMode_Type(Integer32):
    """Custom type hwVoPeerConfigFaxTrainMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("ppp", 2))
    )


_HwVoPeerConfigFaxTrainMode_Type.__name__ = "Integer32"
_HwVoPeerConfigFaxTrainMode_Object = MibTableColumn
hwVoPeerConfigFaxTrainMode = _HwVoPeerConfigFaxTrainMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 20),
    _HwVoPeerConfigFaxTrainMode_Type()
)
hwVoPeerConfigFaxTrainMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigFaxTrainMode.setStatus("current")


class _HwVoPeerConfigFaxRelay_Type(Integer32):
    """Custom type hwVoPeerConfigFaxRelay based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ecm", 1),
          ("noecm", 2))
    )


_HwVoPeerConfigFaxRelay_Type.__name__ = "Integer32"
_HwVoPeerConfigFaxRelay_Object = MibTableColumn
hwVoPeerConfigFaxRelay = _HwVoPeerConfigFaxRelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 21),
    _HwVoPeerConfigFaxRelay_Type()
)
hwVoPeerConfigFaxRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigFaxRelay.setStatus("current")
_HwVoPeerConfigRowStatus_Type = EntryStatus
_HwVoPeerConfigRowStatus_Object = MibTableColumn
hwVoPeerConfigRowStatus = _HwVoPeerConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 22),
    _HwVoPeerConfigRowStatus_Type()
)
hwVoPeerConfigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigRowStatus.setStatus("current")


class _HwVoPeerConfigFaxPassthroughMode_Type(Integer32):
    """Custom type hwVoPeerConfigFaxPassthroughMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("g711alaw", 1),
          ("g711ulaw", 3),
          ("unknown", 0))
    )


_HwVoPeerConfigFaxPassthroughMode_Type.__name__ = "Integer32"
_HwVoPeerConfigFaxPassthroughMode_Object = MibTableColumn
hwVoPeerConfigFaxPassthroughMode = _HwVoPeerConfigFaxPassthroughMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 23),
    _HwVoPeerConfigFaxPassthroughMode_Type()
)
hwVoPeerConfigFaxPassthroughMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigFaxPassthroughMode.setStatus("current")


class _HwVoPeerConfigPriority_Type(Integer32):
    """Custom type hwVoPeerConfigPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_HwVoPeerConfigPriority_Type.__name__ = "Integer32"
_HwVoPeerConfigPriority_Object = MibTableColumn
hwVoPeerConfigPriority = _HwVoPeerConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 24),
    _HwVoPeerConfigPriority_Type()
)
hwVoPeerConfigPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigPriority.setStatus("current")


class _HwVoPeerConfigAuthorizationLevel_Type(Integer32):
    """Custom type hwVoPeerConfigAuthorizationLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_HwVoPeerConfigAuthorizationLevel_Type.__name__ = "Integer32"
_HwVoPeerConfigAuthorizationLevel_Object = MibTableColumn
hwVoPeerConfigAuthorizationLevel = _HwVoPeerConfigAuthorizationLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 25),
    _HwVoPeerConfigAuthorizationLevel_Type()
)
hwVoPeerConfigAuthorizationLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigAuthorizationLevel.setStatus("current")


class _HwVoPeerConfigDescription_Type(OctetString):
    """Custom type hwVoPeerConfigDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwVoPeerConfigDescription_Type.__name__ = "OctetString"
_HwVoPeerConfigDescription_Object = MibTableColumn
hwVoPeerConfigDescription = _HwVoPeerConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 26),
    _HwVoPeerConfigDescription_Type()
)
hwVoPeerConfigDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigDescription.setStatus("current")


class _HwVoPeerConfigCallingNumberType_Type(Integer32):
    """Custom type hwVoPeerConfigCallingNumberType based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("abbreviated", 1),
          ("international", 2),
          ("national", 3),
          ("network", 4),
          ("reserved", 5),
          ("subscriber", 6),
          ("unknown", 7))
    )


_HwVoPeerConfigCallingNumberType_Type.__name__ = "Integer32"
_HwVoPeerConfigCallingNumberType_Object = MibTableColumn
hwVoPeerConfigCallingNumberType = _HwVoPeerConfigCallingNumberType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 27),
    _HwVoPeerConfigCallingNumberType_Type()
)
hwVoPeerConfigCallingNumberType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigCallingNumberType.setStatus("current")


class _HwVoPeerConfigCalledNumberType_Type(Integer32):
    """Custom type hwVoPeerConfigCalledNumberType based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("abbreviated", 1),
          ("international", 2),
          ("national", 3),
          ("network", 4),
          ("reserved", 5),
          ("subscriber", 6),
          ("unknown", 7))
    )


_HwVoPeerConfigCalledNumberType_Type.__name__ = "Integer32"
_HwVoPeerConfigCalledNumberType_Object = MibTableColumn
hwVoPeerConfigCalledNumberType = _HwVoPeerConfigCalledNumberType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 28),
    _HwVoPeerConfigCalledNumberType_Type()
)
hwVoPeerConfigCalledNumberType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigCalledNumberType.setStatus("current")


class _HwVoPeerConfigCallingNumberingPlan_Type(Integer32):
    """Custom type hwVoPeerConfigCallingNumberingPlan based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("isdn", 2),
          ("national", 3),
          ("private", 4),
          ("reserved", 5),
          ("telex", 6),
          ("unknown", 7))
    )


_HwVoPeerConfigCallingNumberingPlan_Type.__name__ = "Integer32"
_HwVoPeerConfigCallingNumberingPlan_Object = MibTableColumn
hwVoPeerConfigCallingNumberingPlan = _HwVoPeerConfigCallingNumberingPlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 29),
    _HwVoPeerConfigCallingNumberingPlan_Type()
)
hwVoPeerConfigCallingNumberingPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigCallingNumberingPlan.setStatus("current")


class _HwVoPeerConfigCalledNumberingPlan_Type(Integer32):
    """Custom type hwVoPeerConfigCalledNumberingPlan based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("isdn", 2),
          ("national", 3),
          ("private", 4),
          ("reserved", 5),
          ("telex", 6),
          ("unknown", 7))
    )


_HwVoPeerConfigCalledNumberingPlan_Type.__name__ = "Integer32"
_HwVoPeerConfigCalledNumberingPlan_Object = MibTableColumn
hwVoPeerConfigCalledNumberingPlan = _HwVoPeerConfigCalledNumberingPlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 30),
    _HwVoPeerConfigCalledNumberingPlan_Type()
)
hwVoPeerConfigCalledNumberingPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigCalledNumberingPlan.setStatus("current")


class _HwVoPeerConfigSelectStop_Type(Integer32):
    """Custom type hwVoPeerConfigSelectStop based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HwVoPeerConfigSelectStop_Type.__name__ = "Integer32"
_HwVoPeerConfigSelectStop_Object = MibTableColumn
hwVoPeerConfigSelectStop = _HwVoPeerConfigSelectStop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 31),
    _HwVoPeerConfigSelectStop_Type()
)
hwVoPeerConfigSelectStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigSelectStop.setStatus("current")


class _HwVoPeerConfigCallingNumSubstRule_Type(Integer32):
    """Custom type hwVoPeerConfigCallingNumSubstRule based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwVoPeerConfigCallingNumSubstRule_Type.__name__ = "Integer32"
_HwVoPeerConfigCallingNumSubstRule_Object = MibTableColumn
hwVoPeerConfigCallingNumSubstRule = _HwVoPeerConfigCallingNumSubstRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 32),
    _HwVoPeerConfigCallingNumSubstRule_Type()
)
hwVoPeerConfigCallingNumSubstRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigCallingNumSubstRule.setStatus("current")


class _HwVoPeerConfigCalledNumSubstRule_Type(Integer32):
    """Custom type hwVoPeerConfigCalledNumSubstRule based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwVoPeerConfigCalledNumSubstRule_Type.__name__ = "Integer32"
_HwVoPeerConfigCalledNumSubstRule_Object = MibTableColumn
hwVoPeerConfigCalledNumSubstRule = _HwVoPeerConfigCalledNumSubstRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 33),
    _HwVoPeerConfigCalledNumSubstRule_Type()
)
hwVoPeerConfigCalledNumSubstRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigCalledNumSubstRule.setStatus("current")


class _HwVoPeerConfigMaxCall_Type(Integer32):
    """Custom type hwVoPeerConfigMaxCall based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwVoPeerConfigMaxCall_Type.__name__ = "Integer32"
_HwVoPeerConfigMaxCall_Object = MibTableColumn
hwVoPeerConfigMaxCall = _HwVoPeerConfigMaxCall_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 1, 1, 34),
    _HwVoPeerConfigMaxCall_Type()
)
hwVoPeerConfigMaxCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigMaxCall.setStatus("current")
_HwVoPOTSPeerConfigTable_Object = MibTable
hwVoPOTSPeerConfigTable = _HwVoPOTSPeerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    hwVoPOTSPeerConfigTable.setStatus("current")
_HwVoPOTSPeerConfigEntry_Object = MibTableRow
hwVoPOTSPeerConfigEntry = _HwVoPOTSPeerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 2, 1)
)
hwVoPOTSPeerConfigEntry.setIndexNames(
    (0, "HUAWEI-VO-DIAL-CONTROL-MIB", "hwVoPOTSPeerConfigIndex"),
)
if mibBuilder.loadTexts:
    hwVoPOTSPeerConfigEntry.setStatus("current")


class _HwVoPOTSPeerConfigIndex_Type(Integer32):
    """Custom type hwVoPOTSPeerConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwVoPOTSPeerConfigIndex_Type.__name__ = "Integer32"
_HwVoPOTSPeerConfigIndex_Object = MibTableColumn
hwVoPOTSPeerConfigIndex = _HwVoPOTSPeerConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 2, 1, 1),
    _HwVoPOTSPeerConfigIndex_Type()
)
hwVoPOTSPeerConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoPOTSPeerConfigIndex.setStatus("current")


class _HwVoPOTSPeerConfigCancelTruncateEnable_Type(Integer32):
    """Custom type hwVoPOTSPeerConfigCancelTruncateEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwVoPOTSPeerConfigCancelTruncateEnable_Type.__name__ = "Integer32"
_HwVoPOTSPeerConfigCancelTruncateEnable_Object = MibTableColumn
hwVoPOTSPeerConfigCancelTruncateEnable = _HwVoPOTSPeerConfigCancelTruncateEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 2, 1, 2),
    _HwVoPOTSPeerConfigCancelTruncateEnable_Type()
)
hwVoPOTSPeerConfigCancelTruncateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPOTSPeerConfigCancelTruncateEnable.setStatus("deprecated")


class _HwVoPOTSPeerConfigPrefix_Type(OctetString):
    """Custom type hwVoPOTSPeerConfigPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwVoPOTSPeerConfigPrefix_Type.__name__ = "OctetString"
_HwVoPOTSPeerConfigPrefix_Object = MibTableColumn
hwVoPOTSPeerConfigPrefix = _HwVoPOTSPeerConfigPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 2, 1, 3),
    _HwVoPOTSPeerConfigPrefix_Type()
)
hwVoPOTSPeerConfigPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPOTSPeerConfigPrefix.setStatus("current")


class _HwVoPOTSPeerConfigPort_Type(OctetString):
    """Custom type hwVoPOTSPeerConfigPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_HwVoPOTSPeerConfigPort_Type.__name__ = "OctetString"
_HwVoPOTSPeerConfigPort_Object = MibTableColumn
hwVoPOTSPeerConfigPort = _HwVoPOTSPeerConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 2, 1, 4),
    _HwVoPOTSPeerConfigPort_Type()
)
hwVoPOTSPeerConfigPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPOTSPeerConfigPort.setStatus("current")


class _HwVoPOTSPeerConfigSendNumber_Type(Integer32):
    """Custom type hwVoPOTSPeerConfigSendNumber based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 31),
    )


_HwVoPOTSPeerConfigSendNumber_Type.__name__ = "Integer32"
_HwVoPOTSPeerConfigSendNumber_Object = MibTableColumn
hwVoPOTSPeerConfigSendNumber = _HwVoPOTSPeerConfigSendNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 2, 1, 5),
    _HwVoPOTSPeerConfigSendNumber_Type()
)
hwVoPOTSPeerConfigSendNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPOTSPeerConfigSendNumber.setStatus("current")
_HwVoVoIPPeerConfigTable_Object = MibTable
hwVoVoIPPeerConfigTable = _HwVoVoIPPeerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 3)
)
if mibBuilder.loadTexts:
    hwVoVoIPPeerConfigTable.setStatus("current")
_HwVoVoIPPeerConfigEntry_Object = MibTableRow
hwVoVoIPPeerConfigEntry = _HwVoVoIPPeerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 3, 1)
)
hwVoVoIPPeerConfigEntry.setIndexNames(
    (0, "HUAWEI-VO-DIAL-CONTROL-MIB", "hwVoVoIPPeerConfigIndex"),
)
if mibBuilder.loadTexts:
    hwVoVoIPPeerConfigEntry.setStatus("current")


class _HwVoVoIPPeerConfigIndex_Type(Integer32):
    """Custom type hwVoVoIPPeerConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwVoVoIPPeerConfigIndex_Type.__name__ = "Integer32"
_HwVoVoIPPeerConfigIndex_Object = MibTableColumn
hwVoVoIPPeerConfigIndex = _HwVoVoIPPeerConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 3, 1, 1),
    _HwVoVoIPPeerConfigIndex_Type()
)
hwVoVoIPPeerConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoVoIPPeerConfigIndex.setStatus("current")


class _HwVoVoIPPeerConfigSessionTargetType_Type(Integer32):
    """Custom type hwVoVoIPPeerConfigSessionTargetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ras", 2),
          ("unknown", 3))
    )


_HwVoVoIPPeerConfigSessionTargetType_Type.__name__ = "Integer32"
_HwVoVoIPPeerConfigSessionTargetType_Object = MibTableColumn
hwVoVoIPPeerConfigSessionTargetType = _HwVoVoIPPeerConfigSessionTargetType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 3, 1, 2),
    _HwVoVoIPPeerConfigSessionTargetType_Type()
)
hwVoVoIPPeerConfigSessionTargetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoVoIPPeerConfigSessionTargetType.setStatus("current")
_HwVoVoIPPeerConfigSessionTarget_Type = IpAddress
_HwVoVoIPPeerConfigSessionTarget_Object = MibTableColumn
hwVoVoIPPeerConfigSessionTarget = _HwVoVoIPPeerConfigSessionTarget_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 3, 1, 3),
    _HwVoVoIPPeerConfigSessionTarget_Type()
)
hwVoVoIPPeerConfigSessionTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoVoIPPeerConfigSessionTarget.setStatus("current")


class _HwVoVoIPPeerConfigFastSwitch_Type(Integer32):
    """Custom type hwVoVoIPPeerConfigFastSwitch based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwVoVoIPPeerConfigFastSwitch_Type.__name__ = "Integer32"
_HwVoVoIPPeerConfigFastSwitch_Object = MibTableColumn
hwVoVoIPPeerConfigFastSwitch = _HwVoVoIPPeerConfigFastSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 3, 1, 4),
    _HwVoVoIPPeerConfigFastSwitch_Type()
)
hwVoVoIPPeerConfigFastSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoVoIPPeerConfigFastSwitch.setStatus("current")


class _HwVoVoIPPeerConfigTunnelSwitch_Type(Integer32):
    """Custom type hwVoVoIPPeerConfigTunnelSwitch based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwVoVoIPPeerConfigTunnelSwitch_Type.__name__ = "Integer32"
_HwVoVoIPPeerConfigTunnelSwitch_Object = MibTableColumn
hwVoVoIPPeerConfigTunnelSwitch = _HwVoVoIPPeerConfigTunnelSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 3, 1, 5),
    _HwVoVoIPPeerConfigTunnelSwitch_Type()
)
hwVoVoIPPeerConfigTunnelSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoVoIPPeerConfigTunnelSwitch.setStatus("current")


class _HwVoVoIPPeerConfigTeachPrefix_Type(OctetString):
    """Custom type hwVoVoIPPeerConfigTeachPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwVoVoIPPeerConfigTeachPrefix_Type.__name__ = "OctetString"
_HwVoVoIPPeerConfigTeachPrefix_Object = MibTableColumn
hwVoVoIPPeerConfigTeachPrefix = _HwVoVoIPPeerConfigTeachPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 3, 1, 6),
    _HwVoVoIPPeerConfigTeachPrefix_Type()
)
hwVoVoIPPeerConfigTeachPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoVoIPPeerConfigTeachPrefix.setStatus("current")


class _HwVoVoIPPeerConfigSendRing_Type(Integer32):
    """Custom type hwVoVoIPPeerConfigSendRing based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwVoVoIPPeerConfigSendRing_Type.__name__ = "Integer32"
_HwVoVoIPPeerConfigSendRing_Object = MibTableColumn
hwVoVoIPPeerConfigSendRing = _HwVoVoIPPeerConfigSendRing_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 3, 1, 7),
    _HwVoVoIPPeerConfigSendRing_Type()
)
hwVoVoIPPeerConfigSendRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoVoIPPeerConfigSendRing.setStatus("current")
_HwVoPeerDefaultConfigObjects_ObjectIdentity = ObjectIdentity
hwVoPeerDefaultConfigObjects = _HwVoPeerDefaultConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 4)
)


class _HwVoPeerDefaultConfigCancelTrun_Type(Integer32):
    """Custom type hwVoPeerDefaultConfigCancelTrun based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwVoPeerDefaultConfigCancelTrun_Type.__name__ = "Integer32"
_HwVoPeerDefaultConfigCancelTrun_Object = MibScalar
hwVoPeerDefaultConfigCancelTrun = _HwVoPeerDefaultConfigCancelTrun_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 4, 1),
    _HwVoPeerDefaultConfigCancelTrun_Type()
)
hwVoPeerDefaultConfigCancelTrun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerDefaultConfigCancelTrun.setStatus("deprecated")


class _HwVoPeerDefaultConfig1STCodecLevel_Type(Integer32):
    """Custom type hwVoPeerDefaultConfig1STCodecLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("g711alaw", 1),
          ("g711ulaw", 4),
          ("g723r53", 3),
          ("g723r63", 2),
          ("g729a", 5),
          ("g729r8", 0))
    )


_HwVoPeerDefaultConfig1STCodecLevel_Type.__name__ = "Integer32"
_HwVoPeerDefaultConfig1STCodecLevel_Object = MibScalar
hwVoPeerDefaultConfig1STCodecLevel = _HwVoPeerDefaultConfig1STCodecLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 4, 2),
    _HwVoPeerDefaultConfig1STCodecLevel_Type()
)
hwVoPeerDefaultConfig1STCodecLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerDefaultConfig1STCodecLevel.setStatus("current")


class _HwVoPeerDefaultConfig2NDCodecLevel_Type(Integer32):
    """Custom type hwVoPeerDefaultConfig2NDCodecLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("g711alaw", 1),
          ("g711ulaw", 4),
          ("g723r53", 3),
          ("g723r63", 2),
          ("g729a", 5),
          ("g729r8", 0))
    )


_HwVoPeerDefaultConfig2NDCodecLevel_Type.__name__ = "Integer32"
_HwVoPeerDefaultConfig2NDCodecLevel_Object = MibScalar
hwVoPeerDefaultConfig2NDCodecLevel = _HwVoPeerDefaultConfig2NDCodecLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 4, 3),
    _HwVoPeerDefaultConfig2NDCodecLevel_Type()
)
hwVoPeerDefaultConfig2NDCodecLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerDefaultConfig2NDCodecLevel.setStatus("current")


class _HwVoPeerDefaultConfig3RDCodecLevel_Type(Integer32):
    """Custom type hwVoPeerDefaultConfig3RDCodecLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("g711alaw", 1),
          ("g711ulaw", 4),
          ("g723r53", 3),
          ("g723r63", 2),
          ("g729a", 5),
          ("g729r8", 0))
    )


_HwVoPeerDefaultConfig3RDCodecLevel_Type.__name__ = "Integer32"
_HwVoPeerDefaultConfig3RDCodecLevel_Object = MibScalar
hwVoPeerDefaultConfig3RDCodecLevel = _HwVoPeerDefaultConfig3RDCodecLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 4, 4),
    _HwVoPeerDefaultConfig3RDCodecLevel_Type()
)
hwVoPeerDefaultConfig3RDCodecLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerDefaultConfig3RDCodecLevel.setStatus("current")


class _HwVoPeerDefaultConfig4THCodecLevel_Type(Integer32):
    """Custom type hwVoPeerDefaultConfig4THCodecLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("g711alaw", 1),
          ("g711ulaw", 4),
          ("g723r53", 3),
          ("g723r63", 2),
          ("g729a", 5),
          ("g729r8", 0))
    )


_HwVoPeerDefaultConfig4THCodecLevel_Type.__name__ = "Integer32"
_HwVoPeerDefaultConfig4THCodecLevel_Object = MibScalar
hwVoPeerDefaultConfig4THCodecLevel = _HwVoPeerDefaultConfig4THCodecLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 4, 5),
    _HwVoPeerDefaultConfig4THCodecLevel_Type()
)
hwVoPeerDefaultConfig4THCodecLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerDefaultConfig4THCodecLevel.setStatus("current")


class _HwVoPeerDefaultConfigVADOn_Type(Integer32):
    """Custom type hwVoPeerDefaultConfigVADOn based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwVoPeerDefaultConfigVADOn_Type.__name__ = "Integer32"
_HwVoPeerDefaultConfigVADOn_Object = MibScalar
hwVoPeerDefaultConfigVADOn = _HwVoPeerDefaultConfigVADOn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 4, 6),
    _HwVoPeerDefaultConfigVADOn_Type()
)
hwVoPeerDefaultConfigVADOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerDefaultConfigVADOn.setStatus("current")


class _HwVoPeerDefaultConfigFaxTransmitLevel_Type(Integer32):
    """Custom type hwVoPeerDefaultConfigFaxTransmitLevel based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 60),
    )


_HwVoPeerDefaultConfigFaxTransmitLevel_Type.__name__ = "Integer32"
_HwVoPeerDefaultConfigFaxTransmitLevel_Object = MibScalar
hwVoPeerDefaultConfigFaxTransmitLevel = _HwVoPeerDefaultConfigFaxTransmitLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 4, 7),
    _HwVoPeerDefaultConfigFaxTransmitLevel_Type()
)
hwVoPeerDefaultConfigFaxTransmitLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerDefaultConfigFaxTransmitLevel.setStatus("current")


class _HwVoPeerDefaultConfigFaxLocalTrain_Type(Integer32):
    """Custom type hwVoPeerDefaultConfigFaxLocalTrain based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwVoPeerDefaultConfigFaxLocalTrain_Type.__name__ = "Integer32"
_HwVoPeerDefaultConfigFaxLocalTrain_Object = MibScalar
hwVoPeerDefaultConfigFaxLocalTrain = _HwVoPeerDefaultConfigFaxLocalTrain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 4, 8),
    _HwVoPeerDefaultConfigFaxLocalTrain_Type()
)
hwVoPeerDefaultConfigFaxLocalTrain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerDefaultConfigFaxLocalTrain.setStatus("current")


class _HwVoPeerDefaultConfigFaxProtocol_Type(Integer32):
    """Custom type hwVoPeerDefaultConfigFaxProtocol based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("h323-t38", 3),
          ("nonstandard-compatible", 1),
          ("pcm-alaw", 5),
          ("pcm-ulaw", 6),
          ("sip-t38", 4),
          ("t38", 2))
    )


_HwVoPeerDefaultConfigFaxProtocol_Type.__name__ = "Integer32"
_HwVoPeerDefaultConfigFaxProtocol_Object = MibScalar
hwVoPeerDefaultConfigFaxProtocol = _HwVoPeerDefaultConfigFaxProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 4, 9),
    _HwVoPeerDefaultConfigFaxProtocol_Type()
)
hwVoPeerDefaultConfigFaxProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerDefaultConfigFaxProtocol.setStatus("current")


class _HwVoPeerDefaultConfigFaxHSRedundancy_Type(Integer32):
    """Custom type hwVoPeerDefaultConfigFaxHSRedundancy based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HwVoPeerDefaultConfigFaxHSRedundancy_Type.__name__ = "Integer32"
_HwVoPeerDefaultConfigFaxHSRedundancy_Object = MibScalar
hwVoPeerDefaultConfigFaxHSRedundancy = _HwVoPeerDefaultConfigFaxHSRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 4, 10),
    _HwVoPeerDefaultConfigFaxHSRedundancy_Type()
)
hwVoPeerDefaultConfigFaxHSRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerDefaultConfigFaxHSRedundancy.setStatus("current")


class _HwVoPeerDefaultConfigFaxLSRedundancy_Type(Integer32):
    """Custom type hwVoPeerDefaultConfigFaxLSRedundancy based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HwVoPeerDefaultConfigFaxLSRedundancy_Type.__name__ = "Integer32"
_HwVoPeerDefaultConfigFaxLSRedundancy_Object = MibScalar
hwVoPeerDefaultConfigFaxLSRedundancy = _HwVoPeerDefaultConfigFaxLSRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 4, 11),
    _HwVoPeerDefaultConfigFaxLSRedundancy_Type()
)
hwVoPeerDefaultConfigFaxLSRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerDefaultConfigFaxLSRedundancy.setStatus("current")


class _HwVoPeerDefaultConfigFaxBaudrate_Type(Integer32):
    """Custom type hwVoPeerDefaultConfigFaxBaudrate based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              5,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("b14400", 7),
          ("b2400", 2),
          ("b4800", 3),
          ("b9600", 5),
          ("disable", 0),
          ("voice", 8))
    )


_HwVoPeerDefaultConfigFaxBaudrate_Type.__name__ = "Integer32"
_HwVoPeerDefaultConfigFaxBaudrate_Object = MibScalar
hwVoPeerDefaultConfigFaxBaudrate = _HwVoPeerDefaultConfigFaxBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 4, 12),
    _HwVoPeerDefaultConfigFaxBaudrate_Type()
)
hwVoPeerDefaultConfigFaxBaudrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerDefaultConfigFaxBaudrate.setStatus("current")


class _HwVoPeerDefaultConfigFaxNSF_Type(Integer32):
    """Custom type hwVoPeerDefaultConfigFaxNSF based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwVoPeerDefaultConfigFaxNSF_Type.__name__ = "Integer32"
_HwVoPeerDefaultConfigFaxNSF_Object = MibScalar
hwVoPeerDefaultConfigFaxNSF = _HwVoPeerDefaultConfigFaxNSF_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 4, 13),
    _HwVoPeerDefaultConfigFaxNSF_Type()
)
hwVoPeerDefaultConfigFaxNSF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerDefaultConfigFaxNSF.setStatus("current")


class _HwVoPeerDefaultConfigFaxSupportMode_Type(Integer32):
    """Custom type hwVoPeerDefaultConfigFaxSupportMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rtp", 1),
          ("vt", 2))
    )


_HwVoPeerDefaultConfigFaxSupportMode_Type.__name__ = "Integer32"
_HwVoPeerDefaultConfigFaxSupportMode_Object = MibScalar
hwVoPeerDefaultConfigFaxSupportMode = _HwVoPeerDefaultConfigFaxSupportMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 4, 14),
    _HwVoPeerDefaultConfigFaxSupportMode_Type()
)
hwVoPeerDefaultConfigFaxSupportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerDefaultConfigFaxSupportMode.setStatus("current")


class _HwVoPeerDefaultConfigFaxTrainMode_Type(Integer32):
    """Custom type hwVoPeerDefaultConfigFaxTrainMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("ppp", 1))
    )


_HwVoPeerDefaultConfigFaxTrainMode_Type.__name__ = "Integer32"
_HwVoPeerDefaultConfigFaxTrainMode_Object = MibScalar
hwVoPeerDefaultConfigFaxTrainMode = _HwVoPeerDefaultConfigFaxTrainMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 4, 15),
    _HwVoPeerDefaultConfigFaxTrainMode_Type()
)
hwVoPeerDefaultConfigFaxTrainMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerDefaultConfigFaxTrainMode.setStatus("current")


class _HwVoPeerDefaultConfigFaxECM_Type(Integer32):
    """Custom type hwVoPeerDefaultConfigFaxECM based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwVoPeerDefaultConfigFaxECM_Type.__name__ = "Integer32"
_HwVoPeerDefaultConfigFaxECM_Object = MibScalar
hwVoPeerDefaultConfigFaxECM = _HwVoPeerDefaultConfigFaxECM_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 4, 16),
    _HwVoPeerDefaultConfigFaxECM_Type()
)
hwVoPeerDefaultConfigFaxECM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerDefaultConfigFaxECM.setStatus("current")
_HwVoPeerConfigCallerPermitNumTable_Object = MibTable
hwVoPeerConfigCallerPermitNumTable = _HwVoPeerConfigCallerPermitNumTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 5)
)
if mibBuilder.loadTexts:
    hwVoPeerConfigCallerPermitNumTable.setStatus("current")
_HwVoPeerConfigCallerPermitNumEntry_Object = MibTableRow
hwVoPeerConfigCallerPermitNumEntry = _HwVoPeerConfigCallerPermitNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 5, 1)
)
hwVoPeerConfigCallerPermitNumEntry.setIndexNames(
    (0, "HUAWEI-VO-DIAL-CONTROL-MIB", "hwVoPeerConfigIndex"),
    (0, "HUAWEI-VO-DIAL-CONTROL-MIB", "hwVoPeerConfigCallerPermitNum"),
)
if mibBuilder.loadTexts:
    hwVoPeerConfigCallerPermitNumEntry.setStatus("current")


class _HwVoPeerConfigCallerPermitNum_Type(OctetString):
    """Custom type hwVoPeerConfigCallerPermitNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwVoPeerConfigCallerPermitNum_Type.__name__ = "OctetString"
_HwVoPeerConfigCallerPermitNum_Object = MibTableColumn
hwVoPeerConfigCallerPermitNum = _HwVoPeerConfigCallerPermitNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 5, 1, 1),
    _HwVoPeerConfigCallerPermitNum_Type()
)
hwVoPeerConfigCallerPermitNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigCallerPermitNum.setStatus("current")
_HwVoPeerConfigCallerPermitNumRowStatus_Type = EntryStatus
_HwVoPeerConfigCallerPermitNumRowStatus_Object = MibTableColumn
hwVoPeerConfigCallerPermitNumRowStatus = _HwVoPeerConfigCallerPermitNumRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 5, 1, 5, 1, 2),
    _HwVoPeerConfigCallerPermitNumRowStatus_Type()
)
hwVoPeerConfigCallerPermitNumRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoPeerConfigCallerPermitNumRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-VO-DIAL-CONTROL-MIB",
    **{"EntryStatus": EntryStatus,
       "hwVoiceDialControlMIB": hwVoiceDialControlMIB,
       "hwVoPeerObjects": hwVoPeerObjects,
       "hwVoPeerCommonConfigTable": hwVoPeerCommonConfigTable,
       "hwVoPeerCommonConfigEntry": hwVoPeerCommonConfigEntry,
       "hwVoPeerConfigIndex": hwVoPeerConfigIndex,
       "hwVoPeerConfigType": hwVoPeerConfigType,
       "hwVoPeerConfigDesPattern": hwVoPeerConfigDesPattern,
       "hwVoPeerConfigCodec1st": hwVoPeerConfigCodec1st,
       "hwVoPeerConfigCodec2st": hwVoPeerConfigCodec2st,
       "hwVoPeerConfigCodec3st": hwVoPeerConfigCodec3st,
       "hwVoPeerConfigCodec4st": hwVoPeerConfigCodec4st,
       "hwVoPeerConfigIpPreced": hwVoPeerConfigIpPreced,
       "hwVoPeerConfigShutDown": hwVoPeerConfigShutDown,
       "hwVoPeerConfigVADSwitch": hwVoPeerConfigVADSwitch,
       "hwVoPeerConfigDtmfRelay": hwVoPeerConfigDtmfRelay,
       "hwVoPeerConfigFaxLevel": hwVoPeerConfigFaxLevel,
       "hwVoPeerConfigFaxRate": hwVoPeerConfigFaxRate,
       "hwVoPeerConfigFaxLocalTrainParam": hwVoPeerConfigFaxLocalTrainParam,
       "hwVoPeerConfigFaxProtocol": hwVoPeerConfigFaxProtocol,
       "hwVoPeerConfigFaxT38HighRedunPackNumber": hwVoPeerConfigFaxT38HighRedunPackNumber,
       "hwVoPeerConfigFaxT38LowRedunPackNumber": hwVoPeerConfigFaxT38LowRedunPackNumber,
       "hwVoPeerConfigFaxSendNSFSwitch": hwVoPeerConfigFaxSendNSFSwitch,
       "hwVoPeerConfigFaxSupportMode": hwVoPeerConfigFaxSupportMode,
       "hwVoPeerConfigFaxTrainMode": hwVoPeerConfigFaxTrainMode,
       "hwVoPeerConfigFaxRelay": hwVoPeerConfigFaxRelay,
       "hwVoPeerConfigRowStatus": hwVoPeerConfigRowStatus,
       "hwVoPeerConfigFaxPassthroughMode": hwVoPeerConfigFaxPassthroughMode,
       "hwVoPeerConfigPriority": hwVoPeerConfigPriority,
       "hwVoPeerConfigAuthorizationLevel": hwVoPeerConfigAuthorizationLevel,
       "hwVoPeerConfigDescription": hwVoPeerConfigDescription,
       "hwVoPeerConfigCallingNumberType": hwVoPeerConfigCallingNumberType,
       "hwVoPeerConfigCalledNumberType": hwVoPeerConfigCalledNumberType,
       "hwVoPeerConfigCallingNumberingPlan": hwVoPeerConfigCallingNumberingPlan,
       "hwVoPeerConfigCalledNumberingPlan": hwVoPeerConfigCalledNumberingPlan,
       "hwVoPeerConfigSelectStop": hwVoPeerConfigSelectStop,
       "hwVoPeerConfigCallingNumSubstRule": hwVoPeerConfigCallingNumSubstRule,
       "hwVoPeerConfigCalledNumSubstRule": hwVoPeerConfigCalledNumSubstRule,
       "hwVoPeerConfigMaxCall": hwVoPeerConfigMaxCall,
       "hwVoPOTSPeerConfigTable": hwVoPOTSPeerConfigTable,
       "hwVoPOTSPeerConfigEntry": hwVoPOTSPeerConfigEntry,
       "hwVoPOTSPeerConfigIndex": hwVoPOTSPeerConfigIndex,
       "hwVoPOTSPeerConfigCancelTruncateEnable": hwVoPOTSPeerConfigCancelTruncateEnable,
       "hwVoPOTSPeerConfigPrefix": hwVoPOTSPeerConfigPrefix,
       "hwVoPOTSPeerConfigPort": hwVoPOTSPeerConfigPort,
       "hwVoPOTSPeerConfigSendNumber": hwVoPOTSPeerConfigSendNumber,
       "hwVoVoIPPeerConfigTable": hwVoVoIPPeerConfigTable,
       "hwVoVoIPPeerConfigEntry": hwVoVoIPPeerConfigEntry,
       "hwVoVoIPPeerConfigIndex": hwVoVoIPPeerConfigIndex,
       "hwVoVoIPPeerConfigSessionTargetType": hwVoVoIPPeerConfigSessionTargetType,
       "hwVoVoIPPeerConfigSessionTarget": hwVoVoIPPeerConfigSessionTarget,
       "hwVoVoIPPeerConfigFastSwitch": hwVoVoIPPeerConfigFastSwitch,
       "hwVoVoIPPeerConfigTunnelSwitch": hwVoVoIPPeerConfigTunnelSwitch,
       "hwVoVoIPPeerConfigTeachPrefix": hwVoVoIPPeerConfigTeachPrefix,
       "hwVoVoIPPeerConfigSendRing": hwVoVoIPPeerConfigSendRing,
       "hwVoPeerDefaultConfigObjects": hwVoPeerDefaultConfigObjects,
       "hwVoPeerDefaultConfigCancelTrun": hwVoPeerDefaultConfigCancelTrun,
       "hwVoPeerDefaultConfig1STCodecLevel": hwVoPeerDefaultConfig1STCodecLevel,
       "hwVoPeerDefaultConfig2NDCodecLevel": hwVoPeerDefaultConfig2NDCodecLevel,
       "hwVoPeerDefaultConfig3RDCodecLevel": hwVoPeerDefaultConfig3RDCodecLevel,
       "hwVoPeerDefaultConfig4THCodecLevel": hwVoPeerDefaultConfig4THCodecLevel,
       "hwVoPeerDefaultConfigVADOn": hwVoPeerDefaultConfigVADOn,
       "hwVoPeerDefaultConfigFaxTransmitLevel": hwVoPeerDefaultConfigFaxTransmitLevel,
       "hwVoPeerDefaultConfigFaxLocalTrain": hwVoPeerDefaultConfigFaxLocalTrain,
       "hwVoPeerDefaultConfigFaxProtocol": hwVoPeerDefaultConfigFaxProtocol,
       "hwVoPeerDefaultConfigFaxHSRedundancy": hwVoPeerDefaultConfigFaxHSRedundancy,
       "hwVoPeerDefaultConfigFaxLSRedundancy": hwVoPeerDefaultConfigFaxLSRedundancy,
       "hwVoPeerDefaultConfigFaxBaudrate": hwVoPeerDefaultConfigFaxBaudrate,
       "hwVoPeerDefaultConfigFaxNSF": hwVoPeerDefaultConfigFaxNSF,
       "hwVoPeerDefaultConfigFaxSupportMode": hwVoPeerDefaultConfigFaxSupportMode,
       "hwVoPeerDefaultConfigFaxTrainMode": hwVoPeerDefaultConfigFaxTrainMode,
       "hwVoPeerDefaultConfigFaxECM": hwVoPeerDefaultConfigFaxECM,
       "hwVoPeerConfigCallerPermitNumTable": hwVoPeerConfigCallerPermitNumTable,
       "hwVoPeerConfigCallerPermitNumEntry": hwVoPeerConfigCallerPermitNumEntry,
       "hwVoPeerConfigCallerPermitNum": hwVoPeerConfigCallerPermitNum,
       "hwVoPeerConfigCallerPermitNumRowStatus": hwVoPeerConfigCallerPermitNumRowStatus}
)
