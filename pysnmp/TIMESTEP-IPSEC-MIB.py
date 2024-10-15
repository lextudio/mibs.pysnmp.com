# SNMP MIB module (TIMESTEP-IPSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMESTEP-IPSEC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:50 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(timestep,) = mibBuilder.importSymbols(
    "TIMESTEP-MIB",
    "timestep")


# MODULE-IDENTITY

ipsecMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1022, 10)
)
ipsecMIB.setRevisions(
        ("1970-01-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpsecMIBObjects_ObjectIdentity = ObjectIdentity
ipsecMIBObjects = _IpsecMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1)
)
_Ipsec_ObjectIdentity = ObjectIdentity
ipsec = _Ipsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1)
)
_IpsecIkeSaTable_Object = MibTable
ipsecIkeSaTable = _IpsecIkeSaTable_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ipsecIkeSaTable.setStatus("current")
_IpsecIkeSaEntry_Object = MibTableRow
ipsecIkeSaEntry = _IpsecIkeSaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1)
)
ipsecIkeSaEntry.setIndexNames(
    (0, "TIMESTEP-IPSEC-MIB", "ipsecIkeSaIndex"),
)
if mibBuilder.loadTexts:
    ipsecIkeSaEntry.setStatus("current")


class _IpsecIkeSaIndex_Type(Integer32):
    """Custom type ipsecIkeSaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_IpsecIkeSaIndex_Type.__name__ = "Integer32"
_IpsecIkeSaIndex_Object = MibTableColumn
ipsecIkeSaIndex = _IpsecIkeSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 1),
    _IpsecIkeSaIndex_Type()
)
ipsecIkeSaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaIndex.setStatus("current")
_IpsecIkeSaPeerIpAddress_Type = IpAddress
_IpsecIkeSaPeerIpAddress_Object = MibTableColumn
ipsecIkeSaPeerIpAddress = _IpsecIkeSaPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 2),
    _IpsecIkeSaPeerIpAddress_Type()
)
ipsecIkeSaPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaPeerIpAddress.setStatus("current")


class _IpsecIkeSaPeerPortNumber_Type(Integer32):
    """Custom type ipsecIkeSaPeerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecIkeSaPeerPortNumber_Type.__name__ = "Integer32"
_IpsecIkeSaPeerPortNumber_Object = MibTableColumn
ipsecIkeSaPeerPortNumber = _IpsecIkeSaPeerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 3),
    _IpsecIkeSaPeerPortNumber_Type()
)
ipsecIkeSaPeerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaPeerPortNumber.setStatus("current")


class _IpsecIkeSaAuthMethod_Type(Integer32):
    """Custom type ipsecIkeSaAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecIkeSaAuthMethod_Type.__name__ = "Integer32"
_IpsecIkeSaAuthMethod_Object = MibTableColumn
ipsecIkeSaAuthMethod = _IpsecIkeSaAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 4),
    _IpsecIkeSaAuthMethod_Type()
)
ipsecIkeSaAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaAuthMethod.setStatus("current")


class _IpsecIkeSaPeerIdType_Type(Integer32):
    """Custom type ipsecIkeSaPeerIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IpsecIkeSaPeerIdType_Type.__name__ = "Integer32"
_IpsecIkeSaPeerIdType_Object = MibTableColumn
ipsecIkeSaPeerIdType = _IpsecIkeSaPeerIdType_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 5),
    _IpsecIkeSaPeerIdType_Type()
)
ipsecIkeSaPeerIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaPeerIdType.setStatus("current")


class _IpsecIkeSaPeerId_Type(OctetString):
    """Custom type ipsecIkeSaPeerId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 511),
    )


_IpsecIkeSaPeerId_Type.__name__ = "OctetString"
_IpsecIkeSaPeerId_Object = MibTableColumn
ipsecIkeSaPeerId = _IpsecIkeSaPeerId_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 6),
    _IpsecIkeSaPeerId_Type()
)
ipsecIkeSaPeerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaPeerId.setStatus("current")


class _IpsecIkeSaPeerCertSerialNum_Type(OctetString):
    """Custom type ipsecIkeSaPeerCertSerialNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IpsecIkeSaPeerCertSerialNum_Type.__name__ = "OctetString"
_IpsecIkeSaPeerCertSerialNum_Object = MibTableColumn
ipsecIkeSaPeerCertSerialNum = _IpsecIkeSaPeerCertSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 7),
    _IpsecIkeSaPeerCertSerialNum_Type()
)
ipsecIkeSaPeerCertSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaPeerCertSerialNum.setStatus("current")


class _IpsecIkeSaPeerCertIssuer_Type(OctetString):
    """Custom type ipsecIkeSaPeerCertIssuer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 511),
    )


_IpsecIkeSaPeerCertIssuer_Type.__name__ = "OctetString"
_IpsecIkeSaPeerCertIssuer_Object = MibTableColumn
ipsecIkeSaPeerCertIssuer = _IpsecIkeSaPeerCertIssuer_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 8),
    _IpsecIkeSaPeerCertIssuer_Type()
)
ipsecIkeSaPeerCertIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaPeerCertIssuer.setStatus("current")


class _IpsecIkeSaType_Type(Integer32):
    """Custom type ipsecIkeSaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permanent", 2),
          ("transient", 1))
    )


_IpsecIkeSaType_Type.__name__ = "Integer32"
_IpsecIkeSaType_Object = MibTableColumn
ipsecIkeSaType = _IpsecIkeSaType_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 9),
    _IpsecIkeSaType_Type()
)
ipsecIkeSaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaType.setStatus("current")


class _IpsecIkeSaStatus_Type(Integer32):
    """Custom type ipsecIkeSaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1),
          ("neverTried", 0))
    )


_IpsecIkeSaStatus_Type.__name__ = "Integer32"
_IpsecIkeSaStatus_Object = MibTableColumn
ipsecIkeSaStatus = _IpsecIkeSaStatus_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 10),
    _IpsecIkeSaStatus_Type()
)
ipsecIkeSaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaStatus.setStatus("current")


class _IpsecIkeSaEncAlg_Type(Integer32):
    """Custom type ipsecIkeSaEncAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecIkeSaEncAlg_Type.__name__ = "Integer32"
_IpsecIkeSaEncAlg_Object = MibTableColumn
ipsecIkeSaEncAlg = _IpsecIkeSaEncAlg_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 11),
    _IpsecIkeSaEncAlg_Type()
)
ipsecIkeSaEncAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaEncAlg.setStatus("current")
_IpsecIkeSaEncKeyLength_Type = Integer32
_IpsecIkeSaEncKeyLength_Object = MibTableColumn
ipsecIkeSaEncKeyLength = _IpsecIkeSaEncKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 12),
    _IpsecIkeSaEncKeyLength_Type()
)
ipsecIkeSaEncKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaEncKeyLength.setStatus("current")


class _IpsecIkeSaHashAlg_Type(Integer32):
    """Custom type ipsecIkeSaHashAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecIkeSaHashAlg_Type.__name__ = "Integer32"
_IpsecIkeSaHashAlg_Object = MibTableColumn
ipsecIkeSaHashAlg = _IpsecIkeSaHashAlg_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 13),
    _IpsecIkeSaHashAlg_Type()
)
ipsecIkeSaHashAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaHashAlg.setStatus("current")


class _IpsecIkeSaDifHelGroupDesc_Type(Integer32):
    """Custom type ipsecIkeSaDifHelGroupDesc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecIkeSaDifHelGroupDesc_Type.__name__ = "Integer32"
_IpsecIkeSaDifHelGroupDesc_Object = MibTableColumn
ipsecIkeSaDifHelGroupDesc = _IpsecIkeSaDifHelGroupDesc_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 14),
    _IpsecIkeSaDifHelGroupDesc_Type()
)
ipsecIkeSaDifHelGroupDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaDifHelGroupDesc.setStatus("current")


class _IpsecIkeSaDifHelGroupType_Type(Integer32):
    """Custom type ipsecIkeSaDifHelGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecIkeSaDifHelGroupType_Type.__name__ = "Integer32"
_IpsecIkeSaDifHelGroupType_Object = MibTableColumn
ipsecIkeSaDifHelGroupType = _IpsecIkeSaDifHelGroupType_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 15),
    _IpsecIkeSaDifHelGroupType_Type()
)
ipsecIkeSaDifHelGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaDifHelGroupType.setStatus("current")
_IpsecIkeSaDifHelFieldSize_Type = Integer32
_IpsecIkeSaDifHelFieldSize_Object = MibTableColumn
ipsecIkeSaDifHelFieldSize = _IpsecIkeSaDifHelFieldSize_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 16),
    _IpsecIkeSaDifHelFieldSize_Type()
)
ipsecIkeSaDifHelFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaDifHelFieldSize.setStatus("current")


class _IpsecIkeSaPRF_Type(Integer32):
    """Custom type ipsecIkeSaPRF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecIkeSaPRF_Type.__name__ = "Integer32"
