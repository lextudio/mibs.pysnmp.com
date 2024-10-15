# SNMP MIB module (ETH-SWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ETH-SWITCH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:54 2024
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

(scanet,) = mibBuilder.importSymbols(
    "SCANET-MIB",
    "scanet")

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



class ProductIds(Integer32):
    """Custom type ProductIds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1163067410,
              1163067456,
              1163067648,
              1163067649,
              1163067650,
              1163067651,
              1163067664,
              1163067665,
              1163067732,
              1163067733,
              1163072800,
              1163072816,
              1163073552,
              1163073568,
              1163073584,
              1163073585,
              1163073586,
              1163073600,
              1163073616,
              1163073617,
              1163076624,
              1163076640,
              1163076656,
              1163076657,
              1280323585,
              1280323586,
              1280323587,
              1280323588,
              1280323589,
              1280323590,
              1280323604,
              1280323605)
        )
    )
    namedValues = NamedValues(
        *(("es-0012", 1163067410),
          ("es-0040", 1163067456),
          ("es-0100", 1163067648),
          ("es-0101", 1163067649),
          ("es-0103", 1163067651),
          ("es-0111", 1163067665),
          ("es-0154", 1163067732),
          ("es-0155", 1163067733),
          ("es-1520", 1163072800),
          ("es-1530", 1163072816),
          ("es-1810", 1163073552),
          ("es-1820", 1163073568),
          ("es-1830", 1163073584),
          ("es-1831", 1163073585),
          ("es-1832", 1163073586),
          ("es-1840", 1163073600),
          ("es-1850", 1163073616),
          ("es100fx", 1163073617),
          ("es100mmfx", 1163067650),
          ("es100mmtx", 1163067664),
          ("es10mmfl", 1163076657),
          ("es10mmt12", 1163076656),
          ("es10t24", 1163076624),
          ("es10t24plus", 1163076640),
          ("lp-3001", 1280323585),
          ("lp-3002", 1280323586),
          ("lp-3003", 1280323587),
          ("lp-3004", 1280323588),
          ("lp-3005", 1280323589),
          ("lp-3006", 1280323590),
          ("lp-3014", 1280323604),
          ("lp-3015", 1280323605),
          ("notAvailable", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EthSwitch_ObjectIdentity = ObjectIdentity
ethSwitch = _EthSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 39)
)
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 39, 1)
)


class _ScSegments_Type(Integer32):
    """Custom type scSegments based on Integer32"""
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
        *(("none", 8),
          ("segmentA", 1),
          ("segmentAandB", 3),
          ("segmentAandBandC", 7),
          ("segmentAandC", 5),
          ("segmentB", 2),
          ("segmentBandC", 6),
          ("segmentC", 4))
    )


_ScSegments_Type.__name__ = "Integer32"
_ScSegments_Object = MibScalar
scSegments = _ScSegments_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 1, 1),
    _ScSegments_Type()
)
scSegments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSegments.setStatus("mandatory")


class _DefaultSwitchMode_Type(Integer32):
    """Custom type defaultSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 5),
          ("cutThrough", 2),
          ("fragmentFree", 3),
          ("storeAndForward", 4))
    )


_DefaultSwitchMode_Type.__name__ = "Integer32"
_DefaultSwitchMode_Object = MibScalar
defaultSwitchMode = _DefaultSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 1, 2),
    _DefaultSwitchMode_Type()
)
defaultSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultSwitchMode.setStatus("mandatory")


class _DefaultThrottleBackMode_Type(Integer32):
    """Custom type defaultThrottleBackMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_DefaultThrottleBackMode_Type.__name__ = "Integer32"
_DefaultThrottleBackMode_Object = MibScalar
defaultThrottleBackMode = _DefaultThrottleBackMode_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 1, 3),
    _DefaultThrottleBackMode_Type()
)
defaultThrottleBackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultThrottleBackMode.setStatus("mandatory")
_NetworkPort_Type = Integer32
_NetworkPort_Object = MibScalar
networkPort = _NetworkPort_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 1, 4),
    _NetworkPort_Type()
)
networkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkPort.setStatus("mandatory")
_Module_ObjectIdentity = ObjectIdentity
module = _Module_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 39, 2)
)
_ExpansionModule_Type = ProductIds
_ExpansionModule_Object = MibScalar
expansionModule = _ExpansionModule_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 2, 1),
    _ExpansionModule_Type()
)
expansionModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expansionModule.setStatus("mandatory")
_Ports_ObjectIdentity = ObjectIdentity
ports = _Ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 39, 3)
)
_PortLastChange_Type = TimeTicks
_PortLastChange_Object = MibScalar
portLastChange = _PortLastChange_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 3, 1),
    _PortLastChange_Type()
)
portLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLastChange.setStatus("mandatory")
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 3, 2)
)
if mibBuilder.loadTexts:
    portTable.setStatus("mandatory")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 3, 2, 1)
)
portEntry.setIndexNames(
    (0, "ETH-SWITCH-MIB", "portNumber"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("mandatory")
_PortNumber_Type = Integer32
_PortNumber_Object = MibTableColumn
portNumber = _PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 3, 2, 1, 1),
    _PortNumber_Type()
)
portNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portNumber.setStatus("mandatory")
_PortInterfaceIndex_Type = Integer32
_PortInterfaceIndex_Object = MibTableColumn
portInterfaceIndex = _PortInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 3, 2, 1, 2),
    _PortInterfaceIndex_Type()
)
portInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInterfaceIndex.setStatus("mandatory")


class _PortLED_Type(OctetString):
    """Custom type portLED based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PortLED_Type.__name__ = "OctetString"
_PortLED_Object = MibTableColumn
portLED = _PortLED_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 3, 2, 1, 3),
    _PortLED_Type()
)
portLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLED.setStatus("mandatory")
_PortState_Type = Integer32
_PortState_Object = MibTableColumn
portState = _PortState_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 3, 2, 1, 4),
    _PortState_Type()
)
portState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portState.setStatus("mandatory")
_PortCardNumber_Type = Integer32
_PortCardNumber_Object = MibTableColumn
portCardNumber = _PortCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 3, 2, 1, 5),
    _PortCardNumber_Type()
)
portCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCardNumber.setStatus("mandatory")
_PortPimNumber_Type = Integer32
_PortPimNumber_Object = MibTableColumn
portPimNumber = _PortPimNumber_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 3, 2, 1, 6),
    _PortPimNumber_Type()
)
portPimNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPimNumber.setStatus("mandatory")
_PortPimPortNumber_Type = Integer32
_PortPimPortNumber_Object = MibTableColumn
portPimPortNumber = _PortPimPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 3, 2, 1, 7),
    _PortPimPortNumber_Type()
)
portPimPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPimPortNumber.setStatus("mandatory")
_PortIfTable_Object = MibTable
portIfTable = _PortIfTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 3, 3)
)
if mibBuilder.loadTexts:
    portIfTable.setStatus("mandatory")
_PortIfEntry_Object = MibTableRow
portIfEntry = _PortIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 3, 3, 1)
)
portIfEntry.setIndexNames(
    (0, "ETH-SWITCH-MIB", "portIfIndex"),
)
if mibBuilder.loadTexts:
    portIfEntry.setStatus("mandatory")
_PortIfIndex_Type = Integer32
_PortIfIndex_Object = MibTableColumn
portIfIndex = _PortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 3, 3, 1, 1),
    _PortIfIndex_Type()
)
portIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIfIndex.setStatus("mandatory")


class _PortIfDescr_Type(DisplayString):
    """Custom type portIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PortIfDescr_Type.__name__ = "DisplayString"
_PortIfDescr_Object = MibTableColumn
portIfDescr = _PortIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 3, 3, 1, 2),
    _PortIfDescr_Type()
)
portIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portIfDescr.setStatus("mandatory")


class _PortIfLocation_Type(DisplayString):
    """Custom type portIfLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PortIfLocation_Type.__name__ = "DisplayString"
