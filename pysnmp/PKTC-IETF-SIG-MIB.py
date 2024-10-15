# SNMP MIB module (PKTC-IETF-SIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PKTC-IETF-SIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:57 2024
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

(Dscp,) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "Dscp")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pktcIetfSigMib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 169)
)
pktcIetfSigMib.setRevisions(
        ("2007-12-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TenthdBm(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"


class PktcCodecType(Integer32, TextualConvention):
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
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("bv16", 14),
          ("g726at16", 10),
          ("g726at24", 11),
          ("g726at32", 7),
          ("g726at40", 12),
          ("g728", 8),
          ("g729", 3),
          ("g729E", 5),
          ("ilbc", 13),
          ("other", 1),
          ("pcma", 9),
          ("pcmu", 6),
          ("reserved", 4),
          ("unknown", 2))
    )



class PktcRingCadence(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 36),
    )



class PktcSigType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ncs", 2),
          ("other", 1))
    )



class DtmfCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("dtmfcode0", 0),
          ("dtmfcode1", 1),
          ("dtmfcode2", 2),
          ("dtmfcode3", 3),
          ("dtmfcode4", 4),
          ("dtmfcode5", 5),
          ("dtmfcode6", 6),
          ("dtmfcode7", 7),
          ("dtmfcode8", 8),
          ("dtmfcode9", 9),
          ("dtmfcodeA", 12),
          ("dtmfcodeB", 13),
          ("dtmfcodeC", 14),
          ("dtmfcodeD", 15),
          ("dtmfcodeHash", 11),
          ("dtmfcodeStar", 10))
    )



class PktcSubscriberSideSigProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtmf", 2),
          ("fsk", 1))
    )



# MIB Managed Objects in the order of their OIDs

_PktcSigNotification_ObjectIdentity = ObjectIdentity
pktcSigNotification = _PktcSigNotification_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 169, 0)
)
_PktcSigMibObjects_ObjectIdentity = ObjectIdentity
pktcSigMibObjects = _PktcSigMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 169, 1)
)
_PktcSigDevObjects_ObjectIdentity = ObjectIdentity
pktcSigDevObjects = _PktcSigDevObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 169, 1, 1)
)
_PktcSigDevCodecTable_Object = MibTable
pktcSigDevCodecTable = _PktcSigDevCodecTable_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pktcSigDevCodecTable.setStatus("current")
_PktcSigDevCodecEntry_Object = MibTableRow
pktcSigDevCodecEntry = _PktcSigDevCodecEntry_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 1, 1)
)
pktcSigDevCodecEntry.setIndexNames(
    (0, "PKTC-IETF-SIG-MIB", "pktcSigDevCodecComboIndex"),
    (0, "PKTC-IETF-SIG-MIB", "pktcSigDevCodecType"),
)
if mibBuilder.loadTexts:
    pktcSigDevCodecEntry.setStatus("current")


class _PktcSigDevCodecComboIndex_Type(Unsigned32):
    """Custom type pktcSigDevCodecComboIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PktcSigDevCodecComboIndex_Type.__name__ = "Unsigned32"
_PktcSigDevCodecComboIndex_Object = MibTableColumn
pktcSigDevCodecComboIndex = _PktcSigDevCodecComboIndex_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 1, 1, 1),
    _PktcSigDevCodecComboIndex_Type()
)
pktcSigDevCodecComboIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcSigDevCodecComboIndex.setStatus("current")
_PktcSigDevCodecType_Type = PktcCodecType
_PktcSigDevCodecType_Object = MibTableColumn
pktcSigDevCodecType = _PktcSigDevCodecType_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 1, 1, 2),
    _PktcSigDevCodecType_Type()
)
pktcSigDevCodecType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcSigDevCodecType.setStatus("current")


class _PktcSigDevCodecMax_Type(Unsigned32):
    """Custom type pktcSigDevCodecMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PktcSigDevCodecMax_Type.__name__ = "Unsigned32"
_PktcSigDevCodecMax_Object = MibTableColumn
pktcSigDevCodecMax = _PktcSigDevCodecMax_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 1, 1, 3),
    _PktcSigDevCodecMax_Type()
)
pktcSigDevCodecMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigDevCodecMax.setStatus("current")
_PktcSigDevEchoCancellation_Type = TruthValue
_PktcSigDevEchoCancellation_Object = MibScalar
pktcSigDevEchoCancellation = _PktcSigDevEchoCancellation_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 2),
    _PktcSigDevEchoCancellation_Type()
)
pktcSigDevEchoCancellation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigDevEchoCancellation.setStatus("current")
_PktcSigDevSilenceSuppression_Type = TruthValue
_PktcSigDevSilenceSuppression_Object = MibScalar
pktcSigDevSilenceSuppression = _PktcSigDevSilenceSuppression_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 3),
    _PktcSigDevSilenceSuppression_Type()
)
pktcSigDevSilenceSuppression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigDevSilenceSuppression.setStatus("current")


class _PktcSigDevCidSigProtocol_Type(PktcSubscriberSideSigProtocol):
    """Custom type pktcSigDevCidSigProtocol based on PktcSubscriberSideSigProtocol"""


_PktcSigDevCidSigProtocol_Object = MibScalar
pktcSigDevCidSigProtocol = _PktcSigDevCidSigProtocol_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 4),
    _PktcSigDevCidSigProtocol_Type()
)
pktcSigDevCidSigProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevCidSigProtocol.setStatus("current")
_PktcSigDevR0Cadence_Type = PktcRingCadence
_PktcSigDevR0Cadence_Object = MibScalar
pktcSigDevR0Cadence = _PktcSigDevR0Cadence_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 5),
    _PktcSigDevR0Cadence_Type()
)
pktcSigDevR0Cadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevR0Cadence.setStatus("current")
_PktcSigDevR1Cadence_Type = PktcRingCadence
_PktcSigDevR1Cadence_Object = MibScalar
pktcSigDevR1Cadence = _PktcSigDevR1Cadence_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 6),
    _PktcSigDevR1Cadence_Type()
)
pktcSigDevR1Cadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevR1Cadence.setStatus("current")
_PktcSigDevR2Cadence_Type = PktcRingCadence
_PktcSigDevR2Cadence_Object = MibScalar
pktcSigDevR2Cadence = _PktcSigDevR2Cadence_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 7),
    _PktcSigDevR2Cadence_Type()
)
pktcSigDevR2Cadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevR2Cadence.setStatus("current")
_PktcSigDevR3Cadence_Type = PktcRingCadence
_PktcSigDevR3Cadence_Object = MibScalar
pktcSigDevR3Cadence = _PktcSigDevR3Cadence_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 8),
    _PktcSigDevR3Cadence_Type()
)
pktcSigDevR3Cadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevR3Cadence.setStatus("current")
_PktcSigDevR4Cadence_Type = PktcRingCadence
_PktcSigDevR4Cadence_Object = MibScalar
pktcSigDevR4Cadence = _PktcSigDevR4Cadence_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 9),
    _PktcSigDevR4Cadence_Type()
)
pktcSigDevR4Cadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevR4Cadence.setStatus("current")
_PktcSigDevR5Cadence_Type = PktcRingCadence
_PktcSigDevR5Cadence_Object = MibScalar
pktcSigDevR5Cadence = _PktcSigDevR5Cadence_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 10),
    _PktcSigDevR5Cadence_Type()
)
pktcSigDevR5Cadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevR5Cadence.setStatus("current")
_PktcSigDevR6Cadence_Type = PktcRingCadence
_PktcSigDevR6Cadence_Object = MibScalar
pktcSigDevR6Cadence = _PktcSigDevR6Cadence_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 11),
    _PktcSigDevR6Cadence_Type()
)
pktcSigDevR6Cadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevR6Cadence.setStatus("current")
_PktcSigDevR7Cadence_Type = PktcRingCadence
_PktcSigDevR7Cadence_Object = MibScalar
pktcSigDevR7Cadence = _PktcSigDevR7Cadence_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 12),
    _PktcSigDevR7Cadence_Type()
)
pktcSigDevR7Cadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevR7Cadence.setStatus("current")
_PktcSigDevRgCadence_Type = PktcRingCadence
_PktcSigDevRgCadence_Object = MibScalar
pktcSigDevRgCadence = _PktcSigDevRgCadence_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 13),
    _PktcSigDevRgCadence_Type()
)
pktcSigDevRgCadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevRgCadence.setStatus("current")
_PktcSigDevRsCadence_Type = PktcRingCadence
_PktcSigDevRsCadence_Object = MibScalar
pktcSigDevRsCadence = _PktcSigDevRsCadence_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 14),
    _PktcSigDevRsCadence_Type()
)
pktcSigDevRsCadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevRsCadence.setStatus("current")


class _PktcSigDefCallSigDscp_Type(Dscp):
    """Custom type pktcSigDefCallSigDscp based on Dscp"""
    defaultValue = 0


_PktcSigDefCallSigDscp_Object = MibScalar
pktcSigDefCallSigDscp = _PktcSigDefCallSigDscp_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 15),
    _PktcSigDefCallSigDscp_Type()
)
pktcSigDefCallSigDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDefCallSigDscp.setStatus("current")


class _PktcSigDefMediaStreamDscp_Type(Dscp):
    """Custom type pktcSigDefMediaStreamDscp based on Dscp"""
    defaultValue = 0


_PktcSigDefMediaStreamDscp_Object = MibScalar
pktcSigDefMediaStreamDscp = _PktcSigDefMediaStreamDscp_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 16),
    _PktcSigDefMediaStreamDscp_Type()
)
pktcSigDefMediaStreamDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDefMediaStreamDscp.setStatus("current")
_PktcSigCapabilityTable_Object = MibTable
pktcSigCapabilityTable = _PktcSigCapabilityTable_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 17)
)
if mibBuilder.loadTexts:
    pktcSigCapabilityTable.setStatus("current")
_PktcSigCapabilityEntry_Object = MibTableRow
pktcSigCapabilityEntry = _PktcSigCapabilityEntry_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 17, 1)
)
pktcSigCapabilityEntry.setIndexNames(
    (0, "PKTC-IETF-SIG-MIB", "pktcSigCapabilityIndex"),
)
if mibBuilder.loadTexts:
    pktcSigCapabilityEntry.setStatus("current")


