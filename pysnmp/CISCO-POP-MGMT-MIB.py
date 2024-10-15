# SNMP MIB module (CISCO-POP-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-POP-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:53 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(dsx1LineIndex,
 dsx1LineStatus) = mibBuilder.importSymbols(
    "DS1-MIB",
    "dsx1LineIndex",
    "dsx1LineStatus")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoPopMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 19)
)
ciscoPopMgmtMIB.setRevisions(
        ("2005-12-21 00:00",
         "2002-12-26 00:00",
         "2000-11-29 00:00",
         "2000-03-03 00:00",
         "1998-02-02 00:00",
         "1997-10-21 00:00",
         "1997-05-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoPopMgmtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoPopMgmtMIBObjects = _CiscoPopMgmtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1)
)
_CpmDS0Usage_ObjectIdentity = ObjectIdentity
cpmDS0Usage = _CpmDS0Usage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1)
)
_CpmDS0UsageTable_Object = MibTable
cpmDS0UsageTable = _CpmDS0UsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cpmDS0UsageTable.setStatus("current")
_CpmDS0UsageEntry_Object = MibTableRow
cpmDS0UsageEntry = _CpmDS0UsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1, 1)
)
cpmDS0UsageEntry.setIndexNames(
    (0, "CISCO-POP-MGMT-MIB", "cpmDS1SlotIndex"),
    (0, "CISCO-POP-MGMT-MIB", "cpmDS1PortIndex"),
    (0, "CISCO-POP-MGMT-MIB", "cpmChannelIndex"),
)
if mibBuilder.loadTexts:
    cpmDS0UsageEntry.setStatus("current")


class _CpmDS1SlotIndex_Type(Integer32):
    """Custom type cpmDS1SlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpmDS1SlotIndex_Type.__name__ = "Integer32"
_CpmDS1SlotIndex_Object = MibTableColumn
cpmDS1SlotIndex = _CpmDS1SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1, 1, 1),
    _CpmDS1SlotIndex_Type()
)
cpmDS1SlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpmDS1SlotIndex.setStatus("current")


class _CpmDS1PortIndex_Type(Integer32):
    """Custom type cpmDS1PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpmDS1PortIndex_Type.__name__ = "Integer32"
_CpmDS1PortIndex_Object = MibTableColumn
cpmDS1PortIndex = _CpmDS1PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1, 1, 2),
    _CpmDS1PortIndex_Type()
)
cpmDS1PortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpmDS1PortIndex.setStatus("current")


class _CpmChannelIndex_Type(Integer32):
    """Custom type cpmChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpmChannelIndex_Type.__name__ = "Integer32"
_CpmChannelIndex_Object = MibTableColumn
cpmChannelIndex = _CpmChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1, 1, 3),
    _CpmChannelIndex_Type()
)
cpmChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpmChannelIndex.setStatus("current")


class _CpmConfiguredType_Type(Integer32):
    """Custom type cpmConfiguredType based on Integer32"""
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
        *(("ce1", 4),
          ("ct1", 3),
          ("isdn", 2),
          ("unknown", 1))
    )


_CpmConfiguredType_Type.__name__ = "Integer32"
_CpmConfiguredType_Object = MibTableColumn
cpmConfiguredType = _CpmConfiguredType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1, 1, 4),
    _CpmConfiguredType_Type()
)
cpmConfiguredType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmConfiguredType.setStatus("current")


class _CpmDS0CallType_Type(Integer32):
    """Custom type cpmDS0CallType based on Integer32"""
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
        *(("analog", 3),
          ("digital", 4),
          ("idle", 1),
          ("unknown", 2),
          ("v110", 5),
          ("v120", 6),
          ("voice", 7))
    )


_CpmDS0CallType_Type.__name__ = "Integer32"
_CpmDS0CallType_Object = MibTableColumn
cpmDS0CallType = _CpmDS0CallType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1, 1, 5),
    _CpmDS0CallType_Type()
)
cpmDS0CallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDS0CallType.setStatus("current")


class _CpmL2Encapsulation_Type(Integer32):
    """Custom type cpmL2Encapsulation based on Integer32"""
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
        *(("arap", 5),
          ("exec", 7),
          ("hdlc", 6),
          ("idle", 1),
          ("ppp", 3),
          ("slip", 4),
          ("unknown", 2),
          ("voice", 8))
    )


_CpmL2Encapsulation_Type.__name__ = "Integer32"
_CpmL2Encapsulation_Object = MibTableColumn
cpmL2Encapsulation = _CpmL2Encapsulation_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1, 1, 6),
    _CpmL2Encapsulation_Type()
)
cpmL2Encapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmL2Encapsulation.setStatus("current")
_CpmCallCount_Type = Counter32
_CpmCallCount_Object = MibTableColumn
cpmCallCount = _CpmCallCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1, 1, 7),
    _CpmCallCount_Type()
)
cpmCallCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCallCount.setStatus("current")
_CpmTimeInUse_Type = TimeTicks
_CpmTimeInUse_Object = MibTableColumn
cpmTimeInUse = _CpmTimeInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1, 1, 8),
    _CpmTimeInUse_Type()
)
cpmTimeInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmTimeInUse.setStatus("current")
_CpmInOctets_Type = Counter32
_CpmInOctets_Object = MibTableColumn
cpmInOctets = _CpmInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1, 1, 9),
    _CpmInOctets_Type()
)
cpmInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmInOctets.setStatus("current")
_CpmOutOctets_Type = Counter32
_CpmOutOctets_Object = MibTableColumn
cpmOutOctets = _CpmOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1, 1, 10),
    _CpmOutOctets_Type()
)
cpmOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmOutOctets.setStatus("current")
_CpmInPackets_Type = Counter32
_CpmInPackets_Object = MibTableColumn
cpmInPackets = _CpmInPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1, 1, 11),
    _CpmInPackets_Type()
)
cpmInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmInPackets.setStatus("current")
_CpmOutPackets_Type = Counter32
_CpmOutPackets_Object = MibTableColumn
cpmOutPackets = _CpmOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1, 1, 12),
    _CpmOutPackets_Type()
)
cpmOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmOutPackets.setStatus("current")
_CpmAssociatedInterface_Type = InterfaceIndexOrZero
_CpmAssociatedInterface_Object = MibTableColumn
cpmAssociatedInterface = _CpmAssociatedInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 1, 1, 13),
    _CpmAssociatedInterface_Type()
)
cpmAssociatedInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAssociatedInterface.setStatus("current")
_CpmISDNCfgBChanInUseForAnalog_Type = Gauge32
_CpmISDNCfgBChanInUseForAnalog_Object = MibScalar
cpmISDNCfgBChanInUseForAnalog = _CpmISDNCfgBChanInUseForAnalog_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 2),
    _CpmISDNCfgBChanInUseForAnalog_Type()
)
cpmISDNCfgBChanInUseForAnalog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmISDNCfgBChanInUseForAnalog.setStatus("current")
_CpmISDNCfgBChannelsInUse_Type = Gauge32
_CpmISDNCfgBChannelsInUse_Object = MibScalar
cpmISDNCfgBChannelsInUse = _CpmISDNCfgBChannelsInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 3),
    _CpmISDNCfgBChannelsInUse_Type()
)
cpmISDNCfgBChannelsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmISDNCfgBChannelsInUse.setStatus("current")
_CpmActiveDS0s_Type = Gauge32
_CpmActiveDS0s_Object = MibScalar
cpmActiveDS0s = _CpmActiveDS0s_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 4),
    _CpmActiveDS0s_Type()
)
cpmActiveDS0s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmActiveDS0s.setStatus("current")
_CpmPPPCalls_Type = Gauge32
_CpmPPPCalls_Object = MibScalar
cpmPPPCalls = _CpmPPPCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 5),
    _CpmPPPCalls_Type()
)
cpmPPPCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmPPPCalls.setStatus("current")
_CpmV120Calls_Type = Gauge32
_CpmV120Calls_Object = MibScalar
cpmV120Calls = _CpmV120Calls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 6),
    _CpmV120Calls_Type()
)
cpmV120Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmV120Calls.setStatus("current")
_CpmV110Calls_Type = Gauge32
_CpmV110Calls_Object = MibScalar
cpmV110Calls = _CpmV110Calls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 7),
    _CpmV110Calls_Type()
)
cpmV110Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmV110Calls.setStatus("current")
_CpmActiveDS0sHighWaterMark_Type = Counter32
_CpmActiveDS0sHighWaterMark_Object = MibScalar
cpmActiveDS0sHighWaterMark = _CpmActiveDS0sHighWaterMark_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 8),
    _CpmActiveDS0sHighWaterMark_Type()
)
cpmActiveDS0sHighWaterMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmActiveDS0sHighWaterMark.setStatus("current")
_CpmDS1DS0UsageTable_Object = MibTable
cpmDS1DS0UsageTable = _CpmDS1DS0UsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 9)
)
if mibBuilder.loadTexts:
    cpmDS1DS0UsageTable.setStatus("current")
_CpmDS1DS0UsageEntry_Object = MibTableRow
cpmDS1DS0UsageEntry = _CpmDS1DS0UsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 9, 1)
)
cpmDS1DS0UsageEntry.setIndexNames(
    (0, "CISCO-POP-MGMT-MIB", "cpmDS1UsageSlotIndex"),
    (0, "CISCO-POP-MGMT-MIB", "cpmDS1UsagePortIndex"),
)
if mibBuilder.loadTexts:
    cpmDS1DS0UsageEntry.setStatus("current")


class _CpmDS1UsageSlotIndex_Type(Integer32):
    """Custom type cpmDS1UsageSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpmDS1UsageSlotIndex_Type.__name__ = "Integer32"
