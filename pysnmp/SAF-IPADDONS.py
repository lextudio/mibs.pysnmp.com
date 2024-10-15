# SNMP MIB module (SAF-IPADDONS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SAF-IPADDONS
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:18 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Saf_ObjectIdentity = ObjectIdentity
saf = _Saf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571)
)
_Tehnika_ObjectIdentity = ObjectIdentity
tehnika = _Tehnika_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100)
)
_MicrowaveRadio_ObjectIdentity = ObjectIdentity
microwaveRadio = _MicrowaveRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1)
)
_PointToPoint_ObjectIdentity = ObjectIdentity
pointToPoint = _PointToPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1)
)
_Safip_ObjectIdentity = ObjectIdentity
safip = _Safip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5)
)
_Safipaddons_ObjectIdentity = ObjectIdentity
safipaddons = _Safipaddons_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15)
)
_IpaddSys_ObjectIdentity = ObjectIdentity
ipaddSys = _IpaddSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 1)
)
_ModemTemperature_Type = DisplayString
_ModemTemperature_Object = MibScalar
modemTemperature = _ModemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 1, 1),
    _ModemTemperature_Type()
)
modemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemTemperature.setStatus("mandatory")
_IduInputVoltage_Type = DisplayString
_IduInputVoltage_Object = MibScalar
iduInputVoltage = _IduInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 1, 2),
    _IduInputVoltage_Type()
)
iduInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iduInputVoltage.setStatus("mandatory")
_IduInputCurrent_Type = DisplayString
_IduInputCurrent_Object = MibScalar
iduInputCurrent = _IduInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 1, 3),
    _IduInputCurrent_Type()
)
iduInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iduInputCurrent.setStatus("mandatory")
_IduPowerConsumption_Type = DisplayString
_IduPowerConsumption_Object = MibScalar
iduPowerConsumption = _IduPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 1, 4),
    _IduPowerConsumption_Type()
)
iduPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iduPowerConsumption.setStatus("mandatory")
_OduTemperature_Type = DisplayString
_OduTemperature_Object = MibScalar
oduTemperature = _OduTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 1, 5),
    _OduTemperature_Type()
)
oduTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduTemperature.setStatus("mandatory")


class _OduPsuState_Type(Integer32):
    """Custom type oduPsuState based on Integer32"""
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
        *(("fault", 7),
          ("idle", 3),
          ("init", 1),
          ("off", 2),
          ("ok", 4),
          ("overload", 5),
          ("short", 6))
    )


_OduPsuState_Type.__name__ = "Integer32"
_OduPsuState_Object = MibScalar
oduPsuState = _OduPsuState_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 1, 6),
    _OduPsuState_Type()
)
oduPsuState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPsuState.setStatus("mandatory")
_IduOutputVoltageToOdu_Type = DisplayString
_IduOutputVoltageToOdu_Object = MibScalar
iduOutputVoltageToOdu = _IduOutputVoltageToOdu_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 1, 7),
    _IduOutputVoltageToOdu_Type()
)
iduOutputVoltageToOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iduOutputVoltageToOdu.setStatus("mandatory")
_IduOutputCurrentToOdu_Type = DisplayString
_IduOutputCurrentToOdu_Object = MibScalar
iduOutputCurrentToOdu = _IduOutputCurrentToOdu_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 1, 8),
    _IduOutputCurrentToOdu_Type()
)
iduOutputCurrentToOdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iduOutputCurrentToOdu.setStatus("mandatory")
_OduPowerConsumption_Type = DisplayString
_OduPowerConsumption_Object = MibScalar
oduPowerConsumption = _OduPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 1, 9),
    _OduPowerConsumption_Type()
)
oduPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPowerConsumption.setStatus("mandatory")
_OduCableAttenuation_Type = Integer32
_OduCableAttenuation_Object = MibScalar
oduCableAttenuation = _OduCableAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 1, 10),
    _OduCableAttenuation_Type()
)
oduCableAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduCableAttenuation.setStatus("mandatory")
_IpaddIfB_ObjectIdentity = ObjectIdentity
ipaddIfB = _IpaddIfB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2)
)
_IpaddIfBTable_Object = MibTable
ipaddIfBTable = _IpaddIfBTable_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2)
)
if mibBuilder.loadTexts:
    ipaddIfBTable.setStatus("current")