_PortIfLocation_Object = MibTableColumn
portIfLocation = _PortIfLocation_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 3, 3, 1, 3),
    _PortIfLocation_Type()
)
portIfLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portIfLocation.setStatus("mandatory")


class _PortIfSwitchMode_Type(Integer32):
    """Custom type portIfSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 5),
          ("cutThrough", 2),
          ("default", 1),
          ("fragmentFree", 3),
          ("notAvailable", 99),
          ("storeAndForward", 4))
    )


_PortIfSwitchMode_Type.__name__ = "Integer32"
_PortIfSwitchMode_Object = MibTableColumn
portIfSwitchMode = _PortIfSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 3, 3, 1, 4),
    _PortIfSwitchMode_Type()
)
portIfSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portIfSwitchMode.setStatus("mandatory")


class _PortIfDuplex_Type(Integer32):
    """Custom type portIfDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("autoDetect", 1),
          ("autoDetectedFull", 5),
          ("autoDetectedHalf", 4),
          ("full", 3),
          ("half", 2),
          ("notAvailable", 99))
    )


_PortIfDuplex_Type.__name__ = "Integer32"
_PortIfDuplex_Object = MibTableColumn
portIfDuplex = _PortIfDuplex_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 3, 3, 1, 5),
    _PortIfDuplex_Type()
)
portIfDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIfDuplex.setStatus("mandatory")


class _PortIfThrottleBack_Type(Integer32):
    """Custom type portIfThrottleBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("disable", 3),
          ("enable", 2),
          ("notAvailable", 99))
    )


_PortIfThrottleBack_Type.__name__ = "Integer32"
_PortIfThrottleBack_Object = MibTableColumn
portIfThrottleBack = _PortIfThrottleBack_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 3, 3, 1, 6),
    _PortIfThrottleBack_Type()
)
portIfThrottleBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portIfThrottleBack.setStatus("mandatory")


class _PortIfType_Type(Integer32):
    """Custom type portIfType based on Integer32"""
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
              14,
              15,
              51,
              54,
              100,
              101,
              102,
              110)
        )
    )
    namedValues = NamedValues(
        *(("absent", 1),
          ("aui", 3),
          ("backplane", 100),
          ("hsb", 101),
          ("hundredbasefx", 54),
          ("hundredbasetx", 51),
          ("internal", 102),
          ("layer3link", 110),
          ("tenbase2", 2),
          ("tenbasefl", 6),
          ("tenbaseflfullduplex", 7),
          ("tenbasetstp", 5),
          ("tenbasetutp", 4),
          ("tenbasetxstp", 15),
          ("tenbasetxutp", 14))
    )


_PortIfType_Type.__name__ = "Integer32"
_PortIfType_Object = MibTableColumn
portIfType = _PortIfType_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 3, 3, 1, 7),
    _PortIfType_Type()
)
portIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIfType.setStatus("mandatory")


class _PortIfDuplexSupported_Type(Integer32):
    """Custom type portIfDuplexSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7,
              99)
        )
    )
    namedValues = NamedValues(
        *(("auto", 4),
          ("autoAndHalfAndFull", 7),
          ("full", 2),
          ("half", 1),
          ("halfAndFull", 3),
          ("notAvailable", 99))
    )


_PortIfDuplexSupported_Type.__name__ = "Integer32"
_PortIfDuplexSupported_Object = MibTableColumn
portIfDuplexSupported = _PortIfDuplexSupported_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 3, 3, 1, 8),
    _PortIfDuplexSupported_Type()
)
portIfDuplexSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIfDuplexSupported.setStatus("mandatory")


class _PortIfSpeedSupported_Type(Integer32):
    """Custom type portIfSpeedSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 99),
          ("speed100Mbit", 2),
          ("speed10And100Mbit", 3),
          ("speed10Mbit", 1),
          ("speed155Mbit", 5),
          ("speedAutoAnd10And100Mbit", 4))
    )


_PortIfSpeedSupported_Type.__name__ = "Integer32"
_PortIfSpeedSupported_Object = MibTableColumn
portIfSpeedSupported = _PortIfSpeedSupported_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 3, 3, 1, 9),
    _PortIfSpeedSupported_Type()
)
portIfSpeedSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIfSpeedSupported.setStatus("mandatory")


class _PortIfSpeedAndDuplex_Type(OctetString):
    """Custom type portIfSpeedAndDuplex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_PortIfSpeedAndDuplex_Type.__name__ = "OctetString"
_PortIfSpeedAndDuplex_Object = MibTableColumn
portIfSpeedAndDuplex = _PortIfSpeedAndDuplex_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 3, 3, 1, 10),
    _PortIfSpeedAndDuplex_Type()
)
portIfSpeedAndDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portIfSpeedAndDuplex.setStatus("mandatory")
_Statistic_ObjectIdentity = ObjectIdentity
statistic = _Statistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 39, 4)
)
_TxStatTable_Object = MibTable
txStatTable = _TxStatTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1)
)
if mibBuilder.loadTexts:
    txStatTable.setStatus("mandatory")
_TxStatEntry_Object = MibTableRow
txStatEntry = _TxStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1)
)
txStatEntry.setIndexNames(
    (0, "ETH-SWITCH-MIB", "txStatIndex"),
)
if mibBuilder.loadTexts:
    txStatEntry.setStatus("mandatory")