_CpmDS1UsageSlotIndex_Object = MibTableColumn
cpmDS1UsageSlotIndex = _CpmDS1UsageSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 9, 1, 1),
    _CpmDS1UsageSlotIndex_Type()
)
cpmDS1UsageSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpmDS1UsageSlotIndex.setStatus("current")


class _CpmDS1UsagePortIndex_Type(Integer32):
    """Custom type cpmDS1UsagePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpmDS1UsagePortIndex_Type.__name__ = "Integer32"
_CpmDS1UsagePortIndex_Object = MibTableColumn
cpmDS1UsagePortIndex = _CpmDS1UsagePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 9, 1, 2),
    _CpmDS1UsagePortIndex_Type()
)
cpmDS1UsagePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpmDS1UsagePortIndex.setStatus("current")
_CpmDS1ActiveDS0s_Type = Gauge32
_CpmDS1ActiveDS0s_Object = MibTableColumn
cpmDS1ActiveDS0s = _CpmDS1ActiveDS0s_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 9, 1, 3),
    _CpmDS1ActiveDS0s_Type()
)
cpmDS1ActiveDS0s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDS1ActiveDS0s.setStatus("current")
_CpmDS1ActiveDS0sHighWaterMark_Type = Counter32
_CpmDS1ActiveDS0sHighWaterMark_Object = MibTableColumn
cpmDS1ActiveDS0sHighWaterMark = _CpmDS1ActiveDS0sHighWaterMark_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 9, 1, 4),
    _CpmDS1ActiveDS0sHighWaterMark_Type()
)
cpmDS1ActiveDS0sHighWaterMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDS1ActiveDS0sHighWaterMark.setStatus("current")
_CpmDS1TotalAnalogCalls_Type = Counter32
_CpmDS1TotalAnalogCalls_Object = MibTableColumn
cpmDS1TotalAnalogCalls = _CpmDS1TotalAnalogCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 9, 1, 5),
    _CpmDS1TotalAnalogCalls_Type()
)
cpmDS1TotalAnalogCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDS1TotalAnalogCalls.setStatus("current")
if mibBuilder.loadTexts:
    cpmDS1TotalAnalogCalls.setUnits("calls")
_CpmDS1TotalDigitalCalls_Type = Counter32
_CpmDS1TotalDigitalCalls_Object = MibTableColumn
cpmDS1TotalDigitalCalls = _CpmDS1TotalDigitalCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 9, 1, 6),
    _CpmDS1TotalDigitalCalls_Type()
)
cpmDS1TotalDigitalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDS1TotalDigitalCalls.setStatus("current")
if mibBuilder.loadTexts:
    cpmDS1TotalDigitalCalls.setUnits("calls")
_CpmDS1TotalV110Calls_Type = Counter32
_CpmDS1TotalV110Calls_Object = MibTableColumn
cpmDS1TotalV110Calls = _CpmDS1TotalV110Calls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 9, 1, 7),
    _CpmDS1TotalV110Calls_Type()
)
cpmDS1TotalV110Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDS1TotalV110Calls.setStatus("current")
if mibBuilder.loadTexts:
    cpmDS1TotalV110Calls.setUnits("calls")
_CpmDS1TotalV120Calls_Type = Counter32
_CpmDS1TotalV120Calls_Object = MibTableColumn
cpmDS1TotalV120Calls = _CpmDS1TotalV120Calls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 9, 1, 8),
    _CpmDS1TotalV120Calls_Type()
)
cpmDS1TotalV120Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDS1TotalV120Calls.setStatus("current")
if mibBuilder.loadTexts:
    cpmDS1TotalV120Calls.setUnits("calls")
_CpmDS1TotalCalls_Type = Counter32
_CpmDS1TotalCalls_Object = MibTableColumn
cpmDS1TotalCalls = _CpmDS1TotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 9, 1, 9),
    _CpmDS1TotalCalls_Type()
)
cpmDS1TotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDS1TotalCalls.setStatus("current")
if mibBuilder.loadTexts:
    cpmDS1TotalCalls.setUnits("calls")
_CpmDS1TotalTimeInUse_Type = Unsigned32
_CpmDS1TotalTimeInUse_Object = MibTableColumn
cpmDS1TotalTimeInUse = _CpmDS1TotalTimeInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 9, 1, 10),
    _CpmDS1TotalTimeInUse_Type()
)
cpmDS1TotalTimeInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDS1TotalTimeInUse.setStatus("current")
if mibBuilder.loadTexts:
    cpmDS1TotalTimeInUse.setUnits("seconds")
_CpmDS1CurrentIdle_Type = Gauge32
_CpmDS1CurrentIdle_Object = MibTableColumn
cpmDS1CurrentIdle = _CpmDS1CurrentIdle_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 9, 1, 11),
    _CpmDS1CurrentIdle_Type()
)
cpmDS1CurrentIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDS1CurrentIdle.setStatus("current")
_CpmDS1CurrentOutOfService_Type = Gauge32
_CpmDS1CurrentOutOfService_Object = MibTableColumn
cpmDS1CurrentOutOfService = _CpmDS1CurrentOutOfService_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 9, 1, 12),
    _CpmDS1CurrentOutOfService_Type()
)
cpmDS1CurrentOutOfService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDS1CurrentOutOfService.setStatus("current")
_CpmDS1CurrentBusyout_Type = Gauge32
_CpmDS1CurrentBusyout_Object = MibTableColumn
cpmDS1CurrentBusyout = _CpmDS1CurrentBusyout_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 9, 1, 13),
    _CpmDS1CurrentBusyout_Type()
)
cpmDS1CurrentBusyout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDS1CurrentBusyout.setStatus("current")
_CpmDS1InOctets_Type = Counter32
_CpmDS1InOctets_Object = MibTableColumn
cpmDS1InOctets = _CpmDS1InOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 9, 1, 14),
    _CpmDS1InOctets_Type()
)
cpmDS1InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDS1InOctets.setStatus("current")
if mibBuilder.loadTexts:
    cpmDS1InOctets.setUnits("octets")
_CpmDS1OutOctets_Type = Counter32
_CpmDS1OutOctets_Object = MibTableColumn
cpmDS1OutOctets = _CpmDS1OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 9, 1, 15),
    _CpmDS1OutOctets_Type()
)
cpmDS1OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDS1OutOctets.setStatus("current")
if mibBuilder.loadTexts:
    cpmDS1OutOctets.setUnits("octets")
_CpmDS1InPackets_Type = Counter32
_CpmDS1InPackets_Object = MibTableColumn
cpmDS1InPackets = _CpmDS1InPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 9, 1, 16),
    _CpmDS1InPackets_Type()
)
cpmDS1InPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDS1InPackets.setStatus("current")
if mibBuilder.loadTexts:
    cpmDS1InPackets.setUnits("packets")
_CpmDS1OutPackets_Type = Counter32
_CpmDS1OutPackets_Object = MibTableColumn
cpmDS1OutPackets = _CpmDS1OutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 9, 1, 17),
    _CpmDS1OutPackets_Type()
)
cpmDS1OutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDS1OutPackets.setStatus("current")
if mibBuilder.loadTexts:
    cpmDS1OutPackets.setUnits("packets")
_CpmSW56CfgBChannelsInUse_Type = Gauge32
_CpmSW56CfgBChannelsInUse_Object = MibScalar
cpmSW56CfgBChannelsInUse = _CpmSW56CfgBChannelsInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 10),
    _CpmSW56CfgBChannelsInUse_Type()
)
cpmSW56CfgBChannelsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmSW56CfgBChannelsInUse.setStatus("current")
_CpmISDNCfgBChanInUseForVoice_Type = Gauge32
_CpmISDNCfgBChanInUseForVoice_Object = MibScalar
cpmISDNCfgBChanInUseForVoice = _CpmISDNCfgBChanInUseForVoice_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 11),
    _CpmISDNCfgBChanInUseForVoice_Type()
)
cpmISDNCfgBChanInUseForVoice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmISDNCfgBChanInUseForVoice.setStatus("current")
_CpmCASCfgBChanInUseForVoice_Type = Gauge32
_CpmCASCfgBChanInUseForVoice_Object = MibScalar
cpmCASCfgBChanInUseForVoice = _CpmCASCfgBChanInUseForVoice_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 12),
    _CpmCASCfgBChanInUseForVoice_Type()
)
cpmCASCfgBChanInUseForVoice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCASCfgBChanInUseForVoice.setStatus("current")
_CpmISDNCfgActiveDChannels_Type = Gauge32
_CpmISDNCfgActiveDChannels_Object = MibScalar
cpmISDNCfgActiveDChannels = _CpmISDNCfgActiveDChannels_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 13),
    _CpmISDNCfgActiveDChannels_Type()
)
cpmISDNCfgActiveDChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmISDNCfgActiveDChannels.setStatus("current")
_CpmISDNCfgBChannelsTimeInUse_Type = Counter32
_CpmISDNCfgBChannelsTimeInUse_Object = MibScalar
cpmISDNCfgBChannelsTimeInUse = _CpmISDNCfgBChannelsTimeInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 14),
    _CpmISDNCfgBChannelsTimeInUse_Type()
)
cpmISDNCfgBChannelsTimeInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmISDNCfgBChannelsTimeInUse.setStatus("current")
if mibBuilder.loadTexts:
    cpmISDNCfgBChannelsTimeInUse.setUnits("seconds")
_CpmISDNCfgBChannelsTimeInUseAnlg_Type = Counter32
_CpmISDNCfgBChannelsTimeInUseAnlg_Object = MibScalar
cpmISDNCfgBChannelsTimeInUseAnlg = _CpmISDNCfgBChannelsTimeInUseAnlg_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 15),
    _CpmISDNCfgBChannelsTimeInUseAnlg_Type()
)
cpmISDNCfgBChannelsTimeInUseAnlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmISDNCfgBChannelsTimeInUseAnlg.setStatus("current")
if mibBuilder.loadTexts:
    cpmISDNCfgBChannelsTimeInUseAnlg.setUnits("seconds")
_CpmISDNCfgBChannelCalls_Type = Counter32
_CpmISDNCfgBChannelCalls_Object = MibScalar
cpmISDNCfgBChannelCalls = _CpmISDNCfgBChannelCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 16),
    _CpmISDNCfgBChannelCalls_Type()
)
cpmISDNCfgBChannelCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmISDNCfgBChannelCalls.setStatus("current")
if mibBuilder.loadTexts:
    cpmISDNCfgBChannelCalls.setUnits("calls")
_CpmISDNCfgBChannelAnalogCalls_Type = Counter32
_CpmISDNCfgBChannelAnalogCalls_Object = MibScalar
cpmISDNCfgBChannelAnalogCalls = _CpmISDNCfgBChannelAnalogCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 17),
    _CpmISDNCfgBChannelAnalogCalls_Type()
)
cpmISDNCfgBChannelAnalogCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmISDNCfgBChannelAnalogCalls.setStatus("current")
if mibBuilder.loadTexts:
    cpmISDNCfgBChannelAnalogCalls.setUnits("calls")
_CpmTotalISDNSyncPPPCalls_Type = Counter32
_CpmTotalISDNSyncPPPCalls_Object = MibScalar
cpmTotalISDNSyncPPPCalls = _CpmTotalISDNSyncPPPCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 1, 18),
    _CpmTotalISDNSyncPPPCalls_Type()
)
cpmTotalISDNSyncPPPCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmTotalISDNSyncPPPCalls.setStatus("current")
_CpmCallFailure_ObjectIdentity = ObjectIdentity
cpmCallFailure = _CpmCallFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 2)
)
_CpmISDNCallsRejected_Type = Counter32
_CpmISDNCallsRejected_Object = MibScalar
cpmISDNCallsRejected = _CpmISDNCallsRejected_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 2, 1),
    _CpmISDNCallsRejected_Type()
)
cpmISDNCallsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmISDNCallsRejected.setStatus("current")
_CpmModemCallsRejected_Type = Counter32
_CpmModemCallsRejected_Object = MibScalar
cpmModemCallsRejected = _CpmModemCallsRejected_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 2, 2),
    _CpmModemCallsRejected_Type()
)
cpmModemCallsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmModemCallsRejected.setStatus("current")
_CpmISDNCallsClearedAbnormally_Type = Counter32
_CpmISDNCallsClearedAbnormally_Object = MibScalar
cpmISDNCallsClearedAbnormally = _CpmISDNCallsClearedAbnormally_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 2, 3),
    _CpmISDNCallsClearedAbnormally_Type()
)
cpmISDNCallsClearedAbnormally.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmISDNCallsClearedAbnormally.setStatus("current")
_CpmModemCallsClearedAbnormally_Type = Counter32
_CpmModemCallsClearedAbnormally_Object = MibScalar
cpmModemCallsClearedAbnormally = _CpmModemCallsClearedAbnormally_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 2, 4),
    _CpmModemCallsClearedAbnormally_Type()
)
cpmModemCallsClearedAbnormally.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmModemCallsClearedAbnormally.setStatus("current")
_CpmISDNNoResource_Type = Counter32
_CpmISDNNoResource_Object = MibScalar
cpmISDNNoResource = _CpmISDNNoResource_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 2, 5),
    _CpmISDNNoResource_Type()
)
cpmISDNNoResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmISDNNoResource.setStatus("current")
_CpmModemNoResource_Type = Counter32
_CpmModemNoResource_Object = MibScalar
cpmModemNoResource = _CpmModemNoResource_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 2, 6),
    _CpmModemNoResource_Type()
)
cpmModemNoResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmModemNoResource.setStatus("current")
_CpmActiveCallSummary_ObjectIdentity = ObjectIdentity
cpmActiveCallSummary = _CpmActiveCallSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3)
)
_CpmActiveCallSummaryTable_Object = MibTable
cpmActiveCallSummaryTable = _CpmActiveCallSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cpmActiveCallSummaryTable.setStatus("current")
_CpmActiveCallSummaryEntry_Object = MibTableRow
cpmActiveCallSummaryEntry = _CpmActiveCallSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1)
)
cpmActiveCallSummaryEntry.setIndexNames(
    (0, "CISCO-POP-MGMT-MIB", "cpmActiveCallStartTimeIndex"),
    (0, "CISCO-POP-MGMT-MIB", "cpmActiveCallSummaryIndex"),
)
if mibBuilder.loadTexts:
    cpmActiveCallSummaryEntry.setStatus("current")
_CpmActiveCallStartTimeIndex_Type = TimeStamp
_CpmActiveCallStartTimeIndex_Object = MibTableColumn
cpmActiveCallStartTimeIndex = _CpmActiveCallStartTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1, 1),
    _CpmActiveCallStartTimeIndex_Type()
)
cpmActiveCallStartTimeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpmActiveCallStartTimeIndex.setStatus("current")


class _CpmActiveCallSummaryIndex_Type(Integer32):
    """Custom type cpmActiveCallSummaryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpmActiveCallSummaryIndex_Type.__name__ = "Integer32"
