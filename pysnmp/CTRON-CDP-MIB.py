# SNMP MIB module (CTRON-CDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-CDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:37 2024
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

(ctCDP,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctCDP")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(TimeFilter,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "TimeFilter")

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
 MacAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ctronCdpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CTCDPCapability(Integer32, TextualConvention):
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("activeDirectory", 12),
          ("bgp", 3),
          ("dhcpServer", 10),
          ("dnsServer", 11),
          ("dvmrp", 5),
          ("gmrp", 8),
          ("gvrp", 7),
          ("ieee8021q", 6),
          ("igmp", 1),
          ("igmpSnoop", 9),
          ("ospf", 4),
          ("rip", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CtCDPNeighbor_ObjectIdentity = ObjectIdentity
ctCDPNeighbor = _CtCDPNeighbor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1)
)
_CtCDPNeighborLastChange_Type = TimeStamp
_CtCDPNeighborLastChange_Object = MibScalar
ctCDPNeighborLastChange = _CtCDPNeighborLastChange_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 1),
    _CtCDPNeighborLastChange_Type()
)
ctCDPNeighborLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCDPNeighborLastChange.setStatus("current")
_CtCDPNeighborLastDelete_Type = TimeStamp
_CtCDPNeighborLastDelete_Object = MibScalar
ctCDPNeighborLastDelete = _CtCDPNeighborLastDelete_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 2),
    _CtCDPNeighborLastDelete_Type()
)
ctCDPNeighborLastDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCDPNeighborLastDelete.setStatus("current")
_CtCDPNeighborTable_Object = MibTable
ctCDPNeighborTable = _CtCDPNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3)
)
if mibBuilder.loadTexts:
    ctCDPNeighborTable.setStatus("current")
_CtCDPNeighborEntry_Object = MibTableRow
ctCDPNeighborEntry = _CtCDPNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1)
)
ctCDPNeighborEntry.setIndexNames(
    (0, "CTRON-CDP-MIB", "ctCDPNeighborTimeMark"),
    (0, "IF-MIB", "ifIndex"),
    (0, "CTRON-CDP-MIB", "ctCDPNeighborMAC"),
)
if mibBuilder.loadTexts:
    ctCDPNeighborEntry.setStatus("current")
_CtCDPNeighborTimeMark_Type = TimeFilter
_CtCDPNeighborTimeMark_Object = MibTableColumn
ctCDPNeighborTimeMark = _CtCDPNeighborTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 1),
    _CtCDPNeighborTimeMark_Type()
)
ctCDPNeighborTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCDPNeighborTimeMark.setStatus("current")
_CtCDPNeighborMAC_Type = MacAddress
_CtCDPNeighborMAC_Object = MibTableColumn
ctCDPNeighborMAC = _CtCDPNeighborMAC_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 2),
    _CtCDPNeighborMAC_Type()
)
ctCDPNeighborMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCDPNeighborMAC.setStatus("current")
_CtCDPNeighborIP_Type = IpAddress
_CtCDPNeighborIP_Object = MibTableColumn
ctCDPNeighborIP = _CtCDPNeighborIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 3),
    _CtCDPNeighborIP_Type()
)
ctCDPNeighborIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCDPNeighborIP.setStatus("current")
_CtCDPNeighborPort_Type = InterfaceIndex
_CtCDPNeighborPort_Object = MibTableColumn
ctCDPNeighborPort = _CtCDPNeighborPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 4),
    _CtCDPNeighborPort_Type()
)
ctCDPNeighborPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCDPNeighborPort.setStatus("current")


class _CtCDPNeighborType_Type(Integer32):
    """Custom type ctCDPNeighborType based on Integer32"""
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
        *(("dhcpServer", 7),
          ("dnsDhcpServer", 8),
          ("dnsServer", 6),
          ("dot1dBridge", 4),
          ("dot1qSwitch", 2),
          ("router", 3),
          ("secureFastSwitch", 1),
          ("vlanManager", 5))
    )