_IpsecIkeSaPRF_Object = MibTableColumn
ipsecIkeSaPRF = _IpsecIkeSaPRF_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 17),
    _IpsecIkeSaPRF_Type()
)
ipsecIkeSaPRF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaPRF.setStatus("current")
_IpsecIkeSaPFS_Type = TruthValue
_IpsecIkeSaPFS_Object = MibTableColumn
ipsecIkeSaPFS = _IpsecIkeSaPFS_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 18),
    _IpsecIkeSaPFS_Type()
)
ipsecIkeSaPFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaPFS.setStatus("current")


class _IpsecIkeSaInitiatorCookie_Type(OctetString):
    """Custom type ipsecIkeSaInitiatorCookie based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_IpsecIkeSaInitiatorCookie_Type.__name__ = "OctetString"
_IpsecIkeSaInitiatorCookie_Object = MibTableColumn
ipsecIkeSaInitiatorCookie = _IpsecIkeSaInitiatorCookie_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 19),
    _IpsecIkeSaInitiatorCookie_Type()
)
ipsecIkeSaInitiatorCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaInitiatorCookie.setStatus("current")


class _IpsecIkeSaResponderCookie_Type(OctetString):
    """Custom type ipsecIkeSaResponderCookie based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_IpsecIkeSaResponderCookie_Type.__name__ = "OctetString"
_IpsecIkeSaResponderCookie_Object = MibTableColumn
ipsecIkeSaResponderCookie = _IpsecIkeSaResponderCookie_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 20),
    _IpsecIkeSaResponderCookie_Type()
)
ipsecIkeSaResponderCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaResponderCookie.setStatus("current")
_IpsecIkeSaTimeStart_Type = DateAndTime
_IpsecIkeSaTimeStart_Object = MibTableColumn
ipsecIkeSaTimeStart = _IpsecIkeSaTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 21),
    _IpsecIkeSaTimeStart_Type()
)
ipsecIkeSaTimeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaTimeStart.setStatus("current")
_IpsecIkeSaTimeLimit_Type = Gauge32
_IpsecIkeSaTimeLimit_Object = MibTableColumn
ipsecIkeSaTimeLimit = _IpsecIkeSaTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 22),
    _IpsecIkeSaTimeLimit_Type()
)
ipsecIkeSaTimeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaTimeLimit.setStatus("current")
_IpsecIkeSaTrafficLimit_Type = Gauge32
_IpsecIkeSaTrafficLimit_Object = MibTableColumn
ipsecIkeSaTrafficLimit = _IpsecIkeSaTrafficLimit_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 23),
    _IpsecIkeSaTrafficLimit_Type()
)
ipsecIkeSaTrafficLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaTrafficLimit.setStatus("current")
_IpsecIkeSaInboundTraffic_Type = Counter32
_IpsecIkeSaInboundTraffic_Object = MibTableColumn
ipsecIkeSaInboundTraffic = _IpsecIkeSaInboundTraffic_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 24),
    _IpsecIkeSaInboundTraffic_Type()
)
ipsecIkeSaInboundTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaInboundTraffic.setStatus("current")
_IpsecIkeSaOutboundTraffic_Type = Counter32
_IpsecIkeSaOutboundTraffic_Object = MibTableColumn
ipsecIkeSaOutboundTraffic = _IpsecIkeSaOutboundTraffic_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 25),
    _IpsecIkeSaOutboundTraffic_Type()
)
ipsecIkeSaOutboundTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaOutboundTraffic.setStatus("current")
_IpsecIkeSaInboundPackets_Type = Counter32
_IpsecIkeSaInboundPackets_Object = MibTableColumn
ipsecIkeSaInboundPackets = _IpsecIkeSaInboundPackets_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 26),
    _IpsecIkeSaInboundPackets_Type()
)
ipsecIkeSaInboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaInboundPackets.setStatus("current")
_IpsecIkeSaOutboundPackets_Type = Counter32
_IpsecIkeSaOutboundPackets_Object = MibTableColumn
ipsecIkeSaOutboundPackets = _IpsecIkeSaOutboundPackets_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 27),
    _IpsecIkeSaOutboundPackets_Type()
)
ipsecIkeSaOutboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaOutboundPackets.setStatus("current")
_IpsecIkeSaTotalSaNum_Type = Counter32
_IpsecIkeSaTotalSaNum_Object = MibTableColumn
ipsecIkeSaTotalSaNum = _IpsecIkeSaTotalSaNum_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 28),
    _IpsecIkeSaTotalSaNum_Type()
)
ipsecIkeSaTotalSaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaTotalSaNum.setStatus("current")
_IpsecIkeSaFirstTimeStart_Type = DateAndTime
_IpsecIkeSaFirstTimeStart_Object = MibTableColumn
ipsecIkeSaFirstTimeStart = _IpsecIkeSaFirstTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 29),
    _IpsecIkeSaFirstTimeStart_Type()
)
ipsecIkeSaFirstTimeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaFirstTimeStart.setStatus("current")
_IpsecIkeSaTotalInboundTraffic_Type = Counter32
_IpsecIkeSaTotalInboundTraffic_Object = MibTableColumn
ipsecIkeSaTotalInboundTraffic = _IpsecIkeSaTotalInboundTraffic_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 30),
    _IpsecIkeSaTotalInboundTraffic_Type()
)
ipsecIkeSaTotalInboundTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaTotalInboundTraffic.setStatus("current")
_IpsecIkeSaTotalOutboundTraffic_Type = Counter32
_IpsecIkeSaTotalOutboundTraffic_Object = MibTableColumn
ipsecIkeSaTotalOutboundTraffic = _IpsecIkeSaTotalOutboundTraffic_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 31),
    _IpsecIkeSaTotalOutboundTraffic_Type()
)
ipsecIkeSaTotalOutboundTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaTotalOutboundTraffic.setStatus("current")
_IpsecIkeSaTotalInboundPackets_Type = Counter32
_IpsecIkeSaTotalInboundPackets_Object = MibTableColumn
ipsecIkeSaTotalInboundPackets = _IpsecIkeSaTotalInboundPackets_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 32),
    _IpsecIkeSaTotalInboundPackets_Type()
)
ipsecIkeSaTotalInboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaTotalInboundPackets.setStatus("current")
_IpsecIkeSaTotalOutboundPackets_Type = Counter32
_IpsecIkeSaTotalOutboundPackets_Object = MibTableColumn
ipsecIkeSaTotalOutboundPackets = _IpsecIkeSaTotalOutboundPackets_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 33),
    _IpsecIkeSaTotalOutboundPackets_Type()
)
ipsecIkeSaTotalOutboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaTotalOutboundPackets.setStatus("current")
_IpsecIkeSaDecryptErrors_Type = Counter32
_IpsecIkeSaDecryptErrors_Object = MibTableColumn
ipsecIkeSaDecryptErrors = _IpsecIkeSaDecryptErrors_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 34),
    _IpsecIkeSaDecryptErrors_Type()
)
ipsecIkeSaDecryptErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaDecryptErrors.setStatus("current")
_IpsecIkeSaHashErrors_Type = Counter32
_IpsecIkeSaHashErrors_Object = MibTableColumn
ipsecIkeSaHashErrors = _IpsecIkeSaHashErrors_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 35),
    _IpsecIkeSaHashErrors_Type()
)
ipsecIkeSaHashErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaHashErrors.setStatus("current")
_IpsecIkeSaOtherReceiveErrors_Type = Counter32
_IpsecIkeSaOtherReceiveErrors_Object = MibTableColumn
ipsecIkeSaOtherReceiveErrors = _IpsecIkeSaOtherReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 36),
    _IpsecIkeSaOtherReceiveErrors_Type()
)
ipsecIkeSaOtherReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaOtherReceiveErrors.setStatus("current")
_IpsecIkeSaSendErrors_Type = Counter32
_IpsecIkeSaSendErrors_Object = MibTableColumn
ipsecIkeSaSendErrors = _IpsecIkeSaSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 37),
    _IpsecIkeSaSendErrors_Type()
)
ipsecIkeSaSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaSendErrors.setStatus("current")
_IpsecIkeSaIpsecInboundTraffic_Type = Counter32
_IpsecIkeSaIpsecInboundTraffic_Object = MibTableColumn
ipsecIkeSaIpsecInboundTraffic = _IpsecIkeSaIpsecInboundTraffic_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 38),
    _IpsecIkeSaIpsecInboundTraffic_Type()
)
ipsecIkeSaIpsecInboundTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaIpsecInboundTraffic.setStatus("current")
_IpsecIkeSaIpsecOutboundTraffic_Type = Counter32
_IpsecIkeSaIpsecOutboundTraffic_Object = MibTableColumn
ipsecIkeSaIpsecOutboundTraffic = _IpsecIkeSaIpsecOutboundTraffic_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 39),
    _IpsecIkeSaIpsecOutboundTraffic_Type()
)
ipsecIkeSaIpsecOutboundTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaIpsecOutboundTraffic.setStatus("current")
_IpsecIkeSaIpsecInboundPackets_Type = Counter32
_IpsecIkeSaIpsecInboundPackets_Object = MibTableColumn
ipsecIkeSaIpsecInboundPackets = _IpsecIkeSaIpsecInboundPackets_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 40),
    _IpsecIkeSaIpsecInboundPackets_Type()
)
ipsecIkeSaIpsecInboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaIpsecInboundPackets.setStatus("current")
_IpsecIkeSaIpsecOutboundPackets_Type = Counter32
_IpsecIkeSaIpsecOutboundPackets_Object = MibTableColumn
ipsecIkeSaIpsecOutboundPackets = _IpsecIkeSaIpsecOutboundPackets_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 41),
    _IpsecIkeSaIpsecOutboundPackets_Type()
)
ipsecIkeSaIpsecOutboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaIpsecOutboundPackets.setStatus("current")
_IpsecIkeSaIpsecDecryptErrors_Type = Counter32
_IpsecIkeSaIpsecDecryptErrors_Object = MibTableColumn
ipsecIkeSaIpsecDecryptErrors = _IpsecIkeSaIpsecDecryptErrors_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 42),
    _IpsecIkeSaIpsecDecryptErrors_Type()
)
ipsecIkeSaIpsecDecryptErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaIpsecDecryptErrors.setStatus("current")
_IpsecIkeSaIpsecAuthErrors_Type = Counter32
_IpsecIkeSaIpsecAuthErrors_Object = MibTableColumn
ipsecIkeSaIpsecAuthErrors = _IpsecIkeSaIpsecAuthErrors_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 43),
    _IpsecIkeSaIpsecAuthErrors_Type()
)
ipsecIkeSaIpsecAuthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaIpsecAuthErrors.setStatus("current")
_IpsecIkeSaIpsecReplayErrors_Type = Counter32
_IpsecIkeSaIpsecReplayErrors_Object = MibTableColumn
ipsecIkeSaIpsecReplayErrors = _IpsecIkeSaIpsecReplayErrors_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 44),
    _IpsecIkeSaIpsecReplayErrors_Type()
)
ipsecIkeSaIpsecReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaIpsecReplayErrors.setStatus("current")
_IpsecIkeSaIpsecOtherReceiveErrors_Type = Counter32
_IpsecIkeSaIpsecOtherReceiveErrors_Object = MibTableColumn
ipsecIkeSaIpsecOtherReceiveErrors = _IpsecIkeSaIpsecOtherReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 45),
    _IpsecIkeSaIpsecOtherReceiveErrors_Type()
)
ipsecIkeSaIpsecOtherReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaIpsecOtherReceiveErrors.setStatus("current")
_IpsecIkeSaIpsecSendErrors_Type = Counter32
_IpsecIkeSaIpsecSendErrors_Object = MibTableColumn
ipsecIkeSaIpsecSendErrors = _IpsecIkeSaIpsecSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 1, 1, 46),
    _IpsecIkeSaIpsecSendErrors_Type()
)
ipsecIkeSaIpsecSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeSaIpsecSendErrors.setStatus("current")
_IpsecTunnelTable_Object = MibTable
ipsecTunnelTable = _IpsecTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ipsecTunnelTable.setStatus("current")
_IpsecTunnelEntry_Object = MibTableRow
ipsecTunnelEntry = _IpsecTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1)
)
ipsecTunnelEntry.setIndexNames(
    (0, "TIMESTEP-IPSEC-MIB", "ipsecTunnelIndex"),
)
if mibBuilder.loadTexts:
    ipsecTunnelEntry.setStatus("current")