_CpmActiveCallSummaryIndex_Object = MibTableColumn
cpmActiveCallSummaryIndex = _CpmActiveCallSummaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1, 2),
    _CpmActiveCallSummaryIndex_Type()
)
cpmActiveCallSummaryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpmActiveCallSummaryIndex.setStatus("current")


class _CpmActiveUserID_Type(DisplayString):
    """Custom type cpmActiveUserID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpmActiveUserID_Type.__name__ = "DisplayString"
_CpmActiveUserID_Object = MibTableColumn
cpmActiveUserID = _CpmActiveUserID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1, 3),
    _CpmActiveUserID_Type()
)
cpmActiveUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmActiveUserID.setStatus("current")
_CpmActiveUserIpAddr_Type = IpAddress
_CpmActiveUserIpAddr_Object = MibTableColumn
cpmActiveUserIpAddr = _CpmActiveUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1, 4),
    _CpmActiveUserIpAddr_Type()
)
cpmActiveUserIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmActiveUserIpAddr.setStatus("current")


class _CpmActiveCallType_Type(Integer32):
    """Custom type cpmActiveCallType based on Integer32"""
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
        *(("analog", 2),
          ("digital", 3),
          ("unknown", 1),
          ("v110", 4),
          ("v120", 5),
          ("voice", 6))
    )


_CpmActiveCallType_Type.__name__ = "Integer32"
_CpmActiveCallType_Object = MibTableColumn
cpmActiveCallType = _CpmActiveCallType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1, 5),
    _CpmActiveCallType_Type()
)
cpmActiveCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmActiveCallType.setStatus("current")


class _CpmActiveModemSlot_Type(Integer32):
    """Custom type cpmActiveModemSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpmActiveModemSlot_Type.__name__ = "Integer32"
_CpmActiveModemSlot_Object = MibTableColumn
cpmActiveModemSlot = _CpmActiveModemSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1, 6),
    _CpmActiveModemSlot_Type()
)
cpmActiveModemSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmActiveModemSlot.setStatus("current")


