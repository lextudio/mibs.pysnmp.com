# SNMP MIB module (Motorola-Cpe-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Motorola-Cpe-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:36 2024
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

(ifAdminStatus,
 ifIndex,
 ifOperStatus) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAdminStatus",
    "ifIndex",
    "ifOperStatus")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

gemtekDevCpe = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Gemtek_ObjectIdentity = ObjectIdentity
gemtek = _Gemtek_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529)
)
_GemtekDevCpeStatus_ObjectIdentity = ObjectIdentity
gemtekDevCpeStatus = _GemtekDevCpeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1)
)
_WirelessStatus_ObjectIdentity = ObjectIdentity
wirelessStatus = _WirelessStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 1)
)


class _GemtekDevCpeWimaxRssi_Type(OctetString):
    """Custom type gemtekDevCpeWimaxRssi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GemtekDevCpeWimaxRssi_Type.__name__ = "OctetString"
_GemtekDevCpeWimaxRssi_Object = MibScalar
gemtekDevCpeWimaxRssi = _GemtekDevCpeWimaxRssi_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 1, 1),
    _GemtekDevCpeWimaxRssi_Type()
)
gemtekDevCpeWimaxRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeWimaxRssi.setStatus("current")


class _GemtekDevCpeWimaxCinr_Type(OctetString):
    """Custom type gemtekDevCpeWimaxCinr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GemtekDevCpeWimaxCinr_Type.__name__ = "OctetString"
_GemtekDevCpeWimaxCinr_Object = MibScalar
gemtekDevCpeWimaxCinr = _GemtekDevCpeWimaxCinr_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 1, 2),
    _GemtekDevCpeWimaxCinr_Type()
)
gemtekDevCpeWimaxCinr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeWimaxCinr.setStatus("current")


class _GemtekDevCpeWimaxTxPower_Type(OctetString):
    """Custom type gemtekDevCpeWimaxTxPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GemtekDevCpeWimaxTxPower_Type.__name__ = "OctetString"
_GemtekDevCpeWimaxTxPower_Object = MibScalar
gemtekDevCpeWimaxTxPower = _GemtekDevCpeWimaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 1, 3),
    _GemtekDevCpeWimaxTxPower_Type()
)
gemtekDevCpeWimaxTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeWimaxTxPower.setStatus("current")


class _GemtekDevCpeWimaxMaxTxPower_Type(OctetString):
    """Custom type gemtekDevCpeWimaxMaxTxPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GemtekDevCpeWimaxMaxTxPower_Type.__name__ = "OctetString"
_GemtekDevCpeWimaxMaxTxPower_Object = MibScalar
gemtekDevCpeWimaxMaxTxPower = _GemtekDevCpeWimaxMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 1, 4),
    _GemtekDevCpeWimaxMaxTxPower_Type()
)
gemtekDevCpeWimaxMaxTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeWimaxMaxTxPower.setStatus("current")


class _GemtekDevCpeWimaxUpLinkModulation_Type(OctetString):
    """Custom type gemtekDevCpeWimaxUpLinkModulation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GemtekDevCpeWimaxUpLinkModulation_Type.__name__ = "OctetString"
_GemtekDevCpeWimaxUpLinkModulation_Object = MibScalar
gemtekDevCpeWimaxUpLinkModulation = _GemtekDevCpeWimaxUpLinkModulation_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 1, 5),
    _GemtekDevCpeWimaxUpLinkModulation_Type()
)
gemtekDevCpeWimaxUpLinkModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeWimaxUpLinkModulation.setStatus("current")


class _GemtekDevCpeWimaxDownLinkModulation_Type(OctetString):
    """Custom type gemtekDevCpeWimaxDownLinkModulation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GemtekDevCpeWimaxDownLinkModulation_Type.__name__ = "OctetString"
_GemtekDevCpeWimaxDownLinkModulation_Object = MibScalar
gemtekDevCpeWimaxDownLinkModulation = _GemtekDevCpeWimaxDownLinkModulation_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 1, 6),
    _GemtekDevCpeWimaxDownLinkModulation_Type()
)
gemtekDevCpeWimaxDownLinkModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeWimaxDownLinkModulation.setStatus("current")


class _GemtekDevCpeWimaxBsid_Type(OctetString):
    """Custom type gemtekDevCpeWimaxBsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_GemtekDevCpeWimaxBsid_Type.__name__ = "OctetString"
_GemtekDevCpeWimaxBsid_Object = MibScalar
gemtekDevCpeWimaxBsid = _GemtekDevCpeWimaxBsid_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 1, 7),
    _GemtekDevCpeWimaxBsid_Type()
)
gemtekDevCpeWimaxBsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeWimaxBsid.setStatus("current")
_GemtekDevCpeWimaxFrequency_Type = Unsigned32
_GemtekDevCpeWimaxFrequency_Object = MibScalar
gemtekDevCpeWimaxFrequency = _GemtekDevCpeWimaxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 1, 8),
    _GemtekDevCpeWimaxFrequency_Type()
)
gemtekDevCpeWimaxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeWimaxFrequency.setStatus("current")


class _GemtekDevCpeWimaxUpLinkDataRate_Type(OctetString):
    """Custom type gemtekDevCpeWimaxUpLinkDataRate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GemtekDevCpeWimaxUpLinkDataRate_Type.__name__ = "OctetString"
_GemtekDevCpeWimaxUpLinkDataRate_Object = MibScalar
gemtekDevCpeWimaxUpLinkDataRate = _GemtekDevCpeWimaxUpLinkDataRate_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 1, 9),
    _GemtekDevCpeWimaxUpLinkDataRate_Type()
)
gemtekDevCpeWimaxUpLinkDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeWimaxUpLinkDataRate.setStatus("current")


class _GemtekDevCpeWimaxDownLinkDataRate_Type(OctetString):
    """Custom type gemtekDevCpeWimaxDownLinkDataRate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GemtekDevCpeWimaxDownLinkDataRate_Type.__name__ = "OctetString"
_GemtekDevCpeWimaxDownLinkDataRate_Object = MibScalar
gemtekDevCpeWimaxDownLinkDataRate = _GemtekDevCpeWimaxDownLinkDataRate_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 1, 10),
    _GemtekDevCpeWimaxDownLinkDataRate_Type()
)
gemtekDevCpeWimaxDownLinkDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeWimaxDownLinkDataRate.setStatus("current")
_GemtekDevCpeWimaxTotalUpLinkDataByte_Type = Unsigned32
_GemtekDevCpeWimaxTotalUpLinkDataByte_Object = MibScalar
gemtekDevCpeWimaxTotalUpLinkDataByte = _GemtekDevCpeWimaxTotalUpLinkDataByte_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 1, 11),
    _GemtekDevCpeWimaxTotalUpLinkDataByte_Type()
)
gemtekDevCpeWimaxTotalUpLinkDataByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeWimaxTotalUpLinkDataByte.setStatus("current")
_GemtekDevCpeWimaxTotalDownLinkDataByte_Type = Unsigned32
_GemtekDevCpeWimaxTotalDownLinkDataByte_Object = MibScalar
gemtekDevCpeWimaxTotalDownLinkDataByte = _GemtekDevCpeWimaxTotalDownLinkDataByte_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 1, 12),
    _GemtekDevCpeWimaxTotalDownLinkDataByte_Type()
)
gemtekDevCpeWimaxTotalDownLinkDataByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeWimaxTotalDownLinkDataByte.setStatus("current")


class _GemtekDevCpeWimaxCpeState_Type(OctetString):
    """Custom type gemtekDevCpeWimaxCpeState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GemtekDevCpeWimaxCpeState_Type.__name__ = "OctetString"
_GemtekDevCpeWimaxCpeState_Object = MibScalar
gemtekDevCpeWimaxCpeState = _GemtekDevCpeWimaxCpeState_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 1, 13),
    _GemtekDevCpeWimaxCpeState_Type()
)
gemtekDevCpeWimaxCpeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeWimaxCpeState.setStatus("current")


class _GemtekDevCpeWimaxCinrReuse1_Type(OctetString):
    """Custom type gemtekDevCpeWimaxCinrReuse1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GemtekDevCpeWimaxCinrReuse1_Type.__name__ = "OctetString"
_GemtekDevCpeWimaxCinrReuse1_Object = MibScalar
gemtekDevCpeWimaxCinrReuse1 = _GemtekDevCpeWimaxCinrReuse1_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 1, 14),
    _GemtekDevCpeWimaxCinrReuse1_Type()
)
gemtekDevCpeWimaxCinrReuse1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeWimaxCinrReuse1.setStatus("current")


class _GemtekDevCpeWimaxCinrReuse3_Type(OctetString):
    """Custom type gemtekDevCpeWimaxCinrReuse3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GemtekDevCpeWimaxCinrReuse3_Type.__name__ = "OctetString"
_GemtekDevCpeWimaxCinrReuse3_Object = MibScalar
gemtekDevCpeWimaxCinrReuse3 = _GemtekDevCpeWimaxCinrReuse3_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 1, 15),
    _GemtekDevCpeWimaxCinrReuse3_Type()
)
gemtekDevCpeWimaxCinrReuse3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeWimaxCinrReuse3.setStatus("current")
_GemtekDevCpeWimaxBandwidth_Type = Integer32
_GemtekDevCpeWimaxBandwidth_Object = MibScalar
gemtekDevCpeWimaxBandwidth = _GemtekDevCpeWimaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 1, 16),
    _GemtekDevCpeWimaxBandwidth_Type()
)
gemtekDevCpeWimaxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeWimaxBandwidth.setStatus("current")


class _GemtekDevCpeWimaxZoneCinrChannelZero_Type(OctetString):
    """Custom type gemtekDevCpeWimaxZoneCinrChannelZero based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GemtekDevCpeWimaxZoneCinrChannelZero_Type.__name__ = "OctetString"
_GemtekDevCpeWimaxZoneCinrChannelZero_Object = MibScalar
gemtekDevCpeWimaxZoneCinrChannelZero = _GemtekDevCpeWimaxZoneCinrChannelZero_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 1, 17),
    _GemtekDevCpeWimaxZoneCinrChannelZero_Type()
)
gemtekDevCpeWimaxZoneCinrChannelZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeWimaxZoneCinrChannelZero.setStatus("current")


class _GemtekDevCpeWimaxMimoMode_Type(Integer32):
    """Custom type gemtekDevCpeWimaxMimoMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disconnect", 4),
          ("mimoMatrixA", 1),
          ("mimoMatrixB", 2),
          ("siso", 0))
    )


_GemtekDevCpeWimaxMimoMode_Type.__name__ = "Integer32"
_GemtekDevCpeWimaxMimoMode_Object = MibScalar
gemtekDevCpeWimaxMimoMode = _GemtekDevCpeWimaxMimoMode_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 1, 18),
    _GemtekDevCpeWimaxMimoMode_Type()
)
gemtekDevCpeWimaxMimoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeWimaxMimoMode.setStatus("current")
_NetworkStatus_ObjectIdentity = ObjectIdentity
networkStatus = _NetworkStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 2)
)


class _GemtekDevCpeLanMacAddresss_Type(OctetString):
    """Custom type gemtekDevCpeLanMacAddresss based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_GemtekDevCpeLanMacAddresss_Type.__name__ = "OctetString"
_GemtekDevCpeLanMacAddresss_Object = MibScalar
gemtekDevCpeLanMacAddresss = _GemtekDevCpeLanMacAddresss_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 2, 1),
    _GemtekDevCpeLanMacAddresss_Type()
)
gemtekDevCpeLanMacAddresss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeLanMacAddresss.setStatus("current")
_GemtekDevCpeLanTotalDownLinkDataByte_Type = Unsigned32
_GemtekDevCpeLanTotalDownLinkDataByte_Object = MibScalar
gemtekDevCpeLanTotalDownLinkDataByte = _GemtekDevCpeLanTotalDownLinkDataByte_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 2, 2),
    _GemtekDevCpeLanTotalDownLinkDataByte_Type()
)
gemtekDevCpeLanTotalDownLinkDataByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeLanTotalDownLinkDataByte.setStatus("current")
_GemtekDevCpeLanTotalUpLinkDataByte_Type = Unsigned32
_GemtekDevCpeLanTotalUpLinkDataByte_Object = MibScalar
gemtekDevCpeLanTotalUpLinkDataByte = _GemtekDevCpeLanTotalUpLinkDataByte_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 2, 3),
    _GemtekDevCpeLanTotalUpLinkDataByte_Type()
)
gemtekDevCpeLanTotalUpLinkDataByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeLanTotalUpLinkDataByte.setStatus("current")
_GemtekDevCpeLanTotalDownLinkDataPackets_Type = Unsigned32
_GemtekDevCpeLanTotalDownLinkDataPackets_Object = MibScalar
gemtekDevCpeLanTotalDownLinkDataPackets = _GemtekDevCpeLanTotalDownLinkDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 2, 4),
    _GemtekDevCpeLanTotalDownLinkDataPackets_Type()
)
gemtekDevCpeLanTotalDownLinkDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeLanTotalDownLinkDataPackets.setStatus("current")
_GemtekDevCpeLanTotalUpLinkDataPackets_Type = Unsigned32
_GemtekDevCpeLanTotalUpLinkDataPackets_Object = MibScalar
gemtekDevCpeLanTotalUpLinkDataPackets = _GemtekDevCpeLanTotalUpLinkDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 2, 5),
    _GemtekDevCpeLanTotalUpLinkDataPackets_Type()
)
gemtekDevCpeLanTotalUpLinkDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeLanTotalUpLinkDataPackets.setStatus("current")


class _GemtekDevCpeWanMacAddresss_Type(OctetString):
    """Custom type gemtekDevCpeWanMacAddresss based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_GemtekDevCpeWanMacAddresss_Type.__name__ = "OctetString"
_GemtekDevCpeWanMacAddresss_Object = MibScalar
gemtekDevCpeWanMacAddresss = _GemtekDevCpeWanMacAddresss_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 2, 6),
    _GemtekDevCpeWanMacAddresss_Type()
)
gemtekDevCpeWanMacAddresss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeWanMacAddresss.setStatus("current")
_GemtekDevCpeWanTotalDownLinkDataPackets_Type = Unsigned32
_GemtekDevCpeWanTotalDownLinkDataPackets_Object = MibScalar
gemtekDevCpeWanTotalDownLinkDataPackets = _GemtekDevCpeWanTotalDownLinkDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 2, 7),
    _GemtekDevCpeWanTotalDownLinkDataPackets_Type()
)
gemtekDevCpeWanTotalDownLinkDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeWanTotalDownLinkDataPackets.setStatus("current")
_GemtekDevCpeWanTotalUpLinkDataPackets_Type = Unsigned32
_GemtekDevCpeWanTotalUpLinkDataPackets_Object = MibScalar
gemtekDevCpeWanTotalUpLinkDataPackets = _GemtekDevCpeWanTotalUpLinkDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 2, 8),
    _GemtekDevCpeWanTotalUpLinkDataPackets_Type()
)
gemtekDevCpeWanTotalUpLinkDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeWanTotalUpLinkDataPackets.setStatus("current")
_DeviceStatus_ObjectIdentity = ObjectIdentity
deviceStatus = _DeviceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 3)
)


class _GemtekDevCpeHardwareModel_Type(OctetString):
    """Custom type gemtekDevCpeHardwareModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GemtekDevCpeHardwareModel_Type.__name__ = "OctetString"
_GemtekDevCpeHardwareModel_Object = MibScalar
gemtekDevCpeHardwareModel = _GemtekDevCpeHardwareModel_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 3, 1),
    _GemtekDevCpeHardwareModel_Type()
)
gemtekDevCpeHardwareModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeHardwareModel.setStatus("current")


class _GemtekDevCpeFirmwareVersion_Type(OctetString):
    """Custom type gemtekDevCpeFirmwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GemtekDevCpeFirmwareVersion_Type.__name__ = "OctetString"
_GemtekDevCpeFirmwareVersion_Object = MibScalar
gemtekDevCpeFirmwareVersion = _GemtekDevCpeFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 3, 2),
    _GemtekDevCpeFirmwareVersion_Type()
)
gemtekDevCpeFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeFirmwareVersion.setStatus("current")


class _GemtekDevCpeFirmwareCreationDate_Type(OctetString):
    """Custom type gemtekDevCpeFirmwareCreationDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GemtekDevCpeFirmwareCreationDate_Type.__name__ = "OctetString"
_GemtekDevCpeFirmwareCreationDate_Object = MibScalar
gemtekDevCpeFirmwareCreationDate = _GemtekDevCpeFirmwareCreationDate_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 3, 3),
    _GemtekDevCpeFirmwareCreationDate_Type()
)
gemtekDevCpeFirmwareCreationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeFirmwareCreationDate.setStatus("current")


class _GemtekDevCpeFrequencyRange_Type(OctetString):
    """Custom type gemtekDevCpeFrequencyRange based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GemtekDevCpeFrequencyRange_Type.__name__ = "OctetString"
_GemtekDevCpeFrequencyRange_Object = MibScalar
gemtekDevCpeFrequencyRange = _GemtekDevCpeFrequencyRange_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 3, 4),
    _GemtekDevCpeFrequencyRange_Type()
)
gemtekDevCpeFrequencyRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeFrequencyRange.setStatus("current")


class _GemtekDevCpeSerialNumber_Type(OctetString):
    """Custom type gemtekDevCpeSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GemtekDevCpeSerialNumber_Type.__name__ = "OctetString"
_GemtekDevCpeSerialNumber_Object = MibScalar
gemtekDevCpeSerialNumber = _GemtekDevCpeSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 3, 5),
    _GemtekDevCpeSerialNumber_Type()
)
gemtekDevCpeSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeSerialNumber.setStatus("current")


class _GemtekDevCpeLatitude_Type(OctetString):
    """Custom type gemtekDevCpeLatitude based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GemtekDevCpeLatitude_Type.__name__ = "OctetString"
_GemtekDevCpeLatitude_Object = MibScalar
gemtekDevCpeLatitude = _GemtekDevCpeLatitude_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 3, 6),
    _GemtekDevCpeLatitude_Type()
)
gemtekDevCpeLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeLatitude.setStatus("current")


class _GemtekDevCpeLongitude_Type(OctetString):
    """Custom type gemtekDevCpeLongitude based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GemtekDevCpeLongitude_Type.__name__ = "OctetString"
_GemtekDevCpeLongitude_Object = MibScalar
gemtekDevCpeLongitude = _GemtekDevCpeLongitude_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 3, 7),
    _GemtekDevCpeLongitude_Type()
)
gemtekDevCpeLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeLongitude.setStatus("current")


class _GemtekDevCpeHeight_Type(OctetString):
    """Custom type gemtekDevCpeHeight based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GemtekDevCpeHeight_Type.__name__ = "OctetString"
_GemtekDevCpeHeight_Object = MibScalar
gemtekDevCpeHeight = _GemtekDevCpeHeight_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 3, 8),
    _GemtekDevCpeHeight_Type()
)
gemtekDevCpeHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeHeight.setStatus("current")


class _GemtekDevCpeMibsVersion_Type(OctetString):
    """Custom type gemtekDevCpeMibsVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GemtekDevCpeMibsVersion_Type.__name__ = "OctetString"
_GemtekDevCpeMibsVersion_Object = MibScalar
gemtekDevCpeMibsVersion = _GemtekDevCpeMibsVersion_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 3, 9),
    _GemtekDevCpeMibsVersion_Type()
)
gemtekDevCpeMibsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeMibsVersion.setStatus("current")


class _GemtekDevCpeBootromVersion_Type(OctetString):
    """Custom type gemtekDevCpeBootromVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GemtekDevCpeBootromVersion_Type.__name__ = "OctetString"
_GemtekDevCpeBootromVersion_Object = MibScalar
gemtekDevCpeBootromVersion = _GemtekDevCpeBootromVersion_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 3, 10),
    _GemtekDevCpeBootromVersion_Type()
)
gemtekDevCpeBootromVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeBootromVersion.setStatus("current")


class _GemtekDevCpeBootromCreationDate_Type(OctetString):
    """Custom type gemtekDevCpeBootromCreationDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GemtekDevCpeBootromCreationDate_Type.__name__ = "OctetString"
_GemtekDevCpeBootromCreationDate_Object = MibScalar
gemtekDevCpeBootromCreationDate = _GemtekDevCpeBootromCreationDate_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 3, 11),
    _GemtekDevCpeBootromCreationDate_Type()
)
gemtekDevCpeBootromCreationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeBootromCreationDate.setStatus("current")


class _GemtekDevCpeProductVersion_Type(OctetString):
    """Custom type gemtekDevCpeProductVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GemtekDevCpeProductVersion_Type.__name__ = "OctetString"
_GemtekDevCpeProductVersion_Object = MibScalar
gemtekDevCpeProductVersion = _GemtekDevCpeProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 1, 3, 12),
    _GemtekDevCpeProductVersion_Type()
)
gemtekDevCpeProductVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeProductVersion.setStatus("current")
_GemtekDevCpeControl_ObjectIdentity = ObjectIdentity
gemtekDevCpeControl = _GemtekDevCpeControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 2)
)


class _RebootWithResponse_Type(Integer32):
    """Custom type rebootWithResponse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("reboot", 255),
          ("rebootNotRequired", 0),
          ("rebootRequired", 1))
    )


_RebootWithResponse_Type.__name__ = "Integer32"
_RebootWithResponse_Object = MibScalar
rebootWithResponse = _RebootWithResponse_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 2, 1),
    _RebootWithResponse_Type()
)
rebootWithResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rebootWithResponse.setStatus("current")


class _IsRebootRequired_Type(Integer32):
    """Custom type isRebootRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rebootNotRequired", 0),
          ("rebootRequired", 1))
    )


_IsRebootRequired_Type.__name__ = "Integer32"
_IsRebootRequired_Object = MibScalar
isRebootRequired = _IsRebootRequired_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 2, 2),
    _IsRebootRequired_Type()
)
isRebootRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isRebootRequired.setStatus("current")


class _AutoSaveConfig_Type(Integer32):
    """Custom type autoSaveConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("autoSaveDisabled", 0),
          ("autoSaveEnabled", 1))
    )


_AutoSaveConfig_Type.__name__ = "Integer32"
_AutoSaveConfig_Object = MibScalar
autoSaveConfig = _AutoSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 2, 3),
    _AutoSaveConfig_Type()
)
autoSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoSaveConfig.setStatus("current")
_AutoSavePeriod_Type = Unsigned32
_AutoSavePeriod_Object = MibScalar
autoSavePeriod = _AutoSavePeriod_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 2, 4),
    _AutoSavePeriod_Type()
)
autoSavePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoSavePeriod.setStatus("obsolete")


class _StartStopWimax_Type(Integer32):
    """Custom type startStopWimax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 0))
    )


_StartStopWimax_Type.__name__ = "Integer32"
_StartStopWimax_Object = MibScalar
startStopWimax = _StartStopWimax_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 2, 5),
    _StartStopWimax_Type()
)
startStopWimax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startStopWimax.setStatus("current")


class _SnmpBuzzerConfig_Type(Integer32):
    """Custom type snmpBuzzerConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("snmpBuzzerDemo", 2),
          ("snmpBuzzerDisabled", 0),
          ("snmpBuzzerEnabled", 1))
    )


_SnmpBuzzerConfig_Type.__name__ = "Integer32"
_SnmpBuzzerConfig_Object = MibScalar
snmpBuzzerConfig = _SnmpBuzzerConfig_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 2, 6),
    _SnmpBuzzerConfig_Type()
)
snmpBuzzerConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpBuzzerConfig.setStatus("current")
_SnmpBuzzerDisableDelay_Type = Unsigned32
_SnmpBuzzerDisableDelay_Object = MibScalar
snmpBuzzerDisableDelay = _SnmpBuzzerDisableDelay_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 2, 7),
    _SnmpBuzzerDisableDelay_Type()
)
snmpBuzzerDisableDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpBuzzerDisableDelay.setStatus("current")


class _GemtekDevCpeSnmpReadCommunity_Type(OctetString):
    """Custom type gemtekDevCpeSnmpReadCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GemtekDevCpeSnmpReadCommunity_Type.__name__ = "OctetString"
_GemtekDevCpeSnmpReadCommunity_Object = MibScalar
gemtekDevCpeSnmpReadCommunity = _GemtekDevCpeSnmpReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 2, 8),
    _GemtekDevCpeSnmpReadCommunity_Type()
)
gemtekDevCpeSnmpReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeSnmpReadCommunity.setStatus("current")


class _GemtekDevCpeSnmpSetCommunity_Type(OctetString):
    """Custom type gemtekDevCpeSnmpSetCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GemtekDevCpeSnmpSetCommunity_Type.__name__ = "OctetString"
_GemtekDevCpeSnmpSetCommunity_Object = MibScalar
gemtekDevCpeSnmpSetCommunity = _GemtekDevCpeSnmpSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 2, 9),
    _GemtekDevCpeSnmpSetCommunity_Type()
)
gemtekDevCpeSnmpSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeSnmpSetCommunity.setStatus("current")


class _GemtekDevCpeRestFactoryDefault_Type(Integer32):
    """Custom type gemtekDevCpeRestFactoryDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeRestFactoryDefault_Type.__name__ = "Integer32"