class _PktcSigCapabilityIndex_Type(Unsigned32):
    """Custom type pktcSigCapabilityIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PktcSigCapabilityIndex_Type.__name__ = "Unsigned32"
_PktcSigCapabilityIndex_Object = MibTableColumn
pktcSigCapabilityIndex = _PktcSigCapabilityIndex_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 17, 1, 1),
    _PktcSigCapabilityIndex_Type()
)
pktcSigCapabilityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcSigCapabilityIndex.setStatus("current")
_PktcSigCapabilityType_Type = PktcSigType
_PktcSigCapabilityType_Object = MibTableColumn
pktcSigCapabilityType = _PktcSigCapabilityType_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 17, 1, 2),
    _PktcSigCapabilityType_Type()
)
pktcSigCapabilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigCapabilityType.setStatus("current")
_PktcSigCapabilityVersion_Type = SnmpAdminString
_PktcSigCapabilityVersion_Object = MibTableColumn
pktcSigCapabilityVersion = _PktcSigCapabilityVersion_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 17, 1, 3),
    _PktcSigCapabilityVersion_Type()
)
pktcSigCapabilityVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigCapabilityVersion.setStatus("current")
_PktcSigCapabilityVendorExt_Type = SnmpAdminString
_PktcSigCapabilityVendorExt_Object = MibTableColumn
pktcSigCapabilityVendorExt = _PktcSigCapabilityVendorExt_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 17, 1, 4),
    _PktcSigCapabilityVendorExt_Type()
)
pktcSigCapabilityVendorExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigCapabilityVendorExt.setStatus("current")


class _PktcSigDefNcsReceiveUdpPort_Type(InetPortNumber):
    """Custom type pktcSigDefNcsReceiveUdpPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_PktcSigDefNcsReceiveUdpPort_Type.__name__ = "InetPortNumber"
_PktcSigDefNcsReceiveUdpPort_Object = MibScalar
pktcSigDefNcsReceiveUdpPort = _PktcSigDefNcsReceiveUdpPort_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 18),
    _PktcSigDefNcsReceiveUdpPort_Type()
)
pktcSigDefNcsReceiveUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigDefNcsReceiveUdpPort.setStatus("current")


class _PktcSigPowerRingFrequency_Type(Integer32):
    """Custom type pktcSigPowerRingFrequency based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("f15Hz", 5),
          ("f16Hz", 6),
          ("f20Hz", 1),
          ("f22Hz", 7),
          ("f23Hz", 8),
          ("f25Hz", 2),
          ("f33Point33Hz", 3),
          ("f45Hz", 9),
          ("f50Hz", 4))
    )


_PktcSigPowerRingFrequency_Type.__name__ = "Integer32"
_PktcSigPowerRingFrequency_Object = MibScalar
pktcSigPowerRingFrequency = _PktcSigPowerRingFrequency_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 19),
    _PktcSigPowerRingFrequency_Type()
)
pktcSigPowerRingFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigPowerRingFrequency.setStatus("current")
_PktcSigPulseSignalTable_Object = MibTable
pktcSigPulseSignalTable = _PktcSigPulseSignalTable_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 20)
)
if mibBuilder.loadTexts:
    pktcSigPulseSignalTable.setStatus("current")
_PktcSigPulseSignalEntry_Object = MibTableRow
pktcSigPulseSignalEntry = _PktcSigPulseSignalEntry_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 20, 1)
)
pktcSigPulseSignalEntry.setIndexNames(
    (0, "PKTC-IETF-SIG-MIB", "pktcSigPulseSignalType"),
)
if mibBuilder.loadTexts:
    pktcSigPulseSignalEntry.setStatus("current")


class _PktcSigPulseSignalType_Type(Integer32):
    """Custom type pktcSigPulseSignalType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("enableMeterPulse", 4),
          ("initialRing", 1),
          ("meterPulseBurst", 5),
          ("pulseLoopClose", 2),
          ("pulseLoopOpen", 3),
          ("pulseNoBattery", 6),
          ("pulseNormalPolarity", 7),
          ("pulseReducedBattery", 8),
          ("pulseReversePolarity", 9))
    )


_PktcSigPulseSignalType_Type.__name__ = "Integer32"
_PktcSigPulseSignalType_Object = MibTableColumn
pktcSigPulseSignalType = _PktcSigPulseSignalType_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 20, 1, 1),
    _PktcSigPulseSignalType_Type()
)
pktcSigPulseSignalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcSigPulseSignalType.setStatus("current")


class _PktcSigPulseSignalFrequency_Type(Integer32):
    """Custom type pktcSigPulseSignalFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sixteenthousand", 3),
          ("twelvethousand", 2),
          ("twentyfive", 1))
    )


_PktcSigPulseSignalFrequency_Type.__name__ = "Integer32"
_PktcSigPulseSignalFrequency_Object = MibTableColumn
pktcSigPulseSignalFrequency = _PktcSigPulseSignalFrequency_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 20, 1, 2),
    _PktcSigPulseSignalFrequency_Type()
)
pktcSigPulseSignalFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigPulseSignalFrequency.setStatus("current")


class _PktcSigPulseSignalDbLevel_Type(TenthdBm):
    """Custom type pktcSigPulseSignalDbLevel based on TenthdBm"""
    defaultValue = -135

    subtypeSpec = TenthdBm.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-350, 0),
    )


_PktcSigPulseSignalDbLevel_Type.__name__ = "TenthdBm"
_PktcSigPulseSignalDbLevel_Object = MibTableColumn
pktcSigPulseSignalDbLevel = _PktcSigPulseSignalDbLevel_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 20, 1, 3),
    _PktcSigPulseSignalDbLevel_Type()
)
pktcSigPulseSignalDbLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigPulseSignalDbLevel.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigPulseSignalDbLevel.setUnits("1/10 of a dBm")


class _PktcSigPulseSignalDuration_Type(Unsigned32):
    """Custom type pktcSigPulseSignalDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_PktcSigPulseSignalDuration_Type.__name__ = "Unsigned32"
_PktcSigPulseSignalDuration_Object = MibTableColumn
pktcSigPulseSignalDuration = _PktcSigPulseSignalDuration_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 20, 1, 4),
    _PktcSigPulseSignalDuration_Type()
)
pktcSigPulseSignalDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigPulseSignalDuration.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigPulseSignalDuration.setUnits("Milliseconds")


class _PktcSigPulseSignalPulseInterval_Type(Unsigned32):
    """Custom type pktcSigPulseSignalPulseInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_PktcSigPulseSignalPulseInterval_Type.__name__ = "Unsigned32"
_PktcSigPulseSignalPulseInterval_Object = MibTableColumn
pktcSigPulseSignalPulseInterval = _PktcSigPulseSignalPulseInterval_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 20, 1, 5),
    _PktcSigPulseSignalPulseInterval_Type()
)
pktcSigPulseSignalPulseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigPulseSignalPulseInterval.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigPulseSignalPulseInterval.setUnits("Milliseconds")


class _PktcSigPulseSignalRepeatCount_Type(Unsigned32):
    """Custom type pktcSigPulseSignalRepeatCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_PktcSigPulseSignalRepeatCount_Type.__name__ = "Unsigned32"
_PktcSigPulseSignalRepeatCount_Object = MibTableColumn
pktcSigPulseSignalRepeatCount = _PktcSigPulseSignalRepeatCount_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 20, 1, 6),
    _PktcSigPulseSignalRepeatCount_Type()
)
pktcSigPulseSignalRepeatCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigPulseSignalRepeatCount.setStatus("current")


class _PktcSigDevCidMode_Type(Integer32):
    """Custom type pktcSigDevCidMode based on Integer32"""
    defaultValue = 3

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
        *(("dtAsETS", 2),
          ("duringRingingETS", 1),
          ("lrAsETS", 4),
          ("lrETS", 5),
          ("rpAsETS", 3))
    )


_PktcSigDevCidMode_Type.__name__ = "Integer32"
_PktcSigDevCidMode_Object = MibScalar
pktcSigDevCidMode = _PktcSigDevCidMode_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 21),
    _PktcSigDevCidMode_Type()
)
pktcSigDevCidMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevCidMode.setStatus("current")


class _PktcSigDevCidAfterRing_Type(Unsigned32):
    """Custom type pktcSigDevCidAfterRing based on Unsigned32"""
    defaultValue = 550

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(50, 2000),
    )


_PktcSigDevCidAfterRing_Type.__name__ = "Unsigned32"
_PktcSigDevCidAfterRing_Object = MibScalar
pktcSigDevCidAfterRing = _PktcSigDevCidAfterRing_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 22),
    _PktcSigDevCidAfterRing_Type()
)
pktcSigDevCidAfterRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevCidAfterRing.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigDevCidAfterRing.setUnits("Milliseconds")


