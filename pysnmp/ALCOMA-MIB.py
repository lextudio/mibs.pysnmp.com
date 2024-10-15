# SNMP MIB module (ALCOMA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCOMA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:42 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Alcoma_ObjectIdentity = ObjectIdentity
alcoma = _Alcoma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0)
)
_GeneralOFF_ObjectIdentity = ObjectIdentity
generalOFF = _GeneralOFF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0, 1)
)
_GeneralOK_ObjectIdentity = ObjectIdentity
generalOK = _GeneralOK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0, 2)
)
_GeneralWAR_ObjectIdentity = ObjectIdentity
generalWAR = _GeneralWAR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0, 3)
)
_GeneralERR_ObjectIdentity = ObjectIdentity
generalERR = _GeneralERR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0, 4)
)
_ReceiverLowAlarmOn_ObjectIdentity = ObjectIdentity
receiverLowAlarmOn = _ReceiverLowAlarmOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0, 5)
)
_ReceiverLowAlarmOff_ObjectIdentity = ObjectIdentity
receiverLowAlarmOff = _ReceiverLowAlarmOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0, 6)
)
_TransmitterLowAlarmOn_ObjectIdentity = ObjectIdentity
transmitterLowAlarmOn = _TransmitterLowAlarmOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0, 7)
)
_TransmitterLowAlarmOff_ObjectIdentity = ObjectIdentity
transmitterLowAlarmOff = _TransmitterLowAlarmOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0, 8)
)
_SignalQualityAlarmOn_ObjectIdentity = ObjectIdentity
signalQualityAlarmOn = _SignalQualityAlarmOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0, 9)
)
_SignalQualityAlarmOff_ObjectIdentity = ObjectIdentity
signalQualityAlarmOff = _SignalQualityAlarmOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0, 10)
)
_Ber6EAlarmOn_ObjectIdentity = ObjectIdentity
ber6EAlarmOn = _Ber6EAlarmOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0, 11)
)
_Ber6EAlarmOff_ObjectIdentity = ObjectIdentity
ber6EAlarmOff = _Ber6EAlarmOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0, 12)
)
_Ber4EAlarmOn_ObjectIdentity = ObjectIdentity
ber4EAlarmOn = _Ber4EAlarmOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0, 13)
)
_Ber4EAlarmOff_ObjectIdentity = ObjectIdentity
ber4EAlarmOff = _Ber4EAlarmOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0, 14)
)
_InputSupplyAlarmOn_ObjectIdentity = ObjectIdentity
inputSupplyAlarmOn = _InputSupplyAlarmOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0, 15)
)
_InputSupplyAlarmOff_ObjectIdentity = ObjectIdentity
inputSupplyAlarmOff = _InputSupplyAlarmOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0, 16)
)
_AisFromLineAlarmOn_ObjectIdentity = ObjectIdentity
aisFromLineAlarmOn = _AisFromLineAlarmOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0, 17)
)
_AisFromLineAlarmOff_ObjectIdentity = ObjectIdentity
aisFromLineAlarmOff = _AisFromLineAlarmOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0, 18)
)
_AisToLineAlarmOn_ObjectIdentity = ObjectIdentity
aisToLineAlarmOn = _AisToLineAlarmOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0, 19)
)
_AisToLineAlarmOff_ObjectIdentity = ObjectIdentity
aisToLineAlarmOff = _AisToLineAlarmOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0, 20)
)
_AisToPdhAlarmOn_ObjectIdentity = ObjectIdentity
aisToPdhAlarmOn = _AisToPdhAlarmOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0, 21)
)
_AisToPdhAlarmOff_ObjectIdentity = ObjectIdentity
aisToPdhAlarmOff = _AisToPdhAlarmOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0, 22)
)
_LossAtLineAlarmOn_ObjectIdentity = ObjectIdentity
lossAtLineAlarmOn = _LossAtLineAlarmOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0, 23)
)
_LossAtLineAlarmOff_ObjectIdentity = ObjectIdentity
lossAtLineAlarmOff = _LossAtLineAlarmOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0, 24)
)
_LossAtPdhAlarmOn_ObjectIdentity = ObjectIdentity
lossAtPdhAlarmOn = _LossAtPdhAlarmOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0, 25)
)
_LossAtPdhAlarmOff_ObjectIdentity = ObjectIdentity
lossAtPdhAlarmOff = _LossAtPdhAlarmOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0, 26)
)
_LossAtFrameAlarmOn_ObjectIdentity = ObjectIdentity
lossAtFrameAlarmOn = _LossAtFrameAlarmOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0, 27)
)
_LossAtFrameAlarmOff_ObjectIdentity = ObjectIdentity
lossAtFrameAlarmOff = _LossAtFrameAlarmOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 0, 28)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1)
)
_AlRADIO_RELAY_LINK_ObjectIdentity = ObjectIdentity
alRADIO_RELAY_LINK = _AlRADIO_RELAY_LINK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1)
)
_AlStatusLED_ObjectIdentity = ObjectIdentity
alStatusLED = _AlStatusLED_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 1)
)


class _AlEHW_Type(Integer32):
    """Custom type alEHW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlEHW_Type.__name__ = "Integer32"
_AlEHW_Object = MibScalar
alEHW = _AlEHW_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 1, 1),
    _AlEHW_Type()
)
alEHW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alEHW.setStatus("mandatory")


class _AlESR_Type(Integer32):
    """Custom type alESR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlESR_Type.__name__ = "Integer32"
_AlESR_Object = MibScalar
alESR = _AlESR_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 1, 2),
    _AlESR_Type()
)
alESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alESR.setStatus("mandatory")


class _AlESL_Type(Integer32):
    """Custom type alESL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlESL_Type.__name__ = "Integer32"
_AlESL_Object = MibScalar
alESL = _AlESL_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 1, 3),
    _AlESL_Type()
)
alESL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alESL.setStatus("mandatory")


class _AlCA_Type(Integer32):
    """Custom type alCA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlCA_Type.__name__ = "Integer32"
_AlCA_Object = MibScalar
alCA = _AlCA_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 1, 4),
    _AlCA_Type()
)
alCA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alCA.setStatus("mandatory")
_Local_station_ObjectIdentity = ObjectIdentity
local_station = _Local_station_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2)
)
_AlL_General_ObjectIdentity = ObjectIdentity
alL_General = _AlL_General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 1)
)


class _AlLSupervisor_Type(Integer32):
    """Custom type alLSupervisor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("alcoma", 5),
          ("local", 2),
          ("network", 3),
          ("none", 0),
          ("offline", -1),
          ("service", 4),
          ("terminal", 1))
    )


_AlLSupervisor_Type.__name__ = "Integer32"
_AlLSupervisor_Object = MibScalar
alLSupervisor = _AlLSupervisor_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 1, 1),
    _AlLSupervisor_Type()
)
alLSupervisor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLSupervisor.setStatus("mandatory")


class _AlLConfiguration_Type(Integer32):
    """Custom type alLConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("cf1xE1-Ethernet", 4),
          ("cf1xE2", 3),
          ("cf1xE3-E1", 7),
          ("cf1xEthF", 18),
          ("cf1xEthF-1xE1", 19),
          ("cf1xEthF-2xE1", 20),
          ("cf1xEthF-3xE1", 21),
          ("cf1xEthF-4xE1", 22),
          ("cf1xEthF-5xE1", 23),
          ("cf1xEthF-6xE1", 24),
          ("cf1xEthF-7xE1", 25),
          ("cf1xEthF-8xE1", 26),
          ("cf1xEthF-E1", 9),
          ("cf1xEthF-E1-1xE1", 10),
          ("cf1xEthF-E1-2xE1", 11),
          ("cf1xEthF-E1-3xE1", 12),
          ("cf1xEthF-E1-4xE1", 13),
          ("cf1xEthF-E1-5xE1", 14),
          ("cf1xEthF-E1-6xE1", 15),
          ("cf1xEthF-E1-7xE1", 16),
          ("cf1xEthF-E1-8xE1", 17),
          ("cf1xEthernet", 8),
          ("cf2xE1", 1),
          ("cf2xFEth", 27),
          ("cf2xFEth-1xE1", 28),
          ("cf2xGEth", 30),
          ("cf2xGEth-SFP100", 31),
          ("cf2xGEth-SFP1000", 32),
          ("cf2xGEth-SFPSG", 33),
          ("cf4xE1", 2),
          ("cf4xFEth-2xE1", 29),
          ("offline", -1),
          ("undefined", 0))
    )


_AlLConfiguration_Type.__name__ = "Integer32"
_AlLConfiguration_Object = MibScalar
alLConfiguration = _AlLConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 1, 2),
    _AlLConfiguration_Type()
)
alLConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLConfiguration.setStatus("mandatory")


class _AlLStatus_Type(Integer32):
    """Custom type alLStatus based on Integer32"""
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
        *(("error", 3),
          ("offline", 0),
          ("ok", 1),
          ("warning", 2))
    )


_AlLStatus_Type.__name__ = "Integer32"
_AlLStatus_Object = MibScalar
alLStatus = _AlLStatus_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 1, 3),
    _AlLStatus_Type()
)
alLStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLStatus.setStatus("mandatory")


class _AlLHistory_Type(Integer32):
    """Custom type alLHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlLHistory_Type.__name__ = "Integer32"
_AlLHistory_Object = MibScalar
alLHistory = _AlLHistory_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 1, 4),
    _AlLHistory_Type()
)
alLHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLHistory.setStatus("mandatory")


class _AlLIAISL_Type(Integer32):
    """Custom type alLIAISL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLIAISL_Type.__name__ = "Integer32"
_AlLIAISL_Object = MibScalar
alLIAISL = _AlLIAISL_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 1, 5),
    _AlLIAISL_Type()
)
alLIAISL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLIAISL.setStatus("mandatory")


class _AlLILEVPWR_Type(Integer32):
    """Custom type alLILEVPWR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLILEVPWR_Type.__name__ = "Integer32"
_AlLILEVPWR_Object = MibScalar
alLILEVPWR = _AlLILEVPWR_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 1, 6),
    _AlLILEVPWR_Type()
)
alLILEVPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLILEVPWR.setStatus("mandatory")
_AlL_ODU_ObjectIdentity = ObjectIdentity
alL_ODU = _AlL_ODU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 2)
)


class _AlLRX_Level_Type(Integer32):
    """Custom type alLRX_Level based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlLRX_Level_Type.__name__ = "Integer32"
_AlLRX_Level_Object = MibScalar
alLRX_Level = _AlLRX_Level_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 2, 1),
    _AlLRX_Level_Type()
)
alLRX_Level.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLRX_Level.setStatus("mandatory")


class _AlLTX_PWR_Type(Integer32):
    """Custom type alLTX_PWR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlLTX_PWR_Type.__name__ = "Integer32"
_AlLTX_PWR_Object = MibScalar
alLTX_PWR = _AlLTX_PWR_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 2, 2),
    _AlLTX_PWR_Type()
)
alLTX_PWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLTX_PWR.setStatus("mandatory")


class _AlLMode_TX_Type(Integer32):
    """Custom type alLMode_TX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atpc", 2),
          ("manual", 1),
          ("off", 0),
          ("offline", -1))
    )


_AlLMode_TX_Type.__name__ = "Integer32"
_AlLMode_TX_Object = MibScalar
alLMode_TX = _AlLMode_TX_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 2, 3),
    _AlLMode_TX_Type()
)
alLMode_TX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLMode_TX.setStatus("mandatory")


class _AlLODU_LB_Type(Integer32):
    """Custom type alLODU_LB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLODU_LB_Type.__name__ = "Integer32"
_AlLODU_LB_Object = MibScalar
alLODU_LB = _AlLODU_LB_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 2, 4),
    _AlLODU_LB_Type()
)
alLODU_LB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLODU_LB.setStatus("mandatory")
_AlL_Modem_ObjectIdentity = ObjectIdentity
alL_Modem = _AlL_Modem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 3)
)


class _AlLQuality_Type(Integer32):
    """Custom type alLQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("offline", -1),
          ("ok", 0),
          ("out", 1))
    )


_AlLQuality_Type.__name__ = "Integer32"
_AlLQuality_Object = MibScalar
alLQuality = _AlLQuality_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 3, 1),
    _AlLQuality_Type()
)
alLQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLQuality.setStatus("mandatory")
_AlL_Supply_ObjectIdentity = ObjectIdentity
alL_Supply = _AlL_Supply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 4)
)


class _AlLVoltage_5V_Type(Integer32):
    """Custom type alLVoltage_5V based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlLVoltage_5V_Type.__name__ = "Integer32"
_AlLVoltage_5V_Object = MibScalar
alLVoltage_5V = _AlLVoltage_5V_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 4, 1),
    _AlLVoltage_5V_Type()
)
alLVoltage_5V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLVoltage_5V.setStatus("mandatory")


class _AlLVoltage_5Vor15V_Type(Integer32):
    """Custom type alLVoltage_5Vor15V based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlLVoltage_5Vor15V_Type.__name__ = "Integer32"
_AlLVoltage_5Vor15V_Object = MibScalar
alLVoltage_5Vor15V = _AlLVoltage_5Vor15V_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 4, 2),
    _AlLVoltage_5Vor15V_Type()
)
alLVoltage_5Vor15V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLVoltage_5Vor15V.setStatus("mandatory")


class _AlLVoltage_24V_Type(Integer32):
    """Custom type alLVoltage_24V based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlLVoltage_24V_Type.__name__ = "Integer32"
_AlLVoltage_24V_Object = MibScalar
alLVoltage_24V = _AlLVoltage_24V_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 4, 3),
    _AlLVoltage_24V_Type()
)
alLVoltage_24V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLVoltage_24V.setStatus("mandatory")


class _AlLCurrent_ODU_Type(Integer32):
    """Custom type alLCurrent_ODU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("offline", -1),
          ("ok", 0),
          ("out", 1))
    )


_AlLCurrent_ODU_Type.__name__ = "Integer32"
_AlLCurrent_ODU_Object = MibScalar
alLCurrent_ODU = _AlLCurrent_ODU_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 4, 4),
    _AlLCurrent_ODU_Type()
)
alLCurrent_ODU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLCurrent_ODU.setStatus("mandatory")


class _AlLInput_Type(Integer32):
    """Custom type alLInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlLInput_Type.__name__ = "Integer32"
_AlLInput_Object = MibScalar
alLInput = _AlLInput_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 4, 5),
    _AlLInput_Type()
)
alLInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLInput.setStatus("mandatory")
_AlL_IDU_ObjectIdentity = ObjectIdentity
alL_IDU = _AlL_IDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 5)
)


class _AlLEEPROM_Type(Integer32):
    """Custom type alLEEPROM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bad", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlLEEPROM_Type.__name__ = "Integer32"
_AlLEEPROM_Object = MibScalar
alLEEPROM = _AlLEEPROM_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 5, 1),
    _AlLEEPROM_Type()
)
alLEEPROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLEEPROM.setStatus("mandatory")


class _AlLRAM_Type(Integer32):
    """Custom type alLRAM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bad", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlLRAM_Type.__name__ = "Integer32"
_AlLRAM_Object = MibScalar
alLRAM = _AlLRAM_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 5, 2),
    _AlLRAM_Type()
)
alLRAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLRAM.setStatus("mandatory")


class _AlLBattery_Type(Integer32):
    """Custom type alLBattery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlLBattery_Type.__name__ = "Integer32"
_AlLBattery_Object = MibScalar
alLBattery = _AlLBattery_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 5, 3),
    _AlLBattery_Type()
)
alLBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLBattery.setStatus("mandatory")


class _AlLCommIDU_Type(Integer32):
    """Custom type alLCommIDU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bad", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlLCommIDU_Type.__name__ = "Integer32"
_AlLCommIDU_Object = MibScalar
alLCommIDU = _AlLCommIDU_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 5, 4),
    _AlLCommIDU_Type()
)
alLCommIDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLCommIDU.setStatus("mandatory")


class _AlLCommRMT_Type(Integer32):
    """Custom type alLCommRMT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlLCommRMT_Type.__name__ = "Integer32"
_AlLCommRMT_Object = MibScalar
alLCommRMT = _AlLCommRMT_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 5, 5),
    _AlLCommRMT_Type()
)
alLCommRMT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLCommRMT.setStatus("mandatory")
_AlL_MUX_ObjectIdentity = ObjectIdentity
alL_MUX = _AlL_MUX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 6)
)


class _AlLBER_10E6_Type(Integer32):
    """Custom type alLBER_10E6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlLBER_10E6_Type.__name__ = "Integer32"
_AlLBER_10E6_Object = MibScalar
alLBER_10E6 = _AlLBER_10E6_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 6, 1),
    _AlLBER_10E6_Type()
)
alLBER_10E6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLBER_10E6.setStatus("mandatory")


class _AlLBER_10E4_Type(Integer32):
    """Custom type alLBER_10E4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlLBER_10E4_Type.__name__ = "Integer32"
_AlLBER_10E4_Object = MibScalar
alLBER_10E4 = _AlLBER_10E4_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 6, 2),
    _AlLBER_10E4_Type()
)
alLBER_10E4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLBER_10E4.setStatus("mandatory")