_GemtekDevCpeRestFactoryDefault_Object = MibScalar
gemtekDevCpeRestFactoryDefault = _GemtekDevCpeRestFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 2, 10),
    _GemtekDevCpeRestFactoryDefault_Type()
)
gemtekDevCpeRestFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeRestFactoryDefault.setStatus("current")


class _GemtekDevCpeAutoFirmwareRollback_Type(Integer32):
    """Custom type gemtekDevCpeAutoFirmwareRollback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("levelOne", 1),
          ("levelTwo", 2))
    )


_GemtekDevCpeAutoFirmwareRollback_Type.__name__ = "Integer32"
_GemtekDevCpeAutoFirmwareRollback_Object = MibScalar
gemtekDevCpeAutoFirmwareRollback = _GemtekDevCpeAutoFirmwareRollback_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 2, 11),
    _GemtekDevCpeAutoFirmwareRollback_Type()
)
gemtekDevCpeAutoFirmwareRollback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeAutoFirmwareRollback.setStatus("current")
_GemtekDevCpeFirmwareValidationTime_Type = Unsigned32
_GemtekDevCpeFirmwareValidationTime_Object = MibScalar
gemtekDevCpeFirmwareValidationTime = _GemtekDevCpeFirmwareValidationTime_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 2, 12),
    _GemtekDevCpeFirmwareValidationTime_Type()
)
gemtekDevCpeFirmwareValidationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeFirmwareValidationTime.setStatus("current")
_GemtekDevCpeFirmwareValidationCount_Type = Unsigned32
_GemtekDevCpeFirmwareValidationCount_Object = MibScalar
gemtekDevCpeFirmwareValidationCount = _GemtekDevCpeFirmwareValidationCount_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 2, 13),
    _GemtekDevCpeFirmwareValidationCount_Type()
)
gemtekDevCpeFirmwareValidationCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeFirmwareValidationCount.setStatus("current")


class _GemtekDevCpeSnmpAccessFromLan_Type(Integer32):
    """Custom type gemtekDevCpeSnmpAccessFromLan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeSnmpAccessFromLan_Type.__name__ = "Integer32"
_GemtekDevCpeSnmpAccessFromLan_Object = MibScalar
gemtekDevCpeSnmpAccessFromLan = _GemtekDevCpeSnmpAccessFromLan_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 2, 14),
    _GemtekDevCpeSnmpAccessFromLan_Type()
)
gemtekDevCpeSnmpAccessFromLan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeSnmpAccessFromLan.setStatus("current")


class _GemtekDevCpeDynamicMaxTxPowerBpsk_Type(OctetString):
    """Custom type gemtekDevCpeDynamicMaxTxPowerBpsk based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GemtekDevCpeDynamicMaxTxPowerBpsk_Type.__name__ = "OctetString"
_GemtekDevCpeDynamicMaxTxPowerBpsk_Object = MibScalar
gemtekDevCpeDynamicMaxTxPowerBpsk = _GemtekDevCpeDynamicMaxTxPowerBpsk_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 2, 15),
    _GemtekDevCpeDynamicMaxTxPowerBpsk_Type()
)
gemtekDevCpeDynamicMaxTxPowerBpsk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeDynamicMaxTxPowerBpsk.setStatus("current")


class _GemtekDevCpeDynamicMaxTxPowerQpsk_Type(OctetString):
    """Custom type gemtekDevCpeDynamicMaxTxPowerQpsk based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GemtekDevCpeDynamicMaxTxPowerQpsk_Type.__name__ = "OctetString"
_GemtekDevCpeDynamicMaxTxPowerQpsk_Object = MibScalar
gemtekDevCpeDynamicMaxTxPowerQpsk = _GemtekDevCpeDynamicMaxTxPowerQpsk_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 2, 16),
    _GemtekDevCpeDynamicMaxTxPowerQpsk_Type()
)
gemtekDevCpeDynamicMaxTxPowerQpsk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeDynamicMaxTxPowerQpsk.setStatus("current")


class _GemtekDevCpeDynamicMaxTxPowerQam16_Type(OctetString):
    """Custom type gemtekDevCpeDynamicMaxTxPowerQam16 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GemtekDevCpeDynamicMaxTxPowerQam16_Type.__name__ = "OctetString"
_GemtekDevCpeDynamicMaxTxPowerQam16_Object = MibScalar
gemtekDevCpeDynamicMaxTxPowerQam16 = _GemtekDevCpeDynamicMaxTxPowerQam16_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 2, 17),
    _GemtekDevCpeDynamicMaxTxPowerQam16_Type()
)
gemtekDevCpeDynamicMaxTxPowerQam16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeDynamicMaxTxPowerQam16.setStatus("current")


class _GemtekDevCpeDynamicMaxTxPowerQam64_Type(OctetString):
    """Custom type gemtekDevCpeDynamicMaxTxPowerQam64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GemtekDevCpeDynamicMaxTxPowerQam64_Type.__name__ = "OctetString"
_GemtekDevCpeDynamicMaxTxPowerQam64_Object = MibScalar
gemtekDevCpeDynamicMaxTxPowerQam64 = _GemtekDevCpeDynamicMaxTxPowerQam64_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 2, 18),
    _GemtekDevCpeDynamicMaxTxPowerQam64_Type()
)
gemtekDevCpeDynamicMaxTxPowerQam64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeDynamicMaxTxPowerQam64.setStatus("current")
_GemtekDevCpeSnmpAccessDomain_ObjectIdentity = ObjectIdentity
gemtekDevCpeSnmpAccessDomain = _GemtekDevCpeSnmpAccessDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 2, 19)
)


class _GemtekDevCpeSnmpAccessDomainEnable_Type(Integer32):
    """Custom type gemtekDevCpeSnmpAccessDomainEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeSnmpAccessDomainEnable_Type.__name__ = "Integer32"
_GemtekDevCpeSnmpAccessDomainEnable_Object = MibScalar
gemtekDevCpeSnmpAccessDomainEnable = _GemtekDevCpeSnmpAccessDomainEnable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 2, 19, 1),
    _GemtekDevCpeSnmpAccessDomainEnable_Type()
)
gemtekDevCpeSnmpAccessDomainEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeSnmpAccessDomainEnable.setStatus("current")
_GemtekDevCpeSnmpAccessDomainIp_Type = IpAddress
_GemtekDevCpeSnmpAccessDomainIp_Object = MibScalar
gemtekDevCpeSnmpAccessDomainIp = _GemtekDevCpeSnmpAccessDomainIp_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 2, 19, 2),
    _GemtekDevCpeSnmpAccessDomainIp_Type()
)
gemtekDevCpeSnmpAccessDomainIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeSnmpAccessDomainIp.setStatus("current")
_GemtekDevCpeSnmpAccessDomainNetmask_Type = IpAddress
_GemtekDevCpeSnmpAccessDomainNetmask_Object = MibScalar
gemtekDevCpeSnmpAccessDomainNetmask = _GemtekDevCpeSnmpAccessDomainNetmask_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 2, 19, 3),
    _GemtekDevCpeSnmpAccessDomainNetmask_Type()
)
gemtekDevCpeSnmpAccessDomainNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeSnmpAccessDomainNetmask.setStatus("current")
_GemtekDevCpeTrap_ObjectIdentity = ObjectIdentity
gemtekDevCpeTrap = _GemtekDevCpeTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 3)
)
_GemtekDevCpeTrapServer_ObjectIdentity = ObjectIdentity
gemtekDevCpeTrapServer = _GemtekDevCpeTrapServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 3, 1)
)


class _TrapServerEnable_Type(Integer32):
    """Custom type trapServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TrapServerEnable_Type.__name__ = "Integer32"
_TrapServerEnable_Object = MibScalar
trapServerEnable = _TrapServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 3, 1, 1),
    _TrapServerEnable_Type()
)
trapServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapServerEnable.setStatus("current")
_TrapServerIp_Type = IpAddress
_TrapServerIp_Object = MibScalar
trapServerIp = _TrapServerIp_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 3, 1, 2),
    _TrapServerIp_Type()
)
trapServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapServerIp.setStatus("current")
_TrapServerPort_Type = Integer32
_TrapServerPort_Object = MibScalar
trapServerPort = _TrapServerPort_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 3, 1, 3),
    _TrapServerPort_Type()
)
trapServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapServerPort.setStatus("current")


class _TrapServerCommunity_Type(OctetString):
    """Custom type trapServerCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TrapServerCommunity_Type.__name__ = "OctetString"
_TrapServerCommunity_Object = MibScalar
trapServerCommunity = _TrapServerCommunity_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 3, 1, 4),
    _TrapServerCommunity_Type()
)
trapServerCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapServerCommunity.setStatus("current")
_GemtekDevCpeTrapPrefix_ObjectIdentity = ObjectIdentity
gemtekDevCpeTrapPrefix = _GemtekDevCpeTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 3, 2)
)
_GemtekDevCpeDate_ObjectIdentity = ObjectIdentity
gemtekDevCpeDate = _GemtekDevCpeDate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 4)
)
_GemtekDevCpeSystemDate_Type = OctetString
_GemtekDevCpeSystemDate_Object = MibScalar
gemtekDevCpeSystemDate = _GemtekDevCpeSystemDate_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 4, 1),
    _GemtekDevCpeSystemDate_Type()
)
gemtekDevCpeSystemDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeSystemDate.setStatus("current")


class _GemtekDevCpeNtpServerEnable_Type(Integer32):
    """Custom type gemtekDevCpeNtpServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeNtpServerEnable_Type.__name__ = "Integer32"
_GemtekDevCpeNtpServerEnable_Object = MibScalar
gemtekDevCpeNtpServerEnable = _GemtekDevCpeNtpServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 4, 2),
    _GemtekDevCpeNtpServerEnable_Type()
)
gemtekDevCpeNtpServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeNtpServerEnable.setStatus("current")


class _GemtekDevCpeNtpServer_Type(OctetString):
    """Custom type gemtekDevCpeNtpServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_GemtekDevCpeNtpServer_Type.__name__ = "OctetString"
_GemtekDevCpeNtpServer_Object = MibScalar
gemtekDevCpeNtpServer = _GemtekDevCpeNtpServer_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 4, 3),
    _GemtekDevCpeNtpServer_Type()
)
gemtekDevCpeNtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeNtpServer.setStatus("current")


class _GemtekDevCpeNtpServerFromDHCP_Type(Integer32):
    """Custom type gemtekDevCpeNtpServerFromDHCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeNtpServerFromDHCP_Type.__name__ = "Integer32"
_GemtekDevCpeNtpServerFromDHCP_Object = MibScalar
gemtekDevCpeNtpServerFromDHCP = _GemtekDevCpeNtpServerFromDHCP_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 4, 4),
    _GemtekDevCpeNtpServerFromDHCP_Type()
)
gemtekDevCpeNtpServerFromDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeNtpServerFromDHCP.setStatus("current")


class _GemtekDevCpeTimeZone_Type(Integer32):
    """Custom type gemtekDevCpeTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86),
    )


_GemtekDevCpeTimeZone_Type.__name__ = "Integer32"
_GemtekDevCpeTimeZone_Object = MibScalar
gemtekDevCpeTimeZone = _GemtekDevCpeTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 4, 5),
    _GemtekDevCpeTimeZone_Type()
)
gemtekDevCpeTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeTimeZone.setStatus("current")


class _GemtekDevCpeDaylightSaving_Type(Integer32):
    """Custom type gemtekDevCpeDaylightSaving based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeDaylightSaving_Type.__name__ = "Integer32"
_GemtekDevCpeDaylightSaving_Object = MibScalar
gemtekDevCpeDaylightSaving = _GemtekDevCpeDaylightSaving_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 4, 6),
    _GemtekDevCpeDaylightSaving_Type()
)
gemtekDevCpeDaylightSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeDaylightSaving.setStatus("current")
_GemtekDevCpeAccountManagement_ObjectIdentity = ObjectIdentity
gemtekDevCpeAccountManagement = _GemtekDevCpeAccountManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 5)
)


class _AdministratorUsername_Type(OctetString):
    """Custom type administratorUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdministratorUsername_Type.__name__ = "OctetString"
_AdministratorUsername_Object = MibScalar
administratorUsername = _AdministratorUsername_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 5, 1),
    _AdministratorUsername_Type()
)
administratorUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    administratorUsername.setStatus("current")


class _AdministratorPassword_Type(OctetString):
    """Custom type administratorPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdministratorPassword_Type.__name__ = "OctetString"
_AdministratorPassword_Object = MibScalar
administratorPassword = _AdministratorPassword_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 5, 2),
    _AdministratorPassword_Type()
)
administratorPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    administratorPassword.setStatus("current")


class _AdministratorEnable_Type(Integer32):
    """Custom type administratorEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AdministratorEnable_Type.__name__ = "Integer32"
_AdministratorEnable_Object = MibScalar
administratorEnable = _AdministratorEnable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 5, 3),
    _AdministratorEnable_Type()
)
administratorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    administratorEnable.setStatus("current")


class _OperatorUsername_Type(OctetString):
    """Custom type operatorUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OperatorUsername_Type.__name__ = "OctetString"
_OperatorUsername_Object = MibScalar
operatorUsername = _OperatorUsername_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 5, 4),
    _OperatorUsername_Type()
)
operatorUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    operatorUsername.setStatus("current")


class _OperatorPassword_Type(OctetString):
    """Custom type operatorPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OperatorPassword_Type.__name__ = "OctetString"
_OperatorPassword_Object = MibScalar
operatorPassword = _OperatorPassword_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 5, 5),
    _OperatorPassword_Type()
)
operatorPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    operatorPassword.setStatus("current")


class _OperatorEnable_Type(Integer32):
    """Custom type operatorEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_OperatorEnable_Type.__name__ = "Integer32"
_OperatorEnable_Object = MibScalar
operatorEnable = _OperatorEnable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 5, 6),
    _OperatorEnable_Type()
)
operatorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    operatorEnable.setStatus("current")


class _AdminUsername_Type(OctetString):
    """Custom type adminUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdminUsername_Type.__name__ = "OctetString"
_AdminUsername_Object = MibScalar
adminUsername = _AdminUsername_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 5, 7),
    _AdminUsername_Type()
)
adminUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminUsername.setStatus("current")


class _AdminPassword_Type(OctetString):
    """Custom type adminPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdminPassword_Type.__name__ = "OctetString"
_AdminPassword_Object = MibScalar
adminPassword = _AdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 5, 8),
    _AdminPassword_Type()
)
adminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminPassword.setStatus("current")


class _AdminEnable_Type(Integer32):
    """Custom type adminEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AdminEnable_Type.__name__ = "Integer32"
_AdminEnable_Object = MibScalar
adminEnable = _AdminEnable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 5, 9),
    _AdminEnable_Type()
)
adminEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminEnable.setStatus("current")
_GemtekDevCpeScanner_ObjectIdentity = ObjectIdentity
gemtekDevCpeScanner = _GemtekDevCpeScanner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 6)
)


class _GemtekDevCpeChannelBandwidthRang_Type(Integer32):
    """Custom type gemtekDevCpeChannelBandwidthRang based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sixToTen", 1),
          ("threeToFive", 0))
    )


_GemtekDevCpeChannelBandwidthRang_Type.__name__ = "Integer32"
_GemtekDevCpeChannelBandwidthRang_Object = MibScalar
gemtekDevCpeChannelBandwidthRang = _GemtekDevCpeChannelBandwidthRang_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 6, 1),
    _GemtekDevCpeChannelBandwidthRang_Type()
)
gemtekDevCpeChannelBandwidthRang.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeChannelBandwidthRang.setStatus("deprecated")


class _GemtekDevCpeChannelApplyLoadOrSave_Type(Integer32):
    """Custom type gemtekDevCpeChannelApplyLoadOrSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("load", 0),
          ("save", 1))
    )


_GemtekDevCpeChannelApplyLoadOrSave_Type.__name__ = "Integer32"
_GemtekDevCpeChannelApplyLoadOrSave_Object = MibScalar
gemtekDevCpeChannelApplyLoadOrSave = _GemtekDevCpeChannelApplyLoadOrSave_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 6, 2),
    _GemtekDevCpeChannelApplyLoadOrSave_Type()
)
gemtekDevCpeChannelApplyLoadOrSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeChannelApplyLoadOrSave.setStatus("current")
_GemtekDevCpeChannelTable_Object = MibTable
gemtekDevCpeChannelTable = _GemtekDevCpeChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 6, 3)
)
if mibBuilder.loadTexts:
    gemtekDevCpeChannelTable.setStatus("current")
_GemtekDevCpeChannelEntry_Object = MibTableRow
gemtekDevCpeChannelEntry = _GemtekDevCpeChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 6, 3, 1)
)
gemtekDevCpeChannelEntry.setIndexNames(
    (0, "Motorola-Cpe-PRIVATE-MIB", "gemtekDevCpeChannelIndex"),
)
if mibBuilder.loadTexts:
    gemtekDevCpeChannelEntry.setStatus("current")
_GemtekDevCpeChannelIndex_Type = Integer32
_GemtekDevCpeChannelIndex_Object = MibTableColumn
gemtekDevCpeChannelIndex = _GemtekDevCpeChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 6, 3, 1, 1),
    _GemtekDevCpeChannelIndex_Type()
)
gemtekDevCpeChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeChannelIndex.setStatus("current")


class _GemtekDevCpeChannelActive_Type(Integer32):
    """Custom type gemtekDevCpeChannelActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("disactive", 0))
    )


_GemtekDevCpeChannelActive_Type.__name__ = "Integer32"
_GemtekDevCpeChannelActive_Object = MibTableColumn
gemtekDevCpeChannelActive = _GemtekDevCpeChannelActive_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 6, 3, 1, 2),
    _GemtekDevCpeChannelActive_Type()
)
gemtekDevCpeChannelActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeChannelActive.setStatus("current")
_GemtekDevCpeChannelFrequency_Type = Unsigned32
_GemtekDevCpeChannelFrequency_Object = MibTableColumn
gemtekDevCpeChannelFrequency = _GemtekDevCpeChannelFrequency_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 6, 3, 1, 3),
    _GemtekDevCpeChannelFrequency_Type()
)
gemtekDevCpeChannelFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpeChannelFrequency.setStatus("current")
_GemtekDevCpeChannelBandwidth_Type = Integer32
_GemtekDevCpeChannelBandwidth_Object = MibTableColumn
gemtekDevCpeChannelBandwidth = _GemtekDevCpeChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 6, 3, 1, 4),
    _GemtekDevCpeChannelBandwidth_Type()
)
gemtekDevCpeChannelBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpeChannelBandwidth.setStatus("current")


class _GemtekDevCpeChannelRssi_Type(OctetString):
    """Custom type gemtekDevCpeChannelRssi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GemtekDevCpeChannelRssi_Type.__name__ = "OctetString"
_GemtekDevCpeChannelRssi_Object = MibTableColumn
gemtekDevCpeChannelRssi = _GemtekDevCpeChannelRssi_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 6, 3, 1, 5),
    _GemtekDevCpeChannelRssi_Type()
)
gemtekDevCpeChannelRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeChannelRssi.setStatus("current")


class _GemtekDevCpeChannelCinr_Type(OctetString):
    """Custom type gemtekDevCpeChannelCinr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GemtekDevCpeChannelCinr_Type.__name__ = "OctetString"
_GemtekDevCpeChannelCinr_Object = MibTableColumn
gemtekDevCpeChannelCinr = _GemtekDevCpeChannelCinr_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 6, 3, 1, 6),
    _GemtekDevCpeChannelCinr_Type()
)
gemtekDevCpeChannelCinr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeChannelCinr.setStatus("current")


class _GemtekDevCpeChannelEntryEnable_Type(Integer32):
    """Custom type gemtekDevCpeChannelEntryEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeChannelEntryEnable_Type.__name__ = "Integer32"
_GemtekDevCpeChannelEntryEnable_Object = MibTableColumn
gemtekDevCpeChannelEntryEnable = _GemtekDevCpeChannelEntryEnable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 6, 3, 1, 7),
    _GemtekDevCpeChannelEntryEnable_Type()
)
gemtekDevCpeChannelEntryEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpeChannelEntryEnable.setStatus("current")
_GemtekDevCpeChannelRowstatus_Type = RowStatus
_GemtekDevCpeChannelRowstatus_Object = MibTableColumn
gemtekDevCpeChannelRowstatus = _GemtekDevCpeChannelRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 6, 3, 1, 8),
    _GemtekDevCpeChannelRowstatus_Type()
)
gemtekDevCpeChannelRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpeChannelRowstatus.setStatus("current")


class _GemtekDevCpeChannelBsId_Type(OctetString):
    """Custom type gemtekDevCpeChannelBsId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_GemtekDevCpeChannelBsId_Type.__name__ = "OctetString"
_GemtekDevCpeChannelBsId_Object = MibTableColumn
gemtekDevCpeChannelBsId = _GemtekDevCpeChannelBsId_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 6, 3, 1, 9),
    _GemtekDevCpeChannelBsId_Type()
)
gemtekDevCpeChannelBsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeChannelBsId.setStatus("current")


class _GemtekDevCpeChannelPreambelIndex_Type(OctetString):
    """Custom type gemtekDevCpeChannelPreambelIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_GemtekDevCpeChannelPreambelIndex_Type.__name__ = "OctetString"
_GemtekDevCpeChannelPreambelIndex_Object = MibTableColumn
gemtekDevCpeChannelPreambelIndex = _GemtekDevCpeChannelPreambelIndex_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 6, 3, 1, 10),
    _GemtekDevCpeChannelPreambelIndex_Type()
)
gemtekDevCpeChannelPreambelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeChannelPreambelIndex.setStatus("current")
_GemtekDevCpeFrequencyRangeSetting_ObjectIdentity = ObjectIdentity
gemtekDevCpeFrequencyRangeSetting = _GemtekDevCpeFrequencyRangeSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 6, 4)
)
_GemtekDevCpeLockFrequencyRangeMin_Type = Unsigned32
_GemtekDevCpeLockFrequencyRangeMin_Object = MibScalar
gemtekDevCpeLockFrequencyRangeMin = _GemtekDevCpeLockFrequencyRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 6, 4, 1),
    _GemtekDevCpeLockFrequencyRangeMin_Type()
)
gemtekDevCpeLockFrequencyRangeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeLockFrequencyRangeMin.setStatus("current")
_GemtekDevCpeLockFrequencyRangeMax_Type = Unsigned32
_GemtekDevCpeLockFrequencyRangeMax_Object = MibScalar
gemtekDevCpeLockFrequencyRangeMax = _GemtekDevCpeLockFrequencyRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 6, 4, 2),
    _GemtekDevCpeLockFrequencyRangeMax_Type()
)
gemtekDevCpeLockFrequencyRangeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeLockFrequencyRangeMax.setStatus("current")


class _GemtekDevCpeLockFrequencyRange_Type(Integer32):
    """Custom type gemtekDevCpeLockFrequencyRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lock", 1),
          ("unlock", 0))
    )


_GemtekDevCpeLockFrequencyRange_Type.__name__ = "Integer32"
_GemtekDevCpeLockFrequencyRange_Object = MibScalar
gemtekDevCpeLockFrequencyRange = _GemtekDevCpeLockFrequencyRange_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 6, 4, 3),
    _GemtekDevCpeLockFrequencyRange_Type()
)
gemtekDevCpeLockFrequencyRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeLockFrequencyRange.setStatus("current")
_GemtekDevCpeModelFrequencyRangeMin_Type = Unsigned32
_GemtekDevCpeModelFrequencyRangeMin_Object = MibScalar
gemtekDevCpeModelFrequencyRangeMin = _GemtekDevCpeModelFrequencyRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 6, 4, 4),
    _GemtekDevCpeModelFrequencyRangeMin_Type()
)
gemtekDevCpeModelFrequencyRangeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeModelFrequencyRangeMin.setStatus("current")
_GemtekDevCpeModelFrequencyRangeMax_Type = Unsigned32
_GemtekDevCpeModelFrequencyRangeMax_Object = MibScalar
gemtekDevCpeModelFrequencyRangeMax = _GemtekDevCpeModelFrequencyRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 6, 4, 5),
    _GemtekDevCpeModelFrequencyRangeMax_Type()
)
gemtekDevCpeModelFrequencyRangeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeModelFrequencyRangeMax.setStatus("current")
_GemtekDevCpeAPPreferredList_ObjectIdentity = ObjectIdentity
gemtekDevCpeAPPreferredList = _GemtekDevCpeAPPreferredList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 6, 5)
)


class _GemtekDevCpeAPPreferredSelectionEnable_Type(Integer32):
    """Custom type gemtekDevCpeAPPreferredSelectionEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeAPPreferredSelectionEnable_Type.__name__ = "Integer32"
_GemtekDevCpeAPPreferredSelectionEnable_Object = MibScalar
gemtekDevCpeAPPreferredSelectionEnable = _GemtekDevCpeAPPreferredSelectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 6, 5, 1),
    _GemtekDevCpeAPPreferredSelectionEnable_Type()
)
gemtekDevCpeAPPreferredSelectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeAPPreferredSelectionEnable.setStatus("current")


class _GemtekDevCpeAPPreferredBsIdListLocked_Type(Integer32):
    """Custom type gemtekDevCpeAPPreferredBsIdListLocked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeAPPreferredBsIdListLocked_Type.__name__ = "Integer32"