class _PktcSigDevCidAfterDTAS_Type(Unsigned32):
    """Custom type pktcSigDevCidAfterDTAS based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(45, 500),
    )


_PktcSigDevCidAfterDTAS_Type.__name__ = "Unsigned32"
_PktcSigDevCidAfterDTAS_Object = MibScalar
pktcSigDevCidAfterDTAS = _PktcSigDevCidAfterDTAS_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 23),
    _PktcSigDevCidAfterDTAS_Type()
)
pktcSigDevCidAfterDTAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevCidAfterDTAS.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigDevCidAfterDTAS.setUnits("Milliseconds")


class _PktcSigDevCidAfterRPAS_Type(Unsigned32):
    """Custom type pktcSigDevCidAfterRPAS based on Unsigned32"""
    defaultValue = 650

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(500, 800),
    )


_PktcSigDevCidAfterRPAS_Type.__name__ = "Unsigned32"
_PktcSigDevCidAfterRPAS_Object = MibScalar
pktcSigDevCidAfterRPAS = _PktcSigDevCidAfterRPAS_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 24),
    _PktcSigDevCidAfterRPAS_Type()
)
pktcSigDevCidAfterRPAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevCidAfterRPAS.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigDevCidAfterRPAS.setUnits("Milliseconds")


class _PktcSigDevRingAfterCID_Type(Unsigned32):
    """Custom type pktcSigDevRingAfterCID based on Unsigned32"""
    defaultValue = 250

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(50, 500),
    )


_PktcSigDevRingAfterCID_Type.__name__ = "Unsigned32"
_PktcSigDevRingAfterCID_Object = MibScalar
pktcSigDevRingAfterCID = _PktcSigDevRingAfterCID_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 25),
    _PktcSigDevRingAfterCID_Type()
)
pktcSigDevRingAfterCID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevRingAfterCID.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigDevRingAfterCID.setUnits("Milliseconds")


class _PktcSigDevCidDTASAfterLR_Type(Unsigned32):
    """Custom type pktcSigDevCidDTASAfterLR based on Unsigned32"""
    defaultValue = 250

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 655),
    )


_PktcSigDevCidDTASAfterLR_Type.__name__ = "Unsigned32"
_PktcSigDevCidDTASAfterLR_Object = MibScalar
pktcSigDevCidDTASAfterLR = _PktcSigDevCidDTASAfterLR_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 26),
    _PktcSigDevCidDTASAfterLR_Type()
)
pktcSigDevCidDTASAfterLR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevCidDTASAfterLR.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigDevCidDTASAfterLR.setUnits("Milliseconds")


class _PktcSigDevVmwiMode_Type(Integer32):
    """Custom type pktcSigDevVmwiMode based on Integer32"""
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
        *(("dtAsETS", 1),
          ("lrAsETS", 3),
          ("lrETS", 5),
          ("osi", 4),
          ("rpAsETS", 2))
    )


_PktcSigDevVmwiMode_Type.__name__ = "Integer32"
_PktcSigDevVmwiMode_Object = MibScalar
pktcSigDevVmwiMode = _PktcSigDevVmwiMode_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 27),
    _PktcSigDevVmwiMode_Type()
)
pktcSigDevVmwiMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevVmwiMode.setStatus("current")


class _PktcSigDevVmwiAfterDTAS_Type(Unsigned32):
    """Custom type pktcSigDevVmwiAfterDTAS based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(45, 500),
    )


_PktcSigDevVmwiAfterDTAS_Type.__name__ = "Unsigned32"
_PktcSigDevVmwiAfterDTAS_Object = MibScalar
pktcSigDevVmwiAfterDTAS = _PktcSigDevVmwiAfterDTAS_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 28),
    _PktcSigDevVmwiAfterDTAS_Type()
)
pktcSigDevVmwiAfterDTAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevVmwiAfterDTAS.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigDevVmwiAfterDTAS.setUnits("Milliseconds")


class _PktcSigDevVmwiAfterRPAS_Type(Unsigned32):
    """Custom type pktcSigDevVmwiAfterRPAS based on Unsigned32"""
    defaultValue = 650

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(500, 800),
    )


_PktcSigDevVmwiAfterRPAS_Type.__name__ = "Unsigned32"
_PktcSigDevVmwiAfterRPAS_Object = MibScalar
pktcSigDevVmwiAfterRPAS = _PktcSigDevVmwiAfterRPAS_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 29),
    _PktcSigDevVmwiAfterRPAS_Type()
)
pktcSigDevVmwiAfterRPAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevVmwiAfterRPAS.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigDevVmwiAfterRPAS.setUnits("Milliseconds")


class _PktcSigDevVmwiDTASAfterLR_Type(Unsigned32):
    """Custom type pktcSigDevVmwiDTASAfterLR based on Unsigned32"""
    defaultValue = 250

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(50, 655),
    )


_PktcSigDevVmwiDTASAfterLR_Type.__name__ = "Unsigned32"
_PktcSigDevVmwiDTASAfterLR_Object = MibScalar
pktcSigDevVmwiDTASAfterLR = _PktcSigDevVmwiDTASAfterLR_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 30),
    _PktcSigDevVmwiDTASAfterLR_Type()
)
pktcSigDevVmwiDTASAfterLR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevVmwiDTASAfterLR.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigDevVmwiDTASAfterLR.setUnits("Milliseconds")
_PktcSigDevRingCadenceTable_Object = MibTable
pktcSigDevRingCadenceTable = _PktcSigDevRingCadenceTable_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 31)
)
if mibBuilder.loadTexts:
    pktcSigDevRingCadenceTable.setStatus("current")
_PktcSigDevRingCadenceEntry_Object = MibTableRow
pktcSigDevRingCadenceEntry = _PktcSigDevRingCadenceEntry_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 31, 1)
)
pktcSigDevRingCadenceEntry.setIndexNames(
    (0, "PKTC-IETF-SIG-MIB", "pktcSigDevRingCadenceIndex"),
)
if mibBuilder.loadTexts:
    pktcSigDevRingCadenceEntry.setStatus("current")


class _PktcSigDevRingCadenceIndex_Type(Unsigned32):
    """Custom type pktcSigDevRingCadenceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_PktcSigDevRingCadenceIndex_Type.__name__ = "Unsigned32"
_PktcSigDevRingCadenceIndex_Object = MibTableColumn
pktcSigDevRingCadenceIndex = _PktcSigDevRingCadenceIndex_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 31, 1, 1),
    _PktcSigDevRingCadenceIndex_Type()
)
pktcSigDevRingCadenceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcSigDevRingCadenceIndex.setStatus("current")
_PktcSigDevRingCadence_Type = PktcRingCadence
_PktcSigDevRingCadence_Object = MibTableColumn
pktcSigDevRingCadence = _PktcSigDevRingCadence_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 31, 1, 2),
    _PktcSigDevRingCadence_Type()
)
pktcSigDevRingCadence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevRingCadence.setStatus("current")
_PktcSigDevToneTable_Object = MibTable
pktcSigDevToneTable = _PktcSigDevToneTable_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 32)
)
if mibBuilder.loadTexts:
    pktcSigDevToneTable.setStatus("current")
_PktcSigDevToneEntry_Object = MibTableRow
pktcSigDevToneEntry = _PktcSigDevToneEntry_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 32, 1)
)
pktcSigDevToneEntry.setIndexNames(
    (0, "PKTC-IETF-SIG-MIB", "pktcSigDevToneType"),
    (0, "PKTC-IETF-SIG-MIB", "pktcSigDevToneFreqGroup"),
)
if mibBuilder.loadTexts:
    pktcSigDevToneEntry.setStatus("current")


class _PktcSigDevToneType_Type(Integer32):
    """Custom type pktcSigDevToneType based on Integer32"""
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
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("alertingSignal", 13),
          ("busy", 1),
          ("callWaiting1", 9),
          ("callWaiting2", 10),
          ("callWaiting3", 11),
          ("callWaiting4", 12),
          ("confirmation", 2),
          ("congestion", 17),
          ("dial", 3),
          ("messageWaiting", 4),
          ("offHookWarning", 5),
          ("reOrder", 7),
          ("release", 16),
          ("ringBack", 6),
          ("specialDial", 14),
          ("specialInfo", 15),
          ("stutterdial", 8),
          ("userDefined1", 18),
          ("userDefined2", 19),
          ("userDefined3", 20),
          ("userDefined4", 21))
    )


_PktcSigDevToneType_Type.__name__ = "Integer32"
_PktcSigDevToneType_Object = MibTableColumn
pktcSigDevToneType = _PktcSigDevToneType_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 32, 1, 1),
    _PktcSigDevToneType_Type()
)
pktcSigDevToneType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcSigDevToneType.setStatus("current")


class _PktcSigDevToneFreqGroup_Type(Unsigned32):
    """Custom type pktcSigDevToneFreqGroup based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_PktcSigDevToneFreqGroup_Type.__name__ = "Unsigned32"
_PktcSigDevToneFreqGroup_Object = MibTableColumn
pktcSigDevToneFreqGroup = _PktcSigDevToneFreqGroup_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 32, 1, 2),
    _PktcSigDevToneFreqGroup_Type()
)
pktcSigDevToneFreqGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcSigDevToneFreqGroup.setStatus("current")


class _PktcSigDevToneFreqCounter_Type(Unsigned32):
    """Custom type pktcSigDevToneFreqCounter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PktcSigDevToneFreqCounter_Type.__name__ = "Unsigned32"
_PktcSigDevToneFreqCounter_Object = MibTableColumn
pktcSigDevToneFreqCounter = _PktcSigDevToneFreqCounter_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 32, 1, 3),
    _PktcSigDevToneFreqCounter_Type()
)
pktcSigDevToneFreqCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigDevToneFreqCounter.setStatus("current")


class _PktcSigDevToneWholeToneRepeatCount_Type(Unsigned32):
    """Custom type pktcSigDevToneWholeToneRepeatCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_PktcSigDevToneWholeToneRepeatCount_Type.__name__ = "Unsigned32"
_PktcSigDevToneWholeToneRepeatCount_Object = MibTableColumn
pktcSigDevToneWholeToneRepeatCount = _PktcSigDevToneWholeToneRepeatCount_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 32, 1, 4),
    _PktcSigDevToneWholeToneRepeatCount_Type()
)
pktcSigDevToneWholeToneRepeatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigDevToneWholeToneRepeatCount.setStatus("current")
_PktcSigDevToneSteady_Type = TruthValue
_PktcSigDevToneSteady_Object = MibTableColumn
pktcSigDevToneSteady = _PktcSigDevToneSteady_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 32, 1, 5),
    _PktcSigDevToneSteady_Type()
)
pktcSigDevToneSteady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigDevToneSteady.setStatus("current")
_PktcSigDevMultiFreqToneTable_Object = MibTable
pktcSigDevMultiFreqToneTable = _PktcSigDevMultiFreqToneTable_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 33)
)
if mibBuilder.loadTexts:
    pktcSigDevMultiFreqToneTable.setStatus("current")
_PktcSigDevMultiFreqToneEntry_Object = MibTableRow
pktcSigDevMultiFreqToneEntry = _PktcSigDevMultiFreqToneEntry_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 33, 1)
)
pktcSigDevMultiFreqToneEntry.setIndexNames(
    (0, "PKTC-IETF-SIG-MIB", "pktcSigDevToneType"),
    (0, "PKTC-IETF-SIG-MIB", "pktcSigDevToneNumber"),
)
if mibBuilder.loadTexts:
    pktcSigDevMultiFreqToneEntry.setStatus("current")