_TxStatIndex_Type = Integer32
_TxStatIndex_Object = MibTableColumn
txStatIndex = _TxStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1, 1),
    _TxStatIndex_Type()
)
txStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txStatIndex.setStatus("mandatory")
_TxUCPkts64Octets_Type = Counter32
_TxUCPkts64Octets_Object = MibTableColumn
txUCPkts64Octets = _TxUCPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1, 2),
    _TxUCPkts64Octets_Type()
)
txUCPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txUCPkts64Octets.setStatus("mandatory")
_TxUCPkts65To127Octets_Type = Counter32
_TxUCPkts65To127Octets_Object = MibTableColumn
txUCPkts65To127Octets = _TxUCPkts65To127Octets_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1, 3),
    _TxUCPkts65To127Octets_Type()
)
txUCPkts65To127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txUCPkts65To127Octets.setStatus("mandatory")
_TxUCPkts128To255Octets_Type = Counter32
_TxUCPkts128To255Octets_Object = MibTableColumn
txUCPkts128To255Octets = _TxUCPkts128To255Octets_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1, 4),
    _TxUCPkts128To255Octets_Type()
)
txUCPkts128To255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txUCPkts128To255Octets.setStatus("mandatory")
_TxUCPkts256To511Octets_Type = Counter32
_TxUCPkts256To511Octets_Object = MibTableColumn
txUCPkts256To511Octets = _TxUCPkts256To511Octets_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1, 5),
    _TxUCPkts256To511Octets_Type()
)
txUCPkts256To511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txUCPkts256To511Octets.setStatus("mandatory")
_TxUCPkts512To1023Octets_Type = Counter32
_TxUCPkts512To1023Octets_Object = MibTableColumn
txUCPkts512To1023Octets = _TxUCPkts512To1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1, 6),
    _TxUCPkts512To1023Octets_Type()
)
txUCPkts512To1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txUCPkts512To1023Octets.setStatus("mandatory")
_TxUCPkts1024To1518Octets_Type = Counter32
_TxUCPkts1024To1518Octets_Object = MibTableColumn
txUCPkts1024To1518Octets = _TxUCPkts1024To1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1, 7),
    _TxUCPkts1024To1518Octets_Type()
)
txUCPkts1024To1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txUCPkts1024To1518Octets.setStatus("mandatory")
_TxMCPkts64Octets_Type = Counter32
_TxMCPkts64Octets_Object = MibTableColumn
txMCPkts64Octets = _TxMCPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1, 8),
    _TxMCPkts64Octets_Type()
)
txMCPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txMCPkts64Octets.setStatus("mandatory")
_TxMCPkts65To127Octets_Type = Counter32
_TxMCPkts65To127Octets_Object = MibTableColumn
txMCPkts65To127Octets = _TxMCPkts65To127Octets_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1, 9),
    _TxMCPkts65To127Octets_Type()
)
txMCPkts65To127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txMCPkts65To127Octets.setStatus("mandatory")
_TxMCPkts128To255Octets_Type = Counter32
_TxMCPkts128To255Octets_Object = MibTableColumn
txMCPkts128To255Octets = _TxMCPkts128To255Octets_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1, 10),
    _TxMCPkts128To255Octets_Type()
)
txMCPkts128To255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txMCPkts128To255Octets.setStatus("mandatory")
_TxMCPkts256To511Octets_Type = Counter32
_TxMCPkts256To511Octets_Object = MibTableColumn
txMCPkts256To511Octets = _TxMCPkts256To511Octets_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1, 11),
    _TxMCPkts256To511Octets_Type()
)
txMCPkts256To511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txMCPkts256To511Octets.setStatus("mandatory")
_TxMCPkts512To1023Octets_Type = Counter32
_TxMCPkts512To1023Octets_Object = MibTableColumn
txMCPkts512To1023Octets = _TxMCPkts512To1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1, 12),
    _TxMCPkts512To1023Octets_Type()
)
txMCPkts512To1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txMCPkts512To1023Octets.setStatus("mandatory")
_TxMCPkts1024To1518Octets_Type = Counter32
_TxMCPkts1024To1518Octets_Object = MibTableColumn
txMCPkts1024To1518Octets = _TxMCPkts1024To1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1, 13),
    _TxMCPkts1024To1518Octets_Type()
)
txMCPkts1024To1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txMCPkts1024To1518Octets.setStatus("mandatory")
_TxBCPkts64Octets_Type = Counter32
_TxBCPkts64Octets_Object = MibTableColumn
txBCPkts64Octets = _TxBCPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1, 14),
    _TxBCPkts64Octets_Type()
)
txBCPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txBCPkts64Octets.setStatus("mandatory")
_TxBCPkts65To127Octets_Type = Counter32
_TxBCPkts65To127Octets_Object = MibTableColumn
txBCPkts65To127Octets = _TxBCPkts65To127Octets_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1, 15),
    _TxBCPkts65To127Octets_Type()
)
txBCPkts65To127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txBCPkts65To127Octets.setStatus("mandatory")
_TxBCPkts128To255Octets_Type = Counter32
_TxBCPkts128To255Octets_Object = MibTableColumn
txBCPkts128To255Octets = _TxBCPkts128To255Octets_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1, 16),
    _TxBCPkts128To255Octets_Type()
)
txBCPkts128To255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txBCPkts128To255Octets.setStatus("mandatory")
_TxBCPkts256To511Octets_Type = Counter32
_TxBCPkts256To511Octets_Object = MibTableColumn
txBCPkts256To511Octets = _TxBCPkts256To511Octets_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1, 17),
    _TxBCPkts256To511Octets_Type()
)
txBCPkts256To511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txBCPkts256To511Octets.setStatus("mandatory")
_TxBCPkts512To1023Octets_Type = Counter32
_TxBCPkts512To1023Octets_Object = MibTableColumn
txBCPkts512To1023Octets = _TxBCPkts512To1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1, 18),
    _TxBCPkts512To1023Octets_Type()
)
txBCPkts512To1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txBCPkts512To1023Octets.setStatus("mandatory")
_TxBCPkts1024To1518Octets_Type = Counter32
_TxBCPkts1024To1518Octets_Object = MibTableColumn
txBCPkts1024To1518Octets = _TxBCPkts1024To1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1, 19),
    _TxBCPkts1024To1518Octets_Type()
)
txBCPkts1024To1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txBCPkts1024To1518Octets.setStatus("mandatory")
_TxDeffereds_Type = Counter32
_TxDeffereds_Object = MibTableColumn
txDeffereds = _TxDeffereds_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1, 20),
    _TxDeffereds_Type()
)
txDeffereds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txDeffereds.setStatus("mandatory")
_TxOctetsHis_Type = Counter32
_TxOctetsHis_Object = MibTableColumn
txOctetsHis = _TxOctetsHis_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1, 21),
    _TxOctetsHis_Type()
)
txOctetsHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txOctetsHis.setStatus("mandatory")
_TxOctetsLos_Type = Counter32
_TxOctetsLos_Object = MibTableColumn
txOctetsLos = _TxOctetsLos_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1, 22),
    _TxOctetsLos_Type()
)
txOctetsLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txOctetsLos.setStatus("mandatory")
_TxExcessiveDefferalsErrors_Type = Counter32
_TxExcessiveDefferalsErrors_Object = MibTableColumn
txExcessiveDefferalsErrors = _TxExcessiveDefferalsErrors_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1, 23),
    _TxExcessiveDefferalsErrors_Type()
)
txExcessiveDefferalsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txExcessiveDefferalsErrors.setStatus("mandatory")
_TxForwardedRxError_Type = Counter32
_TxForwardedRxError_Object = MibTableColumn
txForwardedRxError = _TxForwardedRxError_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1, 24),
    _TxForwardedRxError_Type()
)
txForwardedRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txForwardedRxError.setStatus("mandatory")
_TxNiaUnderRunDrops_Type = Counter32
_TxNiaUnderRunDrops_Object = MibTableColumn
txNiaUnderRunDrops = _TxNiaUnderRunDrops_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1, 25),
    _TxNiaUnderRunDrops_Type()
)
txNiaUnderRunDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txNiaUnderRunDrops.setStatus("mandatory")
_TxLinkDownEvents_Type = Counter32
_TxLinkDownEvents_Object = MibTableColumn
txLinkDownEvents = _TxLinkDownEvents_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1, 26),
    _TxLinkDownEvents_Type()
)
txLinkDownEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txLinkDownEvents.setStatus("mandatory")


class _TxAllCounterPackets_Type(OctetString):
    """Custom type txAllCounterPackets based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(127, 127),
    )


_TxAllCounterPackets_Type.__name__ = "OctetString"
_TxAllCounterPackets_Object = MibTableColumn
txAllCounterPackets = _TxAllCounterPackets_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1, 27),
    _TxAllCounterPackets_Type()
)
txAllCounterPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txAllCounterPackets.setStatus("mandatory")


class _TxAllCounterOthers_Type(OctetString):
    """Custom type txAllCounterOthers based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(127, 127),
    )


_TxAllCounterOthers_Type.__name__ = "OctetString"
_TxAllCounterOthers_Object = MibTableColumn
txAllCounterOthers = _TxAllCounterOthers_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 1, 1, 28),
    _TxAllCounterOthers_Type()
)
txAllCounterOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txAllCounterOthers.setStatus("mandatory")
_RxStatTable_Object = MibTable
rxStatTable = _RxStatTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2)
)
if mibBuilder.loadTexts:
    rxStatTable.setStatus("mandatory")
_RxStatEntry_Object = MibTableRow
rxStatEntry = _RxStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1)
)
rxStatEntry.setIndexNames(
    (0, "ETH-SWITCH-MIB", "rxStatIndex"),
)
if mibBuilder.loadTexts:
    rxStatEntry.setStatus("mandatory")
