# SNMP MIB module (CISCO-PAGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PAGP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:41 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "InterfaceIndexOrZero")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

ciscoPagpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 98)
)
ciscoPagpMIB.setRevisions(
        ("2010-10-20 00:00",
         "2008-02-01 00:00",
         "2002-12-13 00:00",
         "2002-01-02 00:00",
         "1999-03-04 00:00",
         "1998-04-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PagpGroupCapability(Integer32, TextualConvention):
    status = "current"


class PagpEthcOperationMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manual", 2),
          ("off", 1),
          ("pagpOn", 3))
    )



class PagpPortPriority(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class PagpOperationMode(Integer32, TextualConvention):
    status = "current"
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
        *(("automatic", 3),
          ("automaticSilent", 4),
          ("desirable", 1),
          ("desirableSilent", 2))
    )



class PagpLearnMethod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("agPort", 2),
          ("physPort", 1),
          ("undefined", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoPagpMIBObjects_ObjectIdentity = ObjectIdentity
ciscoPagpMIBObjects = _CiscoPagpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1)
)
_PagpGroupCapabilityConfiguration_ObjectIdentity = ObjectIdentity
pagpGroupCapabilityConfiguration = _PagpGroupCapabilityConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1)
)
_PagpEtherChannelTable_Object = MibTable
pagpEtherChannelTable = _PagpEtherChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pagpEtherChannelTable.setStatus("current")
_PagpEtherChannelEntry_Object = MibTableRow
pagpEtherChannelEntry = _PagpEtherChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1, 1, 1)
)
pagpEtherChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pagpEtherChannelEntry.setStatus("current")
_PagpEthcOperationMode_Type = PagpEthcOperationMode
_PagpEthcOperationMode_Object = MibTableColumn
pagpEthcOperationMode = _PagpEthcOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1, 1, 1, 1),
    _PagpEthcOperationMode_Type()
)
pagpEthcOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pagpEthcOperationMode.setStatus("current")
_PagpDeviceId_Type = MacAddress
_PagpDeviceId_Object = MibTableColumn
pagpDeviceId = _PagpDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1, 1, 1, 2),
    _PagpDeviceId_Type()
)
pagpDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagpDeviceId.setStatus("current")
_PagpPhysGroupCapability_Type = PagpGroupCapability
_PagpPhysGroupCapability_Object = MibTableColumn
pagpPhysGroupCapability = _PagpPhysGroupCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1, 1, 1, 3),
    _PagpPhysGroupCapability_Type()
)
pagpPhysGroupCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagpPhysGroupCapability.setStatus("current")
_PagpOperGroupCapability_Type = PagpGroupCapability
_PagpOperGroupCapability_Object = MibTableColumn
pagpOperGroupCapability = _PagpOperGroupCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1, 1, 1, 4),
    _PagpOperGroupCapability_Type()
)
pagpOperGroupCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagpOperGroupCapability.setStatus("current")
_PagpAdminGroupCapability_Type = PagpGroupCapability
_PagpAdminGroupCapability_Object = MibTableColumn
pagpAdminGroupCapability = _PagpAdminGroupCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1, 1, 1, 5),
    _PagpAdminGroupCapability_Type()
)
pagpAdminGroupCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pagpAdminGroupCapability.setStatus("current")
_PagpPortPriority_Type = PagpPortPriority
_PagpPortPriority_Object = MibTableColumn
pagpPortPriority = _PagpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1, 1, 1, 6),
    _PagpPortPriority_Type()
)
pagpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pagpPortPriority.setStatus("current")
_PagpLearnMethod_Type = PagpLearnMethod
_PagpLearnMethod_Object = MibTableColumn
pagpLearnMethod = _PagpLearnMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1, 1, 1, 7),
    _PagpLearnMethod_Type()
)
pagpLearnMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pagpLearnMethod.setStatus("current")
_PagpGroupIfIndex_Type = InterfaceIndexOrZero
_PagpGroupIfIndex_Object = MibTableColumn
pagpGroupIfIndex = _PagpGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1, 1, 1, 8),
    _PagpGroupIfIndex_Type()
)
pagpGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagpGroupIfIndex.setStatus("current")