class _IpsecTunnelIndex_Type(Integer32):
    """Custom type ipsecTunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_IpsecTunnelIndex_Type.__name__ = "Integer32"
_IpsecTunnelIndex_Object = MibTableColumn
ipsecTunnelIndex = _IpsecTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 1),
    _IpsecTunnelIndex_Type()
)
ipsecTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelIndex.setStatus("current")


class _IpsecTunnelIkeSa_Type(Integer32):
    """Custom type ipsecTunnelIkeSa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpsecTunnelIkeSa_Type.__name__ = "Integer32"
_IpsecTunnelIkeSa_Object = MibTableColumn
ipsecTunnelIkeSa = _IpsecTunnelIkeSa_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 2),
    _IpsecTunnelIkeSa_Type()
)
ipsecTunnelIkeSa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelIkeSa.setStatus("current")


class _IpsecTunnelType_Type(Integer32):
    """Custom type ipsecTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permanent", 2),
          ("static", 0),
          ("transient", 1))
    )


_IpsecTunnelType_Type.__name__ = "Integer32"
_IpsecTunnelType_Object = MibTableColumn
ipsecTunnelType = _IpsecTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 3),
    _IpsecTunnelType_Type()
)
ipsecTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelType.setStatus("current")
_IpsecTunnelLocalAddressOrStart_Type = IpAddress
_IpsecTunnelLocalAddressOrStart_Object = MibTableColumn
ipsecTunnelLocalAddressOrStart = _IpsecTunnelLocalAddressOrStart_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 4),
    _IpsecTunnelLocalAddressOrStart_Type()
)
ipsecTunnelLocalAddressOrStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelLocalAddressOrStart.setStatus("current")
_IpsecTunnelLocalAddressMaskOrEnd_Type = IpAddress
_IpsecTunnelLocalAddressMaskOrEnd_Object = MibTableColumn
ipsecTunnelLocalAddressMaskOrEnd = _IpsecTunnelLocalAddressMaskOrEnd_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 5),
    _IpsecTunnelLocalAddressMaskOrEnd_Type()
)
ipsecTunnelLocalAddressMaskOrEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelLocalAddressMaskOrEnd.setStatus("current")
_IpsecTunnelRemoteAddressOrStart_Type = IpAddress
_IpsecTunnelRemoteAddressOrStart_Object = MibTableColumn
ipsecTunnelRemoteAddressOrStart = _IpsecTunnelRemoteAddressOrStart_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 6),
    _IpsecTunnelRemoteAddressOrStart_Type()
)
ipsecTunnelRemoteAddressOrStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelRemoteAddressOrStart.setStatus("current")
_IpsecTunnelRemoteAddressMaskOrEnd_Type = IpAddress
_IpsecTunnelRemoteAddressMaskOrEnd_Object = MibTableColumn
ipsecTunnelRemoteAddressMaskOrEnd = _IpsecTunnelRemoteAddressMaskOrEnd_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 7),
    _IpsecTunnelRemoteAddressMaskOrEnd_Type()
)
ipsecTunnelRemoteAddressMaskOrEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelRemoteAddressMaskOrEnd.setStatus("current")


class _IpsecTunnelProtocol_Type(Integer32):
    """Custom type ipsecTunnelProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpsecTunnelProtocol_Type.__name__ = "Integer32"
_IpsecTunnelProtocol_Object = MibTableColumn
ipsecTunnelProtocol = _IpsecTunnelProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 8),
    _IpsecTunnelProtocol_Type()
)
ipsecTunnelProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelProtocol.setStatus("current")


class _IpsecTunnelLocalPort_Type(Integer32):
    """Custom type ipsecTunnelLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecTunnelLocalPort_Type.__name__ = "Integer32"
_IpsecTunnelLocalPort_Object = MibTableColumn
ipsecTunnelLocalPort = _IpsecTunnelLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 9),
    _IpsecTunnelLocalPort_Type()
)
ipsecTunnelLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelLocalPort.setStatus("current")


class _IpsecTunnelRemotePort_Type(Integer32):
    """Custom type ipsecTunnelRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecTunnelRemotePort_Type.__name__ = "Integer32"
