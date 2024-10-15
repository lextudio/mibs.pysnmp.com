# SNMP MIB module (HUAWEI-RSVPTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-RSVPTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:49 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(BitRate,
 BurstSize,
 MessageSize,
 QosService,
 SessionType) = mibBuilder.importSymbols(
    "INTEGRATED-SERVICES-MIB",
    "BitRate",
    "BurstSize",
    "MessageSize",
    "QosService",
    "SessionType")

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
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

hwRsvpTe = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148)
)
hwRsvpTe.setRevisions(
        ("2014-10-25 17:36",
         "2014-06-16 14:55",
         "2013-08-28 17:55")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwRsvpTeObjects_ObjectIdentity = ObjectIdentity
hwRsvpTeObjects = _HwRsvpTeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1)
)
_HwRsvpTeSessionTable_Object = MibTable
hwRsvpTeSessionTable = _HwRsvpTeSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 1)
)
if mibBuilder.loadTexts:
    hwRsvpTeSessionTable.setStatus("current")
_HwRsvpTeSessionEntry_Object = MibTableRow
hwRsvpTeSessionEntry = _HwRsvpTeSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 1, 1)
)
hwRsvpTeSessionEntry.setIndexNames(
    (0, "HUAWEI-RSVPTE-MIB", "hwRsvpTeSessionNumber"),
)
if mibBuilder.loadTexts:
    hwRsvpTeSessionEntry.setStatus("current")
_HwRsvpTeSessionNumber_Type = Gauge32
_HwRsvpTeSessionNumber_Object = MibTableColumn
hwRsvpTeSessionNumber = _HwRsvpTeSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 1, 1, 1),
    _HwRsvpTeSessionNumber_Type()
)
hwRsvpTeSessionNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRsvpTeSessionNumber.setStatus("current")
_HwRsvpTeSessionType_Type = SessionType
_HwRsvpTeSessionType_Object = MibTableColumn
hwRsvpTeSessionType = _HwRsvpTeSessionType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 1, 1, 2),
    _HwRsvpTeSessionType_Type()
)
hwRsvpTeSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSessionType.setStatus("current")


class _HwRsvpTeSessionDestAddr_Type(OctetString):
    """Custom type hwRsvpTeSessionDestAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwRsvpTeSessionDestAddr_Type.__name__ = "OctetString"
_HwRsvpTeSessionDestAddr_Object = MibTableColumn
hwRsvpTeSessionDestAddr = _HwRsvpTeSessionDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 1, 1, 3),
    _HwRsvpTeSessionDestAddr_Type()
)
hwRsvpTeSessionDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSessionDestAddr.setStatus("current")
_HwRsvpTeSessionDestAddrLength_Type = Integer32
_HwRsvpTeSessionDestAddrLength_Object = MibTableColumn
hwRsvpTeSessionDestAddrLength = _HwRsvpTeSessionDestAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 1, 1, 4),
    _HwRsvpTeSessionDestAddrLength_Type()
)
hwRsvpTeSessionDestAddrLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSessionDestAddrLength.setStatus("current")
_HwRsvpTeSessionSenders_Type = Gauge32
_HwRsvpTeSessionSenders_Object = MibTableColumn
hwRsvpTeSessionSenders = _HwRsvpTeSessionSenders_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 1, 1, 5),
    _HwRsvpTeSessionSenders_Type()
)
hwRsvpTeSessionSenders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSessionSenders.setStatus("current")
_HwRsvpTeSessionReceivers_Type = Gauge32
_HwRsvpTeSessionReceivers_Object = MibTableColumn
hwRsvpTeSessionReceivers = _HwRsvpTeSessionReceivers_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 1, 1, 6),
    _HwRsvpTeSessionReceivers_Type()
)
hwRsvpTeSessionReceivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSessionReceivers.setStatus("current")
_HwRsvpTeSessionRequests_Type = Gauge32
_HwRsvpTeSessionRequests_Object = MibTableColumn
hwRsvpTeSessionRequests = _HwRsvpTeSessionRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 1, 1, 7),
    _HwRsvpTeSessionRequests_Type()
)
hwRsvpTeSessionRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSessionRequests.setStatus("current")
_HwRsvpTeSessionTunnelId_Type = Integer32
_HwRsvpTeSessionTunnelId_Object = MibTableColumn
hwRsvpTeSessionTunnelId = _HwRsvpTeSessionTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 1, 1, 8),
    _HwRsvpTeSessionTunnelId_Type()
)
hwRsvpTeSessionTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSessionTunnelId.setStatus("current")
_HwRsvpTeSessionTunnelExtId_Type = IpAddress
_HwRsvpTeSessionTunnelExtId_Object = MibTableColumn
hwRsvpTeSessionTunnelExtId = _HwRsvpTeSessionTunnelExtId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 1, 1, 9),
    _HwRsvpTeSessionTunnelExtId_Type()
)
hwRsvpTeSessionTunnelExtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSessionTunnelExtId.setStatus("current")
_HwRsvpTeSessionLspsNumber_Type = Gauge32
_HwRsvpTeSessionLspsNumber_Object = MibTableColumn
hwRsvpTeSessionLspsNumber = _HwRsvpTeSessionLspsNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 1, 1, 10),
    _HwRsvpTeSessionLspsNumber_Type()
)
hwRsvpTeSessionLspsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSessionLspsNumber.setStatus("current")


class _HwRsvpTeSessionStyle_Type(Integer32):
    """Custom type hwRsvpTeSessionStyle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("ff", 10),
          ("se", 18),
          ("wf", 17))
    )


_HwRsvpTeSessionStyle_Type.__name__ = "Integer32"
_HwRsvpTeSessionStyle_Object = MibTableColumn
hwRsvpTeSessionStyle = _HwRsvpTeSessionStyle_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 1, 1, 11),
    _HwRsvpTeSessionStyle_Type()
)
hwRsvpTeSessionStyle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSessionStyle.setStatus("current")
_HwRsvpTeSenderTable_Object = MibTable
hwRsvpTeSenderTable = _HwRsvpTeSenderTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2)
)
if mibBuilder.loadTexts:
    hwRsvpTeSenderTable.setStatus("current")
_HwRsvpTeSenderEntry_Object = MibTableRow
hwRsvpTeSenderEntry = _HwRsvpTeSenderEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1)
)
hwRsvpTeSenderEntry.setIndexNames(
    (0, "HUAWEI-RSVPTE-MIB", "hwRsvpTeSessionNumber"),
    (0, "HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderNumber"),
)
if mibBuilder.loadTexts:
    hwRsvpTeSenderEntry.setStatus("current")
_HwRsvpTeSenderNumber_Type = Gauge32
_HwRsvpTeSenderNumber_Object = MibTableColumn
hwRsvpTeSenderNumber = _HwRsvpTeSenderNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 1),
    _HwRsvpTeSenderNumber_Type()
)
hwRsvpTeSenderNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRsvpTeSenderNumber.setStatus("current")
_HwRsvpTeSenderType_Type = SessionType
_HwRsvpTeSenderType_Object = MibTableColumn
hwRsvpTeSenderType = _HwRsvpTeSenderType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 2),
    _HwRsvpTeSenderType_Type()
)
hwRsvpTeSenderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderType.setStatus("current")


class _HwRsvpTeSenderDestAddr_Type(OctetString):
    """Custom type hwRsvpTeSenderDestAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwRsvpTeSenderDestAddr_Type.__name__ = "OctetString"
_HwRsvpTeSenderDestAddr_Object = MibTableColumn
hwRsvpTeSenderDestAddr = _HwRsvpTeSenderDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 3),
    _HwRsvpTeSenderDestAddr_Type()
)
hwRsvpTeSenderDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderDestAddr.setStatus("current")


class _HwRsvpTeSenderAddr_Type(OctetString):
    """Custom type hwRsvpTeSenderAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwRsvpTeSenderAddr_Type.__name__ = "OctetString"
_HwRsvpTeSenderAddr_Object = MibTableColumn
hwRsvpTeSenderAddr = _HwRsvpTeSenderAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 4),
    _HwRsvpTeSenderAddr_Type()
)
hwRsvpTeSenderAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAddr.setStatus("current")
_HwRsvpTeSenderDestAddrLength_Type = Integer32
_HwRsvpTeSenderDestAddrLength_Object = MibTableColumn
hwRsvpTeSenderDestAddrLength = _HwRsvpTeSenderDestAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 5),
    _HwRsvpTeSenderDestAddrLength_Type()
)
hwRsvpTeSenderDestAddrLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderDestAddrLength.setStatus("current")
_HwRsvpTeSenderAddrLength_Type = Integer32
_HwRsvpTeSenderAddrLength_Object = MibTableColumn
hwRsvpTeSenderAddrLength = _HwRsvpTeSenderAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 6),
    _HwRsvpTeSenderAddrLength_Type()
)
hwRsvpTeSenderAddrLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAddrLength.setStatus("current")


class _HwRsvpTeSenderHopAddr_Type(OctetString):
    """Custom type hwRsvpTeSenderHopAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwRsvpTeSenderHopAddr_Type.__name__ = "OctetString"
_HwRsvpTeSenderHopAddr_Object = MibTableColumn
hwRsvpTeSenderHopAddr = _HwRsvpTeSenderHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 7),
    _HwRsvpTeSenderHopAddr_Type()
)
hwRsvpTeSenderHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderHopAddr.setStatus("current")
_HwRsvpTeSenderHopLih_Type = Integer32
_HwRsvpTeSenderHopLih_Object = MibTableColumn
hwRsvpTeSenderHopLih = _HwRsvpTeSenderHopLih_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 8),
    _HwRsvpTeSenderHopLih_Type()
)
hwRsvpTeSenderHopLih.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderHopLih.setStatus("current")
_HwRsvpTeSenderInterface_Type = Integer32
_HwRsvpTeSenderInterface_Object = MibTableColumn
hwRsvpTeSenderInterface = _HwRsvpTeSenderInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 9),
    _HwRsvpTeSenderInterface_Type()
)
hwRsvpTeSenderInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderInterface.setStatus("current")
_HwRsvpTeSenderTSpecRate_Type = BitRate
_HwRsvpTeSenderTSpecRate_Object = MibTableColumn
hwRsvpTeSenderTSpecRate = _HwRsvpTeSenderTSpecRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 10),
    _HwRsvpTeSenderTSpecRate_Type()
)
hwRsvpTeSenderTSpecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderTSpecRate.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeSenderTSpecRate.setUnits("bits per second")
_HwRsvpTeSenderTSpecPeakRate_Type = BitRate
_HwRsvpTeSenderTSpecPeakRate_Object = MibTableColumn
hwRsvpTeSenderTSpecPeakRate = _HwRsvpTeSenderTSpecPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 11),
    _HwRsvpTeSenderTSpecPeakRate_Type()
)
hwRsvpTeSenderTSpecPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderTSpecPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeSenderTSpecPeakRate.setUnits("bits per second")
_HwRsvpTeSenderTSpecBurst_Type = BurstSize
_HwRsvpTeSenderTSpecBurst_Object = MibTableColumn
hwRsvpTeSenderTSpecBurst = _HwRsvpTeSenderTSpecBurst_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 12),
    _HwRsvpTeSenderTSpecBurst_Type()
)
hwRsvpTeSenderTSpecBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderTSpecBurst.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeSenderTSpecBurst.setUnits("bytes")
_HwRsvpTeSenderTSpecMinTu_Type = MessageSize
_HwRsvpTeSenderTSpecMinTu_Object = MibTableColumn
hwRsvpTeSenderTSpecMinTu = _HwRsvpTeSenderTSpecMinTu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 13),
    _HwRsvpTeSenderTSpecMinTu_Type()
)
hwRsvpTeSenderTSpecMinTu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderTSpecMinTu.setStatus("current")
_HwRsvpTeSenderTSpecMaxTu_Type = MessageSize
_HwRsvpTeSenderTSpecMaxTu_Object = MibTableColumn
hwRsvpTeSenderTSpecMaxTu = _HwRsvpTeSenderTSpecMaxTu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 14),
    _HwRsvpTeSenderTSpecMaxTu_Type()
)
hwRsvpTeSenderTSpecMaxTu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderTSpecMaxTu.setStatus("current")
_HwRsvpTeSenderInterval_Type = Integer32
_HwRsvpTeSenderInterval_Object = MibTableColumn
hwRsvpTeSenderInterval = _HwRsvpTeSenderInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 15),
    _HwRsvpTeSenderInterval_Type()
)
hwRsvpTeSenderInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderInterval.setStatus("current")
_HwRsvpTeSenderRsvpHop_Type = TruthValue
_HwRsvpTeSenderRsvpHop_Object = MibTableColumn
hwRsvpTeSenderRsvpHop = _HwRsvpTeSenderRsvpHop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 16),
    _HwRsvpTeSenderRsvpHop_Type()
)
hwRsvpTeSenderRsvpHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderRsvpHop.setStatus("current")


class _HwRsvpTeSenderPolicy_Type(OctetString):
    """Custom type hwRsvpTeSenderPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65532),
    )