class _AlLFrame_Type(Integer32):
    """Custom type alLFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loss", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlLFrame_Type.__name__ = "Integer32"
_AlLFrame_Object = MibScalar
alLFrame = _AlLFrame_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 6, 3),
    _AlLFrame_Type()
)
alLFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLFrame.setStatus("mandatory")
_AlL_PDH1_ObjectIdentity = ObjectIdentity
alL_PDH1 = _AlL_PDH1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 7)
)


class _AlLPDHFrame_Type(Integer32):
    """Custom type alLPDHFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loss", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlLPDHFrame_Type.__name__ = "Integer32"
_AlLPDHFrame_Object = MibScalar
alLPDHFrame = _AlLPDHFrame_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 7, 1),
    _AlLPDHFrame_Type()
)
alLPDHFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLPDHFrame.setStatus("mandatory")


class _AlLAISPDH_Type(Integer32):
    """Custom type alLAISPDH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("offline", -1),
          ("ok", 0),
          ("on", 1))
    )


_AlLAISPDH_Type.__name__ = "Integer32"
_AlLAISPDH_Object = MibScalar
alLAISPDH = _AlLAISPDH_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 7, 2),
    _AlLAISPDH_Type()
)
alLAISPDH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLAISPDH.setStatus("mandatory")


class _AlLLLBPDH_Type(Integer32):
    """Custom type alLLLBPDH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLLLBPDH_Type.__name__ = "Integer32"
_AlLLLBPDH_Object = MibScalar
alLLLBPDH = _AlLLLBPDH_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 7, 3),
    _AlLLLBPDH_Type()
)
alLLLBPDH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLLLBPDH.setStatus("mandatory")


class _AlLRLBPDH_Type(Integer32):
    """Custom type alLRLBPDH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLRLBPDH_Type.__name__ = "Integer32"
_AlLRLBPDH_Object = MibScalar
alLRLBPDH = _AlLRLBPDH_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 7, 4),
    _AlLRLBPDH_Type()
)
alLRLBPDH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLRLBPDH.setStatus("mandatory")
_AlL_Line1_ObjectIdentity = ObjectIdentity
alL_Line1 = _AlL_Line1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 9)
)


class _AlLOSS1_Type(Integer32):
    """Custom type alLOSS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlLOSS1_Type.__name__ = "Integer32"
_AlLOSS1_Object = MibScalar
alLOSS1 = _AlLOSS1_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 9, 1),
    _AlLOSS1_Type()
)
alLOSS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLOSS1.setStatus("mandatory")


class _AlILOSS1_Type(Integer32):
    """Custom type alILOSS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlILOSS1_Type.__name__ = "Integer32"
_AlILOSS1_Object = MibScalar
alILOSS1 = _AlILOSS1_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 9, 2),
    _AlILOSS1_Type()
)
alILOSS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alILOSS1.setStatus("mandatory")


class _AlAIS1_Type(Integer32):
    """Custom type alAIS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlAIS1_Type.__name__ = "Integer32"
_AlAIS1_Object = MibScalar
alAIS1 = _AlAIS1_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 9, 3),
    _AlAIS1_Type()
)
alAIS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAIS1.setStatus("mandatory")


class _AlAISL1_Type(Integer32):
    """Custom type alAISL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlAISL1_Type.__name__ = "Integer32"
_AlAISL1_Object = MibScalar
alAISL1 = _AlAISL1_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 9, 4),
    _AlAISL1_Type()
)
alAISL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAISL1.setStatus("mandatory")


class _AlLLB1_Type(Integer32):
    """Custom type alLLB1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLLB1_Type.__name__ = "Integer32"
_AlLLB1_Object = MibScalar
alLLB1 = _AlLLB1_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 9, 5),
    _AlLLB1_Type()
)
alLLB1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLLB1.setStatus("mandatory")


class _AlRLB1_Type(Integer32):
    """Custom type alRLB1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRLB1_Type.__name__ = "Integer32"
_AlRLB1_Object = MibScalar
alRLB1 = _AlRLB1_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 9, 6),
    _AlRLB1_Type()
)
alRLB1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRLB1.setStatus("mandatory")
_AlL_Line2_ObjectIdentity = ObjectIdentity
alL_Line2 = _AlL_Line2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 10)
)


class _AlLLOSS2_Type(Integer32):
    """Custom type alLLOSS2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlLLOSS2_Type.__name__ = "Integer32"
_AlLLOSS2_Object = MibScalar
alLLOSS2 = _AlLLOSS2_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 10, 1),
    _AlLLOSS2_Type()
)
alLLOSS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLLOSS2.setStatus("mandatory")


class _AlLILOSS2_Type(Integer32):
    """Custom type alLILOSS2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLILOSS2_Type.__name__ = "Integer32"
_AlLILOSS2_Object = MibScalar
alLILOSS2 = _AlLILOSS2_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 10, 2),
    _AlLILOSS2_Type()
)
alLILOSS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLILOSS2.setStatus("mandatory")


class _AlLAIS2_Type(Integer32):
    """Custom type alLAIS2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlLAIS2_Type.__name__ = "Integer32"
_AlLAIS2_Object = MibScalar
alLAIS2 = _AlLAIS2_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 10, 3),
    _AlLAIS2_Type()
)
alLAIS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLAIS2.setStatus("mandatory")


class _AlLAISL2_Type(Integer32):
    """Custom type alLAISL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLAISL2_Type.__name__ = "Integer32"
_AlLAISL2_Object = MibScalar
alLAISL2 = _AlLAISL2_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 10, 4),
    _AlLAISL2_Type()
)
alLAISL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLAISL2.setStatus("mandatory")


class _AlLLLB2_Type(Integer32):
    """Custom type alLLLB2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLLLB2_Type.__name__ = "Integer32"
_AlLLLB2_Object = MibScalar
alLLLB2 = _AlLLLB2_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 10, 5),
    _AlLLLB2_Type()
)
alLLLB2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLLLB2.setStatus("mandatory")


class _AlLRLB2_Type(Integer32):
    """Custom type alLRLB2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLRLB2_Type.__name__ = "Integer32"
_AlLRLB2_Object = MibScalar
alLRLB2 = _AlLRLB2_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 10, 6),
    _AlLRLB2_Type()
)
alLRLB2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLRLB2.setStatus("mandatory")
_AlL_Line3_ObjectIdentity = ObjectIdentity
alL_Line3 = _AlL_Line3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 11)
)


class _AlLLOSS3_Type(Integer32):
    """Custom type alLLOSS3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlLLOSS3_Type.__name__ = "Integer32"
_AlLLOSS3_Object = MibScalar
alLLOSS3 = _AlLLOSS3_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 11, 1),
    _AlLLOSS3_Type()
)
alLLOSS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLLOSS3.setStatus("mandatory")


class _AlLILOSS3_Type(Integer32):
    """Custom type alLILOSS3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLILOSS3_Type.__name__ = "Integer32"
_AlLILOSS3_Object = MibScalar
alLILOSS3 = _AlLILOSS3_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 11, 2),
    _AlLILOSS3_Type()
)
alLILOSS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLILOSS3.setStatus("mandatory")


class _AlLAIS3_Type(Integer32):
    """Custom type alLAIS3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlLAIS3_Type.__name__ = "Integer32"
_AlLAIS3_Object = MibScalar
alLAIS3 = _AlLAIS3_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 11, 3),
    _AlLAIS3_Type()
)
alLAIS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLAIS3.setStatus("mandatory")


class _AlLAISL3_Type(Integer32):
    """Custom type alLAISL3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLAISL3_Type.__name__ = "Integer32"
_AlLAISL3_Object = MibScalar
alLAISL3 = _AlLAISL3_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 11, 4),
    _AlLAISL3_Type()
)
alLAISL3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLAISL3.setStatus("mandatory")


class _AlLLLB3_Type(Integer32):
    """Custom type alLLLB3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLLLB3_Type.__name__ = "Integer32"
_AlLLLB3_Object = MibScalar
alLLLB3 = _AlLLLB3_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 11, 5),
    _AlLLLB3_Type()
)
alLLLB3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLLLB3.setStatus("mandatory")


class _AlLRLB3_Type(Integer32):
    """Custom type alLRLB3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLRLB3_Type.__name__ = "Integer32"
_AlLRLB3_Object = MibScalar
alLRLB3 = _AlLRLB3_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 11, 6),
    _AlLRLB3_Type()
)
alLRLB3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLRLB3.setStatus("mandatory")
_AlL_Line4_ObjectIdentity = ObjectIdentity
alL_Line4 = _AlL_Line4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 12)
)


class _AlLLOSS4_Type(Integer32):
    """Custom type alLLOSS4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlLLOSS4_Type.__name__ = "Integer32"
_AlLLOSS4_Object = MibScalar
alLLOSS4 = _AlLLOSS4_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 12, 1),
    _AlLLOSS4_Type()
)
alLLOSS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLLOSS4.setStatus("mandatory")


class _AlLILOSS4_Type(Integer32):
    """Custom type alLILOSS4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLILOSS4_Type.__name__ = "Integer32"
_AlLILOSS4_Object = MibScalar
alLILOSS4 = _AlLILOSS4_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 12, 2),
    _AlLILOSS4_Type()
)
alLILOSS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLILOSS4.setStatus("mandatory")


class _AlLAIS4_Type(Integer32):
    """Custom type alLAIS4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlLAIS4_Type.__name__ = "Integer32"
_AlLAIS4_Object = MibScalar
alLAIS4 = _AlLAIS4_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 12, 3),
    _AlLAIS4_Type()
)
alLAIS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLAIS4.setStatus("mandatory")


class _AlLAISL4_Type(Integer32):
    """Custom type alLAISL4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLAISL4_Type.__name__ = "Integer32"
_AlLAISL4_Object = MibScalar
alLAISL4 = _AlLAISL4_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 12, 4),
    _AlLAISL4_Type()
)
alLAISL4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLAISL4.setStatus("mandatory")


class _AlLLLB4_Type(Integer32):
    """Custom type alLLLB4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLLLB4_Type.__name__ = "Integer32"
_AlLLLB4_Object = MibScalar
alLLLB4 = _AlLLLB4_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 12, 5),
    _AlLLLB4_Type()
)
alLLLB4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLLLB4.setStatus("mandatory")


class _AlLRLB4_Type(Integer32):
    """Custom type alLRLB4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLRLB4_Type.__name__ = "Integer32"
_AlLRLB4_Object = MibScalar
alLRLB4 = _AlLRLB4_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 12, 6),
    _AlLRLB4_Type()
)
alLRLB4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLRLB4.setStatus("mandatory")
_AlL_Line5_ObjectIdentity = ObjectIdentity
alL_Line5 = _AlL_Line5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 13)
)


class _AlLLOSS5_Type(Integer32):
    """Custom type alLLOSS5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlLLOSS5_Type.__name__ = "Integer32"
_AlLLOSS5_Object = MibScalar
alLLOSS5 = _AlLLOSS5_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 13, 1),
    _AlLLOSS5_Type()
)
alLLOSS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLLOSS5.setStatus("mandatory")


class _AlLILOSS5_Type(Integer32):
    """Custom type alLILOSS5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLILOSS5_Type.__name__ = "Integer32"
_AlLILOSS5_Object = MibScalar
alLILOSS5 = _AlLILOSS5_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 13, 2),
    _AlLILOSS5_Type()
)
alLILOSS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLILOSS5.setStatus("mandatory")


class _AlLAIS5_Type(Integer32):
    """Custom type alLAIS5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlLAIS5_Type.__name__ = "Integer32"
_AlLAIS5_Object = MibScalar
alLAIS5 = _AlLAIS5_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 13, 3),
    _AlLAIS5_Type()
)
alLAIS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLAIS5.setStatus("mandatory")


class _AlLAISL5_Type(Integer32):
    """Custom type alLAISL5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLAISL5_Type.__name__ = "Integer32"
_AlLAISL5_Object = MibScalar
alLAISL5 = _AlLAISL5_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 13, 4),
    _AlLAISL5_Type()
)
alLAISL5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLAISL5.setStatus("mandatory")


class _AlLLLB5_Type(Integer32):
    """Custom type alLLLB5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLLLB5_Type.__name__ = "Integer32"
_AlLLLB5_Object = MibScalar
alLLLB5 = _AlLLLB5_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 13, 5),
    _AlLLLB5_Type()
)
alLLLB5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLLLB5.setStatus("mandatory")


class _AlLRLB5_Type(Integer32):
    """Custom type alLRLB5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLRLB5_Type.__name__ = "Integer32"
_AlLRLB5_Object = MibScalar
alLRLB5 = _AlLRLB5_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 13, 6),
    _AlLRLB5_Type()
)
alLRLB5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLRLB5.setStatus("mandatory")
_AlL_Line6_ObjectIdentity = ObjectIdentity
alL_Line6 = _AlL_Line6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 14)
)


class _AlLLOSS6_Type(Integer32):
    """Custom type alLLOSS6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlLLOSS6_Type.__name__ = "Integer32"
_AlLLOSS6_Object = MibScalar
alLLOSS6 = _AlLLOSS6_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 14, 1),
    _AlLLOSS6_Type()
)
alLLOSS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLLOSS6.setStatus("mandatory")


class _AlLILOSS6_Type(Integer32):
    """Custom type alLILOSS6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLILOSS6_Type.__name__ = "Integer32"
_AlLILOSS6_Object = MibScalar
alLILOSS6 = _AlLILOSS6_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 14, 2),
    _AlLILOSS6_Type()
)
alLILOSS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLILOSS6.setStatus("mandatory")


class _AlLAIS6_Type(Integer32):
    """Custom type alLAIS6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlLAIS6_Type.__name__ = "Integer32"
_AlLAIS6_Object = MibScalar
alLAIS6 = _AlLAIS6_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 14, 3),
    _AlLAIS6_Type()
)
alLAIS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLAIS6.setStatus("mandatory")


class _AlLAISL6_Type(Integer32):
    """Custom type alLAISL6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLAISL6_Type.__name__ = "Integer32"
_AlLAISL6_Object = MibScalar
alLAISL6 = _AlLAISL6_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 14, 4),
    _AlLAISL6_Type()
)
alLAISL6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLAISL6.setStatus("mandatory")


class _AlLLLB6_Type(Integer32):
    """Custom type alLLLB6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLLLB6_Type.__name__ = "Integer32"
_AlLLLB6_Object = MibScalar
alLLLB6 = _AlLLLB6_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 14, 5),
    _AlLLLB6_Type()
)
alLLLB6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLLLB6.setStatus("mandatory")


class _AlLRLB6_Type(Integer32):
    """Custom type alLRLB6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLRLB6_Type.__name__ = "Integer32"
_AlLRLB6_Object = MibScalar
alLRLB6 = _AlLRLB6_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 14, 6),
    _AlLRLB6_Type()
)
alLRLB6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLRLB6.setStatus("mandatory")
_AlL_Line7_ObjectIdentity = ObjectIdentity
alL_Line7 = _AlL_Line7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 15)
)


class _AlLLOSS7_Type(Integer32):
    """Custom type alLLOSS7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlLLOSS7_Type.__name__ = "Integer32"
_AlLLOSS7_Object = MibScalar
alLLOSS7 = _AlLLOSS7_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 15, 1),
    _AlLLOSS7_Type()
)
alLLOSS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLLOSS7.setStatus("mandatory")


class _AlLILOSS7_Type(Integer32):
    """Custom type alLILOSS7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLILOSS7_Type.__name__ = "Integer32"
_AlLILOSS7_Object = MibScalar
alLILOSS7 = _AlLILOSS7_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 15, 2),
    _AlLILOSS7_Type()
)
alLILOSS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLILOSS7.setStatus("mandatory")


class _AlLAIS7_Type(Integer32):
    """Custom type alLAIS7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlLAIS7_Type.__name__ = "Integer32"
_AlLAIS7_Object = MibScalar
alLAIS7 = _AlLAIS7_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 15, 3),
    _AlLAIS7_Type()
)
alLAIS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLAIS7.setStatus("mandatory")


class _AlLAISL7_Type(Integer32):
    """Custom type alLAISL7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLAISL7_Type.__name__ = "Integer32"
_AlLAISL7_Object = MibScalar
alLAISL7 = _AlLAISL7_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 15, 4),
    _AlLAISL7_Type()
)
alLAISL7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLAISL7.setStatus("mandatory")


class _AlLLLB7_Type(Integer32):
    """Custom type alLLLB7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLLLB7_Type.__name__ = "Integer32"
_AlLLLB7_Object = MibScalar
alLLLB7 = _AlLLLB7_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 15, 5),
    _AlLLLB7_Type()
)
alLLLB7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLLLB7.setStatus("mandatory")


class _AlLRLB7_Type(Integer32):
    """Custom type alLRLB7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLRLB7_Type.__name__ = "Integer32"
_AlLRLB7_Object = MibScalar
alLRLB7 = _AlLRLB7_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 15, 6),
    _AlLRLB7_Type()
)
alLRLB7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLRLB7.setStatus("mandatory")
_AlL_Line8_ObjectIdentity = ObjectIdentity
alL_Line8 = _AlL_Line8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 16)
)


class _AlLLOSS8_Type(Integer32):
    """Custom type alLLOSS8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlLLOSS8_Type.__name__ = "Integer32"
