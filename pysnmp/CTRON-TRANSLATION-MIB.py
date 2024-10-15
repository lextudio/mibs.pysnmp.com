# SNMP MIB module (CTRON-TRANSLATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-TRANSLATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:49 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

(ctTranslation,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctTranslation")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtTransFddiAtm_ObjectIdentity = ObjectIdentity
ctTransFddiAtm = _CtTransFddiAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 1)
)


class _CtTransFddiAtmMtu_Type(Integer32):
    """Custom type ctTransFddiAtmMtu based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("greater1518MTU", 1),
          ("less1518MTU", 2))
    )


_CtTransFddiAtmMtu_Type.__name__ = "Integer32"
_CtTransFddiAtmMtu_Object = MibScalar
ctTransFddiAtmMtu = _CtTransFddiAtmMtu_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 1, 1),
    _CtTransFddiAtmMtu_Type()
)
ctTransFddiAtmMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransFddiAtmMtu.setStatus("mandatory")


class _CtTransFddiAtmIPFrag_Type(Integer32):
    """Custom type ctTransFddiAtmIPFrag based on Integer32"""
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


_CtTransFddiAtmIPFrag_Type.__name__ = "Integer32"
_CtTransFddiAtmIPFrag_Object = MibScalar
ctTransFddiAtmIPFrag = _CtTransFddiAtmIPFrag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 1, 2),
    _CtTransFddiAtmIPFrag_Type()
)
ctTransFddiAtmIPFrag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransFddiAtmIPFrag.setStatus("mandatory")
_CtTransFddiEthernet_ObjectIdentity = ObjectIdentity
ctTransFddiEthernet = _CtTransFddiEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 2)
)


class _CtTransFddiEthernetIPFrag_Type(Integer32):
    """Custom type ctTransFddiEthernetIPFrag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtTransFddiEthernetIPFrag_Type.__name__ = "Integer32"
_CtTransFddiEthernetIPFrag_Object = MibScalar
ctTransFddiEthernetIPFrag = _CtTransFddiEthernetIPFrag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 2, 1),
    _CtTransFddiEthernetIPFrag_Type()
)
ctTransFddiEthernetIPFrag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransFddiEthernetIPFrag.setStatus("mandatory")


class _CtTransFddiSnapEthernetType_Type(Integer32):
    """Custom type ctTransFddiSnapEthernetType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernetII", 1),
          ("ethernetSnap", 2))
    )


_CtTransFddiSnapEthernetType_Type.__name__ = "Integer32"
_CtTransFddiSnapEthernetType_Object = MibScalar
ctTransFddiSnapEthernetType = _CtTransFddiSnapEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 2, 2),
    _CtTransFddiSnapEthernetType_Type()
)
ctTransFddiSnapEthernetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransFddiSnapEthernetType.setStatus("mandatory")


class _CtTransFddiEthernetAuto_Type(Integer32):
    """Custom type ctTransFddiEthernetAuto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notSupported", 3))
    )


_CtTransFddiEthernetAuto_Type.__name__ = "Integer32"
_CtTransFddiEthernetAuto_Object = MibScalar
ctTransFddiEthernetAuto = _CtTransFddiEthernetAuto_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 2, 3),
    _CtTransFddiEthernetAuto_Type()
)
ctTransFddiEthernetAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransFddiEthernetAuto.setStatus("mandatory")


class _CtTransFddiEthernetSnapIPX_Type(Integer32):
    """Custom type ctTransFddiEthernetSnapIPX based on Integer32"""
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
        *(("ethernet802dot3", 3),
          ("ethernet802dot3Raw", 4),
          ("ethernetII", 1),
          ("ethernetSnap", 2))
    )


_CtTransFddiEthernetSnapIPX_Type.__name__ = "Integer32"
_CtTransFddiEthernetSnapIPX_Object = MibScalar
ctTransFddiEthernetSnapIPX = _CtTransFddiEthernetSnapIPX_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 2, 4),
    _CtTransFddiEthernetSnapIPX_Type()
)
ctTransFddiEthernetSnapIPX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransFddiEthernetSnapIPX.setStatus("mandatory")


class _CtTransFddiEthernet802dot2IPX_Type(Integer32):
    """Custom type ctTransFddiEthernet802dot2IPX based on Integer32"""
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
        *(("ethernet802dot3", 3),
          ("ethernet802dot3Raw", 4),
          ("ethernetII", 1),
          ("ethernetSnap", 2))
    )


_CtTransFddiEthernet802dot2IPX_Type.__name__ = "Integer32"
_CtTransFddiEthernet802dot2IPX_Object = MibScalar
ctTransFddiEthernet802dot2IPX = _CtTransFddiEthernet802dot2IPX_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 2, 5),
    _CtTransFddiEthernet802dot2IPX_Type()
)
ctTransFddiEthernet802dot2IPX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransFddiEthernet802dot2IPX.setStatus("mandatory")


class _CtTransFddiEthernetMACIPX_Type(Integer32):
    """Custom type ctTransFddiEthernetMACIPX based on Integer32"""
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
        *(("ethernet802dot3", 3),
          ("ethernet802dot3Raw", 4),
          ("ethernetII", 1),
          ("ethernetSnap", 2))
    )


_CtTransFddiEthernetMACIPX_Type.__name__ = "Integer32"
_CtTransFddiEthernetMACIPX_Object = MibScalar
ctTransFddiEthernetMACIPX = _CtTransFddiEthernetMACIPX_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 2, 6),
    _CtTransFddiEthernetMACIPX_Type()
)
ctTransFddiEthernetMACIPX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransFddiEthernetMACIPX.setStatus("mandatory")
_CtTransEthernetFddi_ObjectIdentity = ObjectIdentity
ctTransEthernetFddi = _CtTransEthernetFddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 3)
)