_IpaddIfBEntry_Object = MibTableRow
ipaddIfBEntry = _IpaddIfBEntry_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1)
)
ipaddIfBEntry.setIndexNames(
    (0, "SAF-IPADDONS", "ipaddIfBIndex"),
)
if mibBuilder.loadTexts:
    ipaddIfBEntry.setStatus("current")
_IpaddIfBIndex_Type = Integer32
_IpaddIfBIndex_Object = MibTableColumn
ipaddIfBIndex = _IpaddIfBIndex_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 1),
    _IpaddIfBIndex_Type()
)
ipaddIfBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfBIndex.setStatus("mandatory")


class _IpaddIfBduplex_Type(Integer32):
    """Custom type ipaddIfBduplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2))
    )


_IpaddIfBduplex_Type.__name__ = "Integer32"
_IpaddIfBduplex_Object = MibTableColumn
ipaddIfBduplex = _IpaddIfBduplex_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 2),
    _IpaddIfBduplex_Type()
)
ipaddIfBduplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfBduplex.setStatus("mandatory")


class _IpaddIfBRxFlow_Type(Integer32):
    """Custom type ipaddIfBRxFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_IpaddIfBRxFlow_Type.__name__ = "Integer32"
_IpaddIfBRxFlow_Object = MibTableColumn
ipaddIfBRxFlow = _IpaddIfBRxFlow_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 3),
    _IpaddIfBRxFlow_Type()
)
ipaddIfBRxFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfBRxFlow.setStatus("mandatory")


class _IpaddIfBTxFlow_Type(Integer32):
    """Custom type ipaddIfBTxFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_IpaddIfBTxFlow_Type.__name__ = "Integer32"
_IpaddIfBTxFlow_Object = MibTableColumn
ipaddIfBTxFlow = _IpaddIfBTxFlow_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 4),
    _IpaddIfBTxFlow_Type()
)
ipaddIfBTxFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfBTxFlow.setStatus("mandatory")


class _IpaddIfBRxState_Type(Integer32):
    """Custom type ipaddIfBRxState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_IpaddIfBRxState_Type.__name__ = "Integer32"
_IpaddIfBRxState_Object = MibTableColumn
ipaddIfBRxState = _IpaddIfBRxState_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 5),
    _IpaddIfBRxState_Type()
)
ipaddIfBRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfBRxState.setStatus("mandatory")