_CtCDPNeighborType_Type.__name__ = "Integer32"
_CtCDPNeighborType_Object = MibTableColumn
ctCDPNeighborType = _CtCDPNeighborType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 5),
    _CtCDPNeighborType_Type()
)
ctCDPNeighborType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCDPNeighborType.setStatus("current")
_CtCDPNeighborChassisMAC_Type = MacAddress
_CtCDPNeighborChassisMAC_Object = MibTableColumn
ctCDPNeighborChassisMAC = _CtCDPNeighborChassisMAC_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 6),
    _CtCDPNeighborChassisMAC_Type()
)
ctCDPNeighborChassisMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCDPNeighborChassisMAC.setStatus("current")
_CtCDPNeighborChassisIP_Type = IpAddress
_CtCDPNeighborChassisIP_Object = MibTableColumn
ctCDPNeighborChassisIP = _CtCDPNeighborChassisIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 7),
    _CtCDPNeighborChassisIP_Type()
)
ctCDPNeighborChassisIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCDPNeighborChassisIP.setStatus("current")
_CtCDPNeighborDescription_Type = DisplayString
_CtCDPNeighborDescription_Object = MibTableColumn
ctCDPNeighborDescription = _CtCDPNeighborDescription_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 8),
    _CtCDPNeighborDescription_Type()
)
ctCDPNeighborDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCDPNeighborDescription.setStatus("current")
_CtCDPNeighborPortName_Type = DisplayString
_CtCDPNeighborPortName_Object = MibTableColumn
ctCDPNeighborPortName = _CtCDPNeighborPortName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 9),
    _CtCDPNeighborPortName_Type()
)
ctCDPNeighborPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCDPNeighborPortName.setStatus("current")
_CtCDPNeighborCapability_Type = CTCDPCapability
_CtCDPNeighborCapability_Object = MibTableColumn
ctCDPNeighborCapability = _CtCDPNeighborCapability_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 1, 3, 1, 10),
    _CtCDPNeighborCapability_Type()
)
ctCDPNeighborCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCDPNeighborCapability.setStatus("current")
_CtCDPStatus_ObjectIdentity = ObjectIdentity
ctCDPStatus = _CtCDPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2)
)


class _CtCDPGlobalStatus_Type(Integer32):
    """Custom type ctCDPGlobalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoEnable", 3),
          ("disable", 2),
          ("enable", 1))
    )


_CtCDPGlobalStatus_Type.__name__ = "Integer32"
_CtCDPGlobalStatus_Object = MibScalar
ctCDPGlobalStatus = _CtCDPGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2, 1),
    _CtCDPGlobalStatus_Type()
)
ctCDPGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctCDPGlobalStatus.setStatus("current")


class _CtCDPAuthenticationCode_Type(OctetString):
    """Custom type ctCDPAuthenticationCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CtCDPAuthenticationCode_Type.__name__ = "OctetString"
_CtCDPAuthenticationCode_Object = MibScalar
ctCDPAuthenticationCode = _CtCDPAuthenticationCode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2, 2),
    _CtCDPAuthenticationCode_Type()
)
ctCDPAuthenticationCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctCDPAuthenticationCode.setStatus("current")
_CtCDPPortTable_Object = MibTable
ctCDPPortTable = _CtCDPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2, 3)
)
if mibBuilder.loadTexts:
    ctCDPPortTable.setStatus("current")
_CtCDPPortTableEntry_Object = MibTableRow
ctCDPPortTableEntry = _CtCDPPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2, 3, 1)
)
ctCDPPortTableEntry.setIndexNames(
    (0, "CTRON-CDP-MIB", "ctCDPPort"),
)
if mibBuilder.loadTexts:
    ctCDPPortTableEntry.setStatus("current")
_CtCDPPort_Type = InterfaceIndex
_CtCDPPort_Object = MibTableColumn
ctCDPPort = _CtCDPPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2, 3, 1, 1),
    _CtCDPPort_Type()
)
ctCDPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCDPPort.setStatus("current")


class _CtCDPPortStatus_Type(Integer32):
    """Custom type ctCDPPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoEnable", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_CtCDPPortStatus_Type.__name__ = "Integer32"
_CtCDPPortStatus_Object = MibTableColumn
ctCDPPortStatus = _CtCDPPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2, 3, 1, 2),
    _CtCDPPortStatus_Type()
)
ctCDPPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctCDPPortStatus.setStatus("current")


class _CtCDPTransmitFrequency_Type(Integer32):
    """Custom type ctCDPTransmitFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 900),
    )