_AlLLOSS8_Object = MibScalar
alLLOSS8 = _AlLLOSS8_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 16, 1),
    _AlLLOSS8_Type()
)
alLLOSS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLLOSS8.setStatus("mandatory")


class _AlLILOSS8_Type(Integer32):
    """Custom type alLILOSS8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLILOSS8_Type.__name__ = "Integer32"
_AlLILOSS8_Object = MibScalar
alLILOSS8 = _AlLILOSS8_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 16, 2),
    _AlLILOSS8_Type()
)
alLILOSS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLILOSS8.setStatus("mandatory")


class _AlLAIS8_Type(Integer32):
    """Custom type alLAIS8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlLAIS8_Type.__name__ = "Integer32"
_AlLAIS8_Object = MibScalar
alLAIS8 = _AlLAIS8_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 16, 3),
    _AlLAIS8_Type()
)
alLAIS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLAIS8.setStatus("mandatory")


class _AlLAISL8_Type(Integer32):
    """Custom type alLAISL8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLAISL8_Type.__name__ = "Integer32"
_AlLAISL8_Object = MibScalar
alLAISL8 = _AlLAISL8_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 16, 4),
    _AlLAISL8_Type()
)
alLAISL8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLAISL8.setStatus("mandatory")


class _AlLLLB8_Type(Integer32):
    """Custom type alLLLB8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLLLB8_Type.__name__ = "Integer32"
_AlLLLB8_Object = MibScalar
alLLLB8 = _AlLLLB8_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 16, 5),
    _AlLLLB8_Type()
)
alLLLB8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLLLB8.setStatus("mandatory")


class _AlLRLB8_Type(Integer32):
    """Custom type alLRLB8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLRLB8_Type.__name__ = "Integer32"
_AlLRLB8_Object = MibScalar
alLRLB8 = _AlLRLB8_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 16, 6),
    _AlLRLB8_Type()
)
alLRLB8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLRLB8.setStatus("mandatory")
_AlL_Line9_ObjectIdentity = ObjectIdentity
alL_Line9 = _AlL_Line9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 17)
)


class _AlLLOSS9_Type(Integer32):
    """Custom type alLLOSS9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlLLOSS9_Type.__name__ = "Integer32"
_AlLLOSS9_Object = MibScalar
alLLOSS9 = _AlLLOSS9_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 17, 1),
    _AlLLOSS9_Type()
)
alLLOSS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLLOSS9.setStatus("mandatory")


class _AlLILOSS9_Type(Integer32):
    """Custom type alLILOSS9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLILOSS9_Type.__name__ = "Integer32"
_AlLILOSS9_Object = MibScalar
alLILOSS9 = _AlLILOSS9_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 17, 2),
    _AlLILOSS9_Type()
)
alLILOSS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLILOSS9.setStatus("mandatory")


class _AlLAIS9_Type(Integer32):
    """Custom type alLAIS9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlLAIS9_Type.__name__ = "Integer32"
_AlLAIS9_Object = MibScalar
alLAIS9 = _AlLAIS9_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 17, 3),
    _AlLAIS9_Type()
)
alLAIS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLAIS9.setStatus("mandatory")


class _AlLAISL9_Type(Integer32):
    """Custom type alLAISL9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLAISL9_Type.__name__ = "Integer32"
_AlLAISL9_Object = MibScalar
alLAISL9 = _AlLAISL9_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 17, 4),
    _AlLAISL9_Type()
)
alLAISL9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLAISL9.setStatus("mandatory")


class _AlLLLB9_Type(Integer32):
    """Custom type alLLLB9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLLLB9_Type.__name__ = "Integer32"
_AlLLLB9_Object = MibScalar
alLLLB9 = _AlLLLB9_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 17, 5),
    _AlLLLB9_Type()
)
alLLLB9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLLLB9.setStatus("mandatory")


class _AlLRLB9_Type(Integer32):
    """Custom type alLRLB9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLRLB9_Type.__name__ = "Integer32"
_AlLRLB9_Object = MibScalar
alLRLB9 = _AlLRLB9_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 17, 6),
    _AlLRLB9_Type()
)
alLRLB9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLRLB9.setStatus("mandatory")
_AlL_Line10_ObjectIdentity = ObjectIdentity
alL_Line10 = _AlL_Line10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 18)
)


class _AlLLOSS10_Type(Integer32):
    """Custom type alLLOSS10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlLLOSS10_Type.__name__ = "Integer32"
_AlLLOSS10_Object = MibScalar
alLLOSS10 = _AlLLOSS10_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 18, 1),
    _AlLLOSS10_Type()
)
alLLOSS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLLOSS10.setStatus("mandatory")


class _AlLILOSS10_Type(Integer32):
    """Custom type alLILOSS10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLILOSS10_Type.__name__ = "Integer32"
_AlLILOSS10_Object = MibScalar
alLILOSS10 = _AlLILOSS10_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 18, 2),
    _AlLILOSS10_Type()
)
alLILOSS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLILOSS10.setStatus("mandatory")


class _AlLAIS10_Type(Integer32):
    """Custom type alLAIS10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlLAIS10_Type.__name__ = "Integer32"
_AlLAIS10_Object = MibScalar
alLAIS10 = _AlLAIS10_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 18, 3),
    _AlLAIS10_Type()
)
alLAIS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLAIS10.setStatus("mandatory")


class _AlLAISL10_Type(Integer32):
    """Custom type alLAISL10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLAISL10_Type.__name__ = "Integer32"
_AlLAISL10_Object = MibScalar
alLAISL10 = _AlLAISL10_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 18, 4),
    _AlLAISL10_Type()
)
alLAISL10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLAISL10.setStatus("mandatory")


class _AlLLLB10_Type(Integer32):
    """Custom type alLLLB10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLLLB10_Type.__name__ = "Integer32"
_AlLLLB10_Object = MibScalar
alLLLB10 = _AlLLLB10_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 18, 5),
    _AlLLLB10_Type()
)
alLLLB10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLLLB10.setStatus("mandatory")


class _AlLRLB10_Type(Integer32):
    """Custom type alLRLB10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLRLB10_Type.__name__ = "Integer32"
_AlLRLB10_Object = MibScalar
alLRLB10 = _AlLRLB10_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 18, 6),
    _AlLRLB10_Type()
)
alLRLB10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLRLB10.setStatus("mandatory")
_AlL_Line11_ObjectIdentity = ObjectIdentity
alL_Line11 = _AlL_Line11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 19)
)


class _AlLLOSS11_Type(Integer32):
    """Custom type alLLOSS11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlLLOSS11_Type.__name__ = "Integer32"
_AlLLOSS11_Object = MibScalar
alLLOSS11 = _AlLLOSS11_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 19, 1),
    _AlLLOSS11_Type()
)
alLLOSS11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLLOSS11.setStatus("mandatory")


class _AlLILOSS11_Type(Integer32):
    """Custom type alLILOSS11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLILOSS11_Type.__name__ = "Integer32"
_AlLILOSS11_Object = MibScalar
alLILOSS11 = _AlLILOSS11_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 19, 2),
    _AlLILOSS11_Type()
)
alLILOSS11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLILOSS11.setStatus("mandatory")


class _AlLAIS11_Type(Integer32):
    """Custom type alLAIS11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlLAIS11_Type.__name__ = "Integer32"
_AlLAIS11_Object = MibScalar
alLAIS11 = _AlLAIS11_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 19, 3),
    _AlLAIS11_Type()
)
alLAIS11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLAIS11.setStatus("mandatory")


class _AlLAISL11_Type(Integer32):
    """Custom type alLAISL11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLAISL11_Type.__name__ = "Integer32"
_AlLAISL11_Object = MibScalar
alLAISL11 = _AlLAISL11_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 19, 4),
    _AlLAISL11_Type()
)
alLAISL11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLAISL11.setStatus("mandatory")


class _AlLLLB11_Type(Integer32):
    """Custom type alLLLB11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLLLB11_Type.__name__ = "Integer32"
_AlLLLB11_Object = MibScalar
alLLLB11 = _AlLLLB11_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 19, 5),
    _AlLLLB11_Type()
)
alLLLB11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLLLB11.setStatus("mandatory")


class _AlLRLB11_Type(Integer32):
    """Custom type alLRLB11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLRLB11_Type.__name__ = "Integer32"
_AlLRLB11_Object = MibScalar
alLRLB11 = _AlLRLB11_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 19, 6),
    _AlLRLB11_Type()
)
alLRLB11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLRLB11.setStatus("mandatory")
_AlL_Line12_ObjectIdentity = ObjectIdentity
alL_Line12 = _AlL_Line12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 20)
)


class _AlLLOSS12_Type(Integer32):
    """Custom type alLLOSS12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlLLOSS12_Type.__name__ = "Integer32"
_AlLLOSS12_Object = MibScalar
alLLOSS12 = _AlLLOSS12_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 20, 1),
    _AlLLOSS12_Type()
)
alLLOSS12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLLOSS12.setStatus("mandatory")


class _AlLILOSS12_Type(Integer32):
    """Custom type alLILOSS12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLILOSS12_Type.__name__ = "Integer32"
_AlLILOSS12_Object = MibScalar
alLILOSS12 = _AlLILOSS12_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 20, 2),
    _AlLILOSS12_Type()
)
alLILOSS12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLILOSS12.setStatus("mandatory")


class _AlLAIS12_Type(Integer32):
    """Custom type alLAIS12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlLAIS12_Type.__name__ = "Integer32"
_AlLAIS12_Object = MibScalar
alLAIS12 = _AlLAIS12_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 20, 3),
    _AlLAIS12_Type()
)
alLAIS12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLAIS12.setStatus("mandatory")


class _AlLAISL12_Type(Integer32):
    """Custom type alLAISL12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLAISL12_Type.__name__ = "Integer32"
_AlLAISL12_Object = MibScalar
alLAISL12 = _AlLAISL12_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 20, 4),
    _AlLAISL12_Type()
)
alLAISL12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLAISL12.setStatus("mandatory")


class _AlLLLB12_Type(Integer32):
    """Custom type alLLLB12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLLLB12_Type.__name__ = "Integer32"
_AlLLLB12_Object = MibScalar
alLLLB12 = _AlLLLB12_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 20, 5),
    _AlLLLB12_Type()
)
alLLLB12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLLLB12.setStatus("mandatory")


class _AlLRLB12_Type(Integer32):
    """Custom type alLRLB12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlLRLB12_Type.__name__ = "Integer32"
_AlLRLB12_Object = MibScalar
alLRLB12 = _AlLRLB12_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 2, 20, 6),
    _AlLRLB12_Type()
)
alLRLB12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLRLB12.setStatus("mandatory")
_Remote_station_ObjectIdentity = ObjectIdentity
remote_station = _Remote_station_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3)
)
_AlR_General_ObjectIdentity = ObjectIdentity
alR_General = _AlR_General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 1)
)


class _AlRSupervisor_Type(Integer32):
    """Custom type alRSupervisor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("alcoma", 5),
          ("local", 2),
          ("network", 3),
          ("none", 0),
          ("offline", -1),
          ("service", 4),
          ("terminal", 1))
    )


_AlRSupervisor_Type.__name__ = "Integer32"
_AlRSupervisor_Object = MibScalar
alRSupervisor = _AlRSupervisor_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 1, 1),
    _AlRSupervisor_Type()
)
alRSupervisor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRSupervisor.setStatus("mandatory")


class _AlRConfiguration_Type(Integer32):
    """Custom type alRConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("cf1xE1-Ethernet", 4),
          ("cf1xE2", 3),
          ("cf1xE3-E1", 7),
          ("cf1xEthF", 18),
          ("cf1xEthF-1xE1", 19),
          ("cf1xEthF-2xE1", 20),
          ("cf1xEthF-3xE1", 21),
          ("cf1xEthF-4xE1", 22),
          ("cf1xEthF-5xE1", 23),
          ("cf1xEthF-6xE1", 24),
          ("cf1xEthF-7xE1", 25),
          ("cf1xEthF-8xE1", 26),
          ("cf1xEthF-E1", 9),
          ("cf1xEthF-E1-1xE1", 10),
          ("cf1xEthF-E1-2xE1", 11),
          ("cf1xEthF-E1-3xE1", 12),
          ("cf1xEthF-E1-4xE1", 13),
          ("cf1xEthF-E1-5xE1", 14),
          ("cf1xEthF-E1-6xE1", 15),
          ("cf1xEthF-E1-7xE1", 16),
          ("cf1xEthF-E1-8xE1", 17),
          ("cf1xEthernet", 8),
          ("cf2xE1", 1),
          ("cf2xFEth", 27),
          ("cf2xFEth-1xE1", 28),
          ("cf2xGEth", 30),
          ("cf2xGEth-SFP100", 31),
          ("cf2xGEth-SFP1000", 32),
          ("cf2xGEth-SFPSG", 33),
          ("cf4xE1", 2),
          ("cf4xFEth-2xE1", 29),
          ("offline", -1),
          ("undefined", 0))
    )


_AlRConfiguration_Type.__name__ = "Integer32"
_AlRConfiguration_Object = MibScalar
alRConfiguration = _AlRConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 1, 2),
    _AlRConfiguration_Type()
)
alRConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRConfiguration.setStatus("mandatory")


class _AlRStatus_Type(Integer32):
    """Custom type alRStatus based on Integer32"""
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
        *(("error", 3),
          ("offline", 0),
          ("ok", 1),
          ("warning", 2))
    )


_AlRStatus_Type.__name__ = "Integer32"
_AlRStatus_Object = MibScalar
alRStatus = _AlRStatus_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 1, 3),
    _AlRStatus_Type()
)
alRStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRStatus.setStatus("mandatory")


class _AlRHistory_Type(Integer32):
    """Custom type alRHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlRHistory_Type.__name__ = "Integer32"
_AlRHistory_Object = MibScalar
alRHistory = _AlRHistory_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 1, 4),
    _AlRHistory_Type()
)
alRHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRHistory.setStatus("mandatory")


class _AlRIAISL_Type(Integer32):
    """Custom type alRIAISL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRIAISL_Type.__name__ = "Integer32"
_AlRIAISL_Object = MibScalar
alRIAISL = _AlRIAISL_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 1, 5),
    _AlRIAISL_Type()
)
alRIAISL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRIAISL.setStatus("mandatory")


class _AlRILEVPWR_Type(Integer32):
    """Custom type alRILEVPWR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRILEVPWR_Type.__name__ = "Integer32"
_AlRILEVPWR_Object = MibScalar
alRILEVPWR = _AlRILEVPWR_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 1, 6),
    _AlRILEVPWR_Type()
)
alRILEVPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRILEVPWR.setStatus("mandatory")
_AlR_ODU_ObjectIdentity = ObjectIdentity
alR_ODU = _AlR_ODU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 2)
)


class _AlRRX_Level_Type(Integer32):
    """Custom type alRRX_Level based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlRRX_Level_Type.__name__ = "Integer32"
_AlRRX_Level_Object = MibScalar
alRRX_Level = _AlRRX_Level_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 2, 1),
    _AlRRX_Level_Type()
)
alRRX_Level.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRRX_Level.setStatus("mandatory")


class _AlRTX_PWR_Type(Integer32):
    """Custom type alRTX_PWR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlRTX_PWR_Type.__name__ = "Integer32"
_AlRTX_PWR_Object = MibScalar
alRTX_PWR = _AlRTX_PWR_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 2, 2),
    _AlRTX_PWR_Type()
)
alRTX_PWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRTX_PWR.setStatus("mandatory")


class _AlRMode_TX_Type(Integer32):
    """Custom type alRMode_TX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atpc", 2),
          ("manual", 1),
          ("off", 0),
          ("offline", -1))
    )


_AlRMode_TX_Type.__name__ = "Integer32"
_AlRMode_TX_Object = MibScalar
alRMode_TX = _AlRMode_TX_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 2, 3),
    _AlRMode_TX_Type()
)
alRMode_TX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRMode_TX.setStatus("mandatory")


class _AlRODU_LB_Type(Integer32):
    """Custom type alRODU_LB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRODU_LB_Type.__name__ = "Integer32"
_AlRODU_LB_Object = MibScalar
alRODU_LB = _AlRODU_LB_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 2, 4),
    _AlRODU_LB_Type()
)
alRODU_LB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRODU_LB.setStatus("mandatory")
_AlR_Modem_ObjectIdentity = ObjectIdentity
alR_Modem = _AlR_Modem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 3)
)


class _AlRQuality_Type(Integer32):
    """Custom type alRQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("offline", -1),
          ("ok", 0),
          ("out", 1))
    )


_AlRQuality_Type.__name__ = "Integer32"
_AlRQuality_Object = MibScalar
alRQuality = _AlRQuality_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 3, 1),
    _AlRQuality_Type()
)
alRQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRQuality.setStatus("mandatory")
_AlR_Supply_ObjectIdentity = ObjectIdentity
alR_Supply = _AlR_Supply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 4)
)


class _AlRVoltage_5V_Type(Integer32):
    """Custom type alRVoltage_5V based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlRVoltage_5V_Type.__name__ = "Integer32"
_AlRVoltage_5V_Object = MibScalar
alRVoltage_5V = _AlRVoltage_5V_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 4, 1),
    _AlRVoltage_5V_Type()
)
alRVoltage_5V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRVoltage_5V.setStatus("mandatory")