class _CpmActiveModemPort_Type(Integer32):
    """Custom type cpmActiveModemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpmActiveModemPort_Type.__name__ = "Integer32"
_CpmActiveModemPort_Object = MibTableColumn
cpmActiveModemPort = _CpmActiveModemPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1, 7),
    _CpmActiveModemPort_Type()
)
cpmActiveModemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmActiveModemPort.setStatus("current")
_CpmActiveCallDuration_Type = TimeTicks
_CpmActiveCallDuration_Object = MibTableColumn
cpmActiveCallDuration = _CpmActiveCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1, 8),
    _CpmActiveCallDuration_Type()
)
cpmActiveCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmActiveCallDuration.setStatus("current")


class _CpmActiveEntrySlot_Type(Integer32):
    """Custom type cpmActiveEntrySlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpmActiveEntrySlot_Type.__name__ = "Integer32"
_CpmActiveEntrySlot_Object = MibTableColumn
cpmActiveEntrySlot = _CpmActiveEntrySlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1, 9),
    _CpmActiveEntrySlot_Type()
)
cpmActiveEntrySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmActiveEntrySlot.setStatus("current")


class _CpmActiveEntryPort_Type(Integer32):
    """Custom type cpmActiveEntryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpmActiveEntryPort_Type.__name__ = "Integer32"
_CpmActiveEntryPort_Object = MibTableColumn
cpmActiveEntryPort = _CpmActiveEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1, 10),
    _CpmActiveEntryPort_Type()
)
cpmActiveEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmActiveEntryPort.setStatus("current")


class _CpmActiveEntryChannel_Type(Integer32):
    """Custom type cpmActiveEntryChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpmActiveEntryChannel_Type.__name__ = "Integer32"
_CpmActiveEntryChannel_Object = MibTableColumn
cpmActiveEntryChannel = _CpmActiveEntryChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1, 11),
    _CpmActiveEntryChannel_Type()
)
cpmActiveEntryChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmActiveEntryChannel.setStatus("current")


class _CpmActiveRemotePhoneNumber_Type(DisplayString):
    """Custom type cpmActiveRemotePhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpmActiveRemotePhoneNumber_Type.__name__ = "DisplayString"
_CpmActiveRemotePhoneNumber_Object = MibTableColumn
cpmActiveRemotePhoneNumber = _CpmActiveRemotePhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1, 12),
    _CpmActiveRemotePhoneNumber_Type()
)
cpmActiveRemotePhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmActiveRemotePhoneNumber.setStatus("current")


class _CpmActiveLocalPhoneNumber_Type(DisplayString):
    """Custom type cpmActiveLocalPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpmActiveLocalPhoneNumber_Type.__name__ = "DisplayString"
_CpmActiveLocalPhoneNumber_Object = MibTableColumn
cpmActiveLocalPhoneNumber = _CpmActiveLocalPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1, 13),
    _CpmActiveLocalPhoneNumber_Type()
)
cpmActiveLocalPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmActiveLocalPhoneNumber.setStatus("current")
_CpmActiveTTYNumber_Type = Integer32
_CpmActiveTTYNumber_Object = MibTableColumn
cpmActiveTTYNumber = _CpmActiveTTYNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 3, 1, 1, 14),
    _CpmActiveTTYNumber_Type()
)
cpmActiveTTYNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmActiveTTYNumber.setStatus("current")
_CpmCallHistorySummary_ObjectIdentity = ObjectIdentity
cpmCallHistorySummary = _CpmCallHistorySummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4)
)


class _CpmCallHistorySummaryTableMaxLength_Type(Integer32):
    """Custom type cpmCallHistorySummaryTableMaxLength based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_CpmCallHistorySummaryTableMaxLength_Type.__name__ = "Integer32"
_CpmCallHistorySummaryTableMaxLength_Object = MibScalar
cpmCallHistorySummaryTableMaxLength = _CpmCallHistorySummaryTableMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 1),
    _CpmCallHistorySummaryTableMaxLength_Type()
)
cpmCallHistorySummaryTableMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmCallHistorySummaryTableMaxLength.setStatus("current")


class _CpmCallHistorySummaryRetainTimer_Type(Integer32):
    """Custom type cpmCallHistorySummaryRetainTimer based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_CpmCallHistorySummaryRetainTimer_Type.__name__ = "Integer32"
_CpmCallHistorySummaryRetainTimer_Object = MibScalar
cpmCallHistorySummaryRetainTimer = _CpmCallHistorySummaryRetainTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 2),
    _CpmCallHistorySummaryRetainTimer_Type()
)
cpmCallHistorySummaryRetainTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmCallHistorySummaryRetainTimer.setStatus("current")
if mibBuilder.loadTexts:
    cpmCallHistorySummaryRetainTimer.setUnits("minutes")
_CpmCallHistorySummaryTable_Object = MibTable
cpmCallHistorySummaryTable = _CpmCallHistorySummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cpmCallHistorySummaryTable.setStatus("current")
_CpmCallHistorySummaryEntry_Object = MibTableRow
cpmCallHistorySummaryEntry = _CpmCallHistorySummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1)
)
cpmCallHistorySummaryEntry.setIndexNames(
    (0, "CISCO-POP-MGMT-MIB", "cpmCallDisconnectTimeIndex"),
    (0, "CISCO-POP-MGMT-MIB", "cpmCallStartTimeIndex"),
    (0, "CISCO-POP-MGMT-MIB", "cpmCallHistorySummaryIndex"),
)
if mibBuilder.loadTexts:
    cpmCallHistorySummaryEntry.setStatus("current")
_CpmCallDisconnectTimeIndex_Type = TimeStamp
_CpmCallDisconnectTimeIndex_Object = MibTableColumn
cpmCallDisconnectTimeIndex = _CpmCallDisconnectTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 1),
    _CpmCallDisconnectTimeIndex_Type()
)
cpmCallDisconnectTimeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpmCallDisconnectTimeIndex.setStatus("current")
_CpmCallStartTimeIndex_Type = TimeStamp
_CpmCallStartTimeIndex_Object = MibTableColumn
cpmCallStartTimeIndex = _CpmCallStartTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 2),
    _CpmCallStartTimeIndex_Type()
)
cpmCallStartTimeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpmCallStartTimeIndex.setStatus("current")


class _CpmCallHistorySummaryIndex_Type(Integer32):
    """Custom type cpmCallHistorySummaryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpmCallHistorySummaryIndex_Type.__name__ = "Integer32"
_CpmCallHistorySummaryIndex_Object = MibTableColumn
cpmCallHistorySummaryIndex = _CpmCallHistorySummaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 3),
    _CpmCallHistorySummaryIndex_Type()
)
cpmCallHistorySummaryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpmCallHistorySummaryIndex.setStatus("current")


class _CpmUserID_Type(DisplayString):
    """Custom type cpmUserID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpmUserID_Type.__name__ = "DisplayString"
_CpmUserID_Object = MibTableColumn
cpmUserID = _CpmUserID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 4),
    _CpmUserID_Type()
)
cpmUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmUserID.setStatus("current")
_CpmUserIpAddr_Type = IpAddress
_CpmUserIpAddr_Object = MibTableColumn
cpmUserIpAddr = _CpmUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 5),
    _CpmUserIpAddr_Type()
)
cpmUserIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmUserIpAddr.setStatus("current")


class _CpmCallType_Type(Integer32):
    """Custom type cpmCallType based on Integer32"""
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
        *(("analog", 2),
          ("digital", 3),
          ("unknown", 1),
          ("v110", 4),
          ("v120", 5),
          ("voice", 6))
    )


_CpmCallType_Type.__name__ = "Integer32"
_CpmCallType_Object = MibTableColumn
cpmCallType = _CpmCallType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 6),
    _CpmCallType_Type()
)
cpmCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCallType.setStatus("current")
_CpmModemSlot_Type = Integer32
_CpmModemSlot_Object = MibTableColumn
cpmModemSlot = _CpmModemSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 7),
    _CpmModemSlot_Type()
)
cpmModemSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmModemSlot.setStatus("current")
_CpmModemPort_Type = Integer32
_CpmModemPort_Object = MibTableColumn
cpmModemPort = _CpmModemPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 8),
    _CpmModemPort_Type()
)
cpmModemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmModemPort.setStatus("current")
_CpmCallDuration_Type = TimeTicks
_CpmCallDuration_Object = MibTableColumn
cpmCallDuration = _CpmCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 9),
    _CpmCallDuration_Type()
)
cpmCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCallDuration.setStatus("current")
_CpmEntrySlot_Type = Integer32
_CpmEntrySlot_Object = MibTableColumn
cpmEntrySlot = _CpmEntrySlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 10),
    _CpmEntrySlot_Type()
)
cpmEntrySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmEntrySlot.setStatus("current")
_CpmEntryPort_Type = Integer32
_CpmEntryPort_Object = MibTableColumn
cpmEntryPort = _CpmEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 11),
    _CpmEntryPort_Type()
)
cpmEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmEntryPort.setStatus("current")
_CpmEntryChannel_Type = Integer32
_CpmEntryChannel_Object = MibTableColumn
cpmEntryChannel = _CpmEntryChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 12),
    _CpmEntryChannel_Type()
)
cpmEntryChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmEntryChannel.setStatus("current")