_GemtekDevCpeAPPreferredBsIdListLocked_Object = MibScalar
gemtekDevCpeAPPreferredBsIdListLocked = _GemtekDevCpeAPPreferredBsIdListLocked_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 6, 5, 2),
    _GemtekDevCpeAPPreferredBsIdListLocked_Type()
)
gemtekDevCpeAPPreferredBsIdListLocked.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeAPPreferredBsIdListLocked.setStatus("current")


class _GemtekDevCpeAPPreferredPriorityOneBsId_Type(OctetString):
    """Custom type gemtekDevCpeAPPreferredPriorityOneBsId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_GemtekDevCpeAPPreferredPriorityOneBsId_Type.__name__ = "OctetString"
_GemtekDevCpeAPPreferredPriorityOneBsId_Object = MibScalar
gemtekDevCpeAPPreferredPriorityOneBsId = _GemtekDevCpeAPPreferredPriorityOneBsId_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 6, 5, 3),
    _GemtekDevCpeAPPreferredPriorityOneBsId_Type()
)
gemtekDevCpeAPPreferredPriorityOneBsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeAPPreferredPriorityOneBsId.setStatus("current")


class _GemtekDevCpeAPPreferredPriorityTwoBsId_Type(OctetString):
    """Custom type gemtekDevCpeAPPreferredPriorityTwoBsId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_GemtekDevCpeAPPreferredPriorityTwoBsId_Type.__name__ = "OctetString"
_GemtekDevCpeAPPreferredPriorityTwoBsId_Object = MibScalar
gemtekDevCpeAPPreferredPriorityTwoBsId = _GemtekDevCpeAPPreferredPriorityTwoBsId_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 6, 5, 4),
    _GemtekDevCpeAPPreferredPriorityTwoBsId_Type()
)
gemtekDevCpeAPPreferredPriorityTwoBsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeAPPreferredPriorityTwoBsId.setStatus("current")


class _GemtekDevCpeAPPreferredPriorityThreeBsId_Type(OctetString):
    """Custom type gemtekDevCpeAPPreferredPriorityThreeBsId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_GemtekDevCpeAPPreferredPriorityThreeBsId_Type.__name__ = "OctetString"
_GemtekDevCpeAPPreferredPriorityThreeBsId_Object = MibScalar
gemtekDevCpeAPPreferredPriorityThreeBsId = _GemtekDevCpeAPPreferredPriorityThreeBsId_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 6, 5, 5),
    _GemtekDevCpeAPPreferredPriorityThreeBsId_Type()
)
gemtekDevCpeAPPreferredPriorityThreeBsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeAPPreferredPriorityThreeBsId.setStatus("current")


class _GemtekDevCpeAPPreferredPriorityFourBsId_Type(OctetString):
    """Custom type gemtekDevCpeAPPreferredPriorityFourBsId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_GemtekDevCpeAPPreferredPriorityFourBsId_Type.__name__ = "OctetString"
_GemtekDevCpeAPPreferredPriorityFourBsId_Object = MibScalar
gemtekDevCpeAPPreferredPriorityFourBsId = _GemtekDevCpeAPPreferredPriorityFourBsId_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 6, 5, 6),
    _GemtekDevCpeAPPreferredPriorityFourBsId_Type()
)
gemtekDevCpeAPPreferredPriorityFourBsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeAPPreferredPriorityFourBsId.setStatus("current")
_GemtekDevCpeAuthentication_ObjectIdentity = ObjectIdentity
gemtekDevCpeAuthentication = _GemtekDevCpeAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7)
)


class _GemtekDevCpeAuthenticationSelectionPhase1_Type(Integer32):
    """Custom type gemtekDevCpeAuthenticationSelectionPhase1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eapTls", 2),
          ("eapTtls", 1),
          ("none", 0))
    )


_GemtekDevCpeAuthenticationSelectionPhase1_Type.__name__ = "Integer32"
_GemtekDevCpeAuthenticationSelectionPhase1_Object = MibScalar
gemtekDevCpeAuthenticationSelectionPhase1 = _GemtekDevCpeAuthenticationSelectionPhase1_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 1),
    _GemtekDevCpeAuthenticationSelectionPhase1_Type()
)
gemtekDevCpeAuthenticationSelectionPhase1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeAuthenticationSelectionPhase1.setStatus("current")


class _EapIdentityType_Type(Integer32):
    """Custom type eapIdentityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manaulIdentity", 1),
          ("noIdentity", 0),
          ("randomIdentity", 2))
    )


_EapIdentityType_Type.__name__ = "Integer32"
_EapIdentityType_Object = MibScalar
eapIdentityType = _EapIdentityType_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 2),
    _EapIdentityType_Type()
)
eapIdentityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eapIdentityType.setStatus("current")


class _EapIdentityUseRealm_Type(Integer32):
    """Custom type eapIdentityUseRealm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EapIdentityUseRealm_Type.__name__ = "Integer32"
_EapIdentityUseRealm_Object = MibScalar
eapIdentityUseRealm = _EapIdentityUseRealm_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 3),
    _EapIdentityUseRealm_Type()
)
eapIdentityUseRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eapIdentityUseRealm.setStatus("current")


class _EapIdentityString_Type(OctetString):
    """Custom type eapIdentityString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EapIdentityString_Type.__name__ = "OctetString"
_EapIdentityString_Object = MibScalar
eapIdentityString = _EapIdentityString_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 4),
    _EapIdentityString_Type()
)
eapIdentityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eapIdentityString.setStatus("current")


class _EapRealmString_Type(OctetString):
    """Custom type eapRealmString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EapRealmString_Type.__name__ = "OctetString"
_EapRealmString_Object = MibScalar
eapRealmString = _EapRealmString_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 5),
    _EapRealmString_Type()
)
eapRealmString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eapRealmString.setStatus("current")


class _EapValidateTheDateDurationOfCaCertificate_Type(Integer32):
    """Custom type eapValidateTheDateDurationOfCaCertificate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EapValidateTheDateDurationOfCaCertificate_Type.__name__ = "Integer32"
_EapValidateTheDateDurationOfCaCertificate_Object = MibScalar
eapValidateTheDateDurationOfCaCertificate = _EapValidateTheDateDurationOfCaCertificate_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 6),
    _EapValidateTheDateDurationOfCaCertificate_Type()
)
eapValidateTheDateDurationOfCaCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eapValidateTheDateDurationOfCaCertificate.setStatus("current")


class _EapValidateTheServerCertificate_Type(Integer32):
    """Custom type eapValidateTheServerCertificate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EapValidateTheServerCertificate_Type.__name__ = "Integer32"
_EapValidateTheServerCertificate_Object = MibScalar
eapValidateTheServerCertificate = _EapValidateTheServerCertificate_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 7),
    _EapValidateTheServerCertificate_Type()
)
eapValidateTheServerCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eapValidateTheServerCertificate.setStatus("current")
_GemtekDevCpeAuthenticationEAPTLS_ObjectIdentity = ObjectIdentity
gemtekDevCpeAuthenticationEAPTLS = _GemtekDevCpeAuthenticationEAPTLS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 8)
)


class _EapTlsPrivateKeyPassword_Type(OctetString):
    """Custom type eapTlsPrivateKeyPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EapTlsPrivateKeyPassword_Type.__name__ = "OctetString"
_EapTlsPrivateKeyPassword_Object = MibScalar
eapTlsPrivateKeyPassword = _EapTlsPrivateKeyPassword_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 8, 1),
    _EapTlsPrivateKeyPassword_Type()
)
eapTlsPrivateKeyPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eapTlsPrivateKeyPassword.setStatus("current")
_GemtekDevCpeAuthenticationEAPTTLS_ObjectIdentity = ObjectIdentity
gemtekDevCpeAuthenticationEAPTTLS = _GemtekDevCpeAuthenticationEAPTTLS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 9)
)


class _EapTtlsPhase2_Type(Integer32):
    """Custom type eapTtlsPhase2 based on Integer32"""
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
        *(("chap", 2),
          ("md5", 5),
          ("mschap", 3),
          ("mschapV2", 4),
          ("pap", 1))
    )


_EapTtlsPhase2_Type.__name__ = "Integer32"
_EapTtlsPhase2_Object = MibScalar
eapTtlsPhase2 = _EapTtlsPhase2_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 9, 1),
    _EapTtlsPhase2_Type()
)
eapTtlsPhase2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eapTtlsPhase2.setStatus("current")


class _EapTtlsUsername_Type(OctetString):
    """Custom type eapTtlsUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EapTtlsUsername_Type.__name__ = "OctetString"
_EapTtlsUsername_Object = MibScalar
eapTtlsUsername = _EapTtlsUsername_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 9, 2),
    _EapTtlsUsername_Type()
)
eapTtlsUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eapTtlsUsername.setStatus("current")


class _EapTtlsPassword_Type(OctetString):
    """Custom type eapTtlsPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EapTtlsPassword_Type.__name__ = "OctetString"
_EapTtlsPassword_Object = MibScalar
eapTtlsPassword = _EapTtlsPassword_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 9, 3),
    _EapTtlsPassword_Type()
)
eapTtlsPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eapTtlsPassword.setStatus("current")


class _EapTtlsUseDeviceCertificate_Type(Integer32):
    """Custom type eapTtlsUseDeviceCertificate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EapTtlsUseDeviceCertificate_Type.__name__ = "Integer32"
_EapTtlsUseDeviceCertificate_Object = MibScalar
eapTtlsUseDeviceCertificate = _EapTtlsUseDeviceCertificate_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 9, 4),
    _EapTtlsUseDeviceCertificate_Type()
)
eapTtlsUseDeviceCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eapTtlsUseDeviceCertificate.setStatus("current")


class _EapTtlsPrivateKeyPassword_Type(OctetString):
    """Custom type eapTtlsPrivateKeyPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EapTtlsPrivateKeyPassword_Type.__name__ = "OctetString"
_EapTtlsPrivateKeyPassword_Object = MibScalar
eapTtlsPrivateKeyPassword = _EapTtlsPrivateKeyPassword_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 9, 5),
    _EapTtlsPrivateKeyPassword_Type()
)
eapTtlsPrivateKeyPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eapTtlsPrivateKeyPassword.setStatus("current")
_GemtekDevCpeCertificationFileManagement_ObjectIdentity = ObjectIdentity
gemtekDevCpeCertificationFileManagement = _GemtekDevCpeCertificationFileManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 10)
)
_GemtekDevCpeCertificateUpload_ObjectIdentity = ObjectIdentity
gemtekDevCpeCertificateUpload = _GemtekDevCpeCertificateUpload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 10, 1)
)


class _GemtekDevCpeCACertificateFileName_Type(OctetString):
    """Custom type gemtekDevCpeCACertificateFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_GemtekDevCpeCACertificateFileName_Type.__name__ = "OctetString"
_GemtekDevCpeCACertificateFileName_Object = MibScalar
gemtekDevCpeCACertificateFileName = _GemtekDevCpeCACertificateFileName_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 10, 1, 1),
    _GemtekDevCpeCACertificateFileName_Type()
)
gemtekDevCpeCACertificateFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeCACertificateFileName.setStatus("current")


class _GemtekDevCpeCACertificateFileUpload_Type(Integer32):
    """Custom type gemtekDevCpeCACertificateFileUpload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("upload", 1))
    )


_GemtekDevCpeCACertificateFileUpload_Type.__name__ = "Integer32"
_GemtekDevCpeCACertificateFileUpload_Object = MibScalar
gemtekDevCpeCACertificateFileUpload = _GemtekDevCpeCACertificateFileUpload_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 10, 1, 2),
    _GemtekDevCpeCACertificateFileUpload_Type()
)
gemtekDevCpeCACertificateFileUpload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeCACertificateFileUpload.setStatus("current")


class _GemtekDevCpeUserCertificateFileName_Type(OctetString):
    """Custom type gemtekDevCpeUserCertificateFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_GemtekDevCpeUserCertificateFileName_Type.__name__ = "OctetString"
_GemtekDevCpeUserCertificateFileName_Object = MibScalar
gemtekDevCpeUserCertificateFileName = _GemtekDevCpeUserCertificateFileName_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 10, 1, 3),
    _GemtekDevCpeUserCertificateFileName_Type()
)
gemtekDevCpeUserCertificateFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeUserCertificateFileName.setStatus("current")


class _GemtekDevCpeUserCertificateFileUpload_Type(Integer32):
    """Custom type gemtekDevCpeUserCertificateFileUpload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("upload", 1))
    )


_GemtekDevCpeUserCertificateFileUpload_Type.__name__ = "Integer32"
_GemtekDevCpeUserCertificateFileUpload_Object = MibScalar
gemtekDevCpeUserCertificateFileUpload = _GemtekDevCpeUserCertificateFileUpload_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 10, 1, 4),
    _GemtekDevCpeUserCertificateFileUpload_Type()
)
gemtekDevCpeUserCertificateFileUpload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeUserCertificateFileUpload.setStatus("current")


class _GemtekDevCpeCACertificateFileDelete_Type(Integer32):
    """Custom type gemtekDevCpeCACertificateFileDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fileOne", 1),
          ("fileTwo", 2))
    )


_GemtekDevCpeCACertificateFileDelete_Type.__name__ = "Integer32"
_GemtekDevCpeCACertificateFileDelete_Object = MibScalar
gemtekDevCpeCACertificateFileDelete = _GemtekDevCpeCACertificateFileDelete_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 10, 2),
    _GemtekDevCpeCACertificateFileDelete_Type()
)
gemtekDevCpeCACertificateFileDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeCACertificateFileDelete.setStatus("current")


class _GemtekDevCpeUserCertificateFileDelete_Type(Integer32):
    """Custom type gemtekDevCpeUserCertificateFileDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fileOne", 1),
          ("fileTwo", 2))
    )


_GemtekDevCpeUserCertificateFileDelete_Type.__name__ = "Integer32"
_GemtekDevCpeUserCertificateFileDelete_Object = MibScalar
gemtekDevCpeUserCertificateFileDelete = _GemtekDevCpeUserCertificateFileDelete_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 10, 3),
    _GemtekDevCpeUserCertificateFileDelete_Type()
)
gemtekDevCpeUserCertificateFileDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeUserCertificateFileDelete.setStatus("current")
_GemtekDevCpeCACertificateFileTable_Object = MibTable
gemtekDevCpeCACertificateFileTable = _GemtekDevCpeCACertificateFileTable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 10, 4)
)
if mibBuilder.loadTexts:
    gemtekDevCpeCACertificateFileTable.setStatus("current")
_GemtekDevCpeCACertificateFileEntry_Object = MibTableRow
gemtekDevCpeCACertificateFileEntry = _GemtekDevCpeCACertificateFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 10, 4, 1)
)
gemtekDevCpeCACertificateFileEntry.setIndexNames(
    (0, "Motorola-Cpe-PRIVATE-MIB", "gemtekDevCpeCACertificateIndex"),
)
if mibBuilder.loadTexts:
    gemtekDevCpeCACertificateFileEntry.setStatus("current")
_GemtekDevCpeCACertificateIndex_Type = Integer32
_GemtekDevCpeCACertificateIndex_Object = MibTableColumn
gemtekDevCpeCACertificateIndex = _GemtekDevCpeCACertificateIndex_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 10, 4, 1, 1),
    _GemtekDevCpeCACertificateIndex_Type()
)
gemtekDevCpeCACertificateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeCACertificateIndex.setStatus("current")
_GemtekDevCpeCACertificateSize_Type = Unsigned32
_GemtekDevCpeCACertificateSize_Object = MibTableColumn
gemtekDevCpeCACertificateSize = _GemtekDevCpeCACertificateSize_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 10, 4, 1, 2),
    _GemtekDevCpeCACertificateSize_Type()
)
gemtekDevCpeCACertificateSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeCACertificateSize.setStatus("current")


class _GemtekDevCpeCACertificateIssuer_Type(OctetString):
    """Custom type gemtekDevCpeCACertificateIssuer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_GemtekDevCpeCACertificateIssuer_Type.__name__ = "OctetString"
_GemtekDevCpeCACertificateIssuer_Object = MibTableColumn
gemtekDevCpeCACertificateIssuer = _GemtekDevCpeCACertificateIssuer_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 10, 4, 1, 3),
    _GemtekDevCpeCACertificateIssuer_Type()
)
gemtekDevCpeCACertificateIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeCACertificateIssuer.setStatus("current")


class _GemtekDevCpeCAValidityDateBegin_Type(OctetString):
    """Custom type gemtekDevCpeCAValidityDateBegin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GemtekDevCpeCAValidityDateBegin_Type.__name__ = "OctetString"
_GemtekDevCpeCAValidityDateBegin_Object = MibTableColumn
gemtekDevCpeCAValidityDateBegin = _GemtekDevCpeCAValidityDateBegin_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 10, 4, 1, 4),
    _GemtekDevCpeCAValidityDateBegin_Type()
)
gemtekDevCpeCAValidityDateBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeCAValidityDateBegin.setStatus("current")


class _GemtekDevCpeCAValidityDateEnd_Type(OctetString):
    """Custom type gemtekDevCpeCAValidityDateEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GemtekDevCpeCAValidityDateEnd_Type.__name__ = "OctetString"
_GemtekDevCpeCAValidityDateEnd_Object = MibTableColumn
gemtekDevCpeCAValidityDateEnd = _GemtekDevCpeCAValidityDateEnd_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 10, 4, 1, 5),
    _GemtekDevCpeCAValidityDateEnd_Type()
)
gemtekDevCpeCAValidityDateEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeCAValidityDateEnd.setStatus("current")


class _GemtekDevCpeCACertificateSubject_Type(OctetString):
    """Custom type gemtekDevCpeCACertificateSubject based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_GemtekDevCpeCACertificateSubject_Type.__name__ = "OctetString"
_GemtekDevCpeCACertificateSubject_Object = MibTableColumn
gemtekDevCpeCACertificateSubject = _GemtekDevCpeCACertificateSubject_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 10, 4, 1, 6),
    _GemtekDevCpeCACertificateSubject_Type()
)
gemtekDevCpeCACertificateSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeCACertificateSubject.setStatus("current")
_GemtekDevCpeUserCertificateFileTable_Object = MibTable
gemtekDevCpeUserCertificateFileTable = _GemtekDevCpeUserCertificateFileTable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 10, 5)
)
if mibBuilder.loadTexts:
    gemtekDevCpeUserCertificateFileTable.setStatus("current")
_GemtekDevCpeUserCertificateFileEntry_Object = MibTableRow
gemtekDevCpeUserCertificateFileEntry = _GemtekDevCpeUserCertificateFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 10, 5, 1)
)
gemtekDevCpeUserCertificateFileEntry.setIndexNames(
    (0, "Motorola-Cpe-PRIVATE-MIB", "gemtekDevCpeUserCertificateIndex"),
)
if mibBuilder.loadTexts:
    gemtekDevCpeUserCertificateFileEntry.setStatus("current")
_GemtekDevCpeUserCertificateIndex_Type = Integer32
_GemtekDevCpeUserCertificateIndex_Object = MibTableColumn
gemtekDevCpeUserCertificateIndex = _GemtekDevCpeUserCertificateIndex_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 10, 5, 1, 1),
    _GemtekDevCpeUserCertificateIndex_Type()
)
gemtekDevCpeUserCertificateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeUserCertificateIndex.setStatus("current")
_GemtekDevCpeUserCertificateSize_Type = Unsigned32
_GemtekDevCpeUserCertificateSize_Object = MibTableColumn
gemtekDevCpeUserCertificateSize = _GemtekDevCpeUserCertificateSize_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 10, 5, 1, 2),
    _GemtekDevCpeUserCertificateSize_Type()
)
gemtekDevCpeUserCertificateSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeUserCertificateSize.setStatus("current")


class _GemtekDevCpeUserCertificateIssuer_Type(OctetString):
    """Custom type gemtekDevCpeUserCertificateIssuer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_GemtekDevCpeUserCertificateIssuer_Type.__name__ = "OctetString"
_GemtekDevCpeUserCertificateIssuer_Object = MibTableColumn
gemtekDevCpeUserCertificateIssuer = _GemtekDevCpeUserCertificateIssuer_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 10, 5, 1, 3),
    _GemtekDevCpeUserCertificateIssuer_Type()
)
gemtekDevCpeUserCertificateIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeUserCertificateIssuer.setStatus("current")


class _GemtekDevCpeUserValidityDateBegin_Type(OctetString):
    """Custom type gemtekDevCpeUserValidityDateBegin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GemtekDevCpeUserValidityDateBegin_Type.__name__ = "OctetString"
_GemtekDevCpeUserValidityDateBegin_Object = MibTableColumn
gemtekDevCpeUserValidityDateBegin = _GemtekDevCpeUserValidityDateBegin_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 10, 5, 1, 4),
    _GemtekDevCpeUserValidityDateBegin_Type()
)
gemtekDevCpeUserValidityDateBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeUserValidityDateBegin.setStatus("current")


class _GemtekDevCpeUserValidityDateEnd_Type(OctetString):
    """Custom type gemtekDevCpeUserValidityDateEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GemtekDevCpeUserValidityDateEnd_Type.__name__ = "OctetString"
_GemtekDevCpeUserValidityDateEnd_Object = MibTableColumn
gemtekDevCpeUserValidityDateEnd = _GemtekDevCpeUserValidityDateEnd_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 10, 5, 1, 5),
    _GemtekDevCpeUserValidityDateEnd_Type()
)
gemtekDevCpeUserValidityDateEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeUserValidityDateEnd.setStatus("current")


class _GemtekDevCpeUserCertificateSubject_Type(OctetString):
    """Custom type gemtekDevCpeUserCertificateSubject based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_GemtekDevCpeUserCertificateSubject_Type.__name__ = "OctetString"
_GemtekDevCpeUserCertificateSubject_Object = MibTableColumn
gemtekDevCpeUserCertificateSubject = _GemtekDevCpeUserCertificateSubject_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 7, 10, 5, 1, 6),
    _GemtekDevCpeUserCertificateSubject_Type()
)
gemtekDevCpeUserCertificateSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeUserCertificateSubject.setStatus("current")
_GemtekDevCpeNetworkMode_ObjectIdentity = ObjectIdentity
gemtekDevCpeNetworkMode = _GemtekDevCpeNetworkMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8)
)


class _GemtekDevCpeNetoworkOperatingMode_Type(Integer32):
    """Custom type gemtekDevCpeNetoworkOperatingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 1),
          ("nat", 0))
    )


_GemtekDevCpeNetoworkOperatingMode_Type.__name__ = "Integer32"
_GemtekDevCpeNetoworkOperatingMode_Object = MibScalar
gemtekDevCpeNetoworkOperatingMode = _GemtekDevCpeNetoworkOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 1),
    _GemtekDevCpeNetoworkOperatingMode_Type()
)
gemtekDevCpeNetoworkOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeNetoworkOperatingMode.setStatus("current")
_GemtekDevCpeBridgeMode_ObjectIdentity = ObjectIdentity
gemtekDevCpeBridgeMode = _GemtekDevCpeBridgeMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2)
)


class _GemtekDevCpeBridgeIpType_Type(Integer32):
    """Custom type gemtekDevCpeBridgeIpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("static", 0))
    )


_GemtekDevCpeBridgeIpType_Type.__name__ = "Integer32"
_GemtekDevCpeBridgeIpType_Object = MibScalar
gemtekDevCpeBridgeIpType = _GemtekDevCpeBridgeIpType_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 1),
    _GemtekDevCpeBridgeIpType_Type()
)
gemtekDevCpeBridgeIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeBridgeIpType.setStatus("current")
_GemtekDevCpeBridgeIpAddress_Type = IpAddress
_GemtekDevCpeBridgeIpAddress_Object = MibScalar
gemtekDevCpeBridgeIpAddress = _GemtekDevCpeBridgeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 2),
    _GemtekDevCpeBridgeIpAddress_Type()
)
gemtekDevCpeBridgeIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeBridgeIpAddress.setStatus("current")
_GemtekDevCpeBridgeNetmask_Type = IpAddress
_GemtekDevCpeBridgeNetmask_Object = MibScalar
gemtekDevCpeBridgeNetmask = _GemtekDevCpeBridgeNetmask_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 3),
    _GemtekDevCpeBridgeNetmask_Type()
)
gemtekDevCpeBridgeNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeBridgeNetmask.setStatus("current")
_GemtekDevCpeBridgeGateway_Type = IpAddress
_GemtekDevCpeBridgeGateway_Object = MibScalar
gemtekDevCpeBridgeGateway = _GemtekDevCpeBridgeGateway_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 4),
    _GemtekDevCpeBridgeGateway_Type()
)
gemtekDevCpeBridgeGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeBridgeGateway.setStatus("current")
_GemtekDevCpeBridgeDhcpLeaseTime_Type = Unsigned32
_GemtekDevCpeBridgeDhcpLeaseTime_Object = MibScalar
gemtekDevCpeBridgeDhcpLeaseTime = _GemtekDevCpeBridgeDhcpLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 5),
    _GemtekDevCpeBridgeDhcpLeaseTime_Type()
)
gemtekDevCpeBridgeDhcpLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeBridgeDhcpLeaseTime.setStatus("current")
_GemtekDevCpeBridgeDhcpRenewalTime_Type = Unsigned32
_GemtekDevCpeBridgeDhcpRenewalTime_Object = MibScalar
gemtekDevCpeBridgeDhcpRenewalTime = _GemtekDevCpeBridgeDhcpRenewalTime_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 6),
    _GemtekDevCpeBridgeDhcpRenewalTime_Type()
)
gemtekDevCpeBridgeDhcpRenewalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeBridgeDhcpRenewalTime.setStatus("current")
_GemtekDevCpeBridgeDhcpRebindTime_Type = Unsigned32
_GemtekDevCpeBridgeDhcpRebindTime_Object = MibScalar
gemtekDevCpeBridgeDhcpRebindTime = _GemtekDevCpeBridgeDhcpRebindTime_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 7),
    _GemtekDevCpeBridgeDhcpRebindTime_Type()
)
gemtekDevCpeBridgeDhcpRebindTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeBridgeDhcpRebindTime.setStatus("current")
_GemtekDevCpeMVLAN_ObjectIdentity = ObjectIdentity
gemtekDevCpeMVLAN = _GemtekDevCpeMVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 8)
)
_GemtekDevCpeMgmtVlan_ObjectIdentity = ObjectIdentity
gemtekDevCpeMgmtVlan = _GemtekDevCpeMgmtVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 8, 1)
)


