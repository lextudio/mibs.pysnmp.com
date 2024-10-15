# SNMP MIB module (CISCO-CALL-TRACKER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CALL-TRACKER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:48 2024
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

(AbsoluteCounter32,) = mibBuilder.importSymbols(
    "DIAL-CONTROL-MIB",
    "AbsoluteCounter32")

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

ciscoCallTrackerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 163)
)
ciscoCallTrackerMIB.setRevisions(
        ("2005-04-12 00:00",
         "2004-02-02 00:00",
         "2000-02-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CctCallId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CctServiceType(Integer32, TextualConvention):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("exec", 8),
          ("l2f", 9),
          ("l2tp", 10),
          ("mp", 5),
          ("none", 1),
          ("other", 2),
          ("ppp", 4),
          ("slip", 3),
          ("tcpClear", 6),
          ("telnet", 7))
    )



class CctCallCategory(Integer32, TextualConvention):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("casDigital", 7),
          ("isdnSync", 4),
          ("lapb-ta", 10),
          ("mgcpData", 8),
          ("modem", 3),
          ("none", 1),
          ("other", 2),
          ("syncData", 9),
          ("v110", 5),
          ("v120", 6))
    )



class CctCallSigType(Integer32, TextualConvention):
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
        *(("autoDetect", 4),
          ("external", 2),
          ("q931", 3),
          ("unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CctMIBObjects_ObjectIdentity = ObjectIdentity
cctMIBObjects = _CctMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1)
)
_CctGeneral_ObjectIdentity = ObjectIdentity
cctGeneral = _CctGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 1)
)
_CctCallIdPrefix_Type = Unsigned32
_CctCallIdPrefix_Object = MibScalar
cctCallIdPrefix = _CctCallIdPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 1, 1),
    _CctCallIdPrefix_Type()
)
cctCallIdPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctCallIdPrefix.setStatus("current")
_CctActive_ObjectIdentity = ObjectIdentity
cctActive = _CctActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2)
)
_CctActiveTableNumberEntries_Type = Gauge32
_CctActiveTableNumberEntries_Object = MibScalar
cctActiveTableNumberEntries = _CctActiveTableNumberEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 1),
    _CctActiveTableNumberEntries_Type()
)
cctActiveTableNumberEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActiveTableNumberEntries.setStatus("current")
_CctActiveTableHighWaterMark_Type = Gauge32
_CctActiveTableHighWaterMark_Object = MibScalar
cctActiveTableHighWaterMark = _CctActiveTableHighWaterMark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 2),
    _CctActiveTableHighWaterMark_Type()
)
cctActiveTableHighWaterMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActiveTableHighWaterMark.setStatus("current")
_CctActiveTable_Object = MibTable
cctActiveTable = _CctActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cctActiveTable.setStatus("current")
_CctActiveEntry_Object = MibTableRow
cctActiveEntry = _CctActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1)
)
cctActiveEntry.setIndexNames(
    (0, "CISCO-CALL-TRACKER-MIB", "cctActiveCallId"),
)
if mibBuilder.loadTexts:
    cctActiveEntry.setStatus("current")
_CctActiveCallId_Type = CctCallId
_CctActiveCallId_Object = MibTableColumn
cctActiveCallId = _CctActiveCallId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1, 1),
    _CctActiveCallId_Type()
)
cctActiveCallId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cctActiveCallId.setStatus("current")
_CctActiveSetupTime_Type = TimeStamp
_CctActiveSetupTime_Object = MibTableColumn
cctActiveSetupTime = _CctActiveSetupTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1, 2),
    _CctActiveSetupTime_Type()
)
cctActiveSetupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActiveSetupTime.setStatus("current")


class _CctActiveOrigin_Type(Integer32):
    """Custom type cctActiveOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("answer", 2),
          ("originate", 1))
    )


_CctActiveOrigin_Type.__name__ = "Integer32"
_CctActiveOrigin_Object = MibTableColumn
cctActiveOrigin = _CctActiveOrigin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1, 3),
    _CctActiveOrigin_Type()
)
cctActiveOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActiveOrigin.setStatus("current")
_CctActiveConnectionTime_Type = TimeStamp
_CctActiveConnectionTime_Object = MibTableColumn
cctActiveConnectionTime = _CctActiveConnectionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1, 4),
    _CctActiveConnectionTime_Type()
)
cctActiveConnectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActiveConnectionTime.setStatus("current")
_CctActivePhysicalLayerReadyTime_Type = TimeStamp
_CctActivePhysicalLayerReadyTime_Object = MibTableColumn
cctActivePhysicalLayerReadyTime = _CctActivePhysicalLayerReadyTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1, 5),
    _CctActivePhysicalLayerReadyTime_Type()
)
cctActivePhysicalLayerReadyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActivePhysicalLayerReadyTime.setStatus("current")
_CctActiveServiceUpTime_Type = TimeStamp
_CctActiveServiceUpTime_Object = MibTableColumn
cctActiveServiceUpTime = _CctActiveServiceUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1, 6),
    _CctActiveServiceUpTime_Type()
)
cctActiveServiceUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActiveServiceUpTime.setStatus("current")
_CctActiveServiceType_Type = CctServiceType
_CctActiveServiceType_Object = MibTableColumn
cctActiveServiceType = _CctActiveServiceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1, 7),
    _CctActiveServiceType_Type()
)
cctActiveServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActiveServiceType.setStatus("current")
_CctActiveUserValidationTime_Type = TimeStamp
_CctActiveUserValidationTime_Object = MibTableColumn
cctActiveUserValidationTime = _CctActiveUserValidationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1, 8),
    _CctActiveUserValidationTime_Type()
)
cctActiveUserValidationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActiveUserValidationTime.setStatus("current")


class _CctActiveUserId_Type(DisplayString):
    """Custom type cctActiveUserId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CctActiveUserId_Type.__name__ = "DisplayString"