class _AlRVoltage_5Vor15V_Type(Integer32):
    """Custom type alRVoltage_5Vor15V based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlRVoltage_5Vor15V_Type.__name__ = "Integer32"
_AlRVoltage_5Vor15V_Object = MibScalar
alRVoltage_5Vor15V = _AlRVoltage_5Vor15V_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 4, 2),
    _AlRVoltage_5Vor15V_Type()
)
alRVoltage_5Vor15V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRVoltage_5Vor15V.setStatus("mandatory")


class _AlRVoltage_24V_Type(Integer32):
    """Custom type alRVoltage_24V based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlRVoltage_24V_Type.__name__ = "Integer32"
_AlRVoltage_24V_Object = MibScalar
alRVoltage_24V = _AlRVoltage_24V_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 4, 3),
    _AlRVoltage_24V_Type()
)
alRVoltage_24V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRVoltage_24V.setStatus("mandatory")


class _AlRCurrent_ODU_Type(Integer32):
    """Custom type alRCurrent_ODU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("offline", -1),
          ("ok", 0),
          ("out", 1))
    )


_AlRCurrent_ODU_Type.__name__ = "Integer32"
_AlRCurrent_ODU_Object = MibScalar
alRCurrent_ODU = _AlRCurrent_ODU_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 4, 4),
    _AlRCurrent_ODU_Type()
)
alRCurrent_ODU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRCurrent_ODU.setStatus("mandatory")


class _AlRInput_Type(Integer32):
    """Custom type alRInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlRInput_Type.__name__ = "Integer32"
_AlRInput_Object = MibScalar
alRInput = _AlRInput_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 4, 5),
    _AlRInput_Type()
)
alRInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRInput.setStatus("mandatory")
_AlR_IDU_ObjectIdentity = ObjectIdentity
alR_IDU = _AlR_IDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 5)
)


class _AlREEPROM_Type(Integer32):
    """Custom type alREEPROM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bad", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlREEPROM_Type.__name__ = "Integer32"
_AlREEPROM_Object = MibScalar
alREEPROM = _AlREEPROM_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 5, 1),
    _AlREEPROM_Type()
)
alREEPROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alREEPROM.setStatus("mandatory")


class _AlRRAM_Type(Integer32):
    """Custom type alRRAM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bad", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlRRAM_Type.__name__ = "Integer32"
_AlRRAM_Object = MibScalar
alRRAM = _AlRRAM_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 5, 2),
    _AlRRAM_Type()
)
alRRAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRRAM.setStatus("mandatory")


class _AlRBattery_Type(Integer32):
    """Custom type alRBattery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlRBattery_Type.__name__ = "Integer32"
_AlRBattery_Object = MibScalar
alRBattery = _AlRBattery_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 5, 3),
    _AlRBattery_Type()
)
alRBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRBattery.setStatus("mandatory")


class _AlRCommIDU_Type(Integer32):
    """Custom type alRCommIDU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bad", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlRCommIDU_Type.__name__ = "Integer32"
_AlRCommIDU_Object = MibScalar
alRCommIDU = _AlRCommIDU_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 5, 4),
    _AlRCommIDU_Type()
)
alRCommIDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRCommIDU.setStatus("mandatory")


class _AlRCommRMT_Type(Integer32):
    """Custom type alRCommRMT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlRCommRMT_Type.__name__ = "Integer32"
_AlRCommRMT_Object = MibScalar
alRCommRMT = _AlRCommRMT_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 5, 5),
    _AlRCommRMT_Type()
)
alRCommRMT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRCommRMT.setStatus("mandatory")
_AlR_MUX_ObjectIdentity = ObjectIdentity
alR_MUX = _AlR_MUX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 6)
)


class _AlRBER_10E6_Type(Integer32):
    """Custom type alRBER_10E6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlRBER_10E6_Type.__name__ = "Integer32"
_AlRBER_10E6_Object = MibScalar
alRBER_10E6 = _AlRBER_10E6_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 6, 1),
    _AlRBER_10E6_Type()
)
alRBER_10E6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRBER_10E6.setStatus("mandatory")


class _AlRBER_10E4_Type(Integer32):
    """Custom type alRBER_10E4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlRBER_10E4_Type.__name__ = "Integer32"
_AlRBER_10E4_Object = MibScalar
alRBER_10E4 = _AlRBER_10E4_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 6, 2),
    _AlRBER_10E4_Type()
)
alRBER_10E4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRBER_10E4.setStatus("mandatory")


class _AlRFrame_Type(Integer32):
    """Custom type alRFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loss", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlRFrame_Type.__name__ = "Integer32"
_AlRFrame_Object = MibScalar
alRFrame = _AlRFrame_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 6, 3),
    _AlRFrame_Type()
)
alRFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRFrame.setStatus("mandatory")
_AlR_PDH1_ObjectIdentity = ObjectIdentity
alR_PDH1 = _AlR_PDH1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 7)
)


class _AlRPDHFrame_Type(Integer32):
    """Custom type alRPDHFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loss", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlRPDHFrame_Type.__name__ = "Integer32"
_AlRPDHFrame_Object = MibScalar
alRPDHFrame = _AlRPDHFrame_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 7, 1),
    _AlRPDHFrame_Type()
)
alRPDHFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRPDHFrame.setStatus("mandatory")


class _AlRAISPDH_Type(Integer32):
    """Custom type alRAISPDH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("offline", -1),
          ("ok", 0),
          ("on", 1))
    )


_AlRAISPDH_Type.__name__ = "Integer32"
_AlRAISPDH_Object = MibScalar
alRAISPDH = _AlRAISPDH_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 7, 2),
    _AlRAISPDH_Type()
)
alRAISPDH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRAISPDH.setStatus("mandatory")


class _AlRLLBPDH_Type(Integer32):
    """Custom type alRLLBPDH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRLLBPDH_Type.__name__ = "Integer32"
_AlRLLBPDH_Object = MibScalar
alRLLBPDH = _AlRLLBPDH_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 7, 3),
    _AlRLLBPDH_Type()
)
alRLLBPDH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRLLBPDH.setStatus("mandatory")


class _AlRRLBPDH_Type(Integer32):
    """Custom type alRRLBPDH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRRLBPDH_Type.__name__ = "Integer32"
_AlRRLBPDH_Object = MibScalar
alRRLBPDH = _AlRRLBPDH_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 7, 4),
    _AlRRLBPDH_Type()
)
alRRLBPDH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRRLBPDH.setStatus("mandatory")
_AlR_Line1_ObjectIdentity = ObjectIdentity
alR_Line1 = _AlR_Line1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 9)
)


class _AlRLOSS1_Type(Integer32):
    """Custom type alRLOSS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlRLOSS1_Type.__name__ = "Integer32"
_AlRLOSS1_Object = MibScalar
alRLOSS1 = _AlRLOSS1_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 9, 1),
    _AlRLOSS1_Type()
)
alRLOSS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRLOSS1.setStatus("mandatory")


class _AlRILOSS1_Type(Integer32):
    """Custom type alRILOSS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRILOSS1_Type.__name__ = "Integer32"
_AlRILOSS1_Object = MibScalar
alRILOSS1 = _AlRILOSS1_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 9, 2),
    _AlRILOSS1_Type()
)
alRILOSS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRILOSS1.setStatus("mandatory")


class _AlRAIS1_Type(Integer32):
    """Custom type alRAIS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlRAIS1_Type.__name__ = "Integer32"
_AlRAIS1_Object = MibScalar
alRAIS1 = _AlRAIS1_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 9, 3),
    _AlRAIS1_Type()
)
alRAIS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRAIS1.setStatus("mandatory")


class _AlRAISL1_Type(Integer32):
    """Custom type alRAISL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRAISL1_Type.__name__ = "Integer32"
_AlRAISL1_Object = MibScalar
alRAISL1 = _AlRAISL1_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 9, 4),
    _AlRAISL1_Type()
)
alRAISL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRAISL1.setStatus("mandatory")


class _AlRLLB1_Type(Integer32):
    """Custom type alRLLB1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRLLB1_Type.__name__ = "Integer32"
_AlRLLB1_Object = MibScalar
alRLLB1 = _AlRLLB1_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 9, 5),
    _AlRLLB1_Type()
)
alRLLB1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRLLB1.setStatus("mandatory")


class _AlRRLB1_Type(Integer32):
    """Custom type alRRLB1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRRLB1_Type.__name__ = "Integer32"
_AlRRLB1_Object = MibScalar
alRRLB1 = _AlRRLB1_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 9, 6),
    _AlRRLB1_Type()
)
alRRLB1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRRLB1.setStatus("mandatory")
_AlR_Line2_ObjectIdentity = ObjectIdentity
alR_Line2 = _AlR_Line2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 10)
)


class _AlRLOSS2_Type(Integer32):
    """Custom type alRLOSS2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlRLOSS2_Type.__name__ = "Integer32"
_AlRLOSS2_Object = MibScalar
alRLOSS2 = _AlRLOSS2_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 10, 1),
    _AlRLOSS2_Type()
)
alRLOSS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRLOSS2.setStatus("mandatory")


class _AlRILOSS2_Type(Integer32):
    """Custom type alRILOSS2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRILOSS2_Type.__name__ = "Integer32"
_AlRILOSS2_Object = MibScalar
alRILOSS2 = _AlRILOSS2_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 10, 2),
    _AlRILOSS2_Type()
)
alRILOSS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRILOSS2.setStatus("mandatory")


class _AlRAIS2_Type(Integer32):
    """Custom type alRAIS2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlRAIS2_Type.__name__ = "Integer32"
_AlRAIS2_Object = MibScalar
alRAIS2 = _AlRAIS2_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 10, 3),
    _AlRAIS2_Type()
)
alRAIS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRAIS2.setStatus("mandatory")


class _AlRAISL2_Type(Integer32):
    """Custom type alRAISL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRAISL2_Type.__name__ = "Integer32"
_AlRAISL2_Object = MibScalar
alRAISL2 = _AlRAISL2_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 10, 4),
    _AlRAISL2_Type()
)
alRAISL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRAISL2.setStatus("mandatory")


class _AlRLLB2_Type(Integer32):
    """Custom type alRLLB2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRLLB2_Type.__name__ = "Integer32"
_AlRLLB2_Object = MibScalar
alRLLB2 = _AlRLLB2_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 10, 5),
    _AlRLLB2_Type()
)
alRLLB2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRLLB2.setStatus("mandatory")


class _AlRRLB2_Type(Integer32):
    """Custom type alRRLB2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRRLB2_Type.__name__ = "Integer32"
_AlRRLB2_Object = MibScalar
alRRLB2 = _AlRRLB2_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 10, 6),
    _AlRRLB2_Type()
)
alRRLB2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRRLB2.setStatus("mandatory")
_AlR_Line3_ObjectIdentity = ObjectIdentity
alR_Line3 = _AlR_Line3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 11)
)


class _AlRLOSS3_Type(Integer32):
    """Custom type alRLOSS3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlRLOSS3_Type.__name__ = "Integer32"
_AlRLOSS3_Object = MibScalar
alRLOSS3 = _AlRLOSS3_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 11, 1),
    _AlRLOSS3_Type()
)
alRLOSS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRLOSS3.setStatus("mandatory")


class _AlRILOSS3_Type(Integer32):
    """Custom type alRILOSS3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRILOSS3_Type.__name__ = "Integer32"
_AlRILOSS3_Object = MibScalar
alRILOSS3 = _AlRILOSS3_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 11, 2),
    _AlRILOSS3_Type()
)
alRILOSS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRILOSS3.setStatus("mandatory")


class _AlRAIS3_Type(Integer32):
    """Custom type alRAIS3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlRAIS3_Type.__name__ = "Integer32"
_AlRAIS3_Object = MibScalar
alRAIS3 = _AlRAIS3_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 11, 3),
    _AlRAIS3_Type()
)
alRAIS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRAIS3.setStatus("mandatory")


class _AlRAISL3_Type(Integer32):
    """Custom type alRAISL3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRAISL3_Type.__name__ = "Integer32"
_AlRAISL3_Object = MibScalar
alRAISL3 = _AlRAISL3_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 11, 4),
    _AlRAISL3_Type()
)
alRAISL3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRAISL3.setStatus("mandatory")


class _AlRLLB3_Type(Integer32):
    """Custom type alRLLB3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRLLB3_Type.__name__ = "Integer32"
_AlRLLB3_Object = MibScalar
alRLLB3 = _AlRLLB3_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 11, 5),
    _AlRLLB3_Type()
)
alRLLB3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRLLB3.setStatus("mandatory")


class _AlRRLB3_Type(Integer32):
    """Custom type alRRLB3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRRLB3_Type.__name__ = "Integer32"
_AlRRLB3_Object = MibScalar
alRRLB3 = _AlRRLB3_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 11, 6),
    _AlRRLB3_Type()
)
alRRLB3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRRLB3.setStatus("mandatory")
_AlR_Line4_ObjectIdentity = ObjectIdentity
alR_Line4 = _AlR_Line4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 12)
)


class _AlRLOSS4_Type(Integer32):
    """Custom type alRLOSS4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlRLOSS4_Type.__name__ = "Integer32"
_AlRLOSS4_Object = MibScalar
alRLOSS4 = _AlRLOSS4_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 12, 1),
    _AlRLOSS4_Type()
)
alRLOSS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRLOSS4.setStatus("mandatory")


class _AlRILOSS4_Type(Integer32):
    """Custom type alRILOSS4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRILOSS4_Type.__name__ = "Integer32"
_AlRILOSS4_Object = MibScalar
alRILOSS4 = _AlRILOSS4_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 12, 2),
    _AlRILOSS4_Type()
)
alRILOSS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRILOSS4.setStatus("mandatory")


class _AlRAIS4_Type(Integer32):
    """Custom type alRAIS4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlRAIS4_Type.__name__ = "Integer32"
_AlRAIS4_Object = MibScalar
alRAIS4 = _AlRAIS4_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 12, 3),
    _AlRAIS4_Type()
)
alRAIS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRAIS4.setStatus("mandatory")


class _AlRAISL4_Type(Integer32):
    """Custom type alRAISL4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRAISL4_Type.__name__ = "Integer32"
_AlRAISL4_Object = MibScalar
alRAISL4 = _AlRAISL4_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 12, 4),
    _AlRAISL4_Type()
)
alRAISL4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRAISL4.setStatus("mandatory")


class _AlRLLB4_Type(Integer32):
    """Custom type alRLLB4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRLLB4_Type.__name__ = "Integer32"
_AlRLLB4_Object = MibScalar
alRLLB4 = _AlRLLB4_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 12, 5),
    _AlRLLB4_Type()
)
alRLLB4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRLLB4.setStatus("mandatory")


class _AlRRLB4_Type(Integer32):
    """Custom type alRRLB4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRRLB4_Type.__name__ = "Integer32"
_AlRRLB4_Object = MibScalar
alRRLB4 = _AlRRLB4_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 12, 6),
    _AlRRLB4_Type()
)
alRRLB4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRRLB4.setStatus("mandatory")
_AlR_Line5_ObjectIdentity = ObjectIdentity
alR_Line5 = _AlR_Line5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 13)
)


class _AlRLOSS5_Type(Integer32):
    """Custom type alRLOSS5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlRLOSS5_Type.__name__ = "Integer32"
_AlRLOSS5_Object = MibScalar
alRLOSS5 = _AlRLOSS5_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 13, 1),
    _AlRLOSS5_Type()
)
alRLOSS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRLOSS5.setStatus("mandatory")


class _AlRILOSS5_Type(Integer32):
    """Custom type alRILOSS5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRILOSS5_Type.__name__ = "Integer32"
_AlRILOSS5_Object = MibScalar
alRILOSS5 = _AlRILOSS5_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 13, 2),
    _AlRILOSS5_Type()
)
alRILOSS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRILOSS5.setStatus("mandatory")


class _AlRAIS5_Type(Integer32):
    """Custom type alRAIS5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlRAIS5_Type.__name__ = "Integer32"
_AlRAIS5_Object = MibScalar
alRAIS5 = _AlRAIS5_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 13, 3),
    _AlRAIS5_Type()
)
alRAIS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRAIS5.setStatus("mandatory")


class _AlRAISL5_Type(Integer32):
    """Custom type alRAISL5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRAISL5_Type.__name__ = "Integer32"
_AlRAISL5_Object = MibScalar
alRAISL5 = _AlRAISL5_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 13, 4),
    _AlRAISL5_Type()
)
alRAISL5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRAISL5.setStatus("mandatory")


class _AlRLLB5_Type(Integer32):
    """Custom type alRLLB5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRLLB5_Type.__name__ = "Integer32"
_AlRLLB5_Object = MibScalar
alRLLB5 = _AlRLLB5_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 13, 5),
    _AlRLLB5_Type()
)
alRLLB5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRLLB5.setStatus("mandatory")


class _AlRRLB5_Type(Integer32):
    """Custom type alRRLB5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRRLB5_Type.__name__ = "Integer32"
_AlRRLB5_Object = MibScalar
alRRLB5 = _AlRRLB5_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 13, 6),
    _AlRRLB5_Type()
)
alRRLB5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRRLB5.setStatus("mandatory")
_AlR_Line6_ObjectIdentity = ObjectIdentity
alR_Line6 = _AlR_Line6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 14)
)