class _CtTransEthernetFddiRAW_Type(Integer32):
    """Custom type ctTransEthernetFddiRAW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fDDI802dot2", 1),
          ("fDDIMAC", 3),
          ("fDDISnap", 2))
    )


_CtTransEthernetFddiRAW_Type.__name__ = "Integer32"
_CtTransEthernetFddiRAW_Object = MibScalar
ctTransEthernetFddiRAW = _CtTransEthernetFddiRAW_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 3, 1),
    _CtTransEthernetFddiRAW_Type()
)
ctTransEthernetFddiRAW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransEthernetFddiRAW.setStatus("mandatory")


class _CtTransEthernetFddiPadVerify_Type(Integer32):
    """Custom type ctTransEthernetFddiPadVerify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("not-supported", 3))
    )


_CtTransEthernetFddiPadVerify_Type.__name__ = "Integer32"
_CtTransEthernetFddiPadVerify_Object = MibScalar
ctTransEthernetFddiPadVerify = _CtTransEthernetFddiPadVerify_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 3, 2),
    _CtTransEthernetFddiPadVerify_Type()
)
ctTransEthernetFddiPadVerify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransEthernetFddiPadVerify.setStatus("mandatory")
_CtTransRifDb_ObjectIdentity = ObjectIdentity
ctTransRifDb = _CtTransRifDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4)
)
_CtTransRifDbTable_Object = MibTable
ctTransRifDbTable = _CtTransRifDbTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 1)
)
if mibBuilder.loadTexts:
    ctTransRifDbTable.setStatus("mandatory")
_CtTransRifDbEntry_Object = MibTableRow
ctTransRifDbEntry = _CtTransRifDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 1, 1)
)
ctTransRifDbEntry.setIndexNames(
    (0, "CTRON-TRANSLATION-MIB", "ctTransRifDbMacAddr"),
)
if mibBuilder.loadTexts:
    ctTransRifDbEntry.setStatus("mandatory")
_CtTransRifDbMacAddr_Type = MacAddress
_CtTransRifDbMacAddr_Object = MibTableColumn
ctTransRifDbMacAddr = _CtTransRifDbMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 1, 1, 1),
    _CtTransRifDbMacAddr_Type()
)
ctTransRifDbMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctTransRifDbMacAddr.setStatus("mandatory")
_CtTransRifDbSrcPort_Type = Integer32
_CtTransRifDbSrcPort_Object = MibTableColumn
ctTransRifDbSrcPort = _CtTransRifDbSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 1, 1, 2),
    _CtTransRifDbSrcPort_Type()
)
ctTransRifDbSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctTransRifDbSrcPort.setStatus("mandatory")
_CtTransRifDbLength_Type = Integer32
_CtTransRifDbLength_Object = MibTableColumn
ctTransRifDbLength = _CtTransRifDbLength_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 1, 1, 3),
    _CtTransRifDbLength_Type()
)
ctTransRifDbLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctTransRifDbLength.setStatus("mandatory")


class _CtTransRifDbRIF_Type(DisplayString):
    """Custom type ctTransRifDbRIF based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CtTransRifDbRIF_Type.__name__ = "DisplayString"
_CtTransRifDbRIF_Object = MibTableColumn
ctTransRifDbRIF = _CtTransRifDbRIF_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 1, 1, 4),
    _CtTransRifDbRIF_Type()
)
ctTransRifDbRIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctTransRifDbRIF.setStatus("mandatory")
_CtTransRifDbCtrlTable_Object = MibTable
ctTransRifDbCtrlTable = _CtTransRifDbCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 2)
)
if mibBuilder.loadTexts:
    ctTransRifDbCtrlTable.setStatus("mandatory")
_CtTransRifDbCtrlEntry_Object = MibTableRow
ctTransRifDbCtrlEntry = _CtTransRifDbCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 2, 1)
)
ctTransRifDbCtrlEntry.setIndexNames(
    (0, "CTRON-TRANSLATION-MIB", "ctTransRifDbCtrlPort"),
)
if mibBuilder.loadTexts:
    ctTransRifDbCtrlEntry.setStatus("mandatory")
_CtTransRifDbCtrlPort_Type = Integer32
_CtTransRifDbCtrlPort_Object = MibTableColumn
ctTransRifDbCtrlPort = _CtTransRifDbCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 2, 1, 1),
    _CtTransRifDbCtrlPort_Type()
)
ctTransRifDbCtrlPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctTransRifDbCtrlPort.setStatus("mandatory")


class _CtTransRifDbWeightState_Type(Integer32):
    """Custom type ctTransRifDbWeightState based on Integer32"""
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
        *(("largestmtu", 4),
          ("lastseen", 5),
          ("notsupported", 1),
          ("quickestpath", 3),
          ("shortestpath", 2))
    )


_CtTransRifDbWeightState_Type.__name__ = "Integer32"
_CtTransRifDbWeightState_Object = MibTableColumn
ctTransRifDbWeightState = _CtTransRifDbWeightState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 2, 1, 2),
    _CtTransRifDbWeightState_Type()
)
ctTransRifDbWeightState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransRifDbWeightState.setStatus("mandatory")


class _CtTransRifDbCtrlType_Type(Integer32):
    """Custom type ctTransRifDbCtrlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("explorer", 1),
          ("notsupported", 3))
    )


_CtTransRifDbCtrlType_Type.__name__ = "Integer32"
_CtTransRifDbCtrlType_Object = MibTableColumn
ctTransRifDbCtrlType = _CtTransRifDbCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 2, 1, 3),
    _CtTransRifDbCtrlType_Type()
)
ctTransRifDbCtrlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransRifDbCtrlType.setStatus("mandatory")
_CtTransRifDbAgingTimer_Type = Integer32
_CtTransRifDbAgingTimer_Object = MibTableColumn
ctTransRifDbAgingTimer = _CtTransRifDbAgingTimer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 2, 1, 4),
    _CtTransRifDbAgingTimer_Type()
)
ctTransRifDbAgingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransRifDbAgingTimer.setStatus("mandatory")
_CtTransBcastX_ObjectIdentity = ObjectIdentity
ctTransBcastX = _CtTransBcastX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 5)
)
_CtTransBcastXTable_Object = MibTable
ctTransBcastXTable = _CtTransBcastXTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 5, 1)
)
if mibBuilder.loadTexts:
    ctTransBcastXTable.setStatus("mandatory")