class _IpaddIfBTxTxState_Type(Integer32):
    """Custom type ipaddIfBTxTxState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_IpaddIfBTxTxState_Type.__name__ = "Integer32"
_IpaddIfBTxTxState_Object = MibTableColumn
ipaddIfBTxTxState = _IpaddIfBTxTxState_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 6),
    _IpaddIfBTxTxState_Type()
)
ipaddIfBTxTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfBTxTxState.setStatus("mandatory")
_IpaddIfBTxQ0PKT_Type = Integer32
_IpaddIfBTxQ0PKT_Object = MibTableColumn
ipaddIfBTxQ0PKT = _IpaddIfBTxQ0PKT_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 7),
    _IpaddIfBTxQ0PKT_Type()
)
ipaddIfBTxQ0PKT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfBTxQ0PKT.setStatus("mandatory")
_IpaddIfBTxCollisions_Type = Integer32
_IpaddIfBTxCollisions_Object = MibTableColumn
ipaddIfBTxCollisions = _IpaddIfBTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 8),
    _IpaddIfBTxCollisions_Type()
)
ipaddIfBTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfBTxCollisions.setStatus("mandatory")
_IpaddIfBTxSingleCollision_Type = Integer32
_IpaddIfBTxSingleCollision_Object = MibTableColumn
ipaddIfBTxSingleCollision = _IpaddIfBTxSingleCollision_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 9),
    _IpaddIfBTxSingleCollision_Type()
)
ipaddIfBTxSingleCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfBTxSingleCollision.setStatus("mandatory")
_IpaddIfBTxMultiCollision_Type = Integer32
_IpaddIfBTxMultiCollision_Object = MibTableColumn
ipaddIfBTxMultiCollision = _IpaddIfBTxMultiCollision_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 10),
    _IpaddIfBTxMultiCollision_Type()
)
ipaddIfBTxMultiCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfBTxMultiCollision.setStatus("mandatory")
_IpaddIfBRxPausePkts_Type = Integer32
_IpaddIfBRxPausePkts_Object = MibTableColumn
ipaddIfBRxPausePkts = _IpaddIfBRxPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 11),
    _IpaddIfBRxPausePkts_Type()
)
ipaddIfBRxPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfBRxPausePkts.setStatus("mandatory")
_IpaddIfBRxFCSErrors_Type = Integer32
_IpaddIfBRxFCSErrors_Object = MibTableColumn
ipaddIfBRxFCSErrors = _IpaddIfBRxFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 12),
    _IpaddIfBRxFCSErrors_Type()
)
ipaddIfBRxFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfBRxFCSErrors.setStatus("mandatory")
_IpaddIfBRxGoodOctets_Type = Integer32
_IpaddIfBRxGoodOctets_Object = MibTableColumn
ipaddIfBRxGoodOctets = _IpaddIfBRxGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 13),
    _IpaddIfBRxGoodOctets_Type()
)
ipaddIfBRxGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfBRxGoodOctets.setStatus("mandatory")
_IpaddIfBRxSAChanges_Type = Integer32
_IpaddIfBRxSAChanges_Object = MibTableColumn
ipaddIfBRxSAChanges = _IpaddIfBRxSAChanges_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 14),
    _IpaddIfBRxSAChanges_Type()
)
ipaddIfBRxSAChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfBRxSAChanges.setStatus("mandatory")
_IpaddIfBRxExcessSizeDisc_Type = Integer32
_IpaddIfBRxExcessSizeDisc_Object = MibTableColumn
ipaddIfBRxExcessSizeDisc = _IpaddIfBRxExcessSizeDisc_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 15),
    _IpaddIfBRxExcessSizeDisc_Type()
)
ipaddIfBRxExcessSizeDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfBRxExcessSizeDisc.setStatus("mandatory")
_IpaddIfBRxSymbolError_Type = Integer32
_IpaddIfBRxSymbolError_Object = MibTableColumn
ipaddIfBRxSymbolError = _IpaddIfBRxSymbolError_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 16),
    _IpaddIfBRxSymbolError_Type()
)
ipaddIfBRxSymbolError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfBRxSymbolError.setStatus("mandatory")
_IpaddIfBRxPkts1523to2047Octets_Type = Integer32
_IpaddIfBRxPkts1523to2047Octets_Object = MibTableColumn
ipaddIfBRxPkts1523to2047Octets = _IpaddIfBRxPkts1523to2047Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 17),
    _IpaddIfBRxPkts1523to2047Octets_Type()
)
ipaddIfBRxPkts1523to2047Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfBRxPkts1523to2047Octets.setStatus("mandatory")
_IpaddIfBRxPkts2048to4095Octets_Type = Integer32
_IpaddIfBRxPkts2048to4095Octets_Object = MibTableColumn
ipaddIfBRxPkts2048to4095Octets = _IpaddIfBRxPkts2048to4095Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 18),
    _IpaddIfBRxPkts2048to4095Octets_Type()
)
ipaddIfBRxPkts2048to4095Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfBRxPkts2048to4095Octets.setStatus("mandatory")
_IpaddIfBRxPkts4096to8191Octets_Type = Integer32
_IpaddIfBRxPkts4096to8191Octets_Object = MibTableColumn
ipaddIfBRxPkts4096to8191Octets = _IpaddIfBRxPkts4096to8191Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 19),
    _IpaddIfBRxPkts4096to8191Octets_Type()
)
ipaddIfBRxPkts4096to8191Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfBRxPkts4096to8191Octets.setStatus("mandatory")
_IpaddIfBRxPkts8192to9728Octets_Type = Integer32
_IpaddIfBRxPkts8192to9728Octets_Object = MibTableColumn
ipaddIfBRxPkts8192to9728Octets = _IpaddIfBRxPkts8192to9728Octets_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 2, 2, 1, 20),
    _IpaddIfBRxPkts8192to9728Octets_Type()
)
ipaddIfBRxPkts8192to9728Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfBRxPkts8192to9728Octets.setStatus("mandatory")
_IpaddIfM_ObjectIdentity = ObjectIdentity
ipaddIfM = _IpaddIfM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3)
)
_IpaddIfMTable_Object = MibTable
ipaddIfMTable = _IpaddIfMTable_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2)
)
if mibBuilder.loadTexts:
    ipaddIfMTable.setStatus("current")
_IpaddIfMEntry_Object = MibTableRow
ipaddIfMEntry = _IpaddIfMEntry_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1)
)
ipaddIfMEntry.setIndexNames(
    (0, "SAF-IPADDONS", "ipaddIfMIndex"),
)
if mibBuilder.loadTexts:
    ipaddIfMEntry.setStatus("current")
_IpaddIfMIndex_Type = Integer32
_IpaddIfMIndex_Object = MibTableColumn
ipaddIfMIndex = _IpaddIfMIndex_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 1),
    _IpaddIfMIndex_Type()
)
ipaddIfMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfMIndex.setStatus("mandatory")


class _IpaddIfMduplex_Type(Integer32):
    """Custom type ipaddIfMduplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2))
    )