_CtCDPTransmitFrequency_Type.__name__ = "Integer32"
_CtCDPTransmitFrequency_Object = MibScalar
ctCDPTransmitFrequency = _CtCDPTransmitFrequency_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2, 4),
    _CtCDPTransmitFrequency_Type()
)
ctCDPTransmitFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctCDPTransmitFrequency.setStatus("current")


class _CtCDPHoldTime_Type(Integer32):
    """Custom type ctCDPHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 600),
    )


_CtCDPHoldTime_Type.__name__ = "Integer32"
_CtCDPHoldTime_Object = MibScalar
ctCDPHoldTime = _CtCDPHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2, 5),
    _CtCDPHoldTime_Type()
)
ctCDPHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctCDPHoldTime.setStatus("current")


class _CtCDPVersion_Type(OctetString):
    """Custom type ctCDPVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CtCDPVersion_Type.__name__ = "OctetString"
_CtCDPVersion_Object = MibScalar
ctCDPVersion = _CtCDPVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 2, 6),
    _CtCDPVersion_Type()
)
ctCDPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCDPVersion.setStatus("current")
_CtCDPConformance_ObjectIdentity = ObjectIdentity
ctCDPConformance = _CtCDPConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 3, 11)
)
_CtCDPCompliances_ObjectIdentity = ObjectIdentity
ctCDPCompliances = _CtCDPCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 3, 11, 1)
)
_CtCDPGroups_ObjectIdentity = ObjectIdentity
ctCDPGroups = _CtCDPGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 3, 11, 2)
)
_CtCDPStats_ObjectIdentity = ObjectIdentity
ctCDPStats = _CtCDPStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 4)
)
_CtCDPInPackets_Type = Counter32
_CtCDPInPackets_Object = MibScalar
ctCDPInPackets = _CtCDPInPackets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 4, 1),
    _CtCDPInPackets_Type()
)
ctCDPInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCDPInPackets.setStatus("current")
_CtCDPOutPackets_Type = Counter32
_CtCDPOutPackets_Object = MibScalar
ctCDPOutPackets = _CtCDPOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 4, 2),
    _CtCDPOutPackets_Type()
)
ctCDPOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCDPOutPackets.setStatus("current")
_CtCDPInvalidVersionPackets_Type = Counter32
_CtCDPInvalidVersionPackets_Object = MibScalar
ctCDPInvalidVersionPackets = _CtCDPInvalidVersionPackets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 4, 3),
    _CtCDPInvalidVersionPackets_Type()
)
ctCDPInvalidVersionPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCDPInvalidVersionPackets.setStatus("current")
_CtCDPParseErrorPackets_Type = Counter32
_CtCDPParseErrorPackets_Object = MibScalar
ctCDPParseErrorPackets = _CtCDPParseErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 4, 4),
    _CtCDPParseErrorPackets_Type()
)
ctCDPParseErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCDPParseErrorPackets.setStatus("current")
_CtCDPTransmitErrors_Type = Counter32
_CtCDPTransmitErrors_Object = MibScalar
ctCDPTransmitErrors = _CtCDPTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 4, 5),
    _CtCDPTransmitErrors_Type()
)
ctCDPTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCDPTransmitErrors.setStatus("current")
_CtCDPMemoryErrors_Type = Counter32
_CtCDPMemoryErrors_Object = MibScalar
ctCDPMemoryErrors = _CtCDPMemoryErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 4, 6),
    _CtCDPMemoryErrors_Type()
)
ctCDPMemoryErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctCDPMemoryErrors.setStatus("current")

# Managed Objects groups