_HwRsvpTeSenderPolicy_Type.__name__ = "OctetString"
_HwRsvpTeSenderPolicy_Object = MibTableColumn
hwRsvpTeSenderPolicy = _HwRsvpTeSenderPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 17),
    _HwRsvpTeSenderPolicy_Type()
)
hwRsvpTeSenderPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderPolicy.setStatus("current")
_HwRsvpTeSenderAdspecBreak_Type = TruthValue
_HwRsvpTeSenderAdspecBreak_Object = MibTableColumn
hwRsvpTeSenderAdspecBreak = _HwRsvpTeSenderAdspecBreak_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 18),
    _HwRsvpTeSenderAdspecBreak_Type()
)
hwRsvpTeSenderAdspecBreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecBreak.setStatus("current")
_HwRsvpTeSenderAdspecHopCount_Type = Integer32
_HwRsvpTeSenderAdspecHopCount_Object = MibTableColumn
hwRsvpTeSenderAdspecHopCount = _HwRsvpTeSenderAdspecHopCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 19),
    _HwRsvpTeSenderAdspecHopCount_Type()
)
hwRsvpTeSenderAdspecHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecHopCount.setStatus("current")
_HwRsvpTeSenderAdspecPathBw_Type = BitRate
_HwRsvpTeSenderAdspecPathBw_Object = MibTableColumn
hwRsvpTeSenderAdspecPathBw = _HwRsvpTeSenderAdspecPathBw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 20),
    _HwRsvpTeSenderAdspecPathBw_Type()
)
hwRsvpTeSenderAdspecPathBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecPathBw.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecPathBw.setUnits("bits per second")
_HwRsvpTeSenderAdspecMinLatency_Type = Integer32
_HwRsvpTeSenderAdspecMinLatency_Object = MibTableColumn
hwRsvpTeSenderAdspecMinLatency = _HwRsvpTeSenderAdspecMinLatency_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 21),
    _HwRsvpTeSenderAdspecMinLatency_Type()
)
hwRsvpTeSenderAdspecMinLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecMinLatency.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecMinLatency.setUnits("microseconds")
_HwRsvpTeSenderAdspecMtu_Type = Integer32
_HwRsvpTeSenderAdspecMtu_Object = MibTableColumn
hwRsvpTeSenderAdspecMtu = _HwRsvpTeSenderAdspecMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 22),
    _HwRsvpTeSenderAdspecMtu_Type()
)
hwRsvpTeSenderAdspecMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecMtu.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecMtu.setUnits("bytes")
_HwRsvpTeSenderAdspecGuaranteedSvc_Type = TruthValue
_HwRsvpTeSenderAdspecGuaranteedSvc_Object = MibTableColumn
hwRsvpTeSenderAdspecGuaranteedSvc = _HwRsvpTeSenderAdspecGuaranteedSvc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 23),
    _HwRsvpTeSenderAdspecGuaranteedSvc_Type()
)
hwRsvpTeSenderAdspecGuaranteedSvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecGuaranteedSvc.setStatus("current")
_HwRsvpTeSenderAdspecGuaranteedBreak_Type = TruthValue
_HwRsvpTeSenderAdspecGuaranteedBreak_Object = MibTableColumn
hwRsvpTeSenderAdspecGuaranteedBreak = _HwRsvpTeSenderAdspecGuaranteedBreak_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 24),
    _HwRsvpTeSenderAdspecGuaranteedBreak_Type()
)
hwRsvpTeSenderAdspecGuaranteedBreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecGuaranteedBreak.setStatus("current")
_HwRsvpTeSenderAdspecGuaranteedCtot_Type = Integer32
_HwRsvpTeSenderAdspecGuaranteedCtot_Object = MibTableColumn
hwRsvpTeSenderAdspecGuaranteedCtot = _HwRsvpTeSenderAdspecGuaranteedCtot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 25),
    _HwRsvpTeSenderAdspecGuaranteedCtot_Type()
)
hwRsvpTeSenderAdspecGuaranteedCtot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecGuaranteedCtot.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecGuaranteedCtot.setUnits("bytes")
_HwRsvpTeSenderAdspecGuaranteedDtot_Type = Integer32
_HwRsvpTeSenderAdspecGuaranteedDtot_Object = MibTableColumn
hwRsvpTeSenderAdspecGuaranteedDtot = _HwRsvpTeSenderAdspecGuaranteedDtot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 26),
    _HwRsvpTeSenderAdspecGuaranteedDtot_Type()
)
hwRsvpTeSenderAdspecGuaranteedDtot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecGuaranteedDtot.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecGuaranteedDtot.setUnits("microseconds")
_HwRsvpTeSenderAdspecGuaranteedCsum_Type = Integer32
_HwRsvpTeSenderAdspecGuaranteedCsum_Object = MibTableColumn
hwRsvpTeSenderAdspecGuaranteedCsum = _HwRsvpTeSenderAdspecGuaranteedCsum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 27),
    _HwRsvpTeSenderAdspecGuaranteedCsum_Type()
)
hwRsvpTeSenderAdspecGuaranteedCsum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecGuaranteedCsum.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecGuaranteedCsum.setUnits("bytes")
_HwRsvpTeSenderAdspecGuaranteedDsum_Type = Integer32
_HwRsvpTeSenderAdspecGuaranteedDsum_Object = MibTableColumn
hwRsvpTeSenderAdspecGuaranteedDsum = _HwRsvpTeSenderAdspecGuaranteedDsum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 28),
    _HwRsvpTeSenderAdspecGuaranteedDsum_Type()
)
hwRsvpTeSenderAdspecGuaranteedDsum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecGuaranteedDsum.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecGuaranteedDsum.setUnits("microseconds")
_HwRsvpTeSenderAdspecGuaranteedHopCount_Type = Integer32
_HwRsvpTeSenderAdspecGuaranteedHopCount_Object = MibTableColumn
hwRsvpTeSenderAdspecGuaranteedHopCount = _HwRsvpTeSenderAdspecGuaranteedHopCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 29),
    _HwRsvpTeSenderAdspecGuaranteedHopCount_Type()
)
hwRsvpTeSenderAdspecGuaranteedHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecGuaranteedHopCount.setStatus("current")
_HwRsvpTeSenderAdspecGuaranteedPathBw_Type = BitRate
_HwRsvpTeSenderAdspecGuaranteedPathBw_Object = MibTableColumn
hwRsvpTeSenderAdspecGuaranteedPathBw = _HwRsvpTeSenderAdspecGuaranteedPathBw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 30),
    _HwRsvpTeSenderAdspecGuaranteedPathBw_Type()
)
hwRsvpTeSenderAdspecGuaranteedPathBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecGuaranteedPathBw.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecGuaranteedPathBw.setUnits("bits per second")
_HwRsvpTeSenderAdspecGuaranteedMinLatency_Type = Integer32
_HwRsvpTeSenderAdspecGuaranteedMinLatency_Object = MibTableColumn
hwRsvpTeSenderAdspecGuaranteedMinLatency = _HwRsvpTeSenderAdspecGuaranteedMinLatency_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 31),
    _HwRsvpTeSenderAdspecGuaranteedMinLatency_Type()
)
hwRsvpTeSenderAdspecGuaranteedMinLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecGuaranteedMinLatency.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecGuaranteedMinLatency.setUnits("microseconds")
_HwRsvpTeSenderAdspecGuaranteedMtu_Type = Integer32
_HwRsvpTeSenderAdspecGuaranteedMtu_Object = MibTableColumn
hwRsvpTeSenderAdspecGuaranteedMtu = _HwRsvpTeSenderAdspecGuaranteedMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 32),
    _HwRsvpTeSenderAdspecGuaranteedMtu_Type()
)
hwRsvpTeSenderAdspecGuaranteedMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecGuaranteedMtu.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecGuaranteedMtu.setUnits("bytes")
_HwRsvpTeSenderAdspecCtrlLoadSvc_Type = TruthValue
_HwRsvpTeSenderAdspecCtrlLoadSvc_Object = MibTableColumn
hwRsvpTeSenderAdspecCtrlLoadSvc = _HwRsvpTeSenderAdspecCtrlLoadSvc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 33),
    _HwRsvpTeSenderAdspecCtrlLoadSvc_Type()
)
hwRsvpTeSenderAdspecCtrlLoadSvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecCtrlLoadSvc.setStatus("current")
_HwRsvpTeSenderAdspecCtrlLoadBreak_Type = TruthValue
_HwRsvpTeSenderAdspecCtrlLoadBreak_Object = MibTableColumn
hwRsvpTeSenderAdspecCtrlLoadBreak = _HwRsvpTeSenderAdspecCtrlLoadBreak_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 34),
    _HwRsvpTeSenderAdspecCtrlLoadBreak_Type()
)
hwRsvpTeSenderAdspecCtrlLoadBreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecCtrlLoadBreak.setStatus("current")
_HwRsvpTeSenderAdspecCtrlLoadHopCount_Type = Integer32
_HwRsvpTeSenderAdspecCtrlLoadHopCount_Object = MibTableColumn
hwRsvpTeSenderAdspecCtrlLoadHopCount = _HwRsvpTeSenderAdspecCtrlLoadHopCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 35),
    _HwRsvpTeSenderAdspecCtrlLoadHopCount_Type()
)
hwRsvpTeSenderAdspecCtrlLoadHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecCtrlLoadHopCount.setStatus("current")
_HwRsvpTeSenderAdspecCtrlLoadPathBw_Type = BitRate
_HwRsvpTeSenderAdspecCtrlLoadPathBw_Object = MibTableColumn
hwRsvpTeSenderAdspecCtrlLoadPathBw = _HwRsvpTeSenderAdspecCtrlLoadPathBw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 36),
    _HwRsvpTeSenderAdspecCtrlLoadPathBw_Type()
)
hwRsvpTeSenderAdspecCtrlLoadPathBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecCtrlLoadPathBw.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecCtrlLoadPathBw.setUnits("bits per second")
_HwRsvpTeSenderAdspecCtrlLoadMinLatency_Type = Integer32
_HwRsvpTeSenderAdspecCtrlLoadMinLatency_Object = MibTableColumn
hwRsvpTeSenderAdspecCtrlLoadMinLatency = _HwRsvpTeSenderAdspecCtrlLoadMinLatency_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 37),
    _HwRsvpTeSenderAdspecCtrlLoadMinLatency_Type()
)
hwRsvpTeSenderAdspecCtrlLoadMinLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecCtrlLoadMinLatency.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecCtrlLoadMinLatency.setUnits("microseconds")
_HwRsvpTeSenderAdspecCtrlLoadMtu_Type = Integer32
_HwRsvpTeSenderAdspecCtrlLoadMtu_Object = MibTableColumn
hwRsvpTeSenderAdspecCtrlLoadMtu = _HwRsvpTeSenderAdspecCtrlLoadMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 38),
    _HwRsvpTeSenderAdspecCtrlLoadMtu_Type()
)
hwRsvpTeSenderAdspecCtrlLoadMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecCtrlLoadMtu.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeSenderAdspecCtrlLoadMtu.setUnits("bytes")
_HwRsvpTeSenderTtl_Type = Integer32
_HwRsvpTeSenderTtl_Object = MibTableColumn
hwRsvpTeSenderTtl = _HwRsvpTeSenderTtl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 39),
    _HwRsvpTeSenderTtl_Type()
)
hwRsvpTeSenderTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderTtl.setStatus("current")
_HwRsvpTeLspId_Type = Integer32
_HwRsvpTeLspId_Object = MibTableColumn
hwRsvpTeLspId = _HwRsvpTeLspId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 40),
    _HwRsvpTeLspId_Type()
)
hwRsvpTeLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeLspId.setStatus("current")
_HwRsvpTeSenderMsgIdSndFlag_Type = Integer32
_HwRsvpTeSenderMsgIdSndFlag_Object = MibTableColumn
hwRsvpTeSenderMsgIdSndFlag = _HwRsvpTeSenderMsgIdSndFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 41),
    _HwRsvpTeSenderMsgIdSndFlag_Type()
)
hwRsvpTeSenderMsgIdSndFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderMsgIdSndFlag.setStatus("current")
_HwRsvpTeSenderMsgIdSndEpoch_Type = Gauge32
_HwRsvpTeSenderMsgIdSndEpoch_Object = MibTableColumn
hwRsvpTeSenderMsgIdSndEpoch = _HwRsvpTeSenderMsgIdSndEpoch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 42),
    _HwRsvpTeSenderMsgIdSndEpoch_Type()
)
hwRsvpTeSenderMsgIdSndEpoch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderMsgIdSndEpoch.setStatus("current")
_HwRsvpTeSenderMsgIdSndNumber_Type = Gauge32
_HwRsvpTeSenderMsgIdSndNumber_Object = MibTableColumn
hwRsvpTeSenderMsgIdSndNumber = _HwRsvpTeSenderMsgIdSndNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 43),
    _HwRsvpTeSenderMsgIdSndNumber_Type()
)
hwRsvpTeSenderMsgIdSndNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderMsgIdSndNumber.setStatus("current")
_HwRsvpTeSenderMsgIdRcvFlag_Type = Integer32
_HwRsvpTeSenderMsgIdRcvFlag_Object = MibTableColumn
hwRsvpTeSenderMsgIdRcvFlag = _HwRsvpTeSenderMsgIdRcvFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 44),
    _HwRsvpTeSenderMsgIdRcvFlag_Type()
)
hwRsvpTeSenderMsgIdRcvFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderMsgIdRcvFlag.setStatus("current")
_HwRsvpTeSenderMsgIdRcvEpoch_Type = Gauge32
_HwRsvpTeSenderMsgIdRcvEpoch_Object = MibTableColumn
hwRsvpTeSenderMsgIdRcvEpoch = _HwRsvpTeSenderMsgIdRcvEpoch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 45),
    _HwRsvpTeSenderMsgIdRcvEpoch_Type()
)
hwRsvpTeSenderMsgIdRcvEpoch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderMsgIdRcvEpoch.setStatus("current")
_HwRsvpTeSenderMsgIdRcvNumber_Type = Gauge32
_HwRsvpTeSenderMsgIdRcvNumber_Object = MibTableColumn
hwRsvpTeSenderMsgIdRcvNumber = _HwRsvpTeSenderMsgIdRcvNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 46),
    _HwRsvpTeSenderMsgIdRcvNumber_Type()
)
hwRsvpTeSenderMsgIdRcvNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderMsgIdRcvNumber.setStatus("current")
_HwRsvpTeSenderClassType_Type = Integer32
_HwRsvpTeSenderClassType_Object = MibTableColumn
hwRsvpTeSenderClassType = _HwRsvpTeSenderClassType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 47),
    _HwRsvpTeSenderClassType_Type()
)
hwRsvpTeSenderClassType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderClassType.setStatus("current")


class _HwRsvpTeSenderLabelRequestCtype_Type(Integer32):
    """Custom type hwRsvpTeSenderLabelRequestCtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("withAtmLabelRange", 2),
          ("withFrameRelayLabelRange", 3),
          ("withoutLabelRange", 1))
    )


_HwRsvpTeSenderLabelRequestCtype_Type.__name__ = "Integer32"
_HwRsvpTeSenderLabelRequestCtype_Object = MibTableColumn
hwRsvpTeSenderLabelRequestCtype = _HwRsvpTeSenderLabelRequestCtype_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 48),
    _HwRsvpTeSenderLabelRequestCtype_Type()
)
hwRsvpTeSenderLabelRequestCtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderLabelRequestCtype.setStatus("current")
_HwRsvpTeSenderLabelRequestL3pid_Type = Integer32
_HwRsvpTeSenderLabelRequestL3pid_Object = MibTableColumn
hwRsvpTeSenderLabelRequestL3pid = _HwRsvpTeSenderLabelRequestL3pid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 49),
    _HwRsvpTeSenderLabelRequestL3pid_Type()
)
hwRsvpTeSenderLabelRequestL3pid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderLabelRequestL3pid.setStatus("current")
_HwRsvpTeSenderLabelRequestAtmMinVpi_Type = Integer32
_HwRsvpTeSenderLabelRequestAtmMinVpi_Object = MibTableColumn
hwRsvpTeSenderLabelRequestAtmMinVpi = _HwRsvpTeSenderLabelRequestAtmMinVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 50),
    _HwRsvpTeSenderLabelRequestAtmMinVpi_Type()
)
hwRsvpTeSenderLabelRequestAtmMinVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderLabelRequestAtmMinVpi.setStatus("current")
_HwRsvpTeSenderLabelRequestAtmMinVci_Type = Integer32
_HwRsvpTeSenderLabelRequestAtmMinVci_Object = MibTableColumn
hwRsvpTeSenderLabelRequestAtmMinVci = _HwRsvpTeSenderLabelRequestAtmMinVci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 51),
    _HwRsvpTeSenderLabelRequestAtmMinVci_Type()
)
hwRsvpTeSenderLabelRequestAtmMinVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderLabelRequestAtmMinVci.setStatus("current")
_HwRsvpTeSenderLabelRequestAtmMaxVpi_Type = Integer32
_HwRsvpTeSenderLabelRequestAtmMaxVpi_Object = MibTableColumn
hwRsvpTeSenderLabelRequestAtmMaxVpi = _HwRsvpTeSenderLabelRequestAtmMaxVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 52),
    _HwRsvpTeSenderLabelRequestAtmMaxVpi_Type()
)
hwRsvpTeSenderLabelRequestAtmMaxVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderLabelRequestAtmMaxVpi.setStatus("current")
_HwRsvpTeSenderLabelRequestAtmMaxVci_Type = Integer32
_HwRsvpTeSenderLabelRequestAtmMaxVci_Object = MibTableColumn
hwRsvpTeSenderLabelRequestAtmMaxVci = _HwRsvpTeSenderLabelRequestAtmMaxVci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 53),
    _HwRsvpTeSenderLabelRequestAtmMaxVci_Type()
)
hwRsvpTeSenderLabelRequestAtmMaxVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderLabelRequestAtmMaxVci.setStatus("current")
_HwRsvpTeSenderLabelRequestFrMinDlci_Type = Integer32
_HwRsvpTeSenderLabelRequestFrMinDlci_Object = MibTableColumn
hwRsvpTeSenderLabelRequestFrMinDlci = _HwRsvpTeSenderLabelRequestFrMinDlci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 54),
    _HwRsvpTeSenderLabelRequestFrMinDlci_Type()
)
hwRsvpTeSenderLabelRequestFrMinDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderLabelRequestFrMinDlci.setStatus("current")
_HwRsvpTeSenderLabelRequestFrMaxDlci_Type = Integer32
_HwRsvpTeSenderLabelRequestFrMaxDlci_Object = MibTableColumn
hwRsvpTeSenderLabelRequestFrMaxDlci = _HwRsvpTeSenderLabelRequestFrMaxDlci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 55),
    _HwRsvpTeSenderLabelRequestFrMaxDlci_Type()
)
hwRsvpTeSenderLabelRequestFrMaxDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderLabelRequestFrMaxDlci.setStatus("current")


class _HwRsvpTeSenderSessionAttrType_Type(Integer32):
    """Custom type hwRsvpTeSenderSessionAttrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              7)
        )
    )
    namedValues = NamedValues(
        *(("withRa", 1),
          ("withoutRa", 7))
    )