_IpsecTunnelRemotePort_Object = MibTableColumn
ipsecTunnelRemotePort = _IpsecTunnelRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 10),
    _IpsecTunnelRemotePort_Type()
)
ipsecTunnelRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelRemotePort.setStatus("current")


class _IpsecTunnelMode_Type(Integer32):
    """Custom type ipsecTunnelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transport", 1),
          ("tunnel", 2))
    )


_IpsecTunnelMode_Type.__name__ = "Integer32"
_IpsecTunnelMode_Object = MibTableColumn
ipsecTunnelMode = _IpsecTunnelMode_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 11),
    _IpsecTunnelMode_Type()
)
ipsecTunnelMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelMode.setStatus("current")


class _IpsecTunnelEspEncAlg_Type(Integer32):
    """Custom type ipsecTunnelEspEncAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpsecTunnelEspEncAlg_Type.__name__ = "Integer32"
_IpsecTunnelEspEncAlg_Object = MibTableColumn
ipsecTunnelEspEncAlg = _IpsecTunnelEspEncAlg_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 12),
    _IpsecTunnelEspEncAlg_Type()
)
ipsecTunnelEspEncAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelEspEncAlg.setStatus("current")
_IpsecTunnelEspEncKeyLength_Type = Integer32
_IpsecTunnelEspEncKeyLength_Object = MibTableColumn
ipsecTunnelEspEncKeyLength = _IpsecTunnelEspEncKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 13),
    _IpsecTunnelEspEncKeyLength_Type()
)
ipsecTunnelEspEncKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelEspEncKeyLength.setStatus("current")


class _IpsecTunnelEspAuthAlg_Type(Integer32):
    """Custom type ipsecTunnelEspAuthAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpsecTunnelEspAuthAlg_Type.__name__ = "Integer32"
_IpsecTunnelEspAuthAlg_Object = MibTableColumn
ipsecTunnelEspAuthAlg = _IpsecTunnelEspAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 14),
    _IpsecTunnelEspAuthAlg_Type()
)
ipsecTunnelEspAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelEspAuthAlg.setStatus("current")


class _IpsecTunnelAhAuthAlg_Type(Integer32):
    """Custom type ipsecTunnelAhAuthAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpsecTunnelAhAuthAlg_Type.__name__ = "Integer32"
_IpsecTunnelAhAuthAlg_Object = MibTableColumn
ipsecTunnelAhAuthAlg = _IpsecTunnelAhAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 15),
    _IpsecTunnelAhAuthAlg_Type()
)
ipsecTunnelAhAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelAhAuthAlg.setStatus("current")


class _IpsecTunnelCompAlg_Type(Integer32):
    """Custom type ipsecTunnelCompAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpsecTunnelCompAlg_Type.__name__ = "Integer32"
_IpsecTunnelCompAlg_Object = MibTableColumn
ipsecTunnelCompAlg = _IpsecTunnelCompAlg_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 16),
    _IpsecTunnelCompAlg_Type()
)
ipsecTunnelCompAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelCompAlg.setStatus("current")
_IpsecTunnelStartTime_Type = DateAndTime
_IpsecTunnelStartTime_Object = MibTableColumn
ipsecTunnelStartTime = _IpsecTunnelStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 17),
    _IpsecTunnelStartTime_Type()
)
ipsecTunnelStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelStartTime.setStatus("current")
_IpsecTunnelCurrentSaNum_Type = Gauge32
_IpsecTunnelCurrentSaNum_Object = MibTableColumn
ipsecTunnelCurrentSaNum = _IpsecTunnelCurrentSaNum_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 18),
    _IpsecTunnelCurrentSaNum_Type()
)
ipsecTunnelCurrentSaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelCurrentSaNum.setStatus("current")
_IpsecTunnelTotalSaNum_Type = Counter32
_IpsecTunnelTotalSaNum_Object = MibTableColumn
ipsecTunnelTotalSaNum = _IpsecTunnelTotalSaNum_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 19),
    _IpsecTunnelTotalSaNum_Type()
)
ipsecTunnelTotalSaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelTotalSaNum.setStatus("current")
_IpsecTunnelTotalInboundTraffic_Type = Counter32
_IpsecTunnelTotalInboundTraffic_Object = MibTableColumn
ipsecTunnelTotalInboundTraffic = _IpsecTunnelTotalInboundTraffic_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 20),
    _IpsecTunnelTotalInboundTraffic_Type()
)
ipsecTunnelTotalInboundTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelTotalInboundTraffic.setStatus("current")
_IpsecTunnelTotalOutboundTraffic_Type = Counter32
_IpsecTunnelTotalOutboundTraffic_Object = MibTableColumn
ipsecTunnelTotalOutboundTraffic = _IpsecTunnelTotalOutboundTraffic_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 21),
    _IpsecTunnelTotalOutboundTraffic_Type()
)
ipsecTunnelTotalOutboundTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelTotalOutboundTraffic.setStatus("current")
_IpsecTunnelTotalInboundPackets_Type = Counter32
_IpsecTunnelTotalInboundPackets_Object = MibTableColumn
ipsecTunnelTotalInboundPackets = _IpsecTunnelTotalInboundPackets_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 22),
    _IpsecTunnelTotalInboundPackets_Type()
)
ipsecTunnelTotalInboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelTotalInboundPackets.setStatus("current")
_IpsecTunnelTotalOutboundPackets_Type = Counter32
_IpsecTunnelTotalOutboundPackets_Object = MibTableColumn
ipsecTunnelTotalOutboundPackets = _IpsecTunnelTotalOutboundPackets_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 23),
    _IpsecTunnelTotalOutboundPackets_Type()
)
ipsecTunnelTotalOutboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelTotalOutboundPackets.setStatus("current")
_IpsecTunnelDecryptErrors_Type = Counter32
_IpsecTunnelDecryptErrors_Object = MibTableColumn
ipsecTunnelDecryptErrors = _IpsecTunnelDecryptErrors_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 24),
    _IpsecTunnelDecryptErrors_Type()
)
ipsecTunnelDecryptErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelDecryptErrors.setStatus("current")
_IpsecTunnelAuthErrors_Type = Counter32
_IpsecTunnelAuthErrors_Object = MibTableColumn
ipsecTunnelAuthErrors = _IpsecTunnelAuthErrors_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 25),
    _IpsecTunnelAuthErrors_Type()
)
ipsecTunnelAuthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelAuthErrors.setStatus("current")
_IpsecTunnelReplayErrors_Type = Counter32
_IpsecTunnelReplayErrors_Object = MibTableColumn
ipsecTunnelReplayErrors = _IpsecTunnelReplayErrors_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 26),
    _IpsecTunnelReplayErrors_Type()
)
ipsecTunnelReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelReplayErrors.setStatus("current")
_IpsecTunnelPolicyErrors_Type = Counter32
_IpsecTunnelPolicyErrors_Object = MibTableColumn
ipsecTunnelPolicyErrors = _IpsecTunnelPolicyErrors_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 27),
    _IpsecTunnelPolicyErrors_Type()
)
ipsecTunnelPolicyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelPolicyErrors.setStatus("current")
_IpsecTunnelOtherReceiveErrors_Type = Counter32
_IpsecTunnelOtherReceiveErrors_Object = MibTableColumn
ipsecTunnelOtherReceiveErrors = _IpsecTunnelOtherReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 28),
    _IpsecTunnelOtherReceiveErrors_Type()
)
ipsecTunnelOtherReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelOtherReceiveErrors.setStatus("current")
_IpsecTunnelSendErrors_Type = Counter32
_IpsecTunnelSendErrors_Object = MibTableColumn
ipsecTunnelSendErrors = _IpsecTunnelSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 2, 1, 29),
    _IpsecTunnelSendErrors_Type()
)
ipsecTunnelSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTunnelSendErrors.setStatus("current")
_IpsecSaTable_Object = MibTable
ipsecSaTable = _IpsecSaTable_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ipsecSaTable.setStatus("current")
_IpsecSaEntry_Object = MibTableRow
ipsecSaEntry = _IpsecSaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 3, 1)
)
ipsecSaEntry.setIndexNames(
    (0, "TIMESTEP-IPSEC-MIB", "ipsecSaIndex"),
)
if mibBuilder.loadTexts:
    ipsecSaEntry.setStatus("current")


class _IpsecSaIndex_Type(Integer32):
    """Custom type ipsecSaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpsecSaIndex_Type.__name__ = "Integer32"