_RxStatIndex_Type = Integer32
_RxStatIndex_Object = MibTableColumn
rxStatIndex = _RxStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 1),
    _RxStatIndex_Type()
)
rxStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxStatIndex.setStatus("mandatory")
_RxUCPkts64OctetsLocals_Type = Counter32
_RxUCPkts64OctetsLocals_Object = MibTableColumn
rxUCPkts64OctetsLocals = _RxUCPkts64OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 2),
    _RxUCPkts64OctetsLocals_Type()
)
rxUCPkts64OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUCPkts64OctetsLocals.setStatus("mandatory")
_RxUCPkts64OctetsForwardeds_Type = Counter32
_RxUCPkts64OctetsForwardeds_Object = MibTableColumn
rxUCPkts64OctetsForwardeds = _RxUCPkts64OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 3),
    _RxUCPkts64OctetsForwardeds_Type()
)
rxUCPkts64OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUCPkts64OctetsForwardeds.setStatus("mandatory")
_RxUCPkts65To127OctetsLocals_Type = Counter32
_RxUCPkts65To127OctetsLocals_Object = MibTableColumn
rxUCPkts65To127OctetsLocals = _RxUCPkts65To127OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 4),
    _RxUCPkts65To127OctetsLocals_Type()
)
rxUCPkts65To127OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUCPkts65To127OctetsLocals.setStatus("mandatory")
_RxUCPkts65To127OctetsForwardeds_Type = Counter32
_RxUCPkts65To127OctetsForwardeds_Object = MibTableColumn
rxUCPkts65To127OctetsForwardeds = _RxUCPkts65To127OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 5),
    _RxUCPkts65To127OctetsForwardeds_Type()
)
rxUCPkts65To127OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUCPkts65To127OctetsForwardeds.setStatus("mandatory")
_RxUCPkts128To255OctetsLocals_Type = Counter32
_RxUCPkts128To255OctetsLocals_Object = MibTableColumn
rxUCPkts128To255OctetsLocals = _RxUCPkts128To255OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 6),
    _RxUCPkts128To255OctetsLocals_Type()
)
rxUCPkts128To255OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUCPkts128To255OctetsLocals.setStatus("mandatory")
_RxUCPkts128To255OctetsForwardeds_Type = Counter32
_RxUCPkts128To255OctetsForwardeds_Object = MibTableColumn
rxUCPkts128To255OctetsForwardeds = _RxUCPkts128To255OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 7),
    _RxUCPkts128To255OctetsForwardeds_Type()
)
rxUCPkts128To255OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUCPkts128To255OctetsForwardeds.setStatus("mandatory")
_RxUCPkts256To511OctetsLocals_Type = Counter32
_RxUCPkts256To511OctetsLocals_Object = MibTableColumn
rxUCPkts256To511OctetsLocals = _RxUCPkts256To511OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 8),
    _RxUCPkts256To511OctetsLocals_Type()
)
rxUCPkts256To511OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUCPkts256To511OctetsLocals.setStatus("mandatory")
_RxUCPkts256To511OctetsForwardeds_Type = Counter32
_RxUCPkts256To511OctetsForwardeds_Object = MibTableColumn
rxUCPkts256To511OctetsForwardeds = _RxUCPkts256To511OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 9),
    _RxUCPkts256To511OctetsForwardeds_Type()
)
rxUCPkts256To511OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUCPkts256To511OctetsForwardeds.setStatus("mandatory")
_RxUCPkts512To1023OctetsLocals_Type = Counter32
_RxUCPkts512To1023OctetsLocals_Object = MibTableColumn
rxUCPkts512To1023OctetsLocals = _RxUCPkts512To1023OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 10),
    _RxUCPkts512To1023OctetsLocals_Type()
)
rxUCPkts512To1023OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUCPkts512To1023OctetsLocals.setStatus("mandatory")
_RxUCPkts512To1023OctetsForwardeds_Type = Counter32
_RxUCPkts512To1023OctetsForwardeds_Object = MibTableColumn
rxUCPkts512To1023OctetsForwardeds = _RxUCPkts512To1023OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 11),
    _RxUCPkts512To1023OctetsForwardeds_Type()
)
rxUCPkts512To1023OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUCPkts512To1023OctetsForwardeds.setStatus("mandatory")
_RxUCPkts1024To1518OctetsLocals_Type = Counter32
_RxUCPkts1024To1518OctetsLocals_Object = MibTableColumn
rxUCPkts1024To1518OctetsLocals = _RxUCPkts1024To1518OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 12),
    _RxUCPkts1024To1518OctetsLocals_Type()
)
rxUCPkts1024To1518OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUCPkts1024To1518OctetsLocals.setStatus("mandatory")
_RxUCPkts1024To1518OctetsForwardeds_Type = Counter32
_RxUCPkts1024To1518OctetsForwardeds_Object = MibTableColumn
rxUCPkts1024To1518OctetsForwardeds = _RxUCPkts1024To1518OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 13),
    _RxUCPkts1024To1518OctetsForwardeds_Type()
)
rxUCPkts1024To1518OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUCPkts1024To1518OctetsForwardeds.setStatus("mandatory")
_RxShortErrors_Type = Counter32
_RxShortErrors_Object = MibTableColumn
rxShortErrors = _RxShortErrors_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 14),
    _RxShortErrors_Type()
)
rxShortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxShortErrors.setStatus("mandatory")
_RxRuntErrors_Type = Counter32
_RxRuntErrors_Object = MibTableColumn
rxRuntErrors = _RxRuntErrors_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 15),
    _RxRuntErrors_Type()
)
rxRuntErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxRuntErrors.setStatus("mandatory")
_RxDataRateMMErrors_Type = Counter32
_RxDataRateMMErrors_Object = MibTableColumn
rxDataRateMMErrors = _RxDataRateMMErrors_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 16),
    _RxDataRateMMErrors_Type()
)
rxDataRateMMErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxDataRateMMErrors.setStatus("mandatory")
_RxMCPkts64OctetsLocals_Type = Counter32
_RxMCPkts64OctetsLocals_Object = MibTableColumn
rxMCPkts64OctetsLocals = _RxMCPkts64OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 17),
    _RxMCPkts64OctetsLocals_Type()
)
rxMCPkts64OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxMCPkts64OctetsLocals.setStatus("mandatory")
_RxMCPkts64OctetsForwardeds_Type = Counter32
_RxMCPkts64OctetsForwardeds_Object = MibTableColumn
rxMCPkts64OctetsForwardeds = _RxMCPkts64OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 18),
    _RxMCPkts64OctetsForwardeds_Type()
)
rxMCPkts64OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxMCPkts64OctetsForwardeds.setStatus("mandatory")
_RxMCPkts65To127OctetsLocals_Type = Counter32
_RxMCPkts65To127OctetsLocals_Object = MibTableColumn
rxMCPkts65To127OctetsLocals = _RxMCPkts65To127OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 19),
    _RxMCPkts65To127OctetsLocals_Type()
)
rxMCPkts65To127OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxMCPkts65To127OctetsLocals.setStatus("mandatory")
_RxMCPkts65To127OctetsForwardeds_Type = Counter32
_RxMCPkts65To127OctetsForwardeds_Object = MibTableColumn
rxMCPkts65To127OctetsForwardeds = _RxMCPkts65To127OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 20),
    _RxMCPkts65To127OctetsForwardeds_Type()
)
rxMCPkts65To127OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxMCPkts65To127OctetsForwardeds.setStatus("mandatory")
_RxMCPkts128To255OctetsLocals_Type = Counter32
_RxMCPkts128To255OctetsLocals_Object = MibTableColumn
rxMCPkts128To255OctetsLocals = _RxMCPkts128To255OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 21),
    _RxMCPkts128To255OctetsLocals_Type()
)
rxMCPkts128To255OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxMCPkts128To255OctetsLocals.setStatus("mandatory")
_RxMCPkts128To255OctetsForwardeds_Type = Counter32
_RxMCPkts128To255OctetsForwardeds_Object = MibTableColumn
rxMCPkts128To255OctetsForwardeds = _RxMCPkts128To255OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 22),
    _RxMCPkts128To255OctetsForwardeds_Type()
)
rxMCPkts128To255OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxMCPkts128To255OctetsForwardeds.setStatus("mandatory")
_RxMCPkts256To511OctetsLocals_Type = Counter32
_RxMCPkts256To511OctetsLocals_Object = MibTableColumn
rxMCPkts256To511OctetsLocals = _RxMCPkts256To511OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 23),
    _RxMCPkts256To511OctetsLocals_Type()
)
rxMCPkts256To511OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxMCPkts256To511OctetsLocals.setStatus("mandatory")
_RxMCPkts256To511OctetsForwardeds_Type = Counter32
_RxMCPkts256To511OctetsForwardeds_Object = MibTableColumn
rxMCPkts256To511OctetsForwardeds = _RxMCPkts256To511OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 24),
    _RxMCPkts256To511OctetsForwardeds_Type()
)
rxMCPkts256To511OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxMCPkts256To511OctetsForwardeds.setStatus("mandatory")
_RxMCPkts512To1023OctetsLocals_Type = Counter32
_RxMCPkts512To1023OctetsLocals_Object = MibTableColumn
rxMCPkts512To1023OctetsLocals = _RxMCPkts512To1023OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 25),
    _RxMCPkts512To1023OctetsLocals_Type()
)
rxMCPkts512To1023OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxMCPkts512To1023OctetsLocals.setStatus("mandatory")
_RxMCPkts512To1023OctetsForwardeds_Type = Counter32
_RxMCPkts512To1023OctetsForwardeds_Object = MibTableColumn
rxMCPkts512To1023OctetsForwardeds = _RxMCPkts512To1023OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 26),
    _RxMCPkts512To1023OctetsForwardeds_Type()
)
rxMCPkts512To1023OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxMCPkts512To1023OctetsForwardeds.setStatus("mandatory")
_RxMCPkts1024To1518OctetsLocals_Type = Counter32
_RxMCPkts1024To1518OctetsLocals_Object = MibTableColumn
rxMCPkts1024To1518OctetsLocals = _RxMCPkts1024To1518OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 27),
    _RxMCPkts1024To1518OctetsLocals_Type()
)
rxMCPkts1024To1518OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxMCPkts1024To1518OctetsLocals.setStatus("mandatory")
_RxMCPkts1024To1518OctetsForwardeds_Type = Counter32
_RxMCPkts1024To1518OctetsForwardeds_Object = MibTableColumn
rxMCPkts1024To1518OctetsForwardeds = _RxMCPkts1024To1518OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 28),
    _RxMCPkts1024To1518OctetsForwardeds_Type()
)
rxMCPkts1024To1518OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxMCPkts1024To1518OctetsForwardeds.setStatus("mandatory")
_RxOctetsLocalHis_Type = Counter32
_RxOctetsLocalHis_Object = MibTableColumn
rxOctetsLocalHis = _RxOctetsLocalHis_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 29),
    _RxOctetsLocalHis_Type()
)
rxOctetsLocalHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxOctetsLocalHis.setStatus("mandatory")
_RxOctetsLocalLos_Type = Counter32
_RxOctetsLocalLos_Object = MibTableColumn
rxOctetsLocalLos = _RxOctetsLocalLos_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 30),
    _RxOctetsLocalLos_Type()
)
rxOctetsLocalLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxOctetsLocalLos.setStatus("mandatory")
_RxOctetsForwardedHis_Type = Counter32
_RxOctetsForwardedHis_Object = MibTableColumn
rxOctetsForwardedHis = _RxOctetsForwardedHis_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 31),
    _RxOctetsForwardedHis_Type()
)
rxOctetsForwardedHis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxOctetsForwardedHis.setStatus("mandatory")
_RxOctetsForwardedLos_Type = Counter32
_RxOctetsForwardedLos_Object = MibTableColumn
rxOctetsForwardedLos = _RxOctetsForwardedLos_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 32),
    _RxOctetsForwardedLos_Type()
)
rxOctetsForwardedLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxOctetsForwardedLos.setStatus("mandatory")
_RxBCPkts64OctetsLocals_Type = Counter32
_RxBCPkts64OctetsLocals_Object = MibTableColumn
rxBCPkts64OctetsLocals = _RxBCPkts64OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 33),
    _RxBCPkts64OctetsLocals_Type()
)
rxBCPkts64OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBCPkts64OctetsLocals.setStatus("mandatory")
_RxBCPkts64OctetsForwardeds_Type = Counter32
_RxBCPkts64OctetsForwardeds_Object = MibTableColumn
rxBCPkts64OctetsForwardeds = _RxBCPkts64OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 34),
    _RxBCPkts64OctetsForwardeds_Type()
)
rxBCPkts64OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBCPkts64OctetsForwardeds.setStatus("mandatory")
_RxBCPkts65To127OctetsLocals_Type = Counter32
_RxBCPkts65To127OctetsLocals_Object = MibTableColumn
rxBCPkts65To127OctetsLocals = _RxBCPkts65To127OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 35),
    _RxBCPkts65To127OctetsLocals_Type()
)
rxBCPkts65To127OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBCPkts65To127OctetsLocals.setStatus("mandatory")
_RxBCPkts65To127OctetsForwardeds_Type = Counter32
_RxBCPkts65To127OctetsForwardeds_Object = MibTableColumn
rxBCPkts65To127OctetsForwardeds = _RxBCPkts65To127OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 36),
    _RxBCPkts65To127OctetsForwardeds_Type()
)
rxBCPkts65To127OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBCPkts65To127OctetsForwardeds.setStatus("mandatory")
_RxBCPkts128To255OctetsLocals_Type = Counter32
_RxBCPkts128To255OctetsLocals_Object = MibTableColumn
rxBCPkts128To255OctetsLocals = _RxBCPkts128To255OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 37),
    _RxBCPkts128To255OctetsLocals_Type()
)
rxBCPkts128To255OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBCPkts128To255OctetsLocals.setStatus("mandatory")
_RxBCPkts128To255OctetsForwardeds_Type = Counter32
_RxBCPkts128To255OctetsForwardeds_Object = MibTableColumn
rxBCPkts128To255OctetsForwardeds = _RxBCPkts128To255OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 38),
    _RxBCPkts128To255OctetsForwardeds_Type()
)
rxBCPkts128To255OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBCPkts128To255OctetsForwardeds.setStatus("mandatory")
_RxBCPkts256To511OctetsLocals_Type = Counter32
_RxBCPkts256To511OctetsLocals_Object = MibTableColumn
rxBCPkts256To511OctetsLocals = _RxBCPkts256To511OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 39),
    _RxBCPkts256To511OctetsLocals_Type()
)
rxBCPkts256To511OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBCPkts256To511OctetsLocals.setStatus("mandatory")
_RxBCPkts256To511OctetsForwardeds_Type = Counter32
_RxBCPkts256To511OctetsForwardeds_Object = MibTableColumn
rxBCPkts256To511OctetsForwardeds = _RxBCPkts256To511OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 40),
    _RxBCPkts256To511OctetsForwardeds_Type()
)
rxBCPkts256To511OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBCPkts256To511OctetsForwardeds.setStatus("mandatory")
_RxBCPkts512To1023OctetsLocals_Type = Counter32
_RxBCPkts512To1023OctetsLocals_Object = MibTableColumn
rxBCPkts512To1023OctetsLocals = _RxBCPkts512To1023OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 41),
    _RxBCPkts512To1023OctetsLocals_Type()
)
rxBCPkts512To1023OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBCPkts512To1023OctetsLocals.setStatus("mandatory")
_RxBCPkts512To1023OctetsForwardeds_Type = Counter32
_RxBCPkts512To1023OctetsForwardeds_Object = MibTableColumn
rxBCPkts512To1023OctetsForwardeds = _RxBCPkts512To1023OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 42),
    _RxBCPkts512To1023OctetsForwardeds_Type()
)
rxBCPkts512To1023OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBCPkts512To1023OctetsForwardeds.setStatus("mandatory")
_RxBCPkts1024To1518OctetsLocals_Type = Counter32
_RxBCPkts1024To1518OctetsLocals_Object = MibTableColumn
rxBCPkts1024To1518OctetsLocals = _RxBCPkts1024To1518OctetsLocals_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 43),
    _RxBCPkts1024To1518OctetsLocals_Type()
)
rxBCPkts1024To1518OctetsLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBCPkts1024To1518OctetsLocals.setStatus("mandatory")
_RxBCPkts1024To1518OctetsForwardeds_Type = Counter32
_RxBCPkts1024To1518OctetsForwardeds_Object = MibTableColumn
rxBCPkts1024To1518OctetsForwardeds = _RxBCPkts1024To1518OctetsForwardeds_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 44),
    _RxBCPkts1024To1518OctetsForwardeds_Type()
)
rxBCPkts1024To1518OctetsForwardeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBCPkts1024To1518OctetsForwardeds.setStatus("mandatory")
_RxFilterMACUnexp2ndPortDrops_Type = Counter32
_RxFilterMACUnexp2ndPortDrops_Object = MibTableColumn
rxFilterMACUnexp2ndPortDrops = _RxFilterMACUnexp2ndPortDrops_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 45),
    _RxFilterMACUnexp2ndPortDrops_Type()
)
rxFilterMACUnexp2ndPortDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFilterMACUnexp2ndPortDrops.setStatus("mandatory")
_RxFilterIllegalMACDrops_Type = Counter32
_RxFilterIllegalMACDrops_Object = MibTableColumn
rxFilterIllegalMACDrops = _RxFilterIllegalMACDrops_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 46),
    _RxFilterIllegalMACDrops_Type()
)
rxFilterIllegalMACDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFilterIllegalMACDrops.setStatus("mandatory")
_RxFlowCtrlCollCounter_Type = Counter32
_RxFlowCtrlCollCounter_Object = MibTableColumn
rxFlowCtrlCollCounter = _RxFlowCtrlCollCounter_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 47),
    _RxFlowCtrlCollCounter_Type()
)
rxFlowCtrlCollCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFlowCtrlCollCounter.setStatus("mandatory")
_RxVeryLongErrors_Type = Counter32
_RxVeryLongErrors_Object = MibTableColumn
rxVeryLongErrors = _RxVeryLongErrors_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 48),
    _RxVeryLongErrors_Type()
)
rxVeryLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxVeryLongErrors.setStatus("mandatory")
_RxLongErrors_Type = Counter32
_RxLongErrors_Object = MibTableColumn
rxLongErrors = _RxLongErrors_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 49),
    _RxLongErrors_Type()
)
rxLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxLongErrors.setStatus("mandatory")
_RxPiaOutOfPoolsDrop_Type = Counter32
_RxPiaOutOfPoolsDrop_Object = MibTableColumn
rxPiaOutOfPoolsDrop = _RxPiaOutOfPoolsDrop_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 50),
    _RxPiaOutOfPoolsDrop_Type()
)
rxPiaOutOfPoolsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPiaOutOfPoolsDrop.setStatus("mandatory")
_RxManchesterCodeViolationErrors_Type = Counter32
_RxManchesterCodeViolationErrors_Object = MibTableColumn
rxManchesterCodeViolationErrors = _RxManchesterCodeViolationErrors_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 51),
    _RxManchesterCodeViolationErrors_Type()
)
rxManchesterCodeViolationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxManchesterCodeViolationErrors.setStatus("mandatory")
_RxRxJabbers_Type = Counter32
_RxRxJabbers_Object = MibTableColumn
rxRxJabbers = _RxRxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 52),
    _RxRxJabbers_Type()
)
rxRxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxRxJabbers.setStatus("mandatory")
_RxNiaOverRunDrops_Type = Counter32
_RxNiaOverRunDrops_Object = MibTableColumn
rxNiaOverRunDrops = _RxNiaOverRunDrops_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 53),
    _RxNiaOverRunDrops_Type()
)
rxNiaOverRunDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxNiaOverRunDrops.setStatus("mandatory")