class _PktcSigDevToneNumber_Type(Unsigned32):
    """Custom type pktcSigDevToneNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PktcSigDevToneNumber_Type.__name__ = "Unsigned32"
_PktcSigDevToneNumber_Object = MibTableColumn
pktcSigDevToneNumber = _PktcSigDevToneNumber_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 33, 1, 1),
    _PktcSigDevToneNumber_Type()
)
pktcSigDevToneNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcSigDevToneNumber.setStatus("current")


class _PktcSigDevToneFirstFreqValue_Type(Unsigned32):
    """Custom type pktcSigDevToneFirstFreqValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_PktcSigDevToneFirstFreqValue_Type.__name__ = "Unsigned32"
_PktcSigDevToneFirstFreqValue_Object = MibTableColumn
pktcSigDevToneFirstFreqValue = _PktcSigDevToneFirstFreqValue_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 33, 1, 2),
    _PktcSigDevToneFirstFreqValue_Type()
)
pktcSigDevToneFirstFreqValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigDevToneFirstFreqValue.setStatus("current")


class _PktcSigDevToneSecondFreqValue_Type(Unsigned32):
    """Custom type pktcSigDevToneSecondFreqValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_PktcSigDevToneSecondFreqValue_Type.__name__ = "Unsigned32"
_PktcSigDevToneSecondFreqValue_Object = MibTableColumn
pktcSigDevToneSecondFreqValue = _PktcSigDevToneSecondFreqValue_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 33, 1, 3),
    _PktcSigDevToneSecondFreqValue_Type()
)
pktcSigDevToneSecondFreqValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigDevToneSecondFreqValue.setStatus("current")


class _PktcSigDevToneThirdFreqValue_Type(Unsigned32):
    """Custom type pktcSigDevToneThirdFreqValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_PktcSigDevToneThirdFreqValue_Type.__name__ = "Unsigned32"
_PktcSigDevToneThirdFreqValue_Object = MibTableColumn
pktcSigDevToneThirdFreqValue = _PktcSigDevToneThirdFreqValue_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 33, 1, 4),
    _PktcSigDevToneThirdFreqValue_Type()
)
pktcSigDevToneThirdFreqValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigDevToneThirdFreqValue.setStatus("current")


class _PktcSigDevToneFourthFreqValue_Type(Unsigned32):
    """Custom type pktcSigDevToneFourthFreqValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_PktcSigDevToneFourthFreqValue_Type.__name__ = "Unsigned32"
_PktcSigDevToneFourthFreqValue_Object = MibTableColumn
pktcSigDevToneFourthFreqValue = _PktcSigDevToneFourthFreqValue_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 33, 1, 5),
    _PktcSigDevToneFourthFreqValue_Type()
)
pktcSigDevToneFourthFreqValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigDevToneFourthFreqValue.setStatus("current")


class _PktcSigDevToneFreqMode_Type(Integer32):
    """Custom type pktcSigDevToneFreqMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("firstModulatedBySecond", 1),
          ("summation", 2))
    )


_PktcSigDevToneFreqMode_Type.__name__ = "Integer32"
_PktcSigDevToneFreqMode_Object = MibTableColumn
pktcSigDevToneFreqMode = _PktcSigDevToneFreqMode_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 33, 1, 6),
    _PktcSigDevToneFreqMode_Type()
)
pktcSigDevToneFreqMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigDevToneFreqMode.setStatus("current")


class _PktcSigDevToneFreqAmpModePrtg_Type(Unsigned32):
    """Custom type pktcSigDevToneFreqAmpModePrtg based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PktcSigDevToneFreqAmpModePrtg_Type.__name__ = "Unsigned32"
_PktcSigDevToneFreqAmpModePrtg_Object = MibTableColumn
pktcSigDevToneFreqAmpModePrtg = _PktcSigDevToneFreqAmpModePrtg_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 33, 1, 7),
    _PktcSigDevToneFreqAmpModePrtg_Type()
)
pktcSigDevToneFreqAmpModePrtg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigDevToneFreqAmpModePrtg.setStatus("current")


class _PktcSigDevToneDbLevel_Type(TenthdBm):
    """Custom type pktcSigDevToneDbLevel based on TenthdBm"""
    defaultValue = -120

    subtypeSpec = TenthdBm.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-250, -110),
    )


_PktcSigDevToneDbLevel_Type.__name__ = "TenthdBm"
_PktcSigDevToneDbLevel_Object = MibTableColumn
pktcSigDevToneDbLevel = _PktcSigDevToneDbLevel_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 33, 1, 8),
    _PktcSigDevToneDbLevel_Type()
)
pktcSigDevToneDbLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigDevToneDbLevel.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigDevToneDbLevel.setUnits("1/10 of a dBm")


class _PktcSigDevToneFreqOnDuration_Type(Unsigned32):
    """Custom type pktcSigDevToneFreqOnDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_PktcSigDevToneFreqOnDuration_Type.__name__ = "Unsigned32"
_PktcSigDevToneFreqOnDuration_Object = MibTableColumn
pktcSigDevToneFreqOnDuration = _PktcSigDevToneFreqOnDuration_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 33, 1, 9),
    _PktcSigDevToneFreqOnDuration_Type()
)
pktcSigDevToneFreqOnDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigDevToneFreqOnDuration.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigDevToneFreqOnDuration.setUnits("milliseconds")


class _PktcSigDevToneFreqOffDuration_Type(Unsigned32):
    """Custom type pktcSigDevToneFreqOffDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_PktcSigDevToneFreqOffDuration_Type.__name__ = "Unsigned32"
_PktcSigDevToneFreqOffDuration_Object = MibTableColumn
pktcSigDevToneFreqOffDuration = _PktcSigDevToneFreqOffDuration_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 33, 1, 10),
    _PktcSigDevToneFreqOffDuration_Type()
)
pktcSigDevToneFreqOffDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigDevToneFreqOffDuration.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigDevToneFreqOffDuration.setUnits("milliseconds")


class _PktcSigDevToneFreqRepeatCount_Type(Unsigned32):
    """Custom type pktcSigDevToneFreqRepeatCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_PktcSigDevToneFreqRepeatCount_Type.__name__ = "Unsigned32"
_PktcSigDevToneFreqRepeatCount_Object = MibTableColumn
pktcSigDevToneFreqRepeatCount = _PktcSigDevToneFreqRepeatCount_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 33, 1, 11),
    _PktcSigDevToneFreqRepeatCount_Type()
)
pktcSigDevToneFreqRepeatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigDevToneFreqRepeatCount.setStatus("current")


class _PktcSigDevCidDelayAfterLR_Type(Unsigned32):
    """Custom type pktcSigDevCidDelayAfterLR based on Unsigned32"""
    defaultValue = 400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 800),
    )


_PktcSigDevCidDelayAfterLR_Type.__name__ = "Unsigned32"
_PktcSigDevCidDelayAfterLR_Object = MibScalar
pktcSigDevCidDelayAfterLR = _PktcSigDevCidDelayAfterLR_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 34),
    _PktcSigDevCidDelayAfterLR_Type()
)
pktcSigDevCidDelayAfterLR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevCidDelayAfterLR.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigDevCidDelayAfterLR.setUnits("Milliseconds")


class _PktcSigDevCidDtmfStartCode_Type(DtmfCode):
    """Custom type pktcSigDevCidDtmfStartCode based on DtmfCode"""


_PktcSigDevCidDtmfStartCode_Object = MibScalar
pktcSigDevCidDtmfStartCode = _PktcSigDevCidDtmfStartCode_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 35),
    _PktcSigDevCidDtmfStartCode_Type()
)
pktcSigDevCidDtmfStartCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevCidDtmfStartCode.setStatus("current")


class _PktcSigDevCidDtmfEndCode_Type(DtmfCode):
    """Custom type pktcSigDevCidDtmfEndCode based on DtmfCode"""


_PktcSigDevCidDtmfEndCode_Object = MibScalar
pktcSigDevCidDtmfEndCode = _PktcSigDevCidDtmfEndCode_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 36),
    _PktcSigDevCidDtmfEndCode_Type()
)
pktcSigDevCidDtmfEndCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevCidDtmfEndCode.setStatus("current")


class _PktcSigDevVmwiSigProtocol_Type(PktcSubscriberSideSigProtocol):
    """Custom type pktcSigDevVmwiSigProtocol based on PktcSubscriberSideSigProtocol"""


_PktcSigDevVmwiSigProtocol_Object = MibScalar
pktcSigDevVmwiSigProtocol = _PktcSigDevVmwiSigProtocol_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 37),
    _PktcSigDevVmwiSigProtocol_Type()
)
pktcSigDevVmwiSigProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevVmwiSigProtocol.setStatus("current")


class _PktcSigDevVmwiDelayAfterLR_Type(Unsigned32):
    """Custom type pktcSigDevVmwiDelayAfterLR based on Unsigned32"""
    defaultValue = 400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(300, 800),
    )


_PktcSigDevVmwiDelayAfterLR_Type.__name__ = "Unsigned32"
_PktcSigDevVmwiDelayAfterLR_Object = MibScalar
pktcSigDevVmwiDelayAfterLR = _PktcSigDevVmwiDelayAfterLR_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 38),
    _PktcSigDevVmwiDelayAfterLR_Type()
)
pktcSigDevVmwiDelayAfterLR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevVmwiDelayAfterLR.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigDevVmwiDelayAfterLR.setUnits("Milliseconds")


class _PktcSigDevVmwiDtmfStartCode_Type(DtmfCode):
    """Custom type pktcSigDevVmwiDtmfStartCode based on DtmfCode"""


_PktcSigDevVmwiDtmfStartCode_Object = MibScalar
pktcSigDevVmwiDtmfStartCode = _PktcSigDevVmwiDtmfStartCode_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 39),
    _PktcSigDevVmwiDtmfStartCode_Type()
)
pktcSigDevVmwiDtmfStartCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevVmwiDtmfStartCode.setStatus("current")