_IpsecSaIndex_Object = MibTableColumn
ipsecSaIndex = _IpsecSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 3, 1, 1),
    _IpsecSaIndex_Type()
)
ipsecSaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaIndex.setStatus("current")


class _IpsecSaTunnel_Type(Integer32):
    """Custom type ipsecSaTunnel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpsecSaTunnel_Type.__name__ = "Integer32"
_IpsecSaTunnel_Object = MibTableColumn
ipsecSaTunnel = _IpsecSaTunnel_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 3, 1, 2),
    _IpsecSaTunnel_Type()
)
ipsecSaTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaTunnel.setStatus("current")
_IpsecSaInboundEspSpi_Type = Unsigned32
_IpsecSaInboundEspSpi_Object = MibTableColumn
ipsecSaInboundEspSpi = _IpsecSaInboundEspSpi_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 3, 1, 3),
    _IpsecSaInboundEspSpi_Type()
)
ipsecSaInboundEspSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaInboundEspSpi.setStatus("current")
_IpsecSaOutboundEspSpi_Type = Unsigned32
_IpsecSaOutboundEspSpi_Object = MibTableColumn
ipsecSaOutboundEspSpi = _IpsecSaOutboundEspSpi_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 3, 1, 4),
    _IpsecSaOutboundEspSpi_Type()
)
ipsecSaOutboundEspSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaOutboundEspSpi.setStatus("current")
_IpsecSaInboundAhSpi_Type = Unsigned32
_IpsecSaInboundAhSpi_Object = MibTableColumn
ipsecSaInboundAhSpi = _IpsecSaInboundAhSpi_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 3, 1, 5),
    _IpsecSaInboundAhSpi_Type()
)
ipsecSaInboundAhSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaInboundAhSpi.setStatus("current")
_IpsecSaOutboundAhSpi_Type = Unsigned32
_IpsecSaOutboundAhSpi_Object = MibTableColumn
ipsecSaOutboundAhSpi = _IpsecSaOutboundAhSpi_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 3, 1, 6),
    _IpsecSaOutboundAhSpi_Type()
)
ipsecSaOutboundAhSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaOutboundAhSpi.setStatus("current")


class _IpsecSaInboundCompCpi_Type(Integer32):
    """Custom type ipsecSaInboundCompCpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecSaInboundCompCpi_Type.__name__ = "Integer32"
_IpsecSaInboundCompCpi_Object = MibTableColumn
ipsecSaInboundCompCpi = _IpsecSaInboundCompCpi_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 3, 1, 7),
    _IpsecSaInboundCompCpi_Type()
)
ipsecSaInboundCompCpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaInboundCompCpi.setStatus("current")