class _CpmRemotePhoneNumber_Type(DisplayString):
    """Custom type cpmRemotePhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpmRemotePhoneNumber_Type.__name__ = "DisplayString"
_CpmRemotePhoneNumber_Object = MibTableColumn
cpmRemotePhoneNumber = _CpmRemotePhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 13),
    _CpmRemotePhoneNumber_Type()
)
cpmRemotePhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmRemotePhoneNumber.setStatus("current")


class _CpmLocalPhoneNumber_Type(DisplayString):
    """Custom type cpmLocalPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpmLocalPhoneNumber_Type.__name__ = "DisplayString"
_CpmLocalPhoneNumber_Object = MibTableColumn
cpmLocalPhoneNumber = _CpmLocalPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 14),
    _CpmLocalPhoneNumber_Type()
)
cpmLocalPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmLocalPhoneNumber.setStatus("current")
_CpmTTYNumber_Type = Integer32
_CpmTTYNumber_Object = MibTableColumn
cpmTTYNumber = _CpmTTYNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 4, 3, 1, 15),
    _CpmTTYNumber_Type()
)
cpmTTYNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmTTYNumber.setStatus("current")
_CpmDS0Status_ObjectIdentity = ObjectIdentity
cpmDS0Status = _CpmDS0Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 5)
)
_CpmDS0BusyoutNotifyEnable_Type = TruthValue
_CpmDS0BusyoutNotifyEnable_Object = MibScalar
cpmDS0BusyoutNotifyEnable = _CpmDS0BusyoutNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 5, 1),
    _CpmDS0BusyoutNotifyEnable_Type()
)
cpmDS0BusyoutNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDS0BusyoutNotifyEnable.setStatus("current")
_CpmDS0StatusTable_Object = MibTable
cpmDS0StatusTable = _CpmDS0StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cpmDS0StatusTable.setStatus("current")
_CpmDS0StatusEntry_Object = MibTableRow
cpmDS0StatusEntry = _CpmDS0StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    cpmDS0StatusEntry.setStatus("current")


class _CpmDS0OperStatus_Type(Integer32):
    """Custom type cpmDS0OperStatus based on Integer32"""
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
        *(("connected", 5),
          ("down", 2),
          ("idle", 3),
          ("setup", 4),
          ("test", 6),
          ("unknown", 1))
    )


_CpmDS0OperStatus_Type.__name__ = "Integer32"
_CpmDS0OperStatus_Object = MibTableColumn
cpmDS0OperStatus = _CpmDS0OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 5, 2, 1, 1),
    _CpmDS0OperStatus_Type()
)
cpmDS0OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDS0OperStatus.setStatus("current")


class _CpmDS0BusyoutAdminStatus_Type(Integer32):
    """Custom type cpmDS0BusyoutAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("busyout", 2),
          ("busyoutImmediate", 3),
          ("noBusyout", 1))
    )


_CpmDS0BusyoutAdminStatus_Type.__name__ = "Integer32"
_CpmDS0BusyoutAdminStatus_Object = MibTableColumn
cpmDS0BusyoutAdminStatus = _CpmDS0BusyoutAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 5, 2, 1, 2),
    _CpmDS0BusyoutAdminStatus_Type()
)
cpmDS0BusyoutAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDS0BusyoutAdminStatus.setStatus("current")
_CpmDS0BusyoutAllow_Type = TruthValue
_CpmDS0BusyoutAllow_Object = MibTableColumn
cpmDS0BusyoutAllow = _CpmDS0BusyoutAllow_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 5, 2, 1, 3),
    _CpmDS0BusyoutAllow_Type()
)
cpmDS0BusyoutAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDS0BusyoutAllow.setStatus("current")


class _CpmDS0BusyoutStatus_Type(Integer32):
    """Custom type cpmDS0BusyoutStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("busiedOut", 3),
          ("busyoutPending", 2),
          ("noBusyout", 1))
    )


_CpmDS0BusyoutStatus_Type.__name__ = "Integer32"
_CpmDS0BusyoutStatus_Object = MibTableColumn
cpmDS0BusyoutStatus = _CpmDS0BusyoutStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 5, 2, 1, 4),
    _CpmDS0BusyoutStatus_Type()
)
cpmDS0BusyoutStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDS0BusyoutStatus.setStatus("current")


class _CpmDS0BusyoutSource_Type(Integer32):
    """Custom type cpmDS0BusyoutSource based on Integer32"""
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
        *(("internal", 3),
          ("local", 2),
          ("none", 1),
          ("remote", 4))
    )


_CpmDS0BusyoutSource_Type.__name__ = "Integer32"
_CpmDS0BusyoutSource_Object = MibTableColumn
cpmDS0BusyoutSource = _CpmDS0BusyoutSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 5, 2, 1, 5),
    _CpmDS0BusyoutSource_Type()
)
cpmDS0BusyoutSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDS0BusyoutSource.setStatus("current")
_CpmDS0BusyoutTime_Type = TimeStamp
_CpmDS0BusyoutTime_Object = MibTableColumn
cpmDS0BusyoutTime = _CpmDS0BusyoutTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 5, 2, 1, 6),
    _CpmDS0BusyoutTime_Type()
)
cpmDS0BusyoutTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDS0BusyoutTime.setStatus("current")


class _CpmDS0ConfigFunction_Type(Integer32):
    """Custom type cpmDS0ConfigFunction based on Integer32"""
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
        *(("e1CasChan", 7),
          ("e1CcsBearerChan", 5),
          ("e1CcsSignallingChan", 4),
          ("t1CasChan", 6),
          ("t1CcsBearerChan", 3),
          ("t1CcsSignallingChan", 2),
          ("unknown", 1))
    )


_CpmDS0ConfigFunction_Type.__name__ = "Integer32"
_CpmDS0ConfigFunction_Object = MibTableColumn
cpmDS0ConfigFunction = _CpmDS0ConfigFunction_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 5, 2, 1, 7),
    _CpmDS0ConfigFunction_Type()
)
cpmDS0ConfigFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDS0ConfigFunction.setStatus("current")
_CpmDS0InterfaceIndex_Type = InterfaceIndexOrZero
_CpmDS0InterfaceIndex_Object = MibTableColumn
cpmDS0InterfaceIndex = _CpmDS0InterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 5, 2, 1, 8),
    _CpmDS0InterfaceIndex_Type()
)
cpmDS0InterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDS0InterfaceIndex.setStatus("current")
_CpmDS1LoopbackNotifyConfig_ObjectIdentity = ObjectIdentity
cpmDS1LoopbackNotifyConfig = _CpmDS1LoopbackNotifyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 6)
)
_CpmDS1LoopbackNotifyEnable_Type = TruthValue
_CpmDS1LoopbackNotifyEnable_Object = MibScalar
cpmDS1LoopbackNotifyEnable = _CpmDS1LoopbackNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 6, 1),
    _CpmDS1LoopbackNotifyEnable_Type()
)
cpmDS1LoopbackNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDS1LoopbackNotifyEnable.setStatus("current")
_CpmCallVolume_ObjectIdentity = ObjectIdentity
cpmCallVolume = _CpmCallVolume_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 7)
)
_CpmCallVolSuccISDNDigital_Type = Counter32
_CpmCallVolSuccISDNDigital_Object = MibScalar
cpmCallVolSuccISDNDigital = _CpmCallVolSuccISDNDigital_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 7, 1),
    _CpmCallVolSuccISDNDigital_Type()
)
cpmCallVolSuccISDNDigital.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCallVolSuccISDNDigital.setStatus("current")
_CpmCallVolAnalogCallClearedNormally_Type = Counter32
_CpmCallVolAnalogCallClearedNormally_Object = MibScalar
cpmCallVolAnalogCallClearedNormally = _CpmCallVolAnalogCallClearedNormally_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 1, 7, 2),
    _CpmCallVolAnalogCallClearedNormally_Type()
)
cpmCallVolAnalogCallClearedNormally.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmCallVolAnalogCallClearedNormally.setStatus("current")
_CPopMgmtMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cPopMgmtMIBNotificationPrefix = _CPopMgmtMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 2)
)
_CpmNotifications_ObjectIdentity = ObjectIdentity
cpmNotifications = _CpmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 2, 0)
)
_CpmMIBConformance_ObjectIdentity = ObjectIdentity
cpmMIBConformance = _CpmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 3)
)
_CpmMIBCompliances_ObjectIdentity = ObjectIdentity
cpmMIBCompliances = _CpmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 3, 1)
)
_CpmMIBGroups_ObjectIdentity = ObjectIdentity
cpmMIBGroups = _CpmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 3, 2)
)
cpmDS0UsageEntry.registerAugmentions(
    ("CISCO-POP-MGMT-MIB",
     "cpmDS0StatusEntry")
)
cpmDS0StatusEntry.setIndexNames(*cpmDS0UsageEntry.getIndexNames())