class _PktcSigDevVmwiDtmfEndCode_Type(DtmfCode):
    """Custom type pktcSigDevVmwiDtmfEndCode based on DtmfCode"""


_PktcSigDevVmwiDtmfEndCode_Object = MibScalar
pktcSigDevVmwiDtmfEndCode = _PktcSigDevVmwiDtmfEndCode_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 40),
    _PktcSigDevVmwiDtmfEndCode_Type()
)
pktcSigDevVmwiDtmfEndCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevVmwiDtmfEndCode.setStatus("current")


class _PktcSigDevrpAsDtsDuration_Type(Unsigned32):
    """Custom type pktcSigDevrpAsDtsDuration based on Unsigned32"""
    defaultValue = 250

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(200, 500),
    )


_PktcSigDevrpAsDtsDuration_Type.__name__ = "Unsigned32"
_PktcSigDevrpAsDtsDuration_Object = MibScalar
pktcSigDevrpAsDtsDuration = _PktcSigDevrpAsDtsDuration_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 1, 41),
    _PktcSigDevrpAsDtsDuration_Type()
)
pktcSigDevrpAsDtsDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcSigDevrpAsDtsDuration.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigDevrpAsDtsDuration.setUnits("Milliseconds")
_PktcSigEndPntConfigObjects_ObjectIdentity = ObjectIdentity
pktcSigEndPntConfigObjects = _PktcSigEndPntConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 169, 1, 2)
)
_PktcSigEndPntConfigTable_Object = MibTable
pktcSigEndPntConfigTable = _PktcSigEndPntConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pktcSigEndPntConfigTable.setStatus("current")
_PktcSigEndPntConfigEntry_Object = MibTableRow
pktcSigEndPntConfigEntry = _PktcSigEndPntConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1)
)
pktcSigEndPntConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pktcSigEndPntConfigEntry.setStatus("current")


class _PktcSigEndPntConfigCallAgentId_Type(SnmpAdminString):
    """Custom type pktcSigEndPntConfigCallAgentId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 255),
    )


_PktcSigEndPntConfigCallAgentId_Type.__name__ = "SnmpAdminString"
_PktcSigEndPntConfigCallAgentId_Object = MibTableColumn
pktcSigEndPntConfigCallAgentId = _PktcSigEndPntConfigCallAgentId_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 1),
    _PktcSigEndPntConfigCallAgentId_Type()
)
pktcSigEndPntConfigCallAgentId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigCallAgentId.setStatus("current")


class _PktcSigEndPntConfigCallAgentUdpPort_Type(InetPortNumber):
    """Custom type pktcSigEndPntConfigCallAgentUdpPort based on InetPortNumber"""
    defaultValue = 2727

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_PktcSigEndPntConfigCallAgentUdpPort_Type.__name__ = "InetPortNumber"
_PktcSigEndPntConfigCallAgentUdpPort_Object = MibTableColumn
pktcSigEndPntConfigCallAgentUdpPort = _PktcSigEndPntConfigCallAgentUdpPort_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 2),
    _PktcSigEndPntConfigCallAgentUdpPort_Type()
)
pktcSigEndPntConfigCallAgentUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigCallAgentUdpPort.setStatus("current")


class _PktcSigEndPntConfigPartialDialTO_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigPartialDialTO based on Unsigned32"""
    defaultValue = 16


_PktcSigEndPntConfigPartialDialTO_Object = MibTableColumn
pktcSigEndPntConfigPartialDialTO = _PktcSigEndPntConfigPartialDialTO_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 3),
    _PktcSigEndPntConfigPartialDialTO_Type()
)
pktcSigEndPntConfigPartialDialTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigPartialDialTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigPartialDialTO.setUnits("seconds")


class _PktcSigEndPntConfigCriticalDialTO_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigCriticalDialTO based on Unsigned32"""
    defaultValue = 4


_PktcSigEndPntConfigCriticalDialTO_Object = MibTableColumn
pktcSigEndPntConfigCriticalDialTO = _PktcSigEndPntConfigCriticalDialTO_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 4),
    _PktcSigEndPntConfigCriticalDialTO_Type()
)
pktcSigEndPntConfigCriticalDialTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigCriticalDialTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigCriticalDialTO.setUnits("seconds")


class _PktcSigEndPntConfigBusyToneTO_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigBusyToneTO based on Unsigned32"""
    defaultValue = 30


_PktcSigEndPntConfigBusyToneTO_Object = MibTableColumn
pktcSigEndPntConfigBusyToneTO = _PktcSigEndPntConfigBusyToneTO_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 5),
    _PktcSigEndPntConfigBusyToneTO_Type()
)
pktcSigEndPntConfigBusyToneTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigBusyToneTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigBusyToneTO.setUnits("seconds")


class _PktcSigEndPntConfigDialToneTO_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigDialToneTO based on Unsigned32"""
    defaultValue = 16


_PktcSigEndPntConfigDialToneTO_Object = MibTableColumn
pktcSigEndPntConfigDialToneTO = _PktcSigEndPntConfigDialToneTO_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 6),
    _PktcSigEndPntConfigDialToneTO_Type()
)
pktcSigEndPntConfigDialToneTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigDialToneTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigDialToneTO.setUnits("seconds")


class _PktcSigEndPntConfigMessageWaitingTO_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigMessageWaitingTO based on Unsigned32"""
    defaultValue = 16


_PktcSigEndPntConfigMessageWaitingTO_Object = MibTableColumn
pktcSigEndPntConfigMessageWaitingTO = _PktcSigEndPntConfigMessageWaitingTO_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 7),
    _PktcSigEndPntConfigMessageWaitingTO_Type()
)
pktcSigEndPntConfigMessageWaitingTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigMessageWaitingTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigMessageWaitingTO.setUnits("seconds")


class _PktcSigEndPntConfigOffHookWarnToneTO_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigOffHookWarnToneTO based on Unsigned32"""
    defaultValue = 0


_PktcSigEndPntConfigOffHookWarnToneTO_Object = MibTableColumn
pktcSigEndPntConfigOffHookWarnToneTO = _PktcSigEndPntConfigOffHookWarnToneTO_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 8),
    _PktcSigEndPntConfigOffHookWarnToneTO_Type()
)
pktcSigEndPntConfigOffHookWarnToneTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigOffHookWarnToneTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigOffHookWarnToneTO.setUnits("seconds")


class _PktcSigEndPntConfigRingingTO_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigRingingTO based on Unsigned32"""
    defaultValue = 180


_PktcSigEndPntConfigRingingTO_Object = MibTableColumn
pktcSigEndPntConfigRingingTO = _PktcSigEndPntConfigRingingTO_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 9),
    _PktcSigEndPntConfigRingingTO_Type()
)
pktcSigEndPntConfigRingingTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigRingingTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigRingingTO.setUnits("seconds")


class _PktcSigEndPntConfigRingBackTO_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigRingBackTO based on Unsigned32"""
    defaultValue = 180


_PktcSigEndPntConfigRingBackTO_Object = MibTableColumn
pktcSigEndPntConfigRingBackTO = _PktcSigEndPntConfigRingBackTO_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 10),
    _PktcSigEndPntConfigRingBackTO_Type()
)
pktcSigEndPntConfigRingBackTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigRingBackTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigRingBackTO.setUnits("seconds")


class _PktcSigEndPntConfigReorderToneTO_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigReorderToneTO based on Unsigned32"""
    defaultValue = 30


_PktcSigEndPntConfigReorderToneTO_Object = MibTableColumn
pktcSigEndPntConfigReorderToneTO = _PktcSigEndPntConfigReorderToneTO_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 11),
    _PktcSigEndPntConfigReorderToneTO_Type()
)
pktcSigEndPntConfigReorderToneTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigReorderToneTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigReorderToneTO.setUnits("seconds")


class _PktcSigEndPntConfigStutterDialToneTO_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigStutterDialToneTO based on Unsigned32"""
    defaultValue = 16


_PktcSigEndPntConfigStutterDialToneTO_Object = MibTableColumn
pktcSigEndPntConfigStutterDialToneTO = _PktcSigEndPntConfigStutterDialToneTO_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 12),
    _PktcSigEndPntConfigStutterDialToneTO_Type()
)
pktcSigEndPntConfigStutterDialToneTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigStutterDialToneTO.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigStutterDialToneTO.setUnits("seconds")


class _PktcSigEndPntConfigTSMax_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigTSMax based on Unsigned32"""
    defaultValue = 20


_PktcSigEndPntConfigTSMax_Object = MibTableColumn
pktcSigEndPntConfigTSMax = _PktcSigEndPntConfigTSMax_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 13),
    _PktcSigEndPntConfigTSMax_Type()
)
pktcSigEndPntConfigTSMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigTSMax.setStatus("current")


class _PktcSigEndPntConfigMax1_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigMax1 based on Unsigned32"""
    defaultValue = 5


_PktcSigEndPntConfigMax1_Object = MibTableColumn
pktcSigEndPntConfigMax1 = _PktcSigEndPntConfigMax1_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 14),
    _PktcSigEndPntConfigMax1_Type()
)
pktcSigEndPntConfigMax1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigMax1.setStatus("current")


class _PktcSigEndPntConfigMax2_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigMax2 based on Unsigned32"""
    defaultValue = 7


_PktcSigEndPntConfigMax2_Object = MibTableColumn
pktcSigEndPntConfigMax2 = _PktcSigEndPntConfigMax2_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 15),
    _PktcSigEndPntConfigMax2_Type()
)
pktcSigEndPntConfigMax2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigMax2.setStatus("current")


class _PktcSigEndPntConfigMax1QEnable_Type(TruthValue):
    """Custom type pktcSigEndPntConfigMax1QEnable based on TruthValue"""


_PktcSigEndPntConfigMax1QEnable_Object = MibTableColumn
pktcSigEndPntConfigMax1QEnable = _PktcSigEndPntConfigMax1QEnable_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 16),
    _PktcSigEndPntConfigMax1QEnable_Type()
)
pktcSigEndPntConfigMax1QEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigMax1QEnable.setStatus("current")