_CtTransBcastXEntry_Object = MibTableRow
ctTransBcastXEntry = _CtTransBcastXEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 5, 1, 1)
)
ctTransBcastXEntry.setIndexNames(
    (0, "CTRON-TRANSLATION-MIB", "ctTransBcastXPort"),
)
if mibBuilder.loadTexts:
    ctTransBcastXEntry.setStatus("mandatory")
_CtTransBcastXPort_Type = Integer32
_CtTransBcastXPort_Object = MibTableColumn
ctTransBcastXPort = _CtTransBcastXPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 5, 1, 1, 1),
    _CtTransBcastXPort_Type()
)
ctTransBcastXPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctTransBcastXPort.setStatus("mandatory")


class _CtTransBcastXMode_Type(Integer32):
    """Custom type ctTransBcastXMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtTransBcastXMode_Type.__name__ = "Integer32"
_CtTransBcastXMode_Object = MibTableColumn
ctTransBcastXMode = _CtTransBcastXMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 5, 1, 1, 2),
    _CtTransBcastXMode_Type()
)
ctTransBcastXMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransBcastXMode.setStatus("mandatory")
_CtTransBcastXMedia_Type = MacAddress
_CtTransBcastXMedia_Object = MibTableColumn
ctTransBcastXMedia = _CtTransBcastXMedia_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 5, 1, 1, 3),
    _CtTransBcastXMedia_Type()
)
ctTransBcastXMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransBcastXMedia.setStatus("mandatory")
_CtTransBcastXCanonical_Type = MacAddress
_CtTransBcastXCanonical_Object = MibTableColumn
ctTransBcastXCanonical = _CtTransBcastXCanonical_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 5, 1, 1, 4),
    _CtTransBcastXCanonical_Type()
)
ctTransBcastXCanonical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransBcastXCanonical.setStatus("mandatory")
_CtTransIbmLlc_ObjectIdentity = ObjectIdentity
ctTransIbmLlc = _CtTransIbmLlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6)
)
_CtTransIbmLlcTable_Object = MibTable
ctTransIbmLlcTable = _CtTransIbmLlcTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1)
)
if mibBuilder.loadTexts:
    ctTransIbmLlcTable.setStatus("mandatory")
_CtTransIbmLlcEntry_Object = MibTableRow
ctTransIbmLlcEntry = _CtTransIbmLlcEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1)
)
ctTransIbmLlcEntry.setIndexNames(
    (0, "CTRON-TRANSLATION-MIB", "ctTransIbmLlcPort"),
)
if mibBuilder.loadTexts:
    ctTransIbmLlcEntry.setStatus("mandatory")
_CtTransIbmLlcPort_Type = Integer32
_CtTransIbmLlcPort_Object = MibTableColumn
ctTransIbmLlcPort = _CtTransIbmLlcPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1, 1),
    _CtTransIbmLlcPort_Type()
)
ctTransIbmLlcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctTransIbmLlcPort.setStatus("mandatory")


class _CtTransIbmLlcNullMode_Type(Integer32):
    """Custom type ctTransIbmLlcNullMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notsupported", 3))
    )


_CtTransIbmLlcNullMode_Type.__name__ = "Integer32"
_CtTransIbmLlcNullMode_Object = MibTableColumn
ctTransIbmLlcNullMode = _CtTransIbmLlcNullMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1, 2),
    _CtTransIbmLlcNullMode_Type()
)
ctTransIbmLlcNullMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransIbmLlcNullMode.setStatus("mandatory")


class _CtTransIbmLlcSnaPathMode_Type(Integer32):
    """Custom type ctTransIbmLlcSnaPathMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notsupported", 3))
    )


_CtTransIbmLlcSnaPathMode_Type.__name__ = "Integer32"
_CtTransIbmLlcSnaPathMode_Object = MibTableColumn
ctTransIbmLlcSnaPathMode = _CtTransIbmLlcSnaPathMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1, 3),
    _CtTransIbmLlcSnaPathMode_Type()
)
ctTransIbmLlcSnaPathMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransIbmLlcSnaPathMode.setStatus("mandatory")


class _CtTransIbmLlcSnaMode_Type(Integer32):
    """Custom type ctTransIbmLlcSnaMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notsupported", 3))
    )


_CtTransIbmLlcSnaMode_Type.__name__ = "Integer32"
_CtTransIbmLlcSnaMode_Object = MibTableColumn
ctTransIbmLlcSnaMode = _CtTransIbmLlcSnaMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1, 4),
    _CtTransIbmLlcSnaMode_Type()
)
ctTransIbmLlcSnaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransIbmLlcSnaMode.setStatus("mandatory")


class _CtTransIbmLlcNbMode_Type(Integer32):
    """Custom type ctTransIbmLlcNbMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notsupported", 3))
    )


_CtTransIbmLlcNbMode_Type.__name__ = "Integer32"
_CtTransIbmLlcNbMode_Object = MibTableColumn
ctTransIbmLlcNbMode = _CtTransIbmLlcNbMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1, 5),
    _CtTransIbmLlcNbMode_Type()
)
ctTransIbmLlcNbMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransIbmLlcNbMode.setStatus("mandatory")


class _CtTransIbmLlcLnmMode_Type(Integer32):
    """Custom type ctTransIbmLlcLnmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notsupported", 3))
    )


_CtTransIbmLlcLnmMode_Type.__name__ = "Integer32"
_CtTransIbmLlcLnmMode_Object = MibTableColumn
ctTransIbmLlcLnmMode = _CtTransIbmLlcLnmMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1, 6),
    _CtTransIbmLlcLnmMode_Type()
)
ctTransIbmLlcLnmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransIbmLlcLnmMode.setStatus("mandatory")


class _CtTransIbmLlcDscMode_Type(Integer32):
    """Custom type ctTransIbmLlcDscMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notsupported", 3))
    )


_CtTransIbmLlcDscMode_Type.__name__ = "Integer32"
_CtTransIbmLlcDscMode_Object = MibTableColumn
ctTransIbmLlcDscMode = _CtTransIbmLlcDscMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1, 7),
    _CtTransIbmLlcDscMode_Type()
)
ctTransIbmLlcDscMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransIbmLlcDscMode.setStatus("mandatory")


class _CtTransIbmLlcOtherMode_Type(Integer32):
    """Custom type ctTransIbmLlcOtherMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notsupported", 3))
    )