class _GemtekDevCpeMgmtVlanEnalbe_Type(Integer32):
    """Custom type gemtekDevCpeMgmtVlanEnalbe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeMgmtVlanEnalbe_Type.__name__ = "Integer32"
_GemtekDevCpeMgmtVlanEnalbe_Object = MibScalar
gemtekDevCpeMgmtVlanEnalbe = _GemtekDevCpeMgmtVlanEnalbe_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 8, 1, 1),
    _GemtekDevCpeMgmtVlanEnalbe_Type()
)
gemtekDevCpeMgmtVlanEnalbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeMgmtVlanEnalbe.setStatus("current")
_GemtekDevCpeMgmtVlanVid_Type = Unsigned32
_GemtekDevCpeMgmtVlanVid_Object = MibScalar
gemtekDevCpeMgmtVlanVid = _GemtekDevCpeMgmtVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 8, 1, 2),
    _GemtekDevCpeMgmtVlanVid_Type()
)
gemtekDevCpeMgmtVlanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeMgmtVlanVid.setStatus("current")
_GemtekDevCpeMgmtVlanVp_Type = Unsigned32
_GemtekDevCpeMgmtVlanVp_Object = MibScalar
gemtekDevCpeMgmtVlanVp = _GemtekDevCpeMgmtVlanVp_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 8, 1, 3),
    _GemtekDevCpeMgmtVlanVp_Type()
)
gemtekDevCpeMgmtVlanVp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeMgmtVlanVp.setStatus("current")
_GemtekDevCpeDataVlan_ObjectIdentity = ObjectIdentity
gemtekDevCpeDataVlan = _GemtekDevCpeDataVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 8, 2)
)


class _GemtekDevCpeDataVlanEnalbe_Type(Integer32):
    """Custom type gemtekDevCpeDataVlanEnalbe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeDataVlanEnalbe_Type.__name__ = "Integer32"
_GemtekDevCpeDataVlanEnalbe_Object = MibScalar
gemtekDevCpeDataVlanEnalbe = _GemtekDevCpeDataVlanEnalbe_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 8, 2, 1),
    _GemtekDevCpeDataVlanEnalbe_Type()
)
gemtekDevCpeDataVlanEnalbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeDataVlanEnalbe.setStatus("current")
_GemtekDevCpeDataVlanVid_Type = Unsigned32
_GemtekDevCpeDataVlanVid_Object = MibScalar
gemtekDevCpeDataVlanVid = _GemtekDevCpeDataVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 8, 2, 2),
    _GemtekDevCpeDataVlanVid_Type()
)
gemtekDevCpeDataVlanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeDataVlanVid.setStatus("current")


class _GemtekDevCpeAllowPacketType_Type(Integer32):
    """Custom type gemtekDevCpeAllowPacketType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("taggedOnly", 1),
          ("untaggedOnly", 2))
    )


_GemtekDevCpeAllowPacketType_Type.__name__ = "Integer32"
_GemtekDevCpeAllowPacketType_Object = MibScalar
gemtekDevCpeAllowPacketType = _GemtekDevCpeAllowPacketType_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 8, 2, 3),
    _GemtekDevCpeAllowPacketType_Type()
)
gemtekDevCpeAllowPacketType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeAllowPacketType.setStatus("current")
_GemtekDevCpeVlanMembershipTable_Object = MibTable
gemtekDevCpeVlanMembershipTable = _GemtekDevCpeVlanMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 8, 3)
)
if mibBuilder.loadTexts:
    gemtekDevCpeVlanMembershipTable.setStatus("current")
_GemtekDevCpeVlanMembershipEntry_Object = MibTableRow
gemtekDevCpeVlanMembershipEntry = _GemtekDevCpeVlanMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 8, 3, 1)
)
gemtekDevCpeVlanMembershipEntry.setIndexNames(
    (0, "Motorola-Cpe-PRIVATE-MIB", "gemtekDevCpeVlanMembershipIndex"),
)
if mibBuilder.loadTexts:
    gemtekDevCpeVlanMembershipEntry.setStatus("current")
_GemtekDevCpeVlanMembershipIndex_Type = Integer32
_GemtekDevCpeVlanMembershipIndex_Object = MibTableColumn
gemtekDevCpeVlanMembershipIndex = _GemtekDevCpeVlanMembershipIndex_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 8, 3, 1, 1),
    _GemtekDevCpeVlanMembershipIndex_Type()
)
gemtekDevCpeVlanMembershipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeVlanMembershipIndex.setStatus("current")
_GemtekDevCpeVlanMembershipVidBegin_Type = Unsigned32
_GemtekDevCpeVlanMembershipVidBegin_Object = MibTableColumn
gemtekDevCpeVlanMembershipVidBegin = _GemtekDevCpeVlanMembershipVidBegin_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 8, 3, 1, 2),
    _GemtekDevCpeVlanMembershipVidBegin_Type()
)
gemtekDevCpeVlanMembershipVidBegin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpeVlanMembershipVidBegin.setStatus("current")
_GemtekDevCpeVlanMembershipVidEnd_Type = Unsigned32
_GemtekDevCpeVlanMembershipVidEnd_Object = MibTableColumn
gemtekDevCpeVlanMembershipVidEnd = _GemtekDevCpeVlanMembershipVidEnd_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 8, 3, 1, 3),
    _GemtekDevCpeVlanMembershipVidEnd_Type()
)
gemtekDevCpeVlanMembershipVidEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpeVlanMembershipVidEnd.setStatus("current")
_GemtekDevCpeVlanMembershipVidRowstatus_Type = RowStatus
_GemtekDevCpeVlanMembershipVidRowstatus_Object = MibTableColumn
gemtekDevCpeVlanMembershipVidRowstatus = _GemtekDevCpeVlanMembershipVidRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 8, 3, 1, 4),
    _GemtekDevCpeVlanMembershipVidRowstatus_Type()
)
gemtekDevCpeVlanMembershipVidRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpeVlanMembershipVidRowstatus.setStatus("current")
_GemtekDevCpeDscpToVp_ObjectIdentity = ObjectIdentity
gemtekDevCpeDscpToVp = _GemtekDevCpeDscpToVp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 8, 4)
)


class _GemtekDevCpeDscpToVpMapping_Type(OctetString):
    """Custom type gemtekDevCpeDscpToVpMapping based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_GemtekDevCpeDscpToVpMapping_Type.__name__ = "OctetString"
_GemtekDevCpeDscpToVpMapping_Object = MibScalar
gemtekDevCpeDscpToVpMapping = _GemtekDevCpeDscpToVpMapping_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 8, 4, 1),
    _GemtekDevCpeDscpToVpMapping_Type()
)
gemtekDevCpeDscpToVpMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeDscpToVpMapping.setStatus("current")
_GemtekDevCpePktCounter_ObjectIdentity = ObjectIdentity
gemtekDevCpePktCounter = _GemtekDevCpePktCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 8, 5)
)
_GemtekDevCpeTaggedPkts_Type = Unsigned32
_GemtekDevCpeTaggedPkts_Object = MibScalar
gemtekDevCpeTaggedPkts = _GemtekDevCpeTaggedPkts_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 8, 5, 1),
    _GemtekDevCpeTaggedPkts_Type()
)
gemtekDevCpeTaggedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeTaggedPkts.setStatus("current")


class _GemtekDevCpeTaggedPktsReset_Type(Integer32):
    """Custom type gemtekDevCpeTaggedPktsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_GemtekDevCpeTaggedPktsReset_Type.__name__ = "Integer32"
_GemtekDevCpeTaggedPktsReset_Object = MibScalar
gemtekDevCpeTaggedPktsReset = _GemtekDevCpeTaggedPktsReset_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 8, 5, 2),
    _GemtekDevCpeTaggedPktsReset_Type()
)
gemtekDevCpeTaggedPktsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeTaggedPktsReset.setStatus("current")
_GemtekDevCpeUntaggedPkts_Type = Unsigned32
_GemtekDevCpeUntaggedPkts_Object = MibScalar
gemtekDevCpeUntaggedPkts = _GemtekDevCpeUntaggedPkts_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 8, 5, 3),
    _GemtekDevCpeUntaggedPkts_Type()
)
gemtekDevCpeUntaggedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeUntaggedPkts.setStatus("current")


class _GemtekDevCpeUntaggedPktsReset_Type(Integer32):
    """Custom type gemtekDevCpeUntaggedPktsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_GemtekDevCpeUntaggedPktsReset_Type.__name__ = "Integer32"
_GemtekDevCpeUntaggedPktsReset_Object = MibScalar
gemtekDevCpeUntaggedPktsReset = _GemtekDevCpeUntaggedPktsReset_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 8, 5, 4),
    _GemtekDevCpeUntaggedPktsReset_Type()
)
gemtekDevCpeUntaggedPktsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeUntaggedPktsReset.setStatus("current")
_GemtekDevCpeNonmemberPkts_Type = Unsigned32
_GemtekDevCpeNonmemberPkts_Object = MibScalar
gemtekDevCpeNonmemberPkts = _GemtekDevCpeNonmemberPkts_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 8, 5, 5),
    _GemtekDevCpeNonmemberPkts_Type()
)
gemtekDevCpeNonmemberPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeNonmemberPkts.setStatus("current")


class _GemtekDevCpeNonmemberPktsReset_Type(Integer32):
    """Custom type gemtekDevCpeNonmemberPktsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_GemtekDevCpeNonmemberPktsReset_Type.__name__ = "Integer32"
_GemtekDevCpeNonmemberPktsReset_Object = MibScalar
gemtekDevCpeNonmemberPktsReset = _GemtekDevCpeNonmemberPktsReset_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 2, 8, 5, 6),
    _GemtekDevCpeNonmemberPktsReset_Type()
)
gemtekDevCpeNonmemberPktsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeNonmemberPktsReset.setStatus("current")
_GemtekDevCpeNatMode_ObjectIdentity = ObjectIdentity
gemtekDevCpeNatMode = _GemtekDevCpeNatMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3)
)


class _GemtekDevCpeNatWanIpType_Type(Integer32):
    """Custom type gemtekDevCpeNatWanIpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("static", 0))
    )


_GemtekDevCpeNatWanIpType_Type.__name__ = "Integer32"
_GemtekDevCpeNatWanIpType_Object = MibScalar
gemtekDevCpeNatWanIpType = _GemtekDevCpeNatWanIpType_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 1),
    _GemtekDevCpeNatWanIpType_Type()
)
gemtekDevCpeNatWanIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeNatWanIpType.setStatus("current")
_GemtekDevCpeNatWanIpAddress_Type = IpAddress
_GemtekDevCpeNatWanIpAddress_Object = MibScalar
gemtekDevCpeNatWanIpAddress = _GemtekDevCpeNatWanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 2),
    _GemtekDevCpeNatWanIpAddress_Type()
)
gemtekDevCpeNatWanIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeNatWanIpAddress.setStatus("current")
_GemtekDevCpeNatWanNetmask_Type = IpAddress
_GemtekDevCpeNatWanNetmask_Object = MibScalar
gemtekDevCpeNatWanNetmask = _GemtekDevCpeNatWanNetmask_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 3),
    _GemtekDevCpeNatWanNetmask_Type()
)
gemtekDevCpeNatWanNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeNatWanNetmask.setStatus("current")
_GemtekDevCpeNatWanGateway_Type = IpAddress
_GemtekDevCpeNatWanGateway_Object = MibScalar
gemtekDevCpeNatWanGateway = _GemtekDevCpeNatWanGateway_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 4),
    _GemtekDevCpeNatWanGateway_Type()
)
gemtekDevCpeNatWanGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeNatWanGateway.setStatus("current")


class _GemtekDevCpeNatLanIpType_Type(Integer32):
    """Custom type gemtekDevCpeNatLanIpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("static", 0))
    )


_GemtekDevCpeNatLanIpType_Type.__name__ = "Integer32"
_GemtekDevCpeNatLanIpType_Object = MibScalar
gemtekDevCpeNatLanIpType = _GemtekDevCpeNatLanIpType_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 5),
    _GemtekDevCpeNatLanIpType_Type()
)
gemtekDevCpeNatLanIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeNatLanIpType.setStatus("current")
_GemtekDevCpeNatLanIpAddress_Type = IpAddress
_GemtekDevCpeNatLanIpAddress_Object = MibScalar
gemtekDevCpeNatLanIpAddress = _GemtekDevCpeNatLanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 6),
    _GemtekDevCpeNatLanIpAddress_Type()
)
gemtekDevCpeNatLanIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeNatLanIpAddress.setStatus("current")
_GemtekDevCpeNatLanNetmask_Type = IpAddress
_GemtekDevCpeNatLanNetmask_Object = MibScalar
gemtekDevCpeNatLanNetmask = _GemtekDevCpeNatLanNetmask_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 7),
    _GemtekDevCpeNatLanNetmask_Type()
)
gemtekDevCpeNatLanNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeNatLanNetmask.setStatus("current")
_GemtekDevCpeNatMtu_Type = Integer32
_GemtekDevCpeNatMtu_Object = MibScalar
gemtekDevCpeNatMtu = _GemtekDevCpeNatMtu_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 8),
    _GemtekDevCpeNatMtu_Type()
)
gemtekDevCpeNatMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeNatMtu.setStatus("current")
_GemtekDevCpeDhcpServer_ObjectIdentity = ObjectIdentity
gemtekDevCpeDhcpServer = _GemtekDevCpeDhcpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 9)
)


class _GemtekDevCpeDhcpServerEnable_Type(Integer32):
    """Custom type gemtekDevCpeDhcpServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeDhcpServerEnable_Type.__name__ = "Integer32"
_GemtekDevCpeDhcpServerEnable_Object = MibScalar
gemtekDevCpeDhcpServerEnable = _GemtekDevCpeDhcpServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 9, 1),
    _GemtekDevCpeDhcpServerEnable_Type()
)
gemtekDevCpeDhcpServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeDhcpServerEnable.setStatus("current")
_GemtekDevCpeDhcpServerStartIp_Type = IpAddress
_GemtekDevCpeDhcpServerStartIp_Object = MibScalar
gemtekDevCpeDhcpServerStartIp = _GemtekDevCpeDhcpServerStartIp_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 9, 2),
    _GemtekDevCpeDhcpServerStartIp_Type()
)
gemtekDevCpeDhcpServerStartIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeDhcpServerStartIp.setStatus("current")
_GemtekDevCpeDhcpServerEndIp_Type = IpAddress
_GemtekDevCpeDhcpServerEndIp_Object = MibScalar
gemtekDevCpeDhcpServerEndIp = _GemtekDevCpeDhcpServerEndIp_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 9, 3),
    _GemtekDevCpeDhcpServerEndIp_Type()
)
gemtekDevCpeDhcpServerEndIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeDhcpServerEndIp.setStatus("current")
_GemtekDevCpeDhcpServerPrimaryDnsIp_Type = IpAddress
_GemtekDevCpeDhcpServerPrimaryDnsIp_Object = MibScalar
gemtekDevCpeDhcpServerPrimaryDnsIp = _GemtekDevCpeDhcpServerPrimaryDnsIp_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 9, 4),
    _GemtekDevCpeDhcpServerPrimaryDnsIp_Type()
)
gemtekDevCpeDhcpServerPrimaryDnsIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeDhcpServerPrimaryDnsIp.setStatus("current")


class _GemtekDevCpeDhcpServerPrimaryDnsFromIsp_Type(Integer32):
    """Custom type gemtekDevCpeDhcpServerPrimaryDnsFromIsp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeDhcpServerPrimaryDnsFromIsp_Type.__name__ = "Integer32"
_GemtekDevCpeDhcpServerPrimaryDnsFromIsp_Object = MibScalar
gemtekDevCpeDhcpServerPrimaryDnsFromIsp = _GemtekDevCpeDhcpServerPrimaryDnsFromIsp_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 9, 5),
    _GemtekDevCpeDhcpServerPrimaryDnsFromIsp_Type()
)
gemtekDevCpeDhcpServerPrimaryDnsFromIsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeDhcpServerPrimaryDnsFromIsp.setStatus("current")
_GemtekDevCpeDhcpServerSecondDnsIp_Type = IpAddress
_GemtekDevCpeDhcpServerSecondDnsIp_Object = MibScalar
gemtekDevCpeDhcpServerSecondDnsIp = _GemtekDevCpeDhcpServerSecondDnsIp_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 9, 6),
    _GemtekDevCpeDhcpServerSecondDnsIp_Type()
)
gemtekDevCpeDhcpServerSecondDnsIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeDhcpServerSecondDnsIp.setStatus("current")


class _GemtekDevCpeDhcpServerSecondDnsFromIsp_Type(Integer32):
    """Custom type gemtekDevCpeDhcpServerSecondDnsFromIsp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeDhcpServerSecondDnsFromIsp_Type.__name__ = "Integer32"
_GemtekDevCpeDhcpServerSecondDnsFromIsp_Object = MibScalar
gemtekDevCpeDhcpServerSecondDnsFromIsp = _GemtekDevCpeDhcpServerSecondDnsFromIsp_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 9, 7),
    _GemtekDevCpeDhcpServerSecondDnsFromIsp_Type()
)
gemtekDevCpeDhcpServerSecondDnsFromIsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeDhcpServerSecondDnsFromIsp.setStatus("current")
_GemtekDevCpeDhcpServerTertiaryDnsIp_Type = IpAddress
_GemtekDevCpeDhcpServerTertiaryDnsIp_Object = MibScalar
gemtekDevCpeDhcpServerTertiaryDnsIp = _GemtekDevCpeDhcpServerTertiaryDnsIp_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 9, 8),
    _GemtekDevCpeDhcpServerTertiaryDnsIp_Type()
)
gemtekDevCpeDhcpServerTertiaryDnsIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeDhcpServerTertiaryDnsIp.setStatus("current")


class _GemtekDevCpeDhcpServerTertiaryDnsFromIsp_Type(Integer32):
    """Custom type gemtekDevCpeDhcpServerTertiaryDnsFromIsp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeDhcpServerTertiaryDnsFromIsp_Type.__name__ = "Integer32"
_GemtekDevCpeDhcpServerTertiaryDnsFromIsp_Object = MibScalar
gemtekDevCpeDhcpServerTertiaryDnsFromIsp = _GemtekDevCpeDhcpServerTertiaryDnsFromIsp_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 9, 9),
    _GemtekDevCpeDhcpServerTertiaryDnsFromIsp_Type()
)
gemtekDevCpeDhcpServerTertiaryDnsFromIsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeDhcpServerTertiaryDnsFromIsp.setStatus("current")


class _GemtekDevCpeDhcpServerDomainName_Type(OctetString):
    """Custom type gemtekDevCpeDhcpServerDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_GemtekDevCpeDhcpServerDomainName_Type.__name__ = "OctetString"
_GemtekDevCpeDhcpServerDomainName_Object = MibScalar
gemtekDevCpeDhcpServerDomainName = _GemtekDevCpeDhcpServerDomainName_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 9, 10),
    _GemtekDevCpeDhcpServerDomainName_Type()
)
gemtekDevCpeDhcpServerDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeDhcpServerDomainName.setStatus("current")
_GemtekDevCpeDhcpServerMaxLeaseTime_Type = Integer32
_GemtekDevCpeDhcpServerMaxLeaseTime_Object = MibScalar
gemtekDevCpeDhcpServerMaxLeaseTime = _GemtekDevCpeDhcpServerMaxLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 9, 11),
    _GemtekDevCpeDhcpServerMaxLeaseTime_Type()
)
gemtekDevCpeDhcpServerMaxLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeDhcpServerMaxLeaseTime.setStatus("current")
_GemtekDevCpeDhcpServerPermanentHostTable_Object = MibTable
gemtekDevCpeDhcpServerPermanentHostTable = _GemtekDevCpeDhcpServerPermanentHostTable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 9, 12)
)
if mibBuilder.loadTexts:
    gemtekDevCpeDhcpServerPermanentHostTable.setStatus("current")
_GemtekDevCpeDhcpServerPermanentHostEntry_Object = MibTableRow
gemtekDevCpeDhcpServerPermanentHostEntry = _GemtekDevCpeDhcpServerPermanentHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 9, 12, 1)
)
gemtekDevCpeDhcpServerPermanentHostEntry.setIndexNames(
    (0, "Motorola-Cpe-PRIVATE-MIB", "gemtekDevCpeDhcpServerPermanentHostIndex"),
)
if mibBuilder.loadTexts:
    gemtekDevCpeDhcpServerPermanentHostEntry.setStatus("current")
_GemtekDevCpeDhcpServerPermanentHostIndex_Type = Integer32
_GemtekDevCpeDhcpServerPermanentHostIndex_Object = MibTableColumn
gemtekDevCpeDhcpServerPermanentHostIndex = _GemtekDevCpeDhcpServerPermanentHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 9, 12, 1, 1),
    _GemtekDevCpeDhcpServerPermanentHostIndex_Type()
)
gemtekDevCpeDhcpServerPermanentHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeDhcpServerPermanentHostIndex.setStatus("current")


class _GemtekDevCpeDhcpServerPermanentHostMac_Type(OctetString):
    """Custom type gemtekDevCpeDhcpServerPermanentHostMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_GemtekDevCpeDhcpServerPermanentHostMac_Type.__name__ = "OctetString"
_GemtekDevCpeDhcpServerPermanentHostMac_Object = MibTableColumn
gemtekDevCpeDhcpServerPermanentHostMac = _GemtekDevCpeDhcpServerPermanentHostMac_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 9, 12, 1, 2),
    _GemtekDevCpeDhcpServerPermanentHostMac_Type()
)
gemtekDevCpeDhcpServerPermanentHostMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpeDhcpServerPermanentHostMac.setStatus("current")
_GemtekDevCpeDhcpServerPermanentHostIp_Type = IpAddress
_GemtekDevCpeDhcpServerPermanentHostIp_Object = MibTableColumn
gemtekDevCpeDhcpServerPermanentHostIp = _GemtekDevCpeDhcpServerPermanentHostIp_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 9, 12, 1, 3),
    _GemtekDevCpeDhcpServerPermanentHostIp_Type()
)
gemtekDevCpeDhcpServerPermanentHostIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpeDhcpServerPermanentHostIp.setStatus("current")


class _GemtekDevCpeDhcpServerPermanentHostEntryEnable_Type(Integer32):
    """Custom type gemtekDevCpeDhcpServerPermanentHostEntryEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeDhcpServerPermanentHostEntryEnable_Type.__name__ = "Integer32"
_GemtekDevCpeDhcpServerPermanentHostEntryEnable_Object = MibTableColumn
gemtekDevCpeDhcpServerPermanentHostEntryEnable = _GemtekDevCpeDhcpServerPermanentHostEntryEnable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 9, 12, 1, 4),
    _GemtekDevCpeDhcpServerPermanentHostEntryEnable_Type()
)
gemtekDevCpeDhcpServerPermanentHostEntryEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpeDhcpServerPermanentHostEntryEnable.setStatus("current")
_GemtekDevCpeDhcpServerPermanentRowstatus_Type = RowStatus
_GemtekDevCpeDhcpServerPermanentRowstatus_Object = MibTableColumn
gemtekDevCpeDhcpServerPermanentRowstatus = _GemtekDevCpeDhcpServerPermanentRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 9, 12, 1, 5),
    _GemtekDevCpeDhcpServerPermanentRowstatus_Type()
)
gemtekDevCpeDhcpServerPermanentRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpeDhcpServerPermanentRowstatus.setStatus("current")
_GemtekDevCpePortForwarding_ObjectIdentity = ObjectIdentity
gemtekDevCpePortForwarding = _GemtekDevCpePortForwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 10)
)
_GemtekDevCpePortForwardingTable_Object = MibTable
gemtekDevCpePortForwardingTable = _GemtekDevCpePortForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 10, 1)
)
if mibBuilder.loadTexts:
    gemtekDevCpePortForwardingTable.setStatus("current")
_GemtekDevCpePortForwardingEntry_Object = MibTableRow
gemtekDevCpePortForwardingEntry = _GemtekDevCpePortForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 10, 1, 1)
)
gemtekDevCpePortForwardingEntry.setIndexNames(
    (0, "Motorola-Cpe-PRIVATE-MIB", "gemtekDevCpePortForwardingIndex"),
)
if mibBuilder.loadTexts:
    gemtekDevCpePortForwardingEntry.setStatus("current")