class _PktcSigEndPntConfigMax2QEnable_Type(TruthValue):
    """Custom type pktcSigEndPntConfigMax2QEnable based on TruthValue"""


_PktcSigEndPntConfigMax2QEnable_Object = MibTableColumn
pktcSigEndPntConfigMax2QEnable = _PktcSigEndPntConfigMax2QEnable_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 17),
    _PktcSigEndPntConfigMax2QEnable_Type()
)
pktcSigEndPntConfigMax2QEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigMax2QEnable.setStatus("current")


class _PktcSigEndPntConfigMWD_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigMWD based on Unsigned32"""
    defaultValue = 600


_PktcSigEndPntConfigMWD_Object = MibTableColumn
pktcSigEndPntConfigMWD = _PktcSigEndPntConfigMWD_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 18),
    _PktcSigEndPntConfigMWD_Type()
)
pktcSigEndPntConfigMWD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigMWD.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigMWD.setUnits("seconds")


class _PktcSigEndPntConfigTdinit_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigTdinit based on Unsigned32"""
    defaultValue = 15


_PktcSigEndPntConfigTdinit_Object = MibTableColumn
pktcSigEndPntConfigTdinit = _PktcSigEndPntConfigTdinit_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 19),
    _PktcSigEndPntConfigTdinit_Type()
)
pktcSigEndPntConfigTdinit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigTdinit.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigTdinit.setUnits("seconds")


class _PktcSigEndPntConfigTdmin_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigTdmin based on Unsigned32"""
    defaultValue = 15


_PktcSigEndPntConfigTdmin_Object = MibTableColumn
pktcSigEndPntConfigTdmin = _PktcSigEndPntConfigTdmin_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 20),
    _PktcSigEndPntConfigTdmin_Type()
)
pktcSigEndPntConfigTdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigTdmin.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigTdmin.setUnits("seconds")


class _PktcSigEndPntConfigTdmax_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigTdmax based on Unsigned32"""
    defaultValue = 600


_PktcSigEndPntConfigTdmax_Object = MibTableColumn
pktcSigEndPntConfigTdmax = _PktcSigEndPntConfigTdmax_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 21),
    _PktcSigEndPntConfigTdmax_Type()
)
pktcSigEndPntConfigTdmax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigTdmax.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigTdmax.setUnits("seconds")


class _PktcSigEndPntConfigRtoMax_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigRtoMax based on Unsigned32"""
    defaultValue = 4


_PktcSigEndPntConfigRtoMax_Object = MibTableColumn
pktcSigEndPntConfigRtoMax = _PktcSigEndPntConfigRtoMax_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 22),
    _PktcSigEndPntConfigRtoMax_Type()
)
pktcSigEndPntConfigRtoMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigRtoMax.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigRtoMax.setUnits("seconds")


class _PktcSigEndPntConfigRtoInit_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigRtoInit based on Unsigned32"""
    defaultValue = 200


_PktcSigEndPntConfigRtoInit_Object = MibTableColumn
pktcSigEndPntConfigRtoInit = _PktcSigEndPntConfigRtoInit_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 23),
    _PktcSigEndPntConfigRtoInit_Type()
)
pktcSigEndPntConfigRtoInit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigRtoInit.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigRtoInit.setUnits("milliseconds")


class _PktcSigEndPntConfigLongDurationKeepAlive_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigLongDurationKeepAlive based on Unsigned32"""
    defaultValue = 60


_PktcSigEndPntConfigLongDurationKeepAlive_Object = MibTableColumn
pktcSigEndPntConfigLongDurationKeepAlive = _PktcSigEndPntConfigLongDurationKeepAlive_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 24),
    _PktcSigEndPntConfigLongDurationKeepAlive_Type()
)
pktcSigEndPntConfigLongDurationKeepAlive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigLongDurationKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigLongDurationKeepAlive.setUnits("minutes")


class _PktcSigEndPntConfigThist_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigThist based on Unsigned32"""
    defaultValue = 30


_PktcSigEndPntConfigThist_Object = MibTableColumn
pktcSigEndPntConfigThist = _PktcSigEndPntConfigThist_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 25),
    _PktcSigEndPntConfigThist_Type()
)
pktcSigEndPntConfigThist.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigThist.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigThist.setUnits("seconds")
_PktcSigEndPntConfigStatus_Type = RowStatus
_PktcSigEndPntConfigStatus_Object = MibTableColumn
pktcSigEndPntConfigStatus = _PktcSigEndPntConfigStatus_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 26),
    _PktcSigEndPntConfigStatus_Type()
)
pktcSigEndPntConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigStatus.setStatus("current")


class _PktcSigEndPntConfigCallWaitingMaxRep_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigCallWaitingMaxRep based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_PktcSigEndPntConfigCallWaitingMaxRep_Type.__name__ = "Unsigned32"
_PktcSigEndPntConfigCallWaitingMaxRep_Object = MibTableColumn
pktcSigEndPntConfigCallWaitingMaxRep = _PktcSigEndPntConfigCallWaitingMaxRep_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 27),
    _PktcSigEndPntConfigCallWaitingMaxRep_Type()
)
pktcSigEndPntConfigCallWaitingMaxRep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigCallWaitingMaxRep.setStatus("current")


class _PktcSigEndPntConfigCallWaitingDelay_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigCallWaitingDelay based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PktcSigEndPntConfigCallWaitingDelay_Type.__name__ = "Unsigned32"
_PktcSigEndPntConfigCallWaitingDelay_Object = MibTableColumn
pktcSigEndPntConfigCallWaitingDelay = _PktcSigEndPntConfigCallWaitingDelay_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 28),
    _PktcSigEndPntConfigCallWaitingDelay_Type()
)
pktcSigEndPntConfigCallWaitingDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigCallWaitingDelay.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigCallWaitingDelay.setUnits("seconds")
_PktcSigEndPntStatusCallIpAddressType_Type = InetAddressType
_PktcSigEndPntStatusCallIpAddressType_Object = MibTableColumn
pktcSigEndPntStatusCallIpAddressType = _PktcSigEndPntStatusCallIpAddressType_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 29),
    _PktcSigEndPntStatusCallIpAddressType_Type()
)
pktcSigEndPntStatusCallIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigEndPntStatusCallIpAddressType.setStatus("current")
_PktcSigEndPntStatusCallIpAddress_Type = InetAddress
_PktcSigEndPntStatusCallIpAddress_Object = MibTableColumn
pktcSigEndPntStatusCallIpAddress = _PktcSigEndPntStatusCallIpAddress_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 30),
    _PktcSigEndPntStatusCallIpAddress_Type()
)
pktcSigEndPntStatusCallIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigEndPntStatusCallIpAddress.setStatus("current")


class _PktcSigEndPntStatusError_Type(Integer32):
    """Custom type pktcSigEndPntStatusError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 3),
          ("noSecurityAssociation", 2),
          ("operational", 1))
    )


_PktcSigEndPntStatusError_Type.__name__ = "Integer32"
_PktcSigEndPntStatusError_Object = MibTableColumn
pktcSigEndPntStatusError = _PktcSigEndPntStatusError_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 31),
    _PktcSigEndPntStatusError_Type()
)
pktcSigEndPntStatusError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigEndPntStatusError.setStatus("current")


class _PktcSigEndPntConfigMinHookFlash_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigMinHookFlash based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 1550),
    )


_PktcSigEndPntConfigMinHookFlash_Type.__name__ = "Unsigned32"
_PktcSigEndPntConfigMinHookFlash_Object = MibTableColumn
pktcSigEndPntConfigMinHookFlash = _PktcSigEndPntConfigMinHookFlash_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 32),
    _PktcSigEndPntConfigMinHookFlash_Type()
)
pktcSigEndPntConfigMinHookFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigMinHookFlash.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigMinHookFlash.setUnits("Milliseconds")


class _PktcSigEndPntConfigMaxHookFlash_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigMaxHookFlash based on Unsigned32"""
    defaultValue = 800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 1550),
    )


_PktcSigEndPntConfigMaxHookFlash_Type.__name__ = "Unsigned32"
_PktcSigEndPntConfigMaxHookFlash_Object = MibTableColumn
pktcSigEndPntConfigMaxHookFlash = _PktcSigEndPntConfigMaxHookFlash_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 33),
    _PktcSigEndPntConfigMaxHookFlash_Type()
)
pktcSigEndPntConfigMaxHookFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigMaxHookFlash.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigMaxHookFlash.setUnits("Milliseconds")


class _PktcSigEndPntConfigPulseDialInterdigitTime_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigPulseDialInterdigitTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1500),
    )


_PktcSigEndPntConfigPulseDialInterdigitTime_Type.__name__ = "Unsigned32"
_PktcSigEndPntConfigPulseDialInterdigitTime_Object = MibTableColumn
pktcSigEndPntConfigPulseDialInterdigitTime = _PktcSigEndPntConfigPulseDialInterdigitTime_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 34),
    _PktcSigEndPntConfigPulseDialInterdigitTime_Type()
)
pktcSigEndPntConfigPulseDialInterdigitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigPulseDialInterdigitTime.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigPulseDialInterdigitTime.setUnits("Milliseconds")


class _PktcSigEndPntConfigPulseDialMinMakeTime_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigPulseDialMinMakeTime based on Unsigned32"""
    defaultValue = 25

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 200),
    )


_PktcSigEndPntConfigPulseDialMinMakeTime_Type.__name__ = "Unsigned32"
_PktcSigEndPntConfigPulseDialMinMakeTime_Object = MibTableColumn
pktcSigEndPntConfigPulseDialMinMakeTime = _PktcSigEndPntConfigPulseDialMinMakeTime_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 35),
    _PktcSigEndPntConfigPulseDialMinMakeTime_Type()
)
pktcSigEndPntConfigPulseDialMinMakeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigPulseDialMinMakeTime.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigPulseDialMinMakeTime.setUnits("Milliseconds")


class _PktcSigEndPntConfigPulseDialMaxMakeTime_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigPulseDialMaxMakeTime based on Unsigned32"""
    defaultValue = 55

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 200),
    )