_CtTransIbmLlcOtherMode_Type.__name__ = "Integer32"
_CtTransIbmLlcOtherMode_Object = MibTableColumn
ctTransIbmLlcOtherMode = _CtTransIbmLlcOtherMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1, 8),
    _CtTransIbmLlcOtherMode_Type()
)
ctTransIbmLlcOtherMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransIbmLlcOtherMode.setStatus("mandatory")


class _CtTransIbmLlcOtherValue_Type(Integer32):
    """Custom type ctTransIbmLlcOtherValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CtTransIbmLlcOtherValue_Type.__name__ = "Integer32"
_CtTransIbmLlcOtherValue_Object = MibTableColumn
ctTransIbmLlcOtherValue = _CtTransIbmLlcOtherValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1, 9),
    _CtTransIbmLlcOtherValue_Type()
)
ctTransIbmLlcOtherValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransIbmLlcOtherValue.setStatus("mandatory")
_CtTransSr_ObjectIdentity = ObjectIdentity
ctTransSr = _CtTransSr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7)
)
_CtTransSrTable_Object = MibTable
ctTransSrTable = _CtTransSrTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1)
)
if mibBuilder.loadTexts:
    ctTransSrTable.setStatus("mandatory")
_CtTransSrEntry_Object = MibTableRow
ctTransSrEntry = _CtTransSrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1)
)
ctTransSrEntry.setIndexNames(
    (0, "CTRON-TRANSLATION-MIB", "ctTransSrPort"),
)
if mibBuilder.loadTexts:
    ctTransSrEntry.setStatus("mandatory")
_CtTransSrPort_Type = Integer32
_CtTransSrPort_Object = MibTableColumn
ctTransSrPort = _CtTransSrPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 1),
    _CtTransSrPort_Type()
)
ctTransSrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctTransSrPort.setStatus("mandatory")


class _CtTransSrIfMode_Type(Integer32):
    """Custom type ctTransSrIfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sr", 2),
          ("srt", 3),
          ("tp", 1))
    )


_CtTransSrIfMode_Type.__name__ = "Integer32"
_CtTransSrIfMode_Object = MibTableColumn
ctTransSrIfMode = _CtTransSrIfMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 2),
    _CtTransSrIfMode_Type()
)
ctTransSrIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransSrIfMode.setStatus("mandatory")


class _CtTransSrExpMode_Type(Integer32):
    """Custom type ctTransSrExpMode based on Integer32"""
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
        *(("are", 2),
          ("inboundtype", 4),
          ("notsupported", 1),
          ("ste", 3))
    )


_CtTransSrExpMode_Type.__name__ = "Integer32"
_CtTransSrExpMode_Object = MibTableColumn
ctTransSrExpMode = _CtTransSrExpMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 3),
    _CtTransSrExpMode_Type()
)
ctTransSrExpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransSrExpMode.setStatus("mandatory")


class _CtTransSrIP_Type(Integer32):
    """Custom type ctTransSrIP based on Integer32"""
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
        *(("auto", 3),
          ("notsupported", 4),
          ("sr", 2),
          ("tp", 1))
    )


_CtTransSrIP_Type.__name__ = "Integer32"
_CtTransSrIP_Object = MibTableColumn
ctTransSrIP = _CtTransSrIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 4),
    _CtTransSrIP_Type()
)
ctTransSrIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransSrIP.setStatus("mandatory")


class _CtTransSrIPX_Type(Integer32):
    """Custom type ctTransSrIPX based on Integer32"""
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
        *(("auto", 3),
          ("notsupported", 4),
          ("sr", 2),
          ("tp", 1))
    )


_CtTransSrIPX_Type.__name__ = "Integer32"
_CtTransSrIPX_Object = MibTableColumn
ctTransSrIPX = _CtTransSrIPX_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 5),
    _CtTransSrIPX_Type()
)
ctTransSrIPX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransSrIPX.setStatus("mandatory")


class _CtTransSrNetBIOS_Type(Integer32):
    """Custom type ctTransSrNetBIOS based on Integer32"""
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
        *(("auto", 3),
          ("notsupported", 4),
          ("sr", 2),
          ("tp", 1))
    )


_CtTransSrNetBIOS_Type.__name__ = "Integer32"
_CtTransSrNetBIOS_Object = MibTableColumn
ctTransSrNetBIOS = _CtTransSrNetBIOS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 6),
    _CtTransSrNetBIOS_Type()
)
ctTransSrNetBIOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransSrNetBIOS.setStatus("mandatory")


class _CtTransSrSNA_Type(Integer32):
    """Custom type ctTransSrSNA based on Integer32"""
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
        *(("auto", 3),
          ("notsupported", 4),
          ("sr", 2),
          ("tp", 1))
    )


_CtTransSrSNA_Type.__name__ = "Integer32"
_CtTransSrSNA_Object = MibTableColumn
ctTransSrSNA = _CtTransSrSNA_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 7),
    _CtTransSrSNA_Type()
)
ctTransSrSNA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransSrSNA.setStatus("mandatory")


class _CtTransSrOther_Type(Integer32):
    """Custom type ctTransSrOther based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("sr", 2),
          ("tp", 1))
    )


_CtTransSrOther_Type.__name__ = "Integer32"
_CtTransSrOther_Object = MibTableColumn
ctTransSrOther = _CtTransSrOther_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 8),
    _CtTransSrOther_Type()
)
ctTransSrOther.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransSrOther.setStatus("mandatory")
_CtTransSRLocalSegment_Type = Integer32
_CtTransSRLocalSegment_Object = MibTableColumn
ctTransSRLocalSegment = _CtTransSRLocalSegment_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 9),
    _CtTransSRLocalSegment_Type()
)
ctTransSRLocalSegment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransSRLocalSegment.setStatus("mandatory")
_CtTransSrSRLF_Type = Integer32
_CtTransSrSRLF_Object = MibTableColumn
ctTransSrSRLF = _CtTransSrSRLF_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 10),
    _CtTransSrSRLF_Type()
)
ctTransSrSRLF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransSrSRLF.setStatus("mandatory")


class _CtTransSRAutoRingNumberDetect_Type(Integer32):
    """Custom type ctTransSRAutoRingNumberDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("notsupported", 1))
    )