# Managed Objects groups

cpmDS0UsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 3, 2, 1)
)
cpmDS0UsageGroup.setObjects(
      *(("CISCO-POP-MGMT-MIB", "cpmConfiguredType"),
        ("CISCO-POP-MGMT-MIB", "cpmDS0CallType"),
        ("CISCO-POP-MGMT-MIB", "cpmL2Encapsulation"),
        ("CISCO-POP-MGMT-MIB", "cpmCallCount"),
        ("CISCO-POP-MGMT-MIB", "cpmTimeInUse"),
        ("CISCO-POP-MGMT-MIB", "cpmInOctets"),
        ("CISCO-POP-MGMT-MIB", "cpmOutOctets"),
        ("CISCO-POP-MGMT-MIB", "cpmInPackets"),
        ("CISCO-POP-MGMT-MIB", "cpmOutPackets"),
        ("CISCO-POP-MGMT-MIB", "cpmAssociatedInterface"),
        ("CISCO-POP-MGMT-MIB", "cpmISDNCfgBChanInUseForAnalog"),
        ("CISCO-POP-MGMT-MIB", "cpmISDNCfgBChannelsInUse"),
        ("CISCO-POP-MGMT-MIB", "cpmActiveDS0s"),
        ("CISCO-POP-MGMT-MIB", "cpmPPPCalls"),
        ("CISCO-POP-MGMT-MIB", "cpmV120Calls"),
        ("CISCO-POP-MGMT-MIB", "cpmV110Calls"))
)
if mibBuilder.loadTexts:
    cpmDS0UsageGroup.setStatus("obsolete")

cpmCallFailureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 3, 2, 2)
)
cpmCallFailureGroup.setObjects(
      *(("CISCO-POP-MGMT-MIB", "cpmISDNCallsRejected"),
        ("CISCO-POP-MGMT-MIB", "cpmModemCallsRejected"),
        ("CISCO-POP-MGMT-MIB", "cpmISDNCallsClearedAbnormally"),
        ("CISCO-POP-MGMT-MIB", "cpmModemCallsClearedAbnormally"),
        ("CISCO-POP-MGMT-MIB", "cpmISDNNoResource"),
        ("CISCO-POP-MGMT-MIB", "cpmModemNoResource"))
)
if mibBuilder.loadTexts:
    cpmCallFailureGroup.setStatus("current")

cpmActiveCallSummaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 3, 2, 3)
)
cpmActiveCallSummaryGroup.setObjects(
      *(("CISCO-POP-MGMT-MIB", "cpmActiveUserID"),
        ("CISCO-POP-MGMT-MIB", "cpmActiveCallType"),
        ("CISCO-POP-MGMT-MIB", "cpmActiveUserIpAddr"),
        ("CISCO-POP-MGMT-MIB", "cpmActiveModemSlot"),
        ("CISCO-POP-MGMT-MIB", "cpmActiveModemPort"),
        ("CISCO-POP-MGMT-MIB", "cpmActiveCallDuration"),
        ("CISCO-POP-MGMT-MIB", "cpmActiveEntrySlot"),
        ("CISCO-POP-MGMT-MIB", "cpmActiveEntryPort"),
        ("CISCO-POP-MGMT-MIB", "cpmActiveEntryChannel"),
        ("CISCO-POP-MGMT-MIB", "cpmActiveRemotePhoneNumber"),
        ("CISCO-POP-MGMT-MIB", "cpmActiveLocalPhoneNumber"),
        ("CISCO-POP-MGMT-MIB", "cpmActiveTTYNumber"))
)
if mibBuilder.loadTexts:
    cpmActiveCallSummaryGroup.setStatus("current")

cpmCallHistorySummaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 3, 2, 4)
)
cpmCallHistorySummaryGroup.setObjects(
      *(("CISCO-POP-MGMT-MIB", "cpmCallHistorySummaryTableMaxLength"),
        ("CISCO-POP-MGMT-MIB", "cpmCallHistorySummaryRetainTimer"),
        ("CISCO-POP-MGMT-MIB", "cpmUserID"),
        ("CISCO-POP-MGMT-MIB", "cpmUserIpAddr"),
        ("CISCO-POP-MGMT-MIB", "cpmCallType"),
        ("CISCO-POP-MGMT-MIB", "cpmModemSlot"),
        ("CISCO-POP-MGMT-MIB", "cpmModemPort"),
        ("CISCO-POP-MGMT-MIB", "cpmCallDuration"),
        ("CISCO-POP-MGMT-MIB", "cpmEntrySlot"),
        ("CISCO-POP-MGMT-MIB", "cpmEntryPort"),
        ("CISCO-POP-MGMT-MIB", "cpmEntryChannel"),
        ("CISCO-POP-MGMT-MIB", "cpmRemotePhoneNumber"),
        ("CISCO-POP-MGMT-MIB", "cpmLocalPhoneNumber"),
        ("CISCO-POP-MGMT-MIB", "cpmTTYNumber"))
)
if mibBuilder.loadTexts:
    cpmCallHistorySummaryGroup.setStatus("current")

cpmDS0UsageGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 3, 2, 5)
)
cpmDS0UsageGroupRev1.setObjects(
      *(("CISCO-POP-MGMT-MIB", "cpmConfiguredType"),
        ("CISCO-POP-MGMT-MIB", "cpmDS0CallType"),
        ("CISCO-POP-MGMT-MIB", "cpmL2Encapsulation"),
        ("CISCO-POP-MGMT-MIB", "cpmCallCount"),
        ("CISCO-POP-MGMT-MIB", "cpmTimeInUse"),
        ("CISCO-POP-MGMT-MIB", "cpmInOctets"),
        ("CISCO-POP-MGMT-MIB", "cpmOutOctets"),
        ("CISCO-POP-MGMT-MIB", "cpmInPackets"),
        ("CISCO-POP-MGMT-MIB", "cpmOutPackets"),
        ("CISCO-POP-MGMT-MIB", "cpmAssociatedInterface"),
        ("CISCO-POP-MGMT-MIB", "cpmISDNCfgBChanInUseForAnalog"),
        ("CISCO-POP-MGMT-MIB", "cpmISDNCfgBChannelsInUse"),
        ("CISCO-POP-MGMT-MIB", "cpmActiveDS0s"),
        ("CISCO-POP-MGMT-MIB", "cpmPPPCalls"),
        ("CISCO-POP-MGMT-MIB", "cpmV120Calls"),
        ("CISCO-POP-MGMT-MIB", "cpmV110Calls"),
        ("CISCO-POP-MGMT-MIB", "cpmActiveDS0sHighWaterMark"),
        ("CISCO-POP-MGMT-MIB", "cpmDS1ActiveDS0s"),
        ("CISCO-POP-MGMT-MIB", "cpmDS1ActiveDS0sHighWaterMark"),
        ("CISCO-POP-MGMT-MIB", "cpmSW56CfgBChannelsInUse"))
)
if mibBuilder.loadTexts:
    cpmDS0UsageGroupRev1.setStatus("obsolete")

cpmDS0UsageGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 3, 2, 6)
)
cpmDS0UsageGroupRev2.setObjects(
      *(("CISCO-POP-MGMT-MIB", "cpmConfiguredType"),
        ("CISCO-POP-MGMT-MIB", "cpmDS0CallType"),
        ("CISCO-POP-MGMT-MIB", "cpmL2Encapsulation"),
        ("CISCO-POP-MGMT-MIB", "cpmCallCount"),
        ("CISCO-POP-MGMT-MIB", "cpmTimeInUse"),
        ("CISCO-POP-MGMT-MIB", "cpmInOctets"),
        ("CISCO-POP-MGMT-MIB", "cpmOutOctets"),
        ("CISCO-POP-MGMT-MIB", "cpmInPackets"),
        ("CISCO-POP-MGMT-MIB", "cpmOutPackets"),
        ("CISCO-POP-MGMT-MIB", "cpmAssociatedInterface"),
        ("CISCO-POP-MGMT-MIB", "cpmISDNCfgBChanInUseForAnalog"),
        ("CISCO-POP-MGMT-MIB", "cpmISDNCfgBChannelsInUse"),
        ("CISCO-POP-MGMT-MIB", "cpmActiveDS0s"),
        ("CISCO-POP-MGMT-MIB", "cpmPPPCalls"),
        ("CISCO-POP-MGMT-MIB", "cpmV120Calls"),
        ("CISCO-POP-MGMT-MIB", "cpmV110Calls"),
        ("CISCO-POP-MGMT-MIB", "cpmActiveDS0sHighWaterMark"),
        ("CISCO-POP-MGMT-MIB", "cpmDS1ActiveDS0s"),
        ("CISCO-POP-MGMT-MIB", "cpmDS1ActiveDS0sHighWaterMark"),
        ("CISCO-POP-MGMT-MIB", "cpmSW56CfgBChannelsInUse"),
        ("CISCO-POP-MGMT-MIB", "cpmISDNCfgBChanInUseForVoice"),
        ("CISCO-POP-MGMT-MIB", "cpmCASCfgBChanInUseForVoice"))
)
if mibBuilder.loadTexts:
    cpmDS0UsageGroupRev2.setStatus("current")