class _AlRLOSS6_Type(Integer32):
    """Custom type alRLOSS6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlRLOSS6_Type.__name__ = "Integer32"
_AlRLOSS6_Object = MibScalar
alRLOSS6 = _AlRLOSS6_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 14, 1),
    _AlRLOSS6_Type()
)
alRLOSS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRLOSS6.setStatus("mandatory")


class _AlRILOSS6_Type(Integer32):
    """Custom type alRILOSS6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRILOSS6_Type.__name__ = "Integer32"
_AlRILOSS6_Object = MibScalar
alRILOSS6 = _AlRILOSS6_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 14, 2),
    _AlRILOSS6_Type()
)
alRILOSS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRILOSS6.setStatus("mandatory")


class _AlRAIS6_Type(Integer32):
    """Custom type alRAIS6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlRAIS6_Type.__name__ = "Integer32"
_AlRAIS6_Object = MibScalar
alRAIS6 = _AlRAIS6_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 14, 3),
    _AlRAIS6_Type()
)
alRAIS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRAIS6.setStatus("mandatory")


class _AlRAISL6_Type(Integer32):
    """Custom type alRAISL6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRAISL6_Type.__name__ = "Integer32"
_AlRAISL6_Object = MibScalar
alRAISL6 = _AlRAISL6_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 14, 4),
    _AlRAISL6_Type()
)
alRAISL6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRAISL6.setStatus("mandatory")


class _AlRLLB6_Type(Integer32):
    """Custom type alRLLB6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRLLB6_Type.__name__ = "Integer32"
_AlRLLB6_Object = MibScalar
alRLLB6 = _AlRLLB6_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 14, 5),
    _AlRLLB6_Type()
)
alRLLB6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRLLB6.setStatus("mandatory")


class _AlRRLB6_Type(Integer32):
    """Custom type alRRLB6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRRLB6_Type.__name__ = "Integer32"
_AlRRLB6_Object = MibScalar
alRRLB6 = _AlRRLB6_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 14, 6),
    _AlRRLB6_Type()
)
alRRLB6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRRLB6.setStatus("mandatory")
_AlR_Line7_ObjectIdentity = ObjectIdentity
alR_Line7 = _AlR_Line7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 15)
)


class _AlRLOSS7_Type(Integer32):
    """Custom type alRLOSS7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlRLOSS7_Type.__name__ = "Integer32"
_AlRLOSS7_Object = MibScalar
alRLOSS7 = _AlRLOSS7_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 15, 1),
    _AlRLOSS7_Type()
)
alRLOSS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRLOSS7.setStatus("mandatory")


class _AlRILOSS7_Type(Integer32):
    """Custom type alRILOSS7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRILOSS7_Type.__name__ = "Integer32"
_AlRILOSS7_Object = MibScalar
alRILOSS7 = _AlRILOSS7_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 15, 2),
    _AlRILOSS7_Type()
)
alRILOSS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRILOSS7.setStatus("mandatory")


class _AlRAIS7_Type(Integer32):
    """Custom type alRAIS7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlRAIS7_Type.__name__ = "Integer32"
_AlRAIS7_Object = MibScalar
alRAIS7 = _AlRAIS7_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 15, 3),
    _AlRAIS7_Type()
)
alRAIS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRAIS7.setStatus("mandatory")


class _AlRAISL7_Type(Integer32):
    """Custom type alRAISL7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRAISL7_Type.__name__ = "Integer32"
_AlRAISL7_Object = MibScalar
alRAISL7 = _AlRAISL7_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 15, 4),
    _AlRAISL7_Type()
)
alRAISL7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRAISL7.setStatus("mandatory")


class _AlRLLB7_Type(Integer32):
    """Custom type alRLLB7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRLLB7_Type.__name__ = "Integer32"
_AlRLLB7_Object = MibScalar
alRLLB7 = _AlRLLB7_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 15, 5),
    _AlRLLB7_Type()
)
alRLLB7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRLLB7.setStatus("mandatory")


class _AlRRLB7_Type(Integer32):
    """Custom type alRRLB7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRRLB7_Type.__name__ = "Integer32"
_AlRRLB7_Object = MibScalar
alRRLB7 = _AlRRLB7_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 15, 6),
    _AlRRLB7_Type()
)
alRRLB7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRRLB7.setStatus("mandatory")
_AlR_Line8_ObjectIdentity = ObjectIdentity
alR_Line8 = _AlR_Line8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 16)
)


class _AlRLOSS8_Type(Integer32):
    """Custom type alRLOSS8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlRLOSS8_Type.__name__ = "Integer32"
_AlRLOSS8_Object = MibScalar
alRLOSS8 = _AlRLOSS8_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 16, 1),
    _AlRLOSS8_Type()
)
alRLOSS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRLOSS8.setStatus("mandatory")


class _AlRILOSS8_Type(Integer32):
    """Custom type alRILOSS8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRILOSS8_Type.__name__ = "Integer32"
_AlRILOSS8_Object = MibScalar
alRILOSS8 = _AlRILOSS8_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 16, 2),
    _AlRILOSS8_Type()
)
alRILOSS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRILOSS8.setStatus("mandatory")


class _AlRAIS8_Type(Integer32):
    """Custom type alRAIS8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlRAIS8_Type.__name__ = "Integer32"
_AlRAIS8_Object = MibScalar
alRAIS8 = _AlRAIS8_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 16, 3),
    _AlRAIS8_Type()
)
alRAIS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRAIS8.setStatus("mandatory")


class _AlRAISL8_Type(Integer32):
    """Custom type alRAISL8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRAISL8_Type.__name__ = "Integer32"
_AlRAISL8_Object = MibScalar
alRAISL8 = _AlRAISL8_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 16, 4),
    _AlRAISL8_Type()
)
alRAISL8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRAISL8.setStatus("mandatory")


class _AlRLLB8_Type(Integer32):
    """Custom type alRLLB8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRLLB8_Type.__name__ = "Integer32"
_AlRLLB8_Object = MibScalar
alRLLB8 = _AlRLLB8_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 16, 5),
    _AlRLLB8_Type()
)
alRLLB8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRLLB8.setStatus("mandatory")


class _AlRRLB8_Type(Integer32):
    """Custom type alRRLB8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRRLB8_Type.__name__ = "Integer32"
_AlRRLB8_Object = MibScalar
alRRLB8 = _AlRRLB8_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 16, 6),
    _AlRRLB8_Type()
)
alRRLB8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRRLB8.setStatus("mandatory")
_AlR_Line9_ObjectIdentity = ObjectIdentity
alR_Line9 = _AlR_Line9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 17)
)


class _AlRLOSS9_Type(Integer32):
    """Custom type alRLOSS9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlRLOSS9_Type.__name__ = "Integer32"
_AlRLOSS9_Object = MibScalar
alRLOSS9 = _AlRLOSS9_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 17, 1),
    _AlRLOSS9_Type()
)
alRLOSS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRLOSS9.setStatus("mandatory")


class _AlRILOSS9_Type(Integer32):
    """Custom type alRILOSS9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRILOSS9_Type.__name__ = "Integer32"
_AlRILOSS9_Object = MibScalar
alRILOSS9 = _AlRILOSS9_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 17, 2),
    _AlRILOSS9_Type()
)
alRILOSS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRILOSS9.setStatus("mandatory")


class _AlRAIS9_Type(Integer32):
    """Custom type alRAIS9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlRAIS9_Type.__name__ = "Integer32"
_AlRAIS9_Object = MibScalar
alRAIS9 = _AlRAIS9_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 17, 3),
    _AlRAIS9_Type()
)
alRAIS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRAIS9.setStatus("mandatory")


class _AlRAISL9_Type(Integer32):
    """Custom type alRAISL9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRAISL9_Type.__name__ = "Integer32"
_AlRAISL9_Object = MibScalar
alRAISL9 = _AlRAISL9_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 17, 4),
    _AlRAISL9_Type()
)
alRAISL9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRAISL9.setStatus("mandatory")


class _AlRLLB9_Type(Integer32):
    """Custom type alRLLB9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRLLB9_Type.__name__ = "Integer32"
_AlRLLB9_Object = MibScalar
alRLLB9 = _AlRLLB9_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 17, 5),
    _AlRLLB9_Type()
)
alRLLB9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRLLB9.setStatus("mandatory")


class _AlRRLB9_Type(Integer32):
    """Custom type alRRLB9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRRLB9_Type.__name__ = "Integer32"
_AlRRLB9_Object = MibScalar
alRRLB9 = _AlRRLB9_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 17, 6),
    _AlRRLB9_Type()
)
alRRLB9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRRLB9.setStatus("mandatory")
_AlR_Line10_ObjectIdentity = ObjectIdentity
alR_Line10 = _AlR_Line10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 18)
)


class _AlRLOSS10_Type(Integer32):
    """Custom type alRLOSS10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlRLOSS10_Type.__name__ = "Integer32"
_AlRLOSS10_Object = MibScalar
alRLOSS10 = _AlRLOSS10_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 18, 1),
    _AlRLOSS10_Type()
)
alRLOSS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRLOSS10.setStatus("mandatory")


class _AlRILOSS10_Type(Integer32):
    """Custom type alRILOSS10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRILOSS10_Type.__name__ = "Integer32"
_AlRILOSS10_Object = MibScalar
alRILOSS10 = _AlRILOSS10_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 18, 2),
    _AlRILOSS10_Type()
)
alRILOSS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRILOSS10.setStatus("mandatory")


class _AlRAIS10_Type(Integer32):
    """Custom type alRAIS10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlRAIS10_Type.__name__ = "Integer32"
_AlRAIS10_Object = MibScalar
alRAIS10 = _AlRAIS10_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 18, 3),
    _AlRAIS10_Type()
)
alRAIS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRAIS10.setStatus("mandatory")


class _AlRAISL10_Type(Integer32):
    """Custom type alRAISL10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRAISL10_Type.__name__ = "Integer32"
_AlRAISL10_Object = MibScalar
alRAISL10 = _AlRAISL10_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 18, 4),
    _AlRAISL10_Type()
)
alRAISL10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRAISL10.setStatus("mandatory")


class _AlRLLB10_Type(Integer32):
    """Custom type alRLLB10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRLLB10_Type.__name__ = "Integer32"
_AlRLLB10_Object = MibScalar
alRLLB10 = _AlRLLB10_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 18, 5),
    _AlRLLB10_Type()
)
alRLLB10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRLLB10.setStatus("mandatory")


class _AlRRLB10_Type(Integer32):
    """Custom type alRRLB10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRRLB10_Type.__name__ = "Integer32"
_AlRRLB10_Object = MibScalar
alRRLB10 = _AlRRLB10_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 18, 6),
    _AlRRLB10_Type()
)
alRRLB10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRRLB10.setStatus("mandatory")
_AlR_Line11_ObjectIdentity = ObjectIdentity
alR_Line11 = _AlR_Line11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 19)
)


class _AlRLOSS11_Type(Integer32):
    """Custom type alRLOSS11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlRLOSS11_Type.__name__ = "Integer32"
_AlRLOSS11_Object = MibScalar
alRLOSS11 = _AlRLOSS11_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 19, 1),
    _AlRLOSS11_Type()
)
alRLOSS11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRLOSS11.setStatus("mandatory")


class _AlRILOSS11_Type(Integer32):
    """Custom type alRILOSS11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRILOSS11_Type.__name__ = "Integer32"
_AlRILOSS11_Object = MibScalar
alRILOSS11 = _AlRILOSS11_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 19, 2),
    _AlRILOSS11_Type()
)
alRILOSS11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRILOSS11.setStatus("mandatory")


class _AlRAIS11_Type(Integer32):
    """Custom type alRAIS11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlRAIS11_Type.__name__ = "Integer32"
_AlRAIS11_Object = MibScalar
alRAIS11 = _AlRAIS11_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 19, 3),
    _AlRAIS11_Type()
)
alRAIS11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRAIS11.setStatus("mandatory")


class _AlRAISL11_Type(Integer32):
    """Custom type alRAISL11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRAISL11_Type.__name__ = "Integer32"
_AlRAISL11_Object = MibScalar
alRAISL11 = _AlRAISL11_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 19, 4),
    _AlRAISL11_Type()
)
alRAISL11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRAISL11.setStatus("mandatory")


class _AlRLLB11_Type(Integer32):
    """Custom type alRLLB11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRLLB11_Type.__name__ = "Integer32"
_AlRLLB11_Object = MibScalar
alRLLB11 = _AlRLLB11_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 19, 5),
    _AlRLLB11_Type()
)
alRLLB11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRLLB11.setStatus("mandatory")


class _AlRRLB11_Type(Integer32):
    """Custom type alRRLB11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRRLB11_Type.__name__ = "Integer32"
_AlRRLB11_Object = MibScalar
alRRLB11 = _AlRRLB11_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 19, 6),
    _AlRRLB11_Type()
)
alRRLB11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRRLB11.setStatus("mandatory")
_AlR_Line12_ObjectIdentity = ObjectIdentity
alR_Line12 = _AlR_Line12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 20)
)


class _AlRLOSS12_Type(Integer32):
    """Custom type alRLOSS12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlRLOSS12_Type.__name__ = "Integer32"
_AlRLOSS12_Object = MibScalar
alRLOSS12 = _AlRLOSS12_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 20, 1),
    _AlRLOSS12_Type()
)
alRLOSS12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRLOSS12.setStatus("mandatory")


class _AlRILOSS12_Type(Integer32):
    """Custom type alRILOSS12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRILOSS12_Type.__name__ = "Integer32"
_AlRILOSS12_Object = MibScalar
alRILOSS12 = _AlRILOSS12_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 20, 2),
    _AlRILOSS12_Type()
)
alRILOSS12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRILOSS12.setStatus("mandatory")


class _AlRAIS12_Type(Integer32):
    """Custom type alRAIS12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlRAIS12_Type.__name__ = "Integer32"
_AlRAIS12_Object = MibScalar
alRAIS12 = _AlRAIS12_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 20, 3),
    _AlRAIS12_Type()
)
alRAIS12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRAIS12.setStatus("mandatory")


class _AlRAISL12_Type(Integer32):
    """Custom type alRAISL12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRAISL12_Type.__name__ = "Integer32"
_AlRAISL12_Object = MibScalar
alRAISL12 = _AlRAISL12_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 20, 4),
    _AlRAISL12_Type()
)
alRAISL12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRAISL12.setStatus("mandatory")


class _AlRLLB12_Type(Integer32):
    """Custom type alRLLB12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRLLB12_Type.__name__ = "Integer32"
_AlRLLB12_Object = MibScalar
alRLLB12 = _AlRLLB12_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 20, 5),
    _AlRLLB12_Type()
)
alRLLB12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRLLB12.setStatus("mandatory")


class _AlRRLB12_Type(Integer32):
    """Custom type alRRLB12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlRRLB12_Type.__name__ = "Integer32"
_AlRRLB12_Object = MibScalar
alRRLB12 = _AlRRLB12_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 3, 20, 6),
    _AlRRLB12_Type()
)
alRRLB12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alRRLB12.setStatus("mandatory")
_AlRRLTrap_ObjectIdentity = ObjectIdentity
alRRLTrap = _AlRRLTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 4)
)


class _AlLast_Message_Type(DisplayString):
    """Custom type alLast_Message based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_AlLast_Message_Type.__name__ = "DisplayString"
_AlLast_Message_Object = MibScalar
alLast_Message = _AlLast_Message_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 1, 4, 1),
    _AlLast_Message_Type()
)
alLast_Message.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alLast_Message.setStatus("mandatory")
_AlNMS_ObjectIdentity = ObjectIdentity
alNMS = _AlNMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 2)
)
_TrapParam_ObjectIdentity = ObjectIdentity
trapParam = _TrapParam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 1, 2, 1)
)


class _NmsTrapTime_Type(DisplayString):
    """Custom type nmsTrapTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NmsTrapTime_Type.__name__ = "DisplayString"
_NmsTrapTime_Object = MibScalar
nmsTrapTime = _NmsTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 2, 1, 1),
    _NmsTrapTime_Type()
)
nmsTrapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsTrapTime.setStatus("mandatory")


class _TrapSequence_Type(DisplayString):
    """Custom type trapSequence based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_TrapSequence_Type.__name__ = "DisplayString"
_TrapSequence_Object = MibScalar
trapSequence = _TrapSequence_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 2, 1, 2),
    _TrapSequence_Type()
)
trapSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSequence.setStatus("mandatory")


class _MwRouteID_Type(DisplayString):
    """Custom type mwRouteID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_MwRouteID_Type.__name__ = "DisplayString"
_MwRouteID_Object = MibScalar
mwRouteID = _MwRouteID_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 2, 1, 3),
    _MwRouteID_Type()
)
mwRouteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRouteID.setStatus("mandatory")


class _StationID_Type(DisplayString):
    """Custom type stationID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_StationID_Type.__name__ = "DisplayString"
_StationID_Object = MibScalar
stationID = _StationID_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 2, 1, 4),
    _StationID_Type()
)
stationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationID.setStatus("mandatory")


class _StationName_Type(DisplayString):
    """Custom type stationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_StationName_Type.__name__ = "DisplayString"
_StationName_Object = MibScalar
stationName = _StationName_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 2, 1, 5),
    _StationName_Type()
)
stationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationName.setStatus("mandatory")