_CtTransSRAutoRingNumberDetect_Type.__name__ = "Integer32"
_CtTransSRAutoRingNumberDetect_Object = MibTableColumn
ctTransSRAutoRingNumberDetect = _CtTransSRAutoRingNumberDetect_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 11),
    _CtTransSRAutoRingNumberDetect_Type()
)
ctTransSRAutoRingNumberDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransSRAutoRingNumberDetect.setStatus("mandatory")
_CtTransNovellCfg_ObjectIdentity = ObjectIdentity
ctTransNovellCfg = _CtTransNovellCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 8)
)
_CtTransNovellCfgTable_Object = MibTable
ctTransNovellCfgTable = _CtTransNovellCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 8, 1)
)
if mibBuilder.loadTexts:
    ctTransNovellCfgTable.setStatus("mandatory")
_CtTransNovellCfgEntry_Object = MibTableRow
ctTransNovellCfgEntry = _CtTransNovellCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 8, 1, 1)
)
ctTransNovellCfgEntry.setIndexNames(
    (0, "CTRON-TRANSLATION-MIB", "ctTransNovellCfgPort"),
)
if mibBuilder.loadTexts:
    ctTransNovellCfgEntry.setStatus("mandatory")
_CtTransNovellCfgPort_Type = Integer32
_CtTransNovellCfgPort_Object = MibTableColumn
ctTransNovellCfgPort = _CtTransNovellCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 8, 1, 1, 1),
    _CtTransNovellCfgPort_Type()
)
ctTransNovellCfgPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctTransNovellCfgPort.setStatus("mandatory")


class _CtTransNovellCfgMode_Type(Integer32):
    """Custom type ctTransNovellCfgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("enabledType2", 3))
    )


_CtTransNovellCfgMode_Type.__name__ = "Integer32"
_CtTransNovellCfgMode_Object = MibTableColumn
ctTransNovellCfgMode = _CtTransNovellCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 8, 1, 1, 2),
    _CtTransNovellCfgMode_Type()
)
ctTransNovellCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransNovellCfgMode.setStatus("mandatory")


class _CtTransNovellGroupMode_Type(Integer32):
    """Custom type ctTransNovellGroupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notsupported", 3))
    )


_CtTransNovellGroupMode_Type.__name__ = "Integer32"
_CtTransNovellGroupMode_Object = MibTableColumn
ctTransNovellGroupMode = _CtTransNovellGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 8, 1, 1, 3),
    _CtTransNovellGroupMode_Type()
)
ctTransNovellGroupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransNovellGroupMode.setStatus("mandatory")
_CtTransIPCfg_ObjectIdentity = ObjectIdentity
ctTransIPCfg = _CtTransIPCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 9)
)
_CtTransIPCfgTable_Object = MibTable
ctTransIPCfgTable = _CtTransIPCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 9, 1)
)
if mibBuilder.loadTexts:
    ctTransIPCfgTable.setStatus("mandatory")
_CtTransIPCfgEntry_Object = MibTableRow
ctTransIPCfgEntry = _CtTransIPCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 9, 1, 1)
)
ctTransIPCfgEntry.setIndexNames(
    (0, "CTRON-TRANSLATION-MIB", "ctTransIPCfgPort"),
)
if mibBuilder.loadTexts:
    ctTransIPCfgEntry.setStatus("mandatory")
_CtTransIPCfgPort_Type = Integer32
_CtTransIPCfgPort_Object = MibTableColumn
ctTransIPCfgPort = _CtTransIPCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 9, 1, 1, 1),
    _CtTransIPCfgPort_Type()
)
ctTransIPCfgPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctTransIPCfgPort.setStatus("mandatory")


class _CtTransIPDataCfgMode_Type(Integer32):
    """Custom type ctTransIPDataCfgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtTransIPDataCfgMode_Type.__name__ = "Integer32"
_CtTransIPDataCfgMode_Object = MibTableColumn
ctTransIPDataCfgMode = _CtTransIPDataCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 9, 1, 1, 2),
    _CtTransIPDataCfgMode_Type()
)
ctTransIPDataCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransIPDataCfgMode.setStatus("mandatory")


class _CtTransIPArpCfgMode_Type(Integer32):
    """Custom type ctTransIPArpCfgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtTransIPArpCfgMode_Type.__name__ = "Integer32"
_CtTransIPArpCfgMode_Object = MibTableColumn
ctTransIPArpCfgMode = _CtTransIPArpCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 9, 1, 1, 3),
    _CtTransIPArpCfgMode_Type()
)
ctTransIPArpCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransIPArpCfgMode.setStatus("mandatory")


class _CtTransIPRarpCfgMode_Type(Integer32):
    """Custom type ctTransIPRarpCfgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtTransIPRarpCfgMode_Type.__name__ = "Integer32"
_CtTransIPRarpCfgMode_Object = MibTableColumn
ctTransIPRarpCfgMode = _CtTransIPRarpCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 9, 1, 1, 4),
    _CtTransIPRarpCfgMode_Type()
)
ctTransIPRarpCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransIPRarpCfgMode.setStatus("mandatory")
_CtTransA2Cfg_ObjectIdentity = ObjectIdentity
ctTransA2Cfg = _CtTransA2Cfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 10)
)
_CtTransA2CfgTable_Object = MibTable
ctTransA2CfgTable = _CtTransA2CfgTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 10, 1)
)
if mibBuilder.loadTexts:
    ctTransA2CfgTable.setStatus("mandatory")
_CtTransA2CfgEntry_Object = MibTableRow
ctTransA2CfgEntry = _CtTransA2CfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 10, 1, 1)
)
ctTransA2CfgEntry.setIndexNames(
    (0, "CTRON-TRANSLATION-MIB", "ctTransA2CfgPort"),
)
if mibBuilder.loadTexts:
    ctTransA2CfgEntry.setStatus("mandatory")
_CtTransA2CfgPort_Type = Integer32
_CtTransA2CfgPort_Object = MibTableColumn
ctTransA2CfgPort = _CtTransA2CfgPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 10, 1, 1, 1),
    _CtTransA2CfgPort_Type()
)
ctTransA2CfgPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctTransA2CfgPort.setStatus("mandatory")


class _CtTransA2DataCfgMode_Type(Integer32):
    """Custom type ctTransA2DataCfgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtTransA2DataCfgMode_Type.__name__ = "Integer32"