_HwRsvpTeSenderSessionAttrType_Type.__name__ = "Integer32"
_HwRsvpTeSenderSessionAttrType_Object = MibTableColumn
hwRsvpTeSenderSessionAttrType = _HwRsvpTeSenderSessionAttrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 56),
    _HwRsvpTeSenderSessionAttrType_Type()
)
hwRsvpTeSenderSessionAttrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderSessionAttrType.setStatus("current")
_HwRsvpTeSenderSessionAttrSetupPrio_Type = Integer32
_HwRsvpTeSenderSessionAttrSetupPrio_Object = MibTableColumn
hwRsvpTeSenderSessionAttrSetupPrio = _HwRsvpTeSenderSessionAttrSetupPrio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 57),
    _HwRsvpTeSenderSessionAttrSetupPrio_Type()
)
hwRsvpTeSenderSessionAttrSetupPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderSessionAttrSetupPrio.setStatus("current")
_HwRsvpTeSenderSessionAttrHoldPrio_Type = Integer32
_HwRsvpTeSenderSessionAttrHoldPrio_Object = MibTableColumn
hwRsvpTeSenderSessionAttrHoldPrio = _HwRsvpTeSenderSessionAttrHoldPrio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 58),
    _HwRsvpTeSenderSessionAttrHoldPrio_Type()
)
hwRsvpTeSenderSessionAttrHoldPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderSessionAttrHoldPrio.setStatus("current")
_HwRsvpTeSenderSessionAttrFlag_Type = Integer32
_HwRsvpTeSenderSessionAttrFlag_Object = MibTableColumn
hwRsvpTeSenderSessionAttrFlag = _HwRsvpTeSenderSessionAttrFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 59),
    _HwRsvpTeSenderSessionAttrFlag_Type()
)
hwRsvpTeSenderSessionAttrFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderSessionAttrFlag.setStatus("current")


class _HwRsvpTeSenderSessionAttrName_Type(OctetString):
    """Custom type hwRsvpTeSenderSessionAttrName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwRsvpTeSenderSessionAttrName_Type.__name__ = "OctetString"
_HwRsvpTeSenderSessionAttrName_Object = MibTableColumn
hwRsvpTeSenderSessionAttrName = _HwRsvpTeSenderSessionAttrName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 60),
    _HwRsvpTeSenderSessionAttrName_Type()
)
hwRsvpTeSenderSessionAttrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderSessionAttrName.setStatus("current")
_HwRsvpTeSenderSessionAttrExcludeAny_Type = Gauge32
_HwRsvpTeSenderSessionAttrExcludeAny_Object = MibTableColumn
hwRsvpTeSenderSessionAttrExcludeAny = _HwRsvpTeSenderSessionAttrExcludeAny_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 61),
    _HwRsvpTeSenderSessionAttrExcludeAny_Type()
)
hwRsvpTeSenderSessionAttrExcludeAny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderSessionAttrExcludeAny.setStatus("current")
_HwRsvpTeSenderSessionAttrIncludeAny_Type = Gauge32
_HwRsvpTeSenderSessionAttrIncludeAny_Object = MibTableColumn
hwRsvpTeSenderSessionAttrIncludeAny = _HwRsvpTeSenderSessionAttrIncludeAny_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 62),
    _HwRsvpTeSenderSessionAttrIncludeAny_Type()
)
hwRsvpTeSenderSessionAttrIncludeAny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderSessionAttrIncludeAny.setStatus("current")
_HwRsvpTeSenderSessionAttrIncludeAll_Type = Gauge32
_HwRsvpTeSenderSessionAttrIncludeAll_Object = MibTableColumn
hwRsvpTeSenderSessionAttrIncludeAll = _HwRsvpTeSenderSessionAttrIncludeAll_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 63),
    _HwRsvpTeSenderSessionAttrIncludeAll_Type()
)
hwRsvpTeSenderSessionAttrIncludeAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderSessionAttrIncludeAll.setStatus("current")
_HwRsvpTeSenderFrrSetupPrio_Type = Integer32
_HwRsvpTeSenderFrrSetupPrio_Object = MibTableColumn
hwRsvpTeSenderFrrSetupPrio = _HwRsvpTeSenderFrrSetupPrio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 64),
    _HwRsvpTeSenderFrrSetupPrio_Type()
)
hwRsvpTeSenderFrrSetupPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderFrrSetupPrio.setStatus("current")
_HwRsvpTeSenderFrrHoldPrio_Type = Integer32
_HwRsvpTeSenderFrrHoldPrio_Object = MibTableColumn
hwRsvpTeSenderFrrHoldPrio = _HwRsvpTeSenderFrrHoldPrio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 65),
    _HwRsvpTeSenderFrrHoldPrio_Type()
)
hwRsvpTeSenderFrrHoldPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderFrrHoldPrio.setStatus("current")
_HwRsvpTeSenderFrrHopLimit_Type = Integer32
_HwRsvpTeSenderFrrHopLimit_Object = MibTableColumn
hwRsvpTeSenderFrrHopLimit = _HwRsvpTeSenderFrrHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 66),
    _HwRsvpTeSenderFrrHopLimit_Type()
)
hwRsvpTeSenderFrrHopLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderFrrHopLimit.setStatus("current")


class _HwRsvpTeSenderFrrFlag_Type(Integer32):
    """Custom type hwRsvpTeSenderFrrFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("facilityDesired", 2),
          ("noBackupDesired", 3),
          ("oneToOneDesired", 1))
    )


_HwRsvpTeSenderFrrFlag_Type.__name__ = "Integer32"
_HwRsvpTeSenderFrrFlag_Object = MibTableColumn
hwRsvpTeSenderFrrFlag = _HwRsvpTeSenderFrrFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 67),
    _HwRsvpTeSenderFrrFlag_Type()
)
hwRsvpTeSenderFrrFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderFrrFlag.setStatus("current")
_HwRsvpTeSenderFrrBandwidth_Type = BitRate
_HwRsvpTeSenderFrrBandwidth_Object = MibTableColumn
hwRsvpTeSenderFrrBandwidth = _HwRsvpTeSenderFrrBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 68),
    _HwRsvpTeSenderFrrBandwidth_Type()
)
hwRsvpTeSenderFrrBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderFrrBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeSenderFrrBandwidth.setUnits("bits per second")
_HwRsvpTeSenderFrrExcludeAny_Type = Gauge32
_HwRsvpTeSenderFrrExcludeAny_Object = MibTableColumn
hwRsvpTeSenderFrrExcludeAny = _HwRsvpTeSenderFrrExcludeAny_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 69),
    _HwRsvpTeSenderFrrExcludeAny_Type()
)
hwRsvpTeSenderFrrExcludeAny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderFrrExcludeAny.setStatus("current")
_HwRsvpTeSenderFrrIncludeAny_Type = Gauge32
_HwRsvpTeSenderFrrIncludeAny_Object = MibTableColumn
hwRsvpTeSenderFrrIncludeAny = _HwRsvpTeSenderFrrIncludeAny_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 70),
    _HwRsvpTeSenderFrrIncludeAny_Type()
)
hwRsvpTeSenderFrrIncludeAny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderFrrIncludeAny.setStatus("current")
_HwRsvpTeSenderFrrIncludeAll_Type = Gauge32
_HwRsvpTeSenderFrrIncludeAll_Object = MibTableColumn
hwRsvpTeSenderFrrIncludeAll = _HwRsvpTeSenderFrrIncludeAll_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 71),
    _HwRsvpTeSenderFrrIncludeAll_Type()
)
hwRsvpTeSenderFrrIncludeAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderFrrIncludeAll.setStatus("current")


class _HwRsvpTeSenderFrrInuseFlag_Type(Integer32):
    """Custom type hwRsvpTeSenderFrrInuseFlag based on Integer32"""
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
        *(("mpInUse", 3),
          ("normal", 1),
          ("plrAndMpInUse", 4),
          ("plrInUse", 2),
          ("underProtection", 5))
    )


_HwRsvpTeSenderFrrInuseFlag_Type.__name__ = "Integer32"
_HwRsvpTeSenderFrrInuseFlag_Object = MibTableColumn
hwRsvpTeSenderFrrInuseFlag = _HwRsvpTeSenderFrrInuseFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 72),
    _HwRsvpTeSenderFrrInuseFlag_Type()
)
hwRsvpTeSenderFrrInuseFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderFrrInuseFlag.setStatus("current")
_HwRsvpTeSenderDiffServPsc_Type = Integer32
_HwRsvpTeSenderDiffServPsc_Object = MibTableColumn
hwRsvpTeSenderDiffServPsc = _HwRsvpTeSenderDiffServPsc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 2, 1, 73),
    _HwRsvpTeSenderDiffServPsc_Type()
)
hwRsvpTeSenderDiffServPsc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeSenderDiffServPsc.setStatus("current")
_HwRsvpTeResvTable_Object = MibTable
hwRsvpTeResvTable = _HwRsvpTeResvTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 3)
)
if mibBuilder.loadTexts:
    hwRsvpTeResvTable.setStatus("current")
_HwRsvpTeResvEntry_Object = MibTableRow
hwRsvpTeResvEntry = _HwRsvpTeResvEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 3, 1)
)
hwRsvpTeResvEntry.setIndexNames(
    (0, "HUAWEI-RSVPTE-MIB", "hwRsvpTeSessionNumber"),
    (0, "HUAWEI-RSVPTE-MIB", "hwRsvpTeResvNumber"),
)
if mibBuilder.loadTexts:
    hwRsvpTeResvEntry.setStatus("current")
_HwRsvpTeResvNumber_Type = Gauge32
_HwRsvpTeResvNumber_Object = MibTableColumn
hwRsvpTeResvNumber = _HwRsvpTeResvNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 3, 1, 1),
    _HwRsvpTeResvNumber_Type()
)
hwRsvpTeResvNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRsvpTeResvNumber.setStatus("current")
_HwRsvpTeResvType_Type = SessionType
_HwRsvpTeResvType_Object = MibTableColumn
hwRsvpTeResvType = _HwRsvpTeResvType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 3, 1, 2),
    _HwRsvpTeResvType_Type()
)
hwRsvpTeResvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvType.setStatus("current")


class _HwRsvpTeResvDestAddr_Type(OctetString):
    """Custom type hwRsvpTeResvDestAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwRsvpTeResvDestAddr_Type.__name__ = "OctetString"
_HwRsvpTeResvDestAddr_Object = MibTableColumn
hwRsvpTeResvDestAddr = _HwRsvpTeResvDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 3, 1, 3),
    _HwRsvpTeResvDestAddr_Type()
)
hwRsvpTeResvDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvDestAddr.setStatus("current")


class _HwRsvpTeResvSenderAddr_Type(OctetString):
    """Custom type hwRsvpTeResvSenderAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwRsvpTeResvSenderAddr_Type.__name__ = "OctetString"
_HwRsvpTeResvSenderAddr_Object = MibTableColumn
hwRsvpTeResvSenderAddr = _HwRsvpTeResvSenderAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 3, 1, 4),
    _HwRsvpTeResvSenderAddr_Type()
)
hwRsvpTeResvSenderAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvSenderAddr.setStatus("current")
_HwRsvpTeResvDestAddrLength_Type = Integer32
_HwRsvpTeResvDestAddrLength_Object = MibTableColumn
hwRsvpTeResvDestAddrLength = _HwRsvpTeResvDestAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 3, 1, 5),
    _HwRsvpTeResvDestAddrLength_Type()
)
hwRsvpTeResvDestAddrLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvDestAddrLength.setStatus("current")
_HwRsvpTeResvSenderAddrLength_Type = Integer32
_HwRsvpTeResvSenderAddrLength_Object = MibTableColumn
hwRsvpTeResvSenderAddrLength = _HwRsvpTeResvSenderAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 3, 1, 6),
    _HwRsvpTeResvSenderAddrLength_Type()
)
hwRsvpTeResvSenderAddrLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvSenderAddrLength.setStatus("current")


class _HwRsvpTeResvHopAddr_Type(OctetString):
    """Custom type hwRsvpTeResvHopAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwRsvpTeResvHopAddr_Type.__name__ = "OctetString"
_HwRsvpTeResvHopAddr_Object = MibTableColumn
hwRsvpTeResvHopAddr = _HwRsvpTeResvHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 3, 1, 7),
    _HwRsvpTeResvHopAddr_Type()
)
hwRsvpTeResvHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvHopAddr.setStatus("current")
_HwRsvpTeResvHopLih_Type = Integer32
_HwRsvpTeResvHopLih_Object = MibTableColumn
hwRsvpTeResvHopLih = _HwRsvpTeResvHopLih_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 3, 1, 8),
    _HwRsvpTeResvHopLih_Type()
)
hwRsvpTeResvHopLih.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvHopLih.setStatus("current")
_HwRsvpTeResvInterface_Type = Integer32
_HwRsvpTeResvInterface_Object = MibTableColumn
hwRsvpTeResvInterface = _HwRsvpTeResvInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 3, 1, 9),
    _HwRsvpTeResvInterface_Type()
)
hwRsvpTeResvInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvInterface.setStatus("current")
_HwRsvpTeResvService_Type = QosService
_HwRsvpTeResvService_Object = MibTableColumn
hwRsvpTeResvService = _HwRsvpTeResvService_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 3, 1, 10),
    _HwRsvpTeResvService_Type()
)
hwRsvpTeResvService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvService.setStatus("current")
_HwRsvpTeResvTSpecRate_Type = BitRate
_HwRsvpTeResvTSpecRate_Object = MibTableColumn
hwRsvpTeResvTSpecRate = _HwRsvpTeResvTSpecRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 3, 1, 11),
    _HwRsvpTeResvTSpecRate_Type()
)
hwRsvpTeResvTSpecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvTSpecRate.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeResvTSpecRate.setUnits("bits per second")
_HwRsvpTeResvTSpecPeakRate_Type = BitRate
_HwRsvpTeResvTSpecPeakRate_Object = MibTableColumn
hwRsvpTeResvTSpecPeakRate = _HwRsvpTeResvTSpecPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 3, 1, 12),
    _HwRsvpTeResvTSpecPeakRate_Type()
)
hwRsvpTeResvTSpecPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvTSpecPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeResvTSpecPeakRate.setUnits("bits per second")
_HwRsvpTeResvTSpecBurst_Type = BurstSize
_HwRsvpTeResvTSpecBurst_Object = MibTableColumn
hwRsvpTeResvTSpecBurst = _HwRsvpTeResvTSpecBurst_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 3, 1, 13),
    _HwRsvpTeResvTSpecBurst_Type()
)
hwRsvpTeResvTSpecBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvTSpecBurst.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeResvTSpecBurst.setUnits("bytes")
_HwRsvpTeResvTSpecMinTu_Type = MessageSize
_HwRsvpTeResvTSpecMinTu_Object = MibTableColumn
hwRsvpTeResvTSpecMinTu = _HwRsvpTeResvTSpecMinTu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 3, 1, 14),
    _HwRsvpTeResvTSpecMinTu_Type()
)
hwRsvpTeResvTSpecMinTu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvTSpecMinTu.setStatus("current")
_HwRsvpTeResvTSpecMaxTu_Type = MessageSize
_HwRsvpTeResvTSpecMaxTu_Object = MibTableColumn
hwRsvpTeResvTSpecMaxTu = _HwRsvpTeResvTSpecMaxTu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 3, 1, 15),
    _HwRsvpTeResvTSpecMaxTu_Type()
)
hwRsvpTeResvTSpecMaxTu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvTSpecMaxTu.setStatus("current")
_HwRsvpTeResvRSpecRate_Type = BitRate
_HwRsvpTeResvRSpecRate_Object = MibTableColumn
hwRsvpTeResvRSpecRate = _HwRsvpTeResvRSpecRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 3, 1, 16),
    _HwRsvpTeResvRSpecRate_Type()
)
hwRsvpTeResvRSpecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvRSpecRate.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeResvRSpecRate.setUnits("bits per second")
_HwRsvpTeResvRSpecSlack_Type = Integer32
_HwRsvpTeResvRSpecSlack_Object = MibTableColumn
hwRsvpTeResvRSpecSlack = _HwRsvpTeResvRSpecSlack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 3, 1, 17),
    _HwRsvpTeResvRSpecSlack_Type()
)
hwRsvpTeResvRSpecSlack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvRSpecSlack.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeResvRSpecSlack.setUnits("microseconds")
_HwRsvpTeResvInterval_Type = Integer32
_HwRsvpTeResvInterval_Object = MibTableColumn
hwRsvpTeResvInterval = _HwRsvpTeResvInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 3, 1, 18),
    _HwRsvpTeResvInterval_Type()
)
hwRsvpTeResvInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvInterval.setStatus("current")


class _HwRsvpTeResvScope_Type(OctetString):
    """Custom type hwRsvpTeResvScope based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_HwRsvpTeResvScope_Type.__name__ = "OctetString"