class _IpsecSaOutboundCompCpi_Type(Integer32):
    """Custom type ipsecSaOutboundCompCpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecSaOutboundCompCpi_Type.__name__ = "Integer32"
_IpsecSaOutboundCompCpi_Object = MibTableColumn
ipsecSaOutboundCompCpi = _IpsecSaOutboundCompCpi_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 3, 1, 8),
    _IpsecSaOutboundCompCpi_Type()
)
ipsecSaOutboundCompCpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaOutboundCompCpi.setStatus("current")
_IpsecSaCreationTime_Type = DateAndTime
_IpsecSaCreationTime_Object = MibTableColumn
ipsecSaCreationTime = _IpsecSaCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 3, 1, 9),
    _IpsecSaCreationTime_Type()
)
ipsecSaCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaCreationTime.setStatus("current")
_IpsecSaTimeLimit_Type = Gauge32
_IpsecSaTimeLimit_Object = MibTableColumn
ipsecSaTimeLimit = _IpsecSaTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 3, 1, 10),
    _IpsecSaTimeLimit_Type()
)
ipsecSaTimeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaTimeLimit.setStatus("current")
_IpsecSaTrafficLimit_Type = Gauge32
_IpsecSaTrafficLimit_Object = MibTableColumn
ipsecSaTrafficLimit = _IpsecSaTrafficLimit_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 3, 1, 11),
    _IpsecSaTrafficLimit_Type()
)
ipsecSaTrafficLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaTrafficLimit.setStatus("current")
_IpsecSaInboundTraffic_Type = Counter32
_IpsecSaInboundTraffic_Object = MibTableColumn
ipsecSaInboundTraffic = _IpsecSaInboundTraffic_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 3, 1, 12),
    _IpsecSaInboundTraffic_Type()
)
ipsecSaInboundTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaInboundTraffic.setStatus("current")
_IpsecSaOutboundTraffic_Type = Counter32
_IpsecSaOutboundTraffic_Object = MibTableColumn
ipsecSaOutboundTraffic = _IpsecSaOutboundTraffic_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 3, 1, 13),
    _IpsecSaOutboundTraffic_Type()
)
ipsecSaOutboundTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaOutboundTraffic.setStatus("current")
_IpsecSaInboundPackets_Type = Counter32
_IpsecSaInboundPackets_Object = MibTableColumn
ipsecSaInboundPackets = _IpsecSaInboundPackets_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 3, 1, 14),
    _IpsecSaInboundPackets_Type()
)
ipsecSaInboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaInboundPackets.setStatus("current")
_IpsecSaOutboundPackets_Type = Counter32
_IpsecSaOutboundPackets_Object = MibTableColumn
ipsecSaOutboundPackets = _IpsecSaOutboundPackets_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 3, 1, 15),
    _IpsecSaOutboundPackets_Type()
)
ipsecSaOutboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaOutboundPackets.setStatus("current")
_IpsecSaDecryptErrors_Type = Counter32
_IpsecSaDecryptErrors_Object = MibTableColumn
ipsecSaDecryptErrors = _IpsecSaDecryptErrors_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 3, 1, 16),
    _IpsecSaDecryptErrors_Type()
)
ipsecSaDecryptErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaDecryptErrors.setStatus("current")
_IpsecSaAuthErrors_Type = Counter32
_IpsecSaAuthErrors_Object = MibTableColumn
ipsecSaAuthErrors = _IpsecSaAuthErrors_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 3, 1, 17),
    _IpsecSaAuthErrors_Type()
)
ipsecSaAuthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaAuthErrors.setStatus("current")
_IpsecSaReplayErrors_Type = Counter32
_IpsecSaReplayErrors_Object = MibTableColumn
ipsecSaReplayErrors = _IpsecSaReplayErrors_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 3, 1, 18),
    _IpsecSaReplayErrors_Type()
)
ipsecSaReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaReplayErrors.setStatus("current")
_IpsecSaOtherReceiveErrors_Type = Counter32
_IpsecSaOtherReceiveErrors_Object = MibTableColumn
ipsecSaOtherReceiveErrors = _IpsecSaOtherReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 3, 1, 19),
    _IpsecSaOtherReceiveErrors_Type()
)
ipsecSaOtherReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaOtherReceiveErrors.setStatus("current")
_IpsecSaSendErrors_Type = Counter32
_IpsecSaSendErrors_Object = MibTableColumn
ipsecSaSendErrors = _IpsecSaSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 3, 1, 20),
    _IpsecSaSendErrors_Type()
)
ipsecSaSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecSaSendErrors.setStatus("current")
_IpsecTraps_ObjectIdentity = ObjectIdentity
ipsecTraps = _IpsecTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 4)
)
_IpsecTrapsObjects_ObjectIdentity = ObjectIdentity
ipsecTrapsObjects = _IpsecTrapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 4, 0)
)
_IpsecSaCounts_ObjectIdentity = ObjectIdentity
ipsecSaCounts = _IpsecSaCounts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 5)
)
_IpsecTotalIkeSAs_Type = Counter32
_IpsecTotalIkeSAs_Object = MibScalar
ipsecTotalIkeSAs = _IpsecTotalIkeSAs_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 5, 1),
    _IpsecTotalIkeSAs_Type()
)
ipsecTotalIkeSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTotalIkeSAs.setStatus("current")
_IpsecTotalIpsecSAs_Type = Counter32
_IpsecTotalIpsecSAs_Object = MibScalar
ipsecTotalIpsecSAs = _IpsecTotalIpsecSAs_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 5, 2),
    _IpsecTotalIpsecSAs_Type()
)
ipsecTotalIpsecSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTotalIpsecSAs.setStatus("current")
_IpsecPermTunStats_ObjectIdentity = ObjectIdentity
ipsecPermTunStats = _IpsecPermTunStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 6)
)
_IpsecCnfgPermIkeTunnels_Type = Gauge32
_IpsecCnfgPermIkeTunnels_Object = MibScalar
ipsecCnfgPermIkeTunnels = _IpsecCnfgPermIkeTunnels_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 6, 1),
    _IpsecCnfgPermIkeTunnels_Type()
)
ipsecCnfgPermIkeTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecCnfgPermIkeTunnels.setStatus("current")
_IpsecUpPermIkeTunnels_Type = Gauge32
_IpsecUpPermIkeTunnels_Object = MibScalar
ipsecUpPermIkeTunnels = _IpsecUpPermIkeTunnels_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 6, 2),
    _IpsecUpPermIkeTunnels_Type()
)
ipsecUpPermIkeTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecUpPermIkeTunnels.setStatus("current")
_IpsecCnfgPermIpsecTunnels_Type = Gauge32
_IpsecCnfgPermIpsecTunnels_Object = MibScalar
ipsecCnfgPermIpsecTunnels = _IpsecCnfgPermIpsecTunnels_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 6, 3),
    _IpsecCnfgPermIpsecTunnels_Type()
)
ipsecCnfgPermIpsecTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecCnfgPermIpsecTunnels.setStatus("current")
_IpsecUpPermIpsecTunnels_Type = Gauge32
_IpsecUpPermIpsecTunnels_Object = MibScalar
ipsecUpPermIpsecTunnels = _IpsecUpPermIpsecTunnels_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 6, 4),
    _IpsecUpPermIpsecTunnels_Type()
)
ipsecUpPermIpsecTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecUpPermIpsecTunnels.setStatus("current")
_IpsecTransTunStats_ObjectIdentity = ObjectIdentity
ipsecTransTunStats = _IpsecTransTunStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 7)
)
_IpsecTotalTransIkeTunnels_Type = Counter32
_IpsecTotalTransIkeTunnels_Object = MibScalar
ipsecTotalTransIkeTunnels = _IpsecTotalTransIkeTunnels_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 7, 1),
    _IpsecTotalTransIkeTunnels_Type()
)
ipsecTotalTransIkeTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTotalTransIkeTunnels.setStatus("current")
_IpsecCurrentTransIkeTunnels_Type = Gauge32
_IpsecCurrentTransIkeTunnels_Object = MibScalar
ipsecCurrentTransIkeTunnels = _IpsecCurrentTransIkeTunnels_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 7, 2),
    _IpsecCurrentTransIkeTunnels_Type()
)
ipsecCurrentTransIkeTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecCurrentTransIkeTunnels.setStatus("current")
_IpsecTotalTransIpsecTunnels_Type = Counter32
_IpsecTotalTransIpsecTunnels_Object = MibScalar
ipsecTotalTransIpsecTunnels = _IpsecTotalTransIpsecTunnels_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 7, 3),
    _IpsecTotalTransIpsecTunnels_Type()
)
ipsecTotalTransIpsecTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTotalTransIpsecTunnels.setStatus("current")
_IpsecCurrentTransIpsecTunnels_Type = Gauge32
_IpsecCurrentTransIpsecTunnels_Object = MibScalar
ipsecCurrentTransIpsecTunnels = _IpsecCurrentTransIpsecTunnels_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 7, 4),
    _IpsecCurrentTransIpsecTunnels_Type()
)
ipsecCurrentTransIpsecTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecCurrentTransIpsecTunnels.setStatus("current")
_IpsecTotalTransInboundPackets_Type = Counter32
_IpsecTotalTransInboundPackets_Object = MibScalar
ipsecTotalTransInboundPackets = _IpsecTotalTransInboundPackets_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 7, 5),
    _IpsecTotalTransInboundPackets_Type()
)
ipsecTotalTransInboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTotalTransInboundPackets.setStatus("current")
_IpsecTotalTransOutboundPackets_Type = Counter32
_IpsecTotalTransOutboundPackets_Object = MibScalar
ipsecTotalTransOutboundPackets = _IpsecTotalTransOutboundPackets_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 7, 6),
    _IpsecTotalTransOutboundPackets_Type()
)
ipsecTotalTransOutboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTotalTransOutboundPackets.setStatus("current")
_IpsecTotalTransInboundTraffic_Type = Counter32
_IpsecTotalTransInboundTraffic_Object = MibScalar
ipsecTotalTransInboundTraffic = _IpsecTotalTransInboundTraffic_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 7, 7),
    _IpsecTotalTransInboundTraffic_Type()
)
ipsecTotalTransInboundTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTotalTransInboundTraffic.setStatus("current")
_IpsecTotalTransOutboundTraffic_Type = Counter32
_IpsecTotalTransOutboundTraffic_Object = MibScalar
ipsecTotalTransOutboundTraffic = _IpsecTotalTransOutboundTraffic_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 7, 8),
    _IpsecTotalTransOutboundTraffic_Type()
)
ipsecTotalTransOutboundTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTotalTransOutboundTraffic.setStatus("current")
_IpsecTotalTransIkeSetupFailures_Type = Counter32
_IpsecTotalTransIkeSetupFailures_Object = MibScalar
ipsecTotalTransIkeSetupFailures = _IpsecTotalTransIkeSetupFailures_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 7, 9),
    _IpsecTotalTransIkeSetupFailures_Type()
)
ipsecTotalTransIkeSetupFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecTotalTransIkeSetupFailures.setStatus("current")
_IpsecNotifications_ObjectIdentity = ObjectIdentity
ipsecNotifications = _IpsecNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 8)
)
_IpsecNotifyMessageTotalCount_Type = Counter32
_IpsecNotifyMessageTotalCount_Object = MibScalar
ipsecNotifyMessageTotalCount = _IpsecNotifyMessageTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 8, 1),
    _IpsecNotifyMessageTotalCount_Type()
)
ipsecNotifyMessageTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecNotifyMessageTotalCount.setStatus("current")
_IpsecNotifyCountTable_Object = MibTable
ipsecNotifyCountTable = _IpsecNotifyCountTable_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 8, 2)
)
if mibBuilder.loadTexts:
    ipsecNotifyCountTable.setStatus("current")
_IpsecNotifyCountEntry_Object = MibTableRow
ipsecNotifyCountEntry = _IpsecNotifyCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 8, 2, 1)
)
ipsecNotifyCountEntry.setIndexNames(
    (0, "TIMESTEP-IPSEC-MIB", "ipsecNotifyMessage"),
)
if mibBuilder.loadTexts:
    ipsecNotifyCountEntry.setStatus("current")


class _IpsecNotifyMessage_Type(Integer32):
    """Custom type ipsecNotifyMessage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpsecNotifyMessage_Type.__name__ = "Integer32"
_IpsecNotifyMessage_Object = MibTableColumn
ipsecNotifyMessage = _IpsecNotifyMessage_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 8, 2, 1, 1),
    _IpsecNotifyMessage_Type()
)
ipsecNotifyMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecNotifyMessage.setStatus("current")
_IpsecNotifyMessageCount_Type = Counter32
_IpsecNotifyMessageCount_Object = MibTableColumn
ipsecNotifyMessageCount = _IpsecNotifyMessageCount_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 8, 2, 1, 2),
    _IpsecNotifyMessageCount_Type()
)
ipsecNotifyMessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecNotifyMessageCount.setStatus("current")
_IpsecErrorStats_ObjectIdentity = ObjectIdentity
ipsecErrorStats = _IpsecErrorStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 9)
)
_IpsecUnknownSpiErrors_Type = Counter32
_IpsecUnknownSpiErrors_Object = MibScalar
ipsecUnknownSpiErrors = _IpsecUnknownSpiErrors_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 9, 1),
    _IpsecUnknownSpiErrors_Type()
)
ipsecUnknownSpiErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecUnknownSpiErrors.setStatus("current")
_IpsecIkeProtocolErrors_Type = Counter32
_IpsecIkeProtocolErrors_Object = MibScalar
ipsecIkeProtocolErrors = _IpsecIkeProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 9, 2),
    _IpsecIkeProtocolErrors_Type()
)
ipsecIkeProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIkeProtocolErrors.setStatus("current")
_IpsecIpsecAuthenticationErrors_Type = Counter32
_IpsecIpsecAuthenticationErrors_Object = MibScalar
ipsecIpsecAuthenticationErrors = _IpsecIpsecAuthenticationErrors_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 9, 3),
    _IpsecIpsecAuthenticationErrors_Type()
)
ipsecIpsecAuthenticationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIpsecAuthenticationErrors.setStatus("current")
_IpsecIpsecReplayErrors_Type = Counter32
_IpsecIpsecReplayErrors_Object = MibScalar
ipsecIpsecReplayErrors = _IpsecIpsecReplayErrors_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 9, 4),
    _IpsecIpsecReplayErrors_Type()
)
ipsecIpsecReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIpsecReplayErrors.setStatus("current")
_IpsecIpsecPolicyErrors_Type = Counter32
_IpsecIpsecPolicyErrors_Object = MibScalar
ipsecIpsecPolicyErrors = _IpsecIpsecPolicyErrors_Object(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 9, 5),
    _IpsecIpsecPolicyErrors_Type()
)
ipsecIpsecPolicyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecIpsecPolicyErrors.setStatus("current")