class _MgmtGWaddr_Type(DisplayString):
    """Custom type mgmtGWaddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_MgmtGWaddr_Type.__name__ = "DisplayString"
_MgmtGWaddr_Object = MibScalar
mgmtGWaddr = _MgmtGWaddr_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 2, 1, 6),
    _MgmtGWaddr_Type()
)
mgmtGWaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtGWaddr.setStatus("mandatory")


class _LineID_Type(DisplayString):
    """Custom type lineID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_LineID_Type.__name__ = "DisplayString"
_LineID_Object = MibScalar
lineID = _LineID_Object(
    (1, 3, 6, 1, 4, 1, 12140, 1, 2, 1, 7),
    _LineID_Type()
)
lineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineID.setStatus("mandatory")
_AlMP_ObjectIdentity = ObjectIdentity
alMP = _AlMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 2)
)
_AlMPStatusLED_ObjectIdentity = ObjectIdentity
alMPStatusLED = _AlMPStatusLED_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 2, 1)
)


class _AlMPEHW_Type(Integer32):
    """Custom type alMPEHW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlMPEHW_Type.__name__ = "Integer32"
_AlMPEHW_Object = MibScalar
alMPEHW = _AlMPEHW_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 1, 1),
    _AlMPEHW_Type()
)
alMPEHW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPEHW.setStatus("mandatory")


class _AlMPESR_Type(Integer32):
    """Custom type alMPESR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlMPESR_Type.__name__ = "Integer32"
_AlMPESR_Object = MibScalar
alMPESR = _AlMPESR_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 1, 2),
    _AlMPESR_Type()
)
alMPESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPESR.setStatus("mandatory")


class _AlMPESL_Type(Integer32):
    """Custom type alMPESL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlMPESL_Type.__name__ = "Integer32"
_AlMPESL_Object = MibScalar
alMPESL = _AlMPESL_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 1, 3),
    _AlMPESL_Type()
)
alMPESL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPESL.setStatus("mandatory")


class _AlMPCA_Type(Integer32):
    """Custom type alMPCA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlMPCA_Type.__name__ = "Integer32"
_AlMPCA_Object = MibScalar
alMPCA = _AlMPCA_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 1, 4),
    _AlMPCA_Type()
)
alMPCA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPCA.setStatus("mandatory")
_AlMPGeneral_ObjectIdentity = ObjectIdentity
alMPGeneral = _AlMPGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 2, 2)
)


class _AlMPSupervisor_Type(Integer32):
    """Custom type alMPSupervisor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("alcoma", 5),
          ("local", 2),
          ("network", 3),
          ("none", 0),
          ("offline", -1),
          ("service", 4),
          ("terminal", 1))
    )


_AlMPSupervisor_Type.__name__ = "Integer32"
_AlMPSupervisor_Object = MibScalar
alMPSupervisor = _AlMPSupervisor_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 2, 1),
    _AlMPSupervisor_Type()
)
alMPSupervisor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPSupervisor.setStatus("mandatory")


class _AlMPConfiguration_Type(Integer32):
    """Custom type alMPConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("cf1xE1-Ethernet", 4),
          ("cf1xE2", 3),
          ("cf1xE3-E1", 7),
          ("cf1xEthF", 18),
          ("cf1xEthF-1xE1", 19),
          ("cf1xEthF-2xE1", 20),
          ("cf1xEthF-3xE1", 21),
          ("cf1xEthF-4xE1", 22),
          ("cf1xEthF-5xE1", 23),
          ("cf1xEthF-6xE1", 24),
          ("cf1xEthF-7xE1", 25),
          ("cf1xEthF-8xE1", 26),
          ("cf1xEthF-E1", 9),
          ("cf1xEthF-E1-1xE1", 10),
          ("cf1xEthF-E1-2xE1", 11),
          ("cf1xEthF-E1-3xE1", 12),
          ("cf1xEthF-E1-4xE1", 13),
          ("cf1xEthF-E1-5xE1", 14),
          ("cf1xEthF-E1-6xE1", 15),
          ("cf1xEthF-E1-7xE1", 16),
          ("cf1xEthF-E1-8xE1", 17),
          ("cf1xEthernet", 8),
          ("cf2xE1", 1),
          ("cf2xFEth", 27),
          ("cf2xFEth-1xE1", 28),
          ("cf2xGEth", 30),
          ("cf2xGEth-SFP100", 31),
          ("cf2xGEth-SFP1000", 32),
          ("cf2xGEth-SFPSG", 33),
          ("cf4xE1", 2),
          ("cf4xFEth-2xE1", 29),
          ("offline", -1),
          ("undefined", 0))
    )


_AlMPConfiguration_Type.__name__ = "Integer32"
_AlMPConfiguration_Object = MibScalar
alMPConfiguration = _AlMPConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 2, 2),
    _AlMPConfiguration_Type()
)
alMPConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPConfiguration.setStatus("mandatory")


class _AlMPStatus_Type(Integer32):
    """Custom type alMPStatus based on Integer32"""
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
        *(("error", 3),
          ("offline", 0),
          ("ok", 1),
          ("warning", 2))
    )


_AlMPStatus_Type.__name__ = "Integer32"
_AlMPStatus_Object = MibScalar
alMPStatus = _AlMPStatus_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 2, 3),
    _AlMPStatus_Type()
)
alMPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPStatus.setStatus("mandatory")


class _AlMPHistory_Type(Integer32):
    """Custom type alMPHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlMPHistory_Type.__name__ = "Integer32"
_AlMPHistory_Object = MibScalar
alMPHistory = _AlMPHistory_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 2, 4),
    _AlMPHistory_Type()
)
alMPHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPHistory.setStatus("mandatory")


class _AlMPIAISL_Type(Integer32):
    """Custom type alMPIAISL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlMPIAISL_Type.__name__ = "Integer32"
_AlMPIAISL_Object = MibScalar
alMPIAISL = _AlMPIAISL_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 2, 5),
    _AlMPIAISL_Type()
)
alMPIAISL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPIAISL.setStatus("mandatory")


class _AlMPILEVPWR_Type(Integer32):
    """Custom type alMPILEVPWR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlMPILEVPWR_Type.__name__ = "Integer32"
_AlMPILEVPWR_Object = MibScalar
alMPILEVPWR = _AlMPILEVPWR_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 2, 6),
    _AlMPILEVPWR_Type()
)
alMPILEVPWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPILEVPWR.setStatus("mandatory")
_AlMPODU_ObjectIdentity = ObjectIdentity
alMPODU = _AlMPODU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 2, 3)
)


class _AlMPTuneTX_Type(DisplayString):
    """Custom type alMPTuneTX based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_AlMPTuneTX_Type.__name__ = "DisplayString"
_AlMPTuneTX_Object = MibScalar
alMPTuneTX = _AlMPTuneTX_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 3, 1),
    _AlMPTuneTX_Type()
)
alMPTuneTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPTuneTX.setStatus("mandatory")


class _AlMPTuneRX_Type(DisplayString):
    """Custom type alMPTuneRX based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_AlMPTuneRX_Type.__name__ = "DisplayString"
_AlMPTuneRX_Object = MibScalar
alMPTuneRX = _AlMPTuneRX_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 3, 2),
    _AlMPTuneRX_Type()
)
alMPTuneRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPTuneRX.setStatus("mandatory")


class _AlMPTX_PWR_Type(Integer32):
    """Custom type alMPTX_PWR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -128
        )
    )
    namedValues = NamedValues(
        ("offline", -128)
    )


_AlMPTX_PWR_Type.__name__ = "Integer32"
_AlMPTX_PWR_Object = MibScalar
alMPTX_PWR = _AlMPTX_PWR_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 3, 3),
    _AlMPTX_PWR_Type()
)
alMPTX_PWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPTX_PWR.setStatus("mandatory")


class _AlMPRX_Level_Type(Integer32):
    """Custom type alMPRX_Level based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -128
        )
    )
    namedValues = NamedValues(
        ("offline", -128)
    )


_AlMPRX_Level_Type.__name__ = "Integer32"
_AlMPRX_Level_Object = MibScalar
alMPRX_Level = _AlMPRX_Level_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 3, 4),
    _AlMPRX_Level_Type()
)
alMPRX_Level.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPRX_Level.setStatus("mandatory")


class _AlMPTX_PWRAlrm_Type(Integer32):
    """Custom type alMPTX_PWRAlrm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("offline", -1),
          ("ok", 0),
          ("out", 1))
    )


_AlMPTX_PWRAlrm_Type.__name__ = "Integer32"
_AlMPTX_PWRAlrm_Object = MibScalar
alMPTX_PWRAlrm = _AlMPTX_PWRAlrm_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 3, 5),
    _AlMPTX_PWRAlrm_Type()
)
alMPTX_PWRAlrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPTX_PWRAlrm.setStatus("mandatory")


class _AlMPRX_LevelAlrm_Type(Integer32):
    """Custom type alMPRX_LevelAlrm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlMPRX_LevelAlrm_Type.__name__ = "Integer32"
_AlMPRX_LevelAlrm_Object = MibScalar
alMPRX_LevelAlrm = _AlMPRX_LevelAlrm_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 3, 6),
    _AlMPRX_LevelAlrm_Type()
)
alMPRX_LevelAlrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPRX_LevelAlrm.setStatus("mandatory")


class _AlMPMode_TX_Type(Integer32):
    """Custom type alMPMode_TX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atpc", 2),
          ("manual", 1),
          ("off", 0),
          ("offline", -1))
    )


_AlMPMode_TX_Type.__name__ = "Integer32"
_AlMPMode_TX_Object = MibScalar
alMPMode_TX = _AlMPMode_TX_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 3, 7),
    _AlMPMode_TX_Type()
)
alMPMode_TX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPMode_TX.setStatus("mandatory")


class _AlMPODU_LB_Type(Integer32):
    """Custom type alMPODU_LB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlMPODU_LB_Type.__name__ = "Integer32"
_AlMPODU_LB_Object = MibScalar
alMPODU_LB = _AlMPODU_LB_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 3, 8),
    _AlMPODU_LB_Type()
)
alMPODU_LB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPODU_LB.setStatus("mandatory")


class _AlMPTemperature_Type(Integer32):
    """Custom type alMPTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("offline", -1)
    )


_AlMPTemperature_Type.__name__ = "Integer32"
_AlMPTemperature_Object = MibScalar
alMPTemperature = _AlMPTemperature_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 3, 9),
    _AlMPTemperature_Type()
)
alMPTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPTemperature.setStatus("mandatory")
_AlMPModem_ObjectIdentity = ObjectIdentity
alMPModem = _AlMPModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 2, 4)
)


class _AlMPQuality_Type(Integer32):
    """Custom type alMPQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("offline", -1)
    )


_AlMPQuality_Type.__name__ = "Integer32"
_AlMPQuality_Object = MibScalar
alMPQuality = _AlMPQuality_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 4, 1),
    _AlMPQuality_Type()
)
alMPQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPQuality.setStatus("mandatory")


class _AlMPSNR_Type(DisplayString):
    """Custom type alMPSNR based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_AlMPSNR_Type.__name__ = "DisplayString"
_AlMPSNR_Object = MibScalar
alMPSNR = _AlMPSNR_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 4, 2),
    _AlMPSNR_Type()
)
alMPSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPSNR.setStatus("mandatory")


class _AlMPQualityAlrm_Type(Integer32):
    """Custom type alMPQualityAlrm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("offline", -1),
          ("ok", 0),
          ("out", 1))
    )


_AlMPQualityAlrm_Type.__name__ = "Integer32"
_AlMPQualityAlrm_Object = MibScalar
alMPQualityAlrm = _AlMPQualityAlrm_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 4, 3),
    _AlMPQualityAlrm_Type()
)
alMPQualityAlrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPQualityAlrm.setStatus("mandatory")


class _AlMPSNRAlrm_Type(Integer32):
    """Custom type alMPSNRAlrm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlMPSNRAlrm_Type.__name__ = "Integer32"
_AlMPSNRAlrm_Object = MibScalar
alMPSNRAlrm = _AlMPSNRAlrm_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 4, 4),
    _AlMPSNRAlrm_Type()
)
alMPSNRAlrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPSNRAlrm.setStatus("mandatory")


class _AlMPRate_Type(Integer32):
    """Custom type alMPRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62)
        )
    )
    namedValues = NamedValues(
        *(("ndef", 0),
          ("offline", -1),
          ("r100Mbps", 27),
          ("r102Mbps", 58),
          ("r10Mbps1", 7),
          ("r116Mbps", 47),
          ("r119Mbps", 59),
          ("r11Mbps", 15),
          ("r123Mbps", 28),
          ("r1250Mbps", 44),
          ("r127Mbps", 60),
          ("r137Mbps", 61),
          ("r149Mbps", 48),
          ("r14Mbps", 11),
          ("r158Mbps", 29),
          ("r165Mbps", 34),
          ("r168Mbps", 30),
          ("r16Mbps", 19),
          ("r16Mbps1", 3),
          ("r178Mbps", 42),
          ("r179Mbps", 9),
          ("r17Mbps", 38),
          ("r183Mbps", 49),
          ("r186Mbps", 43),
          ("r19Mbps", 37),
          ("r200Mbps", 2),
          ("r20Mbps1", 6),
          ("r216Mbps", 50),
          ("r22Mbps", 14),
          ("r230Mbps", 10),
          ("r249Mbps", 51),
          ("r25Mbps", 33),
          ("r282Mbps", 4),
          ("r300Mbps", 1),
          ("r30Mbps", 39),
          ("r31Mbps", 52),
          ("r32Mbps2", 12),
          ("r333Mbps", 22),
          ("r33Mbps", 18),
          ("r34Mbps", 40),
          ("r355Mbps", 23),
          ("r35Mbps", 32),
          ("r384Mbps", 24),
          ("r39Mbps", 36),
          ("r40Mbps1", 5),
          ("r41Mbps", 53),
          ("r44Mbps", 13),
          ("r50Mbps", 25),
          ("r58Mbps", 46),
          ("r59Mbps", 54),
          ("r5Mbps", 16),
          ("r5Mbps1", 8),
          ("r60Mbps", 41),
          ("r61Mbps", 35),
          ("r64Mbps", 55),
          ("r66Mbps", 17),
          ("r69Mbps", 56),
          ("r70Mbps", 45),
          ("r72Mbps", 26),
          ("r77Mbps", 31),
          ("r80Mbps", 21),
          ("r83Mbps", 57),
          ("r89Mbps", 62),
          ("r8Mbps", 20))
    )


_AlMPRate_Type.__name__ = "Integer32"
_AlMPRate_Object = MibScalar
alMPRate = _AlMPRate_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 4, 5),
    _AlMPRate_Type()
)
alMPRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPRate.setStatus("mandatory")


class _AlMPQAM_Type(Integer32):
    """Custom type alMPQAM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("mp128QAM", 10),
          ("mp16QAM1", 5),
          ("mp16QAM2", 7),
          ("mp256QAM", 11),
          ("mp32QAM", 8),
          ("mp4FSK", 1),
          ("mp4QAM1", 3),
          ("mp4QAM2", 6),
          ("mp64QAM", 9),
          ("mp8QAM", 4),
          ("mpQPSK", 2),
          ("ndef", 0),
          ("offline", -1))
    )


_AlMPQAM_Type.__name__ = "Integer32"
_AlMPQAM_Object = MibScalar
alMPQAM = _AlMPQAM_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 4, 6),
    _AlMPQAM_Type()
)
alMPQAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPQAM.setStatus("mandatory")


class _AlMPActiveACM_Type(Integer32):
    """Custom type alMPActiveACM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlMPActiveACM_Type.__name__ = "Integer32"
_AlMPActiveACM_Object = MibScalar
alMPActiveACM = _AlMPActiveACM_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 4, 7),
    _AlMPActiveACM_Type()
)
alMPActiveACM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPActiveACM.setStatus("mandatory")


class _AlMPStatusACM_Type(Integer32):
    """Custom type alMPStatusACM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("normal", 0),
          ("offline", -1))
    )


_AlMPStatusACM_Type.__name__ = "Integer32"
_AlMPStatusACM_Object = MibScalar
alMPStatusACM = _AlMPStatusACM_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 4, 8),
    _AlMPStatusACM_Type()
)
alMPStatusACM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPStatusACM.setStatus("mandatory")
_AlMPSupply_ObjectIdentity = ObjectIdentity
alMPSupply = _AlMPSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 2, 5)
)


class _AlMPInput_Type(Integer32):
    """Custom type alMPInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlMPInput_Type.__name__ = "Integer32"
_AlMPInput_Object = MibScalar
alMPInput = _AlMPInput_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 5, 1),
    _AlMPInput_Type()
)
alMPInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPInput.setStatus("mandatory")
_AlMPRDG_ObjectIdentity = ObjectIdentity
alMPRDG = _AlMPRDG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 2, 6)
)


class _AlMPEEPROM_Type(Integer32):
    """Custom type alMPEEPROM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bad", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlMPEEPROM_Type.__name__ = "Integer32"
_AlMPEEPROM_Object = MibScalar
alMPEEPROM = _AlMPEEPROM_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 6, 1),
    _AlMPEEPROM_Type()
)
alMPEEPROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPEEPROM.setStatus("mandatory")