cpmDS1UsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 3, 2, 7)
)
cpmDS1UsageGroup.setObjects(
      *(("CISCO-POP-MGMT-MIB", "cpmDS1TotalAnalogCalls"),
        ("CISCO-POP-MGMT-MIB", "cpmDS1TotalDigitalCalls"),
        ("CISCO-POP-MGMT-MIB", "cpmDS1TotalV110Calls"),
        ("CISCO-POP-MGMT-MIB", "cpmDS1TotalV120Calls"),
        ("CISCO-POP-MGMT-MIB", "cpmDS1TotalCalls"),
        ("CISCO-POP-MGMT-MIB", "cpmDS1TotalTimeInUse"),
        ("CISCO-POP-MGMT-MIB", "cpmDS1CurrentIdle"),
        ("CISCO-POP-MGMT-MIB", "cpmDS1CurrentOutOfService"),
        ("CISCO-POP-MGMT-MIB", "cpmDS1CurrentBusyout"),
        ("CISCO-POP-MGMT-MIB", "cpmDS1InOctets"),
        ("CISCO-POP-MGMT-MIB", "cpmDS1OutOctets"),
        ("CISCO-POP-MGMT-MIB", "cpmDS1InPackets"),
        ("CISCO-POP-MGMT-MIB", "cpmDS1OutPackets"))
)
if mibBuilder.loadTexts:
    cpmDS1UsageGroup.setStatus("current")

cpmSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 3, 2, 8)
)
cpmSystemGroup.setObjects(
      *(("CISCO-POP-MGMT-MIB", "cpmISDNCfgActiveDChannels"),
        ("CISCO-POP-MGMT-MIB", "cpmISDNCfgBChannelsTimeInUse"),
        ("CISCO-POP-MGMT-MIB", "cpmISDNCfgBChannelsTimeInUseAnlg"),
        ("CISCO-POP-MGMT-MIB", "cpmISDNCfgBChannelCalls"),
        ("CISCO-POP-MGMT-MIB", "cpmISDNCfgBChannelAnalogCalls"),
        ("CISCO-POP-MGMT-MIB", "cpmTotalISDNSyncPPPCalls"))
)
if mibBuilder.loadTexts:
    cpmSystemGroup.setStatus("current")

cpmDS0StatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 3, 2, 9)
)
cpmDS0StatusGroup.setObjects(
      *(("CISCO-POP-MGMT-MIB", "cpmDS0BusyoutNotifyEnable"),
        ("CISCO-POP-MGMT-MIB", "cpmDS0OperStatus"),
        ("CISCO-POP-MGMT-MIB", "cpmDS0BusyoutAdminStatus"),
        ("CISCO-POP-MGMT-MIB", "cpmDS0BusyoutAllow"),
        ("CISCO-POP-MGMT-MIB", "cpmDS0BusyoutStatus"),
        ("CISCO-POP-MGMT-MIB", "cpmDS0BusyoutSource"),
        ("CISCO-POP-MGMT-MIB", "cpmDS0BusyoutTime"),
        ("CISCO-POP-MGMT-MIB", "cpmDS0ConfigFunction"),
        ("CISCO-POP-MGMT-MIB", "cpmDS0InterfaceIndex"))
)
if mibBuilder.loadTexts:
    cpmDS0StatusGroup.setStatus("current")

cpmDS1LoopbackNotifyConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 3, 2, 11)
)
cpmDS1LoopbackNotifyConfigGroup.setObjects(
    ("CISCO-POP-MGMT-MIB", "cpmDS1LoopbackNotifyEnable")
)
if mibBuilder.loadTexts:
    cpmDS1LoopbackNotifyConfigGroup.setStatus("current")

cpmCallVolumeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 3, 2, 12)
)
cpmCallVolumeGroup.setObjects(
      *(("CISCO-POP-MGMT-MIB", "cpmCallVolSuccISDNDigital"),
        ("CISCO-POP-MGMT-MIB", "cpmCallVolAnalogCallClearedNormally"))
)
if mibBuilder.loadTexts:
    cpmCallVolumeGroup.setStatus("current")


# Notification objects

cpmDS0BusyoutNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 2, 0, 1)
)
cpmDS0BusyoutNotification.setObjects(
      *(("CISCO-POP-MGMT-MIB", "cpmDS0BusyoutStatus"),
        ("CISCO-POP-MGMT-MIB", "cpmDS0BusyoutTime"),
        ("CISCO-POP-MGMT-MIB", "cpmDS0BusyoutSource"),
        ("CISCO-POP-MGMT-MIB", "cpmDS0InterfaceIndex"))
)
if mibBuilder.loadTexts:
    cpmDS0BusyoutNotification.setStatus(
        "current"
    )

cpmDS1LoopbackNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 2, 0, 2)
)
cpmDS1LoopbackNotification.setObjects(
      *(("DS1-MIB", "dsx1LineStatus"),
        ("DS1-MIB", "dsx1LineIndex"))
)
if mibBuilder.loadTexts:
    cpmDS1LoopbackNotification.setStatus(
        "current"
    )


# Notifications groups

cpmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 3, 2, 10)
)
cpmNotificationGroup.setObjects(
    ("CISCO-POP-MGMT-MIB", "cpmDS0BusyoutNotification")
)
if mibBuilder.loadTexts:
    cpmNotificationGroup.setStatus(
        "deprecated"
    )

cpmNotificationGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 3, 2, 13)
)
cpmNotificationGroupRev1.setObjects(
      *(("CISCO-POP-MGMT-MIB", "cpmDS0BusyoutNotification"),
        ("CISCO-POP-MGMT-MIB", "cpmDS1LoopbackNotification"))
)
if mibBuilder.loadTexts:
    cpmNotificationGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cpmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cpmMIBCompliance.setStatus(
        "obsolete"
    )

cpmMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cpmMIBComplianceRev1.setStatus(
        "obsolete"
    )

cpmComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cpmComplianceRev2.setStatus(
        "obsolete"
    )

cpmMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 3, 1, 4)
)
if mibBuilder.loadTexts:
    cpmMIBComplianceRev3.setStatus(
        "deprecated"
    )

cpmMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 3, 1, 5)
)
if mibBuilder.loadTexts:
    cpmMIBComplianceRev4.setStatus(
        "deprecated"
    )

cpmMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 19, 3, 1, 6)
)
if mibBuilder.loadTexts:
    cpmMIBComplianceRev5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-POP-MGMT-MIB",
    **{"ciscoPopMgmtMIB": ciscoPopMgmtMIB,
       "ciscoPopMgmtMIBObjects": ciscoPopMgmtMIBObjects,
       "cpmDS0Usage": cpmDS0Usage,
       "cpmDS0UsageTable": cpmDS0UsageTable,
       "cpmDS0UsageEntry": cpmDS0UsageEntry,
       "cpmDS1SlotIndex": cpmDS1SlotIndex,
       "cpmDS1PortIndex": cpmDS1PortIndex,
       "cpmChannelIndex": cpmChannelIndex,
       "cpmConfiguredType": cpmConfiguredType,
       "cpmDS0CallType": cpmDS0CallType,
       "cpmL2Encapsulation": cpmL2Encapsulation,
       "cpmCallCount": cpmCallCount,
       "cpmTimeInUse": cpmTimeInUse,
       "cpmInOctets": cpmInOctets,
       "cpmOutOctets": cpmOutOctets,
       "cpmInPackets": cpmInPackets,
       "cpmOutPackets": cpmOutPackets,
       "cpmAssociatedInterface": cpmAssociatedInterface,
       "cpmISDNCfgBChanInUseForAnalog": cpmISDNCfgBChanInUseForAnalog,
       "cpmISDNCfgBChannelsInUse": cpmISDNCfgBChannelsInUse,
       "cpmActiveDS0s": cpmActiveDS0s,
       "cpmPPPCalls": cpmPPPCalls,
       "cpmV120Calls": cpmV120Calls,
       "cpmV110Calls": cpmV110Calls,
       "cpmActiveDS0sHighWaterMark": cpmActiveDS0sHighWaterMark,
       "cpmDS1DS0UsageTable": cpmDS1DS0UsageTable,
       "cpmDS1DS0UsageEntry": cpmDS1DS0UsageEntry,
       "cpmDS1UsageSlotIndex": cpmDS1UsageSlotIndex,
       "cpmDS1UsagePortIndex": cpmDS1UsagePortIndex,
       "cpmDS1ActiveDS0s": cpmDS1ActiveDS0s,
       "cpmDS1ActiveDS0sHighWaterMark": cpmDS1ActiveDS0sHighWaterMark,
       "cpmDS1TotalAnalogCalls": cpmDS1TotalAnalogCalls,
       "cpmDS1TotalDigitalCalls": cpmDS1TotalDigitalCalls,
       "cpmDS1TotalV110Calls": cpmDS1TotalV110Calls,
       "cpmDS1TotalV120Calls": cpmDS1TotalV120Calls,
       "cpmDS1TotalCalls": cpmDS1TotalCalls,
       "cpmDS1TotalTimeInUse": cpmDS1TotalTimeInUse,
       "cpmDS1CurrentIdle": cpmDS1CurrentIdle,
       "cpmDS1CurrentOutOfService": cpmDS1CurrentOutOfService,
       "cpmDS1CurrentBusyout": cpmDS1CurrentBusyout,
       "cpmDS1InOctets": cpmDS1InOctets,
       "cpmDS1OutOctets": cpmDS1OutOctets,
       "cpmDS1InPackets": cpmDS1InPackets,
       "cpmDS1OutPackets": cpmDS1OutPackets,
       "cpmSW56CfgBChannelsInUse": cpmSW56CfgBChannelsInUse,
       "cpmISDNCfgBChanInUseForVoice": cpmISDNCfgBChanInUseForVoice,
       "cpmCASCfgBChanInUseForVoice": cpmCASCfgBChanInUseForVoice,
       "cpmISDNCfgActiveDChannels": cpmISDNCfgActiveDChannels,
       "cpmISDNCfgBChannelsTimeInUse": cpmISDNCfgBChannelsTimeInUse,
       "cpmISDNCfgBChannelsTimeInUseAnlg": cpmISDNCfgBChannelsTimeInUseAnlg,
       "cpmISDNCfgBChannelCalls": cpmISDNCfgBChannelCalls,
       "cpmISDNCfgBChannelAnalogCalls": cpmISDNCfgBChannelAnalogCalls,
       "cpmTotalISDNSyncPPPCalls": cpmTotalISDNSyncPPPCalls,
       "cpmCallFailure": cpmCallFailure,
       "cpmISDNCallsRejected": cpmISDNCallsRejected,
       "cpmModemCallsRejected": cpmModemCallsRejected,
       "cpmISDNCallsClearedAbnormally": cpmISDNCallsClearedAbnormally,
       "cpmModemCallsClearedAbnormally": cpmModemCallsClearedAbnormally,
       "cpmISDNNoResource": cpmISDNNoResource,
       "cpmModemNoResource": cpmModemNoResource,
       "cpmActiveCallSummary": cpmActiveCallSummary,
       "cpmActiveCallSummaryTable": cpmActiveCallSummaryTable,
       "cpmActiveCallSummaryEntry": cpmActiveCallSummaryEntry,
       "cpmActiveCallStartTimeIndex": cpmActiveCallStartTimeIndex,
       "cpmActiveCallSummaryIndex": cpmActiveCallSummaryIndex,
       "cpmActiveUserID": cpmActiveUserID,
       "cpmActiveUserIpAddr": cpmActiveUserIpAddr,
       "cpmActiveCallType": cpmActiveCallType,
       "cpmActiveModemSlot": cpmActiveModemSlot,
       "cpmActiveModemPort": cpmActiveModemPort,
       "cpmActiveCallDuration": cpmActiveCallDuration,
       "cpmActiveEntrySlot": cpmActiveEntrySlot,
       "cpmActiveEntryPort": cpmActiveEntryPort,
       "cpmActiveEntryChannel": cpmActiveEntryChannel,
       "cpmActiveRemotePhoneNumber": cpmActiveRemotePhoneNumber,
       "cpmActiveLocalPhoneNumber": cpmActiveLocalPhoneNumber,
       "cpmActiveTTYNumber": cpmActiveTTYNumber,
       "cpmCallHistorySummary": cpmCallHistorySummary,
       "cpmCallHistorySummaryTableMaxLength": cpmCallHistorySummaryTableMaxLength,
       "cpmCallHistorySummaryRetainTimer": cpmCallHistorySummaryRetainTimer,
       "cpmCallHistorySummaryTable": cpmCallHistorySummaryTable,
       "cpmCallHistorySummaryEntry": cpmCallHistorySummaryEntry,
       "cpmCallDisconnectTimeIndex": cpmCallDisconnectTimeIndex,
       "cpmCallStartTimeIndex": cpmCallStartTimeIndex,
       "cpmCallHistorySummaryIndex": cpmCallHistorySummaryIndex,
       "cpmUserID": cpmUserID,
       "cpmUserIpAddr": cpmUserIpAddr,
       "cpmCallType": cpmCallType,
       "cpmModemSlot": cpmModemSlot,
       "cpmModemPort": cpmModemPort,
       "cpmCallDuration": cpmCallDuration,
       "cpmEntrySlot": cpmEntrySlot,
       "cpmEntryPort": cpmEntryPort,
       "cpmEntryChannel": cpmEntryChannel,
       "cpmRemotePhoneNumber": cpmRemotePhoneNumber,
       "cpmLocalPhoneNumber": cpmLocalPhoneNumber,
       "cpmTTYNumber": cpmTTYNumber,
       "cpmDS0Status": cpmDS0Status,
       "cpmDS0BusyoutNotifyEnable": cpmDS0BusyoutNotifyEnable,
       "cpmDS0StatusTable": cpmDS0StatusTable,
       "cpmDS0StatusEntry": cpmDS0StatusEntry,
       "cpmDS0OperStatus": cpmDS0OperStatus,
       "cpmDS0BusyoutAdminStatus": cpmDS0BusyoutAdminStatus,
       "cpmDS0BusyoutAllow": cpmDS0BusyoutAllow,
       "cpmDS0BusyoutStatus": cpmDS0BusyoutStatus,
       "cpmDS0BusyoutSource": cpmDS0BusyoutSource,
       "cpmDS0BusyoutTime": cpmDS0BusyoutTime,
       "cpmDS0ConfigFunction": cpmDS0ConfigFunction,
       "cpmDS0InterfaceIndex": cpmDS0InterfaceIndex,
       "cpmDS1LoopbackNotifyConfig": cpmDS1LoopbackNotifyConfig,
       "cpmDS1LoopbackNotifyEnable": cpmDS1LoopbackNotifyEnable,
       "cpmCallVolume": cpmCallVolume,
       "cpmCallVolSuccISDNDigital": cpmCallVolSuccISDNDigital,
       "cpmCallVolAnalogCallClearedNormally": cpmCallVolAnalogCallClearedNormally,
       "cPopMgmtMIBNotificationPrefix": cPopMgmtMIBNotificationPrefix,
       "cpmNotifications": cpmNotifications,
       "cpmDS0BusyoutNotification": cpmDS0BusyoutNotification,
       "cpmDS1LoopbackNotification": cpmDS1LoopbackNotification,
       "cpmMIBConformance": cpmMIBConformance,
       "cpmMIBCompliances": cpmMIBCompliances,
       "cpmMIBCompliance": cpmMIBCompliance,
       "cpmMIBComplianceRev1": cpmMIBComplianceRev1,
       "cpmComplianceRev2": cpmComplianceRev2,
       "cpmMIBComplianceRev3": cpmMIBComplianceRev3,
       "cpmMIBComplianceRev4": cpmMIBComplianceRev4,
       "cpmMIBComplianceRev5": cpmMIBComplianceRev5,
       "cpmMIBGroups": cpmMIBGroups,
       "cpmDS0UsageGroup": cpmDS0UsageGroup,
       "cpmCallFailureGroup": cpmCallFailureGroup,
       "cpmActiveCallSummaryGroup": cpmActiveCallSummaryGroup,
       "cpmCallHistorySummaryGroup": cpmCallHistorySummaryGroup,
       "cpmDS0UsageGroupRev1": cpmDS0UsageGroupRev1,
       "cpmDS0UsageGroupRev2": cpmDS0UsageGroupRev2,
       "cpmDS1UsageGroup": cpmDS1UsageGroup,
       "cpmSystemGroup": cpmSystemGroup,
       "cpmDS0StatusGroup": cpmDS0StatusGroup,
       "cpmNotificationGroup": cpmNotificationGroup,
       "cpmDS1LoopbackNotifyConfigGroup": cpmDS1LoopbackNotifyConfigGroup,
       "cpmCallVolumeGroup": cpmCallVolumeGroup,
       "cpmNotificationGroupRev1": cpmNotificationGroupRev1}
)