# Managed Objects groups


# Notification objects

ipsecTrapPermIkeNegFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 4, 0, 1)
)
ipsecTrapPermIkeNegFailure.setObjects(
      *(("TIMESTEP-IPSEC-MIB", "ipsecIkeSaIndex"),
        ("TIMESTEP-IPSEC-MIB", "ipsecNotifyMessage"))
)
if mibBuilder.loadTexts:
    ipsecTrapPermIkeNegFailure.setStatus(
        "current"
    )

ipsecTrapTransIkeNegFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 4, 0, 2)
)
ipsecTrapTransIkeNegFailure.setObjects(
      *(("TIMESTEP-IPSEC-MIB", "ipsecIkeSaPeerIpAddress"),
        ("TIMESTEP-IPSEC-MIB", "ipsecIkeSaPeerPortNumber"),
        ("TIMESTEP-IPSEC-MIB", "ipsecIkeSaAuthMethod"),
        ("TIMESTEP-IPSEC-MIB", "ipsecIkeSaPeerIdType"),
        ("TIMESTEP-IPSEC-MIB", "ipsecIkeSaPeerId"),
        ("TIMESTEP-IPSEC-MIB", "ipsecIkeSaPeerCertSerialNum"),
        ("TIMESTEP-IPSEC-MIB", "ipsecIkeSaPeerCertIssuer"),
        ("TIMESTEP-IPSEC-MIB", "ipsecNotifyMessage"))
)
if mibBuilder.loadTexts:
    ipsecTrapTransIkeNegFailure.setStatus(
        "current"
    )

ipsecTrapInvalidCookie = NotificationType(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 4, 0, 3)
)
ipsecTrapInvalidCookie.setObjects(
      *(("TIMESTEP-IPSEC-MIB", "ipsecIkeSaPeerIpAddress"),
        ("TIMESTEP-IPSEC-MIB", "ipsecIkeSaPeerPortNumber"))
)
if mibBuilder.loadTexts:
    ipsecTrapInvalidCookie.setStatus(
        "current"
    )

ipsecTrapIpsecNegFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 4, 0, 4)
)
ipsecTrapIpsecNegFailure.setObjects(
      *(("TIMESTEP-IPSEC-MIB", "ipsecIkeSaIndex"),
        ("TIMESTEP-IPSEC-MIB", "ipsecNotifyMessage"))
)
if mibBuilder.loadTexts:
    ipsecTrapIpsecNegFailure.setStatus(
        "current"
    )

ipsecTrapIpsecAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 4, 0, 5)
)
ipsecTrapIpsecAuthFailure.setObjects(
    ("TIMESTEP-IPSEC-MIB", "ipsecSaIndex")
)
if mibBuilder.loadTexts:
    ipsecTrapIpsecAuthFailure.setStatus(
        "current"
    )

ipsecTrapIpsecReplayFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 4, 0, 6)
)
ipsecTrapIpsecReplayFailure.setObjects(
    ("TIMESTEP-IPSEC-MIB", "ipsecSaIndex")
)
if mibBuilder.loadTexts:
    ipsecTrapIpsecReplayFailure.setStatus(
        "current"
    )

ipsecTrapIpsecPolicyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 4, 0, 7)
)
ipsecTrapIpsecPolicyFailure.setObjects(
    ("TIMESTEP-IPSEC-MIB", "ipsecSaIndex")
)
if mibBuilder.loadTexts:
    ipsecTrapIpsecPolicyFailure.setStatus(
        "current"
    )