class _PagpDistributionProtocol_Type(Integer32):
    """Custom type pagpDistributionProtocol based on Integer32"""
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
        *(("ip", 1),
          ("ipPort", 6),
          ("mac", 2),
          ("port", 3),
          ("vlanIp", 5),
          ("vlanIpPort", 4))
    )


_PagpDistributionProtocol_Type.__name__ = "Integer32"
_PagpDistributionProtocol_Object = MibTableColumn
pagpDistributionProtocol = _PagpDistributionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1, 1, 1, 9),
    _PagpDistributionProtocol_Type()
)
pagpDistributionProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pagpDistributionProtocol.setStatus("current")


class _PagpDistributionAddress_Type(Integer32):
    """Custom type pagpDistributionAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("destination", 2),
          ("source", 1))
    )


_PagpDistributionAddress_Type.__name__ = "Integer32"
_PagpDistributionAddress_Object = MibTableColumn
pagpDistributionAddress = _PagpDistributionAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1, 1, 1, 10),
    _PagpDistributionAddress_Type()
)
pagpDistributionAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pagpDistributionAddress.setStatus("current")


class _PagpRate_Type(Integer32):
    """Custom type pagpRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fast", 1),
          ("normal", 2))
    )


_PagpRate_Type.__name__ = "Integer32"
_PagpRate_Object = MibTableColumn
pagpRate = _PagpRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1, 1, 1, 11),
    _PagpRate_Type()
)
pagpRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pagpRate.setStatus("current")


class _PagpInPacketTimeout_Type(Unsigned32):
    """Custom type pagpInPacketTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PagpInPacketTimeout_Type.__name__ = "Unsigned32"
_PagpInPacketTimeout_Object = MibTableColumn
pagpInPacketTimeout = _PagpInPacketTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1, 1, 1, 12),
    _PagpInPacketTimeout_Type()
)
pagpInPacketTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pagpInPacketTimeout.setStatus("current")
if mibBuilder.loadTexts:
    pagpInPacketTimeout.setUnits("Seconds")
_PagpProtocol_ObjectIdentity = ObjectIdentity
pagpProtocol = _PagpProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2)
)
_PagpProtocolConfigTable_Object = MibTable
pagpProtocolConfigTable = _PagpProtocolConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pagpProtocolConfigTable.setStatus("current")
_PagpProtocolConfigEntry_Object = MibTableRow
pagpProtocolConfigEntry = _PagpProtocolConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1)
)
pagpProtocolConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pagpProtocolConfigEntry.setStatus("current")
_PagpOperationMode_Type = PagpOperationMode
_PagpOperationMode_Object = MibTableColumn
pagpOperationMode = _PagpOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 1),
    _PagpOperationMode_Type()
)
pagpOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pagpOperationMode.setStatus("current")


class _PagpPortState_Type(Integer32):
    """Custom type pagpPortState based on Integer32"""
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
        *(("biDirectional", 6),
          ("dataReceived", 3),
          ("pagpReceived", 5),
          ("portDown", 1),
          ("portUp", 2),
          ("upData", 4),
          ("upMult", 8),
          ("upPagp", 7))
    )


_PagpPortState_Type.__name__ = "Integer32"
_PagpPortState_Object = MibTableColumn
pagpPortState = _PagpPortState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 2),
    _PagpPortState_Type()
)
pagpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagpPortState.setStatus("current")
_PagpLastStateChange_Type = TimeStamp
_PagpLastStateChange_Object = MibTableColumn
pagpLastStateChange = _PagpLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 3),
    _PagpLastStateChange_Type()
)
pagpLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagpLastStateChange.setStatus("current")


class _PagpHelloFrequency_Type(Integer32):
    """Custom type pagpHelloFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fast", 1),
          ("slow", 2))
    )