_CctActiveUserId_Object = MibTableColumn
cctActiveUserId = _CctActiveUserId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1, 9),
    _CctActiveUserId_Type()
)
cctActiveUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActiveUserId.setStatus("current")
_CctActiveUserIpAddr_Type = IpAddress
_CctActiveUserIpAddr_Object = MibTableColumn
cctActiveUserIpAddr = _CctActiveUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1, 10),
    _CctActiveUserIpAddr_Type()
)
cctActiveUserIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActiveUserIpAddr.setStatus("current")
_CctActiveUserSubnetMask_Type = IpAddress
_CctActiveUserSubnetMask_Object = MibTableColumn
cctActiveUserSubnetMask = _CctActiveUserSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1, 11),
    _CctActiveUserSubnetMask_Type()
)
cctActiveUserSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActiveUserSubnetMask.setStatus("current")


class _CctActiveAccountingSessionId_Type(DisplayString):
    """Custom type cctActiveAccountingSessionId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CctActiveAccountingSessionId_Type.__name__ = "DisplayString"
_CctActiveAccountingSessionId_Object = MibTableColumn
cctActiveAccountingSessionId = _CctActiveAccountingSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1, 12),
    _CctActiveAccountingSessionId_Type()
)
cctActiveAccountingSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActiveAccountingSessionId.setStatus("current")
_CctActiveCallCategory_Type = CctCallCategory
_CctActiveCallCategory_Object = MibTableColumn
cctActiveCallCategory = _CctActiveCallCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1, 13),
    _CctActiveCallCategory_Type()
)
cctActiveCallCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActiveCallCategory.setStatus("current")
_CctActiveInitialRxRate_Type = Unsigned32
_CctActiveInitialRxRate_Object = MibTableColumn
cctActiveInitialRxRate = _CctActiveInitialRxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1, 14),
    _CctActiveInitialRxRate_Type()
)
cctActiveInitialRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActiveInitialRxRate.setStatus("current")
if mibBuilder.loadTexts:
    cctActiveInitialRxRate.setUnits("bits per second")
_CctActiveInitialTxRate_Type = Unsigned32
_CctActiveInitialTxRate_Object = MibTableColumn
cctActiveInitialTxRate = _CctActiveInitialTxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1, 15),
    _CctActiveInitialTxRate_Type()
)
cctActiveInitialTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActiveInitialTxRate.setStatus("current")
if mibBuilder.loadTexts:
    cctActiveInitialTxRate.setUnits("bits per second")


class _CctActiveResourceSlot_Type(Integer32):
    """Custom type cctActiveResourceSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 214783647),
    )


_CctActiveResourceSlot_Type.__name__ = "Integer32"
_CctActiveResourceSlot_Object = MibTableColumn
cctActiveResourceSlot = _CctActiveResourceSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1, 16),
    _CctActiveResourceSlot_Type()
)
cctActiveResourceSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActiveResourceSlot.setStatus("current")


class _CctActiveResourcePort_Type(Integer32):
    """Custom type cctActiveResourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 214783647),
    )


_CctActiveResourcePort_Type.__name__ = "Integer32"
_CctActiveResourcePort_Object = MibTableColumn
cctActiveResourcePort = _CctActiveResourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1, 17),
    _CctActiveResourcePort_Type()
)
cctActiveResourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActiveResourcePort.setStatus("current")


class _CctActiveEntrySlot_Type(Integer32):
    """Custom type cctActiveEntrySlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 214783647),
    )


_CctActiveEntrySlot_Type.__name__ = "Integer32"
_CctActiveEntrySlot_Object = MibTableColumn
cctActiveEntrySlot = _CctActiveEntrySlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1, 18),
    _CctActiveEntrySlot_Type()
)
cctActiveEntrySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActiveEntrySlot.setStatus("current")


class _CctActiveEntryPort_Type(Integer32):
    """Custom type cctActiveEntryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 214783647),
    )


_CctActiveEntryPort_Type.__name__ = "Integer32"
_CctActiveEntryPort_Object = MibTableColumn
cctActiveEntryPort = _CctActiveEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1, 19),
    _CctActiveEntryPort_Type()
)
cctActiveEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActiveEntryPort.setStatus("current")


class _CctActiveEntryDs1_Type(Integer32):
    """Custom type cctActiveEntryDs1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 214783647),
    )


_CctActiveEntryDs1_Type.__name__ = "Integer32"
_CctActiveEntryDs1_Object = MibTableColumn
cctActiveEntryDs1 = _CctActiveEntryDs1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1, 20),
    _CctActiveEntryDs1_Type()
)
cctActiveEntryDs1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActiveEntryDs1.setStatus("current")