_IpaddIfMduplex_Type.__name__ = "Integer32"
_IpaddIfMduplex_Object = MibTableColumn
ipaddIfMduplex = _IpaddIfMduplex_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 2),
    _IpaddIfMduplex_Type()
)
ipaddIfMduplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfMduplex.setStatus("mandatory")


class _IpaddIfMFlowControl_Type(Integer32):
    """Custom type ipaddIfMFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_IpaddIfMFlowControl_Type.__name__ = "Integer32"
_IpaddIfMFlowControl_Object = MibTableColumn
ipaddIfMFlowControl = _IpaddIfMFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 3),
    _IpaddIfMFlowControl_Type()
)
ipaddIfMFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfMFlowControl.setStatus("mandatory")
_IpaddIfMRxLoPriorityByte_Type = Integer32
_IpaddIfMRxLoPriorityByte_Object = MibTableColumn
ipaddIfMRxLoPriorityByte = _IpaddIfMRxLoPriorityByte_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 4),
    _IpaddIfMRxLoPriorityByte_Type()
)
ipaddIfMRxLoPriorityByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfMRxLoPriorityByte.setStatus("mandatory")
_IpaddIfMRxHiPriorityByte_Type = Integer32
_IpaddIfMRxHiPriorityByte_Object = MibTableColumn
ipaddIfMRxHiPriorityByte = _IpaddIfMRxHiPriorityByte_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 5),
    _IpaddIfMRxHiPriorityByte_Type()
)
ipaddIfMRxHiPriorityByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfMRxHiPriorityByte.setStatus("mandatory")
_IpaddIfMRxSymbolError_Type = Integer32
_IpaddIfMRxSymbolError_Object = MibTableColumn
ipaddIfMRxSymbolError = _IpaddIfMRxSymbolError_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 6),
    _IpaddIfMRxSymbolError_Type()
)
ipaddIfMRxSymbolError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfMRxSymbolError.setStatus("mandatory")
_IpaddIfMRxCRCerror_Type = Integer32
_IpaddIfMRxCRCerror_Object = MibTableColumn
ipaddIfMRxCRCerror = _IpaddIfMRxCRCerror_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 7),
    _IpaddIfMRxCRCerror_Type()
)
ipaddIfMRxCRCerror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfMRxCRCerror.setStatus("mandatory")
_IpaddIfMRxControl8808Pkts_Type = Integer32
_IpaddIfMRxControl8808Pkts_Object = MibTableColumn
ipaddIfMRxControl8808Pkts = _IpaddIfMRxControl8808Pkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 8),
    _IpaddIfMRxControl8808Pkts_Type()
)
ipaddIfMRxControl8808Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfMRxControl8808Pkts.setStatus("mandatory")
_IpaddIfMRxPausePkts_Type = Integer32
_IpaddIfMRxPausePkts_Object = MibTableColumn
ipaddIfMRxPausePkts = _IpaddIfMRxPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 9),
    _IpaddIfMRxPausePkts_Type()
)
ipaddIfMRxPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfMRxPausePkts.setStatus("mandatory")
_IpaddIfMTxLoPriorityByte_Type = Integer32
_IpaddIfMTxLoPriorityByte_Object = MibTableColumn
ipaddIfMTxLoPriorityByte = _IpaddIfMTxLoPriorityByte_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 10),
    _IpaddIfMTxLoPriorityByte_Type()
)
ipaddIfMTxLoPriorityByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfMTxLoPriorityByte.setStatus("mandatory")
_IpaddIfMTxHiPriorityByte_Type = Integer32
_IpaddIfMTxHiPriorityByte_Object = MibTableColumn
ipaddIfMTxHiPriorityByte = _IpaddIfMTxHiPriorityByte_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 11),
    _IpaddIfMTxHiPriorityByte_Type()
)
ipaddIfMTxHiPriorityByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfMTxHiPriorityByte.setStatus("mandatory")
_IpaddIfMTxLateCollision_Type = Integer32
_IpaddIfMTxLateCollision_Object = MibTableColumn
ipaddIfMTxLateCollision = _IpaddIfMTxLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 12),
    _IpaddIfMTxLateCollision_Type()
)
ipaddIfMTxLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfMTxLateCollision.setStatus("mandatory")
_IpaddIfMTxPausePkts_Type = Integer32
_IpaddIfMTxPausePkts_Object = MibTableColumn
ipaddIfMTxPausePkts = _IpaddIfMTxPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 13),
    _IpaddIfMTxPausePkts_Type()
)
ipaddIfMTxPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfMTxPausePkts.setStatus("mandatory")
_IpaddIfMTxDeferred_Type = Integer32
_IpaddIfMTxDeferred_Object = MibTableColumn
ipaddIfMTxDeferred = _IpaddIfMTxDeferred_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 14),
    _IpaddIfMTxDeferred_Type()
)
ipaddIfMTxDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfMTxDeferred.setStatus("mandatory")
_IpaddIfMTxTotalCollision_Type = Integer32
_IpaddIfMTxTotalCollision_Object = MibTableColumn
ipaddIfMTxTotalCollision = _IpaddIfMTxTotalCollision_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 15),
    _IpaddIfMTxTotalCollision_Type()
)
ipaddIfMTxTotalCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfMTxTotalCollision.setStatus("mandatory")
_IpaddIfMTxExcessiveCollision_Type = Integer32
_IpaddIfMTxExcessiveCollision_Object = MibTableColumn
ipaddIfMTxExcessiveCollision = _IpaddIfMTxExcessiveCollision_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 16),
    _IpaddIfMTxExcessiveCollision_Type()
)
ipaddIfMTxExcessiveCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfMTxExcessiveCollision.setStatus("mandatory")
_IpaddIfMTxSingleCollision_Type = Integer32
_IpaddIfMTxSingleCollision_Object = MibTableColumn
ipaddIfMTxSingleCollision = _IpaddIfMTxSingleCollision_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 17),
    _IpaddIfMTxSingleCollision_Type()
)
ipaddIfMTxSingleCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfMTxSingleCollision.setStatus("mandatory")
_IpaddIfMTxMultipleCollision_Type = Integer32
_IpaddIfMTxMultipleCollision_Object = MibTableColumn
ipaddIfMTxMultipleCollision = _IpaddIfMTxMultipleCollision_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 5, 15, 3, 2, 1, 18),
    _IpaddIfMTxMultipleCollision_Type()
)
ipaddIfMTxMultipleCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddIfMTxMultipleCollision.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SAF-IPADDONS",
    **{"saf": saf,
       "tehnika": tehnika,
       "microwaveRadio": microwaveRadio,
       "pointToPoint": pointToPoint,
       "safip": safip,
       "safipaddons": safipaddons,
       "ipaddSys": ipaddSys,
       "modemTemperature": modemTemperature,
       "iduInputVoltage": iduInputVoltage,
       "iduInputCurrent": iduInputCurrent,
       "iduPowerConsumption": iduPowerConsumption,
       "oduTemperature": oduTemperature,
       "oduPsuState": oduPsuState,
       "iduOutputVoltageToOdu": iduOutputVoltageToOdu,
       "iduOutputCurrentToOdu": iduOutputCurrentToOdu,
       "oduPowerConsumption": oduPowerConsumption,
       "oduCableAttenuation": oduCableAttenuation,
       "ipaddIfB": ipaddIfB,
       "ipaddIfBTable": ipaddIfBTable,
       "ipaddIfBEntry": ipaddIfBEntry,
       "ipaddIfBIndex": ipaddIfBIndex,
       "ipaddIfBduplex": ipaddIfBduplex,
       "ipaddIfBRxFlow": ipaddIfBRxFlow,
       "ipaddIfBTxFlow": ipaddIfBTxFlow,
       "ipaddIfBRxState": ipaddIfBRxState,
       "ipaddIfBTxTxState": ipaddIfBTxTxState,
       "ipaddIfBTxQ0PKT": ipaddIfBTxQ0PKT,
       "ipaddIfBTxCollisions": ipaddIfBTxCollisions,
       "ipaddIfBTxSingleCollision": ipaddIfBTxSingleCollision,
       "ipaddIfBTxMultiCollision": ipaddIfBTxMultiCollision,
       "ipaddIfBRxPausePkts": ipaddIfBRxPausePkts,
       "ipaddIfBRxFCSErrors": ipaddIfBRxFCSErrors,
       "ipaddIfBRxGoodOctets": ipaddIfBRxGoodOctets,
       "ipaddIfBRxSAChanges": ipaddIfBRxSAChanges,
       "ipaddIfBRxExcessSizeDisc": ipaddIfBRxExcessSizeDisc,
       "ipaddIfBRxSymbolError": ipaddIfBRxSymbolError,
       "ipaddIfBRxPkts1523to2047Octets": ipaddIfBRxPkts1523to2047Octets,
       "ipaddIfBRxPkts2048to4095Octets": ipaddIfBRxPkts2048to4095Octets,
       "ipaddIfBRxPkts4096to8191Octets": ipaddIfBRxPkts4096to8191Octets,
       "ipaddIfBRxPkts8192to9728Octets": ipaddIfBRxPkts8192to9728Octets,
       "ipaddIfM": ipaddIfM,
       "ipaddIfMTable": ipaddIfMTable,
       "ipaddIfMEntry": ipaddIfMEntry,
       "ipaddIfMIndex": ipaddIfMIndex,
       "ipaddIfMduplex": ipaddIfMduplex,
       "ipaddIfMFlowControl": ipaddIfMFlowControl,
       "ipaddIfMRxLoPriorityByte": ipaddIfMRxLoPriorityByte,
       "ipaddIfMRxHiPriorityByte": ipaddIfMRxHiPriorityByte,
       "ipaddIfMRxSymbolError": ipaddIfMRxSymbolError,
       "ipaddIfMRxCRCerror": ipaddIfMRxCRCerror,
       "ipaddIfMRxControl8808Pkts": ipaddIfMRxControl8808Pkts,
       "ipaddIfMRxPausePkts": ipaddIfMRxPausePkts,
       "ipaddIfMTxLoPriorityByte": ipaddIfMTxLoPriorityByte,
       "ipaddIfMTxHiPriorityByte": ipaddIfMTxHiPriorityByte,
       "ipaddIfMTxLateCollision": ipaddIfMTxLateCollision,
       "ipaddIfMTxPausePkts": ipaddIfMTxPausePkts,
       "ipaddIfMTxDeferred": ipaddIfMTxDeferred,
       "ipaddIfMTxTotalCollision": ipaddIfMTxTotalCollision,
       "ipaddIfMTxExcessiveCollision": ipaddIfMTxExcessiveCollision,
       "ipaddIfMTxSingleCollision": ipaddIfMTxSingleCollision,
       "ipaddIfMTxMultipleCollision": ipaddIfMTxMultipleCollision}
)