class _RxAllCounterPackets_Type(OctetString):
    """Custom type rxAllCounterPackets based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(164, 164),
    )


_RxAllCounterPackets_Type.__name__ = "OctetString"
_RxAllCounterPackets_Object = MibTableColumn
rxAllCounterPackets = _RxAllCounterPackets_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 54),
    _RxAllCounterPackets_Type()
)
rxAllCounterPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxAllCounterPackets.setStatus("mandatory")


class _RxAllCounterOthers_Type(OctetString):
    """Custom type rxAllCounterOthers based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(60, 60),
    )


_RxAllCounterOthers_Type.__name__ = "OctetString"
_RxAllCounterOthers_Object = MibTableColumn
rxAllCounterOthers = _RxAllCounterOthers_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 2, 1, 55),
    _RxAllCounterOthers_Type()
)
rxAllCounterOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxAllCounterOthers.setStatus("mandatory")
_TotalRxTxPackets_Type = OctetString
_TotalRxTxPackets_Object = MibScalar
totalRxTxPackets = _TotalRxTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 3),
    _TotalRxTxPackets_Type()
)
totalRxTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalRxTxPackets.setStatus("mandatory")
_TotalCollisions_Type = OctetString
_TotalCollisions_Object = MibScalar
totalCollisions = _TotalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 4, 4),
    _TotalCollisions_Type()
)
totalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalCollisions.setStatus("mandatory")
_AdaptiveForwardMode_ObjectIdentity = ObjectIdentity
adaptiveForwardMode = _AdaptiveForwardMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 39, 5)
)
_AdaptiveForwardModeSampleTime_Type = Integer32
_AdaptiveForwardModeSampleTime_Object = MibScalar
adaptiveForwardModeSampleTime = _AdaptiveForwardModeSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 5, 1),
    _AdaptiveForwardModeSampleTime_Type()
)
adaptiveForwardModeSampleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adaptiveForwardModeSampleTime.setStatus("mandatory")
_AdaptiveForwardModeRuntsOffset_Type = Integer32
_AdaptiveForwardModeRuntsOffset_Object = MibScalar
adaptiveForwardModeRuntsOffset = _AdaptiveForwardModeRuntsOffset_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 5, 2),
    _AdaptiveForwardModeRuntsOffset_Type()
)
adaptiveForwardModeRuntsOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adaptiveForwardModeRuntsOffset.setStatus("mandatory")
_AdaptiveForwardModeRuntsRange_Type = Integer32
_AdaptiveForwardModeRuntsRange_Object = MibScalar
adaptiveForwardModeRuntsRange = _AdaptiveForwardModeRuntsRange_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 5, 3),
    _AdaptiveForwardModeRuntsRange_Type()
)
adaptiveForwardModeRuntsRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adaptiveForwardModeRuntsRange.setStatus("mandatory")
_AdaptiveForwardModeCrcsOffset_Type = Integer32
_AdaptiveForwardModeCrcsOffset_Object = MibScalar
adaptiveForwardModeCrcsOffset = _AdaptiveForwardModeCrcsOffset_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 5, 4),
    _AdaptiveForwardModeCrcsOffset_Type()
)
adaptiveForwardModeCrcsOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adaptiveForwardModeCrcsOffset.setStatus("mandatory")
_AdaptiveForwardModeCrcsRange_Type = Integer32
_AdaptiveForwardModeCrcsRange_Object = MibScalar
adaptiveForwardModeCrcsRange = _AdaptiveForwardModeCrcsRange_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 5, 5),
    _AdaptiveForwardModeCrcsRange_Type()
)
adaptiveForwardModeCrcsRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adaptiveForwardModeCrcsRange.setStatus("mandatory")
_ChipSets_ObjectIdentity = ObjectIdentity
chipSets = _ChipSets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 39, 6)
)
_ChipSetNIA10_ObjectIdentity = ObjectIdentity
chipSetNIA10 = _ChipSetNIA10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 39, 6, 1)
)
_ChipSetNIA100_ObjectIdentity = ObjectIdentity
chipSetNIA100 = _ChipSetNIA100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 39, 6, 2)
)
_Cards_ObjectIdentity = ObjectIdentity
cards = _Cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 39, 7)
)
_CardTable_Object = MibTable
cardTable = _CardTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 7, 1)
)
if mibBuilder.loadTexts:
    cardTable.setStatus("mandatory")