class _CctActiveEntryChannel_Type(Integer32):
    """Custom type cctActiveEntryChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 214783647),
    )


_CctActiveEntryChannel_Type.__name__ = "Integer32"
_CctActiveEntryChannel_Object = MibTableColumn
cctActiveEntryChannel = _CctActiveEntryChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1, 21),
    _CctActiveEntryChannel_Type()
)
cctActiveEntryChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActiveEntryChannel.setStatus("current")


class _CctActiveCalledPartyId_Type(DisplayString):
    """Custom type cctActiveCalledPartyId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CctActiveCalledPartyId_Type.__name__ = "DisplayString"
_CctActiveCalledPartyId_Object = MibTableColumn
cctActiveCalledPartyId = _CctActiveCalledPartyId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1, 22),
    _CctActiveCalledPartyId_Type()
)
cctActiveCalledPartyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActiveCalledPartyId.setStatus("current")


class _CctActiveCallingPartyId_Type(DisplayString):
    """Custom type cctActiveCallingPartyId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CctActiveCallingPartyId_Type.__name__ = "DisplayString"
_CctActiveCallingPartyId_Object = MibTableColumn
cctActiveCallingPartyId = _CctActiveCallingPartyId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1, 23),
    _CctActiveCallingPartyId_Type()
)
cctActiveCallingPartyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActiveCallingPartyId.setStatus("current")
_CctActiveMpBundleId_Type = Unsigned32
_CctActiveMpBundleId_Object = MibTableColumn
cctActiveMpBundleId = _CctActiveMpBundleId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1, 24),
    _CctActiveMpBundleId_Type()
)
cctActiveMpBundleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActiveMpBundleId.setStatus("current")
_CctActiveChargedUnits_Type = AbsoluteCounter32
_CctActiveChargedUnits_Object = MibTableColumn
cctActiveChargedUnits = _CctActiveChargedUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1, 25),
    _CctActiveChargedUnits_Type()
)
cctActiveChargedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActiveChargedUnits.setStatus("current")
_CctActiveReceiveBytes_Type = AbsoluteCounter32
_CctActiveReceiveBytes_Object = MibTableColumn
cctActiveReceiveBytes = _CctActiveReceiveBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1, 26),
    _CctActiveReceiveBytes_Type()
)
cctActiveReceiveBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActiveReceiveBytes.setStatus("current")
if mibBuilder.loadTexts:
    cctActiveReceiveBytes.setUnits("bytes")
_CctActiveTransmitBytes_Type = AbsoluteCounter32
_CctActiveTransmitBytes_Object = MibTableColumn
cctActiveTransmitBytes = _CctActiveTransmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1, 27),
    _CctActiveTransmitBytes_Type()
)
cctActiveTransmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActiveTransmitBytes.setStatus("current")
if mibBuilder.loadTexts:
    cctActiveTransmitBytes.setUnits("bytes")
_CctActiveCallSignalingType_Type = CctCallSigType
_CctActiveCallSignalingType_Object = MibTableColumn
cctActiveCallSignalingType = _CctActiveCallSignalingType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 2, 3, 1, 28),
    _CctActiveCallSignalingType_Type()
)
cctActiveCallSignalingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctActiveCallSignalingType.setStatus("current")
_CctHistory_ObjectIdentity = ObjectIdentity
cctHistory = _CctHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3)
)


class _CctHistoryTableEntriesLimit_Type(Unsigned32):
    """Custom type cctHistoryTableEntriesLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CctHistoryTableEntriesLimit_Type.__name__ = "Unsigned32"
_CctHistoryTableEntriesLimit_Object = MibScalar
cctHistoryTableEntriesLimit = _CctHistoryTableEntriesLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 1),
    _CctHistoryTableEntriesLimit_Type()
)
cctHistoryTableEntriesLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cctHistoryTableEntriesLimit.setStatus("current")
_CctHistoryTableMaxEntries_Type = Unsigned32
_CctHistoryTableMaxEntries_Object = MibScalar
cctHistoryTableMaxEntries = _CctHistoryTableMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 2),
    _CctHistoryTableMaxEntries_Type()
)
cctHistoryTableMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryTableMaxEntries.setStatus("current")


class _CctHistoryTableRetainTimer_Type(Unsigned32):
    """Custom type cctHistoryTableRetainTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CctHistoryTableRetainTimer_Type.__name__ = "Unsigned32"
_CctHistoryTableRetainTimer_Object = MibScalar
cctHistoryTableRetainTimer = _CctHistoryTableRetainTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 3),
    _CctHistoryTableRetainTimer_Type()
)
cctHistoryTableRetainTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cctHistoryTableRetainTimer.setStatus("current")
if mibBuilder.loadTexts:
    cctHistoryTableRetainTimer.setUnits("minutes")
_CctHistoryTableNumberEntries_Type = Gauge32
_CctHistoryTableNumberEntries_Object = MibScalar
cctHistoryTableNumberEntries = _CctHistoryTableNumberEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 4),
    _CctHistoryTableNumberEntries_Type()
)
cctHistoryTableNumberEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryTableNumberEntries.setStatus("current")
_CctHistoryTableHighWaterMark_Type = Gauge32
_CctHistoryTableHighWaterMark_Object = MibScalar
cctHistoryTableHighWaterMark = _CctHistoryTableHighWaterMark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 5),
    _CctHistoryTableHighWaterMark_Type()
)
cctHistoryTableHighWaterMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryTableHighWaterMark.setStatus("current")


class _CctHistoryTableNewestIndex_Type(Unsigned32):
    """Custom type cctHistoryTableNewestIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CctHistoryTableNewestIndex_Type.__name__ = "Unsigned32"