_CtTransA2DataCfgMode_Object = MibTableColumn
ctTransA2DataCfgMode = _CtTransA2DataCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 10, 1, 1, 2),
    _CtTransA2DataCfgMode_Type()
)
ctTransA2DataCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransA2DataCfgMode.setStatus("mandatory")


class _CtTransA2ArpCfgMode_Type(Integer32):
    """Custom type ctTransA2ArpCfgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtTransA2ArpCfgMode_Type.__name__ = "Integer32"
_CtTransA2ArpCfgMode_Object = MibTableColumn
ctTransA2ArpCfgMode = _CtTransA2ArpCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 10, 1, 1, 3),
    _CtTransA2ArpCfgMode_Type()
)
ctTransA2ArpCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransA2ArpCfgMode.setStatus("mandatory")


class _CtTransA2McastCfgMode_Type(Integer32):
    """Custom type ctTransA2McastCfgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtTransA2McastCfgMode_Type.__name__ = "Integer32"
_CtTransA2McastCfgMode_Object = MibTableColumn
ctTransA2McastCfgMode = _CtTransA2McastCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 10, 1, 1, 4),
    _CtTransA2McastCfgMode_Type()
)
ctTransA2McastCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransA2McastCfgMode.setStatus("mandatory")
_CtTransOtherCfg_ObjectIdentity = ObjectIdentity
ctTransOtherCfg = _CtTransOtherCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11)
)
_CtTransOtherTable_Object = MibTable
ctTransOtherTable = _CtTransOtherTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1)
)
if mibBuilder.loadTexts:
    ctTransOtherTable.setStatus("mandatory")
_CtTransOtherEntry_Object = MibTableRow
ctTransOtherEntry = _CtTransOtherEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1)
)
ctTransOtherEntry.setIndexNames(
    (0, "CTRON-TRANSLATION-MIB", "ctTransOtherPort"),
)
if mibBuilder.loadTexts:
    ctTransOtherEntry.setStatus("mandatory")
_CtTransOtherPort_Type = Integer32
_CtTransOtherPort_Object = MibTableColumn
ctTransOtherPort = _CtTransOtherPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 1),
    _CtTransOtherPort_Type()
)
ctTransOtherPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctTransOtherPort.setStatus("mandatory")


class _CtTransOtherUnknownSap_Type(Integer32):
    """Custom type ctTransOtherUnknownSap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtTransOtherUnknownSap_Type.__name__ = "Integer32"
_CtTransOtherUnknownSap_Object = MibTableColumn
ctTransOtherUnknownSap = _CtTransOtherUnknownSap_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 2),
    _CtTransOtherUnknownSap_Type()
)
ctTransOtherUnknownSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransOtherUnknownSap.setStatus("mandatory")


class _CtTransOtherUnknownSnap_Type(Integer32):
    """Custom type ctTransOtherUnknownSnap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtTransOtherUnknownSnap_Type.__name__ = "Integer32"
_CtTransOtherUnknownSnap_Object = MibTableColumn
ctTransOtherUnknownSnap = _CtTransOtherUnknownSnap_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 3),
    _CtTransOtherUnknownSnap_Type()
)
ctTransOtherUnknownSnap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransOtherUnknownSnap.setStatus("mandatory")


class _CtTransOtherSapDsap1Mode_Type(Integer32):
    """Custom type ctTransOtherSapDsap1Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtTransOtherSapDsap1Mode_Type.__name__ = "Integer32"
_CtTransOtherSapDsap1Mode_Object = MibTableColumn
ctTransOtherSapDsap1Mode = _CtTransOtherSapDsap1Mode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 4),
    _CtTransOtherSapDsap1Mode_Type()
)
ctTransOtherSapDsap1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransOtherSapDsap1Mode.setStatus("mandatory")


class _CtTransOtherSapDsap1Val_Type(Integer32):
    """Custom type ctTransOtherSapDsap1Val based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CtTransOtherSapDsap1Val_Type.__name__ = "Integer32"
_CtTransOtherSapDsap1Val_Object = MibTableColumn
ctTransOtherSapDsap1Val = _CtTransOtherSapDsap1Val_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 5),
    _CtTransOtherSapDsap1Val_Type()
)
ctTransOtherSapDsap1Val.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransOtherSapDsap1Val.setStatus("mandatory")


class _CtTransOtherSapDsap2Mode_Type(Integer32):
    """Custom type ctTransOtherSapDsap2Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtTransOtherSapDsap2Mode_Type.__name__ = "Integer32"
_CtTransOtherSapDsap2Mode_Object = MibTableColumn
ctTransOtherSapDsap2Mode = _CtTransOtherSapDsap2Mode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 6),
    _CtTransOtherSapDsap2Mode_Type()
)
ctTransOtherSapDsap2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransOtherSapDsap2Mode.setStatus("mandatory")


class _CtTransOtherSapDsap2Val_Type(Integer32):
    """Custom type ctTransOtherSapDsap2Val based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CtTransOtherSapDsap2Val_Type.__name__ = "Integer32"
_CtTransOtherSapDsap2Val_Object = MibTableColumn
ctTransOtherSapDsap2Val = _CtTransOtherSapDsap2Val_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 7),
    _CtTransOtherSapDsap2Val_Type()
)
ctTransOtherSapDsap2Val.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransOtherSapDsap2Val.setStatus("mandatory")


class _CtTransOtherSapDsap3Mode_Type(Integer32):
    """Custom type ctTransOtherSapDsap3Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtTransOtherSapDsap3Mode_Type.__name__ = "Integer32"
_CtTransOtherSapDsap3Mode_Object = MibTableColumn
ctTransOtherSapDsap3Mode = _CtTransOtherSapDsap3Mode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 8),
    _CtTransOtherSapDsap3Mode_Type()
)
ctTransOtherSapDsap3Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransOtherSapDsap3Mode.setStatus("mandatory")


class _CtTransOtherSapDsap3Val_Type(Integer32):
    """Custom type ctTransOtherSapDsap3Val based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CtTransOtherSapDsap3Val_Type.__name__ = "Integer32"