class _AlMPRAM_Type(Integer32):
    """Custom type alMPRAM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bad", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlMPRAM_Type.__name__ = "Integer32"
_AlMPRAM_Object = MibScalar
alMPRAM = _AlMPRAM_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 6, 2),
    _AlMPRAM_Type()
)
alMPRAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPRAM.setStatus("mandatory")


class _AlMPCommRMT_Type(Integer32):
    """Custom type alMPCommRMT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlMPCommRMT_Type.__name__ = "Integer32"
_AlMPCommRMT_Object = MibScalar
alMPCommRMT = _AlMPCommRMT_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 6, 3),
    _AlMPCommRMT_Type()
)
alMPCommRMT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPCommRMT.setStatus("mandatory")
_AlMPMUX_ObjectIdentity = ObjectIdentity
alMPMUX = _AlMPMUX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 2, 7)
)


class _AlMPBER_Type(DisplayString):
    """Custom type alMPBER based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_AlMPBER_Type.__name__ = "DisplayString"
_AlMPBER_Object = MibScalar
alMPBER = _AlMPBER_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 7, 1),
    _AlMPBER_Type()
)
alMPBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPBER.setStatus("mandatory")


class _AlMPBER_10E6_Type(Integer32):
    """Custom type alMPBER_10E6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlMPBER_10E6_Type.__name__ = "Integer32"
_AlMPBER_10E6_Object = MibScalar
alMPBER_10E6 = _AlMPBER_10E6_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 7, 2),
    _AlMPBER_10E6_Type()
)
alMPBER_10E6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPBER_10E6.setStatus("mandatory")


class _AlMPBER_10E4_Type(Integer32):
    """Custom type alMPBER_10E4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlMPBER_10E4_Type.__name__ = "Integer32"
_AlMPBER_10E4_Object = MibScalar
alMPBER_10E4 = _AlMPBER_10E4_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 7, 3),
    _AlMPBER_10E4_Type()
)
alMPBER_10E4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPBER_10E4.setStatus("mandatory")


class _AlMPFrame_Type(Integer32):
    """Custom type alMPFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loss", 1),
          ("offline", -1),
          ("ok", 0))
    )


_AlMPFrame_Type.__name__ = "Integer32"
_AlMPFrame_Object = MibScalar
alMPFrame = _AlMPFrame_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 7, 4),
    _AlMPFrame_Type()
)
alMPFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPFrame.setStatus("mandatory")
_AlMPLine1_ObjectIdentity = ObjectIdentity
alMPLine1 = _AlMPLine1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 2, 8)
)


class _AlMPLOSS1_Type(Integer32):
    """Custom type alMPLOSS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlMPLOSS1_Type.__name__ = "Integer32"
_AlMPLOSS1_Object = MibScalar
alMPLOSS1 = _AlMPLOSS1_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 8, 1),
    _AlMPLOSS1_Type()
)
alMPLOSS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPLOSS1.setStatus("mandatory")


class _AlMPILOSS1_Type(Integer32):
    """Custom type alMPILOSS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlMPILOSS1_Type.__name__ = "Integer32"
_AlMPILOSS1_Object = MibScalar
alMPILOSS1 = _AlMPILOSS1_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 8, 2),
    _AlMPILOSS1_Type()
)
alMPILOSS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPILOSS1.setStatus("mandatory")


class _AlMPAIS1_Type(Integer32):
    """Custom type alMPAIS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlMPAIS1_Type.__name__ = "Integer32"
_AlMPAIS1_Object = MibScalar
alMPAIS1 = _AlMPAIS1_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 8, 3),
    _AlMPAIS1_Type()
)
alMPAIS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPAIS1.setStatus("mandatory")


class _AlMPAISL1_Type(Integer32):
    """Custom type alMPAISL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlMPAISL1_Type.__name__ = "Integer32"
_AlMPAISL1_Object = MibScalar
alMPAISL1 = _AlMPAISL1_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 8, 4),
    _AlMPAISL1_Type()
)
alMPAISL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPAISL1.setStatus("mandatory")


class _AlMPLLB1_Type(Integer32):
    """Custom type alMPLLB1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlMPLLB1_Type.__name__ = "Integer32"
_AlMPLLB1_Object = MibScalar
alMPLLB1 = _AlMPLLB1_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 8, 5),
    _AlMPLLB1_Type()
)
alMPLLB1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPLLB1.setStatus("mandatory")


class _AlMPRLB1_Type(Integer32):
    """Custom type alMPRLB1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlMPRLB1_Type.__name__ = "Integer32"
_AlMPRLB1_Object = MibScalar
alMPRLB1 = _AlMPRLB1_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 8, 6),
    _AlMPRLB1_Type()
)
alMPRLB1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPRLB1.setStatus("mandatory")
_AlMPLine2_ObjectIdentity = ObjectIdentity
alMPLine2 = _AlMPLine2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 2, 9)
)


class _AlMPLOSS2_Type(Integer32):
    """Custom type alMPLOSS2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlMPLOSS2_Type.__name__ = "Integer32"
_AlMPLOSS2_Object = MibScalar
alMPLOSS2 = _AlMPLOSS2_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 9, 1),
    _AlMPLOSS2_Type()
)
alMPLOSS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPLOSS2.setStatus("mandatory")


class _AlMPILOSS2_Type(Integer32):
    """Custom type alMPILOSS2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlMPILOSS2_Type.__name__ = "Integer32"
_AlMPILOSS2_Object = MibScalar
alMPILOSS2 = _AlMPILOSS2_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 9, 2),
    _AlMPILOSS2_Type()
)
alMPILOSS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPILOSS2.setStatus("mandatory")


class _AlMPLink2_Type(Integer32):
    """Custom type alMPLink2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("offline", -1),
          ("up", 1))
    )


_AlMPLink2_Type.__name__ = "Integer32"
_AlMPLink2_Object = MibScalar
alMPLink2 = _AlMPLink2_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 9, 3),
    _AlMPLink2_Type()
)
alMPLink2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPLink2.setStatus("mandatory")


class _AlMPSpeed2_Type(Integer32):
    """Custom type alMPSpeed2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1000Mbps", 2),
          ("e100Mbps", 1),
          ("e10Mbps", 0),
          ("offline", -1))
    )


_AlMPSpeed2_Type.__name__ = "Integer32"
_AlMPSpeed2_Object = MibScalar
alMPSpeed2 = _AlMPSpeed2_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 9, 4),
    _AlMPSpeed2_Type()
)
alMPSpeed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPSpeed2.setStatus("mandatory")


class _AlMPType2_Type(Integer32):
    """Custom type alMPType2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fullduplex", 1),
          ("halfduplex", 0),
          ("offline", -1))
    )


_AlMPType2_Type.__name__ = "Integer32"
_AlMPType2_Object = MibScalar
alMPType2 = _AlMPType2_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 9, 5),
    _AlMPType2_Type()
)
alMPType2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPType2.setStatus("mandatory")


class _AlMPFlow2_Type(Integer32):
    """Custom type alMPFlow2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlMPFlow2_Type.__name__ = "Integer32"
_AlMPFlow2_Object = MibScalar
alMPFlow2 = _AlMPFlow2_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 9, 6),
    _AlMPFlow2_Type()
)
alMPFlow2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPFlow2.setStatus("mandatory")
_AlMPPktRX2_Type = Unsigned32
_AlMPPktRX2_Object = MibScalar
alMPPktRX2 = _AlMPPktRX2_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 9, 7),
    _AlMPPktRX2_Type()
)
alMPPktRX2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPPktRX2.setStatus("mandatory")
_AlMPByteRX2_Type = Unsigned32
_AlMPByteRX2_Object = MibScalar
alMPByteRX2 = _AlMPByteRX2_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 9, 8),
    _AlMPByteRX2_Type()
)
alMPByteRX2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPByteRX2.setStatus("mandatory")
_AlMPPktTX2_Type = Unsigned32
_AlMPPktTX2_Object = MibScalar
alMPPktTX2 = _AlMPPktTX2_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 9, 9),
    _AlMPPktTX2_Type()
)
alMPPktTX2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPPktTX2.setStatus("mandatory")
_AlMPByteTX2_Type = Unsigned32
_AlMPByteTX2_Object = MibScalar
alMPByteTX2 = _AlMPByteTX2_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 9, 10),
    _AlMPByteTX2_Type()
)
alMPByteTX2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPByteTX2.setStatus("mandatory")
_AlMPError2_Type = Unsigned32
_AlMPError2_Object = MibScalar
alMPError2 = _AlMPError2_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 9, 11),
    _AlMPError2_Type()
)
alMPError2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPError2.setStatus("mandatory")
_AlMPCollision2_Type = Unsigned32
_AlMPCollision2_Object = MibScalar
alMPCollision2 = _AlMPCollision2_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 9, 12),
    _AlMPCollision2_Type()
)
alMPCollision2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPCollision2.setStatus("mandatory")
_AlMPLine3_ObjectIdentity = ObjectIdentity
alMPLine3 = _AlMPLine3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 2, 10)
)


class _AlMPLOSS3_Type(Integer32):
    """Custom type alMPLOSS3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlMPLOSS3_Type.__name__ = "Integer32"
_AlMPLOSS3_Object = MibScalar
alMPLOSS3 = _AlMPLOSS3_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 10, 1),
    _AlMPLOSS3_Type()
)
alMPLOSS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPLOSS3.setStatus("mandatory")


class _AlMPILOSS3_Type(Integer32):
    """Custom type alMPILOSS3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlMPILOSS3_Type.__name__ = "Integer32"
_AlMPILOSS3_Object = MibScalar
alMPILOSS3 = _AlMPILOSS3_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 10, 2),
    _AlMPILOSS3_Type()
)
alMPILOSS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPILOSS3.setStatus("mandatory")


class _AlMPLink3_Type(Integer32):
    """Custom type alMPLink3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("offline", -1),
          ("up", 1))
    )


_AlMPLink3_Type.__name__ = "Integer32"
_AlMPLink3_Object = MibScalar
alMPLink3 = _AlMPLink3_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 10, 3),
    _AlMPLink3_Type()
)
alMPLink3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPLink3.setStatus("mandatory")


class _AlMPSpeed3_Type(Integer32):
    """Custom type alMPSpeed3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1000Mbps", 2),
          ("e100Mbps", 1),
          ("e10Mbps", 0),
          ("offline", -1))
    )


_AlMPSpeed3_Type.__name__ = "Integer32"
_AlMPSpeed3_Object = MibScalar
alMPSpeed3 = _AlMPSpeed3_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 10, 4),
    _AlMPSpeed3_Type()
)
alMPSpeed3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPSpeed3.setStatus("mandatory")


class _AlMPType3_Type(Integer32):
    """Custom type alMPType3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fullduplex", 1),
          ("halfduplex", 0),
          ("offline", -1))
    )


_AlMPType3_Type.__name__ = "Integer32"
_AlMPType3_Object = MibScalar
alMPType3 = _AlMPType3_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 10, 5),
    _AlMPType3_Type()
)
alMPType3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPType3.setStatus("mandatory")


class _AlMPFlow3_Type(Integer32):
    """Custom type alMPFlow3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlMPFlow3_Type.__name__ = "Integer32"
_AlMPFlow3_Object = MibScalar
alMPFlow3 = _AlMPFlow3_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 10, 6),
    _AlMPFlow3_Type()
)
alMPFlow3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPFlow3.setStatus("mandatory")
_AlMPPktRX3_Type = Unsigned32
_AlMPPktRX3_Object = MibScalar
alMPPktRX3 = _AlMPPktRX3_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 10, 7),
    _AlMPPktRX3_Type()
)
alMPPktRX3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPPktRX3.setStatus("mandatory")
_AlMPByteRX3_Type = Unsigned32
_AlMPByteRX3_Object = MibScalar
alMPByteRX3 = _AlMPByteRX3_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 10, 8),
    _AlMPByteRX3_Type()
)
alMPByteRX3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPByteRX3.setStatus("mandatory")
_AlMPPktTX3_Type = Unsigned32
_AlMPPktTX3_Object = MibScalar
alMPPktTX3 = _AlMPPktTX3_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 10, 9),
    _AlMPPktTX3_Type()
)
alMPPktTX3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPPktTX3.setStatus("mandatory")
_AlMPByteTX3_Type = Unsigned32
_AlMPByteTX3_Object = MibScalar
alMPByteTX3 = _AlMPByteTX3_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 10, 10),
    _AlMPByteTX3_Type()
)
alMPByteTX3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPByteTX3.setStatus("mandatory")
_AlMPError3_Type = Unsigned32
_AlMPError3_Object = MibScalar
alMPError3 = _AlMPError3_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 10, 11),
    _AlMPError3_Type()
)
alMPError3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPError3.setStatus("mandatory")
_AlMPCollision3_Type = Unsigned32
_AlMPCollision3_Object = MibScalar
alMPCollision3 = _AlMPCollision3_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 10, 12),
    _AlMPCollision3_Type()
)
alMPCollision3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPCollision3.setStatus("mandatory")
_AlMPLine4_ObjectIdentity = ObjectIdentity
alMPLine4 = _AlMPLine4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12140, 2, 11)
)


class _AlMPLOSS4_Type(Integer32):
    """Custom type alMPLOSS4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not", 0),
          ("offline", -1),
          ("yes", 1))
    )


_AlMPLOSS4_Type.__name__ = "Integer32"
_AlMPLOSS4_Object = MibScalar
alMPLOSS4 = _AlMPLOSS4_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 11, 1),
    _AlMPLOSS4_Type()
)
alMPLOSS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPLOSS4.setStatus("mandatory")


class _AlMPILOSS4_Type(Integer32):
    """Custom type alMPILOSS4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlMPILOSS4_Type.__name__ = "Integer32"
_AlMPILOSS4_Object = MibScalar
alMPILOSS4 = _AlMPILOSS4_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 11, 2),
    _AlMPILOSS4_Type()
)
alMPILOSS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPILOSS4.setStatus("mandatory")


class _AlMPLink4_Type(Integer32):
    """Custom type alMPLink4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("offline", -1),
          ("up", 1))
    )


_AlMPLink4_Type.__name__ = "Integer32"
_AlMPLink4_Object = MibScalar
alMPLink4 = _AlMPLink4_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 11, 3),
    _AlMPLink4_Type()
)
alMPLink4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPLink4.setStatus("mandatory")


class _AlMPSpeed4_Type(Integer32):
    """Custom type alMPSpeed4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1000Mbps", 2),
          ("e100Mbps", 1),
          ("e10Mbps", 0),
          ("offline", -1))
    )


_AlMPSpeed4_Type.__name__ = "Integer32"
_AlMPSpeed4_Object = MibScalar
alMPSpeed4 = _AlMPSpeed4_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 11, 4),
    _AlMPSpeed4_Type()
)
alMPSpeed4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPSpeed4.setStatus("mandatory")


class _AlMPType4_Type(Integer32):
    """Custom type alMPType4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fullduplex", 1),
          ("halfduplex", 0),
          ("offline", -1))
    )


_AlMPType4_Type.__name__ = "Integer32"
_AlMPType4_Object = MibScalar
alMPType4 = _AlMPType4_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 11, 5),
    _AlMPType4_Type()
)
alMPType4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPType4.setStatus("mandatory")


class _AlMPFlow4_Type(Integer32):
    """Custom type alMPFlow4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("offline", -1),
          ("on", 1))
    )