_HwRsvpTeResvScope_Object = MibTableColumn
hwRsvpTeResvScope = _HwRsvpTeResvScope_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 3, 1, 19),
    _HwRsvpTeResvScope_Type()
)
hwRsvpTeResvScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvScope.setStatus("current")
_HwRsvpTeResvShared_Type = TruthValue
_HwRsvpTeResvShared_Object = MibTableColumn
hwRsvpTeResvShared = _HwRsvpTeResvShared_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 3, 1, 20),
    _HwRsvpTeResvShared_Type()
)
hwRsvpTeResvShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvShared.setStatus("current")
_HwRsvpTeResvExplicit_Type = TruthValue
_HwRsvpTeResvExplicit_Object = MibTableColumn
hwRsvpTeResvExplicit = _HwRsvpTeResvExplicit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 3, 1, 21),
    _HwRsvpTeResvExplicit_Type()
)
hwRsvpTeResvExplicit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvExplicit.setStatus("current")
_HwRsvpTeResvRsvpHop_Type = TruthValue
_HwRsvpTeResvRsvpHop_Object = MibTableColumn
hwRsvpTeResvRsvpHop = _HwRsvpTeResvRsvpHop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 3, 1, 22),
    _HwRsvpTeResvRsvpHop_Type()
)
hwRsvpTeResvRsvpHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvRsvpHop.setStatus("current")


class _HwRsvpTeResvPolicy_Type(OctetString):
    """Custom type hwRsvpTeResvPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_HwRsvpTeResvPolicy_Type.__name__ = "OctetString"
_HwRsvpTeResvPolicy_Object = MibTableColumn
hwRsvpTeResvPolicy = _HwRsvpTeResvPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 3, 1, 23),
    _HwRsvpTeResvPolicy_Type()
)
hwRsvpTeResvPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvPolicy.setStatus("current")
_HwRsvpTeResvTtl_Type = Integer32
_HwRsvpTeResvTtl_Object = MibTableColumn
hwRsvpTeResvTtl = _HwRsvpTeResvTtl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 3, 1, 24),
    _HwRsvpTeResvTtl_Type()
)
hwRsvpTeResvTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvTtl.setStatus("current")


class _HwRsvpTeResvConfirm_Type(OctetString):
    """Custom type hwRsvpTeResvConfirm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwRsvpTeResvConfirm_Type.__name__ = "OctetString"
_HwRsvpTeResvConfirm_Object = MibTableColumn
hwRsvpTeResvConfirm = _HwRsvpTeResvConfirm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 3, 1, 25),
    _HwRsvpTeResvConfirm_Type()
)
hwRsvpTeResvConfirm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvConfirm.setStatus("current")
_HwRsvpTeResvFwdTable_Object = MibTable
hwRsvpTeResvFwdTable = _HwRsvpTeResvFwdTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4)
)
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdTable.setStatus("current")
_HwRsvpTeResvFwdEntry_Object = MibTableRow
hwRsvpTeResvFwdEntry = _HwRsvpTeResvFwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4, 1)
)
hwRsvpTeResvFwdEntry.setIndexNames(
    (0, "HUAWEI-RSVPTE-MIB", "hwRsvpTeSessionNumber"),
    (0, "HUAWEI-RSVPTE-MIB", "hwRsvpTeResvFwdNumber"),
)
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdEntry.setStatus("current")
_HwRsvpTeResvFwdNumber_Type = Gauge32
_HwRsvpTeResvFwdNumber_Object = MibTableColumn
hwRsvpTeResvFwdNumber = _HwRsvpTeResvFwdNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4, 1, 1),
    _HwRsvpTeResvFwdNumber_Type()
)
hwRsvpTeResvFwdNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdNumber.setStatus("current")
_HwRsvpTeResvFwdType_Type = SessionType
_HwRsvpTeResvFwdType_Object = MibTableColumn
hwRsvpTeResvFwdType = _HwRsvpTeResvFwdType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4, 1, 2),
    _HwRsvpTeResvFwdType_Type()
)
hwRsvpTeResvFwdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdType.setStatus("current")


class _HwRsvpTeResvFwdDestAddr_Type(OctetString):
    """Custom type hwRsvpTeResvFwdDestAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwRsvpTeResvFwdDestAddr_Type.__name__ = "OctetString"
_HwRsvpTeResvFwdDestAddr_Object = MibTableColumn
hwRsvpTeResvFwdDestAddr = _HwRsvpTeResvFwdDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4, 1, 3),
    _HwRsvpTeResvFwdDestAddr_Type()
)
hwRsvpTeResvFwdDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdDestAddr.setStatus("current")


class _HwRsvpTeResvFwdSenderAddr_Type(OctetString):
    """Custom type hwRsvpTeResvFwdSenderAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwRsvpTeResvFwdSenderAddr_Type.__name__ = "OctetString"
_HwRsvpTeResvFwdSenderAddr_Object = MibTableColumn
hwRsvpTeResvFwdSenderAddr = _HwRsvpTeResvFwdSenderAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4, 1, 4),
    _HwRsvpTeResvFwdSenderAddr_Type()
)
hwRsvpTeResvFwdSenderAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdSenderAddr.setStatus("current")
_HwRsvpTeResvFwdDestAddrLength_Type = Integer32
_HwRsvpTeResvFwdDestAddrLength_Object = MibTableColumn
hwRsvpTeResvFwdDestAddrLength = _HwRsvpTeResvFwdDestAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4, 1, 5),
    _HwRsvpTeResvFwdDestAddrLength_Type()
)
hwRsvpTeResvFwdDestAddrLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdDestAddrLength.setStatus("current")
_HwRsvpTeResvFwdSenderAddrLength_Type = Integer32
_HwRsvpTeResvFwdSenderAddrLength_Object = MibTableColumn
hwRsvpTeResvFwdSenderAddrLength = _HwRsvpTeResvFwdSenderAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4, 1, 6),
    _HwRsvpTeResvFwdSenderAddrLength_Type()
)
hwRsvpTeResvFwdSenderAddrLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdSenderAddrLength.setStatus("current")


class _HwRsvpTeResvFwdHopAddr_Type(OctetString):
    """Custom type hwRsvpTeResvFwdHopAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwRsvpTeResvFwdHopAddr_Type.__name__ = "OctetString"
_HwRsvpTeResvFwdHopAddr_Object = MibTableColumn
hwRsvpTeResvFwdHopAddr = _HwRsvpTeResvFwdHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4, 1, 7),
    _HwRsvpTeResvFwdHopAddr_Type()
)
hwRsvpTeResvFwdHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdHopAddr.setStatus("current")
_HwRsvpTeResvFwdHopLih_Type = Integer32
_HwRsvpTeResvFwdHopLih_Object = MibTableColumn
hwRsvpTeResvFwdHopLih = _HwRsvpTeResvFwdHopLih_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4, 1, 8),
    _HwRsvpTeResvFwdHopLih_Type()
)
hwRsvpTeResvFwdHopLih.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdHopLih.setStatus("current")
_HwRsvpTeResvFwdInterface_Type = Integer32
_HwRsvpTeResvFwdInterface_Object = MibTableColumn
hwRsvpTeResvFwdInterface = _HwRsvpTeResvFwdInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4, 1, 9),
    _HwRsvpTeResvFwdInterface_Type()
)
hwRsvpTeResvFwdInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdInterface.setStatus("current")
_HwRsvpTeResvFwdService_Type = QosService
_HwRsvpTeResvFwdService_Object = MibTableColumn
hwRsvpTeResvFwdService = _HwRsvpTeResvFwdService_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4, 1, 10),
    _HwRsvpTeResvFwdService_Type()
)
hwRsvpTeResvFwdService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdService.setStatus("current")
_HwRsvpTeResvFwdTSpecRate_Type = BitRate
_HwRsvpTeResvFwdTSpecRate_Object = MibTableColumn
hwRsvpTeResvFwdTSpecRate = _HwRsvpTeResvFwdTSpecRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4, 1, 11),
    _HwRsvpTeResvFwdTSpecRate_Type()
)
hwRsvpTeResvFwdTSpecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdTSpecRate.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdTSpecRate.setUnits("bits per second")
_HwRsvpTeResvFwdTSpecPeakRate_Type = BitRate
_HwRsvpTeResvFwdTSpecPeakRate_Object = MibTableColumn
hwRsvpTeResvFwdTSpecPeakRate = _HwRsvpTeResvFwdTSpecPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4, 1, 12),
    _HwRsvpTeResvFwdTSpecPeakRate_Type()
)
hwRsvpTeResvFwdTSpecPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdTSpecPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdTSpecPeakRate.setUnits("bits per second")
_HwRsvpTeResvFwdTSpecBurst_Type = BurstSize
_HwRsvpTeResvFwdTSpecBurst_Object = MibTableColumn
hwRsvpTeResvFwdTSpecBurst = _HwRsvpTeResvFwdTSpecBurst_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4, 1, 13),
    _HwRsvpTeResvFwdTSpecBurst_Type()
)
hwRsvpTeResvFwdTSpecBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdTSpecBurst.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdTSpecBurst.setUnits("bytes")
_HwRsvpTeResvFwdTSpecMinTu_Type = MessageSize
_HwRsvpTeResvFwdTSpecMinTu_Object = MibTableColumn
hwRsvpTeResvFwdTSpecMinTu = _HwRsvpTeResvFwdTSpecMinTu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4, 1, 14),
    _HwRsvpTeResvFwdTSpecMinTu_Type()
)
hwRsvpTeResvFwdTSpecMinTu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdTSpecMinTu.setStatus("current")
_HwRsvpTeResvFwdTSpecMaxTu_Type = MessageSize
_HwRsvpTeResvFwdTSpecMaxTu_Object = MibTableColumn
hwRsvpTeResvFwdTSpecMaxTu = _HwRsvpTeResvFwdTSpecMaxTu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4, 1, 15),
    _HwRsvpTeResvFwdTSpecMaxTu_Type()
)
hwRsvpTeResvFwdTSpecMaxTu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdTSpecMaxTu.setStatus("current")
_HwRsvpTeResvFwdRSpecRate_Type = BitRate
_HwRsvpTeResvFwdRSpecRate_Object = MibTableColumn
hwRsvpTeResvFwdRSpecRate = _HwRsvpTeResvFwdRSpecRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4, 1, 16),
    _HwRsvpTeResvFwdRSpecRate_Type()
)
hwRsvpTeResvFwdRSpecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdRSpecRate.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdRSpecRate.setUnits("bytes per second")
_HwRsvpTeResvFwdRSpecSlack_Type = Integer32
_HwRsvpTeResvFwdRSpecSlack_Object = MibTableColumn
hwRsvpTeResvFwdRSpecSlack = _HwRsvpTeResvFwdRSpecSlack_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4, 1, 17),
    _HwRsvpTeResvFwdRSpecSlack_Type()
)
hwRsvpTeResvFwdRSpecSlack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdRSpecSlack.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdRSpecSlack.setUnits("microseconds")
_HwRsvpTeResvFwdInterval_Type = Integer32
_HwRsvpTeResvFwdInterval_Object = MibTableColumn
hwRsvpTeResvFwdInterval = _HwRsvpTeResvFwdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4, 1, 18),
    _HwRsvpTeResvFwdInterval_Type()
)
hwRsvpTeResvFwdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdInterval.setStatus("current")


class _HwRsvpTeResvFwdScope_Type(OctetString):
    """Custom type hwRsvpTeResvFwdScope based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_HwRsvpTeResvFwdScope_Type.__name__ = "OctetString"
_HwRsvpTeResvFwdScope_Object = MibTableColumn
hwRsvpTeResvFwdScope = _HwRsvpTeResvFwdScope_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4, 1, 19),
    _HwRsvpTeResvFwdScope_Type()
)
hwRsvpTeResvFwdScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdScope.setStatus("current")
_HwRsvpTeResvFwdShared_Type = TruthValue
_HwRsvpTeResvFwdShared_Object = MibTableColumn
hwRsvpTeResvFwdShared = _HwRsvpTeResvFwdShared_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4, 1, 20),
    _HwRsvpTeResvFwdShared_Type()
)
hwRsvpTeResvFwdShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdShared.setStatus("current")
_HwRsvpTeResvFwdExplicit_Type = TruthValue
_HwRsvpTeResvFwdExplicit_Object = MibTableColumn
hwRsvpTeResvFwdExplicit = _HwRsvpTeResvFwdExplicit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4, 1, 21),
    _HwRsvpTeResvFwdExplicit_Type()
)
hwRsvpTeResvFwdExplicit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdExplicit.setStatus("current")
_HwRsvpTeResvFwdRsvpHop_Type = TruthValue
_HwRsvpTeResvFwdRsvpHop_Object = MibTableColumn
hwRsvpTeResvFwdRsvpHop = _HwRsvpTeResvFwdRsvpHop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4, 1, 22),
    _HwRsvpTeResvFwdRsvpHop_Type()
)
hwRsvpTeResvFwdRsvpHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdRsvpHop.setStatus("current")