_GemtekDevCpePortForwardingIndex_Type = Integer32
_GemtekDevCpePortForwardingIndex_Object = MibTableColumn
gemtekDevCpePortForwardingIndex = _GemtekDevCpePortForwardingIndex_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 10, 1, 1, 1),
    _GemtekDevCpePortForwardingIndex_Type()
)
gemtekDevCpePortForwardingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpePortForwardingIndex.setStatus("current")
_GemtekDevCpePortForwardingWanPortBegin_Type = Integer32
_GemtekDevCpePortForwardingWanPortBegin_Object = MibTableColumn
gemtekDevCpePortForwardingWanPortBegin = _GemtekDevCpePortForwardingWanPortBegin_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 10, 1, 1, 2),
    _GemtekDevCpePortForwardingWanPortBegin_Type()
)
gemtekDevCpePortForwardingWanPortBegin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpePortForwardingWanPortBegin.setStatus("current")
_GemtekDevCpePortForwardingWanPortEnd_Type = Integer32
_GemtekDevCpePortForwardingWanPortEnd_Object = MibTableColumn
gemtekDevCpePortForwardingWanPortEnd = _GemtekDevCpePortForwardingWanPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 10, 1, 1, 3),
    _GemtekDevCpePortForwardingWanPortEnd_Type()
)
gemtekDevCpePortForwardingWanPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpePortForwardingWanPortEnd.setStatus("current")
_GemtekDevCpePortForwardingLanIp_Type = IpAddress
_GemtekDevCpePortForwardingLanIp_Object = MibTableColumn
gemtekDevCpePortForwardingLanIp = _GemtekDevCpePortForwardingLanIp_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 10, 1, 1, 4),
    _GemtekDevCpePortForwardingLanIp_Type()
)
gemtekDevCpePortForwardingLanIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpePortForwardingLanIp.setStatus("current")
_GemtekDevCpePortForwardingLanPortBegin_Type = Integer32
_GemtekDevCpePortForwardingLanPortBegin_Object = MibTableColumn
gemtekDevCpePortForwardingLanPortBegin = _GemtekDevCpePortForwardingLanPortBegin_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 10, 1, 1, 5),
    _GemtekDevCpePortForwardingLanPortBegin_Type()
)
gemtekDevCpePortForwardingLanPortBegin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpePortForwardingLanPortBegin.setStatus("current")
_GemtekDevCpePortForwardingLanPortEnd_Type = Integer32
_GemtekDevCpePortForwardingLanPortEnd_Object = MibTableColumn
gemtekDevCpePortForwardingLanPortEnd = _GemtekDevCpePortForwardingLanPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 10, 1, 1, 6),
    _GemtekDevCpePortForwardingLanPortEnd_Type()
)
gemtekDevCpePortForwardingLanPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpePortForwardingLanPortEnd.setStatus("current")


class _GemtekDevCpePortForwardingProtocol_Type(Integer32):
    """Custom type gemtekDevCpePortForwardingProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 0),
          ("tcpAndUdp", 2),
          ("udp", 1))
    )


_GemtekDevCpePortForwardingProtocol_Type.__name__ = "Integer32"
_GemtekDevCpePortForwardingProtocol_Object = MibTableColumn
gemtekDevCpePortForwardingProtocol = _GemtekDevCpePortForwardingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 10, 1, 1, 7),
    _GemtekDevCpePortForwardingProtocol_Type()
)
gemtekDevCpePortForwardingProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpePortForwardingProtocol.setStatus("current")


class _GemtekDevCpePortForwardingEntryEnable_Type(Integer32):
    """Custom type gemtekDevCpePortForwardingEntryEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpePortForwardingEntryEnable_Type.__name__ = "Integer32"
_GemtekDevCpePortForwardingEntryEnable_Object = MibTableColumn
gemtekDevCpePortForwardingEntryEnable = _GemtekDevCpePortForwardingEntryEnable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 10, 1, 1, 8),
    _GemtekDevCpePortForwardingEntryEnable_Type()
)
gemtekDevCpePortForwardingEntryEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpePortForwardingEntryEnable.setStatus("current")
_GemtekDevCpePortForwardingRowstatus_Type = RowStatus
_GemtekDevCpePortForwardingRowstatus_Object = MibTableColumn
gemtekDevCpePortForwardingRowstatus = _GemtekDevCpePortForwardingRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 10, 1, 1, 9),
    _GemtekDevCpePortForwardingRowstatus_Type()
)
gemtekDevCpePortForwardingRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpePortForwardingRowstatus.setStatus("current")
_GemtekDevCpePortTrigger_ObjectIdentity = ObjectIdentity
gemtekDevCpePortTrigger = _GemtekDevCpePortTrigger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 11)
)
_GemtekDevCpePortTriggerTable_Object = MibTable
gemtekDevCpePortTriggerTable = _GemtekDevCpePortTriggerTable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 11, 1)
)
if mibBuilder.loadTexts:
    gemtekDevCpePortTriggerTable.setStatus("current")
_GemtekDevCpePortTriggerEntry_Object = MibTableRow
gemtekDevCpePortTriggerEntry = _GemtekDevCpePortTriggerEntry_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 11, 1, 1)
)
gemtekDevCpePortTriggerEntry.setIndexNames(
    (0, "Motorola-Cpe-PRIVATE-MIB", "gemtekDevCpePortTriggerIndex"),
)
if mibBuilder.loadTexts:
    gemtekDevCpePortTriggerEntry.setStatus("current")
_GemtekDevCpePortTriggerIndex_Type = Integer32
_GemtekDevCpePortTriggerIndex_Object = MibTableColumn
gemtekDevCpePortTriggerIndex = _GemtekDevCpePortTriggerIndex_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 11, 1, 1, 1),
    _GemtekDevCpePortTriggerIndex_Type()
)
gemtekDevCpePortTriggerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpePortTriggerIndex.setStatus("current")


class _GemtekDevCpePortTriggerName_Type(OctetString):
    """Custom type gemtekDevCpePortTriggerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_GemtekDevCpePortTriggerName_Type.__name__ = "OctetString"
_GemtekDevCpePortTriggerName_Object = MibTableColumn
gemtekDevCpePortTriggerName = _GemtekDevCpePortTriggerName_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 11, 1, 1, 2),
    _GemtekDevCpePortTriggerName_Type()
)
gemtekDevCpePortTriggerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpePortTriggerName.setStatus("current")
_GemtekDevCpePortTriggerTriggerPortBegin_Type = Integer32
_GemtekDevCpePortTriggerTriggerPortBegin_Object = MibTableColumn
gemtekDevCpePortTriggerTriggerPortBegin = _GemtekDevCpePortTriggerTriggerPortBegin_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 11, 1, 1, 3),
    _GemtekDevCpePortTriggerTriggerPortBegin_Type()
)
gemtekDevCpePortTriggerTriggerPortBegin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpePortTriggerTriggerPortBegin.setStatus("current")
_GemtekDevCpePortTriggerTriggerPortEnd_Type = Integer32
_GemtekDevCpePortTriggerTriggerPortEnd_Object = MibTableColumn
gemtekDevCpePortTriggerTriggerPortEnd = _GemtekDevCpePortTriggerTriggerPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 11, 1, 1, 4),
    _GemtekDevCpePortTriggerTriggerPortEnd_Type()
)
gemtekDevCpePortTriggerTriggerPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpePortTriggerTriggerPortEnd.setStatus("current")
_GemtekDevCpePortTriggerForwardingPortBegin_Type = Integer32
_GemtekDevCpePortTriggerForwardingPortBegin_Object = MibTableColumn
gemtekDevCpePortTriggerForwardingPortBegin = _GemtekDevCpePortTriggerForwardingPortBegin_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 11, 1, 1, 5),
    _GemtekDevCpePortTriggerForwardingPortBegin_Type()
)
gemtekDevCpePortTriggerForwardingPortBegin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpePortTriggerForwardingPortBegin.setStatus("current")
_GemtekDevCpePortTriggerForwardingPortEnd_Type = Integer32
_GemtekDevCpePortTriggerForwardingPortEnd_Object = MibTableColumn
gemtekDevCpePortTriggerForwardingPortEnd = _GemtekDevCpePortTriggerForwardingPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 11, 1, 1, 6),
    _GemtekDevCpePortTriggerForwardingPortEnd_Type()
)
gemtekDevCpePortTriggerForwardingPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpePortTriggerForwardingPortEnd.setStatus("current")


class _GemtekDevCpePortTriggerProtocol_Type(Integer32):
    """Custom type gemtekDevCpePortTriggerProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 0),
          ("udp", 1))
    )


_GemtekDevCpePortTriggerProtocol_Type.__name__ = "Integer32"
_GemtekDevCpePortTriggerProtocol_Object = MibTableColumn
gemtekDevCpePortTriggerProtocol = _GemtekDevCpePortTriggerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 11, 1, 1, 7),
    _GemtekDevCpePortTriggerProtocol_Type()
)
gemtekDevCpePortTriggerProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpePortTriggerProtocol.setStatus("current")


class _GemtekDevCpePortTriggerEntryEnable_Type(Integer32):
    """Custom type gemtekDevCpePortTriggerEntryEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpePortTriggerEntryEnable_Type.__name__ = "Integer32"
_GemtekDevCpePortTriggerEntryEnable_Object = MibTableColumn
gemtekDevCpePortTriggerEntryEnable = _GemtekDevCpePortTriggerEntryEnable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 11, 1, 1, 8),
    _GemtekDevCpePortTriggerEntryEnable_Type()
)
gemtekDevCpePortTriggerEntryEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpePortTriggerEntryEnable.setStatus("current")
_GemtekDevCpePortTriggerRowstatus_Type = RowStatus
_GemtekDevCpePortTriggerRowstatus_Object = MibTableColumn
gemtekDevCpePortTriggerRowstatus = _GemtekDevCpePortTriggerRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 11, 1, 1, 9),
    _GemtekDevCpePortTriggerRowstatus_Type()
)
gemtekDevCpePortTriggerRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpePortTriggerRowstatus.setStatus("current")
_GemtekDevCpeDhcpClientList_ObjectIdentity = ObjectIdentity
gemtekDevCpeDhcpClientList = _GemtekDevCpeDhcpClientList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 12)
)
_GemtekDevCpeDhcpClentListTable_Object = MibTable
gemtekDevCpeDhcpClentListTable = _GemtekDevCpeDhcpClentListTable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 12, 1)
)
if mibBuilder.loadTexts:
    gemtekDevCpeDhcpClentListTable.setStatus("current")
_GemtekDevCpeDhcpClentListEntry_Object = MibTableRow
gemtekDevCpeDhcpClentListEntry = _GemtekDevCpeDhcpClentListEntry_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 12, 1, 1)
)
gemtekDevCpeDhcpClentListEntry.setIndexNames(
    (0, "Motorola-Cpe-PRIVATE-MIB", "gemtekDevCpeDhcpClentListIndex"),
)
if mibBuilder.loadTexts:
    gemtekDevCpeDhcpClentListEntry.setStatus("current")
_GemtekDevCpeDhcpClentListIndex_Type = Integer32
_GemtekDevCpeDhcpClentListIndex_Object = MibTableColumn
gemtekDevCpeDhcpClentListIndex = _GemtekDevCpeDhcpClentListIndex_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 12, 1, 1, 1),
    _GemtekDevCpeDhcpClentListIndex_Type()
)
gemtekDevCpeDhcpClentListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeDhcpClentListIndex.setStatus("current")
_GemtekDevCpeDhcpClentListIp_Type = IpAddress
_GemtekDevCpeDhcpClentListIp_Object = MibTableColumn
gemtekDevCpeDhcpClentListIp = _GemtekDevCpeDhcpClentListIp_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 12, 1, 1, 2),
    _GemtekDevCpeDhcpClentListIp_Type()
)
gemtekDevCpeDhcpClentListIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeDhcpClentListIp.setStatus("current")


class _GemtekDevCpeDhcpClentListMacAddress_Type(OctetString):
    """Custom type gemtekDevCpeDhcpClentListMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_GemtekDevCpeDhcpClentListMacAddress_Type.__name__ = "OctetString"
_GemtekDevCpeDhcpClentListMacAddress_Object = MibTableColumn
gemtekDevCpeDhcpClentListMacAddress = _GemtekDevCpeDhcpClentListMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 12, 1, 1, 3),
    _GemtekDevCpeDhcpClentListMacAddress_Type()
)
gemtekDevCpeDhcpClentListMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeDhcpClentListMacAddress.setStatus("current")
_GemtekDevCpeDhcpClentListExpireTime_Type = OctetString
_GemtekDevCpeDhcpClentListExpireTime_Object = MibTableColumn
gemtekDevCpeDhcpClentListExpireTime = _GemtekDevCpeDhcpClentListExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 12, 1, 1, 4),
    _GemtekDevCpeDhcpClentListExpireTime_Type()
)
gemtekDevCpeDhcpClentListExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeDhcpClentListExpireTime.setStatus("current")
_GemtekDevCpeDscpConfiguration_ObjectIdentity = ObjectIdentity
gemtekDevCpeDscpConfiguration = _GemtekDevCpeDscpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 13)
)
_GemtekDevCpeMgmtDscpId_Type = Integer32
_GemtekDevCpeMgmtDscpId_Object = MibScalar
gemtekDevCpeMgmtDscpId = _GemtekDevCpeMgmtDscpId_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 13, 1),
    _GemtekDevCpeMgmtDscpId_Type()
)
gemtekDevCpeMgmtDscpId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeMgmtDscpId.setStatus("current")


class _GemtekDevCpeDropDataPacket_Type(Integer32):
    """Custom type gemtekDevCpeDropDataPacket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeDropDataPacket_Type.__name__ = "Integer32"
_GemtekDevCpeDropDataPacket_Object = MibScalar
gemtekDevCpeDropDataPacket = _GemtekDevCpeDropDataPacket_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 13, 2),
    _GemtekDevCpeDropDataPacket_Type()
)
gemtekDevCpeDropDataPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeDropDataPacket.setStatus("current")
_GemtekDevCpeNatWanDhcpLeaseTime_Type = Unsigned32
_GemtekDevCpeNatWanDhcpLeaseTime_Object = MibScalar
gemtekDevCpeNatWanDhcpLeaseTime = _GemtekDevCpeNatWanDhcpLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 14),
    _GemtekDevCpeNatWanDhcpLeaseTime_Type()
)
gemtekDevCpeNatWanDhcpLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeNatWanDhcpLeaseTime.setStatus("current")
_GemtekDevCpeNatWanDhcpRenewalTime_Type = Unsigned32
_GemtekDevCpeNatWanDhcpRenewalTime_Object = MibScalar
gemtekDevCpeNatWanDhcpRenewalTime = _GemtekDevCpeNatWanDhcpRenewalTime_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 15),
    _GemtekDevCpeNatWanDhcpRenewalTime_Type()
)
gemtekDevCpeNatWanDhcpRenewalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeNatWanDhcpRenewalTime.setStatus("current")
_GemtekDevCpeNatWanDhcpRebindTime_Type = Unsigned32
_GemtekDevCpeNatWanDhcpRebindTime_Object = MibScalar
gemtekDevCpeNatWanDhcpRebindTime = _GemtekDevCpeNatWanDhcpRebindTime_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 16),
    _GemtekDevCpeNatWanDhcpRebindTime_Type()
)
gemtekDevCpeNatWanDhcpRebindTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeNatWanDhcpRebindTime.setStatus("current")
_GemtekDevCpeNatModeVLAN_ObjectIdentity = ObjectIdentity
gemtekDevCpeNatModeVLAN = _GemtekDevCpeNatModeVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 17)
)
_GemtekDevCpeNatModeMgmtVlan_ObjectIdentity = ObjectIdentity
gemtekDevCpeNatModeMgmtVlan = _GemtekDevCpeNatModeMgmtVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 17, 1)
)


class _GemtekDevCpeNatModeMgmtVlanEnalbe_Type(Integer32):
    """Custom type gemtekDevCpeNatModeMgmtVlanEnalbe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeNatModeMgmtVlanEnalbe_Type.__name__ = "Integer32"
_GemtekDevCpeNatModeMgmtVlanEnalbe_Object = MibScalar
gemtekDevCpeNatModeMgmtVlanEnalbe = _GemtekDevCpeNatModeMgmtVlanEnalbe_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 17, 1, 1),
    _GemtekDevCpeNatModeMgmtVlanEnalbe_Type()
)
gemtekDevCpeNatModeMgmtVlanEnalbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeNatModeMgmtVlanEnalbe.setStatus("current")
_GemtekDevCpeNatModeMgmtVlanVid_Type = Unsigned32
_GemtekDevCpeNatModeMgmtVlanVid_Object = MibScalar
gemtekDevCpeNatModeMgmtVlanVid = _GemtekDevCpeNatModeMgmtVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 17, 1, 2),
    _GemtekDevCpeNatModeMgmtVlanVid_Type()
)
gemtekDevCpeNatModeMgmtVlanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeNatModeMgmtVlanVid.setStatus("current")
_GemtekDevCpeNatModeMgmtVlanVp_Type = Unsigned32
_GemtekDevCpeNatModeMgmtVlanVp_Object = MibScalar
gemtekDevCpeNatModeMgmtVlanVp = _GemtekDevCpeNatModeMgmtVlanVp_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 17, 1, 3),
    _GemtekDevCpeNatModeMgmtVlanVp_Type()
)
gemtekDevCpeNatModeMgmtVlanVp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeNatModeMgmtVlanVp.setStatus("current")
_GemtekDevCpeNatModeDataVlan_ObjectIdentity = ObjectIdentity
gemtekDevCpeNatModeDataVlan = _GemtekDevCpeNatModeDataVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 17, 2)
)


class _GemtekDevCpeNatModeDataVlanEnalbe_Type(Integer32):
    """Custom type gemtekDevCpeNatModeDataVlanEnalbe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeNatModeDataVlanEnalbe_Type.__name__ = "Integer32"
_GemtekDevCpeNatModeDataVlanEnalbe_Object = MibScalar
gemtekDevCpeNatModeDataVlanEnalbe = _GemtekDevCpeNatModeDataVlanEnalbe_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 17, 2, 1),
    _GemtekDevCpeNatModeDataVlanEnalbe_Type()
)
gemtekDevCpeNatModeDataVlanEnalbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeNatModeDataVlanEnalbe.setStatus("current")
_GemtekDevCpeNatModeDataVlanVid_Type = Unsigned32
_GemtekDevCpeNatModeDataVlanVid_Object = MibScalar
gemtekDevCpeNatModeDataVlanVid = _GemtekDevCpeNatModeDataVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 17, 2, 2),
    _GemtekDevCpeNatModeDataVlanVid_Type()
)
gemtekDevCpeNatModeDataVlanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeNatModeDataVlanVid.setStatus("current")
_GemtekDevCpeNatModeDataVlanVp_Type = Unsigned32
_GemtekDevCpeNatModeDataVlanVp_Object = MibScalar
gemtekDevCpeNatModeDataVlanVp = _GemtekDevCpeNatModeDataVlanVp_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 8, 3, 17, 2, 3),
    _GemtekDevCpeNatModeDataVlanVp_Type()
)
gemtekDevCpeNatModeDataVlanVp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeNatModeDataVlanVp.setStatus("current")
_GemtekDevCpeFirewall_ObjectIdentity = ObjectIdentity
gemtekDevCpeFirewall = _GemtekDevCpeFirewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9)
)


class _GemtekDevCpeAllowWebAccessingFromWan_Type(Integer32):
    """Custom type gemtekDevCpeAllowWebAccessingFromWan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeAllowWebAccessingFromWan_Type.__name__ = "Integer32"
_GemtekDevCpeAllowWebAccessingFromWan_Object = MibScalar
gemtekDevCpeAllowWebAccessingFromWan = _GemtekDevCpeAllowWebAccessingFromWan_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 1),
    _GemtekDevCpeAllowWebAccessingFromWan_Type()
)
gemtekDevCpeAllowWebAccessingFromWan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeAllowWebAccessingFromWan.setStatus("current")


class _GemtekDevCpeAllowTelnetAccessingFromWan_Type(Integer32):
    """Custom type gemtekDevCpeAllowTelnetAccessingFromWan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeAllowTelnetAccessingFromWan_Type.__name__ = "Integer32"
_GemtekDevCpeAllowTelnetAccessingFromWan_Object = MibScalar
gemtekDevCpeAllowTelnetAccessingFromWan = _GemtekDevCpeAllowTelnetAccessingFromWan_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 2),
    _GemtekDevCpeAllowTelnetAccessingFromWan_Type()
)
gemtekDevCpeAllowTelnetAccessingFromWan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeAllowTelnetAccessingFromWan.setStatus("current")


class _GemtekDevCpeDmzEnable_Type(Integer32):
    """Custom type gemtekDevCpeDmzEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeDmzEnable_Type.__name__ = "Integer32"
_GemtekDevCpeDmzEnable_Object = MibScalar
gemtekDevCpeDmzEnable = _GemtekDevCpeDmzEnable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 3),
    _GemtekDevCpeDmzEnable_Type()
)
gemtekDevCpeDmzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeDmzEnable.setStatus("current")
_GemtekDevCpeDmzIpAddress_Type = IpAddress
_GemtekDevCpeDmzIpAddress_Object = MibScalar
gemtekDevCpeDmzIpAddress = _GemtekDevCpeDmzIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 4),
    _GemtekDevCpeDmzIpAddress_Type()
)
gemtekDevCpeDmzIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeDmzIpAddress.setStatus("current")


class _GemtekDevCpeRedirectIcmpToTheDmzHostEnable_Type(Integer32):
    """Custom type gemtekDevCpeRedirectIcmpToTheDmzHostEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeRedirectIcmpToTheDmzHostEnable_Type.__name__ = "Integer32"
_GemtekDevCpeRedirectIcmpToTheDmzHostEnable_Object = MibScalar
gemtekDevCpeRedirectIcmpToTheDmzHostEnable = _GemtekDevCpeRedirectIcmpToTheDmzHostEnable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 5),
    _GemtekDevCpeRedirectIcmpToTheDmzHostEnable_Type()
)
gemtekDevCpeRedirectIcmpToTheDmzHostEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeRedirectIcmpToTheDmzHostEnable.setStatus("current")


class _GemtekDevCpeFirewallEnable_Type(Integer32):
    """Custom type gemtekDevCpeFirewallEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeFirewallEnable_Type.__name__ = "Integer32"
_GemtekDevCpeFirewallEnable_Object = MibScalar
gemtekDevCpeFirewallEnable = _GemtekDevCpeFirewallEnable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 6),
    _GemtekDevCpeFirewallEnable_Type()
)
gemtekDevCpeFirewallEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallEnable.setStatus("current")
_GemtekDevCpeFirewallTable_Object = MibTable
gemtekDevCpeFirewallTable = _GemtekDevCpeFirewallTable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 7)
)
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallTable.setStatus("current")
_GemtekDevCpeFirewallEntry_Object = MibTableRow
gemtekDevCpeFirewallEntry = _GemtekDevCpeFirewallEntry_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 7, 1)
)
gemtekDevCpeFirewallEntry.setIndexNames(
    (0, "Motorola-Cpe-PRIVATE-MIB", "gemtekDevCpeFirewallIndex"),
)
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallEntry.setStatus("current")
_GemtekDevCpeFirewallIndex_Type = Integer32
_GemtekDevCpeFirewallIndex_Object = MibTableColumn
gemtekDevCpeFirewallIndex = _GemtekDevCpeFirewallIndex_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 7, 1, 1),
    _GemtekDevCpeFirewallIndex_Type()
)
gemtekDevCpeFirewallIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallIndex.setStatus("current")
_GemtekDevCpeFirewallName_Type = OctetString
_GemtekDevCpeFirewallName_Object = MibTableColumn
gemtekDevCpeFirewallName = _GemtekDevCpeFirewallName_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 7, 1, 2),
    _GemtekDevCpeFirewallName_Type()
)
gemtekDevCpeFirewallName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallName.setStatus("current")


class _GemtekDevCpeFirewallAction_Type(Integer32):
    """Custom type gemtekDevCpeFirewallAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 0))
    )


_GemtekDevCpeFirewallAction_Type.__name__ = "Integer32"
_GemtekDevCpeFirewallAction_Object = MibTableColumn
gemtekDevCpeFirewallAction = _GemtekDevCpeFirewallAction_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 7, 1, 3),
    _GemtekDevCpeFirewallAction_Type()
)
gemtekDevCpeFirewallAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallAction.setStatus("current")


class _GemtekDevCpeFirewallInterface_Type(Integer32):
    """Custom type gemtekDevCpeFirewallInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 0),
          ("wimax", 1))
    )


_GemtekDevCpeFirewallInterface_Type.__name__ = "Integer32"
_GemtekDevCpeFirewallInterface_Object = MibTableColumn
gemtekDevCpeFirewallInterface = _GemtekDevCpeFirewallInterface_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 7, 1, 4),
    _GemtekDevCpeFirewallInterface_Type()
)
gemtekDevCpeFirewallInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallInterface.setStatus("current")