_AlMPFlow4_Type.__name__ = "Integer32"
_AlMPFlow4_Object = MibScalar
alMPFlow4 = _AlMPFlow4_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 11, 6),
    _AlMPFlow4_Type()
)
alMPFlow4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPFlow4.setStatus("mandatory")
_AlMPPktRX4_Type = Unsigned32
_AlMPPktRX4_Object = MibScalar
alMPPktRX4 = _AlMPPktRX4_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 11, 7),
    _AlMPPktRX4_Type()
)
alMPPktRX4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPPktRX4.setStatus("mandatory")
_AlMPByteRX4_Type = Unsigned32
_AlMPByteRX4_Object = MibScalar
alMPByteRX4 = _AlMPByteRX4_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 11, 8),
    _AlMPByteRX4_Type()
)
alMPByteRX4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPByteRX4.setStatus("mandatory")
_AlMPPktTX4_Type = Unsigned32
_AlMPPktTX4_Object = MibScalar
alMPPktTX4 = _AlMPPktTX4_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 11, 9),
    _AlMPPktTX4_Type()
)
alMPPktTX4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPPktTX4.setStatus("mandatory")
_AlMPByteTX4_Type = Unsigned32
_AlMPByteTX4_Object = MibScalar
alMPByteTX4 = _AlMPByteTX4_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 11, 10),
    _AlMPByteTX4_Type()
)
alMPByteTX4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPByteTX4.setStatus("mandatory")
_AlMPError4_Type = Unsigned32
_AlMPError4_Object = MibScalar
alMPError4 = _AlMPError4_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 11, 11),
    _AlMPError4_Type()
)
alMPError4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPError4.setStatus("mandatory")
_AlMPCollision4_Type = Unsigned32
_AlMPCollision4_Object = MibScalar
alMPCollision4 = _AlMPCollision4_Object(
    (1, 3, 6, 1, 4, 1, 12140, 2, 11, 12),
    _AlMPCollision4_Type()
)
alMPCollision4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alMPCollision4.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCOMA-MIB",
    **{"alcoma": alcoma,
       "traps": traps,
       "generalOFF": generalOFF,
       "generalOK": generalOK,
       "generalWAR": generalWAR,
       "generalERR": generalERR,
       "receiverLowAlarmOn": receiverLowAlarmOn,
       "receiverLowAlarmOff": receiverLowAlarmOff,
       "transmitterLowAlarmOn": transmitterLowAlarmOn,
       "transmitterLowAlarmOff": transmitterLowAlarmOff,
       "signalQualityAlarmOn": signalQualityAlarmOn,
       "signalQualityAlarmOff": signalQualityAlarmOff,
       "ber6EAlarmOn": ber6EAlarmOn,
       "ber6EAlarmOff": ber6EAlarmOff,
       "ber4EAlarmOn": ber4EAlarmOn,
       "ber4EAlarmOff": ber4EAlarmOff,
       "inputSupplyAlarmOn": inputSupplyAlarmOn,
       "inputSupplyAlarmOff": inputSupplyAlarmOff,
       "aisFromLineAlarmOn": aisFromLineAlarmOn,
       "aisFromLineAlarmOff": aisFromLineAlarmOff,
       "aisToLineAlarmOn": aisToLineAlarmOn,
       "aisToLineAlarmOff": aisToLineAlarmOff,
       "aisToPdhAlarmOn": aisToPdhAlarmOn,
       "aisToPdhAlarmOff": aisToPdhAlarmOff,
       "lossAtLineAlarmOn": lossAtLineAlarmOn,
       "lossAtLineAlarmOff": lossAtLineAlarmOff,
       "lossAtPdhAlarmOn": lossAtPdhAlarmOn,
       "lossAtPdhAlarmOff": lossAtPdhAlarmOff,
       "lossAtFrameAlarmOn": lossAtFrameAlarmOn,
       "lossAtFrameAlarmOff": lossAtFrameAlarmOff,
       "products": products,
       "alRADIO-RELAY-LINK": alRADIO_RELAY_LINK,
       "alStatusLED": alStatusLED,
       "alEHW": alEHW,
       "alESR": alESR,
       "alESL": alESL,
       "alCA": alCA,
       "local-station": local_station,
       "alL-General": alL_General,
       "alLSupervisor": alLSupervisor,
       "alLConfiguration": alLConfiguration,
       "alLStatus": alLStatus,
       "alLHistory": alLHistory,
       "alLIAISL": alLIAISL,
       "alLILEVPWR": alLILEVPWR,
       "alL-ODU": alL_ODU,
       "alLRX-Level": alLRX_Level,
       "alLTX-PWR": alLTX_PWR,
       "alLMode-TX": alLMode_TX,
       "alLODU-LB": alLODU_LB,
       "alL-Modem": alL_Modem,
       "alLQuality": alLQuality,
       "alL-Supply": alL_Supply,
       "alLVoltage-5V": alLVoltage_5V,
       "alLVoltage-5Vor15V": alLVoltage_5Vor15V,
       "alLVoltage-24V": alLVoltage_24V,
       "alLCurrent-ODU": alLCurrent_ODU,
       "alLInput": alLInput,
       "alL-IDU": alL_IDU,
       "alLEEPROM": alLEEPROM,
       "alLRAM": alLRAM,
       "alLBattery": alLBattery,
       "alLCommIDU": alLCommIDU,
       "alLCommRMT": alLCommRMT,
       "alL-MUX": alL_MUX,
       "alLBER-10E6": alLBER_10E6,
       "alLBER-10E4": alLBER_10E4,
       "alLFrame": alLFrame,
       "alL-PDH1": alL_PDH1,
       "alLPDHFrame": alLPDHFrame,
       "alLAISPDH": alLAISPDH,
       "alLLLBPDH": alLLLBPDH,
       "alLRLBPDH": alLRLBPDH,
       "alL-Line1": alL_Line1,
       "alLOSS1": alLOSS1,
       "alILOSS1": alILOSS1,
       "alAIS1": alAIS1,
       "alAISL1": alAISL1,
       "alLLB1": alLLB1,
       "alRLB1": alRLB1,
       "alL-Line2": alL_Line2,
       "alLLOSS2": alLLOSS2,
       "alLILOSS2": alLILOSS2,
       "alLAIS2": alLAIS2,
       "alLAISL2": alLAISL2,
       "alLLLB2": alLLLB2,
       "alLRLB2": alLRLB2,
       "alL-Line3": alL_Line3,
       "alLLOSS3": alLLOSS3,
       "alLILOSS3": alLILOSS3,
       "alLAIS3": alLAIS3,
       "alLAISL3": alLAISL3,
       "alLLLB3": alLLLB3,
       "alLRLB3": alLRLB3,
       "alL-Line4": alL_Line4,
       "alLLOSS4": alLLOSS4,
       "alLILOSS4": alLILOSS4,
       "alLAIS4": alLAIS4,
       "alLAISL4": alLAISL4,
       "alLLLB4": alLLLB4,
       "alLRLB4": alLRLB4,
       "alL-Line5": alL_Line5,
       "alLLOSS5": alLLOSS5,
       "alLILOSS5": alLILOSS5,
       "alLAIS5": alLAIS5,
       "alLAISL5": alLAISL5,
       "alLLLB5": alLLLB5,
       "alLRLB5": alLRLB5,
       "alL-Line6": alL_Line6,
       "alLLOSS6": alLLOSS6,
       "alLILOSS6": alLILOSS6,
       "alLAIS6": alLAIS6,
       "alLAISL6": alLAISL6,
       "alLLLB6": alLLLB6,
       "alLRLB6": alLRLB6,
       "alL-Line7": alL_Line7,
       "alLLOSS7": alLLOSS7,
       "alLILOSS7": alLILOSS7,
       "alLAIS7": alLAIS7,
       "alLAISL7": alLAISL7,
       "alLLLB7": alLLLB7,
       "alLRLB7": alLRLB7,
       "alL-Line8": alL_Line8,
       "alLLOSS8": alLLOSS8,
       "alLILOSS8": alLILOSS8,
       "alLAIS8": alLAIS8,
       "alLAISL8": alLAISL8,
       "alLLLB8": alLLLB8,
       "alLRLB8": alLRLB8,
       "alL-Line9": alL_Line9,
       "alLLOSS9": alLLOSS9,
       "alLILOSS9": alLILOSS9,
       "alLAIS9": alLAIS9,
       "alLAISL9": alLAISL9,
       "alLLLB9": alLLLB9,
       "alLRLB9": alLRLB9,
       "alL-Line10": alL_Line10,
       "alLLOSS10": alLLOSS10,
       "alLILOSS10": alLILOSS10,
       "alLAIS10": alLAIS10,
       "alLAISL10": alLAISL10,
       "alLLLB10": alLLLB10,
       "alLRLB10": alLRLB10,
       "alL-Line11": alL_Line11,
       "alLLOSS11": alLLOSS11,
       "alLILOSS11": alLILOSS11,
       "alLAIS11": alLAIS11,
       "alLAISL11": alLAISL11,
       "alLLLB11": alLLLB11,
       "alLRLB11": alLRLB11,
       "alL-Line12": alL_Line12,
       "alLLOSS12": alLLOSS12,
       "alLILOSS12": alLILOSS12,
       "alLAIS12": alLAIS12,
       "alLAISL12": alLAISL12,
       "alLLLB12": alLLLB12,
       "alLRLB12": alLRLB12,
       "remote-station": remote_station,
       "alR-General": alR_General,
       "alRSupervisor": alRSupervisor,
       "alRConfiguration": alRConfiguration,
       "alRStatus": alRStatus,
       "alRHistory": alRHistory,
       "alRIAISL": alRIAISL,
       "alRILEVPWR": alRILEVPWR,
       "alR-ODU": alR_ODU,
       "alRRX-Level": alRRX_Level,
       "alRTX-PWR": alRTX_PWR,
       "alRMode-TX": alRMode_TX,
       "alRODU-LB": alRODU_LB,
       "alR-Modem": alR_Modem,
       "alRQuality": alRQuality,
       "alR-Supply": alR_Supply,
       "alRVoltage-5V": alRVoltage_5V,
       "alRVoltage-5Vor15V": alRVoltage_5Vor15V,
       "alRVoltage-24V": alRVoltage_24V,
       "alRCurrent-ODU": alRCurrent_ODU,
       "alRInput": alRInput,
       "alR-IDU": alR_IDU,
       "alREEPROM": alREEPROM,
       "alRRAM": alRRAM,
       "alRBattery": alRBattery,
       "alRCommIDU": alRCommIDU,
       "alRCommRMT": alRCommRMT,
       "alR-MUX": alR_MUX,
       "alRBER-10E6": alRBER_10E6,
       "alRBER-10E4": alRBER_10E4,
       "alRFrame": alRFrame,
       "alR-PDH1": alR_PDH1,
       "alRPDHFrame": alRPDHFrame,
       "alRAISPDH": alRAISPDH,
       "alRLLBPDH": alRLLBPDH,
       "alRRLBPDH": alRRLBPDH,
       "alR-Line1": alR_Line1,
       "alRLOSS1": alRLOSS1,
       "alRILOSS1": alRILOSS1,
       "alRAIS1": alRAIS1,
       "alRAISL1": alRAISL1,
       "alRLLB1": alRLLB1,
       "alRRLB1": alRRLB1,
       "alR-Line2": alR_Line2,
       "alRLOSS2": alRLOSS2,
       "alRILOSS2": alRILOSS2,
       "alRAIS2": alRAIS2,
       "alRAISL2": alRAISL2,
       "alRLLB2": alRLLB2,
       "alRRLB2": alRRLB2,
       "alR-Line3": alR_Line3,
       "alRLOSS3": alRLOSS3,
       "alRILOSS3": alRILOSS3,
       "alRAIS3": alRAIS3,
       "alRAISL3": alRAISL3,
       "alRLLB3": alRLLB3,
       "alRRLB3": alRRLB3,
       "alR-Line4": alR_Line4,
       "alRLOSS4": alRLOSS4,
       "alRILOSS4": alRILOSS4,
       "alRAIS4": alRAIS4,
       "alRAISL4": alRAISL4,
       "alRLLB4": alRLLB4,
       "alRRLB4": alRRLB4,
       "alR-Line5": alR_Line5,
       "alRLOSS5": alRLOSS5,
       "alRILOSS5": alRILOSS5,
       "alRAIS5": alRAIS5,
       "alRAISL5": alRAISL5,
       "alRLLB5": alRLLB5,
       "alRRLB5": alRRLB5,
       "alR-Line6": alR_Line6,
       "alRLOSS6": alRLOSS6,
       "alRILOSS6": alRILOSS6,
       "alRAIS6": alRAIS6,
       "alRAISL6": alRAISL6,
       "alRLLB6": alRLLB6,
       "alRRLB6": alRRLB6,
       "alR-Line7": alR_Line7,
       "alRLOSS7": alRLOSS7,
       "alRILOSS7": alRILOSS7,
       "alRAIS7": alRAIS7,
       "alRAISL7": alRAISL7,
       "alRLLB7": alRLLB7,
       "alRRLB7": alRRLB7,
       "alR-Line8": alR_Line8,
       "alRLOSS8": alRLOSS8,
       "alRILOSS8": alRILOSS8,
       "alRAIS8": alRAIS8,
       "alRAISL8": alRAISL8,
       "alRLLB8": alRLLB8,
       "alRRLB8": alRRLB8,
       "alR-Line9": alR_Line9,
       "alRLOSS9": alRLOSS9,
       "alRILOSS9": alRILOSS9,
       "alRAIS9": alRAIS9,
       "alRAISL9": alRAISL9,
       "alRLLB9": alRLLB9,
       "alRRLB9": alRRLB9,
       "alR-Line10": alR_Line10,
       "alRLOSS10": alRLOSS10,
       "alRILOSS10": alRILOSS10,
       "alRAIS10": alRAIS10,
       "alRAISL10": alRAISL10,
       "alRLLB10": alRLLB10,
       "alRRLB10": alRRLB10,
       "alR-Line11": alR_Line11,
       "alRLOSS11": alRLOSS11,
       "alRILOSS11": alRILOSS11,
       "alRAIS11": alRAIS11,
       "alRAISL11": alRAISL11,
       "alRLLB11": alRLLB11,
       "alRRLB11": alRRLB11,
       "alR-Line12": alR_Line12,
       "alRLOSS12": alRLOSS12,
       "alRILOSS12": alRILOSS12,
       "alRAIS12": alRAIS12,
       "alRAISL12": alRAISL12,
       "alRLLB12": alRLLB12,
       "alRRLB12": alRRLB12,
       "alRRLTrap": alRRLTrap,
       "alLast-Message": alLast_Message,
       "alNMS": alNMS,
       "trapParam": trapParam,
       "nmsTrapTime": nmsTrapTime,
       "trapSequence": trapSequence,
       "mwRouteID": mwRouteID,
       "stationID": stationID,
       "stationName": stationName,
       "mgmtGWaddr": mgmtGWaddr,
       "lineID": lineID,
       "alMP": alMP,
       "alMPStatusLED": alMPStatusLED,
       "alMPEHW": alMPEHW,
       "alMPESR": alMPESR,
       "alMPESL": alMPESL,
       "alMPCA": alMPCA,
       "alMPGeneral": alMPGeneral,
       "alMPSupervisor": alMPSupervisor,
       "alMPConfiguration": alMPConfiguration,
       "alMPStatus": alMPStatus,
       "alMPHistory": alMPHistory,
       "alMPIAISL": alMPIAISL,
       "alMPILEVPWR": alMPILEVPWR,
       "alMPODU": alMPODU,
       "alMPTuneTX": alMPTuneTX,
       "alMPTuneRX": alMPTuneRX,
       "alMPTX-PWR": alMPTX_PWR,
       "alMPRX-Level": alMPRX_Level,
       "alMPTX-PWRAlrm": alMPTX_PWRAlrm,
       "alMPRX-LevelAlrm": alMPRX_LevelAlrm,
       "alMPMode-TX": alMPMode_TX,
       "alMPODU-LB": alMPODU_LB,
       "alMPTemperature": alMPTemperature,
       "alMPModem": alMPModem,
       "alMPQuality": alMPQuality,
       "alMPSNR": alMPSNR,
       "alMPQualityAlrm": alMPQualityAlrm,
       "alMPSNRAlrm": alMPSNRAlrm,
       "alMPRate": alMPRate,
       "alMPQAM": alMPQAM,
       "alMPActiveACM": alMPActiveACM,
       "alMPStatusACM": alMPStatusACM,
       "alMPSupply": alMPSupply,
       "alMPInput": alMPInput,
       "alMPRDG": alMPRDG,
       "alMPEEPROM": alMPEEPROM,
       "alMPRAM": alMPRAM,
       "alMPCommRMT": alMPCommRMT,
       "alMPMUX": alMPMUX,
       "alMPBER": alMPBER,
       "alMPBER-10E6": alMPBER_10E6,
       "alMPBER-10E4": alMPBER_10E4,
       "alMPFrame": alMPFrame,
       "alMPLine1": alMPLine1,
       "alMPLOSS1": alMPLOSS1,
       "alMPILOSS1": alMPILOSS1,
       "alMPAIS1": alMPAIS1,
       "alMPAISL1": alMPAISL1,
       "alMPLLB1": alMPLLB1,
       "alMPRLB1": alMPRLB1,
       "alMPLine2": alMPLine2,
       "alMPLOSS2": alMPLOSS2,
       "alMPILOSS2": alMPILOSS2,
       "alMPLink2": alMPLink2,
       "alMPSpeed2": alMPSpeed2,
       "alMPType2": alMPType2,
       "alMPFlow2": alMPFlow2,
       "alMPPktRX2": alMPPktRX2,
       "alMPByteRX2": alMPByteRX2,
       "alMPPktTX2": alMPPktTX2,
       "alMPByteTX2": alMPByteTX2,
       "alMPError2": alMPError2,
       "alMPCollision2": alMPCollision2,
       "alMPLine3": alMPLine3,
       "alMPLOSS3": alMPLOSS3,
       "alMPILOSS3": alMPILOSS3,
       "alMPLink3": alMPLink3,
       "alMPSpeed3": alMPSpeed3,
       "alMPType3": alMPType3,
       "alMPFlow3": alMPFlow3,
       "alMPPktRX3": alMPPktRX3,
       "alMPByteRX3": alMPByteRX3,
       "alMPPktTX3": alMPPktTX3,
       "alMPByteTX3": alMPByteTX3,
       "alMPError3": alMPError3,
       "alMPCollision3": alMPCollision3,
       "alMPLine4": alMPLine4,
       "alMPLOSS4": alMPLOSS4,
       "alMPILOSS4": alMPILOSS4,
       "alMPLink4": alMPLink4,
       "alMPSpeed4": alMPSpeed4,
       "alMPType4": alMPType4,
       "alMPFlow4": alMPFlow4,
       "alMPPktRX4": alMPPktRX4,
       "alMPByteRX4": alMPByteRX4,
       "alMPPktTX4": alMPPktTX4,
       "alMPByteTX4": alMPByteTX4,
       "alMPError4": alMPError4,
       "alMPCollision4": alMPCollision4}
)