_CtTransOtherSapDsap3Val_Object = MibTableColumn
ctTransOtherSapDsap3Val = _CtTransOtherSapDsap3Val_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 9),
    _CtTransOtherSapDsap3Val_Type()
)
ctTransOtherSapDsap3Val.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransOtherSapDsap3Val.setStatus("mandatory")


class _CtTransOtherSnap1Mode_Type(Integer32):
    """Custom type ctTransOtherSnap1Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtTransOtherSnap1Mode_Type.__name__ = "Integer32"
_CtTransOtherSnap1Mode_Object = MibTableColumn
ctTransOtherSnap1Mode = _CtTransOtherSnap1Mode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 10),
    _CtTransOtherSnap1Mode_Type()
)
ctTransOtherSnap1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransOtherSnap1Mode.setStatus("mandatory")


class _CtTransOtherSnap1Val_Type(Integer32):
    """Custom type ctTransOtherSnap1Val based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CtTransOtherSnap1Val_Type.__name__ = "Integer32"
_CtTransOtherSnap1Val_Object = MibTableColumn
ctTransOtherSnap1Val = _CtTransOtherSnap1Val_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 11),
    _CtTransOtherSnap1Val_Type()
)
ctTransOtherSnap1Val.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransOtherSnap1Val.setStatus("mandatory")


class _CtTransOtherSnap2Mode_Type(Integer32):
    """Custom type ctTransOtherSnap2Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CtTransOtherSnap2Mode_Type.__name__ = "Integer32"
_CtTransOtherSnap2Mode_Object = MibTableColumn
ctTransOtherSnap2Mode = _CtTransOtherSnap2Mode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 12),
    _CtTransOtherSnap2Mode_Type()
)
ctTransOtherSnap2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransOtherSnap2Mode.setStatus("mandatory")


class _CtTransOtherSnap2Val_Type(Integer32):
    """Custom type ctTransOtherSnap2Val based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CtTransOtherSnap2Val_Type.__name__ = "Integer32"
_CtTransOtherSnap2Val_Object = MibTableColumn
ctTransOtherSnap2Val = _CtTransOtherSnap2Val_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 13),
    _CtTransOtherSnap2Val_Type()
)
ctTransOtherSnap2Val.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransOtherSnap2Val.setStatus("mandatory")
_CtTranslfpsCfg_ObjectIdentity = ObjectIdentity
ctTranslfpsCfg = _CtTranslfpsCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 12)
)
_CtTransLfpsTable_Object = MibTable
ctTransLfpsTable = _CtTransLfpsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 12, 1)
)
if mibBuilder.loadTexts:
    ctTransLfpsTable.setStatus("mandatory")
_CtTransLfpsEntry_Object = MibTableRow
ctTransLfpsEntry = _CtTransLfpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 12, 1, 1)
)
ctTransLfpsEntry.setIndexNames(
    (0, "CTRON-TRANSLATION-MIB", "ctTransLfpsPort"),
)
if mibBuilder.loadTexts:
    ctTransLfpsEntry.setStatus("mandatory")
_CtTransLfpsPort_Type = Integer32
_CtTransLfpsPort_Object = MibTableColumn
ctTransLfpsPort = _CtTransLfpsPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 12, 1, 1, 1),
    _CtTransLfpsPort_Type()
)
ctTransLfpsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctTransLfpsPort.setStatus("mandatory")


class _CtTransLfpsAdminStatus_Type(Integer32):
    """Custom type ctTransLfpsAdminStatus based on Integer32"""
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
        *(("auto", 4),
          ("fragment-if-possible", 2),
          ("large", 1),
          ("small", 3))
    )


_CtTransLfpsAdminStatus_Type.__name__ = "Integer32"
_CtTransLfpsAdminStatus_Object = MibTableColumn
ctTransLfpsAdminStatus = _CtTransLfpsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 12, 1, 1, 2),
    _CtTransLfpsAdminStatus_Type()
)
ctTransLfpsAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTransLfpsAdminStatus.setStatus("mandatory")