class _HwRsvpTeResvFwdPolicy_Type(OctetString):
    """Custom type hwRsvpTeResvFwdPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_HwRsvpTeResvFwdPolicy_Type.__name__ = "OctetString"
_HwRsvpTeResvFwdPolicy_Object = MibTableColumn
hwRsvpTeResvFwdPolicy = _HwRsvpTeResvFwdPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4, 1, 23),
    _HwRsvpTeResvFwdPolicy_Type()
)
hwRsvpTeResvFwdPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdPolicy.setStatus("current")
_HwRsvpTeResvFwdTtl_Type = Integer32
_HwRsvpTeResvFwdTtl_Object = MibTableColumn
hwRsvpTeResvFwdTtl = _HwRsvpTeResvFwdTtl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4, 1, 24),
    _HwRsvpTeResvFwdTtl_Type()
)
hwRsvpTeResvFwdTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdTtl.setStatus("current")
_HwRsvpTeResvFwdMsgIdFlag_Type = Integer32
_HwRsvpTeResvFwdMsgIdFlag_Object = MibTableColumn
hwRsvpTeResvFwdMsgIdFlag = _HwRsvpTeResvFwdMsgIdFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4, 1, 25),
    _HwRsvpTeResvFwdMsgIdFlag_Type()
)
hwRsvpTeResvFwdMsgIdFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdMsgIdFlag.setStatus("current")
_HwRsvpTeResvFwdMsgIdEpoch_Type = Gauge32
_HwRsvpTeResvFwdMsgIdEpoch_Object = MibTableColumn
hwRsvpTeResvFwdMsgIdEpoch = _HwRsvpTeResvFwdMsgIdEpoch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4, 1, 26),
    _HwRsvpTeResvFwdMsgIdEpoch_Type()
)
hwRsvpTeResvFwdMsgIdEpoch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdMsgIdEpoch.setStatus("current")
_HwRsvpTeResvFwdMsgIdNumber_Type = Gauge32
_HwRsvpTeResvFwdMsgIdNumber_Object = MibTableColumn
hwRsvpTeResvFwdMsgIdNumber = _HwRsvpTeResvFwdMsgIdNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 4, 1, 27),
    _HwRsvpTeResvFwdMsgIdNumber_Type()
)
hwRsvpTeResvFwdMsgIdNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdMsgIdNumber.setStatus("current")
_HwRsvpTeIfTable_Object = MibTable
hwRsvpTeIfTable = _HwRsvpTeIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 5)
)
if mibBuilder.loadTexts:
    hwRsvpTeIfTable.setStatus("current")
_HwRsvpTeIfEntry_Object = MibTableRow
hwRsvpTeIfEntry = _HwRsvpTeIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 5, 1)
)
hwRsvpTeIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hwRsvpTeIfEntry.setStatus("current")
_HwRsvpTeIfUdpNbrs_Type = Gauge32
_HwRsvpTeIfUdpNbrs_Object = MibTableColumn
hwRsvpTeIfUdpNbrs = _HwRsvpTeIfUdpNbrs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 5, 1, 1),
    _HwRsvpTeIfUdpNbrs_Type()
)
hwRsvpTeIfUdpNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeIfUdpNbrs.setStatus("current")
_HwRsvpTeIfIpNbrs_Type = Gauge32
_HwRsvpTeIfIpNbrs_Object = MibTableColumn
hwRsvpTeIfIpNbrs = _HwRsvpTeIfIpNbrs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 5, 1, 2),
    _HwRsvpTeIfIpNbrs_Type()
)
hwRsvpTeIfIpNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeIfIpNbrs.setStatus("current")
_HwRsvpTeIfNbrs_Type = Gauge32
_HwRsvpTeIfNbrs_Object = MibTableColumn
hwRsvpTeIfNbrs = _HwRsvpTeIfNbrs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 5, 1, 3),
    _HwRsvpTeIfNbrs_Type()
)
hwRsvpTeIfNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeIfNbrs.setStatus("current")
_HwRsvpTeIfRefreshBlockadeMultiple_Type = Integer32
_HwRsvpTeIfRefreshBlockadeMultiple_Object = MibTableColumn
hwRsvpTeIfRefreshBlockadeMultiple = _HwRsvpTeIfRefreshBlockadeMultiple_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 5, 1, 4),
    _HwRsvpTeIfRefreshBlockadeMultiple_Type()
)
hwRsvpTeIfRefreshBlockadeMultiple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeIfRefreshBlockadeMultiple.setStatus("current")
_HwRsvpTeIfRefreshMultiple_Type = Integer32
_HwRsvpTeIfRefreshMultiple_Object = MibTableColumn
hwRsvpTeIfRefreshMultiple = _HwRsvpTeIfRefreshMultiple_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 5, 1, 5),
    _HwRsvpTeIfRefreshMultiple_Type()
)
hwRsvpTeIfRefreshMultiple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeIfRefreshMultiple.setStatus("current")
_HwRsvpTeIfTtl_Type = Integer32
_HwRsvpTeIfTtl_Object = MibTableColumn
hwRsvpTeIfTtl = _HwRsvpTeIfTtl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 5, 1, 6),
    _HwRsvpTeIfTtl_Type()
)
hwRsvpTeIfTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeIfTtl.setStatus("current")
_HwRsvpTeIfRefreshInterval_Type = TimeInterval
_HwRsvpTeIfRefreshInterval_Object = MibTableColumn
hwRsvpTeIfRefreshInterval = _HwRsvpTeIfRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 5, 1, 7),
    _HwRsvpTeIfRefreshInterval_Type()
)
hwRsvpTeIfRefreshInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeIfRefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeIfRefreshInterval.setUnits("milliseconds")
_HwRsvpTeIfRouteDelay_Type = TimeInterval
_HwRsvpTeIfRouteDelay_Object = MibTableColumn
hwRsvpTeIfRouteDelay = _HwRsvpTeIfRouteDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 5, 1, 8),
    _HwRsvpTeIfRouteDelay_Type()
)
hwRsvpTeIfRouteDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeIfRouteDelay.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeIfRouteDelay.setUnits("hundredths of a second")
_HwRsvpTeIfEnabled_Type = TruthValue
_HwRsvpTeIfEnabled_Object = MibTableColumn
hwRsvpTeIfEnabled = _HwRsvpTeIfEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 5, 1, 9),
    _HwRsvpTeIfEnabled_Type()
)
hwRsvpTeIfEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeIfEnabled.setStatus("current")
_HwRsvpTeIfUdpRequired_Type = TruthValue
_HwRsvpTeIfUdpRequired_Object = MibTableColumn
hwRsvpTeIfUdpRequired = _HwRsvpTeIfUdpRequired_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 5, 1, 10),
    _HwRsvpTeIfUdpRequired_Type()
)
hwRsvpTeIfUdpRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeIfUdpRequired.setStatus("current")
_HwRsvpTeIfStatus_Type = RowStatus
_HwRsvpTeIfStatus_Object = MibTableColumn
hwRsvpTeIfStatus = _HwRsvpTeIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 5, 1, 11),
    _HwRsvpTeIfStatus_Type()
)
hwRsvpTeIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRsvpTeIfStatus.setStatus("current")
_HwRsvpTeIfHelloEnabled_Type = TruthValue
_HwRsvpTeIfHelloEnabled_Object = MibTableColumn
hwRsvpTeIfHelloEnabled = _HwRsvpTeIfHelloEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 5, 1, 12),
    _HwRsvpTeIfHelloEnabled_Type()
)
hwRsvpTeIfHelloEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeIfHelloEnabled.setStatus("current")
_HwRsvpTeIfSrefreshEnabled_Type = TruthValue
_HwRsvpTeIfSrefreshEnabled_Object = MibTableColumn
hwRsvpTeIfSrefreshEnabled = _HwRsvpTeIfSrefreshEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 5, 1, 13),
    _HwRsvpTeIfSrefreshEnabled_Type()
)
hwRsvpTeIfSrefreshEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeIfSrefreshEnabled.setStatus("current")
_HwRsvpTeIfSrefreshInterval_Type = TimeInterval
_HwRsvpTeIfSrefreshInterval_Object = MibTableColumn
hwRsvpTeIfSrefreshInterval = _HwRsvpTeIfSrefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 5, 1, 14),
    _HwRsvpTeIfSrefreshInterval_Type()
)
hwRsvpTeIfSrefreshInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeIfSrefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeIfSrefreshInterval.setUnits("milliseconds")
_HwRsvpTeIfRetranIncDelta_Type = Integer32
_HwRsvpTeIfRetranIncDelta_Object = MibTableColumn
hwRsvpTeIfRetranIncDelta = _HwRsvpTeIfRetranIncDelta_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 5, 1, 15),
    _HwRsvpTeIfRetranIncDelta_Type()
)
hwRsvpTeIfRetranIncDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeIfRetranIncDelta.setStatus("current")
_HwRsvpTeIfRetranInterval_Type = TimeInterval
_HwRsvpTeIfRetranInterval_Object = MibTableColumn
hwRsvpTeIfRetranInterval = _HwRsvpTeIfRetranInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 5, 1, 16),
    _HwRsvpTeIfRetranInterval_Type()
)
hwRsvpTeIfRetranInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeIfRetranInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeIfRetranInterval.setUnits("milliseconds")
_HwRsvpTeIfAuthEnabled_Type = TruthValue
_HwRsvpTeIfAuthEnabled_Object = MibTableColumn
hwRsvpTeIfAuthEnabled = _HwRsvpTeIfAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 5, 1, 17),
    _HwRsvpTeIfAuthEnabled_Type()
)
hwRsvpTeIfAuthEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeIfAuthEnabled.setStatus("current")
_HwRsvpTeIfAuthEncrypted_Type = TruthValue
_HwRsvpTeIfAuthEncrypted_Object = MibTableColumn
hwRsvpTeIfAuthEncrypted = _HwRsvpTeIfAuthEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 5, 1, 18),
    _HwRsvpTeIfAuthEncrypted_Type()
)
hwRsvpTeIfAuthEncrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeIfAuthEncrypted.setStatus("current")
_HwRsvpTeIfAuthHandshake_Type = TruthValue
_HwRsvpTeIfAuthHandshake_Object = MibTableColumn
hwRsvpTeIfAuthHandshake = _HwRsvpTeIfAuthHandshake_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 5, 1, 19),
    _HwRsvpTeIfAuthHandshake_Type()
)
hwRsvpTeIfAuthHandshake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeIfAuthHandshake.setStatus("current")
_HwRsvpTeIfAuthLifeTime_Type = TimeInterval
_HwRsvpTeIfAuthLifeTime_Object = MibTableColumn
hwRsvpTeIfAuthLifeTime = _HwRsvpTeIfAuthLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 5, 1, 20),
    _HwRsvpTeIfAuthLifeTime_Type()
)
hwRsvpTeIfAuthLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeIfAuthLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeIfAuthLifeTime.setUnits("milliseconds")


class _HwRsvpTeIfAuthKey_Type(OctetString):
    """Custom type hwRsvpTeIfAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 392),
    )


_HwRsvpTeIfAuthKey_Type.__name__ = "OctetString"
_HwRsvpTeIfAuthKey_Object = MibTableColumn
hwRsvpTeIfAuthKey = _HwRsvpTeIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 5, 1, 21),
    _HwRsvpTeIfAuthKey_Type()
)
hwRsvpTeIfAuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeIfAuthKey.setStatus("current")
_HwRsvpTeIfWindowSize_Type = Integer32
_HwRsvpTeIfWindowSize_Object = MibTableColumn
hwRsvpTeIfWindowSize = _HwRsvpTeIfWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 5, 1, 22),
    _HwRsvpTeIfWindowSize_Type()
)
hwRsvpTeIfWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeIfWindowSize.setStatus("current")
_HwRsvpTeNbrTable_Object = MibTable
hwRsvpTeNbrTable = _HwRsvpTeNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 6)
)
if mibBuilder.loadTexts:
    hwRsvpTeNbrTable.setStatus("current")
_HwRsvpTeNbrEntry_Object = MibTableRow
hwRsvpTeNbrEntry = _HwRsvpTeNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 6, 1)
)
hwRsvpTeNbrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HUAWEI-RSVPTE-MIB", "hwRsvpTeNbrAddress"),
)
if mibBuilder.loadTexts:
    hwRsvpTeNbrEntry.setStatus("current")


class _HwRsvpTeNbrAddress_Type(OctetString):
    """Custom type hwRsvpTeNbrAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwRsvpTeNbrAddress_Type.__name__ = "OctetString"
_HwRsvpTeNbrAddress_Object = MibTableColumn
hwRsvpTeNbrAddress = _HwRsvpTeNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 6, 1, 1),
    _HwRsvpTeNbrAddress_Type()
)
hwRsvpTeNbrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRsvpTeNbrAddress.setStatus("current")


class _HwRsvpTeNbrProtocol_Type(Integer32):
    """Custom type hwRsvpTeNbrProtocol based on Integer32"""
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
          ("ip", 1),
          ("udp", 2))
    )


_HwRsvpTeNbrProtocol_Type.__name__ = "Integer32"
_HwRsvpTeNbrProtocol_Object = MibTableColumn
hwRsvpTeNbrProtocol = _HwRsvpTeNbrProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 6, 1, 2),
    _HwRsvpTeNbrProtocol_Type()
)
hwRsvpTeNbrProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeNbrProtocol.setStatus("current")
_HwRsvpTeNbrStatus_Type = RowStatus
_HwRsvpTeNbrStatus_Object = MibTableColumn
hwRsvpTeNbrStatus = _HwRsvpTeNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 6, 1, 3),
    _HwRsvpTeNbrStatus_Type()
)
hwRsvpTeNbrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRsvpTeNbrStatus.setStatus("current")
_HwRsvpTeNbrSendersNumber_Type = Gauge32
_HwRsvpTeNbrSendersNumber_Object = MibTableColumn
hwRsvpTeNbrSendersNumber = _HwRsvpTeNbrSendersNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 6, 1, 4),
    _HwRsvpTeNbrSendersNumber_Type()
)
hwRsvpTeNbrSendersNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeNbrSendersNumber.setStatus("current")
_HwRsvpTeNbrReceiversNumber_Type = Gauge32
_HwRsvpTeNbrReceiversNumber_Object = MibTableColumn
hwRsvpTeNbrReceiversNumber = _HwRsvpTeNbrReceiversNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 6, 1, 5),
    _HwRsvpTeNbrReceiversNumber_Type()
)
hwRsvpTeNbrReceiversNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeNbrReceiversNumber.setStatus("current")
_HwRsvpTeNbrHelloEnabled_Type = TruthValue
_HwRsvpTeNbrHelloEnabled_Object = MibTableColumn
hwRsvpTeNbrHelloEnabled = _HwRsvpTeNbrHelloEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 6, 1, 6),
    _HwRsvpTeNbrHelloEnabled_Type()
)
hwRsvpTeNbrHelloEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeNbrHelloEnabled.setStatus("current")
_HwRsvpTeNbrHelloSrcInstance_Type = Gauge32
_HwRsvpTeNbrHelloSrcInstance_Object = MibTableColumn
hwRsvpTeNbrHelloSrcInstance = _HwRsvpTeNbrHelloSrcInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 6, 1, 7),
    _HwRsvpTeNbrHelloSrcInstance_Type()
)
hwRsvpTeNbrHelloSrcInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeNbrHelloSrcInstance.setStatus("current")
_HwRsvpTeNbrHelloDstInstance_Type = Gauge32
_HwRsvpTeNbrHelloDstInstance_Object = MibTableColumn
hwRsvpTeNbrHelloDstInstance = _HwRsvpTeNbrHelloDstInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 6, 1, 8),
    _HwRsvpTeNbrHelloDstInstance_Type()
)
hwRsvpTeNbrHelloDstInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeNbrHelloDstInstance.setStatus("current")
_HwRsvpTeNbrHelloLostCounter_Type = Gauge32
_HwRsvpTeNbrHelloLostCounter_Object = MibTableColumn
hwRsvpTeNbrHelloLostCounter = _HwRsvpTeNbrHelloLostCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 6, 1, 9),
    _HwRsvpTeNbrHelloLostCounter_Type()
)
hwRsvpTeNbrHelloLostCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeNbrHelloLostCounter.setStatus("current")


class _HwRsvpTeNbrHelloType_Type(Integer32):
    """Custom type hwRsvpTeNbrHelloType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ack", 2),
          ("none", 3),
          ("request", 1))
    )


_HwRsvpTeNbrHelloType_Type.__name__ = "Integer32"
_HwRsvpTeNbrHelloType_Object = MibTableColumn
hwRsvpTeNbrHelloType = _HwRsvpTeNbrHelloType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 6, 1, 10),
    _HwRsvpTeNbrHelloType_Type()
)
hwRsvpTeNbrHelloType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeNbrHelloType.setStatus("current")
_HwRsvpTeNbrGrCapability_Type = Integer32
_HwRsvpTeNbrGrCapability_Object = MibTableColumn
hwRsvpTeNbrGrCapability = _HwRsvpTeNbrGrCapability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 6, 1, 11),
    _HwRsvpTeNbrGrCapability_Type()
)
hwRsvpTeNbrGrCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeNbrGrCapability.setStatus("current")
_HwRsvpTeNbrGrRestartTime_Type = TimeStamp
_HwRsvpTeNbrGrRestartTime_Object = MibTableColumn
hwRsvpTeNbrGrRestartTime = _HwRsvpTeNbrGrRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 6, 1, 12),
    _HwRsvpTeNbrGrRestartTime_Type()
)
hwRsvpTeNbrGrRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeNbrGrRestartTime.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeNbrGrRestartTime.setUnits("milliseconds")
_HwRsvpTeNbrGrRecoveryTime_Type = TimeStamp
_HwRsvpTeNbrGrRecoveryTime_Object = MibTableColumn
hwRsvpTeNbrGrRecoveryTime = _HwRsvpTeNbrGrRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 6, 1, 13),
    _HwRsvpTeNbrGrRecoveryTime_Type()
)
hwRsvpTeNbrGrRecoveryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeNbrGrRecoveryTime.setStatus("current")
if mibBuilder.loadTexts:
    hwRsvpTeNbrGrRecoveryTime.setUnits("milliseconds")


class _HwRsvpTeNbrGrStatus_Type(Integer32):
    """Custom type hwRsvpTeNbrGrStatus based on Integer32"""
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
        *(("grEnd", 6),
          ("normal", 1),
          ("recoveryTimerRunning", 5),
          ("restartTimerRunning", 4),
          ("restarting", 3),
          ("supporting", 2))
    )


_HwRsvpTeNbrGrStatus_Type.__name__ = "Integer32"
_HwRsvpTeNbrGrStatus_Object = MibTableColumn
hwRsvpTeNbrGrStatus = _HwRsvpTeNbrGrStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 6, 1, 14),
    _HwRsvpTeNbrGrStatus_Type()
)
hwRsvpTeNbrGrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeNbrGrStatus.setStatus("current")