_CctHistoryTableNewestIndex_Object = MibScalar
cctHistoryTableNewestIndex = _CctHistoryTableNewestIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 6),
    _CctHistoryTableNewestIndex_Type()
)
cctHistoryTableNewestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryTableNewestIndex.setStatus("current")
_CctHistoryTable_Object = MibTable
cctHistoryTable = _CctHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7)
)
if mibBuilder.loadTexts:
    cctHistoryTable.setStatus("current")
_CctHistoryEntry_Object = MibTableRow
cctHistoryEntry = _CctHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1)
)
cctHistoryEntry.setIndexNames(
    (0, "CISCO-CALL-TRACKER-MIB", "cctHistoryIndex"),
)
if mibBuilder.loadTexts:
    cctHistoryEntry.setStatus("current")


class _CctHistoryIndex_Type(Unsigned32):
    """Custom type cctHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CctHistoryIndex_Type.__name__ = "Unsigned32"
_CctHistoryIndex_Object = MibTableColumn
cctHistoryIndex = _CctHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 1),
    _CctHistoryIndex_Type()
)
cctHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cctHistoryIndex.setStatus("current")
_CctHistoryCallId_Type = CctCallId
_CctHistoryCallId_Object = MibTableColumn
cctHistoryCallId = _CctHistoryCallId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 2),
    _CctHistoryCallId_Type()
)
cctHistoryCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryCallId.setStatus("current")
_CctHistorySetupTime_Type = TimeStamp
_CctHistorySetupTime_Object = MibTableColumn
cctHistorySetupTime = _CctHistorySetupTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 3),
    _CctHistorySetupTime_Type()
)
cctHistorySetupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistorySetupTime.setStatus("current")


class _CctHistoryOrigin_Type(Integer32):
    """Custom type cctHistoryOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("answer", 2),
          ("originate", 1))
    )


_CctHistoryOrigin_Type.__name__ = "Integer32"
_CctHistoryOrigin_Object = MibTableColumn
cctHistoryOrigin = _CctHistoryOrigin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 4),
    _CctHistoryOrigin_Type()
)
cctHistoryOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryOrigin.setStatus("current")
_CctHistoryConnectionTime_Type = TimeStamp
_CctHistoryConnectionTime_Object = MibTableColumn
cctHistoryConnectionTime = _CctHistoryConnectionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 5),
    _CctHistoryConnectionTime_Type()
)
cctHistoryConnectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryConnectionTime.setStatus("current")
_CctHistoryPhysicalLayerReadyTime_Type = TimeStamp
_CctHistoryPhysicalLayerReadyTime_Object = MibTableColumn
cctHistoryPhysicalLayerReadyTime = _CctHistoryPhysicalLayerReadyTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 6),
    _CctHistoryPhysicalLayerReadyTime_Type()
)
cctHistoryPhysicalLayerReadyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryPhysicalLayerReadyTime.setStatus("current")
_CctHistoryServiceUpTime_Type = TimeStamp
_CctHistoryServiceUpTime_Object = MibTableColumn
cctHistoryServiceUpTime = _CctHistoryServiceUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 7),
    _CctHistoryServiceUpTime_Type()
)
cctHistoryServiceUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryServiceUpTime.setStatus("current")
_CctHistoryServiceType_Type = CctServiceType
_CctHistoryServiceType_Object = MibTableColumn
cctHistoryServiceType = _CctHistoryServiceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 8),
    _CctHistoryServiceType_Type()
)
cctHistoryServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryServiceType.setStatus("current")
_CctHistoryUserValidationTime_Type = TimeStamp
_CctHistoryUserValidationTime_Object = MibTableColumn
cctHistoryUserValidationTime = _CctHistoryUserValidationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 9),
    _CctHistoryUserValidationTime_Type()
)
cctHistoryUserValidationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryUserValidationTime.setStatus("current")


class _CctHistoryUserId_Type(DisplayString):
    """Custom type cctHistoryUserId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CctHistoryUserId_Type.__name__ = "DisplayString"
_CctHistoryUserId_Object = MibTableColumn
cctHistoryUserId = _CctHistoryUserId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 10),
    _CctHistoryUserId_Type()
)
cctHistoryUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryUserId.setStatus("current")
_CctHistoryUserIpAddr_Type = IpAddress
_CctHistoryUserIpAddr_Object = MibTableColumn
cctHistoryUserIpAddr = _CctHistoryUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 11),
    _CctHistoryUserIpAddr_Type()
)
cctHistoryUserIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryUserIpAddr.setStatus("current")
_CctHistoryUserSubnetMask_Type = IpAddress
_CctHistoryUserSubnetMask_Object = MibTableColumn
cctHistoryUserSubnetMask = _CctHistoryUserSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 12),
    _CctHistoryUserSubnetMask_Type()
)
cctHistoryUserSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryUserSubnetMask.setStatus("current")


class _CctHistoryAccountingSessionId_Type(DisplayString):
    """Custom type cctHistoryAccountingSessionId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CctHistoryAccountingSessionId_Type.__name__ = "DisplayString"