class _GemtekDevCpeFirewallProtocol_Type(Integer32):
    """Custom type gemtekDevCpeFirewallProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("icmp", 1),
          ("tcp", 6),
          ("udp", 17))
    )


_GemtekDevCpeFirewallProtocol_Type.__name__ = "Integer32"
_GemtekDevCpeFirewallProtocol_Object = MibTableColumn
gemtekDevCpeFirewallProtocol = _GemtekDevCpeFirewallProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 7, 1, 5),
    _GemtekDevCpeFirewallProtocol_Type()
)
gemtekDevCpeFirewallProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallProtocol.setStatus("current")


class _GemtekDevCpeFirewallPriority_Type(Integer32):
    """Custom type gemtekDevCpeFirewallPriority based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("eight", 8),
          ("five", 5),
          ("four", 4),
          ("hi", 1),
          ("lo", 10),
          ("nine", 9),
          ("seven", 7),
          ("six", 6),
          ("three", 3),
          ("two", 2))
    )


_GemtekDevCpeFirewallPriority_Type.__name__ = "Integer32"
_GemtekDevCpeFirewallPriority_Object = MibTableColumn
gemtekDevCpeFirewallPriority = _GemtekDevCpeFirewallPriority_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 7, 1, 6),
    _GemtekDevCpeFirewallPriority_Type()
)
gemtekDevCpeFirewallPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallPriority.setStatus("current")


class _GemtekDevCpeFirewallEntryEnable_Type(Integer32):
    """Custom type gemtekDevCpeFirewallEntryEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeFirewallEntryEnable_Type.__name__ = "Integer32"
_GemtekDevCpeFirewallEntryEnable_Object = MibTableColumn
gemtekDevCpeFirewallEntryEnable = _GemtekDevCpeFirewallEntryEnable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 7, 1, 7),
    _GemtekDevCpeFirewallEntryEnable_Type()
)
gemtekDevCpeFirewallEntryEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallEntryEnable.setStatus("current")


class _GemtekDevCpeFirewallSrcMac_Type(OctetString):
    """Custom type gemtekDevCpeFirewallSrcMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_GemtekDevCpeFirewallSrcMac_Type.__name__ = "OctetString"
_GemtekDevCpeFirewallSrcMac_Object = MibTableColumn
gemtekDevCpeFirewallSrcMac = _GemtekDevCpeFirewallSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 7, 1, 8),
    _GemtekDevCpeFirewallSrcMac_Type()
)
gemtekDevCpeFirewallSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallSrcMac.setStatus("current")


class _GemtekDevCpeFirewallDstMac_Type(OctetString):
    """Custom type gemtekDevCpeFirewallDstMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_GemtekDevCpeFirewallDstMac_Type.__name__ = "OctetString"
_GemtekDevCpeFirewallDstMac_Object = MibTableColumn
gemtekDevCpeFirewallDstMac = _GemtekDevCpeFirewallDstMac_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 7, 1, 9),
    _GemtekDevCpeFirewallDstMac_Type()
)
gemtekDevCpeFirewallDstMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallDstMac.setStatus("current")
_GemtekDevCpeFirewallSrcIpAddress_Type = IpAddress
_GemtekDevCpeFirewallSrcIpAddress_Object = MibTableColumn
gemtekDevCpeFirewallSrcIpAddress = _GemtekDevCpeFirewallSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 7, 1, 10),
    _GemtekDevCpeFirewallSrcIpAddress_Type()
)
gemtekDevCpeFirewallSrcIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallSrcIpAddress.setStatus("current")
_GemtekDevCpeFirewallDstIpAddress_Type = IpAddress
_GemtekDevCpeFirewallDstIpAddress_Object = MibTableColumn
gemtekDevCpeFirewallDstIpAddress = _GemtekDevCpeFirewallDstIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 7, 1, 11),
    _GemtekDevCpeFirewallDstIpAddress_Type()
)
gemtekDevCpeFirewallDstIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallDstIpAddress.setStatus("current")
_GemtekDevCpeFirewallSrcPortRangeBegin_Type = Integer32
_GemtekDevCpeFirewallSrcPortRangeBegin_Object = MibTableColumn
gemtekDevCpeFirewallSrcPortRangeBegin = _GemtekDevCpeFirewallSrcPortRangeBegin_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 7, 1, 12),
    _GemtekDevCpeFirewallSrcPortRangeBegin_Type()
)
gemtekDevCpeFirewallSrcPortRangeBegin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallSrcPortRangeBegin.setStatus("current")
_GemtekDevCpeFirewallSrcPortRangeEnd_Type = Integer32
_GemtekDevCpeFirewallSrcPortRangeEnd_Object = MibTableColumn
gemtekDevCpeFirewallSrcPortRangeEnd = _GemtekDevCpeFirewallSrcPortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 7, 1, 13),
    _GemtekDevCpeFirewallSrcPortRangeEnd_Type()
)
gemtekDevCpeFirewallSrcPortRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallSrcPortRangeEnd.setStatus("current")
_GemtekDevCpeFirewallDstPortRangeBegin_Type = Integer32
_GemtekDevCpeFirewallDstPortRangeBegin_Object = MibTableColumn
gemtekDevCpeFirewallDstPortRangeBegin = _GemtekDevCpeFirewallDstPortRangeBegin_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 7, 1, 14),
    _GemtekDevCpeFirewallDstPortRangeBegin_Type()
)
gemtekDevCpeFirewallDstPortRangeBegin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallDstPortRangeBegin.setStatus("current")
_GemtekDevCpeFirewallDstPortRangeEnd_Type = Integer32
_GemtekDevCpeFirewallDstPortRangeEnd_Object = MibTableColumn
gemtekDevCpeFirewallDstPortRangeEnd = _GemtekDevCpeFirewallDstPortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 7, 1, 15),
    _GemtekDevCpeFirewallDstPortRangeEnd_Type()
)
gemtekDevCpeFirewallDstPortRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallDstPortRangeEnd.setStatus("current")
_GemtekDevCpeFirewallRowstatus_Type = RowStatus
_GemtekDevCpeFirewallRowstatus_Object = MibTableColumn
gemtekDevCpeFirewallRowstatus = _GemtekDevCpeFirewallRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 7, 1, 16),
    _GemtekDevCpeFirewallRowstatus_Type()
)
gemtekDevCpeFirewallRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallRowstatus.setStatus("current")


class _GemtekDevCpeTelnetEnable_Type(Integer32):
    """Custom type gemtekDevCpeTelnetEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeTelnetEnable_Type.__name__ = "Integer32"
_GemtekDevCpeTelnetEnable_Object = MibScalar
gemtekDevCpeTelnetEnable = _GemtekDevCpeTelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 8),
    _GemtekDevCpeTelnetEnable_Type()
)
gemtekDevCpeTelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeTelnetEnable.setStatus("current")


class _GemtekDevCpeFirewallEtherTypeFilterOneEnable_Type(Integer32):
    """Custom type gemtekDevCpeFirewallEtherTypeFilterOneEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeFirewallEtherTypeFilterOneEnable_Type.__name__ = "Integer32"
_GemtekDevCpeFirewallEtherTypeFilterOneEnable_Object = MibScalar
gemtekDevCpeFirewallEtherTypeFilterOneEnable = _GemtekDevCpeFirewallEtherTypeFilterOneEnable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 9),
    _GemtekDevCpeFirewallEtherTypeFilterOneEnable_Type()
)
gemtekDevCpeFirewallEtherTypeFilterOneEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallEtherTypeFilterOneEnable.setStatus("current")


class _GemtekDevCpeFirewallEtherTypeFilterOneTypeDeny_Type(OctetString):
    """Custom type gemtekDevCpeFirewallEtherTypeFilterOneTypeDeny based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_GemtekDevCpeFirewallEtherTypeFilterOneTypeDeny_Type.__name__ = "OctetString"
_GemtekDevCpeFirewallEtherTypeFilterOneTypeDeny_Object = MibScalar
gemtekDevCpeFirewallEtherTypeFilterOneTypeDeny = _GemtekDevCpeFirewallEtherTypeFilterOneTypeDeny_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 10),
    _GemtekDevCpeFirewallEtherTypeFilterOneTypeDeny_Type()
)
gemtekDevCpeFirewallEtherTypeFilterOneTypeDeny.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallEtherTypeFilterOneTypeDeny.setStatus("current")


class _GemtekDevCpeFirewallEtherTypeFilterTwoEnable_Type(Integer32):
    """Custom type gemtekDevCpeFirewallEtherTypeFilterTwoEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeFirewallEtherTypeFilterTwoEnable_Type.__name__ = "Integer32"
_GemtekDevCpeFirewallEtherTypeFilterTwoEnable_Object = MibScalar
gemtekDevCpeFirewallEtherTypeFilterTwoEnable = _GemtekDevCpeFirewallEtherTypeFilterTwoEnable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 11),
    _GemtekDevCpeFirewallEtherTypeFilterTwoEnable_Type()
)
gemtekDevCpeFirewallEtherTypeFilterTwoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallEtherTypeFilterTwoEnable.setStatus("current")


class _GemtekDevCpeFirewallEtherTypeFilterTwoTypeDeny_Type(OctetString):
    """Custom type gemtekDevCpeFirewallEtherTypeFilterTwoTypeDeny based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_GemtekDevCpeFirewallEtherTypeFilterTwoTypeDeny_Type.__name__ = "OctetString"
_GemtekDevCpeFirewallEtherTypeFilterTwoTypeDeny_Object = MibScalar
gemtekDevCpeFirewallEtherTypeFilterTwoTypeDeny = _GemtekDevCpeFirewallEtherTypeFilterTwoTypeDeny_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 12),
    _GemtekDevCpeFirewallEtherTypeFilterTwoTypeDeny_Type()
)
gemtekDevCpeFirewallEtherTypeFilterTwoTypeDeny.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallEtherTypeFilterTwoTypeDeny.setStatus("current")


class _GemtekDevCpeFirewallEtherTypeFilterThreeEnable_Type(Integer32):
    """Custom type gemtekDevCpeFirewallEtherTypeFilterThreeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeFirewallEtherTypeFilterThreeEnable_Type.__name__ = "Integer32"
_GemtekDevCpeFirewallEtherTypeFilterThreeEnable_Object = MibScalar
gemtekDevCpeFirewallEtherTypeFilterThreeEnable = _GemtekDevCpeFirewallEtherTypeFilterThreeEnable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 13),
    _GemtekDevCpeFirewallEtherTypeFilterThreeEnable_Type()
)
gemtekDevCpeFirewallEtherTypeFilterThreeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallEtherTypeFilterThreeEnable.setStatus("current")


class _GemtekDevCpeFirewallEtherTypeFilterThreeTypeDeny_Type(OctetString):
    """Custom type gemtekDevCpeFirewallEtherTypeFilterThreeTypeDeny based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_GemtekDevCpeFirewallEtherTypeFilterThreeTypeDeny_Type.__name__ = "OctetString"
_GemtekDevCpeFirewallEtherTypeFilterThreeTypeDeny_Object = MibScalar
gemtekDevCpeFirewallEtherTypeFilterThreeTypeDeny = _GemtekDevCpeFirewallEtherTypeFilterThreeTypeDeny_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 14),
    _GemtekDevCpeFirewallEtherTypeFilterThreeTypeDeny_Type()
)
gemtekDevCpeFirewallEtherTypeFilterThreeTypeDeny.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallEtherTypeFilterThreeTypeDeny.setStatus("current")


class _GemtekDevCpeFirewallEtherTypeFilterFourEnable_Type(Integer32):
    """Custom type gemtekDevCpeFirewallEtherTypeFilterFourEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeFirewallEtherTypeFilterFourEnable_Type.__name__ = "Integer32"
_GemtekDevCpeFirewallEtherTypeFilterFourEnable_Object = MibScalar
gemtekDevCpeFirewallEtherTypeFilterFourEnable = _GemtekDevCpeFirewallEtherTypeFilterFourEnable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 15),
    _GemtekDevCpeFirewallEtherTypeFilterFourEnable_Type()
)
gemtekDevCpeFirewallEtherTypeFilterFourEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallEtherTypeFilterFourEnable.setStatus("current")


class _GemtekDevCpeFirewallEtherTypeFilterFourTypeDeny_Type(OctetString):
    """Custom type gemtekDevCpeFirewallEtherTypeFilterFourTypeDeny based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_GemtekDevCpeFirewallEtherTypeFilterFourTypeDeny_Type.__name__ = "OctetString"
_GemtekDevCpeFirewallEtherTypeFilterFourTypeDeny_Object = MibScalar
gemtekDevCpeFirewallEtherTypeFilterFourTypeDeny = _GemtekDevCpeFirewallEtherTypeFilterFourTypeDeny_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 16),
    _GemtekDevCpeFirewallEtherTypeFilterFourTypeDeny_Type()
)
gemtekDevCpeFirewallEtherTypeFilterFourTypeDeny.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallEtherTypeFilterFourTypeDeny.setStatus("current")


class _GemtekDevCpeFirewallEtherTypeFilterFiveEnable_Type(Integer32):
    """Custom type gemtekDevCpeFirewallEtherTypeFilterFiveEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeFirewallEtherTypeFilterFiveEnable_Type.__name__ = "Integer32"
_GemtekDevCpeFirewallEtherTypeFilterFiveEnable_Object = MibScalar
gemtekDevCpeFirewallEtherTypeFilterFiveEnable = _GemtekDevCpeFirewallEtherTypeFilterFiveEnable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 17),
    _GemtekDevCpeFirewallEtherTypeFilterFiveEnable_Type()
)
gemtekDevCpeFirewallEtherTypeFilterFiveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallEtherTypeFilterFiveEnable.setStatus("current")


class _GemtekDevCpeFirewallEtherTypeFilterFiveTypeDeny_Type(OctetString):
    """Custom type gemtekDevCpeFirewallEtherTypeFilterFiveTypeDeny based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_GemtekDevCpeFirewallEtherTypeFilterFiveTypeDeny_Type.__name__ = "OctetString"
_GemtekDevCpeFirewallEtherTypeFilterFiveTypeDeny_Object = MibScalar
gemtekDevCpeFirewallEtherTypeFilterFiveTypeDeny = _GemtekDevCpeFirewallEtherTypeFilterFiveTypeDeny_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 18),
    _GemtekDevCpeFirewallEtherTypeFilterFiveTypeDeny_Type()
)
gemtekDevCpeFirewallEtherTypeFilterFiveTypeDeny.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallEtherTypeFilterFiveTypeDeny.setStatus("current")


class _GemtekDevCpeFirewallPPPoEEnable_Type(Integer32):
    """Custom type gemtekDevCpeFirewallPPPoEEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeFirewallPPPoEEnable_Type.__name__ = "Integer32"
_GemtekDevCpeFirewallPPPoEEnable_Object = MibScalar
gemtekDevCpeFirewallPPPoEEnable = _GemtekDevCpeFirewallPPPoEEnable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 9, 19),
    _GemtekDevCpeFirewallPPPoEEnable_Type()
)
gemtekDevCpeFirewallPPPoEEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeFirewallPPPoEEnable.setStatus("current")
_GemtekDevCpeServiceFlow_ObjectIdentity = ObjectIdentity
gemtekDevCpeServiceFlow = _GemtekDevCpeServiceFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 11)
)
_GemtekDevCpeServiceFlowTable_Object = MibTable
gemtekDevCpeServiceFlowTable = _GemtekDevCpeServiceFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 11, 1)
)
if mibBuilder.loadTexts:
    gemtekDevCpeServiceFlowTable.setStatus("current")
_GemtekDevCpeServiceFlowEntry_Object = MibTableRow
gemtekDevCpeServiceFlowEntry = _GemtekDevCpeServiceFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 11, 1, 1)
)
gemtekDevCpeServiceFlowEntry.setIndexNames(
    (0, "Motorola-Cpe-PRIVATE-MIB", "gemtekDevCpeServiceFlowIndex"),
)
if mibBuilder.loadTexts:
    gemtekDevCpeServiceFlowEntry.setStatus("current")
_GemtekDevCpeServiceFlowIndex_Type = Integer32
_GemtekDevCpeServiceFlowIndex_Object = MibTableColumn
gemtekDevCpeServiceFlowIndex = _GemtekDevCpeServiceFlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 11, 1, 1, 1),
    _GemtekDevCpeServiceFlowIndex_Type()
)
gemtekDevCpeServiceFlowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeServiceFlowIndex.setStatus("current")
_GemtekDevCpeServiceFlowSFID_Type = Unsigned32
_GemtekDevCpeServiceFlowSFID_Object = MibTableColumn
gemtekDevCpeServiceFlowSFID = _GemtekDevCpeServiceFlowSFID_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 11, 1, 1, 2),
    _GemtekDevCpeServiceFlowSFID_Type()
)
gemtekDevCpeServiceFlowSFID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeServiceFlowSFID.setStatus("current")
_GemtekDevCpeServiceFlowCID_Type = Unsigned32
_GemtekDevCpeServiceFlowCID_Object = MibTableColumn
gemtekDevCpeServiceFlowCID = _GemtekDevCpeServiceFlowCID_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 11, 1, 1, 3),
    _GemtekDevCpeServiceFlowCID_Type()
)
gemtekDevCpeServiceFlowCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeServiceFlowCID.setStatus("current")
_GemtekDevCpeServiceFlowBCID_Type = Unsigned32
_GemtekDevCpeServiceFlowBCID_Object = MibTableColumn
gemtekDevCpeServiceFlowBCID = _GemtekDevCpeServiceFlowBCID_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 11, 1, 1, 4),
    _GemtekDevCpeServiceFlowBCID_Type()
)
gemtekDevCpeServiceFlowBCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeServiceFlowBCID.setStatus("current")


class _GemtekDevCpeServiceFlowType_Type(Integer32):
    """Custom type gemtekDevCpeServiceFlowType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("basic", 0),
          ("data", 3),
          ("multicast", 4),
          ("primary", 1),
          ("secondary", 2))
    )


_GemtekDevCpeServiceFlowType_Type.__name__ = "Integer32"
_GemtekDevCpeServiceFlowType_Object = MibTableColumn
gemtekDevCpeServiceFlowType = _GemtekDevCpeServiceFlowType_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 11, 1, 1, 5),
    _GemtekDevCpeServiceFlowType_Type()
)
gemtekDevCpeServiceFlowType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeServiceFlowType.setStatus("current")


class _GemtekDevCpeServiceFlowState_Type(Integer32):
    """Custom type gemtekDevCpeServiceFlowState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("admitted", 1),
          ("provisioned", 0))
    )


_GemtekDevCpeServiceFlowState_Type.__name__ = "Integer32"
_GemtekDevCpeServiceFlowState_Object = MibTableColumn
gemtekDevCpeServiceFlowState = _GemtekDevCpeServiceFlowState_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 11, 1, 1, 6),
    _GemtekDevCpeServiceFlowState_Type()
)
gemtekDevCpeServiceFlowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeServiceFlowState.setStatus("current")


class _GemtekDevCpeServiceFlowDirection_Type(Integer32):
    """Custom type gemtekDevCpeServiceFlowDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 3),
          ("downlink", 2),
          ("uplink", 1))
    )


_GemtekDevCpeServiceFlowDirection_Type.__name__ = "Integer32"
_GemtekDevCpeServiceFlowDirection_Object = MibTableColumn
gemtekDevCpeServiceFlowDirection = _GemtekDevCpeServiceFlowDirection_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 11, 1, 1, 7),
    _GemtekDevCpeServiceFlowDirection_Type()
)
gemtekDevCpeServiceFlowDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeServiceFlowDirection.setStatus("current")


class _GemtekDevCpeServiceFlowEnable_Type(Integer32):
    """Custom type gemtekDevCpeServiceFlowEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_GemtekDevCpeServiceFlowEnable_Type.__name__ = "Integer32"
_GemtekDevCpeServiceFlowEnable_Object = MibTableColumn
gemtekDevCpeServiceFlowEnable = _GemtekDevCpeServiceFlowEnable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 11, 1, 1, 8),
    _GemtekDevCpeServiceFlowEnable_Type()
)
gemtekDevCpeServiceFlowEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeServiceFlowEnable.setStatus("current")


class _GemtekDevCpeServiceFlowScheduling_Type(Integer32):
    """Custom type gemtekDevCpeServiceFlowScheduling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("bestEffort", 2),
          ("ertps", 5),
          ("nrtps", 3),
          ("rtps", 4),
          ("ugs", 6))
    )


_GemtekDevCpeServiceFlowScheduling_Type.__name__ = "Integer32"
_GemtekDevCpeServiceFlowScheduling_Object = MibTableColumn
gemtekDevCpeServiceFlowScheduling = _GemtekDevCpeServiceFlowScheduling_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 11, 1, 1, 9),
    _GemtekDevCpeServiceFlowScheduling_Type()
)
gemtekDevCpeServiceFlowScheduling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeServiceFlowScheduling.setStatus("current")
_GemtekDevCpeServiceFlowMaxRate_Type = Unsigned32
_GemtekDevCpeServiceFlowMaxRate_Object = MibTableColumn
gemtekDevCpeServiceFlowMaxRate = _GemtekDevCpeServiceFlowMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 11, 1, 1, 10),
    _GemtekDevCpeServiceFlowMaxRate_Type()
)
gemtekDevCpeServiceFlowMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeServiceFlowMaxRate.setStatus("current")


class _GemtekDevCpeServiceFlowARQ_Type(Integer32):
    """Custom type gemtekDevCpeServiceFlowARQ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_GemtekDevCpeServiceFlowARQ_Type.__name__ = "Integer32"
_GemtekDevCpeServiceFlowARQ_Object = MibTableColumn
gemtekDevCpeServiceFlowARQ = _GemtekDevCpeServiceFlowARQ_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 11, 1, 1, 11),
    _GemtekDevCpeServiceFlowARQ_Type()
)
gemtekDevCpeServiceFlowARQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeServiceFlowARQ.setStatus("current")


class _GemtekDevCpeServiceFlowHARQ_Type(Integer32):
    """Custom type gemtekDevCpeServiceFlowHARQ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_GemtekDevCpeServiceFlowHARQ_Type.__name__ = "Integer32"
_GemtekDevCpeServiceFlowHARQ_Object = MibTableColumn
gemtekDevCpeServiceFlowHARQ = _GemtekDevCpeServiceFlowHARQ_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 11, 1, 1, 12),
    _GemtekDevCpeServiceFlowHARQ_Type()
)
gemtekDevCpeServiceFlowHARQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeServiceFlowHARQ.setStatus("current")
_GemtekDevCpeServiceFlowRules_Type = Unsigned32
_GemtekDevCpeServiceFlowRules_Object = MibTableColumn
gemtekDevCpeServiceFlowRules = _GemtekDevCpeServiceFlowRules_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 11, 1, 1, 13),
    _GemtekDevCpeServiceFlowRules_Type()
)
gemtekDevCpeServiceFlowRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeServiceFlowRules.setStatus("current")
_GemtekDevCpeSyslog_ObjectIdentity = ObjectIdentity
gemtekDevCpeSyslog = _GemtekDevCpeSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 12)
)


class _GemtekDevCpeSyslogEnable_Type(Integer32):
    """Custom type gemtekDevCpeSyslogEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GemtekDevCpeSyslogEnable_Type.__name__ = "Integer32"
_GemtekDevCpeSyslogEnable_Object = MibScalar
gemtekDevCpeSyslogEnable = _GemtekDevCpeSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 12, 1),
    _GemtekDevCpeSyslogEnable_Type()
)
gemtekDevCpeSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeSyslogEnable.setStatus("current")
_GemtekDevCpeSyslogServerIp_Type = IpAddress
_GemtekDevCpeSyslogServerIp_Object = MibScalar
gemtekDevCpeSyslogServerIp = _GemtekDevCpeSyslogServerIp_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 12, 2),
    _GemtekDevCpeSyslogServerIp_Type()
)
gemtekDevCpeSyslogServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeSyslogServerIp.setStatus("current")
_GemtekDevCpeSyslogServerPort_Type = Integer32
_GemtekDevCpeSyslogServerPort_Object = MibScalar
gemtekDevCpeSyslogServerPort = _GemtekDevCpeSyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 12, 3),
    _GemtekDevCpeSyslogServerPort_Type()
)
gemtekDevCpeSyslogServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gemtekDevCpeSyslogServerPort.setStatus("current")
_GemtekDevCpeMaxTxPower_ObjectIdentity = ObjectIdentity
gemtekDevCpeMaxTxPower = _GemtekDevCpeMaxTxPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 13)
)


class _GemtekDevCpeMaxTxPowerModeSelection_Type(Integer32):
    """Custom type gemtekDevCpeMaxTxPowerModeSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eirp", 1),
          ("rf", 0))
    )