_CardEntry_Object = MibTableRow
cardEntry = _CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 7, 1, 1)
)
cardEntry.setIndexNames(
    (0, "ETH-SWITCH-MIB", "cardNumber"),
)
if mibBuilder.loadTexts:
    cardEntry.setStatus("mandatory")
_CardNumber_Type = Integer32
_CardNumber_Object = MibTableColumn
cardNumber = _CardNumber_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 7, 1, 1, 1),
    _CardNumber_Type()
)
cardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardNumber.setStatus("mandatory")
_CardId_Type = ProductIds
_CardId_Object = MibTableColumn
cardId = _CardId_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 7, 1, 1, 2),
    _CardId_Type()
)
cardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardId.setStatus("mandatory")
_CardFirstPort_Type = Integer32
_CardFirstPort_Object = MibTableColumn
cardFirstPort = _CardFirstPort_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 7, 1, 1, 3),
    _CardFirstPort_Type()
)
cardFirstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardFirstPort.setStatus("mandatory")
_CardMaxPims_Type = Integer32
_CardMaxPims_Object = MibTableColumn
cardMaxPims = _CardMaxPims_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 7, 1, 1, 4),
    _CardMaxPims_Type()
)
cardMaxPims.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardMaxPims.setStatus("mandatory")
_PimTable_Object = MibTable
pimTable = _PimTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 7, 2)
)
if mibBuilder.loadTexts:
    pimTable.setStatus("mandatory")