_CctHistoryAccountingSessionId_Object = MibTableColumn
cctHistoryAccountingSessionId = _CctHistoryAccountingSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 13),
    _CctHistoryAccountingSessionId_Type()
)
cctHistoryAccountingSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryAccountingSessionId.setStatus("current")
_CctHistoryCallCategory_Type = CctCallCategory
_CctHistoryCallCategory_Object = MibTableColumn
cctHistoryCallCategory = _CctHistoryCallCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 14),
    _CctHistoryCallCategory_Type()
)
cctHistoryCallCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryCallCategory.setStatus("current")
_CctHistoryInitialRxRate_Type = Unsigned32
_CctHistoryInitialRxRate_Object = MibTableColumn
cctHistoryInitialRxRate = _CctHistoryInitialRxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 15),
    _CctHistoryInitialRxRate_Type()
)
cctHistoryInitialRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryInitialRxRate.setStatus("current")
if mibBuilder.loadTexts:
    cctHistoryInitialRxRate.setUnits("bits per second")
_CctHistoryInitialTxRate_Type = Unsigned32
_CctHistoryInitialTxRate_Object = MibTableColumn
cctHistoryInitialTxRate = _CctHistoryInitialTxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 16),
    _CctHistoryInitialTxRate_Type()
)
cctHistoryInitialTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryInitialTxRate.setStatus("current")
if mibBuilder.loadTexts:
    cctHistoryInitialTxRate.setUnits("bits per second")


class _CctHistoryResourceSlot_Type(Integer32):
    """Custom type cctHistoryResourceSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 214783647),
    )


_CctHistoryResourceSlot_Type.__name__ = "Integer32"
_CctHistoryResourceSlot_Object = MibTableColumn
cctHistoryResourceSlot = _CctHistoryResourceSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 17),
    _CctHistoryResourceSlot_Type()
)
cctHistoryResourceSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryResourceSlot.setStatus("current")


class _CctHistoryResourcePort_Type(Integer32):
    """Custom type cctHistoryResourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 214783647),
    )


_CctHistoryResourcePort_Type.__name__ = "Integer32"
_CctHistoryResourcePort_Object = MibTableColumn
cctHistoryResourcePort = _CctHistoryResourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 18),
    _CctHistoryResourcePort_Type()
)
cctHistoryResourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryResourcePort.setStatus("current")


class _CctHistoryEntrySlot_Type(Integer32):
    """Custom type cctHistoryEntrySlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 214783647),
    )


_CctHistoryEntrySlot_Type.__name__ = "Integer32"
_CctHistoryEntrySlot_Object = MibTableColumn
cctHistoryEntrySlot = _CctHistoryEntrySlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 19),
    _CctHistoryEntrySlot_Type()
)
cctHistoryEntrySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryEntrySlot.setStatus("current")


class _CctHistoryEntryPort_Type(Integer32):
    """Custom type cctHistoryEntryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 214783647),
    )


_CctHistoryEntryPort_Type.__name__ = "Integer32"
_CctHistoryEntryPort_Object = MibTableColumn
cctHistoryEntryPort = _CctHistoryEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 20),
    _CctHistoryEntryPort_Type()
)
cctHistoryEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryEntryPort.setStatus("current")


class _CctHistoryEntryDs1_Type(Integer32):
    """Custom type cctHistoryEntryDs1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 214783647),
    )


_CctHistoryEntryDs1_Type.__name__ = "Integer32"
_CctHistoryEntryDs1_Object = MibTableColumn
cctHistoryEntryDs1 = _CctHistoryEntryDs1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 22),
    _CctHistoryEntryDs1_Type()
)
cctHistoryEntryDs1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryEntryDs1.setStatus("current")


class _CctHistoryEntryChannel_Type(Integer32):
    """Custom type cctHistoryEntryChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 214783647),
    )


_CctHistoryEntryChannel_Type.__name__ = "Integer32"
_CctHistoryEntryChannel_Object = MibTableColumn
cctHistoryEntryChannel = _CctHistoryEntryChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 23),
    _CctHistoryEntryChannel_Type()
)
cctHistoryEntryChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryEntryChannel.setStatus("current")


class _CctHistoryCalledPartyId_Type(DisplayString):
    """Custom type cctHistoryCalledPartyId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CctHistoryCalledPartyId_Type.__name__ = "DisplayString"
_CctHistoryCalledPartyId_Object = MibTableColumn
cctHistoryCalledPartyId = _CctHistoryCalledPartyId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 24),
    _CctHistoryCalledPartyId_Type()
)
cctHistoryCalledPartyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryCalledPartyId.setStatus("current")


class _CctHistoryCallingPartyId_Type(DisplayString):
    """Custom type cctHistoryCallingPartyId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CctHistoryCallingPartyId_Type.__name__ = "DisplayString"
_CctHistoryCallingPartyId_Object = MibTableColumn
cctHistoryCallingPartyId = _CctHistoryCallingPartyId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 25),
    _CctHistoryCallingPartyId_Type()
)
cctHistoryCallingPartyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryCallingPartyId.setStatus("current")
_CctHistoryMpBundleId_Type = Unsigned32
_CctHistoryMpBundleId_Object = MibTableColumn
cctHistoryMpBundleId = _CctHistoryMpBundleId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 26),
    _CctHistoryMpBundleId_Type()
)
cctHistoryMpBundleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryMpBundleId.setStatus("current")
_CctHistoryChargedUnits_Type = Gauge32
_CctHistoryChargedUnits_Object = MibTableColumn
cctHistoryChargedUnits = _CctHistoryChargedUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 27),
    _CctHistoryChargedUnits_Type()
)
cctHistoryChargedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryChargedUnits.setStatus("current")
_CctHistoryReceiveBytes_Type = Gauge32
_CctHistoryReceiveBytes_Object = MibTableColumn
cctHistoryReceiveBytes = _CctHistoryReceiveBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 28),
    _CctHistoryReceiveBytes_Type()
)
cctHistoryReceiveBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryReceiveBytes.setStatus("current")
if mibBuilder.loadTexts:
    cctHistoryReceiveBytes.setUnits("bytes")