_PagpHelloFrequency_Type.__name__ = "Integer32"
_PagpHelloFrequency_Object = MibTableColumn
pagpHelloFrequency = _PagpHelloFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 4),
    _PagpHelloFrequency_Type()
)
pagpHelloFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagpHelloFrequency.setStatus("current")
_PagpDistributionAlgorithm_Type = DisplayString
_PagpDistributionAlgorithm_Object = MibTableColumn
pagpDistributionAlgorithm = _PagpDistributionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 5),
    _PagpDistributionAlgorithm_Type()
)
pagpDistributionAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagpDistributionAlgorithm.setStatus("current")


class _PagpPartnerCount_Type(Integer32):
    """Custom type pagpPartnerCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("many", 3),
          ("none", 1),
          ("one", 2))
    )


_PagpPartnerCount_Type.__name__ = "Integer32"
_PagpPartnerCount_Object = MibTableColumn
pagpPartnerCount = _PagpPartnerCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 6),
    _PagpPartnerCount_Type()
)
pagpPartnerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagpPartnerCount.setStatus("current")
_PagpPartnerDeviceId_Type = MacAddress
_PagpPartnerDeviceId_Object = MibTableColumn
pagpPartnerDeviceId = _PagpPartnerDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 7),
    _PagpPartnerDeviceId_Type()
)
pagpPartnerDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagpPartnerDeviceId.setStatus("current")
_PagpPartnerLearnMethod_Type = PagpLearnMethod
_PagpPartnerLearnMethod_Object = MibTableColumn
pagpPartnerLearnMethod = _PagpPartnerLearnMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 8),
    _PagpPartnerLearnMethod_Type()
)
pagpPartnerLearnMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagpPartnerLearnMethod.setStatus("current")
_PagpPartnerPortPriority_Type = PagpPortPriority
_PagpPartnerPortPriority_Object = MibTableColumn
pagpPartnerPortPriority = _PagpPartnerPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 9),
    _PagpPartnerPortPriority_Type()
)
pagpPartnerPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagpPartnerPortPriority.setStatus("current")
_PagpPartnerIfIndex_Type = InterfaceIndexOrZero
_PagpPartnerIfIndex_Object = MibTableColumn
pagpPartnerIfIndex = _PagpPartnerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 10),
    _PagpPartnerIfIndex_Type()
)
pagpPartnerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagpPartnerIfIndex.setStatus("current")
_PagpPartnerGroupCapability_Type = PagpGroupCapability
_PagpPartnerGroupCapability_Object = MibTableColumn
pagpPartnerGroupCapability = _PagpPartnerGroupCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 11),
    _PagpPartnerGroupCapability_Type()
)
pagpPartnerGroupCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagpPartnerGroupCapability.setStatus("current")
_PagpPartnerGroupIfIndex_Type = InterfaceIndexOrZero
_PagpPartnerGroupIfIndex_Object = MibTableColumn
pagpPartnerGroupIfIndex = _PagpPartnerGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 12),
    _PagpPartnerGroupIfIndex_Type()
)
pagpPartnerGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagpPartnerGroupIfIndex.setStatus("current")
_PagpPartnerDeviceName_Type = DisplayString
_PagpPartnerDeviceName_Object = MibTableColumn
pagpPartnerDeviceName = _PagpPartnerDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 13),
    _PagpPartnerDeviceName_Type()
)
pagpPartnerDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagpPartnerDeviceName.setStatus("current")
_PagpPartnerPortName_Type = DisplayString
_PagpPartnerPortName_Object = MibTableColumn
pagpPartnerPortName = _PagpPartnerPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 14),
    _PagpPartnerPortName_Type()
)
pagpPartnerPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagpPartnerPortName.setStatus("current")
_PagpPartnerAgportMACAddress_Type = MacAddress
_PagpPartnerAgportMACAddress_Object = MibTableColumn
pagpPartnerAgportMACAddress = _PagpPartnerAgportMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 15),
    _PagpPartnerAgportMACAddress_Type()
)
pagpPartnerAgportMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagpPartnerAgportMACAddress.setStatus("current")
_PagpProtocolStatsTable_Object = MibTable
pagpProtocolStatsTable = _PagpProtocolStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 2)
)
if mibBuilder.loadTexts:
    pagpProtocolStatsTable.setStatus("current")
_PagpProtocolStatsEntry_Object = MibTableRow
pagpProtocolStatsEntry = _PagpProtocolStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 2, 1)
)
pagpProtocolStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pagpProtocolStatsEntry.setStatus("current")
_PagpInPackets_Type = Counter32
_PagpInPackets_Object = MibTableColumn
pagpInPackets = _PagpInPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 2, 1, 3),
    _PagpInPackets_Type()
)
pagpInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagpInPackets.setStatus("current")
if mibBuilder.loadTexts:
    pagpInPackets.setUnits("packets")
_PagpOutPackets_Type = Counter32
_PagpOutPackets_Object = MibTableColumn
pagpOutPackets = _PagpOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 2, 1, 4),
    _PagpOutPackets_Type()
)
pagpOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagpOutPackets.setStatus("current")
if mibBuilder.loadTexts:
    pagpOutPackets.setUnits("packets")
_PagpInFlushes_Type = Counter32
_PagpInFlushes_Object = MibTableColumn
pagpInFlushes = _PagpInFlushes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 2, 1, 5),
    _PagpInFlushes_Type()
)
pagpInFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagpInFlushes.setStatus("current")
if mibBuilder.loadTexts:
    pagpInFlushes.setUnits("packets")
_PagpReturnedFlushes_Type = Counter32
_PagpReturnedFlushes_Object = MibTableColumn
pagpReturnedFlushes = _PagpReturnedFlushes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 2, 1, 6),
    _PagpReturnedFlushes_Type()
)
pagpReturnedFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagpReturnedFlushes.setStatus("current")
if mibBuilder.loadTexts:
    pagpReturnedFlushes.setUnits("packets")
_PagpOutFlushes_Type = Counter32
_PagpOutFlushes_Object = MibTableColumn
pagpOutFlushes = _PagpOutFlushes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 2, 1, 7),
    _PagpOutFlushes_Type()
)
pagpOutFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagpOutFlushes.setStatus("current")
if mibBuilder.loadTexts:
    pagpOutFlushes.setUnits("packets")
_PagpInErrors_Type = Counter32
_PagpInErrors_Object = MibTableColumn
pagpInErrors = _PagpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 2, 1, 8),
    _PagpInErrors_Type()
)
pagpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pagpInErrors.setStatus("current")
if mibBuilder.loadTexts:
    pagpInErrors.setUnits("packets")
_CiscoPagpMIBConformance_ObjectIdentity = ObjectIdentity
ciscoPagpMIBConformance = _CiscoPagpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 3)
)
_CiscoPagpMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoPagpMIBCompliances = _CiscoPagpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 3, 1)
)
_CiscoPagpMIBGroups_ObjectIdentity = ObjectIdentity
ciscoPagpMIBGroups = _CiscoPagpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 3, 2)
)

# Managed Objects groups

ciscoPagpEthcGroupV1R1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 3, 2, 1)
)
ciscoPagpEthcGroupV1R1.setObjects(
      *(("CISCO-PAGP-MIB", "pagpEthcOperationMode"),
        ("CISCO-PAGP-MIB", "pagpDeviceId"),
        ("CISCO-PAGP-MIB", "pagpPhysGroupCapability"),
        ("CISCO-PAGP-MIB", "pagpOperGroupCapability"),
        ("CISCO-PAGP-MIB", "pagpAdminGroupCapability"),
        ("CISCO-PAGP-MIB", "pagpPortPriority"),
        ("CISCO-PAGP-MIB", "pagpLearnMethod"),
        ("CISCO-PAGP-MIB", "pagpGroupIfIndex"))
)
if mibBuilder.loadTexts:
    ciscoPagpEthcGroupV1R1.setStatus("obsolete")

ciscoPagpPagpGroupV1R1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 3, 2, 2)
)
ciscoPagpPagpGroupV1R1.setObjects(
      *(("CISCO-PAGP-MIB", "pagpOperationMode"),
        ("CISCO-PAGP-MIB", "pagpPortState"),
        ("CISCO-PAGP-MIB", "pagpLastStateChange"),
        ("CISCO-PAGP-MIB", "pagpHelloFrequency"),
        ("CISCO-PAGP-MIB", "pagpDistributionAlgorithm"),
        ("CISCO-PAGP-MIB", "pagpPartnerCount"),
        ("CISCO-PAGP-MIB", "pagpPartnerDeviceId"),
        ("CISCO-PAGP-MIB", "pagpPartnerLearnMethod"),
        ("CISCO-PAGP-MIB", "pagpPartnerPortPriority"),
        ("CISCO-PAGP-MIB", "pagpPartnerIfIndex"),
        ("CISCO-PAGP-MIB", "pagpPartnerGroupCapability"),
        ("CISCO-PAGP-MIB", "pagpPartnerGroupIfIndex"),
        ("CISCO-PAGP-MIB", "pagpPartnerDeviceName"),
        ("CISCO-PAGP-MIB", "pagpPartnerPortName"),
        ("CISCO-PAGP-MIB", "pagpPartnerAgportMACAddress"),
        ("CISCO-PAGP-MIB", "pagpInPackets"),
        ("CISCO-PAGP-MIB", "pagpOutPackets"),
        ("CISCO-PAGP-MIB", "pagpInFlushes"),
        ("CISCO-PAGP-MIB", "pagpReturnedFlushes"),
        ("CISCO-PAGP-MIB", "pagpOutFlushes"),
        ("CISCO-PAGP-MIB", "pagpInErrors"))
)
if mibBuilder.loadTexts:
    ciscoPagpPagpGroupV1R1.setStatus("current")

ciscoPagpEthcGroupV2R2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 3, 2, 3)
)
ciscoPagpEthcGroupV2R2.setObjects(
      *(("CISCO-PAGP-MIB", "pagpEthcOperationMode"),
        ("CISCO-PAGP-MIB", "pagpDeviceId"),
        ("CISCO-PAGP-MIB", "pagpPhysGroupCapability"),
        ("CISCO-PAGP-MIB", "pagpOperGroupCapability"),
        ("CISCO-PAGP-MIB", "pagpAdminGroupCapability"),
        ("CISCO-PAGP-MIB", "pagpPortPriority"),
        ("CISCO-PAGP-MIB", "pagpLearnMethod"),
        ("CISCO-PAGP-MIB", "pagpGroupIfIndex"),
        ("CISCO-PAGP-MIB", "pagpDistributionProtocol"),
        ("CISCO-PAGP-MIB", "pagpDistributionAddress"))
)
if mibBuilder.loadTexts:
    ciscoPagpEthcGroupV2R2.setStatus("current")

ciscoPagpRateAndTimeOutGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 3, 2, 4)
)
ciscoPagpRateAndTimeOutGroup.setObjects(
      *(("CISCO-PAGP-MIB", "pagpRate"),
        ("CISCO-PAGP-MIB", "pagpInPacketTimeout"))
)
if mibBuilder.loadTexts:
    ciscoPagpRateAndTimeOutGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoPagpMIBComplianceV1R1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoPagpMIBComplianceV1R1.setStatus(
        "obsolete"
    )

ciscoPagpMIBComplianceV2R2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoPagpMIBComplianceV2R2.setStatus(
        "deprecated"
    )

ciscoPagpMIBComplianceV3R3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 98, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoPagpMIBComplianceV3R3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PAGP-MIB",
    **{"PagpGroupCapability": PagpGroupCapability,
       "PagpEthcOperationMode": PagpEthcOperationMode,
       "PagpPortPriority": PagpPortPriority,
       "PagpOperationMode": PagpOperationMode,
       "PagpLearnMethod": PagpLearnMethod,
       "ciscoPagpMIB": ciscoPagpMIB,
       "ciscoPagpMIBObjects": ciscoPagpMIBObjects,
       "pagpGroupCapabilityConfiguration": pagpGroupCapabilityConfiguration,
       "pagpEtherChannelTable": pagpEtherChannelTable,
       "pagpEtherChannelEntry": pagpEtherChannelEntry,
       "pagpEthcOperationMode": pagpEthcOperationMode,
       "pagpDeviceId": pagpDeviceId,
       "pagpPhysGroupCapability": pagpPhysGroupCapability,
       "pagpOperGroupCapability": pagpOperGroupCapability,
       "pagpAdminGroupCapability": pagpAdminGroupCapability,
       "pagpPortPriority": pagpPortPriority,
       "pagpLearnMethod": pagpLearnMethod,
       "pagpGroupIfIndex": pagpGroupIfIndex,
       "pagpDistributionProtocol": pagpDistributionProtocol,
       "pagpDistributionAddress": pagpDistributionAddress,
       "pagpRate": pagpRate,
       "pagpInPacketTimeout": pagpInPacketTimeout,
       "pagpProtocol": pagpProtocol,
       "pagpProtocolConfigTable": pagpProtocolConfigTable,
       "pagpProtocolConfigEntry": pagpProtocolConfigEntry,
       "pagpOperationMode": pagpOperationMode,
       "pagpPortState": pagpPortState,
       "pagpLastStateChange": pagpLastStateChange,
       "pagpHelloFrequency": pagpHelloFrequency,
       "pagpDistributionAlgorithm": pagpDistributionAlgorithm,
       "pagpPartnerCount": pagpPartnerCount,
       "pagpPartnerDeviceId": pagpPartnerDeviceId,
       "pagpPartnerLearnMethod": pagpPartnerLearnMethod,
       "pagpPartnerPortPriority": pagpPartnerPortPriority,
       "pagpPartnerIfIndex": pagpPartnerIfIndex,
       "pagpPartnerGroupCapability": pagpPartnerGroupCapability,
       "pagpPartnerGroupIfIndex": pagpPartnerGroupIfIndex,
       "pagpPartnerDeviceName": pagpPartnerDeviceName,
       "pagpPartnerPortName": pagpPartnerPortName,
       "pagpPartnerAgportMACAddress": pagpPartnerAgportMACAddress,
       "pagpProtocolStatsTable": pagpProtocolStatsTable,
       "pagpProtocolStatsEntry": pagpProtocolStatsEntry,
       "pagpInPackets": pagpInPackets,
       "pagpOutPackets": pagpOutPackets,
       "pagpInFlushes": pagpInFlushes,
       "pagpReturnedFlushes": pagpReturnedFlushes,
       "pagpOutFlushes": pagpOutFlushes,
       "pagpInErrors": pagpInErrors,
       "ciscoPagpMIBConformance": ciscoPagpMIBConformance,
       "ciscoPagpMIBCompliances": ciscoPagpMIBCompliances,
       "ciscoPagpMIBComplianceV1R1": ciscoPagpMIBComplianceV1R1,
       "ciscoPagpMIBComplianceV2R2": ciscoPagpMIBComplianceV2R2,
       "ciscoPagpMIBComplianceV3R3": ciscoPagpMIBComplianceV3R3,
       "ciscoPagpMIBGroups": ciscoPagpMIBGroups,
       "ciscoPagpEthcGroupV1R1": ciscoPagpEthcGroupV1R1,
       "ciscoPagpPagpGroupV1R1": ciscoPagpPagpGroupV1R1,
       "ciscoPagpEthcGroupV2R2": ciscoPagpEthcGroupV2R2,
       "ciscoPagpRateAndTimeOutGroup": ciscoPagpRateAndTimeOutGroup}
)