_PktcSigEndPntConfigPulseDialMaxMakeTime_Type.__name__ = "Unsigned32"
_PktcSigEndPntConfigPulseDialMaxMakeTime_Object = MibTableColumn
pktcSigEndPntConfigPulseDialMaxMakeTime = _PktcSigEndPntConfigPulseDialMaxMakeTime_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 36),
    _PktcSigEndPntConfigPulseDialMaxMakeTime_Type()
)
pktcSigEndPntConfigPulseDialMaxMakeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigPulseDialMaxMakeTime.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigPulseDialMaxMakeTime.setUnits("Milliseconds")


class _PktcSigEndPntConfigPulseDialMinBreakTime_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigPulseDialMinBreakTime based on Unsigned32"""
    defaultValue = 45

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 200),
    )


_PktcSigEndPntConfigPulseDialMinBreakTime_Type.__name__ = "Unsigned32"
_PktcSigEndPntConfigPulseDialMinBreakTime_Object = MibTableColumn
pktcSigEndPntConfigPulseDialMinBreakTime = _PktcSigEndPntConfigPulseDialMinBreakTime_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 37),
    _PktcSigEndPntConfigPulseDialMinBreakTime_Type()
)
pktcSigEndPntConfigPulseDialMinBreakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigPulseDialMinBreakTime.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigPulseDialMinBreakTime.setUnits("Milliseconds")


class _PktcSigEndPntConfigPulseDialMaxBreakTime_Type(Unsigned32):
    """Custom type pktcSigEndPntConfigPulseDialMaxBreakTime based on Unsigned32"""
    defaultValue = 75

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 200),
    )


_PktcSigEndPntConfigPulseDialMaxBreakTime_Type.__name__ = "Unsigned32"
_PktcSigEndPntConfigPulseDialMaxBreakTime_Object = MibTableColumn
pktcSigEndPntConfigPulseDialMaxBreakTime = _PktcSigEndPntConfigPulseDialMaxBreakTime_Object(
    (1, 3, 6, 1, 2, 1, 169, 1, 2, 1, 1, 38),
    _PktcSigEndPntConfigPulseDialMaxBreakTime_Type()
)
pktcSigEndPntConfigPulseDialMaxBreakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigPulseDialMaxBreakTime.setStatus("current")
if mibBuilder.loadTexts:
    pktcSigEndPntConfigPulseDialMaxBreakTime.setUnits("Milliseconds")
_PktcSigConformance_ObjectIdentity = ObjectIdentity
pktcSigConformance = _PktcSigConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 169, 2)
)
_PktcSigCompliances_ObjectIdentity = ObjectIdentity
pktcSigCompliances = _PktcSigCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 169, 2, 1)
)
_PktcSigGroups_ObjectIdentity = ObjectIdentity
pktcSigGroups = _PktcSigGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 169, 2, 2)
)

# Managed Objects groups

pktcSigDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 169, 2, 2, 1)
)
pktcSigDeviceGroup.setObjects(
      *(("PKTC-IETF-SIG-MIB", "pktcSigDevCodecMax"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevEchoCancellation"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevSilenceSuppression"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevR0Cadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevR1Cadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevR2Cadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevR3Cadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevR4Cadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevR5Cadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevR6Cadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevR7Cadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevRgCadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevRsCadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDefCallSigDscp"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDefMediaStreamDscp"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevVmwiMode"),
        ("PKTC-IETF-SIG-MIB", "pktcSigCapabilityType"),
        ("PKTC-IETF-SIG-MIB", "pktcSigCapabilityVersion"),
        ("PKTC-IETF-SIG-MIB", "pktcSigCapabilityVendorExt"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDefNcsReceiveUdpPort"))
)
if mibBuilder.loadTexts:
    pktcSigDeviceGroup.setStatus("current")

pktcSigEndpointGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 169, 2, 2, 2)
)
pktcSigEndpointGroup.setObjects(
      *(("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigCallAgentId"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigCallAgentUdpPort"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigPartialDialTO"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigCriticalDialTO"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigBusyToneTO"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigDialToneTO"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigMessageWaitingTO"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigOffHookWarnToneTO"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigRingingTO"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigRingBackTO"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigReorderToneTO"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigStutterDialToneTO"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigTSMax"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigMax1"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigMax2"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigMax1QEnable"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigMax2QEnable"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigMWD"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigTdinit"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigTdmin"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigTdmax"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigRtoMax"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigRtoInit"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigLongDurationKeepAlive"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigThist"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigStatus"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigCallWaitingMaxRep"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigCallWaitingDelay"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntStatusCallIpAddressType"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntStatusCallIpAddress"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntStatusError"))
)
if mibBuilder.loadTexts:
    pktcSigEndpointGroup.setStatus("current")

pktcInternationalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 169, 2, 2, 3)
)
pktcInternationalGroup.setObjects(
      *(("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigMinHookFlash"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigMaxHookFlash"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigPulseDialInterdigitTime"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigPulseDialMinMakeTime"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigPulseDialMaxMakeTime"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigPulseDialMinBreakTime"),
        ("PKTC-IETF-SIG-MIB", "pktcSigEndPntConfigPulseDialMaxBreakTime"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevRingCadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevCidSigProtocol"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevCidDelayAfterLR"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevCidDtmfStartCode"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevCidDtmfEndCode"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevVmwiSigProtocol"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevVmwiDelayAfterLR"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevVmwiDtmfStartCode"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevVmwiDtmfEndCode"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevrpAsDtsDuration"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevCidMode"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevCidAfterRing"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevCidAfterDTAS"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevCidAfterRPAS"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevRingAfterCID"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevCidDTASAfterLR"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevVmwiMode"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevVmwiAfterDTAS"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevVmwiAfterRPAS"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevVmwiDTASAfterLR"),
        ("PKTC-IETF-SIG-MIB", "pktcSigPowerRingFrequency"),
        ("PKTC-IETF-SIG-MIB", "pktcSigPulseSignalFrequency"),
        ("PKTC-IETF-SIG-MIB", "pktcSigPulseSignalDbLevel"),
        ("PKTC-IETF-SIG-MIB", "pktcSigPulseSignalDuration"),
        ("PKTC-IETF-SIG-MIB", "pktcSigPulseSignalPulseInterval"),
        ("PKTC-IETF-SIG-MIB", "pktcSigPulseSignalRepeatCount"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevToneDbLevel"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevToneFreqCounter"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevToneWholeToneRepeatCount"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevToneSteady"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevToneFirstFreqValue"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevToneSecondFreqValue"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevToneThirdFreqValue"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevToneFourthFreqValue"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevToneFreqMode"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevToneFreqAmpModePrtg"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevToneFreqOnDuration"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevToneFreqOffDuration"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevToneFreqRepeatCount"))
)
if mibBuilder.loadTexts:
    pktcInternationalGroup.setStatus("current")

pktcLLinePackageGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 169, 2, 2, 4)
)
pktcLLinePackageGroup.setObjects(
      *(("PKTC-IETF-SIG-MIB", "pktcSigDevR0Cadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevR1Cadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevR2Cadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevR3Cadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevR4Cadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevR5Cadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevR6Cadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevR7Cadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevRgCadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevRsCadence"))
)
if mibBuilder.loadTexts:
    pktcLLinePackageGroup.setStatus("current")

pktcELinePackageGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 169, 2, 2, 5)
)
pktcELinePackageGroup.setObjects(
      *(("PKTC-IETF-SIG-MIB", "pktcSigDevR0Cadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevR1Cadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevR2Cadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevR3Cadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevR4Cadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevR5Cadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevR6Cadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevR7Cadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevRgCadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevRsCadence"),
        ("PKTC-IETF-SIG-MIB", "pktcSigPulseSignalFrequency"),
        ("PKTC-IETF-SIG-MIB", "pktcSigPulseSignalDbLevel"),
        ("PKTC-IETF-SIG-MIB", "pktcSigPulseSignalDuration"),
        ("PKTC-IETF-SIG-MIB", "pktcSigPulseSignalPulseInterval"),
        ("PKTC-IETF-SIG-MIB", "pktcSigPulseSignalRepeatCount"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDevRingCadence"))
)
if mibBuilder.loadTexts:
    pktcELinePackageGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pktcSigBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 169, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pktcSigBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PKTC-IETF-SIG-MIB",
    **{"TenthdBm": TenthdBm,
       "PktcCodecType": PktcCodecType,
       "PktcRingCadence": PktcRingCadence,
       "PktcSigType": PktcSigType,
       "DtmfCode": DtmfCode,
       "PktcSubscriberSideSigProtocol": PktcSubscriberSideSigProtocol,
       "pktcIetfSigMib": pktcIetfSigMib,
       "pktcSigNotification": pktcSigNotification,
       "pktcSigMibObjects": pktcSigMibObjects,
       "pktcSigDevObjects": pktcSigDevObjects,
       "pktcSigDevCodecTable": pktcSigDevCodecTable,
       "pktcSigDevCodecEntry": pktcSigDevCodecEntry,
       "pktcSigDevCodecComboIndex": pktcSigDevCodecComboIndex,
       "pktcSigDevCodecType": pktcSigDevCodecType,
       "pktcSigDevCodecMax": pktcSigDevCodecMax,
       "pktcSigDevEchoCancellation": pktcSigDevEchoCancellation,
       "pktcSigDevSilenceSuppression": pktcSigDevSilenceSuppression,
       "pktcSigDevCidSigProtocol": pktcSigDevCidSigProtocol,
       "pktcSigDevR0Cadence": pktcSigDevR0Cadence,
       "pktcSigDevR1Cadence": pktcSigDevR1Cadence,
       "pktcSigDevR2Cadence": pktcSigDevR2Cadence,
       "pktcSigDevR3Cadence": pktcSigDevR3Cadence,
       "pktcSigDevR4Cadence": pktcSigDevR4Cadence,
       "pktcSigDevR5Cadence": pktcSigDevR5Cadence,
       "pktcSigDevR6Cadence": pktcSigDevR6Cadence,
       "pktcSigDevR7Cadence": pktcSigDevR7Cadence,
       "pktcSigDevRgCadence": pktcSigDevRgCadence,
       "pktcSigDevRsCadence": pktcSigDevRsCadence,
       "pktcSigDefCallSigDscp": pktcSigDefCallSigDscp,
       "pktcSigDefMediaStreamDscp": pktcSigDefMediaStreamDscp,
       "pktcSigCapabilityTable": pktcSigCapabilityTable,
       "pktcSigCapabilityEntry": pktcSigCapabilityEntry,
       "pktcSigCapabilityIndex": pktcSigCapabilityIndex,
       "pktcSigCapabilityType": pktcSigCapabilityType,
       "pktcSigCapabilityVersion": pktcSigCapabilityVersion,
       "pktcSigCapabilityVendorExt": pktcSigCapabilityVendorExt,
       "pktcSigDefNcsReceiveUdpPort": pktcSigDefNcsReceiveUdpPort,
       "pktcSigPowerRingFrequency": pktcSigPowerRingFrequency,
       "pktcSigPulseSignalTable": pktcSigPulseSignalTable,
       "pktcSigPulseSignalEntry": pktcSigPulseSignalEntry,
       "pktcSigPulseSignalType": pktcSigPulseSignalType,
       "pktcSigPulseSignalFrequency": pktcSigPulseSignalFrequency,
       "pktcSigPulseSignalDbLevel": pktcSigPulseSignalDbLevel,
       "pktcSigPulseSignalDuration": pktcSigPulseSignalDuration,
       "pktcSigPulseSignalPulseInterval": pktcSigPulseSignalPulseInterval,
       "pktcSigPulseSignalRepeatCount": pktcSigPulseSignalRepeatCount,
       "pktcSigDevCidMode": pktcSigDevCidMode,
       "pktcSigDevCidAfterRing": pktcSigDevCidAfterRing,
       "pktcSigDevCidAfterDTAS": pktcSigDevCidAfterDTAS,
       "pktcSigDevCidAfterRPAS": pktcSigDevCidAfterRPAS,
       "pktcSigDevRingAfterCID": pktcSigDevRingAfterCID,
       "pktcSigDevCidDTASAfterLR": pktcSigDevCidDTASAfterLR,
       "pktcSigDevVmwiMode": pktcSigDevVmwiMode,
       "pktcSigDevVmwiAfterDTAS": pktcSigDevVmwiAfterDTAS,
       "pktcSigDevVmwiAfterRPAS": pktcSigDevVmwiAfterRPAS,
       "pktcSigDevVmwiDTASAfterLR": pktcSigDevVmwiDTASAfterLR,
       "pktcSigDevRingCadenceTable": pktcSigDevRingCadenceTable,
       "pktcSigDevRingCadenceEntry": pktcSigDevRingCadenceEntry,
       "pktcSigDevRingCadenceIndex": pktcSigDevRingCadenceIndex,
       "pktcSigDevRingCadence": pktcSigDevRingCadence,
       "pktcSigDevToneTable": pktcSigDevToneTable,
       "pktcSigDevToneEntry": pktcSigDevToneEntry,
       "pktcSigDevToneType": pktcSigDevToneType,
       "pktcSigDevToneFreqGroup": pktcSigDevToneFreqGroup,
       "pktcSigDevToneFreqCounter": pktcSigDevToneFreqCounter,
       "pktcSigDevToneWholeToneRepeatCount": pktcSigDevToneWholeToneRepeatCount,
       "pktcSigDevToneSteady": pktcSigDevToneSteady,
       "pktcSigDevMultiFreqToneTable": pktcSigDevMultiFreqToneTable,
       "pktcSigDevMultiFreqToneEntry": pktcSigDevMultiFreqToneEntry,
       "pktcSigDevToneNumber": pktcSigDevToneNumber,
       "pktcSigDevToneFirstFreqValue": pktcSigDevToneFirstFreqValue,
       "pktcSigDevToneSecondFreqValue": pktcSigDevToneSecondFreqValue,
       "pktcSigDevToneThirdFreqValue": pktcSigDevToneThirdFreqValue,
       "pktcSigDevToneFourthFreqValue": pktcSigDevToneFourthFreqValue,
       "pktcSigDevToneFreqMode": pktcSigDevToneFreqMode,
       "pktcSigDevToneFreqAmpModePrtg": pktcSigDevToneFreqAmpModePrtg,
       "pktcSigDevToneDbLevel": pktcSigDevToneDbLevel,
       "pktcSigDevToneFreqOnDuration": pktcSigDevToneFreqOnDuration,
       "pktcSigDevToneFreqOffDuration": pktcSigDevToneFreqOffDuration,
       "pktcSigDevToneFreqRepeatCount": pktcSigDevToneFreqRepeatCount,
       "pktcSigDevCidDelayAfterLR": pktcSigDevCidDelayAfterLR,
       "pktcSigDevCidDtmfStartCode": pktcSigDevCidDtmfStartCode,
       "pktcSigDevCidDtmfEndCode": pktcSigDevCidDtmfEndCode,
       "pktcSigDevVmwiSigProtocol": pktcSigDevVmwiSigProtocol,
       "pktcSigDevVmwiDelayAfterLR": pktcSigDevVmwiDelayAfterLR,
       "pktcSigDevVmwiDtmfStartCode": pktcSigDevVmwiDtmfStartCode,
       "pktcSigDevVmwiDtmfEndCode": pktcSigDevVmwiDtmfEndCode,
       "pktcSigDevrpAsDtsDuration": pktcSigDevrpAsDtsDuration,
       "pktcSigEndPntConfigObjects": pktcSigEndPntConfigObjects,
       "pktcSigEndPntConfigTable": pktcSigEndPntConfigTable,
       "pktcSigEndPntConfigEntry": pktcSigEndPntConfigEntry,
       "pktcSigEndPntConfigCallAgentId": pktcSigEndPntConfigCallAgentId,
       "pktcSigEndPntConfigCallAgentUdpPort": pktcSigEndPntConfigCallAgentUdpPort,
       "pktcSigEndPntConfigPartialDialTO": pktcSigEndPntConfigPartialDialTO,
       "pktcSigEndPntConfigCriticalDialTO": pktcSigEndPntConfigCriticalDialTO,
       "pktcSigEndPntConfigBusyToneTO": pktcSigEndPntConfigBusyToneTO,
       "pktcSigEndPntConfigDialToneTO": pktcSigEndPntConfigDialToneTO,
       "pktcSigEndPntConfigMessageWaitingTO": pktcSigEndPntConfigMessageWaitingTO,
       "pktcSigEndPntConfigOffHookWarnToneTO": pktcSigEndPntConfigOffHookWarnToneTO,
       "pktcSigEndPntConfigRingingTO": pktcSigEndPntConfigRingingTO,
       "pktcSigEndPntConfigRingBackTO": pktcSigEndPntConfigRingBackTO,
       "pktcSigEndPntConfigReorderToneTO": pktcSigEndPntConfigReorderToneTO,
       "pktcSigEndPntConfigStutterDialToneTO": pktcSigEndPntConfigStutterDialToneTO,
       "pktcSigEndPntConfigTSMax": pktcSigEndPntConfigTSMax,
       "pktcSigEndPntConfigMax1": pktcSigEndPntConfigMax1,
       "pktcSigEndPntConfigMax2": pktcSigEndPntConfigMax2,
       "pktcSigEndPntConfigMax1QEnable": pktcSigEndPntConfigMax1QEnable,
       "pktcSigEndPntConfigMax2QEnable": pktcSigEndPntConfigMax2QEnable,
       "pktcSigEndPntConfigMWD": pktcSigEndPntConfigMWD,
       "pktcSigEndPntConfigTdinit": pktcSigEndPntConfigTdinit,
       "pktcSigEndPntConfigTdmin": pktcSigEndPntConfigTdmin,
       "pktcSigEndPntConfigTdmax": pktcSigEndPntConfigTdmax,
       "pktcSigEndPntConfigRtoMax": pktcSigEndPntConfigRtoMax,
       "pktcSigEndPntConfigRtoInit": pktcSigEndPntConfigRtoInit,
       "pktcSigEndPntConfigLongDurationKeepAlive": pktcSigEndPntConfigLongDurationKeepAlive,
       "pktcSigEndPntConfigThist": pktcSigEndPntConfigThist,
       "pktcSigEndPntConfigStatus": pktcSigEndPntConfigStatus,
       "pktcSigEndPntConfigCallWaitingMaxRep": pktcSigEndPntConfigCallWaitingMaxRep,
       "pktcSigEndPntConfigCallWaitingDelay": pktcSigEndPntConfigCallWaitingDelay,
       "pktcSigEndPntStatusCallIpAddressType": pktcSigEndPntStatusCallIpAddressType,
       "pktcSigEndPntStatusCallIpAddress": pktcSigEndPntStatusCallIpAddress,
       "pktcSigEndPntStatusError": pktcSigEndPntStatusError,
       "pktcSigEndPntConfigMinHookFlash": pktcSigEndPntConfigMinHookFlash,
       "pktcSigEndPntConfigMaxHookFlash": pktcSigEndPntConfigMaxHookFlash,
       "pktcSigEndPntConfigPulseDialInterdigitTime": pktcSigEndPntConfigPulseDialInterdigitTime,
       "pktcSigEndPntConfigPulseDialMinMakeTime": pktcSigEndPntConfigPulseDialMinMakeTime,
       "pktcSigEndPntConfigPulseDialMaxMakeTime": pktcSigEndPntConfigPulseDialMaxMakeTime,
       "pktcSigEndPntConfigPulseDialMinBreakTime": pktcSigEndPntConfigPulseDialMinBreakTime,
       "pktcSigEndPntConfigPulseDialMaxBreakTime": pktcSigEndPntConfigPulseDialMaxBreakTime,
       "pktcSigConformance": pktcSigConformance,
       "pktcSigCompliances": pktcSigCompliances,
       "pktcSigBasicCompliance": pktcSigBasicCompliance,
       "pktcSigGroups": pktcSigGroups,
       "pktcSigDeviceGroup": pktcSigDeviceGroup,
       "pktcSigEndpointGroup": pktcSigEndpointGroup,
       "pktcInternationalGroup": pktcInternationalGroup,
       "pktcLLinePackageGroup": pktcLLinePackageGroup,
       "pktcELinePackageGroup": pktcELinePackageGroup}
)