_CctHistoryTransmitBytes_Type = Gauge32
_CctHistoryTransmitBytes_Object = MibTableColumn
cctHistoryTransmitBytes = _CctHistoryTransmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 29),
    _CctHistoryTransmitBytes_Type()
)
cctHistoryTransmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryTransmitBytes.setStatus("current")
if mibBuilder.loadTexts:
    cctHistoryTransmitBytes.setUnits("bytes")
_CctHistoryDisconnectTime_Type = TimeStamp
_CctHistoryDisconnectTime_Object = MibTableColumn
cctHistoryDisconnectTime = _CctHistoryDisconnectTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 30),
    _CctHistoryDisconnectTime_Type()
)
cctHistoryDisconnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryDisconnectTime.setStatus("current")


class _CctHistoryDisconnectReasonText_Type(DisplayString):
    """Custom type cctHistoryDisconnectReasonText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CctHistoryDisconnectReasonText_Type.__name__ = "DisplayString"
_CctHistoryDisconnectReasonText_Object = MibTableColumn
cctHistoryDisconnectReasonText = _CctHistoryDisconnectReasonText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 31),
    _CctHistoryDisconnectReasonText_Type()
)
cctHistoryDisconnectReasonText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryDisconnectReasonText.setStatus("current")
_CctHistoryCallSignalingType_Type = CctCallSigType
_CctHistoryCallSignalingType_Object = MibTableColumn
cctHistoryCallSignalingType = _CctHistoryCallSignalingType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 3, 7, 1, 32),
    _CctHistoryCallSignalingType_Type()
)
cctHistoryCallSignalingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctHistoryCallSignalingType.setStatus("current")
_CctNotificationConfig_ObjectIdentity = ObjectIdentity
cctNotificationConfig = _CctNotificationConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 4)
)
_CctCallSetupTermNotifyEnable_Type = TruthValue
_CctCallSetupTermNotifyEnable_Object = MibScalar
cctCallSetupTermNotifyEnable = _CctCallSetupTermNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 1, 4, 1),
    _CctCallSetupTermNotifyEnable_Type()
)
cctCallSetupTermNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cctCallSetupTermNotifyEnable.setStatus("current")
_CctMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cctMIBNotificationPrefix = _CctMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 2)
)
_CctMIBNotifications_ObjectIdentity = ObjectIdentity
cctMIBNotifications = _CctMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 2, 0)
)
_CctMIBConformance_ObjectIdentity = ObjectIdentity
cctMIBConformance = _CctMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 3)
)
_CctMIBCompliances_ObjectIdentity = ObjectIdentity
cctMIBCompliances = _CctMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 3, 1)
)
_CctMIBGroups_ObjectIdentity = ObjectIdentity
cctMIBGroups = _CctMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 3, 2)
)

# Managed Objects groups

cctGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 3, 2, 1)
)
cctGeneralGroup.setObjects(
    ("CISCO-CALL-TRACKER-MIB", "cctCallIdPrefix")
)
if mibBuilder.loadTexts:
    cctGeneralGroup.setStatus("current")

cctActiveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 3, 2, 2)
)
cctActiveGroup.setObjects(
      *(("CISCO-CALL-TRACKER-MIB", "cctActiveTableNumberEntries"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveTableHighWaterMark"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveSetupTime"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveOrigin"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveConnectionTime"),
        ("CISCO-CALL-TRACKER-MIB", "cctActivePhysicalLayerReadyTime"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveServiceUpTime"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveServiceType"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveUserValidationTime"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveUserId"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveUserIpAddr"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveUserSubnetMask"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveAccountingSessionId"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveCallCategory"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveInitialRxRate"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveInitialTxRate"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveResourceSlot"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveResourcePort"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveEntrySlot"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveEntryPort"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveEntryDs1"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveEntryChannel"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveCalledPartyId"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveCallingPartyId"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveMpBundleId"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveChargedUnits"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveReceiveBytes"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveTransmitBytes"))
)
if mibBuilder.loadTexts:
    cctActiveGroup.setStatus("deprecated")

cctHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 3, 2, 3)
)
cctHistoryGroup.setObjects(
      *(("CISCO-CALL-TRACKER-MIB", "cctHistoryTableEntriesLimit"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryTableMaxEntries"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryTableRetainTimer"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryTableNumberEntries"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryTableHighWaterMark"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryTableNewestIndex"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryCallId"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistorySetupTime"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryOrigin"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryConnectionTime"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryPhysicalLayerReadyTime"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryServiceUpTime"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryServiceType"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryUserValidationTime"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryUserId"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryUserIpAddr"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryUserSubnetMask"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryAccountingSessionId"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryCallCategory"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryInitialRxRate"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryInitialTxRate"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryResourceSlot"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryResourcePort"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryEntrySlot"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryEntryPort"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryEntryDs1"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryEntryChannel"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryCalledPartyId"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryCallingPartyId"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryMpBundleId"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryChargedUnits"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryReceiveBytes"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryTransmitBytes"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryDisconnectTime"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryDisconnectReasonText"))
)
if mibBuilder.loadTexts:
    cctHistoryGroup.setStatus("deprecated")

cctNotificationConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 3, 2, 4)
)
cctNotificationConfigGroup.setObjects(
    ("CISCO-CALL-TRACKER-MIB", "cctCallSetupTermNotifyEnable")
)
if mibBuilder.loadTexts:
    cctNotificationConfigGroup.setStatus("current")

cctActiveGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 3, 2, 6)
)
cctActiveGroupRev1.setObjects(
      *(("CISCO-CALL-TRACKER-MIB", "cctActiveTableNumberEntries"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveTableHighWaterMark"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveSetupTime"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveOrigin"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveConnectionTime"),
        ("CISCO-CALL-TRACKER-MIB", "cctActivePhysicalLayerReadyTime"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveServiceUpTime"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveServiceType"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveUserValidationTime"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveUserId"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveUserIpAddr"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveUserSubnetMask"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveAccountingSessionId"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveCallCategory"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveInitialRxRate"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveInitialTxRate"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveResourceSlot"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveResourcePort"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveEntrySlot"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveEntryPort"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveEntryDs1"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveEntryChannel"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveCalledPartyId"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveCallingPartyId"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveMpBundleId"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveChargedUnits"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveReceiveBytes"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveTransmitBytes"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveCallSignalingType"))
)
if mibBuilder.loadTexts:
    cctActiveGroupRev1.setStatus("current")

cctHistoryGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 3, 2, 7)
)
cctHistoryGroupRev1.setObjects(
      *(("CISCO-CALL-TRACKER-MIB", "cctHistoryTableEntriesLimit"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryTableMaxEntries"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryTableRetainTimer"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryTableNumberEntries"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryTableHighWaterMark"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryTableNewestIndex"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryCallId"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistorySetupTime"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryOrigin"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryConnectionTime"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryPhysicalLayerReadyTime"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryServiceUpTime"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryServiceType"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryUserValidationTime"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryUserId"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryUserIpAddr"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryUserSubnetMask"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryAccountingSessionId"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryCallCategory"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryInitialRxRate"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryInitialTxRate"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryResourceSlot"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryResourcePort"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryEntrySlot"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryEntryPort"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryEntryDs1"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryEntryChannel"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryCalledPartyId"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryCallingPartyId"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryMpBundleId"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryChargedUnits"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryReceiveBytes"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryTransmitBytes"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryDisconnectTime"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryDisconnectReasonText"),
        ("CISCO-CALL-TRACKER-MIB", "cctHistoryCallSignalingType"))
)
if mibBuilder.loadTexts:
    cctHistoryGroupRev1.setStatus("current")


# Notification objects

cctCallSetupNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 2, 0, 1)
)
cctCallSetupNotification.setObjects(
      *(("CISCO-CALL-TRACKER-MIB", "cctActiveSetupTime"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveCalledPartyId"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveCallingPartyId"),
        ("CISCO-CALL-TRACKER-MIB", "cctActiveCallCategory"))
)
if mibBuilder.loadTexts:
    cctCallSetupNotification.setStatus(
        "current"
    )

cctCallTerminateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 2, 0, 2)
)
cctCallTerminateNotification.setObjects(
    ("CISCO-CALL-TRACKER-MIB", "cctHistoryCallId")
)
if mibBuilder.loadTexts:
    cctCallTerminateNotification.setStatus(
        "current"
    )


# Notifications groups

cctNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 3, 2, 5)
)
cctNotificationGroup.setObjects(
      *(("CISCO-CALL-TRACKER-MIB", "cctCallSetupNotification"),
        ("CISCO-CALL-TRACKER-MIB", "cctCallTerminateNotification"))
)
if mibBuilder.loadTexts:
    cctNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cctMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cctMIBCompliance.setStatus(
        "deprecated"
    )

cctMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 163, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cctMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CALL-TRACKER-MIB",
    **{"CctCallId": CctCallId,
       "CctServiceType": CctServiceType,
       "CctCallCategory": CctCallCategory,
       "CctCallSigType": CctCallSigType,
       "ciscoCallTrackerMIB": ciscoCallTrackerMIB,
       "cctMIBObjects": cctMIBObjects,
       "cctGeneral": cctGeneral,
       "cctCallIdPrefix": cctCallIdPrefix,
       "cctActive": cctActive,
       "cctActiveTableNumberEntries": cctActiveTableNumberEntries,
       "cctActiveTableHighWaterMark": cctActiveTableHighWaterMark,
       "cctActiveTable": cctActiveTable,
       "cctActiveEntry": cctActiveEntry,
       "cctActiveCallId": cctActiveCallId,
       "cctActiveSetupTime": cctActiveSetupTime,
       "cctActiveOrigin": cctActiveOrigin,
       "cctActiveConnectionTime": cctActiveConnectionTime,
       "cctActivePhysicalLayerReadyTime": cctActivePhysicalLayerReadyTime,
       "cctActiveServiceUpTime": cctActiveServiceUpTime,
       "cctActiveServiceType": cctActiveServiceType,
       "cctActiveUserValidationTime": cctActiveUserValidationTime,
       "cctActiveUserId": cctActiveUserId,
       "cctActiveUserIpAddr": cctActiveUserIpAddr,
       "cctActiveUserSubnetMask": cctActiveUserSubnetMask,
       "cctActiveAccountingSessionId": cctActiveAccountingSessionId,
       "cctActiveCallCategory": cctActiveCallCategory,
       "cctActiveInitialRxRate": cctActiveInitialRxRate,
       "cctActiveInitialTxRate": cctActiveInitialTxRate,
       "cctActiveResourceSlot": cctActiveResourceSlot,
       "cctActiveResourcePort": cctActiveResourcePort,
       "cctActiveEntrySlot": cctActiveEntrySlot,
       "cctActiveEntryPort": cctActiveEntryPort,
       "cctActiveEntryDs1": cctActiveEntryDs1,
       "cctActiveEntryChannel": cctActiveEntryChannel,
       "cctActiveCalledPartyId": cctActiveCalledPartyId,
       "cctActiveCallingPartyId": cctActiveCallingPartyId,
       "cctActiveMpBundleId": cctActiveMpBundleId,
       "cctActiveChargedUnits": cctActiveChargedUnits,
       "cctActiveReceiveBytes": cctActiveReceiveBytes,
       "cctActiveTransmitBytes": cctActiveTransmitBytes,
       "cctActiveCallSignalingType": cctActiveCallSignalingType,
       "cctHistory": cctHistory,
       "cctHistoryTableEntriesLimit": cctHistoryTableEntriesLimit,
       "cctHistoryTableMaxEntries": cctHistoryTableMaxEntries,
       "cctHistoryTableRetainTimer": cctHistoryTableRetainTimer,
       "cctHistoryTableNumberEntries": cctHistoryTableNumberEntries,
       "cctHistoryTableHighWaterMark": cctHistoryTableHighWaterMark,
       "cctHistoryTableNewestIndex": cctHistoryTableNewestIndex,
       "cctHistoryTable": cctHistoryTable,
       "cctHistoryEntry": cctHistoryEntry,
       "cctHistoryIndex": cctHistoryIndex,
       "cctHistoryCallId": cctHistoryCallId,
       "cctHistorySetupTime": cctHistorySetupTime,
       "cctHistoryOrigin": cctHistoryOrigin,
       "cctHistoryConnectionTime": cctHistoryConnectionTime,
       "cctHistoryPhysicalLayerReadyTime": cctHistoryPhysicalLayerReadyTime,
       "cctHistoryServiceUpTime": cctHistoryServiceUpTime,
       "cctHistoryServiceType": cctHistoryServiceType,
       "cctHistoryUserValidationTime": cctHistoryUserValidationTime,
       "cctHistoryUserId": cctHistoryUserId,
       "cctHistoryUserIpAddr": cctHistoryUserIpAddr,
       "cctHistoryUserSubnetMask": cctHistoryUserSubnetMask,
       "cctHistoryAccountingSessionId": cctHistoryAccountingSessionId,
       "cctHistoryCallCategory": cctHistoryCallCategory,
       "cctHistoryInitialRxRate": cctHistoryInitialRxRate,
       "cctHistoryInitialTxRate": cctHistoryInitialTxRate,
       "cctHistoryResourceSlot": cctHistoryResourceSlot,
       "cctHistoryResourcePort": cctHistoryResourcePort,
       "cctHistoryEntrySlot": cctHistoryEntrySlot,
       "cctHistoryEntryPort": cctHistoryEntryPort,
       "cctHistoryEntryDs1": cctHistoryEntryDs1,
       "cctHistoryEntryChannel": cctHistoryEntryChannel,
       "cctHistoryCalledPartyId": cctHistoryCalledPartyId,
       "cctHistoryCallingPartyId": cctHistoryCallingPartyId,
       "cctHistoryMpBundleId": cctHistoryMpBundleId,
       "cctHistoryChargedUnits": cctHistoryChargedUnits,
       "cctHistoryReceiveBytes": cctHistoryReceiveBytes,
       "cctHistoryTransmitBytes": cctHistoryTransmitBytes,
       "cctHistoryDisconnectTime": cctHistoryDisconnectTime,
       "cctHistoryDisconnectReasonText": cctHistoryDisconnectReasonText,
       "cctHistoryCallSignalingType": cctHistoryCallSignalingType,
       "cctNotificationConfig": cctNotificationConfig,
       "cctCallSetupTermNotifyEnable": cctCallSetupTermNotifyEnable,
       "cctMIBNotificationPrefix": cctMIBNotificationPrefix,
       "cctMIBNotifications": cctMIBNotifications,
       "cctCallSetupNotification": cctCallSetupNotification,
       "cctCallTerminateNotification": cctCallTerminateNotification,
       "cctMIBConformance": cctMIBConformance,
       "cctMIBCompliances": cctMIBCompliances,
       "cctMIBCompliance": cctMIBCompliance,
       "cctMIBComplianceRev1": cctMIBComplianceRev1,
       "cctMIBGroups": cctMIBGroups,
       "cctGeneralGroup": cctGeneralGroup,
       "cctActiveGroup": cctActiveGroup,
       "cctHistoryGroup": cctHistoryGroup,
       "cctNotificationConfigGroup": cctNotificationConfigGroup,
       "cctNotificationGroup": cctNotificationGroup,
       "cctActiveGroupRev1": cctActiveGroupRev1,
       "cctHistoryGroupRev1": cctHistoryGroupRev1}
)