ipsecTrapInvalidSpi = NotificationType(
    (1, 3, 6, 1, 4, 1, 1022, 10, 1, 1, 4, 0, 8)
)
ipsecTrapInvalidSpi.setObjects(
    ("TIMESTEP-IPSEC-MIB", "ipsecIkeSaPeerIpAddress")
)
if mibBuilder.loadTexts:
    ipsecTrapInvalidSpi.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMESTEP-IPSEC-MIB",
    **{"ipsecMIB": ipsecMIB,
       "ipsecMIBObjects": ipsecMIBObjects,
       "ipsec": ipsec,
       "ipsecIkeSaTable": ipsecIkeSaTable,
       "ipsecIkeSaEntry": ipsecIkeSaEntry,
       "ipsecIkeSaIndex": ipsecIkeSaIndex,
       "ipsecIkeSaPeerIpAddress": ipsecIkeSaPeerIpAddress,
       "ipsecIkeSaPeerPortNumber": ipsecIkeSaPeerPortNumber,
       "ipsecIkeSaAuthMethod": ipsecIkeSaAuthMethod,
       "ipsecIkeSaPeerIdType": ipsecIkeSaPeerIdType,
       "ipsecIkeSaPeerId": ipsecIkeSaPeerId,
       "ipsecIkeSaPeerCertSerialNum": ipsecIkeSaPeerCertSerialNum,
       "ipsecIkeSaPeerCertIssuer": ipsecIkeSaPeerCertIssuer,
       "ipsecIkeSaType": ipsecIkeSaType,
       "ipsecIkeSaStatus": ipsecIkeSaStatus,
       "ipsecIkeSaEncAlg": ipsecIkeSaEncAlg,
       "ipsecIkeSaEncKeyLength": ipsecIkeSaEncKeyLength,
       "ipsecIkeSaHashAlg": ipsecIkeSaHashAlg,
       "ipsecIkeSaDifHelGroupDesc": ipsecIkeSaDifHelGroupDesc,
       "ipsecIkeSaDifHelGroupType": ipsecIkeSaDifHelGroupType,
       "ipsecIkeSaDifHelFieldSize": ipsecIkeSaDifHelFieldSize,
       "ipsecIkeSaPRF": ipsecIkeSaPRF,
       "ipsecIkeSaPFS": ipsecIkeSaPFS,
       "ipsecIkeSaInitiatorCookie": ipsecIkeSaInitiatorCookie,
       "ipsecIkeSaResponderCookie": ipsecIkeSaResponderCookie,
       "ipsecIkeSaTimeStart": ipsecIkeSaTimeStart,
       "ipsecIkeSaTimeLimit": ipsecIkeSaTimeLimit,
       "ipsecIkeSaTrafficLimit": ipsecIkeSaTrafficLimit,
       "ipsecIkeSaInboundTraffic": ipsecIkeSaInboundTraffic,
       "ipsecIkeSaOutboundTraffic": ipsecIkeSaOutboundTraffic,
       "ipsecIkeSaInboundPackets": ipsecIkeSaInboundPackets,
       "ipsecIkeSaOutboundPackets": ipsecIkeSaOutboundPackets,
       "ipsecIkeSaTotalSaNum": ipsecIkeSaTotalSaNum,
       "ipsecIkeSaFirstTimeStart": ipsecIkeSaFirstTimeStart,
       "ipsecIkeSaTotalInboundTraffic": ipsecIkeSaTotalInboundTraffic,
       "ipsecIkeSaTotalOutboundTraffic": ipsecIkeSaTotalOutboundTraffic,
       "ipsecIkeSaTotalInboundPackets": ipsecIkeSaTotalInboundPackets,
       "ipsecIkeSaTotalOutboundPackets": ipsecIkeSaTotalOutboundPackets,
       "ipsecIkeSaDecryptErrors": ipsecIkeSaDecryptErrors,
       "ipsecIkeSaHashErrors": ipsecIkeSaHashErrors,
       "ipsecIkeSaOtherReceiveErrors": ipsecIkeSaOtherReceiveErrors,
       "ipsecIkeSaSendErrors": ipsecIkeSaSendErrors,
       "ipsecIkeSaIpsecInboundTraffic": ipsecIkeSaIpsecInboundTraffic,
       "ipsecIkeSaIpsecOutboundTraffic": ipsecIkeSaIpsecOutboundTraffic,
       "ipsecIkeSaIpsecInboundPackets": ipsecIkeSaIpsecInboundPackets,
       "ipsecIkeSaIpsecOutboundPackets": ipsecIkeSaIpsecOutboundPackets,
       "ipsecIkeSaIpsecDecryptErrors": ipsecIkeSaIpsecDecryptErrors,
       "ipsecIkeSaIpsecAuthErrors": ipsecIkeSaIpsecAuthErrors,
       "ipsecIkeSaIpsecReplayErrors": ipsecIkeSaIpsecReplayErrors,
       "ipsecIkeSaIpsecOtherReceiveErrors": ipsecIkeSaIpsecOtherReceiveErrors,
       "ipsecIkeSaIpsecSendErrors": ipsecIkeSaIpsecSendErrors,
       "ipsecTunnelTable": ipsecTunnelTable,
       "ipsecTunnelEntry": ipsecTunnelEntry,
       "ipsecTunnelIndex": ipsecTunnelIndex,
       "ipsecTunnelIkeSa": ipsecTunnelIkeSa,
       "ipsecTunnelType": ipsecTunnelType,
       "ipsecTunnelLocalAddressOrStart": ipsecTunnelLocalAddressOrStart,
       "ipsecTunnelLocalAddressMaskOrEnd": ipsecTunnelLocalAddressMaskOrEnd,
       "ipsecTunnelRemoteAddressOrStart": ipsecTunnelRemoteAddressOrStart,
       "ipsecTunnelRemoteAddressMaskOrEnd": ipsecTunnelRemoteAddressMaskOrEnd,
       "ipsecTunnelProtocol": ipsecTunnelProtocol,
       "ipsecTunnelLocalPort": ipsecTunnelLocalPort,
       "ipsecTunnelRemotePort": ipsecTunnelRemotePort,
       "ipsecTunnelMode": ipsecTunnelMode,
       "ipsecTunnelEspEncAlg": ipsecTunnelEspEncAlg,
       "ipsecTunnelEspEncKeyLength": ipsecTunnelEspEncKeyLength,
       "ipsecTunnelEspAuthAlg": ipsecTunnelEspAuthAlg,
       "ipsecTunnelAhAuthAlg": ipsecTunnelAhAuthAlg,
       "ipsecTunnelCompAlg": ipsecTunnelCompAlg,
       "ipsecTunnelStartTime": ipsecTunnelStartTime,
       "ipsecTunnelCurrentSaNum": ipsecTunnelCurrentSaNum,
       "ipsecTunnelTotalSaNum": ipsecTunnelTotalSaNum,
       "ipsecTunnelTotalInboundTraffic": ipsecTunnelTotalInboundTraffic,
       "ipsecTunnelTotalOutboundTraffic": ipsecTunnelTotalOutboundTraffic,
       "ipsecTunnelTotalInboundPackets": ipsecTunnelTotalInboundPackets,
       "ipsecTunnelTotalOutboundPackets": ipsecTunnelTotalOutboundPackets,
       "ipsecTunnelDecryptErrors": ipsecTunnelDecryptErrors,
       "ipsecTunnelAuthErrors": ipsecTunnelAuthErrors,
       "ipsecTunnelReplayErrors": ipsecTunnelReplayErrors,
       "ipsecTunnelPolicyErrors": ipsecTunnelPolicyErrors,
       "ipsecTunnelOtherReceiveErrors": ipsecTunnelOtherReceiveErrors,
       "ipsecTunnelSendErrors": ipsecTunnelSendErrors,
       "ipsecSaTable": ipsecSaTable,
       "ipsecSaEntry": ipsecSaEntry,
       "ipsecSaIndex": ipsecSaIndex,
       "ipsecSaTunnel": ipsecSaTunnel,
       "ipsecSaInboundEspSpi": ipsecSaInboundEspSpi,
       "ipsecSaOutboundEspSpi": ipsecSaOutboundEspSpi,
       "ipsecSaInboundAhSpi": ipsecSaInboundAhSpi,
       "ipsecSaOutboundAhSpi": ipsecSaOutboundAhSpi,
       "ipsecSaInboundCompCpi": ipsecSaInboundCompCpi,
       "ipsecSaOutboundCompCpi": ipsecSaOutboundCompCpi,
       "ipsecSaCreationTime": ipsecSaCreationTime,
       "ipsecSaTimeLimit": ipsecSaTimeLimit,
       "ipsecSaTrafficLimit": ipsecSaTrafficLimit,
       "ipsecSaInboundTraffic": ipsecSaInboundTraffic,
       "ipsecSaOutboundTraffic": ipsecSaOutboundTraffic,
       "ipsecSaInboundPackets": ipsecSaInboundPackets,
       "ipsecSaOutboundPackets": ipsecSaOutboundPackets,
       "ipsecSaDecryptErrors": ipsecSaDecryptErrors,
       "ipsecSaAuthErrors": ipsecSaAuthErrors,
       "ipsecSaReplayErrors": ipsecSaReplayErrors,
       "ipsecSaOtherReceiveErrors": ipsecSaOtherReceiveErrors,
       "ipsecSaSendErrors": ipsecSaSendErrors,
       "ipsecTraps": ipsecTraps,
       "ipsecTrapsObjects": ipsecTrapsObjects,
       "ipsecTrapPermIkeNegFailure": ipsecTrapPermIkeNegFailure,
       "ipsecTrapTransIkeNegFailure": ipsecTrapTransIkeNegFailure,
       "ipsecTrapInvalidCookie": ipsecTrapInvalidCookie,
       "ipsecTrapIpsecNegFailure": ipsecTrapIpsecNegFailure,
       "ipsecTrapIpsecAuthFailure": ipsecTrapIpsecAuthFailure,
       "ipsecTrapIpsecReplayFailure": ipsecTrapIpsecReplayFailure,
       "ipsecTrapIpsecPolicyFailure": ipsecTrapIpsecPolicyFailure,
       "ipsecTrapInvalidSpi": ipsecTrapInvalidSpi,
       "ipsecSaCounts": ipsecSaCounts,
       "ipsecTotalIkeSAs": ipsecTotalIkeSAs,
       "ipsecTotalIpsecSAs": ipsecTotalIpsecSAs,
       "ipsecPermTunStats": ipsecPermTunStats,
       "ipsecCnfgPermIkeTunnels": ipsecCnfgPermIkeTunnels,
       "ipsecUpPermIkeTunnels": ipsecUpPermIkeTunnels,
       "ipsecCnfgPermIpsecTunnels": ipsecCnfgPermIpsecTunnels,
       "ipsecUpPermIpsecTunnels": ipsecUpPermIpsecTunnels,
       "ipsecTransTunStats": ipsecTransTunStats,
       "ipsecTotalTransIkeTunnels": ipsecTotalTransIkeTunnels,
       "ipsecCurrentTransIkeTunnels": ipsecCurrentTransIkeTunnels,
       "ipsecTotalTransIpsecTunnels": ipsecTotalTransIpsecTunnels,
       "ipsecCurrentTransIpsecTunnels": ipsecCurrentTransIpsecTunnels,
       "ipsecTotalTransInboundPackets": ipsecTotalTransInboundPackets,
       "ipsecTotalTransOutboundPackets": ipsecTotalTransOutboundPackets,
       "ipsecTotalTransInboundTraffic": ipsecTotalTransInboundTraffic,
       "ipsecTotalTransOutboundTraffic": ipsecTotalTransOutboundTraffic,
       "ipsecTotalTransIkeSetupFailures": ipsecTotalTransIkeSetupFailures,
       "ipsecNotifications": ipsecNotifications,
       "ipsecNotifyMessageTotalCount": ipsecNotifyMessageTotalCount,
       "ipsecNotifyCountTable": ipsecNotifyCountTable,
       "ipsecNotifyCountEntry": ipsecNotifyCountEntry,
       "ipsecNotifyMessage": ipsecNotifyMessage,
       "ipsecNotifyMessageCount": ipsecNotifyMessageCount,
       "ipsecErrorStats": ipsecErrorStats,
       "ipsecUnknownSpiErrors": ipsecUnknownSpiErrors,
       "ipsecIkeProtocolErrors": ipsecIkeProtocolErrors,
       "ipsecIpsecAuthenticationErrors": ipsecIpsecAuthenticationErrors,
       "ipsecIpsecReplayErrors": ipsecIpsecReplayErrors,
       "ipsecIpsecPolicyErrors": ipsecIpsecPolicyErrors}
)