_PimEntry_Object = MibTableRow
pimEntry = _PimEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 7, 2, 1)
)
pimEntry.setIndexNames(
    (0, "ETH-SWITCH-MIB", "pimCardNumber"),
    (0, "ETH-SWITCH-MIB", "pimNumber"),
)
if mibBuilder.loadTexts:
    pimEntry.setStatus("mandatory")
_PimCardNumber_Type = Integer32
_PimCardNumber_Object = MibTableColumn
pimCardNumber = _PimCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 7, 2, 1, 1),
    _PimCardNumber_Type()
)
pimCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimCardNumber.setStatus("mandatory")
_PimNumber_Type = Integer32
_PimNumber_Object = MibTableColumn
pimNumber = _PimNumber_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 7, 2, 1, 2),
    _PimNumber_Type()
)
pimNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimNumber.setStatus("mandatory")
_PimId_Type = ProductIds
_PimId_Object = MibTableColumn
pimId = _PimId_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 7, 2, 1, 3),
    _PimId_Type()
)
pimId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimId.setStatus("mandatory")
_PimFirstPort_Type = Integer32
_PimFirstPort_Object = MibTableColumn
pimFirstPort = _PimFirstPort_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 7, 2, 1, 4),
    _PimFirstPort_Type()
)
pimFirstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimFirstPort.setStatus("mandatory")
_PimNumberOfPorts_Type = Integer32
_PimNumberOfPorts_Object = MibTableColumn
pimNumberOfPorts = _PimNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 208, 39, 7, 2, 1, 5),
    _PimNumberOfPorts_Type()
)
pimNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimNumberOfPorts.setStatus("mandatory")

# Managed Objects groups


# Notification objects

ethSwitchPermVioEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 208, 39, 0, 1)
)
ethSwitchPermVioEvent.setObjects(
    ("ETH-SWITCH-MIB", "portIfIndex")
)
if mibBuilder.loadTexts:
    ethSwitchPermVioEvent.setStatus(
        ""
    )

ethSwitchOnlyOneMACEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 208, 39, 0, 2)
)
ethSwitchOnlyOneMACEvent.setObjects(
    ("ETH-SWITCH-MIB", "portIfIndex")
)
if mibBuilder.loadTexts:
    ethSwitchOnlyOneMACEvent.setStatus(
        ""
    )

ethSwitchMACVioEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 208, 39, 0, 3)
)
ethSwitchMACVioEvent.setObjects(
    ("ETH-SWITCH-MIB", "portIfIndex")
)
if mibBuilder.loadTexts:
    ethSwitchMACVioEvent.setStatus(
        ""
    )

ethSwitchAdaptiveForwEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 208, 39, 0, 4)
)
ethSwitchAdaptiveForwEvent.setObjects(
      *(("ETH-SWITCH-MIB", "portIfIndex"),
        ("ETH-SWITCH-MIB", "portIfSwitchMode"),
        ("ETH-SWITCH-MIB", "portIfSwitchMode"))
)
if mibBuilder.loadTexts:
    ethSwitchAdaptiveForwEvent.setStatus(
        ""
    )

ethSwitchMACFilterVioEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 208, 39, 0, 5)
)
ethSwitchMACFilterVioEvent.setObjects(
    ("ETH-SWITCH-MIB", "portIfIndex")
)
if mibBuilder.loadTexts:
    ethSwitchMACFilterVioEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ETH-SWITCH-MIB",
    **{"ProductIds": ProductIds,
       "ethSwitch": ethSwitch,
       "ethSwitchPermVioEvent": ethSwitchPermVioEvent,
       "ethSwitchOnlyOneMACEvent": ethSwitchOnlyOneMACEvent,
       "ethSwitchMACVioEvent": ethSwitchMACVioEvent,
       "ethSwitchAdaptiveForwEvent": ethSwitchAdaptiveForwEvent,
       "ethSwitchMACFilterVioEvent": ethSwitchMACFilterVioEvent,
       "control": control,
       "scSegments": scSegments,
       "defaultSwitchMode": defaultSwitchMode,
       "defaultThrottleBackMode": defaultThrottleBackMode,
       "networkPort": networkPort,
       "module": module,
       "expansionModule": expansionModule,
       "ports": ports,
       "portLastChange": portLastChange,
       "portTable": portTable,
       "portEntry": portEntry,
       "portNumber": portNumber,
       "portInterfaceIndex": portInterfaceIndex,
       "portLED": portLED,
       "portState": portState,
       "portCardNumber": portCardNumber,
       "portPimNumber": portPimNumber,
       "portPimPortNumber": portPimPortNumber,
       "portIfTable": portIfTable,
       "portIfEntry": portIfEntry,
       "portIfIndex": portIfIndex,
       "portIfDescr": portIfDescr,
       "portIfLocation": portIfLocation,
       "portIfSwitchMode": portIfSwitchMode,
       "portIfDuplex": portIfDuplex,
       "portIfThrottleBack": portIfThrottleBack,
       "portIfType": portIfType,
       "portIfDuplexSupported": portIfDuplexSupported,
       "portIfSpeedSupported": portIfSpeedSupported,
       "portIfSpeedAndDuplex": portIfSpeedAndDuplex,
       "statistic": statistic,
       "txStatTable": txStatTable,
       "txStatEntry": txStatEntry,
       "txStatIndex": txStatIndex,
       "txUCPkts64Octets": txUCPkts64Octets,
       "txUCPkts65To127Octets": txUCPkts65To127Octets,
       "txUCPkts128To255Octets": txUCPkts128To255Octets,
       "txUCPkts256To511Octets": txUCPkts256To511Octets,
       "txUCPkts512To1023Octets": txUCPkts512To1023Octets,
       "txUCPkts1024To1518Octets": txUCPkts1024To1518Octets,
       "txMCPkts64Octets": txMCPkts64Octets,
       "txMCPkts65To127Octets": txMCPkts65To127Octets,
       "txMCPkts128To255Octets": txMCPkts128To255Octets,
       "txMCPkts256To511Octets": txMCPkts256To511Octets,
       "txMCPkts512To1023Octets": txMCPkts512To1023Octets,
       "txMCPkts1024To1518Octets": txMCPkts1024To1518Octets,
       "txBCPkts64Octets": txBCPkts64Octets,
       "txBCPkts65To127Octets": txBCPkts65To127Octets,
       "txBCPkts128To255Octets": txBCPkts128To255Octets,
       "txBCPkts256To511Octets": txBCPkts256To511Octets,
       "txBCPkts512To1023Octets": txBCPkts512To1023Octets,
       "txBCPkts1024To1518Octets": txBCPkts1024To1518Octets,
       "txDeffereds": txDeffereds,
       "txOctetsHis": txOctetsHis,
       "txOctetsLos": txOctetsLos,
       "txExcessiveDefferalsErrors": txExcessiveDefferalsErrors,
       "txForwardedRxError": txForwardedRxError,
       "txNiaUnderRunDrops": txNiaUnderRunDrops,
       "txLinkDownEvents": txLinkDownEvents,
       "txAllCounterPackets": txAllCounterPackets,
       "txAllCounterOthers": txAllCounterOthers,
       "rxStatTable": rxStatTable,
       "rxStatEntry": rxStatEntry,
       "rxStatIndex": rxStatIndex,
       "rxUCPkts64OctetsLocals": rxUCPkts64OctetsLocals,
       "rxUCPkts64OctetsForwardeds": rxUCPkts64OctetsForwardeds,
       "rxUCPkts65To127OctetsLocals": rxUCPkts65To127OctetsLocals,
       "rxUCPkts65To127OctetsForwardeds": rxUCPkts65To127OctetsForwardeds,
       "rxUCPkts128To255OctetsLocals": rxUCPkts128To255OctetsLocals,
       "rxUCPkts128To255OctetsForwardeds": rxUCPkts128To255OctetsForwardeds,
       "rxUCPkts256To511OctetsLocals": rxUCPkts256To511OctetsLocals,
       "rxUCPkts256To511OctetsForwardeds": rxUCPkts256To511OctetsForwardeds,
       "rxUCPkts512To1023OctetsLocals": rxUCPkts512To1023OctetsLocals,
       "rxUCPkts512To1023OctetsForwardeds": rxUCPkts512To1023OctetsForwardeds,
       "rxUCPkts1024To1518OctetsLocals": rxUCPkts1024To1518OctetsLocals,
       "rxUCPkts1024To1518OctetsForwardeds": rxUCPkts1024To1518OctetsForwardeds,
       "rxShortErrors": rxShortErrors,
       "rxRuntErrors": rxRuntErrors,
       "rxDataRateMMErrors": rxDataRateMMErrors,
       "rxMCPkts64OctetsLocals": rxMCPkts64OctetsLocals,
       "rxMCPkts64OctetsForwardeds": rxMCPkts64OctetsForwardeds,
       "rxMCPkts65To127OctetsLocals": rxMCPkts65To127OctetsLocals,
       "rxMCPkts65To127OctetsForwardeds": rxMCPkts65To127OctetsForwardeds,
       "rxMCPkts128To255OctetsLocals": rxMCPkts128To255OctetsLocals,
       "rxMCPkts128To255OctetsForwardeds": rxMCPkts128To255OctetsForwardeds,
       "rxMCPkts256To511OctetsLocals": rxMCPkts256To511OctetsLocals,
       "rxMCPkts256To511OctetsForwardeds": rxMCPkts256To511OctetsForwardeds,
       "rxMCPkts512To1023OctetsLocals": rxMCPkts512To1023OctetsLocals,
       "rxMCPkts512To1023OctetsForwardeds": rxMCPkts512To1023OctetsForwardeds,
       "rxMCPkts1024To1518OctetsLocals": rxMCPkts1024To1518OctetsLocals,
       "rxMCPkts1024To1518OctetsForwardeds": rxMCPkts1024To1518OctetsForwardeds,
       "rxOctetsLocalHis": rxOctetsLocalHis,
       "rxOctetsLocalLos": rxOctetsLocalLos,
       "rxOctetsForwardedHis": rxOctetsForwardedHis,
       "rxOctetsForwardedLos": rxOctetsForwardedLos,
       "rxBCPkts64OctetsLocals": rxBCPkts64OctetsLocals,
       "rxBCPkts64OctetsForwardeds": rxBCPkts64OctetsForwardeds,
       "rxBCPkts65To127OctetsLocals": rxBCPkts65To127OctetsLocals,
       "rxBCPkts65To127OctetsForwardeds": rxBCPkts65To127OctetsForwardeds,
       "rxBCPkts128To255OctetsLocals": rxBCPkts128To255OctetsLocals,
       "rxBCPkts128To255OctetsForwardeds": rxBCPkts128To255OctetsForwardeds,
       "rxBCPkts256To511OctetsLocals": rxBCPkts256To511OctetsLocals,
       "rxBCPkts256To511OctetsForwardeds": rxBCPkts256To511OctetsForwardeds,
       "rxBCPkts512To1023OctetsLocals": rxBCPkts512To1023OctetsLocals,
       "rxBCPkts512To1023OctetsForwardeds": rxBCPkts512To1023OctetsForwardeds,
       "rxBCPkts1024To1518OctetsLocals": rxBCPkts1024To1518OctetsLocals,
       "rxBCPkts1024To1518OctetsForwardeds": rxBCPkts1024To1518OctetsForwardeds,
       "rxFilterMACUnexp2ndPortDrops": rxFilterMACUnexp2ndPortDrops,
       "rxFilterIllegalMACDrops": rxFilterIllegalMACDrops,
       "rxFlowCtrlCollCounter": rxFlowCtrlCollCounter,
       "rxVeryLongErrors": rxVeryLongErrors,
       "rxLongErrors": rxLongErrors,
       "rxPiaOutOfPoolsDrop": rxPiaOutOfPoolsDrop,
       "rxManchesterCodeViolationErrors": rxManchesterCodeViolationErrors,
       "rxRxJabbers": rxRxJabbers,
       "rxNiaOverRunDrops": rxNiaOverRunDrops,
       "rxAllCounterPackets": rxAllCounterPackets,
       "rxAllCounterOthers": rxAllCounterOthers,
       "totalRxTxPackets": totalRxTxPackets,
       "totalCollisions": totalCollisions,
       "adaptiveForwardMode": adaptiveForwardMode,
       "adaptiveForwardModeSampleTime": adaptiveForwardModeSampleTime,
       "adaptiveForwardModeRuntsOffset": adaptiveForwardModeRuntsOffset,
       "adaptiveForwardModeRuntsRange": adaptiveForwardModeRuntsRange,
       "adaptiveForwardModeCrcsOffset": adaptiveForwardModeCrcsOffset,
       "adaptiveForwardModeCrcsRange": adaptiveForwardModeCrcsRange,
       "chipSets": chipSets,
       "chipSetNIA10": chipSetNIA10,
       "chipSetNIA100": chipSetNIA100,
       "cards": cards,
       "cardTable": cardTable,
       "cardEntry": cardEntry,
       "cardNumber": cardNumber,
       "cardId": cardId,
       "cardFirstPort": cardFirstPort,
       "cardMaxPims": cardMaxPims,
       "pimTable": pimTable,
       "pimEntry": pimEntry,
       "pimCardNumber": pimCardNumber,
       "pimNumber": pimNumber,
       "pimId": pimId,
       "pimFirstPort": pimFirstPort,
       "pimNumberOfPorts": pimNumberOfPorts}
)