class _CtTransLfpsOperationalStatus_Type(Integer32):
    """Custom type ctTransLfpsOperationalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fragment-if-possible", 2),
          ("large", 1),
          ("small", 3))
    )


_CtTransLfpsOperationalStatus_Type.__name__ = "Integer32"
_CtTransLfpsOperationalStatus_Object = MibTableColumn
ctTransLfpsOperationalStatus = _CtTransLfpsOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 12, 1, 1, 3),
    _CtTransLfpsOperationalStatus_Type()
)
ctTransLfpsOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctTransLfpsOperationalStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-TRANSLATION-MIB",
    **{"ctTransFddiAtm": ctTransFddiAtm,
       "ctTransFddiAtmMtu": ctTransFddiAtmMtu,
       "ctTransFddiAtmIPFrag": ctTransFddiAtmIPFrag,
       "ctTransFddiEthernet": ctTransFddiEthernet,
       "ctTransFddiEthernetIPFrag": ctTransFddiEthernetIPFrag,
       "ctTransFddiSnapEthernetType": ctTransFddiSnapEthernetType,
       "ctTransFddiEthernetAuto": ctTransFddiEthernetAuto,
       "ctTransFddiEthernetSnapIPX": ctTransFddiEthernetSnapIPX,
       "ctTransFddiEthernet802dot2IPX": ctTransFddiEthernet802dot2IPX,
       "ctTransFddiEthernetMACIPX": ctTransFddiEthernetMACIPX,
       "ctTransEthernetFddi": ctTransEthernetFddi,
       "ctTransEthernetFddiRAW": ctTransEthernetFddiRAW,
       "ctTransEthernetFddiPadVerify": ctTransEthernetFddiPadVerify,
       "ctTransRifDb": ctTransRifDb,
       "ctTransRifDbTable": ctTransRifDbTable,
       "ctTransRifDbEntry": ctTransRifDbEntry,
       "ctTransRifDbMacAddr": ctTransRifDbMacAddr,
       "ctTransRifDbSrcPort": ctTransRifDbSrcPort,
       "ctTransRifDbLength": ctTransRifDbLength,
       "ctTransRifDbRIF": ctTransRifDbRIF,
       "ctTransRifDbCtrlTable": ctTransRifDbCtrlTable,
       "ctTransRifDbCtrlEntry": ctTransRifDbCtrlEntry,
       "ctTransRifDbCtrlPort": ctTransRifDbCtrlPort,
       "ctTransRifDbWeightState": ctTransRifDbWeightState,
       "ctTransRifDbCtrlType": ctTransRifDbCtrlType,
       "ctTransRifDbAgingTimer": ctTransRifDbAgingTimer,
       "ctTransBcastX": ctTransBcastX,
       "ctTransBcastXTable": ctTransBcastXTable,
       "ctTransBcastXEntry": ctTransBcastXEntry,
       "ctTransBcastXPort": ctTransBcastXPort,
       "ctTransBcastXMode": ctTransBcastXMode,
       "ctTransBcastXMedia": ctTransBcastXMedia,
       "ctTransBcastXCanonical": ctTransBcastXCanonical,
       "ctTransIbmLlc": ctTransIbmLlc,
       "ctTransIbmLlcTable": ctTransIbmLlcTable,
       "ctTransIbmLlcEntry": ctTransIbmLlcEntry,
       "ctTransIbmLlcPort": ctTransIbmLlcPort,
       "ctTransIbmLlcNullMode": ctTransIbmLlcNullMode,
       "ctTransIbmLlcSnaPathMode": ctTransIbmLlcSnaPathMode,
       "ctTransIbmLlcSnaMode": ctTransIbmLlcSnaMode,
       "ctTransIbmLlcNbMode": ctTransIbmLlcNbMode,
       "ctTransIbmLlcLnmMode": ctTransIbmLlcLnmMode,
       "ctTransIbmLlcDscMode": ctTransIbmLlcDscMode,
       "ctTransIbmLlcOtherMode": ctTransIbmLlcOtherMode,
       "ctTransIbmLlcOtherValue": ctTransIbmLlcOtherValue,
       "ctTransSr": ctTransSr,
       "ctTransSrTable": ctTransSrTable,
       "ctTransSrEntry": ctTransSrEntry,
       "ctTransSrPort": ctTransSrPort,
       "ctTransSrIfMode": ctTransSrIfMode,
       "ctTransSrExpMode": ctTransSrExpMode,
       "ctTransSrIP": ctTransSrIP,
       "ctTransSrIPX": ctTransSrIPX,
       "ctTransSrNetBIOS": ctTransSrNetBIOS,
       "ctTransSrSNA": ctTransSrSNA,
       "ctTransSrOther": ctTransSrOther,
       "ctTransSRLocalSegment": ctTransSRLocalSegment,
       "ctTransSrSRLF": ctTransSrSRLF,
       "ctTransSRAutoRingNumberDetect": ctTransSRAutoRingNumberDetect,
       "ctTransNovellCfg": ctTransNovellCfg,
       "ctTransNovellCfgTable": ctTransNovellCfgTable,
       "ctTransNovellCfgEntry": ctTransNovellCfgEntry,
       "ctTransNovellCfgPort": ctTransNovellCfgPort,
       "ctTransNovellCfgMode": ctTransNovellCfgMode,
       "ctTransNovellGroupMode": ctTransNovellGroupMode,
       "ctTransIPCfg": ctTransIPCfg,
       "ctTransIPCfgTable": ctTransIPCfgTable,
       "ctTransIPCfgEntry": ctTransIPCfgEntry,
       "ctTransIPCfgPort": ctTransIPCfgPort,
       "ctTransIPDataCfgMode": ctTransIPDataCfgMode,
       "ctTransIPArpCfgMode": ctTransIPArpCfgMode,
       "ctTransIPRarpCfgMode": ctTransIPRarpCfgMode,
       "ctTransA2Cfg": ctTransA2Cfg,
       "ctTransA2CfgTable": ctTransA2CfgTable,
       "ctTransA2CfgEntry": ctTransA2CfgEntry,
       "ctTransA2CfgPort": ctTransA2CfgPort,
       "ctTransA2DataCfgMode": ctTransA2DataCfgMode,
       "ctTransA2ArpCfgMode": ctTransA2ArpCfgMode,
       "ctTransA2McastCfgMode": ctTransA2McastCfgMode,
       "ctTransOtherCfg": ctTransOtherCfg,
       "ctTransOtherTable": ctTransOtherTable,
       "ctTransOtherEntry": ctTransOtherEntry,
       "ctTransOtherPort": ctTransOtherPort,
       "ctTransOtherUnknownSap": ctTransOtherUnknownSap,
       "ctTransOtherUnknownSnap": ctTransOtherUnknownSnap,
       "ctTransOtherSapDsap1Mode": ctTransOtherSapDsap1Mode,
       "ctTransOtherSapDsap1Val": ctTransOtherSapDsap1Val,
       "ctTransOtherSapDsap2Mode": ctTransOtherSapDsap2Mode,
       "ctTransOtherSapDsap2Val": ctTransOtherSapDsap2Val,
       "ctTransOtherSapDsap3Mode": ctTransOtherSapDsap3Mode,
       "ctTransOtherSapDsap3Val": ctTransOtherSapDsap3Val,
       "ctTransOtherSnap1Mode": ctTransOtherSnap1Mode,
       "ctTransOtherSnap1Val": ctTransOtherSnap1Val,
       "ctTransOtherSnap2Mode": ctTransOtherSnap2Mode,
       "ctTransOtherSnap2Val": ctTransOtherSnap2Val,
       "ctTranslfpsCfg": ctTranslfpsCfg,
       "ctTransLfpsTable": ctTransLfpsTable,
       "ctTransLfpsEntry": ctTransLfpsEntry,
       "ctTransLfpsPort": ctTransLfpsPort,
       "ctTransLfpsAdminStatus": ctTransLfpsAdminStatus,
       "ctTransLfpsOperationalStatus": ctTransLfpsOperationalStatus}
)