class _HwRsvpTeNbrAuthKeyId_Type(OctetString):
    """Custom type hwRsvpTeNbrAuthKeyId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(6, 6),
    )


_HwRsvpTeNbrAuthKeyId_Type.__name__ = "OctetString"
_HwRsvpTeNbrAuthKeyId_Object = MibTableColumn
hwRsvpTeNbrAuthKeyId = _HwRsvpTeNbrAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 6, 1, 15),
    _HwRsvpTeNbrAuthKeyId_Type()
)
hwRsvpTeNbrAuthKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeNbrAuthKeyId.setStatus("current")
_HwRsvpTeNbrReductionEnabled_Type = TruthValue
_HwRsvpTeNbrReductionEnabled_Object = MibTableColumn
hwRsvpTeNbrReductionEnabled = _HwRsvpTeNbrReductionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 6, 1, 16),
    _HwRsvpTeNbrReductionEnabled_Type()
)
hwRsvpTeNbrReductionEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeNbrReductionEnabled.setStatus("current")
_HwRsvpTeNbrReliabilityEnabled_Type = TruthValue
_HwRsvpTeNbrReliabilityEnabled_Object = MibTableColumn
hwRsvpTeNbrReliabilityEnabled = _HwRsvpTeNbrReliabilityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 6, 1, 17),
    _HwRsvpTeNbrReliabilityEnabled_Type()
)
hwRsvpTeNbrReliabilityEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeNbrReliabilityEnabled.setStatus("current")
_HwRsvpTeMessageIdTable_Object = MibTable
hwRsvpTeMessageIdTable = _HwRsvpTeMessageIdTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 7)
)
if mibBuilder.loadTexts:
    hwRsvpTeMessageIdTable.setStatus("current")
_HwRsvpTeMessageIdEntry_Object = MibTableRow
hwRsvpTeMessageIdEntry = _HwRsvpTeMessageIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 7, 1)
)
hwRsvpTeMessageIdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HUAWEI-RSVPTE-MIB", "hwRsvpTeNbrAddress"),
    (0, "HUAWEI-RSVPTE-MIB", "hwRsvpTeMessageIdEpoch"),
    (0, "HUAWEI-RSVPTE-MIB", "hwRsvpTeMessageIdNumber"),
)
if mibBuilder.loadTexts:
    hwRsvpTeMessageIdEntry.setStatus("current")
_HwRsvpTeMessageIdEpoch_Type = Gauge32
_HwRsvpTeMessageIdEpoch_Object = MibTableColumn
hwRsvpTeMessageIdEpoch = _HwRsvpTeMessageIdEpoch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 7, 1, 1),
    _HwRsvpTeMessageIdEpoch_Type()
)
hwRsvpTeMessageIdEpoch.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRsvpTeMessageIdEpoch.setStatus("current")
_HwRsvpTeMessageIdNumber_Type = Gauge32
_HwRsvpTeMessageIdNumber_Object = MibTableColumn
hwRsvpTeMessageIdNumber = _HwRsvpTeMessageIdNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 7, 1, 2),
    _HwRsvpTeMessageIdNumber_Type()
)
hwRsvpTeMessageIdNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRsvpTeMessageIdNumber.setStatus("current")


class _HwRsvpTeMessageIdFlag_Type(Integer32):
    """Custom type hwRsvpTeMessageIdFlag based on Integer32"""
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
        *(("resv", 3),
          ("resvFwd", 4),
          ("rtBuff", 5),
          ("senderIncoming", 1),
          ("senderOutgoing", 2))
    )


_HwRsvpTeMessageIdFlag_Type.__name__ = "Integer32"
_HwRsvpTeMessageIdFlag_Object = MibTableColumn
hwRsvpTeMessageIdFlag = _HwRsvpTeMessageIdFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 7, 1, 3),
    _HwRsvpTeMessageIdFlag_Type()
)
hwRsvpTeMessageIdFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeMessageIdFlag.setStatus("current")
_HwRsvpTeFilterSpecTable_Object = MibTable
hwRsvpTeFilterSpecTable = _HwRsvpTeFilterSpecTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 8)
)
if mibBuilder.loadTexts:
    hwRsvpTeFilterSpecTable.setStatus("current")
_HwRsvpTeFilterSpecEntry_Object = MibTableRow
hwRsvpTeFilterSpecEntry = _HwRsvpTeFilterSpecEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 8, 1)
)
hwRsvpTeFilterSpecEntry.setIndexNames(
    (0, "HUAWEI-RSVPTE-MIB", "hwRsvpTeSessionNumber"),
    (0, "HUAWEI-RSVPTE-MIB", "hwRsvpTeResvNumber"),
    (0, "HUAWEI-RSVPTE-MIB", "hwRsvpTeFilterSpecNumber"),
)
if mibBuilder.loadTexts:
    hwRsvpTeFilterSpecEntry.setStatus("current")
_HwRsvpTeFilterSpecNumber_Type = Gauge32
_HwRsvpTeFilterSpecNumber_Object = MibTableColumn
hwRsvpTeFilterSpecNumber = _HwRsvpTeFilterSpecNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 8, 1, 1),
    _HwRsvpTeFilterSpecNumber_Type()
)
hwRsvpTeFilterSpecNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRsvpTeFilterSpecNumber.setStatus("current")
_HwRsvpTeFilterSpecLspId_Type = Integer32
_HwRsvpTeFilterSpecLspId_Object = MibTableColumn
hwRsvpTeFilterSpecLspId = _HwRsvpTeFilterSpecLspId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 8, 1, 2),
    _HwRsvpTeFilterSpecLspId_Type()
)
hwRsvpTeFilterSpecLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeFilterSpecLspId.setStatus("current")
_HwRsvpTeFilterSpecIngressLsrId_Type = OctetString
_HwRsvpTeFilterSpecIngressLsrId_Object = MibTableColumn
hwRsvpTeFilterSpecIngressLsrId = _HwRsvpTeFilterSpecIngressLsrId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 8, 1, 3),
    _HwRsvpTeFilterSpecIngressLsrId_Type()
)
hwRsvpTeFilterSpecIngressLsrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeFilterSpecIngressLsrId.setStatus("current")
_HwRsvpTeFilterSpecLabel_Type = Gauge32
_HwRsvpTeFilterSpecLabel_Object = MibTableColumn
hwRsvpTeFilterSpecLabel = _HwRsvpTeFilterSpecLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 8, 1, 4),
    _HwRsvpTeFilterSpecLabel_Type()
)
hwRsvpTeFilterSpecLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeFilterSpecLabel.setStatus("current")
_HwRsvpTeRroTable_Object = MibTable
hwRsvpTeRroTable = _HwRsvpTeRroTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 9)
)
if mibBuilder.loadTexts:
    hwRsvpTeRroTable.setStatus("current")
_HwRsvpTeRroEntry_Object = MibTableRow
hwRsvpTeRroEntry = _HwRsvpTeRroEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 9, 1)
)
hwRsvpTeRroEntry.setIndexNames(
    (0, "HUAWEI-RSVPTE-MIB", "hwRsvpTeSessionNumber"),
    (0, "HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderNumber"),
    (0, "HUAWEI-RSVPTE-MIB", "hwRsvpTeRroNumber"),
)
if mibBuilder.loadTexts:
    hwRsvpTeRroEntry.setStatus("current")
_HwRsvpTeRroNumber_Type = Gauge32
_HwRsvpTeRroNumber_Object = MibTableColumn
hwRsvpTeRroNumber = _HwRsvpTeRroNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 9, 1, 1),
    _HwRsvpTeRroNumber_Type()
)
hwRsvpTeRroNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRsvpTeRroNumber.setStatus("current")


class _HwRsvpTeRroType_Type(Integer32):
    """Custom type hwRsvpTeRroType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2),
          ("label", 3))
    )


_HwRsvpTeRroType_Type.__name__ = "Integer32"
_HwRsvpTeRroType_Object = MibTableColumn
hwRsvpTeRroType = _HwRsvpTeRroType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 9, 1, 2),
    _HwRsvpTeRroType_Type()
)
hwRsvpTeRroType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeRroType.setStatus("current")
_HwRsvpTeRroIpAddr_Type = OctetString
_HwRsvpTeRroIpAddr_Object = MibTableColumn
hwRsvpTeRroIpAddr = _HwRsvpTeRroIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 9, 1, 3),
    _HwRsvpTeRroIpAddr_Type()
)
hwRsvpTeRroIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeRroIpAddr.setStatus("current")
_HwRsvpTeRroIpPrefixLen_Type = Integer32
_HwRsvpTeRroIpPrefixLen_Object = MibTableColumn
hwRsvpTeRroIpPrefixLen = _HwRsvpTeRroIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 9, 1, 4),
    _HwRsvpTeRroIpPrefixLen_Type()
)
hwRsvpTeRroIpPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeRroIpPrefixLen.setStatus("current")
_HwRsvpTeRroLabel_Type = Gauge32
_HwRsvpTeRroLabel_Object = MibTableColumn
hwRsvpTeRroLabel = _HwRsvpTeRroLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 9, 1, 5),
    _HwRsvpTeRroLabel_Type()
)
hwRsvpTeRroLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeRroLabel.setStatus("current")
_HwRsvpTeRroFlag_Type = Integer32
_HwRsvpTeRroFlag_Object = MibTableColumn
hwRsvpTeRroFlag = _HwRsvpTeRroFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 9, 1, 6),
    _HwRsvpTeRroFlag_Type()
)
hwRsvpTeRroFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeRroFlag.setStatus("current")
_HwRsvpTeEroTable_Object = MibTable
hwRsvpTeEroTable = _HwRsvpTeEroTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 10)
)
if mibBuilder.loadTexts:
    hwRsvpTeEroTable.setStatus("current")
_HwRsvpTeEroEntry_Object = MibTableRow
hwRsvpTeEroEntry = _HwRsvpTeEroEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 10, 1)
)
hwRsvpTeEroEntry.setIndexNames(
    (0, "HUAWEI-RSVPTE-MIB", "hwRsvpTeSessionNumber"),
    (0, "HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderNumber"),
    (0, "HUAWEI-RSVPTE-MIB", "hwRsvpTeEroNumber"),
)
if mibBuilder.loadTexts:
    hwRsvpTeEroEntry.setStatus("current")
_HwRsvpTeEroNumber_Type = Gauge32
_HwRsvpTeEroNumber_Object = MibTableColumn
hwRsvpTeEroNumber = _HwRsvpTeEroNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 10, 1, 1),
    _HwRsvpTeEroNumber_Type()
)
hwRsvpTeEroNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRsvpTeEroNumber.setStatus("current")