_GemtekDevCpeMaxTxPowerModeSelection_Type.__name__ = "Integer32"
_GemtekDevCpeMaxTxPowerModeSelection_Object = MibScalar
gemtekDevCpeMaxTxPowerModeSelection = _GemtekDevCpeMaxTxPowerModeSelection_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 13, 1),
    _GemtekDevCpeMaxTxPowerModeSelection_Type()
)
gemtekDevCpeMaxTxPowerModeSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeMaxTxPowerModeSelection.setStatus("obsolete")
_GemtekDevCpeMaxTxPowerRfMode_ObjectIdentity = ObjectIdentity
gemtekDevCpeMaxTxPowerRfMode = _GemtekDevCpeMaxTxPowerRfMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 13, 2)
)
_GemtekDevCpeRfModeBPSK_Type = Unsigned32
_GemtekDevCpeRfModeBPSK_Object = MibScalar
gemtekDevCpeRfModeBPSK = _GemtekDevCpeRfModeBPSK_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 13, 2, 1),
    _GemtekDevCpeRfModeBPSK_Type()
)
gemtekDevCpeRfModeBPSK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeRfModeBPSK.setStatus("obsolete")
_GemtekDevCpeRfModeQPSK_Type = Unsigned32
_GemtekDevCpeRfModeQPSK_Object = MibScalar
gemtekDevCpeRfModeQPSK = _GemtekDevCpeRfModeQPSK_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 13, 2, 2),
    _GemtekDevCpeRfModeQPSK_Type()
)
gemtekDevCpeRfModeQPSK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeRfModeQPSK.setStatus("obsolete")
_GemtekDevCpeRfModeQAM16_Type = Unsigned32
_GemtekDevCpeRfModeQAM16_Object = MibScalar
gemtekDevCpeRfModeQAM16 = _GemtekDevCpeRfModeQAM16_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 13, 2, 3),
    _GemtekDevCpeRfModeQAM16_Type()
)
gemtekDevCpeRfModeQAM16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeRfModeQAM16.setStatus("obsolete")
_GemtekDevCpeRfModeQAM64_Type = Unsigned32
_GemtekDevCpeRfModeQAM64_Object = MibScalar
gemtekDevCpeRfModeQAM64 = _GemtekDevCpeRfModeQAM64_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 13, 2, 4),
    _GemtekDevCpeRfModeQAM64_Type()
)
gemtekDevCpeRfModeQAM64.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeRfModeQAM64.setStatus("obsolete")
_GemtekDevCpeMaxTxPowerEirpMode_ObjectIdentity = ObjectIdentity
gemtekDevCpeMaxTxPowerEirpMode = _GemtekDevCpeMaxTxPowerEirpMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 13, 3)
)
_GemtekDevCpeEirpModeAntennaGain_Type = Unsigned32
_GemtekDevCpeEirpModeAntennaGain_Object = MibScalar
gemtekDevCpeEirpModeAntennaGain = _GemtekDevCpeEirpModeAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 13, 3, 1),
    _GemtekDevCpeEirpModeAntennaGain_Type()
)
gemtekDevCpeEirpModeAntennaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeEirpModeAntennaGain.setStatus("obsolete")
_GemtekDevCpeEirpModeBPSK_Type = Unsigned32
_GemtekDevCpeEirpModeBPSK_Object = MibScalar
gemtekDevCpeEirpModeBPSK = _GemtekDevCpeEirpModeBPSK_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 13, 3, 2),
    _GemtekDevCpeEirpModeBPSK_Type()
)
gemtekDevCpeEirpModeBPSK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeEirpModeBPSK.setStatus("obsolete")
_GemtekDevCpeEirpModeQPSK_Type = Unsigned32
_GemtekDevCpeEirpModeQPSK_Object = MibScalar
gemtekDevCpeEirpModeQPSK = _GemtekDevCpeEirpModeQPSK_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 13, 3, 3),
    _GemtekDevCpeEirpModeQPSK_Type()
)
gemtekDevCpeEirpModeQPSK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeEirpModeQPSK.setStatus("obsolete")
_GemtekDevCpeEirpModeQAM16_Type = Unsigned32
_GemtekDevCpeEirpModeQAM16_Object = MibScalar
gemtekDevCpeEirpModeQAM16 = _GemtekDevCpeEirpModeQAM16_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 13, 3, 4),
    _GemtekDevCpeEirpModeQAM16_Type()
)
gemtekDevCpeEirpModeQAM16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeEirpModeQAM16.setStatus("obsolete")
_GemtekDevCpeEirpModeQAM64_Type = Unsigned32
_GemtekDevCpeEirpModeQAM64_Object = MibScalar
gemtekDevCpeEirpModeQAM64 = _GemtekDevCpeEirpModeQAM64_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 13, 3, 5),
    _GemtekDevCpeEirpModeQAM64_Type()
)
gemtekDevCpeEirpModeQAM64.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeEirpModeQAM64.setStatus("obsolete")
_GemtekDevCpePullFtpUpgrade_ObjectIdentity = ObjectIdentity
gemtekDevCpePullFtpUpgrade = _GemtekDevCpePullFtpUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 21)
)
_GemtekDevCpePullFtpServerIP_Type = IpAddress
_GemtekDevCpePullFtpServerIP_Object = MibScalar
gemtekDevCpePullFtpServerIP = _GemtekDevCpePullFtpServerIP_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 21, 1),
    _GemtekDevCpePullFtpServerIP_Type()
)
gemtekDevCpePullFtpServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpePullFtpServerIP.setStatus("current")


class _GemtekDevCpePullFtpServerUserName_Type(OctetString):
    """Custom type gemtekDevCpePullFtpServerUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GemtekDevCpePullFtpServerUserName_Type.__name__ = "OctetString"
_GemtekDevCpePullFtpServerUserName_Object = MibScalar
gemtekDevCpePullFtpServerUserName = _GemtekDevCpePullFtpServerUserName_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 21, 2),
    _GemtekDevCpePullFtpServerUserName_Type()
)
gemtekDevCpePullFtpServerUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpePullFtpServerUserName.setStatus("current")


class _GemtekDevCpePullFtpServerPassword_Type(OctetString):
    """Custom type gemtekDevCpePullFtpServerPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GemtekDevCpePullFtpServerPassword_Type.__name__ = "OctetString"
_GemtekDevCpePullFtpServerPassword_Object = MibScalar
gemtekDevCpePullFtpServerPassword = _GemtekDevCpePullFtpServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 21, 3),
    _GemtekDevCpePullFtpServerPassword_Type()
)
gemtekDevCpePullFtpServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpePullFtpServerPassword.setStatus("current")


class _GemtekDevCpePullFtpFilePath_Type(OctetString):
    """Custom type gemtekDevCpePullFtpFilePath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_GemtekDevCpePullFtpFilePath_Type.__name__ = "OctetString"
_GemtekDevCpePullFtpFilePath_Object = MibScalar
gemtekDevCpePullFtpFilePath = _GemtekDevCpePullFtpFilePath_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 21, 4),
    _GemtekDevCpePullFtpFilePath_Type()
)
gemtekDevCpePullFtpFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpePullFtpFilePath.setStatus("current")


class _GemtekDevCpePullFtpFileName_Type(OctetString):
    """Custom type gemtekDevCpePullFtpFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GemtekDevCpePullFtpFileName_Type.__name__ = "OctetString"
_GemtekDevCpePullFtpFileName_Object = MibScalar
gemtekDevCpePullFtpFileName = _GemtekDevCpePullFtpFileName_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 21, 5),
    _GemtekDevCpePullFtpFileName_Type()
)
gemtekDevCpePullFtpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpePullFtpFileName.setStatus("current")


class _GemtekDevCpePullFtpUpgradeCmd_Type(Integer32):
    """Custom type gemtekDevCpePullFtpUpgradeCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("downloadAndUpgrade", 1),
          ("rollback", 2))
    )


_GemtekDevCpePullFtpUpgradeCmd_Type.__name__ = "Integer32"
_GemtekDevCpePullFtpUpgradeCmd_Object = MibScalar
gemtekDevCpePullFtpUpgradeCmd = _GemtekDevCpePullFtpUpgradeCmd_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 21, 6),
    _GemtekDevCpePullFtpUpgradeCmd_Type()
)
gemtekDevCpePullFtpUpgradeCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpePullFtpUpgradeCmd.setStatus("current")


class _GemtekDevCpePullFtpUpgradeAdminStatus_Type(Integer32):
    """Custom type gemtekDevCpePullFtpUpgradeAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("downloading", 1),
          ("error", 3),
          ("installing", 2),
          ("ready", 0),
          ("success", 4))
    )


_GemtekDevCpePullFtpUpgradeAdminStatus_Type.__name__ = "Integer32"
_GemtekDevCpePullFtpUpgradeAdminStatus_Object = MibScalar
gemtekDevCpePullFtpUpgradeAdminStatus = _GemtekDevCpePullFtpUpgradeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 21, 7),
    _GemtekDevCpePullFtpUpgradeAdminStatus_Type()
)
gemtekDevCpePullFtpUpgradeAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpePullFtpUpgradeAdminStatus.setStatus("current")
_GemtekDevCpePushFtpUpgrade_ObjectIdentity = ObjectIdentity
gemtekDevCpePushFtpUpgrade = _GemtekDevCpePushFtpUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 22)
)


class _GemtekDevCpeCurrentSwVersion_Type(OctetString):
    """Custom type gemtekDevCpeCurrentSwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GemtekDevCpeCurrentSwVersion_Type.__name__ = "OctetString"
_GemtekDevCpeCurrentSwVersion_Object = MibScalar
gemtekDevCpeCurrentSwVersion = _GemtekDevCpeCurrentSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 22, 1),
    _GemtekDevCpeCurrentSwVersion_Type()
)
gemtekDevCpeCurrentSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeCurrentSwVersion.setStatus("current")


class _GemtekDevCpePreviousSwVersion_Type(OctetString):
    """Custom type gemtekDevCpePreviousSwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GemtekDevCpePreviousSwVersion_Type.__name__ = "OctetString"
_GemtekDevCpePreviousSwVersion_Object = MibScalar
gemtekDevCpePreviousSwVersion = _GemtekDevCpePreviousSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 22, 2),
    _GemtekDevCpePreviousSwVersion_Type()
)
gemtekDevCpePreviousSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpePreviousSwVersion.setStatus("current")


class _GemtekDevCpeDownloadSwVersion_Type(OctetString):
    """Custom type gemtekDevCpeDownloadSwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GemtekDevCpeDownloadSwVersion_Type.__name__ = "OctetString"
_GemtekDevCpeDownloadSwVersion_Object = MibScalar
gemtekDevCpeDownloadSwVersion = _GemtekDevCpeDownloadSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 22, 3),
    _GemtekDevCpeDownloadSwVersion_Type()
)
gemtekDevCpeDownloadSwVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeDownloadSwVersion.setStatus("current")


class _GemtekDevCpePushFtpUpgradeCmd_Type(Integer32):
    """Custom type gemtekDevCpePushFtpUpgradeCmd based on Integer32"""
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
        *(("default", 0),
          ("download", 1),
          ("rollback", 3),
          ("upgrade", 2))
    )


_GemtekDevCpePushFtpUpgradeCmd_Type.__name__ = "Integer32"
_GemtekDevCpePushFtpUpgradeCmd_Object = MibScalar
gemtekDevCpePushFtpUpgradeCmd = _GemtekDevCpePushFtpUpgradeCmd_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 22, 4),
    _GemtekDevCpePushFtpUpgradeCmd_Type()
)
gemtekDevCpePushFtpUpgradeCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpePushFtpUpgradeCmd.setStatus("current")


class _GemtekDevCpePushFtpUpgradeAdminStatus_Type(Integer32):
    """Custom type gemtekDevCpePushFtpUpgradeAdminStatus based on Integer32"""
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
        *(("error", 2),
          ("installing", 1),
          ("ready", 0),
          ("success", 3))
    )


_GemtekDevCpePushFtpUpgradeAdminStatus_Type.__name__ = "Integer32"
_GemtekDevCpePushFtpUpgradeAdminStatus_Object = MibScalar
gemtekDevCpePushFtpUpgradeAdminStatus = _GemtekDevCpePushFtpUpgradeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 22, 5),
    _GemtekDevCpePushFtpUpgradeAdminStatus_Type()
)
gemtekDevCpePushFtpUpgradeAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpePushFtpUpgradeAdminStatus.setStatus("current")
_GemtekDevCpeTftpUpgrade_ObjectIdentity = ObjectIdentity
gemtekDevCpeTftpUpgrade = _GemtekDevCpeTftpUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10529, 300, 69)
)
_GemtekDevCpeTftpServerIP_Type = IpAddress
_GemtekDevCpeTftpServerIP_Object = MibScalar
gemtekDevCpeTftpServerIP = _GemtekDevCpeTftpServerIP_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 69, 1),
    _GemtekDevCpeTftpServerIP_Type()
)
gemtekDevCpeTftpServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeTftpServerIP.setStatus("current")


class _GemtekDevCpeTftpFileName_Type(OctetString):
    """Custom type gemtekDevCpeTftpFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_GemtekDevCpeTftpFileName_Type.__name__ = "OctetString"
_GemtekDevCpeTftpFileName_Object = MibScalar
gemtekDevCpeTftpFileName = _GemtekDevCpeTftpFileName_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 69, 2),
    _GemtekDevCpeTftpFileName_Type()
)
gemtekDevCpeTftpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeTftpFileName.setStatus("current")


class _GemtekDevCpeTftpUpgradeCmd_Type(Integer32):
    """Custom type gemtekDevCpeTftpUpgradeCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("downloadAndUpgrade", 1))
    )


_GemtekDevCpeTftpUpgradeCmd_Type.__name__ = "Integer32"
_GemtekDevCpeTftpUpgradeCmd_Object = MibScalar
gemtekDevCpeTftpUpgradeCmd = _GemtekDevCpeTftpUpgradeCmd_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 69, 3),
    _GemtekDevCpeTftpUpgradeCmd_Type()
)
gemtekDevCpeTftpUpgradeCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gemtekDevCpeTftpUpgradeCmd.setStatus("current")


class _GemtekDevCpeTftpUpgradeAdminStatus_Type(Integer32):
    """Custom type gemtekDevCpeTftpUpgradeAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("downloading", 1),
          ("error", 3),
          ("installing", 2),
          ("ready", 0),
          ("success", 4))
    )


_GemtekDevCpeTftpUpgradeAdminStatus_Type.__name__ = "Integer32"
_GemtekDevCpeTftpUpgradeAdminStatus_Object = MibScalar
gemtekDevCpeTftpUpgradeAdminStatus = _GemtekDevCpeTftpUpgradeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10529, 300, 69, 4),
    _GemtekDevCpeTftpUpgradeAdminStatus_Type()
)
gemtekDevCpeTftpUpgradeAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemtekDevCpeTftpUpgradeAdminStatus.setStatus("current")

# Managed Objects groups


# Notification objects

coldStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 10529, 300, 3, 2, 1)
)
if mibBuilder.loadTexts:
    coldStart.setStatus(
        "current"
    )

warmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 10529, 300, 3, 2, 2)
)
if mibBuilder.loadTexts:
    warmStart.setStatus(
        "current"
    )

fatalErrorRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 10529, 300, 3, 2, 3)
)
if mibBuilder.loadTexts:
    fatalErrorRestart.setStatus(
        "current"
    )

linkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 10529, 300, 3, 2, 4)
)
linkUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"))
)
if mibBuilder.loadTexts:
    linkUp.setStatus(
        "current"
    )

notTheHightestPriorityAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 10529, 300, 3, 2, 5)
)
if mibBuilder.loadTexts:
    notTheHightestPriorityAP.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Motorola-Cpe-PRIVATE-MIB",
    **{"gemtek": gemtek,
       "gemtekDevCpe": gemtekDevCpe,
       "gemtekDevCpeStatus": gemtekDevCpeStatus,
       "wirelessStatus": wirelessStatus,
       "gemtekDevCpeWimaxRssi": gemtekDevCpeWimaxRssi,
       "gemtekDevCpeWimaxCinr": gemtekDevCpeWimaxCinr,
       "gemtekDevCpeWimaxTxPower": gemtekDevCpeWimaxTxPower,
       "gemtekDevCpeWimaxMaxTxPower": gemtekDevCpeWimaxMaxTxPower,
       "gemtekDevCpeWimaxUpLinkModulation": gemtekDevCpeWimaxUpLinkModulation,
       "gemtekDevCpeWimaxDownLinkModulation": gemtekDevCpeWimaxDownLinkModulation,
       "gemtekDevCpeWimaxBsid": gemtekDevCpeWimaxBsid,
       "gemtekDevCpeWimaxFrequency": gemtekDevCpeWimaxFrequency,
       "gemtekDevCpeWimaxUpLinkDataRate": gemtekDevCpeWimaxUpLinkDataRate,
       "gemtekDevCpeWimaxDownLinkDataRate": gemtekDevCpeWimaxDownLinkDataRate,
       "gemtekDevCpeWimaxTotalUpLinkDataByte": gemtekDevCpeWimaxTotalUpLinkDataByte,
       "gemtekDevCpeWimaxTotalDownLinkDataByte": gemtekDevCpeWimaxTotalDownLinkDataByte,
       "gemtekDevCpeWimaxCpeState": gemtekDevCpeWimaxCpeState,
       "gemtekDevCpeWimaxCinrReuse1": gemtekDevCpeWimaxCinrReuse1,
       "gemtekDevCpeWimaxCinrReuse3": gemtekDevCpeWimaxCinrReuse3,
       "gemtekDevCpeWimaxBandwidth": gemtekDevCpeWimaxBandwidth,
       "gemtekDevCpeWimaxZoneCinrChannelZero": gemtekDevCpeWimaxZoneCinrChannelZero,
       "gemtekDevCpeWimaxMimoMode": gemtekDevCpeWimaxMimoMode,
       "networkStatus": networkStatus,
       "gemtekDevCpeLanMacAddresss": gemtekDevCpeLanMacAddresss,
       "gemtekDevCpeLanTotalDownLinkDataByte": gemtekDevCpeLanTotalDownLinkDataByte,
       "gemtekDevCpeLanTotalUpLinkDataByte": gemtekDevCpeLanTotalUpLinkDataByte,
       "gemtekDevCpeLanTotalDownLinkDataPackets": gemtekDevCpeLanTotalDownLinkDataPackets,
       "gemtekDevCpeLanTotalUpLinkDataPackets": gemtekDevCpeLanTotalUpLinkDataPackets,
       "gemtekDevCpeWanMacAddresss": gemtekDevCpeWanMacAddresss,
       "gemtekDevCpeWanTotalDownLinkDataPackets": gemtekDevCpeWanTotalDownLinkDataPackets,
       "gemtekDevCpeWanTotalUpLinkDataPackets": gemtekDevCpeWanTotalUpLinkDataPackets,
       "deviceStatus": deviceStatus,
       "gemtekDevCpeHardwareModel": gemtekDevCpeHardwareModel,
       "gemtekDevCpeFirmwareVersion": gemtekDevCpeFirmwareVersion,
       "gemtekDevCpeFirmwareCreationDate": gemtekDevCpeFirmwareCreationDate,
       "gemtekDevCpeFrequencyRange": gemtekDevCpeFrequencyRange,
       "gemtekDevCpeSerialNumber": gemtekDevCpeSerialNumber,
       "gemtekDevCpeLatitude": gemtekDevCpeLatitude,
       "gemtekDevCpeLongitude": gemtekDevCpeLongitude,
       "gemtekDevCpeHeight": gemtekDevCpeHeight,
       "gemtekDevCpeMibsVersion": gemtekDevCpeMibsVersion,
       "gemtekDevCpeBootromVersion": gemtekDevCpeBootromVersion,
       "gemtekDevCpeBootromCreationDate": gemtekDevCpeBootromCreationDate,
       "gemtekDevCpeProductVersion": gemtekDevCpeProductVersion,
       "gemtekDevCpeControl": gemtekDevCpeControl,
       "rebootWithResponse": rebootWithResponse,
       "isRebootRequired": isRebootRequired,
       "autoSaveConfig": autoSaveConfig,
       "autoSavePeriod": autoSavePeriod,
       "startStopWimax": startStopWimax,
       "snmpBuzzerConfig": snmpBuzzerConfig,
       "snmpBuzzerDisableDelay": snmpBuzzerDisableDelay,
       "gemtekDevCpeSnmpReadCommunity": gemtekDevCpeSnmpReadCommunity,
       "gemtekDevCpeSnmpSetCommunity": gemtekDevCpeSnmpSetCommunity,
       "gemtekDevCpeRestFactoryDefault": gemtekDevCpeRestFactoryDefault,
       "gemtekDevCpeAutoFirmwareRollback": gemtekDevCpeAutoFirmwareRollback,
       "gemtekDevCpeFirmwareValidationTime": gemtekDevCpeFirmwareValidationTime,
       "gemtekDevCpeFirmwareValidationCount": gemtekDevCpeFirmwareValidationCount,
       "gemtekDevCpeSnmpAccessFromLan": gemtekDevCpeSnmpAccessFromLan,
       "gemtekDevCpeDynamicMaxTxPowerBpsk": gemtekDevCpeDynamicMaxTxPowerBpsk,
       "gemtekDevCpeDynamicMaxTxPowerQpsk": gemtekDevCpeDynamicMaxTxPowerQpsk,
       "gemtekDevCpeDynamicMaxTxPowerQam16": gemtekDevCpeDynamicMaxTxPowerQam16,
       "gemtekDevCpeDynamicMaxTxPowerQam64": gemtekDevCpeDynamicMaxTxPowerQam64,
       "gemtekDevCpeSnmpAccessDomain": gemtekDevCpeSnmpAccessDomain,
       "gemtekDevCpeSnmpAccessDomainEnable": gemtekDevCpeSnmpAccessDomainEnable,
       "gemtekDevCpeSnmpAccessDomainIp": gemtekDevCpeSnmpAccessDomainIp,
       "gemtekDevCpeSnmpAccessDomainNetmask": gemtekDevCpeSnmpAccessDomainNetmask,
       "gemtekDevCpeTrap": gemtekDevCpeTrap,
       "gemtekDevCpeTrapServer": gemtekDevCpeTrapServer,
       "trapServerEnable": trapServerEnable,
       "trapServerIp": trapServerIp,
       "trapServerPort": trapServerPort,
       "trapServerCommunity": trapServerCommunity,
       "gemtekDevCpeTrapPrefix": gemtekDevCpeTrapPrefix,
       "coldStart": coldStart,
       "warmStart": warmStart,
       "fatalErrorRestart": fatalErrorRestart,
       "linkUp": linkUp,
       "notTheHightestPriorityAP": notTheHightestPriorityAP,
       "gemtekDevCpeDate": gemtekDevCpeDate,
       "gemtekDevCpeSystemDate": gemtekDevCpeSystemDate,
       "gemtekDevCpeNtpServerEnable": gemtekDevCpeNtpServerEnable,
       "gemtekDevCpeNtpServer": gemtekDevCpeNtpServer,
       "gemtekDevCpeNtpServerFromDHCP": gemtekDevCpeNtpServerFromDHCP,
       "gemtekDevCpeTimeZone": gemtekDevCpeTimeZone,
       "gemtekDevCpeDaylightSaving": gemtekDevCpeDaylightSaving,
       "gemtekDevCpeAccountManagement": gemtekDevCpeAccountManagement,
       "administratorUsername": administratorUsername,
       "administratorPassword": administratorPassword,
       "administratorEnable": administratorEnable,
       "operatorUsername": operatorUsername,
       "operatorPassword": operatorPassword,
       "operatorEnable": operatorEnable,
       "adminUsername": adminUsername,
       "adminPassword": adminPassword,
       "adminEnable": adminEnable,
       "gemtekDevCpeScanner": gemtekDevCpeScanner,
       "gemtekDevCpeChannelBandwidthRang": gemtekDevCpeChannelBandwidthRang,
       "gemtekDevCpeChannelApplyLoadOrSave": gemtekDevCpeChannelApplyLoadOrSave,
       "gemtekDevCpeChannelTable": gemtekDevCpeChannelTable,
       "gemtekDevCpeChannelEntry": gemtekDevCpeChannelEntry,
       "gemtekDevCpeChannelIndex": gemtekDevCpeChannelIndex,
       "gemtekDevCpeChannelActive": gemtekDevCpeChannelActive,
       "gemtekDevCpeChannelFrequency": gemtekDevCpeChannelFrequency,
       "gemtekDevCpeChannelBandwidth": gemtekDevCpeChannelBandwidth,
       "gemtekDevCpeChannelRssi": gemtekDevCpeChannelRssi,
       "gemtekDevCpeChannelCinr": gemtekDevCpeChannelCinr,
       "gemtekDevCpeChannelEntryEnable": gemtekDevCpeChannelEntryEnable,
       "gemtekDevCpeChannelRowstatus": gemtekDevCpeChannelRowstatus,
       "gemtekDevCpeChannelBsId": gemtekDevCpeChannelBsId,
       "gemtekDevCpeChannelPreambelIndex": gemtekDevCpeChannelPreambelIndex,
       "gemtekDevCpeFrequencyRangeSetting": gemtekDevCpeFrequencyRangeSetting,
       "gemtekDevCpeLockFrequencyRangeMin": gemtekDevCpeLockFrequencyRangeMin,
       "gemtekDevCpeLockFrequencyRangeMax": gemtekDevCpeLockFrequencyRangeMax,
       "gemtekDevCpeLockFrequencyRange": gemtekDevCpeLockFrequencyRange,
       "gemtekDevCpeModelFrequencyRangeMin": gemtekDevCpeModelFrequencyRangeMin,
       "gemtekDevCpeModelFrequencyRangeMax": gemtekDevCpeModelFrequencyRangeMax,
       "gemtekDevCpeAPPreferredList": gemtekDevCpeAPPreferredList,
       "gemtekDevCpeAPPreferredSelectionEnable": gemtekDevCpeAPPreferredSelectionEnable,
       "gemtekDevCpeAPPreferredBsIdListLocked": gemtekDevCpeAPPreferredBsIdListLocked,
       "gemtekDevCpeAPPreferredPriorityOneBsId": gemtekDevCpeAPPreferredPriorityOneBsId,
       "gemtekDevCpeAPPreferredPriorityTwoBsId": gemtekDevCpeAPPreferredPriorityTwoBsId,
       "gemtekDevCpeAPPreferredPriorityThreeBsId": gemtekDevCpeAPPreferredPriorityThreeBsId,
       "gemtekDevCpeAPPreferredPriorityFourBsId": gemtekDevCpeAPPreferredPriorityFourBsId,
       "gemtekDevCpeAuthentication": gemtekDevCpeAuthentication,
       "gemtekDevCpeAuthenticationSelectionPhase1": gemtekDevCpeAuthenticationSelectionPhase1,
       "eapIdentityType": eapIdentityType,
       "eapIdentityUseRealm": eapIdentityUseRealm,
       "eapIdentityString": eapIdentityString,
       "eapRealmString": eapRealmString,
       "eapValidateTheDateDurationOfCaCertificate": eapValidateTheDateDurationOfCaCertificate,
       "eapValidateTheServerCertificate": eapValidateTheServerCertificate,
       "gemtekDevCpeAuthenticationEAPTLS": gemtekDevCpeAuthenticationEAPTLS,
       "eapTlsPrivateKeyPassword": eapTlsPrivateKeyPassword,
       "gemtekDevCpeAuthenticationEAPTTLS": gemtekDevCpeAuthenticationEAPTTLS,
       "eapTtlsPhase2": eapTtlsPhase2,
       "eapTtlsUsername": eapTtlsUsername,
       "eapTtlsPassword": eapTtlsPassword,
       "eapTtlsUseDeviceCertificate": eapTtlsUseDeviceCertificate,
       "eapTtlsPrivateKeyPassword": eapTtlsPrivateKeyPassword,
       "gemtekDevCpeCertificationFileManagement": gemtekDevCpeCertificationFileManagement,
       "gemtekDevCpeCertificateUpload": gemtekDevCpeCertificateUpload,
       "gemtekDevCpeCACertificateFileName": gemtekDevCpeCACertificateFileName,
       "gemtekDevCpeCACertificateFileUpload": gemtekDevCpeCACertificateFileUpload,
       "gemtekDevCpeUserCertificateFileName": gemtekDevCpeUserCertificateFileName,
       "gemtekDevCpeUserCertificateFileUpload": gemtekDevCpeUserCertificateFileUpload,
       "gemtekDevCpeCACertificateFileDelete": gemtekDevCpeCACertificateFileDelete,
       "gemtekDevCpeUserCertificateFileDelete": gemtekDevCpeUserCertificateFileDelete,
       "gemtekDevCpeCACertificateFileTable": gemtekDevCpeCACertificateFileTable,
       "gemtekDevCpeCACertificateFileEntry": gemtekDevCpeCACertificateFileEntry,
       "gemtekDevCpeCACertificateIndex": gemtekDevCpeCACertificateIndex,
       "gemtekDevCpeCACertificateSize": gemtekDevCpeCACertificateSize,
       "gemtekDevCpeCACertificateIssuer": gemtekDevCpeCACertificateIssuer,
       "gemtekDevCpeCAValidityDateBegin": gemtekDevCpeCAValidityDateBegin,
       "gemtekDevCpeCAValidityDateEnd": gemtekDevCpeCAValidityDateEnd,
       "gemtekDevCpeCACertificateSubject": gemtekDevCpeCACertificateSubject,
       "gemtekDevCpeUserCertificateFileTable": gemtekDevCpeUserCertificateFileTable,
       "gemtekDevCpeUserCertificateFileEntry": gemtekDevCpeUserCertificateFileEntry,
       "gemtekDevCpeUserCertificateIndex": gemtekDevCpeUserCertificateIndex,
       "gemtekDevCpeUserCertificateSize": gemtekDevCpeUserCertificateSize,
       "gemtekDevCpeUserCertificateIssuer": gemtekDevCpeUserCertificateIssuer,
       "gemtekDevCpeUserValidityDateBegin": gemtekDevCpeUserValidityDateBegin,
       "gemtekDevCpeUserValidityDateEnd": gemtekDevCpeUserValidityDateEnd,
       "gemtekDevCpeUserCertificateSubject": gemtekDevCpeUserCertificateSubject,
       "gemtekDevCpeNetworkMode": gemtekDevCpeNetworkMode,
       "gemtekDevCpeNetoworkOperatingMode": gemtekDevCpeNetoworkOperatingMode,
       "gemtekDevCpeBridgeMode": gemtekDevCpeBridgeMode,
       "gemtekDevCpeBridgeIpType": gemtekDevCpeBridgeIpType,
       "gemtekDevCpeBridgeIpAddress": gemtekDevCpeBridgeIpAddress,
       "gemtekDevCpeBridgeNetmask": gemtekDevCpeBridgeNetmask,
       "gemtekDevCpeBridgeGateway": gemtekDevCpeBridgeGateway,
       "gemtekDevCpeBridgeDhcpLeaseTime": gemtekDevCpeBridgeDhcpLeaseTime,
       "gemtekDevCpeBridgeDhcpRenewalTime": gemtekDevCpeBridgeDhcpRenewalTime,
       "gemtekDevCpeBridgeDhcpRebindTime": gemtekDevCpeBridgeDhcpRebindTime,
       "gemtekDevCpeMVLAN": gemtekDevCpeMVLAN,
       "gemtekDevCpeMgmtVlan": gemtekDevCpeMgmtVlan,
       "gemtekDevCpeMgmtVlanEnalbe": gemtekDevCpeMgmtVlanEnalbe,
       "gemtekDevCpeMgmtVlanVid": gemtekDevCpeMgmtVlanVid,
       "gemtekDevCpeMgmtVlanVp": gemtekDevCpeMgmtVlanVp,
       "gemtekDevCpeDataVlan": gemtekDevCpeDataVlan,
       "gemtekDevCpeDataVlanEnalbe": gemtekDevCpeDataVlanEnalbe,
       "gemtekDevCpeDataVlanVid": gemtekDevCpeDataVlanVid,
       "gemtekDevCpeAllowPacketType": gemtekDevCpeAllowPacketType,
       "gemtekDevCpeVlanMembershipTable": gemtekDevCpeVlanMembershipTable,
       "gemtekDevCpeVlanMembershipEntry": gemtekDevCpeVlanMembershipEntry,
       "gemtekDevCpeVlanMembershipIndex": gemtekDevCpeVlanMembershipIndex,
       "gemtekDevCpeVlanMembershipVidBegin": gemtekDevCpeVlanMembershipVidBegin,
       "gemtekDevCpeVlanMembershipVidEnd": gemtekDevCpeVlanMembershipVidEnd,
       "gemtekDevCpeVlanMembershipVidRowstatus": gemtekDevCpeVlanMembershipVidRowstatus,
       "gemtekDevCpeDscpToVp": gemtekDevCpeDscpToVp,
       "gemtekDevCpeDscpToVpMapping": gemtekDevCpeDscpToVpMapping,
       "gemtekDevCpePktCounter": gemtekDevCpePktCounter,
       "gemtekDevCpeTaggedPkts": gemtekDevCpeTaggedPkts,
       "gemtekDevCpeTaggedPktsReset": gemtekDevCpeTaggedPktsReset,
       "gemtekDevCpeUntaggedPkts": gemtekDevCpeUntaggedPkts,
       "gemtekDevCpeUntaggedPktsReset": gemtekDevCpeUntaggedPktsReset,
       "gemtekDevCpeNonmemberPkts": gemtekDevCpeNonmemberPkts,
       "gemtekDevCpeNonmemberPktsReset": gemtekDevCpeNonmemberPktsReset,
       "gemtekDevCpeNatMode": gemtekDevCpeNatMode,
       "gemtekDevCpeNatWanIpType": gemtekDevCpeNatWanIpType,
       "gemtekDevCpeNatWanIpAddress": gemtekDevCpeNatWanIpAddress,
       "gemtekDevCpeNatWanNetmask": gemtekDevCpeNatWanNetmask,
       "gemtekDevCpeNatWanGateway": gemtekDevCpeNatWanGateway,
       "gemtekDevCpeNatLanIpType": gemtekDevCpeNatLanIpType,
       "gemtekDevCpeNatLanIpAddress": gemtekDevCpeNatLanIpAddress,
       "gemtekDevCpeNatLanNetmask": gemtekDevCpeNatLanNetmask,
       "gemtekDevCpeNatMtu": gemtekDevCpeNatMtu,
       "gemtekDevCpeDhcpServer": gemtekDevCpeDhcpServer,
       "gemtekDevCpeDhcpServerEnable": gemtekDevCpeDhcpServerEnable,
       "gemtekDevCpeDhcpServerStartIp": gemtekDevCpeDhcpServerStartIp,
       "gemtekDevCpeDhcpServerEndIp": gemtekDevCpeDhcpServerEndIp,
       "gemtekDevCpeDhcpServerPrimaryDnsIp": gemtekDevCpeDhcpServerPrimaryDnsIp,
       "gemtekDevCpeDhcpServerPrimaryDnsFromIsp": gemtekDevCpeDhcpServerPrimaryDnsFromIsp,
       "gemtekDevCpeDhcpServerSecondDnsIp": gemtekDevCpeDhcpServerSecondDnsIp,
       "gemtekDevCpeDhcpServerSecondDnsFromIsp": gemtekDevCpeDhcpServerSecondDnsFromIsp,
       "gemtekDevCpeDhcpServerTertiaryDnsIp": gemtekDevCpeDhcpServerTertiaryDnsIp,
       "gemtekDevCpeDhcpServerTertiaryDnsFromIsp": gemtekDevCpeDhcpServerTertiaryDnsFromIsp,
       "gemtekDevCpeDhcpServerDomainName": gemtekDevCpeDhcpServerDomainName,
       "gemtekDevCpeDhcpServerMaxLeaseTime": gemtekDevCpeDhcpServerMaxLeaseTime,
       "gemtekDevCpeDhcpServerPermanentHostTable": gemtekDevCpeDhcpServerPermanentHostTable,
       "gemtekDevCpeDhcpServerPermanentHostEntry": gemtekDevCpeDhcpServerPermanentHostEntry,
       "gemtekDevCpeDhcpServerPermanentHostIndex": gemtekDevCpeDhcpServerPermanentHostIndex,
       "gemtekDevCpeDhcpServerPermanentHostMac": gemtekDevCpeDhcpServerPermanentHostMac,
       "gemtekDevCpeDhcpServerPermanentHostIp": gemtekDevCpeDhcpServerPermanentHostIp,
       "gemtekDevCpeDhcpServerPermanentHostEntryEnable": gemtekDevCpeDhcpServerPermanentHostEntryEnable,
       "gemtekDevCpeDhcpServerPermanentRowstatus": gemtekDevCpeDhcpServerPermanentRowstatus,
       "gemtekDevCpePortForwarding": gemtekDevCpePortForwarding,
       "gemtekDevCpePortForwardingTable": gemtekDevCpePortForwardingTable,
       "gemtekDevCpePortForwardingEntry": gemtekDevCpePortForwardingEntry,
       "gemtekDevCpePortForwardingIndex": gemtekDevCpePortForwardingIndex,
       "gemtekDevCpePortForwardingWanPortBegin": gemtekDevCpePortForwardingWanPortBegin,
       "gemtekDevCpePortForwardingWanPortEnd": gemtekDevCpePortForwardingWanPortEnd,
       "gemtekDevCpePortForwardingLanIp": gemtekDevCpePortForwardingLanIp,
       "gemtekDevCpePortForwardingLanPortBegin": gemtekDevCpePortForwardingLanPortBegin,
       "gemtekDevCpePortForwardingLanPortEnd": gemtekDevCpePortForwardingLanPortEnd,
       "gemtekDevCpePortForwardingProtocol": gemtekDevCpePortForwardingProtocol,
       "gemtekDevCpePortForwardingEntryEnable": gemtekDevCpePortForwardingEntryEnable,
       "gemtekDevCpePortForwardingRowstatus": gemtekDevCpePortForwardingRowstatus,
       "gemtekDevCpePortTrigger": gemtekDevCpePortTrigger,
       "gemtekDevCpePortTriggerTable": gemtekDevCpePortTriggerTable,
       "gemtekDevCpePortTriggerEntry": gemtekDevCpePortTriggerEntry,
       "gemtekDevCpePortTriggerIndex": gemtekDevCpePortTriggerIndex,
       "gemtekDevCpePortTriggerName": gemtekDevCpePortTriggerName,
       "gemtekDevCpePortTriggerTriggerPortBegin": gemtekDevCpePortTriggerTriggerPortBegin,
       "gemtekDevCpePortTriggerTriggerPortEnd": gemtekDevCpePortTriggerTriggerPortEnd,
       "gemtekDevCpePortTriggerForwardingPortBegin": gemtekDevCpePortTriggerForwardingPortBegin,
       "gemtekDevCpePortTriggerForwardingPortEnd": gemtekDevCpePortTriggerForwardingPortEnd,
       "gemtekDevCpePortTriggerProtocol": gemtekDevCpePortTriggerProtocol,
       "gemtekDevCpePortTriggerEntryEnable": gemtekDevCpePortTriggerEntryEnable,
       "gemtekDevCpePortTriggerRowstatus": gemtekDevCpePortTriggerRowstatus,
       "gemtekDevCpeDhcpClientList": gemtekDevCpeDhcpClientList,
       "gemtekDevCpeDhcpClentListTable": gemtekDevCpeDhcpClentListTable,
       "gemtekDevCpeDhcpClentListEntry": gemtekDevCpeDhcpClentListEntry,
       "gemtekDevCpeDhcpClentListIndex": gemtekDevCpeDhcpClentListIndex,
       "gemtekDevCpeDhcpClentListIp": gemtekDevCpeDhcpClentListIp,
       "gemtekDevCpeDhcpClentListMacAddress": gemtekDevCpeDhcpClentListMacAddress,
       "gemtekDevCpeDhcpClentListExpireTime": gemtekDevCpeDhcpClentListExpireTime,
       "gemtekDevCpeDscpConfiguration": gemtekDevCpeDscpConfiguration,
       "gemtekDevCpeMgmtDscpId": gemtekDevCpeMgmtDscpId,
       "gemtekDevCpeDropDataPacket": gemtekDevCpeDropDataPacket,
       "gemtekDevCpeNatWanDhcpLeaseTime": gemtekDevCpeNatWanDhcpLeaseTime,
       "gemtekDevCpeNatWanDhcpRenewalTime": gemtekDevCpeNatWanDhcpRenewalTime,
       "gemtekDevCpeNatWanDhcpRebindTime": gemtekDevCpeNatWanDhcpRebindTime,
       "gemtekDevCpeNatModeVLAN": gemtekDevCpeNatModeVLAN,
       "gemtekDevCpeNatModeMgmtVlan": gemtekDevCpeNatModeMgmtVlan,
       "gemtekDevCpeNatModeMgmtVlanEnalbe": gemtekDevCpeNatModeMgmtVlanEnalbe,
       "gemtekDevCpeNatModeMgmtVlanVid": gemtekDevCpeNatModeMgmtVlanVid,
       "gemtekDevCpeNatModeMgmtVlanVp": gemtekDevCpeNatModeMgmtVlanVp,
       "gemtekDevCpeNatModeDataVlan": gemtekDevCpeNatModeDataVlan,
       "gemtekDevCpeNatModeDataVlanEnalbe": gemtekDevCpeNatModeDataVlanEnalbe,
       "gemtekDevCpeNatModeDataVlanVid": gemtekDevCpeNatModeDataVlanVid,
       "gemtekDevCpeNatModeDataVlanVp": gemtekDevCpeNatModeDataVlanVp,
       "gemtekDevCpeFirewall": gemtekDevCpeFirewall,
       "gemtekDevCpeAllowWebAccessingFromWan": gemtekDevCpeAllowWebAccessingFromWan,
       "gemtekDevCpeAllowTelnetAccessingFromWan": gemtekDevCpeAllowTelnetAccessingFromWan,
       "gemtekDevCpeDmzEnable": gemtekDevCpeDmzEnable,
       "gemtekDevCpeDmzIpAddress": gemtekDevCpeDmzIpAddress,
       "gemtekDevCpeRedirectIcmpToTheDmzHostEnable": gemtekDevCpeRedirectIcmpToTheDmzHostEnable,
       "gemtekDevCpeFirewallEnable": gemtekDevCpeFirewallEnable,
       "gemtekDevCpeFirewallTable": gemtekDevCpeFirewallTable,
       "gemtekDevCpeFirewallEntry": gemtekDevCpeFirewallEntry,
       "gemtekDevCpeFirewallIndex": gemtekDevCpeFirewallIndex,
       "gemtekDevCpeFirewallName": gemtekDevCpeFirewallName,
       "gemtekDevCpeFirewallAction": gemtekDevCpeFirewallAction,
       "gemtekDevCpeFirewallInterface": gemtekDevCpeFirewallInterface,
       "gemtekDevCpeFirewallProtocol": gemtekDevCpeFirewallProtocol,
       "gemtekDevCpeFirewallPriority": gemtekDevCpeFirewallPriority,
       "gemtekDevCpeFirewallEntryEnable": gemtekDevCpeFirewallEntryEnable,
       "gemtekDevCpeFirewallSrcMac": gemtekDevCpeFirewallSrcMac,
       "gemtekDevCpeFirewallDstMac": gemtekDevCpeFirewallDstMac,
       "gemtekDevCpeFirewallSrcIpAddress": gemtekDevCpeFirewallSrcIpAddress,
       "gemtekDevCpeFirewallDstIpAddress": gemtekDevCpeFirewallDstIpAddress,
       "gemtekDevCpeFirewallSrcPortRangeBegin": gemtekDevCpeFirewallSrcPortRangeBegin,
       "gemtekDevCpeFirewallSrcPortRangeEnd": gemtekDevCpeFirewallSrcPortRangeEnd,
       "gemtekDevCpeFirewallDstPortRangeBegin": gemtekDevCpeFirewallDstPortRangeBegin,
       "gemtekDevCpeFirewallDstPortRangeEnd": gemtekDevCpeFirewallDstPortRangeEnd,
       "gemtekDevCpeFirewallRowstatus": gemtekDevCpeFirewallRowstatus,
       "gemtekDevCpeTelnetEnable": gemtekDevCpeTelnetEnable,
       "gemtekDevCpeFirewallEtherTypeFilterOneEnable": gemtekDevCpeFirewallEtherTypeFilterOneEnable,
       "gemtekDevCpeFirewallEtherTypeFilterOneTypeDeny": gemtekDevCpeFirewallEtherTypeFilterOneTypeDeny,
       "gemtekDevCpeFirewallEtherTypeFilterTwoEnable": gemtekDevCpeFirewallEtherTypeFilterTwoEnable,
       "gemtekDevCpeFirewallEtherTypeFilterTwoTypeDeny": gemtekDevCpeFirewallEtherTypeFilterTwoTypeDeny,
       "gemtekDevCpeFirewallEtherTypeFilterThreeEnable": gemtekDevCpeFirewallEtherTypeFilterThreeEnable,
       "gemtekDevCpeFirewallEtherTypeFilterThreeTypeDeny": gemtekDevCpeFirewallEtherTypeFilterThreeTypeDeny,
       "gemtekDevCpeFirewallEtherTypeFilterFourEnable": gemtekDevCpeFirewallEtherTypeFilterFourEnable,
       "gemtekDevCpeFirewallEtherTypeFilterFourTypeDeny": gemtekDevCpeFirewallEtherTypeFilterFourTypeDeny,
       "gemtekDevCpeFirewallEtherTypeFilterFiveEnable": gemtekDevCpeFirewallEtherTypeFilterFiveEnable,
       "gemtekDevCpeFirewallEtherTypeFilterFiveTypeDeny": gemtekDevCpeFirewallEtherTypeFilterFiveTypeDeny,
       "gemtekDevCpeFirewallPPPoEEnable": gemtekDevCpeFirewallPPPoEEnable,
       "gemtekDevCpeServiceFlow": gemtekDevCpeServiceFlow,
       "gemtekDevCpeServiceFlowTable": gemtekDevCpeServiceFlowTable,
       "gemtekDevCpeServiceFlowEntry": gemtekDevCpeServiceFlowEntry,
       "gemtekDevCpeServiceFlowIndex": gemtekDevCpeServiceFlowIndex,
       "gemtekDevCpeServiceFlowSFID": gemtekDevCpeServiceFlowSFID,
       "gemtekDevCpeServiceFlowCID": gemtekDevCpeServiceFlowCID,
       "gemtekDevCpeServiceFlowBCID": gemtekDevCpeServiceFlowBCID,
       "gemtekDevCpeServiceFlowType": gemtekDevCpeServiceFlowType,
       "gemtekDevCpeServiceFlowState": gemtekDevCpeServiceFlowState,
       "gemtekDevCpeServiceFlowDirection": gemtekDevCpeServiceFlowDirection,
       "gemtekDevCpeServiceFlowEnable": gemtekDevCpeServiceFlowEnable,
       "gemtekDevCpeServiceFlowScheduling": gemtekDevCpeServiceFlowScheduling,
       "gemtekDevCpeServiceFlowMaxRate": gemtekDevCpeServiceFlowMaxRate,
       "gemtekDevCpeServiceFlowARQ": gemtekDevCpeServiceFlowARQ,
       "gemtekDevCpeServiceFlowHARQ": gemtekDevCpeServiceFlowHARQ,
       "gemtekDevCpeServiceFlowRules": gemtekDevCpeServiceFlowRules,
       "gemtekDevCpeSyslog": gemtekDevCpeSyslog,
       "gemtekDevCpeSyslogEnable": gemtekDevCpeSyslogEnable,
       "gemtekDevCpeSyslogServerIp": gemtekDevCpeSyslogServerIp,
       "gemtekDevCpeSyslogServerPort": gemtekDevCpeSyslogServerPort,
       "gemtekDevCpeMaxTxPower": gemtekDevCpeMaxTxPower,
       "gemtekDevCpeMaxTxPowerModeSelection": gemtekDevCpeMaxTxPowerModeSelection,
       "gemtekDevCpeMaxTxPowerRfMode": gemtekDevCpeMaxTxPowerRfMode,
       "gemtekDevCpeRfModeBPSK": gemtekDevCpeRfModeBPSK,
       "gemtekDevCpeRfModeQPSK": gemtekDevCpeRfModeQPSK,
       "gemtekDevCpeRfModeQAM16": gemtekDevCpeRfModeQAM16,
       "gemtekDevCpeRfModeQAM64": gemtekDevCpeRfModeQAM64,
       "gemtekDevCpeMaxTxPowerEirpMode": gemtekDevCpeMaxTxPowerEirpMode,
       "gemtekDevCpeEirpModeAntennaGain": gemtekDevCpeEirpModeAntennaGain,
       "gemtekDevCpeEirpModeBPSK": gemtekDevCpeEirpModeBPSK,
       "gemtekDevCpeEirpModeQPSK": gemtekDevCpeEirpModeQPSK,
       "gemtekDevCpeEirpModeQAM16": gemtekDevCpeEirpModeQAM16,
       "gemtekDevCpeEirpModeQAM64": gemtekDevCpeEirpModeQAM64,
       "gemtekDevCpePullFtpUpgrade": gemtekDevCpePullFtpUpgrade,
       "gemtekDevCpePullFtpServerIP": gemtekDevCpePullFtpServerIP,
       "gemtekDevCpePullFtpServerUserName": gemtekDevCpePullFtpServerUserName,
       "gemtekDevCpePullFtpServerPassword": gemtekDevCpePullFtpServerPassword,
       "gemtekDevCpePullFtpFilePath": gemtekDevCpePullFtpFilePath,
       "gemtekDevCpePullFtpFileName": gemtekDevCpePullFtpFileName,
       "gemtekDevCpePullFtpUpgradeCmd": gemtekDevCpePullFtpUpgradeCmd,
       "gemtekDevCpePullFtpUpgradeAdminStatus": gemtekDevCpePullFtpUpgradeAdminStatus,
       "gemtekDevCpePushFtpUpgrade": gemtekDevCpePushFtpUpgrade,
       "gemtekDevCpeCurrentSwVersion": gemtekDevCpeCurrentSwVersion,
       "gemtekDevCpePreviousSwVersion": gemtekDevCpePreviousSwVersion,
       "gemtekDevCpeDownloadSwVersion": gemtekDevCpeDownloadSwVersion,
       "gemtekDevCpePushFtpUpgradeCmd": gemtekDevCpePushFtpUpgradeCmd,
       "gemtekDevCpePushFtpUpgradeAdminStatus": gemtekDevCpePushFtpUpgradeAdminStatus,
       "gemtekDevCpeTftpUpgrade": gemtekDevCpeTftpUpgrade,
       "gemtekDevCpeTftpServerIP": gemtekDevCpeTftpServerIP,
       "gemtekDevCpeTftpFileName": gemtekDevCpeTftpFileName,
       "gemtekDevCpeTftpUpgradeCmd": gemtekDevCpeTftpUpgradeCmd,
       "gemtekDevCpeTftpUpgradeAdminStatus": gemtekDevCpeTftpUpgradeAdminStatus}
)