ctCdpGroupV10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 3, 11, 2, 1)
)
ctCdpGroupV10.setObjects(
      *(("CTRON-CDP-MIB", "ctCDPNeighborLastChange"),
        ("CTRON-CDP-MIB", "ctCDPNeighborLastDelete"),
        ("CTRON-CDP-MIB", "ctCDPNeighborTimeMark"),
        ("CTRON-CDP-MIB", "ctCDPNeighborMAC"),
        ("CTRON-CDP-MIB", "ctCDPNeighborIP"),
        ("CTRON-CDP-MIB", "ctCDPNeighborPort"),
        ("CTRON-CDP-MIB", "ctCDPNeighborType"),
        ("CTRON-CDP-MIB", "ctCDPNeighborChassisMAC"),
        ("CTRON-CDP-MIB", "ctCDPNeighborChassisIP"),
        ("CTRON-CDP-MIB", "ctCDPGlobalStatus"),
        ("CTRON-CDP-MIB", "ctCDPAuthenticationCode"),
        ("CTRON-CDP-MIB", "ctCDPPort"),
        ("CTRON-CDP-MIB", "ctCDPPortStatus"),
        ("CTRON-CDP-MIB", "ctCDPNeighborDescription"),
        ("CTRON-CDP-MIB", "ctCDPNeighborPortName"),
        ("CTRON-CDP-MIB", "ctCDPNeighborCapability"),
        ("CTRON-CDP-MIB", "ctCDPTransmitFrequency"),
        ("CTRON-CDP-MIB", "ctCDPHoldTime"),
        ("CTRON-CDP-MIB", "ctCDPVersion"),
        ("CTRON-CDP-MIB", "ctCDPInPackets"),
        ("CTRON-CDP-MIB", "ctCDPOutPackets"),
        ("CTRON-CDP-MIB", "ctCDPInvalidVersionPackets"),
        ("CTRON-CDP-MIB", "ctCDPParseErrorPackets"),
        ("CTRON-CDP-MIB", "ctCDPTransmitErrors"),
        ("CTRON-CDP-MIB", "ctCDPMemoryErrors"))
)
if mibBuilder.loadTexts:
    ctCdpGroupV10.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ctCDPComplianceV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19, 3, 11, 1, 1)
)
if mibBuilder.loadTexts:
    ctCDPComplianceV10.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-CDP-MIB",
    **{"CTCDPCapability": CTCDPCapability,
       "ctCDPNeighbor": ctCDPNeighbor,
       "ctCDPNeighborLastChange": ctCDPNeighborLastChange,
       "ctCDPNeighborLastDelete": ctCDPNeighborLastDelete,
       "ctCDPNeighborTable": ctCDPNeighborTable,
       "ctCDPNeighborEntry": ctCDPNeighborEntry,
       "ctCDPNeighborTimeMark": ctCDPNeighborTimeMark,
       "ctCDPNeighborMAC": ctCDPNeighborMAC,
       "ctCDPNeighborIP": ctCDPNeighborIP,
       "ctCDPNeighborPort": ctCDPNeighborPort,
       "ctCDPNeighborType": ctCDPNeighborType,
       "ctCDPNeighborChassisMAC": ctCDPNeighborChassisMAC,
       "ctCDPNeighborChassisIP": ctCDPNeighborChassisIP,
       "ctCDPNeighborDescription": ctCDPNeighborDescription,
       "ctCDPNeighborPortName": ctCDPNeighborPortName,
       "ctCDPNeighborCapability": ctCDPNeighborCapability,
       "ctCDPStatus": ctCDPStatus,
       "ctCDPGlobalStatus": ctCDPGlobalStatus,
       "ctCDPAuthenticationCode": ctCDPAuthenticationCode,
       "ctCDPPortTable": ctCDPPortTable,
       "ctCDPPortTableEntry": ctCDPPortTableEntry,
       "ctCDPPort": ctCDPPort,
       "ctCDPPortStatus": ctCDPPortStatus,
       "ctCDPTransmitFrequency": ctCDPTransmitFrequency,
       "ctCDPHoldTime": ctCDPHoldTime,
       "ctCDPVersion": ctCDPVersion,
       "ctronCdpMIB": ctronCdpMIB,
       "ctCDPConformance": ctCDPConformance,
       "ctCDPCompliances": ctCDPCompliances,
       "ctCDPComplianceV10": ctCDPComplianceV10,
       "ctCDPGroups": ctCDPGroups,
       "ctCdpGroupV10": ctCdpGroupV10,
       "ctCDPStats": ctCDPStats,
       "ctCDPInPackets": ctCDPInPackets,
       "ctCDPOutPackets": ctCDPOutPackets,
       "ctCDPInvalidVersionPackets": ctCDPInvalidVersionPackets,
       "ctCDPParseErrorPackets": ctCDPParseErrorPackets,
       "ctCDPTransmitErrors": ctCDPTransmitErrors,
       "ctCDPMemoryErrors": ctCDPMemoryErrors}
)