class _HwRsvpTeEroType_Type(Integer32):
    """Custom type hwRsvpTeEroType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_HwRsvpTeEroType_Type.__name__ = "Integer32"
_HwRsvpTeEroType_Object = MibTableColumn
hwRsvpTeEroType = _HwRsvpTeEroType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 10, 1, 2),
    _HwRsvpTeEroType_Type()
)
hwRsvpTeEroType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeEroType.setStatus("current")
_HwRsvpTeEroIpAddr_Type = OctetString
_HwRsvpTeEroIpAddr_Object = MibTableColumn
hwRsvpTeEroIpAddr = _HwRsvpTeEroIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 10, 1, 3),
    _HwRsvpTeEroIpAddr_Type()
)
hwRsvpTeEroIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeEroIpAddr.setStatus("current")
_HwRsvpTeEroIpPrefixLen_Type = Integer32
_HwRsvpTeEroIpPrefixLen_Object = MibTableColumn
hwRsvpTeEroIpPrefixLen = _HwRsvpTeEroIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 10, 1, 4),
    _HwRsvpTeEroIpPrefixLen_Type()
)
hwRsvpTeEroIpPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRsvpTeEroIpPrefixLen.setStatus("current")
_HwRsvpTeExtendObjects_ObjectIdentity = ObjectIdentity
hwRsvpTeExtendObjects = _HwRsvpTeExtendObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 11)
)
_HwRsvpTeExtendTrap_ObjectIdentity = ObjectIdentity
hwRsvpTeExtendTrap = _HwRsvpTeExtendTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 12)
)
_HwRsvpTeTrapObjects_ObjectIdentity = ObjectIdentity
hwRsvpTeTrapObjects = _HwRsvpTeTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 12, 1)
)
_HwRsvpTeNbr_Type = IpAddress
_HwRsvpTeNbr_Object = MibScalar
hwRsvpTeNbr = _HwRsvpTeNbr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 12, 1, 1),
    _HwRsvpTeNbr_Type()
)
hwRsvpTeNbr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwRsvpTeNbr.setStatus("current")
_HwRsvpTeIfNbrCurrentCount_Type = Integer32
_HwRsvpTeIfNbrCurrentCount_Object = MibScalar
hwRsvpTeIfNbrCurrentCount = _HwRsvpTeIfNbrCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 12, 1, 2),
    _HwRsvpTeIfNbrCurrentCount_Type()
)
hwRsvpTeIfNbrCurrentCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwRsvpTeIfNbrCurrentCount.setStatus("current")
_HwRsvpTeIfNbrThreshold_Type = Integer32
_HwRsvpTeIfNbrThreshold_Object = MibScalar
hwRsvpTeIfNbrThreshold = _HwRsvpTeIfNbrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 12, 1, 3),
    _HwRsvpTeIfNbrThreshold_Type()
)
hwRsvpTeIfNbrThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwRsvpTeIfNbrThreshold.setStatus("current")
_HwRsvpTeIfNbrTotalCount_Type = Integer32
_HwRsvpTeIfNbrTotalCount_Object = MibScalar
hwRsvpTeIfNbrTotalCount = _HwRsvpTeIfNbrTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 12, 1, 4),
    _HwRsvpTeIfNbrTotalCount_Type()
)
hwRsvpTeIfNbrTotalCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwRsvpTeIfNbrTotalCount.setStatus("current")
_HwRsvpTeIfName_Type = DisplayString
_HwRsvpTeIfName_Object = MibScalar
hwRsvpTeIfName = _HwRsvpTeIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 12, 1, 5),
    _HwRsvpTeIfName_Type()
)
hwRsvpTeIfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwRsvpTeIfName.setStatus("current")
_HwRsvpTeTrap_ObjectIdentity = ObjectIdentity
hwRsvpTeTrap = _HwRsvpTeTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 12, 2)
)
_HwRsvpTeConformance_ObjectIdentity = ObjectIdentity
hwRsvpTeConformance = _HwRsvpTeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 2)
)
_HwRsvpTeGroups_ObjectIdentity = ObjectIdentity
hwRsvpTeGroups = _HwRsvpTeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 2, 1)
)
_HwRsvpTeCompliances_ObjectIdentity = ObjectIdentity
hwRsvpTeCompliances = _HwRsvpTeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 2, 2)
)

# Managed Objects groups

hwRsvpTeSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 2, 1, 1)
)
hwRsvpTeSessionGroup.setObjects(
      *(("HUAWEI-RSVPTE-MIB", "hwRsvpTeSessionType"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSessionDestAddr"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSessionDestAddrLength"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSessionSenders"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSessionReceivers"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSessionRequests"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSessionTunnelId"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSessionTunnelExtId"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSessionLspsNumber"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSessionStyle"))
)
if mibBuilder.loadTexts:
    hwRsvpTeSessionGroup.setStatus("current")

hwRsvpTeSenderGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 2, 1, 2)
)
hwRsvpTeSenderGroup.setObjects(
      *(("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderType"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderDestAddr"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderAddr"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderDestAddrLength"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderAddrLength"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderHopAddr"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderHopLih"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderInterface"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderTSpecRate"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderTSpecPeakRate"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderTSpecBurst"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderTSpecMinTu"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderTSpecMaxTu"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderInterval"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderRsvpHop"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderPolicy"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderAdspecBreak"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderAdspecHopCount"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderAdspecPathBw"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderAdspecMinLatency"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderAdspecMtu"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderAdspecGuaranteedSvc"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderAdspecGuaranteedBreak"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderAdspecGuaranteedCtot"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderAdspecGuaranteedDtot"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderAdspecGuaranteedCsum"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderAdspecGuaranteedDsum"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderAdspecGuaranteedHopCount"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderAdspecGuaranteedPathBw"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderAdspecGuaranteedMinLatency"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderAdspecGuaranteedMtu"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderAdspecCtrlLoadSvc"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderAdspecCtrlLoadBreak"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderAdspecCtrlLoadHopCount"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderAdspecCtrlLoadPathBw"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderAdspecCtrlLoadMinLatency"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderAdspecCtrlLoadMtu"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderTtl"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeLspId"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderMsgIdSndFlag"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderMsgIdSndEpoch"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderMsgIdSndNumber"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderMsgIdRcvFlag"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderMsgIdRcvEpoch"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderMsgIdRcvNumber"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderClassType"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderLabelRequestCtype"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderLabelRequestL3pid"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderLabelRequestAtmMinVpi"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderLabelRequestAtmMinVci"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderLabelRequestAtmMaxVpi"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderLabelRequestAtmMaxVci"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderLabelRequestFrMinDlci"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderLabelRequestFrMaxDlci"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderSessionAttrType"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderSessionAttrSetupPrio"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderSessionAttrHoldPrio"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderSessionAttrFlag"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderSessionAttrName"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderSessionAttrExcludeAny"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderSessionAttrIncludeAny"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderSessionAttrIncludeAll"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderFrrSetupPrio"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderFrrHoldPrio"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderFrrHopLimit"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderFrrFlag"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderFrrBandwidth"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderFrrExcludeAny"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderFrrIncludeAny"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderFrrIncludeAll"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderFrrInuseFlag"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeSenderDiffServPsc"))
)
if mibBuilder.loadTexts:
    hwRsvpTeSenderGroup.setStatus("current")

hwRsvpTeResvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 2, 1, 3)
)
hwRsvpTeResvGroup.setObjects(
      *(("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvType"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvDestAddr"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvSenderAddr"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvDestAddrLength"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvSenderAddrLength"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvHopAddr"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvHopLih"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvInterface"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvService"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvTSpecRate"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvTSpecPeakRate"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvTSpecBurst"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvTSpecMinTu"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvTSpecMaxTu"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvRSpecRate"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvRSpecSlack"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvInterval"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvScope"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvShared"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvExplicit"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvRsvpHop"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvPolicy"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvTtl"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvConfirm"))
)
if mibBuilder.loadTexts:
    hwRsvpTeResvGroup.setStatus("current")

hwRsvpTeResvFwdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 2, 1, 4)
)
hwRsvpTeResvFwdGroup.setObjects(
      *(("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvFwdType"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvFwdDestAddr"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvFwdSenderAddr"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvFwdDestAddrLength"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvFwdSenderAddrLength"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvFwdHopAddr"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvFwdHopLih"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvFwdInterface"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvFwdService"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvFwdTSpecRate"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvFwdTSpecPeakRate"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvFwdTSpecBurst"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvFwdTSpecMinTu"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvFwdTSpecMaxTu"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvFwdRSpecRate"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvFwdRSpecSlack"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvFwdInterval"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvFwdScope"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvFwdShared"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvFwdExplicit"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvFwdPolicy"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvFwdTtl"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvFwdMsgIdFlag"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvFwdMsgIdEpoch"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvFwdMsgIdNumber"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeResvFwdRsvpHop"))
)
if mibBuilder.loadTexts:
    hwRsvpTeResvFwdGroup.setStatus("current")

hwRsvpTeIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 2, 1, 5)
)
hwRsvpTeIfGroup.setObjects(
      *(("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfUdpNbrs"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfIpNbrs"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfNbrs"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfRefreshBlockadeMultiple"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfRefreshMultiple"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfTtl"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfRefreshInterval"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfRouteDelay"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfEnabled"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfUdpRequired"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfStatus"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfHelloEnabled"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfSrefreshEnabled"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfSrefreshInterval"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfRetranIncDelta"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfRetranInterval"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfAuthEnabled"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfAuthEncrypted"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfAuthHandshake"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfAuthKey"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfWindowSize"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfAuthLifeTime"))
)
if mibBuilder.loadTexts:
    hwRsvpTeIfGroup.setStatus("current")

hwRsvpTeNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 2, 1, 6)
)
hwRsvpTeNbrGroup.setObjects(
      *(("HUAWEI-RSVPTE-MIB", "hwRsvpTeNbrHelloSrcInstance"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeNbrHelloDstInstance"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeNbrHelloLostCounter"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeNbrHelloType"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeNbrHelloEnabled"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeNbrSendersNumber"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeNbrReceiversNumber"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeNbrGrCapability"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeNbrGrRestartTime"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeNbrGrRecoveryTime"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeNbrGrStatus"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeNbrAuthKeyId"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeNbrReductionEnabled"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeNbrReliabilityEnabled"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeNbrProtocol"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeNbrStatus"))
)
if mibBuilder.loadTexts:
    hwRsvpTeNbrGroup.setStatus("current")

hwRsvpTeMessageIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 2, 1, 7)
)
hwRsvpTeMessageIdGroup.setObjects(
    ("HUAWEI-RSVPTE-MIB", "hwRsvpTeMessageIdFlag")
)
if mibBuilder.loadTexts:
    hwRsvpTeMessageIdGroup.setStatus("current")

hwRsvpTeFilterSpecGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 2, 1, 8)
)
hwRsvpTeFilterSpecGroup.setObjects(
      *(("HUAWEI-RSVPTE-MIB", "hwRsvpTeFilterSpecLspId"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeFilterSpecIngressLsrId"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeFilterSpecLabel"))
)
if mibBuilder.loadTexts:
    hwRsvpTeFilterSpecGroup.setStatus("current")

hwRsvpTeRroGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 2, 1, 9)
)
hwRsvpTeRroGroup.setObjects(
      *(("HUAWEI-RSVPTE-MIB", "hwRsvpTeRroType"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeRroIpAddr"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeRroIpPrefixLen"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeRroLabel"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeRroFlag"))
)
if mibBuilder.loadTexts:
    hwRsvpTeRroGroup.setStatus("current")

hwRsvpTeEroGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 2, 1, 10)
)
hwRsvpTeEroGroup.setObjects(
      *(("HUAWEI-RSVPTE-MIB", "hwRsvpTeEroType"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeEroIpAddr"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeEroIpPrefixLen"))
)
if mibBuilder.loadTexts:
    hwRsvpTeEroGroup.setStatus("current")

hwRsvpTeTrapObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 2, 1, 11)
)
hwRsvpTeTrapObjectsGroup.setObjects(
      *(("HUAWEI-RSVPTE-MIB", "hwRsvpTeNbr"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfNbrCurrentCount"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfNbrThreshold"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfNbrTotalCount"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfName"))
)
if mibBuilder.loadTexts:
    hwRsvpTeTrapObjectsGroup.setStatus("current")


# Notification objects

hwRsvpTeHelloLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 12, 2, 1)
)
hwRsvpTeHelloLost.setObjects(
    ("HUAWEI-RSVPTE-MIB", "hwRsvpTeNbr")
)
if mibBuilder.loadTexts:
    hwRsvpTeHelloLost.setStatus(
        "current"
    )

hwRsvpTeHelloLostRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 12, 2, 2)
)
hwRsvpTeHelloLostRecovery.setObjects(
    ("HUAWEI-RSVPTE-MIB", "hwRsvpTeNbr")
)
if mibBuilder.loadTexts:
    hwRsvpTeHelloLostRecovery.setStatus(
        "current"
    )

hwRsvpTeAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 12, 2, 3)
)
hwRsvpTeAuthFail.setObjects(
    ("HUAWEI-RSVPTE-MIB", "hwRsvpTeNbr")
)
if mibBuilder.loadTexts:
    hwRsvpTeAuthFail.setStatus(
        "current"
    )

hwRsvpTeAuthSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 12, 2, 4)
)
hwRsvpTeAuthSuccess.setObjects(
    ("HUAWEI-RSVPTE-MIB", "hwRsvpTeNbr")
)
if mibBuilder.loadTexts:
    hwRsvpTeAuthSuccess.setStatus(
        "current"
    )

hwRsvpTeIfNbrThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 12, 2, 5)
)
hwRsvpTeIfNbrThresholdExceed.setObjects(
      *(("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfName"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfNbrCurrentCount"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfNbrThreshold"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfNbrTotalCount"))
)
if mibBuilder.loadTexts:
    hwRsvpTeIfNbrThresholdExceed.setStatus(
        "current"
    )

hwRsvpTeIfNbrThresholdExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 12, 2, 6)
)
hwRsvpTeIfNbrThresholdExceedClear.setObjects(
    ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfName")
)
if mibBuilder.loadTexts:
    hwRsvpTeIfNbrThresholdExceedClear.setStatus(
        "current"
    )

hwRsvpTeIfNbrTotalCountExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 12, 2, 7)
)
hwRsvpTeIfNbrTotalCountExceed.setObjects(
      *(("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfName"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfNbrTotalCount"))
)
if mibBuilder.loadTexts:
    hwRsvpTeIfNbrTotalCountExceed.setStatus(
        "current"
    )

hwRsvpTeIfNbrTotalCountExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 1, 12, 2, 8)
)
hwRsvpTeIfNbrTotalCountExceedClear.setObjects(
    ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfName")
)
if mibBuilder.loadTexts:
    hwRsvpTeIfNbrTotalCountExceedClear.setStatus(
        "current"
    )


# Notifications groups

hwRsvpTeTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 2, 1, 12)
)
hwRsvpTeTrapGroup.setObjects(
      *(("HUAWEI-RSVPTE-MIB", "hwRsvpTeHelloLost"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeHelloLostRecovery"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeAuthFail"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeAuthSuccess"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfNbrThresholdExceed"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfNbrThresholdExceedClear"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfNbrTotalCountExceed"),
        ("HUAWEI-RSVPTE-MIB", "hwRsvpTeIfNbrTotalCountExceedClear"))
)
if mibBuilder.loadTexts:
    hwRsvpTeTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwRsvpTeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 148, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hwRsvpTeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-RSVPTE-MIB",
    **{"hwRsvpTe": hwRsvpTe,
       "hwRsvpTeObjects": hwRsvpTeObjects,
       "hwRsvpTeSessionTable": hwRsvpTeSessionTable,
       "hwRsvpTeSessionEntry": hwRsvpTeSessionEntry,
       "hwRsvpTeSessionNumber": hwRsvpTeSessionNumber,
       "hwRsvpTeSessionType": hwRsvpTeSessionType,
       "hwRsvpTeSessionDestAddr": hwRsvpTeSessionDestAddr,
       "hwRsvpTeSessionDestAddrLength": hwRsvpTeSessionDestAddrLength,
       "hwRsvpTeSessionSenders": hwRsvpTeSessionSenders,
       "hwRsvpTeSessionReceivers": hwRsvpTeSessionReceivers,
       "hwRsvpTeSessionRequests": hwRsvpTeSessionRequests,
       "hwRsvpTeSessionTunnelId": hwRsvpTeSessionTunnelId,
       "hwRsvpTeSessionTunnelExtId": hwRsvpTeSessionTunnelExtId,
       "hwRsvpTeSessionLspsNumber": hwRsvpTeSessionLspsNumber,
       "hwRsvpTeSessionStyle": hwRsvpTeSessionStyle,
       "hwRsvpTeSenderTable": hwRsvpTeSenderTable,
       "hwRsvpTeSenderEntry": hwRsvpTeSenderEntry,
       "hwRsvpTeSenderNumber": hwRsvpTeSenderNumber,
       "hwRsvpTeSenderType": hwRsvpTeSenderType,
       "hwRsvpTeSenderDestAddr": hwRsvpTeSenderDestAddr,
       "hwRsvpTeSenderAddr": hwRsvpTeSenderAddr,
       "hwRsvpTeSenderDestAddrLength": hwRsvpTeSenderDestAddrLength,
       "hwRsvpTeSenderAddrLength": hwRsvpTeSenderAddrLength,
       "hwRsvpTeSenderHopAddr": hwRsvpTeSenderHopAddr,
       "hwRsvpTeSenderHopLih": hwRsvpTeSenderHopLih,
       "hwRsvpTeSenderInterface": hwRsvpTeSenderInterface,
       "hwRsvpTeSenderTSpecRate": hwRsvpTeSenderTSpecRate,
       "hwRsvpTeSenderTSpecPeakRate": hwRsvpTeSenderTSpecPeakRate,
       "hwRsvpTeSenderTSpecBurst": hwRsvpTeSenderTSpecBurst,
       "hwRsvpTeSenderTSpecMinTu": hwRsvpTeSenderTSpecMinTu,
       "hwRsvpTeSenderTSpecMaxTu": hwRsvpTeSenderTSpecMaxTu,
       "hwRsvpTeSenderInterval": hwRsvpTeSenderInterval,
       "hwRsvpTeSenderRsvpHop": hwRsvpTeSenderRsvpHop,
       "hwRsvpTeSenderPolicy": hwRsvpTeSenderPolicy,
       "hwRsvpTeSenderAdspecBreak": hwRsvpTeSenderAdspecBreak,
       "hwRsvpTeSenderAdspecHopCount": hwRsvpTeSenderAdspecHopCount,
       "hwRsvpTeSenderAdspecPathBw": hwRsvpTeSenderAdspecPathBw,
       "hwRsvpTeSenderAdspecMinLatency": hwRsvpTeSenderAdspecMinLatency,
       "hwRsvpTeSenderAdspecMtu": hwRsvpTeSenderAdspecMtu,
       "hwRsvpTeSenderAdspecGuaranteedSvc": hwRsvpTeSenderAdspecGuaranteedSvc,
       "hwRsvpTeSenderAdspecGuaranteedBreak": hwRsvpTeSenderAdspecGuaranteedBreak,
       "hwRsvpTeSenderAdspecGuaranteedCtot": hwRsvpTeSenderAdspecGuaranteedCtot,
       "hwRsvpTeSenderAdspecGuaranteedDtot": hwRsvpTeSenderAdspecGuaranteedDtot,
       "hwRsvpTeSenderAdspecGuaranteedCsum": hwRsvpTeSenderAdspecGuaranteedCsum,
       "hwRsvpTeSenderAdspecGuaranteedDsum": hwRsvpTeSenderAdspecGuaranteedDsum,
       "hwRsvpTeSenderAdspecGuaranteedHopCount": hwRsvpTeSenderAdspecGuaranteedHopCount,
       "hwRsvpTeSenderAdspecGuaranteedPathBw": hwRsvpTeSenderAdspecGuaranteedPathBw,
       "hwRsvpTeSenderAdspecGuaranteedMinLatency": hwRsvpTeSenderAdspecGuaranteedMinLatency,
       "hwRsvpTeSenderAdspecGuaranteedMtu": hwRsvpTeSenderAdspecGuaranteedMtu,
       "hwRsvpTeSenderAdspecCtrlLoadSvc": hwRsvpTeSenderAdspecCtrlLoadSvc,
       "hwRsvpTeSenderAdspecCtrlLoadBreak": hwRsvpTeSenderAdspecCtrlLoadBreak,
       "hwRsvpTeSenderAdspecCtrlLoadHopCount": hwRsvpTeSenderAdspecCtrlLoadHopCount,
       "hwRsvpTeSenderAdspecCtrlLoadPathBw": hwRsvpTeSenderAdspecCtrlLoadPathBw,
       "hwRsvpTeSenderAdspecCtrlLoadMinLatency": hwRsvpTeSenderAdspecCtrlLoadMinLatency,
       "hwRsvpTeSenderAdspecCtrlLoadMtu": hwRsvpTeSenderAdspecCtrlLoadMtu,
       "hwRsvpTeSenderTtl": hwRsvpTeSenderTtl,
       "hwRsvpTeLspId": hwRsvpTeLspId,
       "hwRsvpTeSenderMsgIdSndFlag": hwRsvpTeSenderMsgIdSndFlag,
       "hwRsvpTeSenderMsgIdSndEpoch": hwRsvpTeSenderMsgIdSndEpoch,
       "hwRsvpTeSenderMsgIdSndNumber": hwRsvpTeSenderMsgIdSndNumber,
       "hwRsvpTeSenderMsgIdRcvFlag": hwRsvpTeSenderMsgIdRcvFlag,
       "hwRsvpTeSenderMsgIdRcvEpoch": hwRsvpTeSenderMsgIdRcvEpoch,
       "hwRsvpTeSenderMsgIdRcvNumber": hwRsvpTeSenderMsgIdRcvNumber,
       "hwRsvpTeSenderClassType": hwRsvpTeSenderClassType,
       "hwRsvpTeSenderLabelRequestCtype": hwRsvpTeSenderLabelRequestCtype,
       "hwRsvpTeSenderLabelRequestL3pid": hwRsvpTeSenderLabelRequestL3pid,
       "hwRsvpTeSenderLabelRequestAtmMinVpi": hwRsvpTeSenderLabelRequestAtmMinVpi,
       "hwRsvpTeSenderLabelRequestAtmMinVci": hwRsvpTeSenderLabelRequestAtmMinVci,
       "hwRsvpTeSenderLabelRequestAtmMaxVpi": hwRsvpTeSenderLabelRequestAtmMaxVpi,
       "hwRsvpTeSenderLabelRequestAtmMaxVci": hwRsvpTeSenderLabelRequestAtmMaxVci,
       "hwRsvpTeSenderLabelRequestFrMinDlci": hwRsvpTeSenderLabelRequestFrMinDlci,
       "hwRsvpTeSenderLabelRequestFrMaxDlci": hwRsvpTeSenderLabelRequestFrMaxDlci,
       "hwRsvpTeSenderSessionAttrType": hwRsvpTeSenderSessionAttrType,
       "hwRsvpTeSenderSessionAttrSetupPrio": hwRsvpTeSenderSessionAttrSetupPrio,
       "hwRsvpTeSenderSessionAttrHoldPrio": hwRsvpTeSenderSessionAttrHoldPrio,
       "hwRsvpTeSenderSessionAttrFlag": hwRsvpTeSenderSessionAttrFlag,
       "hwRsvpTeSenderSessionAttrName": hwRsvpTeSenderSessionAttrName,
       "hwRsvpTeSenderSessionAttrExcludeAny": hwRsvpTeSenderSessionAttrExcludeAny,
       "hwRsvpTeSenderSessionAttrIncludeAny": hwRsvpTeSenderSessionAttrIncludeAny,
       "hwRsvpTeSenderSessionAttrIncludeAll": hwRsvpTeSenderSessionAttrIncludeAll,
       "hwRsvpTeSenderFrrSetupPrio": hwRsvpTeSenderFrrSetupPrio,
       "hwRsvpTeSenderFrrHoldPrio": hwRsvpTeSenderFrrHoldPrio,
       "hwRsvpTeSenderFrrHopLimit": hwRsvpTeSenderFrrHopLimit,
       "hwRsvpTeSenderFrrFlag": hwRsvpTeSenderFrrFlag,
       "hwRsvpTeSenderFrrBandwidth": hwRsvpTeSenderFrrBandwidth,
       "hwRsvpTeSenderFrrExcludeAny": hwRsvpTeSenderFrrExcludeAny,
       "hwRsvpTeSenderFrrIncludeAny": hwRsvpTeSenderFrrIncludeAny,
       "hwRsvpTeSenderFrrIncludeAll": hwRsvpTeSenderFrrIncludeAll,
       "hwRsvpTeSenderFrrInuseFlag": hwRsvpTeSenderFrrInuseFlag,
       "hwRsvpTeSenderDiffServPsc": hwRsvpTeSenderDiffServPsc,
       "hwRsvpTeResvTable": hwRsvpTeResvTable,
       "hwRsvpTeResvEntry": hwRsvpTeResvEntry,
       "hwRsvpTeResvNumber": hwRsvpTeResvNumber,
       "hwRsvpTeResvType": hwRsvpTeResvType,
       "hwRsvpTeResvDestAddr": hwRsvpTeResvDestAddr,
       "hwRsvpTeResvSenderAddr": hwRsvpTeResvSenderAddr,
       "hwRsvpTeResvDestAddrLength": hwRsvpTeResvDestAddrLength,
       "hwRsvpTeResvSenderAddrLength": hwRsvpTeResvSenderAddrLength,
       "hwRsvpTeResvHopAddr": hwRsvpTeResvHopAddr,
       "hwRsvpTeResvHopLih": hwRsvpTeResvHopLih,
       "hwRsvpTeResvInterface": hwRsvpTeResvInterface,
       "hwRsvpTeResvService": hwRsvpTeResvService,
       "hwRsvpTeResvTSpecRate": hwRsvpTeResvTSpecRate,
       "hwRsvpTeResvTSpecPeakRate": hwRsvpTeResvTSpecPeakRate,
       "hwRsvpTeResvTSpecBurst": hwRsvpTeResvTSpecBurst,
       "hwRsvpTeResvTSpecMinTu": hwRsvpTeResvTSpecMinTu,
       "hwRsvpTeResvTSpecMaxTu": hwRsvpTeResvTSpecMaxTu,
       "hwRsvpTeResvRSpecRate": hwRsvpTeResvRSpecRate,
       "hwRsvpTeResvRSpecSlack": hwRsvpTeResvRSpecSlack,
       "hwRsvpTeResvInterval": hwRsvpTeResvInterval,
       "hwRsvpTeResvScope": hwRsvpTeResvScope,
       "hwRsvpTeResvShared": hwRsvpTeResvShared,
       "hwRsvpTeResvExplicit": hwRsvpTeResvExplicit,
       "hwRsvpTeResvRsvpHop": hwRsvpTeResvRsvpHop,
       "hwRsvpTeResvPolicy": hwRsvpTeResvPolicy,
       "hwRsvpTeResvTtl": hwRsvpTeResvTtl,
       "hwRsvpTeResvConfirm": hwRsvpTeResvConfirm,
       "hwRsvpTeResvFwdTable": hwRsvpTeResvFwdTable,
       "hwRsvpTeResvFwdEntry": hwRsvpTeResvFwdEntry,
       "hwRsvpTeResvFwdNumber": hwRsvpTeResvFwdNumber,
       "hwRsvpTeResvFwdType": hwRsvpTeResvFwdType,
       "hwRsvpTeResvFwdDestAddr": hwRsvpTeResvFwdDestAddr,
       "hwRsvpTeResvFwdSenderAddr": hwRsvpTeResvFwdSenderAddr,
       "hwRsvpTeResvFwdDestAddrLength": hwRsvpTeResvFwdDestAddrLength,
       "hwRsvpTeResvFwdSenderAddrLength": hwRsvpTeResvFwdSenderAddrLength,
       "hwRsvpTeResvFwdHopAddr": hwRsvpTeResvFwdHopAddr,
       "hwRsvpTeResvFwdHopLih": hwRsvpTeResvFwdHopLih,
       "hwRsvpTeResvFwdInterface": hwRsvpTeResvFwdInterface,
       "hwRsvpTeResvFwdService": hwRsvpTeResvFwdService,
       "hwRsvpTeResvFwdTSpecRate": hwRsvpTeResvFwdTSpecRate,
       "hwRsvpTeResvFwdTSpecPeakRate": hwRsvpTeResvFwdTSpecPeakRate,
       "hwRsvpTeResvFwdTSpecBurst": hwRsvpTeResvFwdTSpecBurst,
       "hwRsvpTeResvFwdTSpecMinTu": hwRsvpTeResvFwdTSpecMinTu,
       "hwRsvpTeResvFwdTSpecMaxTu": hwRsvpTeResvFwdTSpecMaxTu,
       "hwRsvpTeResvFwdRSpecRate": hwRsvpTeResvFwdRSpecRate,
       "hwRsvpTeResvFwdRSpecSlack": hwRsvpTeResvFwdRSpecSlack,
       "hwRsvpTeResvFwdInterval": hwRsvpTeResvFwdInterval,
       "hwRsvpTeResvFwdScope": hwRsvpTeResvFwdScope,
       "hwRsvpTeResvFwdShared": hwRsvpTeResvFwdShared,
       "hwRsvpTeResvFwdExplicit": hwRsvpTeResvFwdExplicit,
       "hwRsvpTeResvFwdRsvpHop": hwRsvpTeResvFwdRsvpHop,
       "hwRsvpTeResvFwdPolicy": hwRsvpTeResvFwdPolicy,
       "hwRsvpTeResvFwdTtl": hwRsvpTeResvFwdTtl,
       "hwRsvpTeResvFwdMsgIdFlag": hwRsvpTeResvFwdMsgIdFlag,
       "hwRsvpTeResvFwdMsgIdEpoch": hwRsvpTeResvFwdMsgIdEpoch,
       "hwRsvpTeResvFwdMsgIdNumber": hwRsvpTeResvFwdMsgIdNumber,
       "hwRsvpTeIfTable": hwRsvpTeIfTable,
       "hwRsvpTeIfEntry": hwRsvpTeIfEntry,
       "hwRsvpTeIfUdpNbrs": hwRsvpTeIfUdpNbrs,
       "hwRsvpTeIfIpNbrs": hwRsvpTeIfIpNbrs,
       "hwRsvpTeIfNbrs": hwRsvpTeIfNbrs,
       "hwRsvpTeIfRefreshBlockadeMultiple": hwRsvpTeIfRefreshBlockadeMultiple,
       "hwRsvpTeIfRefreshMultiple": hwRsvpTeIfRefreshMultiple,
       "hwRsvpTeIfTtl": hwRsvpTeIfTtl,
       "hwRsvpTeIfRefreshInterval": hwRsvpTeIfRefreshInterval,
       "hwRsvpTeIfRouteDelay": hwRsvpTeIfRouteDelay,
       "hwRsvpTeIfEnabled": hwRsvpTeIfEnabled,
       "hwRsvpTeIfUdpRequired": hwRsvpTeIfUdpRequired,
       "hwRsvpTeIfStatus": hwRsvpTeIfStatus,
       "hwRsvpTeIfHelloEnabled": hwRsvpTeIfHelloEnabled,
       "hwRsvpTeIfSrefreshEnabled": hwRsvpTeIfSrefreshEnabled,
       "hwRsvpTeIfSrefreshInterval": hwRsvpTeIfSrefreshInterval,
       "hwRsvpTeIfRetranIncDelta": hwRsvpTeIfRetranIncDelta,
       "hwRsvpTeIfRetranInterval": hwRsvpTeIfRetranInterval,
       "hwRsvpTeIfAuthEnabled": hwRsvpTeIfAuthEnabled,
       "hwRsvpTeIfAuthEncrypted": hwRsvpTeIfAuthEncrypted,
       "hwRsvpTeIfAuthHandshake": hwRsvpTeIfAuthHandshake,
       "hwRsvpTeIfAuthLifeTime": hwRsvpTeIfAuthLifeTime,
       "hwRsvpTeIfAuthKey": hwRsvpTeIfAuthKey,
       "hwRsvpTeIfWindowSize": hwRsvpTeIfWindowSize,
       "hwRsvpTeNbrTable": hwRsvpTeNbrTable,
       "hwRsvpTeNbrEntry": hwRsvpTeNbrEntry,
       "hwRsvpTeNbrAddress": hwRsvpTeNbrAddress,
       "hwRsvpTeNbrProtocol": hwRsvpTeNbrProtocol,
       "hwRsvpTeNbrStatus": hwRsvpTeNbrStatus,
       "hwRsvpTeNbrSendersNumber": hwRsvpTeNbrSendersNumber,
       "hwRsvpTeNbrReceiversNumber": hwRsvpTeNbrReceiversNumber,
       "hwRsvpTeNbrHelloEnabled": hwRsvpTeNbrHelloEnabled,
       "hwRsvpTeNbrHelloSrcInstance": hwRsvpTeNbrHelloSrcInstance,
       "hwRsvpTeNbrHelloDstInstance": hwRsvpTeNbrHelloDstInstance,
       "hwRsvpTeNbrHelloLostCounter": hwRsvpTeNbrHelloLostCounter,
       "hwRsvpTeNbrHelloType": hwRsvpTeNbrHelloType,
       "hwRsvpTeNbrGrCapability": hwRsvpTeNbrGrCapability,
       "hwRsvpTeNbrGrRestartTime": hwRsvpTeNbrGrRestartTime,
       "hwRsvpTeNbrGrRecoveryTime": hwRsvpTeNbrGrRecoveryTime,
       "hwRsvpTeNbrGrStatus": hwRsvpTeNbrGrStatus,
       "hwRsvpTeNbrAuthKeyId": hwRsvpTeNbrAuthKeyId,
       "hwRsvpTeNbrReductionEnabled": hwRsvpTeNbrReductionEnabled,
       "hwRsvpTeNbrReliabilityEnabled": hwRsvpTeNbrReliabilityEnabled,
       "hwRsvpTeMessageIdTable": hwRsvpTeMessageIdTable,
       "hwRsvpTeMessageIdEntry": hwRsvpTeMessageIdEntry,
       "hwRsvpTeMessageIdEpoch": hwRsvpTeMessageIdEpoch,
       "hwRsvpTeMessageIdNumber": hwRsvpTeMessageIdNumber,
       "hwRsvpTeMessageIdFlag": hwRsvpTeMessageIdFlag,
       "hwRsvpTeFilterSpecTable": hwRsvpTeFilterSpecTable,
       "hwRsvpTeFilterSpecEntry": hwRsvpTeFilterSpecEntry,
       "hwRsvpTeFilterSpecNumber": hwRsvpTeFilterSpecNumber,
       "hwRsvpTeFilterSpecLspId": hwRsvpTeFilterSpecLspId,
       "hwRsvpTeFilterSpecIngressLsrId": hwRsvpTeFilterSpecIngressLsrId,
       "hwRsvpTeFilterSpecLabel": hwRsvpTeFilterSpecLabel,
       "hwRsvpTeRroTable": hwRsvpTeRroTable,
       "hwRsvpTeRroEntry": hwRsvpTeRroEntry,
       "hwRsvpTeRroNumber": hwRsvpTeRroNumber,
       "hwRsvpTeRroType": hwRsvpTeRroType,
       "hwRsvpTeRroIpAddr": hwRsvpTeRroIpAddr,
       "hwRsvpTeRroIpPrefixLen": hwRsvpTeRroIpPrefixLen,
       "hwRsvpTeRroLabel": hwRsvpTeRroLabel,
       "hwRsvpTeRroFlag": hwRsvpTeRroFlag,
       "hwRsvpTeEroTable": hwRsvpTeEroTable,
       "hwRsvpTeEroEntry": hwRsvpTeEroEntry,
       "hwRsvpTeEroNumber": hwRsvpTeEroNumber,
       "hwRsvpTeEroType": hwRsvpTeEroType,
       "hwRsvpTeEroIpAddr": hwRsvpTeEroIpAddr,
       "hwRsvpTeEroIpPrefixLen": hwRsvpTeEroIpPrefixLen,
       "hwRsvpTeExtendObjects": hwRsvpTeExtendObjects,
       "hwRsvpTeExtendTrap": hwRsvpTeExtendTrap,
       "hwRsvpTeTrapObjects": hwRsvpTeTrapObjects,
       "hwRsvpTeNbr": hwRsvpTeNbr,
       "hwRsvpTeIfNbrCurrentCount": hwRsvpTeIfNbrCurrentCount,
       "hwRsvpTeIfNbrThreshold": hwRsvpTeIfNbrThreshold,
       "hwRsvpTeIfNbrTotalCount": hwRsvpTeIfNbrTotalCount,
       "hwRsvpTeIfName": hwRsvpTeIfName,
       "hwRsvpTeTrap": hwRsvpTeTrap,
       "hwRsvpTeHelloLost": hwRsvpTeHelloLost,
       "hwRsvpTeHelloLostRecovery": hwRsvpTeHelloLostRecovery,
       "hwRsvpTeAuthFail": hwRsvpTeAuthFail,
       "hwRsvpTeAuthSuccess": hwRsvpTeAuthSuccess,
       "hwRsvpTeIfNbrThresholdExceed": hwRsvpTeIfNbrThresholdExceed,
       "hwRsvpTeIfNbrThresholdExceedClear": hwRsvpTeIfNbrThresholdExceedClear,
       "hwRsvpTeIfNbrTotalCountExceed": hwRsvpTeIfNbrTotalCountExceed,
       "hwRsvpTeIfNbrTotalCountExceedClear": hwRsvpTeIfNbrTotalCountExceedClear,
       "hwRsvpTeConformance": hwRsvpTeConformance,
       "hwRsvpTeGroups": hwRsvpTeGroups,
       "hwRsvpTeSessionGroup": hwRsvpTeSessionGroup,
       "hwRsvpTeSenderGroup": hwRsvpTeSenderGroup,
       "hwRsvpTeResvGroup": hwRsvpTeResvGroup,
       "hwRsvpTeResvFwdGroup": hwRsvpTeResvFwdGroup,
       "hwRsvpTeIfGroup": hwRsvpTeIfGroup,
       "hwRsvpTeNbrGroup": hwRsvpTeNbrGroup,
       "hwRsvpTeMessageIdGroup": hwRsvpTeMessageIdGroup,
       "hwRsvpTeFilterSpecGroup": hwRsvpTeFilterSpecGroup,
       "hwRsvpTeRroGroup": hwRsvpTeRroGroup,
       "hwRsvpTeEroGroup": hwRsvpTeEroGroup,
       "hwRsvpTeTrapObjectsGroup": hwRsvpTeTrapObjectsGroup,
       "hwRsvpTeTrapGroup": hwRsvpTeTrapGroup,
       "hwRsvpTeCompliances": hwRsvpTeCompliances,
       "hwRsvpTeCompliance": hwRsvpTeCompliance}
)
