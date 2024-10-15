# SNMP MIB module (CISCO-PTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:17 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 760)
)
ciscoPtpMIB.setRevisions(
        ("2011-01-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ClockDomainType(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class ClockIdentity(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class ClockIntervalBase2(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )



class ClockMechanismType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 254),
          ("e2e", 1),
          ("p2p", 2))
    )



class ClockInstanceType(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class ClockPortNumber(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class ClockPortState(Integer32, TextualConvention):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("faulty", 2),
          ("initializing", 1),
          ("listening", 4),
          ("master", 6),
          ("passive", 7),
          ("preMaster", 5),
          ("slave", 9),
          ("uncalibrated", 8))
    )



class ClockProfileType(Integer32, TextualConvention):
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
        *(("default", 1),
          ("telecom", 2),
          ("vendorspecific", 3))
    )



class ClockQualityAccuracyType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("microSec1", 35),
          ("microSec10", 37),
          ("microSec100", 39),
          ("microSec25", 38),
          ("microSec250", 40),
          ("microSec2dot5", 36),
          ("milliSec1", 41),
          ("milliSec10", 43),
          ("milliSec100", 45),
          ("milliSec25", 44),
          ("milliSec250", 46),
          ("milliSec2dot5", 42),
          ("nanoSecond100", 33),
          ("nanoSecond25", 32),
          ("nanoSecond250", 34),
          ("reserved00", 1),
          ("reserved255", 255),
          ("second1", 47),
          ("second10", 48),
          ("secondGreater10", 49),
          ("unknown", 254))
    )



class ClockQualityClassType(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class ClockRoleType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )



class ClockStateType(Integer32, TextualConvention):
    status = "current"
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
        *(("acquiring", 3),
          ("freerun", 1),
          ("frequencyLocked", 4),
          ("holdover", 2),
          ("phaseAligned", 5))
    )



class ClockTimeSourceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              48,
              64,
              80,
              96,
              144,
              160)
        )
    )
    namedValues = NamedValues(
        *(("atomicClock", 16),
          ("gps", 32),
          ("handSet", 96),
          ("internalOsillator", 160),
          ("ntp", 80),
          ("other", 144),
          ("ptp", 64),
          ("terrestrialRadio", 48))
    )



class ClockTimeInterval(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class ClockTxModeType(Integer32, TextualConvention):
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
        *(("multicast", 2),
          ("multicastmix", 3),
          ("unicast", 1))
    )



class ClockType(Integer32, TextualConvention):
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
        *(("boundaryClock", 2),
          ("boundaryNode", 4),
          ("ordinaryClock", 1),
          ("transparentClock", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoPtpMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoPtpMIBNotifs = _CiscoPtpMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 0)
)
_CiscoPtpMIBObjects_ObjectIdentity = ObjectIdentity
ciscoPtpMIBObjects = _CiscoPtpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1)
)
_CiscoPtpMIBSystemInfo_ObjectIdentity = ObjectIdentity
ciscoPtpMIBSystemInfo = _CiscoPtpMIBSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 1)
)
_CPtpSystemTable_Object = MibTable
cPtpSystemTable = _CPtpSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cPtpSystemTable.setStatus("current")
_CPtpSystemEntry_Object = MibTableRow
cPtpSystemEntry = _CPtpSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 1, 1, 1)
)
cPtpSystemEntry.setIndexNames(
    (0, "CISCO-PTP-MIB", "cPtpDomainIndex"),
    (0, "CISCO-PTP-MIB", "cPtpInstanceIndex"),
)
if mibBuilder.loadTexts:
    cPtpSystemEntry.setStatus("current")
_CPtpDomainIndex_Type = ClockDomainType
_CPtpDomainIndex_Object = MibTableColumn
cPtpDomainIndex = _CPtpDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 1, 1, 1, 1),
    _CPtpDomainIndex_Type()
)
cPtpDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpDomainIndex.setStatus("current")


class _CPtpInstanceIndex_Type(ClockInstanceType):
    """Custom type cPtpInstanceIndex based on ClockInstanceType"""
    subtypeSpec = ClockInstanceType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CPtpInstanceIndex_Type.__name__ = "ClockInstanceType"
_CPtpInstanceIndex_Object = MibTableColumn
cPtpInstanceIndex = _CPtpInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 1, 1, 1, 2),
    _CPtpInstanceIndex_Type()
)
cPtpInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpInstanceIndex.setStatus("current")
_CPtpDomainClockPortsTotal_Type = Gauge32
_CPtpDomainClockPortsTotal_Object = MibTableColumn
cPtpDomainClockPortsTotal = _CPtpDomainClockPortsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 1, 1, 1, 3),
    _CPtpDomainClockPortsTotal_Type()
)
cPtpDomainClockPortsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpDomainClockPortsTotal.setStatus("current")
if mibBuilder.loadTexts:
    cPtpDomainClockPortsTotal.setUnits("ptp ports")
_CPtpDomainClockPortPhysicalInterfacesTotal_Type = Gauge32
_CPtpDomainClockPortPhysicalInterfacesTotal_Object = MibTableColumn
cPtpDomainClockPortPhysicalInterfacesTotal = _CPtpDomainClockPortPhysicalInterfacesTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 1, 1, 1, 4),
    _CPtpDomainClockPortPhysicalInterfacesTotal_Type()
)
cPtpDomainClockPortPhysicalInterfacesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpDomainClockPortPhysicalInterfacesTotal.setStatus("current")
if mibBuilder.loadTexts:
    cPtpDomainClockPortPhysicalInterfacesTotal.setUnits("physical ports")
_CPtpSystemDomainTable_Object = MibTable
cPtpSystemDomainTable = _CPtpSystemDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cPtpSystemDomainTable.setStatus("current")
_CPtpSystemDomainEntry_Object = MibTableRow
cPtpSystemDomainEntry = _CPtpSystemDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 1, 2, 1)
)
cPtpSystemDomainEntry.setIndexNames(
    (0, "CISCO-PTP-MIB", "cPtpSystemDomainClockTypeIndex"),
)
if mibBuilder.loadTexts:
    cPtpSystemDomainEntry.setStatus("current")
_CPtpSystemDomainClockTypeIndex_Type = ClockType
_CPtpSystemDomainClockTypeIndex_Object = MibTableColumn
cPtpSystemDomainClockTypeIndex = _CPtpSystemDomainClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 1, 2, 1, 1),
    _CPtpSystemDomainClockTypeIndex_Type()
)
cPtpSystemDomainClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpSystemDomainClockTypeIndex.setStatus("current")
_CPtpSystemDomainTotals_Type = Gauge32
_CPtpSystemDomainTotals_Object = MibTableColumn
cPtpSystemDomainTotals = _CPtpSystemDomainTotals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 1, 2, 1, 2),
    _CPtpSystemDomainTotals_Type()
)
cPtpSystemDomainTotals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpSystemDomainTotals.setStatus("current")
if mibBuilder.loadTexts:
    cPtpSystemDomainTotals.setUnits("domains")
_CPtpClockNodeTable_Object = MibTable
cPtpClockNodeTable = _CPtpClockNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cPtpClockNodeTable.setStatus("current")
_CPtpClockNodeEntry_Object = MibTableRow
cPtpClockNodeEntry = _CPtpClockNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 1, 3, 1)
)
cPtpClockNodeEntry.setIndexNames(
    (0, "CISCO-PTP-MIB", "cPtpClockDomainIndex"),
    (0, "CISCO-PTP-MIB", "cPtpClockTypeIndex"),
    (0, "CISCO-PTP-MIB", "cPtpClockInstanceIndex"),
)
if mibBuilder.loadTexts:
    cPtpClockNodeEntry.setStatus("current")
_CPtpClockDomainIndex_Type = ClockDomainType
_CPtpClockDomainIndex_Object = MibTableColumn
cPtpClockDomainIndex = _CPtpClockDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 1, 3, 1, 1),
    _CPtpClockDomainIndex_Type()
)
cPtpClockDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockDomainIndex.setStatus("current")
_CPtpClockTypeIndex_Type = ClockType
_CPtpClockTypeIndex_Object = MibTableColumn
cPtpClockTypeIndex = _CPtpClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 1, 3, 1, 2),
    _CPtpClockTypeIndex_Type()
)
cPtpClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockTypeIndex.setStatus("current")


class _CPtpClockInstanceIndex_Type(ClockInstanceType):
    """Custom type cPtpClockInstanceIndex based on ClockInstanceType"""
    subtypeSpec = ClockInstanceType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CPtpClockInstanceIndex_Type.__name__ = "ClockInstanceType"
_CPtpClockInstanceIndex_Object = MibTableColumn
cPtpClockInstanceIndex = _CPtpClockInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 1, 3, 1, 3),
    _CPtpClockInstanceIndex_Type()
)
cPtpClockInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockInstanceIndex.setStatus("current")
_CPtpClockInput1ppsEnabled_Type = TruthValue
_CPtpClockInput1ppsEnabled_Object = MibTableColumn
cPtpClockInput1ppsEnabled = _CPtpClockInput1ppsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 1, 3, 1, 4),
    _CPtpClockInput1ppsEnabled_Type()
)
cPtpClockInput1ppsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockInput1ppsEnabled.setStatus("current")
_CPtpClockInputFrequencyEnabled_Type = TruthValue
_CPtpClockInputFrequencyEnabled_Object = MibTableColumn
cPtpClockInputFrequencyEnabled = _CPtpClockInputFrequencyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 1, 3, 1, 5),
    _CPtpClockInputFrequencyEnabled_Type()
)
cPtpClockInputFrequencyEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockInputFrequencyEnabled.setStatus("current")
_CPtpClockTODEnabled_Type = TruthValue
_CPtpClockTODEnabled_Object = MibTableColumn
cPtpClockTODEnabled = _CPtpClockTODEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 1, 3, 1, 6),
    _CPtpClockTODEnabled_Type()
)
cPtpClockTODEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockTODEnabled.setStatus("current")
_CPtpClockOutput1ppsEnabled_Type = TruthValue
_CPtpClockOutput1ppsEnabled_Object = MibTableColumn
cPtpClockOutput1ppsEnabled = _CPtpClockOutput1ppsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 1, 3, 1, 7),
    _CPtpClockOutput1ppsEnabled_Type()
)
cPtpClockOutput1ppsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockOutput1ppsEnabled.setStatus("current")
_CPtpClockOutput1ppsOffsetEnabled_Type = TruthValue
_CPtpClockOutput1ppsOffsetEnabled_Object = MibTableColumn
cPtpClockOutput1ppsOffsetEnabled = _CPtpClockOutput1ppsOffsetEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 1, 3, 1, 8),
    _CPtpClockOutput1ppsOffsetEnabled_Type()
)
cPtpClockOutput1ppsOffsetEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockOutput1ppsOffsetEnabled.setStatus("current")
_CPtpClockOutput1ppsOffsetValue_Type = Unsigned32
_CPtpClockOutput1ppsOffsetValue_Object = MibTableColumn
cPtpClockOutput1ppsOffsetValue = _CPtpClockOutput1ppsOffsetValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 1, 3, 1, 9),
    _CPtpClockOutput1ppsOffsetValue_Type()
)
cPtpClockOutput1ppsOffsetValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockOutput1ppsOffsetValue.setStatus("current")
_CPtpClockOutput1ppsOffsetNegative_Type = TruthValue
_CPtpClockOutput1ppsOffsetNegative_Object = MibTableColumn
cPtpClockOutput1ppsOffsetNegative = _CPtpClockOutput1ppsOffsetNegative_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 1, 3, 1, 10),
    _CPtpClockOutput1ppsOffsetNegative_Type()
)
cPtpClockOutput1ppsOffsetNegative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockOutput1ppsOffsetNegative.setStatus("current")
_CPtpClockInput1ppsInterface_Type = DisplayString
_CPtpClockInput1ppsInterface_Object = MibTableColumn
cPtpClockInput1ppsInterface = _CPtpClockInput1ppsInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 1, 3, 1, 11),
    _CPtpClockInput1ppsInterface_Type()
)
cPtpClockInput1ppsInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockInput1ppsInterface.setStatus("current")
_CPtpClockOutput1ppsInterface_Type = DisplayString
_CPtpClockOutput1ppsInterface_Object = MibTableColumn
cPtpClockOutput1ppsInterface = _CPtpClockOutput1ppsInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 1, 3, 1, 12),
    _CPtpClockOutput1ppsInterface_Type()
)
cPtpClockOutput1ppsInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockOutput1ppsInterface.setStatus("current")
_CPtpClockTODInterface_Type = DisplayString
_CPtpClockTODInterface_Object = MibTableColumn
cPtpClockTODInterface = _CPtpClockTODInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 1, 3, 1, 13),
    _CPtpClockTODInterface_Type()
)
cPtpClockTODInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockTODInterface.setStatus("current")
_CPtpSystemProfile_Type = ClockProfileType
_CPtpSystemProfile_Object = MibScalar
cPtpSystemProfile = _CPtpSystemProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 1, 4),
    _CPtpSystemProfile_Type()
)
cPtpSystemProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpSystemProfile.setStatus("current")
_CiscoPtpMIBClockInfo_ObjectIdentity = ObjectIdentity
ciscoPtpMIBClockInfo = _CiscoPtpMIBClockInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2)
)
_CPtpClockCurrentDSTable_Object = MibTable
cPtpClockCurrentDSTable = _CPtpClockCurrentDSTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cPtpClockCurrentDSTable.setStatus("current")
_CPtpClockCurrentDSEntry_Object = MibTableRow
cPtpClockCurrentDSEntry = _CPtpClockCurrentDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 1, 1)
)
cPtpClockCurrentDSEntry.setIndexNames(
    (0, "CISCO-PTP-MIB", "cPtpClockCurrentDSDomainIndex"),
    (0, "CISCO-PTP-MIB", "cPtpClockCurrentDSClockTypeIndex"),
    (0, "CISCO-PTP-MIB", "cPtpClockCurrentDSInstanceIndex"),
)
if mibBuilder.loadTexts:
    cPtpClockCurrentDSEntry.setStatus("current")
_CPtpClockCurrentDSDomainIndex_Type = ClockDomainType
_CPtpClockCurrentDSDomainIndex_Object = MibTableColumn
cPtpClockCurrentDSDomainIndex = _CPtpClockCurrentDSDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 1, 1, 1),
    _CPtpClockCurrentDSDomainIndex_Type()
)
cPtpClockCurrentDSDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockCurrentDSDomainIndex.setStatus("current")
_CPtpClockCurrentDSClockTypeIndex_Type = ClockType
_CPtpClockCurrentDSClockTypeIndex_Object = MibTableColumn
cPtpClockCurrentDSClockTypeIndex = _CPtpClockCurrentDSClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 1, 1, 2),
    _CPtpClockCurrentDSClockTypeIndex_Type()
)
cPtpClockCurrentDSClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockCurrentDSClockTypeIndex.setStatus("current")


class _CPtpClockCurrentDSInstanceIndex_Type(ClockInstanceType):
    """Custom type cPtpClockCurrentDSInstanceIndex based on ClockInstanceType"""
    subtypeSpec = ClockInstanceType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CPtpClockCurrentDSInstanceIndex_Type.__name__ = "ClockInstanceType"
_CPtpClockCurrentDSInstanceIndex_Object = MibTableColumn
cPtpClockCurrentDSInstanceIndex = _CPtpClockCurrentDSInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 1, 1, 3),
    _CPtpClockCurrentDSInstanceIndex_Type()
)
cPtpClockCurrentDSInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockCurrentDSInstanceIndex.setStatus("current")
_CPtpClockCurrentDSStepsRemoved_Type = Counter32
_CPtpClockCurrentDSStepsRemoved_Object = MibTableColumn
cPtpClockCurrentDSStepsRemoved = _CPtpClockCurrentDSStepsRemoved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 1, 1, 4),
    _CPtpClockCurrentDSStepsRemoved_Type()
)
cPtpClockCurrentDSStepsRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockCurrentDSStepsRemoved.setStatus("current")
if mibBuilder.loadTexts:
    cPtpClockCurrentDSStepsRemoved.setUnits("steps")
_CPtpClockCurrentDSOffsetFromMaster_Type = ClockTimeInterval
_CPtpClockCurrentDSOffsetFromMaster_Object = MibTableColumn
cPtpClockCurrentDSOffsetFromMaster = _CPtpClockCurrentDSOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 1, 1, 5),
    _CPtpClockCurrentDSOffsetFromMaster_Type()
)
cPtpClockCurrentDSOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockCurrentDSOffsetFromMaster.setStatus("current")
if mibBuilder.loadTexts:
    cPtpClockCurrentDSOffsetFromMaster.setUnits("Time Interval")
_CPtpClockCurrentDSMeanPathDelay_Type = ClockTimeInterval
_CPtpClockCurrentDSMeanPathDelay_Object = MibTableColumn
cPtpClockCurrentDSMeanPathDelay = _CPtpClockCurrentDSMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 1, 1, 6),
    _CPtpClockCurrentDSMeanPathDelay_Type()
)
cPtpClockCurrentDSMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockCurrentDSMeanPathDelay.setStatus("current")
_CPtpClockParentDSTable_Object = MibTable
cPtpClockParentDSTable = _CPtpClockParentDSTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cPtpClockParentDSTable.setStatus("current")
_CPtpClockParentDSEntry_Object = MibTableRow
cPtpClockParentDSEntry = _CPtpClockParentDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 2, 1)
)
cPtpClockParentDSEntry.setIndexNames(
    (0, "CISCO-PTP-MIB", "cPtpClockParentDSDomainIndex"),
    (0, "CISCO-PTP-MIB", "cPtpClockParentDSClockTypeIndex"),
    (0, "CISCO-PTP-MIB", "cPtpClockParentDSInstanceIndex"),
)
if mibBuilder.loadTexts:
    cPtpClockParentDSEntry.setStatus("current")
_CPtpClockParentDSDomainIndex_Type = ClockDomainType
_CPtpClockParentDSDomainIndex_Object = MibTableColumn
cPtpClockParentDSDomainIndex = _CPtpClockParentDSDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 2, 1, 1),
    _CPtpClockParentDSDomainIndex_Type()
)
cPtpClockParentDSDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockParentDSDomainIndex.setStatus("current")
_CPtpClockParentDSClockTypeIndex_Type = ClockType
_CPtpClockParentDSClockTypeIndex_Object = MibTableColumn
cPtpClockParentDSClockTypeIndex = _CPtpClockParentDSClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 2, 1, 2),
    _CPtpClockParentDSClockTypeIndex_Type()
)
cPtpClockParentDSClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockParentDSClockTypeIndex.setStatus("current")


class _CPtpClockParentDSInstanceIndex_Type(ClockInstanceType):
    """Custom type cPtpClockParentDSInstanceIndex based on ClockInstanceType"""
    subtypeSpec = ClockInstanceType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CPtpClockParentDSInstanceIndex_Type.__name__ = "ClockInstanceType"
_CPtpClockParentDSInstanceIndex_Object = MibTableColumn
cPtpClockParentDSInstanceIndex = _CPtpClockParentDSInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 2, 1, 3),
    _CPtpClockParentDSInstanceIndex_Type()
)
cPtpClockParentDSInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockParentDSInstanceIndex.setStatus("current")
_CPtpClockParentDSParentPortIdentity_Type = OctetString
_CPtpClockParentDSParentPortIdentity_Object = MibTableColumn
cPtpClockParentDSParentPortIdentity = _CPtpClockParentDSParentPortIdentity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 2, 1, 4),
    _CPtpClockParentDSParentPortIdentity_Type()
)
cPtpClockParentDSParentPortIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockParentDSParentPortIdentity.setStatus("current")
_CPtpClockParentDSParentStats_Type = TruthValue
_CPtpClockParentDSParentStats_Object = MibTableColumn
cPtpClockParentDSParentStats = _CPtpClockParentDSParentStats_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 2, 1, 5),
    _CPtpClockParentDSParentStats_Type()
)
cPtpClockParentDSParentStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockParentDSParentStats.setStatus("current")


class _CPtpClockParentDSOffset_Type(ClockIntervalBase2):
    """Custom type cPtpClockParentDSOffset based on ClockIntervalBase2"""
    subtypeSpec = ClockIntervalBase2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_CPtpClockParentDSOffset_Type.__name__ = "ClockIntervalBase2"
_CPtpClockParentDSOffset_Object = MibTableColumn
cPtpClockParentDSOffset = _CPtpClockParentDSOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 2, 1, 6),
    _CPtpClockParentDSOffset_Type()
)
cPtpClockParentDSOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockParentDSOffset.setStatus("current")
_CPtpClockParentDSClockPhChRate_Type = Integer32
_CPtpClockParentDSClockPhChRate_Object = MibTableColumn
cPtpClockParentDSClockPhChRate = _CPtpClockParentDSClockPhChRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 2, 1, 7),
    _CPtpClockParentDSClockPhChRate_Type()
)
cPtpClockParentDSClockPhChRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockParentDSClockPhChRate.setStatus("current")
_CPtpClockParentDSGMClockIdentity_Type = ClockIdentity
_CPtpClockParentDSGMClockIdentity_Object = MibTableColumn
cPtpClockParentDSGMClockIdentity = _CPtpClockParentDSGMClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 2, 1, 8),
    _CPtpClockParentDSGMClockIdentity_Type()
)
cPtpClockParentDSGMClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockParentDSGMClockIdentity.setStatus("current")
_CPtpClockParentDSGMClockPriority1_Type = Integer32
_CPtpClockParentDSGMClockPriority1_Object = MibTableColumn
cPtpClockParentDSGMClockPriority1 = _CPtpClockParentDSGMClockPriority1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 2, 1, 9),
    _CPtpClockParentDSGMClockPriority1_Type()
)
cPtpClockParentDSGMClockPriority1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockParentDSGMClockPriority1.setStatus("current")
_CPtpClockParentDSGMClockPriority2_Type = Integer32
_CPtpClockParentDSGMClockPriority2_Object = MibTableColumn
cPtpClockParentDSGMClockPriority2 = _CPtpClockParentDSGMClockPriority2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 2, 1, 10),
    _CPtpClockParentDSGMClockPriority2_Type()
)
cPtpClockParentDSGMClockPriority2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockParentDSGMClockPriority2.setStatus("current")


class _CPtpClockParentDSGMClockQualityClass_Type(ClockQualityClassType):
    """Custom type cPtpClockParentDSGMClockQualityClass based on ClockQualityClassType"""
    subtypeSpec = ClockQualityClassType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CPtpClockParentDSGMClockQualityClass_Type.__name__ = "ClockQualityClassType"
_CPtpClockParentDSGMClockQualityClass_Object = MibTableColumn
cPtpClockParentDSGMClockQualityClass = _CPtpClockParentDSGMClockQualityClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 2, 1, 11),
    _CPtpClockParentDSGMClockQualityClass_Type()
)
cPtpClockParentDSGMClockQualityClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockParentDSGMClockQualityClass.setStatus("current")
_CPtpClockParentDSGMClockQualityAccuracy_Type = ClockQualityAccuracyType
_CPtpClockParentDSGMClockQualityAccuracy_Object = MibTableColumn
cPtpClockParentDSGMClockQualityAccuracy = _CPtpClockParentDSGMClockQualityAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 2, 1, 12),
    _CPtpClockParentDSGMClockQualityAccuracy_Type()
)
cPtpClockParentDSGMClockQualityAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockParentDSGMClockQualityAccuracy.setStatus("current")
_CPtpClockParentDSGMClockQualityOffset_Type = Unsigned32
_CPtpClockParentDSGMClockQualityOffset_Object = MibTableColumn
cPtpClockParentDSGMClockQualityOffset = _CPtpClockParentDSGMClockQualityOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 2, 1, 13),
    _CPtpClockParentDSGMClockQualityOffset_Type()
)
cPtpClockParentDSGMClockQualityOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockParentDSGMClockQualityOffset.setStatus("current")
_CPtpClockDefaultDSTable_Object = MibTable
cPtpClockDefaultDSTable = _CPtpClockDefaultDSTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cPtpClockDefaultDSTable.setStatus("current")
_CPtpClockDefaultDSEntry_Object = MibTableRow
cPtpClockDefaultDSEntry = _CPtpClockDefaultDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 3, 1)
)
cPtpClockDefaultDSEntry.setIndexNames(
    (0, "CISCO-PTP-MIB", "cPtpClockDefaultDSDomainIndex"),
    (0, "CISCO-PTP-MIB", "cPtpClockDefaultDSClockTypeIndex"),
    (0, "CISCO-PTP-MIB", "cPtpClockDefaultDSInstanceIndex"),
)
if mibBuilder.loadTexts:
    cPtpClockDefaultDSEntry.setStatus("current")
_CPtpClockDefaultDSDomainIndex_Type = ClockDomainType
_CPtpClockDefaultDSDomainIndex_Object = MibTableColumn
cPtpClockDefaultDSDomainIndex = _CPtpClockDefaultDSDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 3, 1, 1),
    _CPtpClockDefaultDSDomainIndex_Type()
)
cPtpClockDefaultDSDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockDefaultDSDomainIndex.setStatus("current")
_CPtpClockDefaultDSClockTypeIndex_Type = ClockType
_CPtpClockDefaultDSClockTypeIndex_Object = MibTableColumn
cPtpClockDefaultDSClockTypeIndex = _CPtpClockDefaultDSClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 3, 1, 2),
    _CPtpClockDefaultDSClockTypeIndex_Type()
)
cPtpClockDefaultDSClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockDefaultDSClockTypeIndex.setStatus("current")


class _CPtpClockDefaultDSInstanceIndex_Type(ClockInstanceType):
    """Custom type cPtpClockDefaultDSInstanceIndex based on ClockInstanceType"""
    subtypeSpec = ClockInstanceType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CPtpClockDefaultDSInstanceIndex_Type.__name__ = "ClockInstanceType"
_CPtpClockDefaultDSInstanceIndex_Object = MibTableColumn
cPtpClockDefaultDSInstanceIndex = _CPtpClockDefaultDSInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 3, 1, 3),
    _CPtpClockDefaultDSInstanceIndex_Type()
)
cPtpClockDefaultDSInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockDefaultDSInstanceIndex.setStatus("current")
_CPtpClockDefaultDSTwoStepFlag_Type = TruthValue
_CPtpClockDefaultDSTwoStepFlag_Object = MibTableColumn
cPtpClockDefaultDSTwoStepFlag = _CPtpClockDefaultDSTwoStepFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 3, 1, 4),
    _CPtpClockDefaultDSTwoStepFlag_Type()
)
cPtpClockDefaultDSTwoStepFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockDefaultDSTwoStepFlag.setStatus("current")
_CPtpClockDefaultDSClockIdentity_Type = ClockIdentity
_CPtpClockDefaultDSClockIdentity_Object = MibTableColumn
cPtpClockDefaultDSClockIdentity = _CPtpClockDefaultDSClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 3, 1, 5),
    _CPtpClockDefaultDSClockIdentity_Type()
)
cPtpClockDefaultDSClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockDefaultDSClockIdentity.setStatus("current")
_CPtpClockDefaultDSPriority1_Type = Integer32
_CPtpClockDefaultDSPriority1_Object = MibTableColumn
cPtpClockDefaultDSPriority1 = _CPtpClockDefaultDSPriority1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 3, 1, 6),
    _CPtpClockDefaultDSPriority1_Type()
)
cPtpClockDefaultDSPriority1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockDefaultDSPriority1.setStatus("current")
_CPtpClockDefaultDSPriority2_Type = Integer32
_CPtpClockDefaultDSPriority2_Object = MibTableColumn
cPtpClockDefaultDSPriority2 = _CPtpClockDefaultDSPriority2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 3, 1, 7),
    _CPtpClockDefaultDSPriority2_Type()
)
cPtpClockDefaultDSPriority2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockDefaultDSPriority2.setStatus("current")
_CPtpClockDefaultDSSlaveOnly_Type = TruthValue
_CPtpClockDefaultDSSlaveOnly_Object = MibTableColumn
cPtpClockDefaultDSSlaveOnly = _CPtpClockDefaultDSSlaveOnly_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 3, 1, 8),
    _CPtpClockDefaultDSSlaveOnly_Type()
)
cPtpClockDefaultDSSlaveOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockDefaultDSSlaveOnly.setStatus("current")


class _CPtpClockDefaultDSQualityClass_Type(ClockQualityClassType):
    """Custom type cPtpClockDefaultDSQualityClass based on ClockQualityClassType"""
    subtypeSpec = ClockQualityClassType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CPtpClockDefaultDSQualityClass_Type.__name__ = "ClockQualityClassType"
_CPtpClockDefaultDSQualityClass_Object = MibTableColumn
cPtpClockDefaultDSQualityClass = _CPtpClockDefaultDSQualityClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 3, 1, 9),
    _CPtpClockDefaultDSQualityClass_Type()
)
cPtpClockDefaultDSQualityClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockDefaultDSQualityClass.setStatus("current")
_CPtpClockDefaultDSQualityAccuracy_Type = ClockQualityAccuracyType
_CPtpClockDefaultDSQualityAccuracy_Object = MibTableColumn
cPtpClockDefaultDSQualityAccuracy = _CPtpClockDefaultDSQualityAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 3, 1, 10),
    _CPtpClockDefaultDSQualityAccuracy_Type()
)
cPtpClockDefaultDSQualityAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockDefaultDSQualityAccuracy.setStatus("current")
_CPtpClockDefaultDSQualityOffset_Type = Integer32
_CPtpClockDefaultDSQualityOffset_Object = MibTableColumn
cPtpClockDefaultDSQualityOffset = _CPtpClockDefaultDSQualityOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 3, 1, 11),
    _CPtpClockDefaultDSQualityOffset_Type()
)
cPtpClockDefaultDSQualityOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockDefaultDSQualityOffset.setStatus("current")
_CPtpClockRunningTable_Object = MibTable
cPtpClockRunningTable = _CPtpClockRunningTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cPtpClockRunningTable.setStatus("current")
_CPtpClockRunningEntry_Object = MibTableRow
cPtpClockRunningEntry = _CPtpClockRunningEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 4, 1)
)
cPtpClockRunningEntry.setIndexNames(
    (0, "CISCO-PTP-MIB", "cPtpClockRunningDomainIndex"),
    (0, "CISCO-PTP-MIB", "cPtpClockRunningClockTypeIndex"),
    (0, "CISCO-PTP-MIB", "cPtpClockRunningInstanceIndex"),
)
if mibBuilder.loadTexts:
    cPtpClockRunningEntry.setStatus("current")
_CPtpClockRunningDomainIndex_Type = ClockDomainType
_CPtpClockRunningDomainIndex_Object = MibTableColumn
cPtpClockRunningDomainIndex = _CPtpClockRunningDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 4, 1, 1),
    _CPtpClockRunningDomainIndex_Type()
)
cPtpClockRunningDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockRunningDomainIndex.setStatus("current")
_CPtpClockRunningClockTypeIndex_Type = ClockType
_CPtpClockRunningClockTypeIndex_Object = MibTableColumn
cPtpClockRunningClockTypeIndex = _CPtpClockRunningClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 4, 1, 2),
    _CPtpClockRunningClockTypeIndex_Type()
)
cPtpClockRunningClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockRunningClockTypeIndex.setStatus("current")


class _CPtpClockRunningInstanceIndex_Type(ClockInstanceType):
    """Custom type cPtpClockRunningInstanceIndex based on ClockInstanceType"""
    subtypeSpec = ClockInstanceType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CPtpClockRunningInstanceIndex_Type.__name__ = "ClockInstanceType"
_CPtpClockRunningInstanceIndex_Object = MibTableColumn
cPtpClockRunningInstanceIndex = _CPtpClockRunningInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 4, 1, 3),
    _CPtpClockRunningInstanceIndex_Type()
)
cPtpClockRunningInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockRunningInstanceIndex.setStatus("current")
_CPtpClockRunningState_Type = ClockStateType
_CPtpClockRunningState_Object = MibTableColumn
cPtpClockRunningState = _CPtpClockRunningState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 4, 1, 4),
    _CPtpClockRunningState_Type()
)
cPtpClockRunningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockRunningState.setStatus("current")
_CPtpClockRunningPacketsSent_Type = Counter64
_CPtpClockRunningPacketsSent_Object = MibTableColumn
cPtpClockRunningPacketsSent = _CPtpClockRunningPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 4, 1, 5),
    _CPtpClockRunningPacketsSent_Type()
)
cPtpClockRunningPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockRunningPacketsSent.setStatus("current")
_CPtpClockRunningPacketsReceived_Type = Counter64
_CPtpClockRunningPacketsReceived_Object = MibTableColumn
cPtpClockRunningPacketsReceived = _CPtpClockRunningPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 4, 1, 6),
    _CPtpClockRunningPacketsReceived_Type()
)
cPtpClockRunningPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockRunningPacketsReceived.setStatus("current")
_CPtpClockTimePropertiesDSTable_Object = MibTable
cPtpClockTimePropertiesDSTable = _CPtpClockTimePropertiesDSTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cPtpClockTimePropertiesDSTable.setStatus("current")
_CPtpClockTimePropertiesDSEntry_Object = MibTableRow
cPtpClockTimePropertiesDSEntry = _CPtpClockTimePropertiesDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 5, 1)
)
cPtpClockTimePropertiesDSEntry.setIndexNames(
    (0, "CISCO-PTP-MIB", "cPtpClockTimePropertiesDSDomainIndex"),
    (0, "CISCO-PTP-MIB", "cPtpClockTimePropertiesDSClockTypeIndex"),
    (0, "CISCO-PTP-MIB", "cPtpClockTimePropertiesDSInstanceIndex"),
)
if mibBuilder.loadTexts:
    cPtpClockTimePropertiesDSEntry.setStatus("current")
_CPtpClockTimePropertiesDSDomainIndex_Type = ClockDomainType
_CPtpClockTimePropertiesDSDomainIndex_Object = MibTableColumn
cPtpClockTimePropertiesDSDomainIndex = _CPtpClockTimePropertiesDSDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 5, 1, 1),
    _CPtpClockTimePropertiesDSDomainIndex_Type()
)
cPtpClockTimePropertiesDSDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockTimePropertiesDSDomainIndex.setStatus("current")
_CPtpClockTimePropertiesDSClockTypeIndex_Type = ClockType
_CPtpClockTimePropertiesDSClockTypeIndex_Object = MibTableColumn
cPtpClockTimePropertiesDSClockTypeIndex = _CPtpClockTimePropertiesDSClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 5, 1, 2),
    _CPtpClockTimePropertiesDSClockTypeIndex_Type()
)
cPtpClockTimePropertiesDSClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockTimePropertiesDSClockTypeIndex.setStatus("current")


class _CPtpClockTimePropertiesDSInstanceIndex_Type(ClockInstanceType):
    """Custom type cPtpClockTimePropertiesDSInstanceIndex based on ClockInstanceType"""
    subtypeSpec = ClockInstanceType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CPtpClockTimePropertiesDSInstanceIndex_Type.__name__ = "ClockInstanceType"
_CPtpClockTimePropertiesDSInstanceIndex_Object = MibTableColumn
cPtpClockTimePropertiesDSInstanceIndex = _CPtpClockTimePropertiesDSInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 5, 1, 3),
    _CPtpClockTimePropertiesDSInstanceIndex_Type()
)
cPtpClockTimePropertiesDSInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockTimePropertiesDSInstanceIndex.setStatus("current")
_CPtpClockTimePropertiesDSCurrentUTCOffsetValid_Type = TruthValue
_CPtpClockTimePropertiesDSCurrentUTCOffsetValid_Object = MibTableColumn
cPtpClockTimePropertiesDSCurrentUTCOffsetValid = _CPtpClockTimePropertiesDSCurrentUTCOffsetValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 5, 1, 4),
    _CPtpClockTimePropertiesDSCurrentUTCOffsetValid_Type()
)
cPtpClockTimePropertiesDSCurrentUTCOffsetValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockTimePropertiesDSCurrentUTCOffsetValid.setStatus("current")
_CPtpClockTimePropertiesDSCurrentUTCOffset_Type = Integer32
_CPtpClockTimePropertiesDSCurrentUTCOffset_Object = MibTableColumn
cPtpClockTimePropertiesDSCurrentUTCOffset = _CPtpClockTimePropertiesDSCurrentUTCOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 5, 1, 5),
    _CPtpClockTimePropertiesDSCurrentUTCOffset_Type()
)
cPtpClockTimePropertiesDSCurrentUTCOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockTimePropertiesDSCurrentUTCOffset.setStatus("current")
_CPtpClockTimePropertiesDSLeap59_Type = TruthValue
_CPtpClockTimePropertiesDSLeap59_Object = MibTableColumn
cPtpClockTimePropertiesDSLeap59 = _CPtpClockTimePropertiesDSLeap59_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 5, 1, 6),
    _CPtpClockTimePropertiesDSLeap59_Type()
)
cPtpClockTimePropertiesDSLeap59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockTimePropertiesDSLeap59.setStatus("current")
_CPtpClockTimePropertiesDSLeap61_Type = TruthValue
_CPtpClockTimePropertiesDSLeap61_Object = MibTableColumn
cPtpClockTimePropertiesDSLeap61 = _CPtpClockTimePropertiesDSLeap61_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 5, 1, 7),
    _CPtpClockTimePropertiesDSLeap61_Type()
)
cPtpClockTimePropertiesDSLeap61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockTimePropertiesDSLeap61.setStatus("current")
_CPtpClockTimePropertiesDSTimeTraceable_Type = TruthValue
_CPtpClockTimePropertiesDSTimeTraceable_Object = MibTableColumn
cPtpClockTimePropertiesDSTimeTraceable = _CPtpClockTimePropertiesDSTimeTraceable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 5, 1, 8),
    _CPtpClockTimePropertiesDSTimeTraceable_Type()
)
cPtpClockTimePropertiesDSTimeTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockTimePropertiesDSTimeTraceable.setStatus("current")
_CPtpClockTimePropertiesDSFreqTraceable_Type = TruthValue
_CPtpClockTimePropertiesDSFreqTraceable_Object = MibTableColumn
cPtpClockTimePropertiesDSFreqTraceable = _CPtpClockTimePropertiesDSFreqTraceable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 5, 1, 9),
    _CPtpClockTimePropertiesDSFreqTraceable_Type()
)
cPtpClockTimePropertiesDSFreqTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockTimePropertiesDSFreqTraceable.setStatus("current")
_CPtpClockTimePropertiesDSPTPTimescale_Type = TruthValue
_CPtpClockTimePropertiesDSPTPTimescale_Object = MibTableColumn
cPtpClockTimePropertiesDSPTPTimescale = _CPtpClockTimePropertiesDSPTPTimescale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 5, 1, 10),
    _CPtpClockTimePropertiesDSPTPTimescale_Type()
)
cPtpClockTimePropertiesDSPTPTimescale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockTimePropertiesDSPTPTimescale.setStatus("current")
_CPtpClockTimePropertiesDSSource_Type = ClockTimeSourceType
_CPtpClockTimePropertiesDSSource_Object = MibTableColumn
cPtpClockTimePropertiesDSSource = _CPtpClockTimePropertiesDSSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 5, 1, 11),
    _CPtpClockTimePropertiesDSSource_Type()
)
cPtpClockTimePropertiesDSSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockTimePropertiesDSSource.setStatus("current")
_CPtpClockTransDefaultDSTable_Object = MibTable
cPtpClockTransDefaultDSTable = _CPtpClockTransDefaultDSTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cPtpClockTransDefaultDSTable.setStatus("current")
_CPtpClockTransDefaultDSEntry_Object = MibTableRow
cPtpClockTransDefaultDSEntry = _CPtpClockTransDefaultDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 6, 1)
)
cPtpClockTransDefaultDSEntry.setIndexNames(
    (0, "CISCO-PTP-MIB", "cPtpClockTransDefaultDSDomainIndex"),
    (0, "CISCO-PTP-MIB", "cPtpClockTransDefaultDSInstanceIndex"),
)
if mibBuilder.loadTexts:
    cPtpClockTransDefaultDSEntry.setStatus("current")
_CPtpClockTransDefaultDSDomainIndex_Type = ClockDomainType
_CPtpClockTransDefaultDSDomainIndex_Object = MibTableColumn
cPtpClockTransDefaultDSDomainIndex = _CPtpClockTransDefaultDSDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 6, 1, 1),
    _CPtpClockTransDefaultDSDomainIndex_Type()
)
cPtpClockTransDefaultDSDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockTransDefaultDSDomainIndex.setStatus("current")


class _CPtpClockTransDefaultDSInstanceIndex_Type(ClockInstanceType):
    """Custom type cPtpClockTransDefaultDSInstanceIndex based on ClockInstanceType"""
    subtypeSpec = ClockInstanceType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CPtpClockTransDefaultDSInstanceIndex_Type.__name__ = "ClockInstanceType"
_CPtpClockTransDefaultDSInstanceIndex_Object = MibTableColumn
cPtpClockTransDefaultDSInstanceIndex = _CPtpClockTransDefaultDSInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 6, 1, 2),
    _CPtpClockTransDefaultDSInstanceIndex_Type()
)
cPtpClockTransDefaultDSInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockTransDefaultDSInstanceIndex.setStatus("current")
_CPtpClockTransDefaultDSClockIdentity_Type = ClockIdentity
_CPtpClockTransDefaultDSClockIdentity_Object = MibTableColumn
cPtpClockTransDefaultDSClockIdentity = _CPtpClockTransDefaultDSClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 6, 1, 3),
    _CPtpClockTransDefaultDSClockIdentity_Type()
)
cPtpClockTransDefaultDSClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockTransDefaultDSClockIdentity.setStatus("current")
_CPtpClockTransDefaultDSNumOfPorts_Type = Counter32
_CPtpClockTransDefaultDSNumOfPorts_Object = MibTableColumn
cPtpClockTransDefaultDSNumOfPorts = _CPtpClockTransDefaultDSNumOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 6, 1, 4),
    _CPtpClockTransDefaultDSNumOfPorts_Type()
)
cPtpClockTransDefaultDSNumOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockTransDefaultDSNumOfPorts.setStatus("current")
_CPtpClockTransDefaultDSDelay_Type = ClockMechanismType
_CPtpClockTransDefaultDSDelay_Object = MibTableColumn
cPtpClockTransDefaultDSDelay = _CPtpClockTransDefaultDSDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 6, 1, 5),
    _CPtpClockTransDefaultDSDelay_Type()
)
cPtpClockTransDefaultDSDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockTransDefaultDSDelay.setStatus("current")
_CPtpClockTransDefaultDSPrimaryDomain_Type = Integer32
_CPtpClockTransDefaultDSPrimaryDomain_Object = MibTableColumn
cPtpClockTransDefaultDSPrimaryDomain = _CPtpClockTransDefaultDSPrimaryDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 6, 1, 6),
    _CPtpClockTransDefaultDSPrimaryDomain_Type()
)
cPtpClockTransDefaultDSPrimaryDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockTransDefaultDSPrimaryDomain.setStatus("current")
_CPtpClockPortTable_Object = MibTable
cPtpClockPortTable = _CPtpClockPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 7)
)
if mibBuilder.loadTexts:
    cPtpClockPortTable.setStatus("current")
_CPtpClockPortEntry_Object = MibTableRow
cPtpClockPortEntry = _CPtpClockPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 7, 1)
)
cPtpClockPortEntry.setIndexNames(
    (0, "CISCO-PTP-MIB", "cPtpClockPortDomainIndex"),
    (0, "CISCO-PTP-MIB", "cPtpClockPortClockTypeIndex"),
    (0, "CISCO-PTP-MIB", "cPtpClockPortClockInstanceIndex"),
    (0, "CISCO-PTP-MIB", "cPtpClockPortTablePortNumberIndex"),
)
if mibBuilder.loadTexts:
    cPtpClockPortEntry.setStatus("current")
_CPtpClockPortDomainIndex_Type = ClockDomainType
_CPtpClockPortDomainIndex_Object = MibTableColumn
cPtpClockPortDomainIndex = _CPtpClockPortDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 7, 1, 1),
    _CPtpClockPortDomainIndex_Type()
)
cPtpClockPortDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockPortDomainIndex.setStatus("current")
_CPtpClockPortClockTypeIndex_Type = ClockType
_CPtpClockPortClockTypeIndex_Object = MibTableColumn
cPtpClockPortClockTypeIndex = _CPtpClockPortClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 7, 1, 2),
    _CPtpClockPortClockTypeIndex_Type()
)
cPtpClockPortClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockPortClockTypeIndex.setStatus("current")


class _CPtpClockPortClockInstanceIndex_Type(ClockInstanceType):
    """Custom type cPtpClockPortClockInstanceIndex based on ClockInstanceType"""
    subtypeSpec = ClockInstanceType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CPtpClockPortClockInstanceIndex_Type.__name__ = "ClockInstanceType"
_CPtpClockPortClockInstanceIndex_Object = MibTableColumn
cPtpClockPortClockInstanceIndex = _CPtpClockPortClockInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 7, 1, 3),
    _CPtpClockPortClockInstanceIndex_Type()
)
cPtpClockPortClockInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockPortClockInstanceIndex.setStatus("current")


class _CPtpClockPortTablePortNumberIndex_Type(ClockPortNumber):
    """Custom type cPtpClockPortTablePortNumberIndex based on ClockPortNumber"""
    subtypeSpec = ClockPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CPtpClockPortTablePortNumberIndex_Type.__name__ = "ClockPortNumber"
_CPtpClockPortTablePortNumberIndex_Object = MibTableColumn
cPtpClockPortTablePortNumberIndex = _CPtpClockPortTablePortNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 7, 1, 4),
    _CPtpClockPortTablePortNumberIndex_Type()
)
cPtpClockPortTablePortNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockPortTablePortNumberIndex.setStatus("current")


class _CPtpClockPortName_Type(DisplayString):
    """Custom type cPtpClockPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CPtpClockPortName_Type.__name__ = "DisplayString"
_CPtpClockPortName_Object = MibTableColumn
cPtpClockPortName = _CPtpClockPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 7, 1, 5),
    _CPtpClockPortName_Type()
)
cPtpClockPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortName.setStatus("current")
_CPtpClockPortRole_Type = ClockRoleType
_CPtpClockPortRole_Object = MibTableColumn
cPtpClockPortRole = _CPtpClockPortRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 7, 1, 6),
    _CPtpClockPortRole_Type()
)
cPtpClockPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortRole.setStatus("current")
_CPtpClockPortSyncOneStep_Type = TruthValue
_CPtpClockPortSyncOneStep_Object = MibTableColumn
cPtpClockPortSyncOneStep = _CPtpClockPortSyncOneStep_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 7, 1, 7),
    _CPtpClockPortSyncOneStep_Type()
)
cPtpClockPortSyncOneStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortSyncOneStep.setStatus("current")
_CPtpClockPortCurrentPeerAddressType_Type = InetAddressType
_CPtpClockPortCurrentPeerAddressType_Object = MibTableColumn
cPtpClockPortCurrentPeerAddressType = _CPtpClockPortCurrentPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 7, 1, 8),
    _CPtpClockPortCurrentPeerAddressType_Type()
)
cPtpClockPortCurrentPeerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortCurrentPeerAddressType.setStatus("current")
_CPtpClockPortCurrentPeerAddress_Type = InetAddress
_CPtpClockPortCurrentPeerAddress_Object = MibTableColumn
cPtpClockPortCurrentPeerAddress = _CPtpClockPortCurrentPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 7, 1, 9),
    _CPtpClockPortCurrentPeerAddress_Type()
)
cPtpClockPortCurrentPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortCurrentPeerAddress.setStatus("current")
_CPtpClockPortNumOfAssociatedPorts_Type = Gauge32
_CPtpClockPortNumOfAssociatedPorts_Object = MibTableColumn
cPtpClockPortNumOfAssociatedPorts = _CPtpClockPortNumOfAssociatedPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 7, 1, 10),
    _CPtpClockPortNumOfAssociatedPorts_Type()
)
cPtpClockPortNumOfAssociatedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortNumOfAssociatedPorts.setStatus("current")
_CPtpClockPortDSTable_Object = MibTable
cPtpClockPortDSTable = _CPtpClockPortDSTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 8)
)
if mibBuilder.loadTexts:
    cPtpClockPortDSTable.setStatus("current")
_CPtpClockPortDSEntry_Object = MibTableRow
cPtpClockPortDSEntry = _CPtpClockPortDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 8, 1)
)
cPtpClockPortDSEntry.setIndexNames(
    (0, "CISCO-PTP-MIB", "cPtpClockPortDSDomainIndex"),
    (0, "CISCO-PTP-MIB", "cPtpClockPortDSClockTypeIndex"),
    (0, "CISCO-PTP-MIB", "cPtpClockPortDSClockInstanceIndex"),
    (0, "CISCO-PTP-MIB", "cPtpClockPortDSPortNumberIndex"),
)
if mibBuilder.loadTexts:
    cPtpClockPortDSEntry.setStatus("current")
_CPtpClockPortDSDomainIndex_Type = ClockDomainType
_CPtpClockPortDSDomainIndex_Object = MibTableColumn
cPtpClockPortDSDomainIndex = _CPtpClockPortDSDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 8, 1, 1),
    _CPtpClockPortDSDomainIndex_Type()
)
cPtpClockPortDSDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockPortDSDomainIndex.setStatus("current")
_CPtpClockPortDSClockTypeIndex_Type = ClockType
_CPtpClockPortDSClockTypeIndex_Object = MibTableColumn
cPtpClockPortDSClockTypeIndex = _CPtpClockPortDSClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 8, 1, 2),
    _CPtpClockPortDSClockTypeIndex_Type()
)
cPtpClockPortDSClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockPortDSClockTypeIndex.setStatus("current")


class _CPtpClockPortDSClockInstanceIndex_Type(ClockInstanceType):
    """Custom type cPtpClockPortDSClockInstanceIndex based on ClockInstanceType"""
    subtypeSpec = ClockInstanceType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CPtpClockPortDSClockInstanceIndex_Type.__name__ = "ClockInstanceType"
_CPtpClockPortDSClockInstanceIndex_Object = MibTableColumn
cPtpClockPortDSClockInstanceIndex = _CPtpClockPortDSClockInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 8, 1, 3),
    _CPtpClockPortDSClockInstanceIndex_Type()
)
cPtpClockPortDSClockInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockPortDSClockInstanceIndex.setStatus("current")


class _CPtpClockPortDSPortNumberIndex_Type(ClockPortNumber):
    """Custom type cPtpClockPortDSPortNumberIndex based on ClockPortNumber"""
    subtypeSpec = ClockPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CPtpClockPortDSPortNumberIndex_Type.__name__ = "ClockPortNumber"
_CPtpClockPortDSPortNumberIndex_Object = MibTableColumn
cPtpClockPortDSPortNumberIndex = _CPtpClockPortDSPortNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 8, 1, 4),
    _CPtpClockPortDSPortNumberIndex_Type()
)
cPtpClockPortDSPortNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockPortDSPortNumberIndex.setStatus("current")


class _CPtpClockPortDSName_Type(DisplayString):
    """Custom type cPtpClockPortDSName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CPtpClockPortDSName_Type.__name__ = "DisplayString"
_CPtpClockPortDSName_Object = MibTableColumn
cPtpClockPortDSName = _CPtpClockPortDSName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 8, 1, 5),
    _CPtpClockPortDSName_Type()
)
cPtpClockPortDSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortDSName.setStatus("current")
_CPtpClockPortDSPortIdentity_Type = OctetString
_CPtpClockPortDSPortIdentity_Object = MibTableColumn
cPtpClockPortDSPortIdentity = _CPtpClockPortDSPortIdentity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 8, 1, 6),
    _CPtpClockPortDSPortIdentity_Type()
)
cPtpClockPortDSPortIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortDSPortIdentity.setStatus("current")
_CPtpClockPortDSAnnouncementInterval_Type = Integer32
_CPtpClockPortDSAnnouncementInterval_Object = MibTableColumn
cPtpClockPortDSAnnouncementInterval = _CPtpClockPortDSAnnouncementInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 8, 1, 7),
    _CPtpClockPortDSAnnouncementInterval_Type()
)
cPtpClockPortDSAnnouncementInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortDSAnnouncementInterval.setStatus("current")
_CPtpClockPortDSAnnounceRctTimeout_Type = Integer32
_CPtpClockPortDSAnnounceRctTimeout_Object = MibTableColumn
cPtpClockPortDSAnnounceRctTimeout = _CPtpClockPortDSAnnounceRctTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 8, 1, 8),
    _CPtpClockPortDSAnnounceRctTimeout_Type()
)
cPtpClockPortDSAnnounceRctTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortDSAnnounceRctTimeout.setStatus("current")
_CPtpClockPortDSSyncInterval_Type = Integer32
_CPtpClockPortDSSyncInterval_Object = MibTableColumn
cPtpClockPortDSSyncInterval = _CPtpClockPortDSSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 8, 1, 9),
    _CPtpClockPortDSSyncInterval_Type()
)
cPtpClockPortDSSyncInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortDSSyncInterval.setStatus("current")
_CPtpClockPortDSMinDelayReqInterval_Type = Integer32
_CPtpClockPortDSMinDelayReqInterval_Object = MibTableColumn
cPtpClockPortDSMinDelayReqInterval = _CPtpClockPortDSMinDelayReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 8, 1, 10),
    _CPtpClockPortDSMinDelayReqInterval_Type()
)
cPtpClockPortDSMinDelayReqInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortDSMinDelayReqInterval.setStatus("current")
_CPtpClockPortDSPeerDelayReqInterval_Type = Integer32
_CPtpClockPortDSPeerDelayReqInterval_Object = MibTableColumn
cPtpClockPortDSPeerDelayReqInterval = _CPtpClockPortDSPeerDelayReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 8, 1, 11),
    _CPtpClockPortDSPeerDelayReqInterval_Type()
)
cPtpClockPortDSPeerDelayReqInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortDSPeerDelayReqInterval.setStatus("current")
_CPtpClockPortDSDelayMech_Type = ClockMechanismType
_CPtpClockPortDSDelayMech_Object = MibTableColumn
cPtpClockPortDSDelayMech = _CPtpClockPortDSDelayMech_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 8, 1, 12),
    _CPtpClockPortDSDelayMech_Type()
)
cPtpClockPortDSDelayMech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortDSDelayMech.setStatus("current")
_CPtpClockPortDSPeerMeanPathDelay_Type = ClockTimeInterval
_CPtpClockPortDSPeerMeanPathDelay_Object = MibTableColumn
cPtpClockPortDSPeerMeanPathDelay = _CPtpClockPortDSPeerMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 8, 1, 13),
    _CPtpClockPortDSPeerMeanPathDelay_Type()
)
cPtpClockPortDSPeerMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortDSPeerMeanPathDelay.setStatus("current")
_CPtpClockPortDSGrantDuration_Type = Unsigned32
_CPtpClockPortDSGrantDuration_Object = MibTableColumn
cPtpClockPortDSGrantDuration = _CPtpClockPortDSGrantDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 8, 1, 14),
    _CPtpClockPortDSGrantDuration_Type()
)
cPtpClockPortDSGrantDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortDSGrantDuration.setStatus("current")
_CPtpClockPortDSPTPVersion_Type = Integer32
_CPtpClockPortDSPTPVersion_Object = MibTableColumn
cPtpClockPortDSPTPVersion = _CPtpClockPortDSPTPVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 8, 1, 15),
    _CPtpClockPortDSPTPVersion_Type()
)
cPtpClockPortDSPTPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortDSPTPVersion.setStatus("current")
_CPtpClockPortRunningTable_Object = MibTable
cPtpClockPortRunningTable = _CPtpClockPortRunningTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 9)
)
if mibBuilder.loadTexts:
    cPtpClockPortRunningTable.setStatus("current")
_CPtpClockPortRunningEntry_Object = MibTableRow
cPtpClockPortRunningEntry = _CPtpClockPortRunningEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 9, 1)
)
cPtpClockPortRunningEntry.setIndexNames(
    (0, "CISCO-PTP-MIB", "cPtpClockPortRunningDomainIndex"),
    (0, "CISCO-PTP-MIB", "cPtpClockPortRunningClockTypeIndex"),
    (0, "CISCO-PTP-MIB", "cPtpClockPortRunningClockInstanceIndex"),
    (0, "CISCO-PTP-MIB", "cPtpClockPortRunningPortNumberIndex"),
)
if mibBuilder.loadTexts:
    cPtpClockPortRunningEntry.setStatus("current")
_CPtpClockPortRunningDomainIndex_Type = ClockDomainType
_CPtpClockPortRunningDomainIndex_Object = MibTableColumn
cPtpClockPortRunningDomainIndex = _CPtpClockPortRunningDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 9, 1, 1),
    _CPtpClockPortRunningDomainIndex_Type()
)
cPtpClockPortRunningDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockPortRunningDomainIndex.setStatus("current")
_CPtpClockPortRunningClockTypeIndex_Type = ClockType
_CPtpClockPortRunningClockTypeIndex_Object = MibTableColumn
cPtpClockPortRunningClockTypeIndex = _CPtpClockPortRunningClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 9, 1, 2),
    _CPtpClockPortRunningClockTypeIndex_Type()
)
cPtpClockPortRunningClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockPortRunningClockTypeIndex.setStatus("current")


class _CPtpClockPortRunningClockInstanceIndex_Type(ClockInstanceType):
    """Custom type cPtpClockPortRunningClockInstanceIndex based on ClockInstanceType"""
    subtypeSpec = ClockInstanceType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CPtpClockPortRunningClockInstanceIndex_Type.__name__ = "ClockInstanceType"
_CPtpClockPortRunningClockInstanceIndex_Object = MibTableColumn
cPtpClockPortRunningClockInstanceIndex = _CPtpClockPortRunningClockInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 9, 1, 3),
    _CPtpClockPortRunningClockInstanceIndex_Type()
)
cPtpClockPortRunningClockInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockPortRunningClockInstanceIndex.setStatus("current")


class _CPtpClockPortRunningPortNumberIndex_Type(ClockPortNumber):
    """Custom type cPtpClockPortRunningPortNumberIndex based on ClockPortNumber"""
    subtypeSpec = ClockPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CPtpClockPortRunningPortNumberIndex_Type.__name__ = "ClockPortNumber"
_CPtpClockPortRunningPortNumberIndex_Object = MibTableColumn
cPtpClockPortRunningPortNumberIndex = _CPtpClockPortRunningPortNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 9, 1, 4),
    _CPtpClockPortRunningPortNumberIndex_Type()
)
cPtpClockPortRunningPortNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockPortRunningPortNumberIndex.setStatus("current")


class _CPtpClockPortRunningName_Type(DisplayString):
    """Custom type cPtpClockPortRunningName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CPtpClockPortRunningName_Type.__name__ = "DisplayString"
_CPtpClockPortRunningName_Object = MibTableColumn
cPtpClockPortRunningName = _CPtpClockPortRunningName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 9, 1, 5),
    _CPtpClockPortRunningName_Type()
)
cPtpClockPortRunningName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortRunningName.setStatus("current")
_CPtpClockPortRunningState_Type = ClockPortState
_CPtpClockPortRunningState_Object = MibTableColumn
cPtpClockPortRunningState = _CPtpClockPortRunningState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 9, 1, 6),
    _CPtpClockPortRunningState_Type()
)
cPtpClockPortRunningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortRunningState.setStatus("current")
_CPtpClockPortRunningRole_Type = ClockRoleType
_CPtpClockPortRunningRole_Object = MibTableColumn
cPtpClockPortRunningRole = _CPtpClockPortRunningRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 9, 1, 7),
    _CPtpClockPortRunningRole_Type()
)
cPtpClockPortRunningRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortRunningRole.setStatus("current")
_CPtpClockPortRunningInterfaceIndex_Type = InterfaceIndexOrZero
_CPtpClockPortRunningInterfaceIndex_Object = MibTableColumn
cPtpClockPortRunningInterfaceIndex = _CPtpClockPortRunningInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 9, 1, 8),
    _CPtpClockPortRunningInterfaceIndex_Type()
)
cPtpClockPortRunningInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortRunningInterfaceIndex.setStatus("current")
_CPtpClockPortRunningIPversion_Type = Integer32
_CPtpClockPortRunningIPversion_Object = MibTableColumn
cPtpClockPortRunningIPversion = _CPtpClockPortRunningIPversion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 9, 1, 9),
    _CPtpClockPortRunningIPversion_Type()
)
cPtpClockPortRunningIPversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortRunningIPversion.setStatus("current")
_CPtpClockPortRunningEncapsulationType_Type = Integer32
_CPtpClockPortRunningEncapsulationType_Object = MibTableColumn
cPtpClockPortRunningEncapsulationType = _CPtpClockPortRunningEncapsulationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 9, 1, 10),
    _CPtpClockPortRunningEncapsulationType_Type()
)
cPtpClockPortRunningEncapsulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortRunningEncapsulationType.setStatus("current")
_CPtpClockPortRunningTxMode_Type = ClockTxModeType
_CPtpClockPortRunningTxMode_Object = MibTableColumn
cPtpClockPortRunningTxMode = _CPtpClockPortRunningTxMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 9, 1, 11),
    _CPtpClockPortRunningTxMode_Type()
)
cPtpClockPortRunningTxMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortRunningTxMode.setStatus("current")
_CPtpClockPortRunningRxMode_Type = ClockTxModeType
_CPtpClockPortRunningRxMode_Object = MibTableColumn
cPtpClockPortRunningRxMode = _CPtpClockPortRunningRxMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 9, 1, 12),
    _CPtpClockPortRunningRxMode_Type()
)
cPtpClockPortRunningRxMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortRunningRxMode.setStatus("current")
_CPtpClockPortRunningPacketsReceived_Type = Counter64
_CPtpClockPortRunningPacketsReceived_Object = MibTableColumn
cPtpClockPortRunningPacketsReceived = _CPtpClockPortRunningPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 9, 1, 13),
    _CPtpClockPortRunningPacketsReceived_Type()
)
cPtpClockPortRunningPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortRunningPacketsReceived.setStatus("current")
if mibBuilder.loadTexts:
    cPtpClockPortRunningPacketsReceived.setUnits("packets")
_CPtpClockPortRunningPacketsSent_Type = Counter64
_CPtpClockPortRunningPacketsSent_Object = MibTableColumn
cPtpClockPortRunningPacketsSent = _CPtpClockPortRunningPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 9, 1, 14),
    _CPtpClockPortRunningPacketsSent_Type()
)
cPtpClockPortRunningPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortRunningPacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    cPtpClockPortRunningPacketsSent.setUnits("packets")
_CPtpClockPortTransDSTable_Object = MibTable
cPtpClockPortTransDSTable = _CPtpClockPortTransDSTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 10)
)
if mibBuilder.loadTexts:
    cPtpClockPortTransDSTable.setStatus("current")
_CPtpClockPortTransDSEntry_Object = MibTableRow
cPtpClockPortTransDSEntry = _CPtpClockPortTransDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 10, 1)
)
cPtpClockPortTransDSEntry.setIndexNames(
    (0, "CISCO-PTP-MIB", "cPtpClockPortTransDSDomainIndex"),
    (0, "CISCO-PTP-MIB", "cPtpClockPortTransDSInstanceIndex"),
    (0, "CISCO-PTP-MIB", "cPtpClockPortTransDSPortNumberIndex"),
)
if mibBuilder.loadTexts:
    cPtpClockPortTransDSEntry.setStatus("current")
_CPtpClockPortTransDSDomainIndex_Type = ClockDomainType
_CPtpClockPortTransDSDomainIndex_Object = MibTableColumn
cPtpClockPortTransDSDomainIndex = _CPtpClockPortTransDSDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 10, 1, 1),
    _CPtpClockPortTransDSDomainIndex_Type()
)
cPtpClockPortTransDSDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockPortTransDSDomainIndex.setStatus("current")


class _CPtpClockPortTransDSInstanceIndex_Type(ClockInstanceType):
    """Custom type cPtpClockPortTransDSInstanceIndex based on ClockInstanceType"""
    subtypeSpec = ClockInstanceType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CPtpClockPortTransDSInstanceIndex_Type.__name__ = "ClockInstanceType"
_CPtpClockPortTransDSInstanceIndex_Object = MibTableColumn
cPtpClockPortTransDSInstanceIndex = _CPtpClockPortTransDSInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 10, 1, 2),
    _CPtpClockPortTransDSInstanceIndex_Type()
)
cPtpClockPortTransDSInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockPortTransDSInstanceIndex.setStatus("current")


class _CPtpClockPortTransDSPortNumberIndex_Type(ClockPortNumber):
    """Custom type cPtpClockPortTransDSPortNumberIndex based on ClockPortNumber"""
    subtypeSpec = ClockPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CPtpClockPortTransDSPortNumberIndex_Type.__name__ = "ClockPortNumber"
_CPtpClockPortTransDSPortNumberIndex_Object = MibTableColumn
cPtpClockPortTransDSPortNumberIndex = _CPtpClockPortTransDSPortNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 10, 1, 3),
    _CPtpClockPortTransDSPortNumberIndex_Type()
)
cPtpClockPortTransDSPortNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockPortTransDSPortNumberIndex.setStatus("current")
_CPtpClockPortTransDSPortIdentity_Type = ClockIdentity
_CPtpClockPortTransDSPortIdentity_Object = MibTableColumn
cPtpClockPortTransDSPortIdentity = _CPtpClockPortTransDSPortIdentity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 10, 1, 4),
    _CPtpClockPortTransDSPortIdentity_Type()
)
cPtpClockPortTransDSPortIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortTransDSPortIdentity.setStatus("current")
_CPtpClockPortTransDSlogMinPdelayReqInt_Type = Integer32
_CPtpClockPortTransDSlogMinPdelayReqInt_Object = MibTableColumn
cPtpClockPortTransDSlogMinPdelayReqInt = _CPtpClockPortTransDSlogMinPdelayReqInt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 10, 1, 5),
    _CPtpClockPortTransDSlogMinPdelayReqInt_Type()
)
cPtpClockPortTransDSlogMinPdelayReqInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortTransDSlogMinPdelayReqInt.setStatus("current")
_CPtpClockPortTransDSFaultyFlag_Type = TruthValue
_CPtpClockPortTransDSFaultyFlag_Object = MibTableColumn
cPtpClockPortTransDSFaultyFlag = _CPtpClockPortTransDSFaultyFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 10, 1, 6),
    _CPtpClockPortTransDSFaultyFlag_Type()
)
cPtpClockPortTransDSFaultyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortTransDSFaultyFlag.setStatus("current")
_CPtpClockPortTransDSPeerMeanPathDelay_Type = ClockTimeInterval
_CPtpClockPortTransDSPeerMeanPathDelay_Object = MibTableColumn
cPtpClockPortTransDSPeerMeanPathDelay = _CPtpClockPortTransDSPeerMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 10, 1, 7),
    _CPtpClockPortTransDSPeerMeanPathDelay_Type()
)
cPtpClockPortTransDSPeerMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortTransDSPeerMeanPathDelay.setStatus("current")
_CPtpClockPortAssociateTable_Object = MibTable
cPtpClockPortAssociateTable = _CPtpClockPortAssociateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 11)
)
if mibBuilder.loadTexts:
    cPtpClockPortAssociateTable.setStatus("current")
_CPtpClockPortAssociateEntry_Object = MibTableRow
cPtpClockPortAssociateEntry = _CPtpClockPortAssociateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 11, 1)
)
cPtpClockPortAssociateEntry.setIndexNames(
    (0, "CISCO-PTP-MIB", "cPtpClockPortCurrentDomainIndex"),
    (0, "CISCO-PTP-MIB", "cPtpClockPortCurrentClockTypeIndex"),
    (0, "CISCO-PTP-MIB", "cPtpClockPortCurrentClockInstanceIndex"),
    (0, "CISCO-PTP-MIB", "cPtpClockPortCurrentPortNumberIndex"),
    (0, "CISCO-PTP-MIB", "cPtpClockPortAssociatePortIndex"),
)
if mibBuilder.loadTexts:
    cPtpClockPortAssociateEntry.setStatus("current")
_CPtpClockPortCurrentDomainIndex_Type = ClockDomainType
_CPtpClockPortCurrentDomainIndex_Object = MibTableColumn
cPtpClockPortCurrentDomainIndex = _CPtpClockPortCurrentDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 11, 1, 1),
    _CPtpClockPortCurrentDomainIndex_Type()
)
cPtpClockPortCurrentDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockPortCurrentDomainIndex.setStatus("current")
_CPtpClockPortCurrentClockTypeIndex_Type = ClockType
_CPtpClockPortCurrentClockTypeIndex_Object = MibTableColumn
cPtpClockPortCurrentClockTypeIndex = _CPtpClockPortCurrentClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 11, 1, 2),
    _CPtpClockPortCurrentClockTypeIndex_Type()
)
cPtpClockPortCurrentClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockPortCurrentClockTypeIndex.setStatus("current")
_CPtpClockPortCurrentClockInstanceIndex_Type = ClockInstanceType
_CPtpClockPortCurrentClockInstanceIndex_Object = MibTableColumn
cPtpClockPortCurrentClockInstanceIndex = _CPtpClockPortCurrentClockInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 11, 1, 3),
    _CPtpClockPortCurrentClockInstanceIndex_Type()
)
cPtpClockPortCurrentClockInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockPortCurrentClockInstanceIndex.setStatus("current")
_CPtpClockPortCurrentPortNumberIndex_Type = ClockPortNumber
_CPtpClockPortCurrentPortNumberIndex_Object = MibTableColumn
cPtpClockPortCurrentPortNumberIndex = _CPtpClockPortCurrentPortNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 11, 1, 4),
    _CPtpClockPortCurrentPortNumberIndex_Type()
)
cPtpClockPortCurrentPortNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockPortCurrentPortNumberIndex.setStatus("current")


class _CPtpClockPortAssociatePortIndex_Type(Unsigned32):
    """Custom type cPtpClockPortAssociatePortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CPtpClockPortAssociatePortIndex_Type.__name__ = "Unsigned32"
_CPtpClockPortAssociatePortIndex_Object = MibTableColumn
cPtpClockPortAssociatePortIndex = _CPtpClockPortAssociatePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 11, 1, 5),
    _CPtpClockPortAssociatePortIndex_Type()
)
cPtpClockPortAssociatePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtpClockPortAssociatePortIndex.setStatus("current")
_CPtpClockPortAssociateAddressType_Type = InetAddressType
_CPtpClockPortAssociateAddressType_Object = MibTableColumn
cPtpClockPortAssociateAddressType = _CPtpClockPortAssociateAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 11, 1, 6),
    _CPtpClockPortAssociateAddressType_Type()
)
cPtpClockPortAssociateAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortAssociateAddressType.setStatus("current")
_CPtpClockPortAssociateAddress_Type = InetAddress
_CPtpClockPortAssociateAddress_Object = MibTableColumn
cPtpClockPortAssociateAddress = _CPtpClockPortAssociateAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 11, 1, 7),
    _CPtpClockPortAssociateAddress_Type()
)
cPtpClockPortAssociateAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortAssociateAddress.setStatus("current")
_CPtpClockPortAssociatePacketsSent_Type = Counter64
_CPtpClockPortAssociatePacketsSent_Object = MibTableColumn
cPtpClockPortAssociatePacketsSent = _CPtpClockPortAssociatePacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 11, 1, 8),
    _CPtpClockPortAssociatePacketsSent_Type()
)
cPtpClockPortAssociatePacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortAssociatePacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    cPtpClockPortAssociatePacketsSent.setUnits("packets")
_CPtpClockPortAssociatePacketsReceived_Type = Counter64
_CPtpClockPortAssociatePacketsReceived_Object = MibTableColumn
cPtpClockPortAssociatePacketsReceived = _CPtpClockPortAssociatePacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 11, 1, 9),
    _CPtpClockPortAssociatePacketsReceived_Type()
)
cPtpClockPortAssociatePacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortAssociatePacketsReceived.setStatus("current")
if mibBuilder.loadTexts:
    cPtpClockPortAssociatePacketsReceived.setUnits("packets")
_CPtpClockPortAssociateInErrors_Type = Counter64
_CPtpClockPortAssociateInErrors_Object = MibTableColumn
cPtpClockPortAssociateInErrors = _CPtpClockPortAssociateInErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 11, 1, 10),
    _CPtpClockPortAssociateInErrors_Type()
)
cPtpClockPortAssociateInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortAssociateInErrors.setStatus("current")
if mibBuilder.loadTexts:
    cPtpClockPortAssociateInErrors.setUnits("packets")
_CPtpClockPortAssociateOutErrors_Type = Counter64
_CPtpClockPortAssociateOutErrors_Object = MibTableColumn
cPtpClockPortAssociateOutErrors = _CPtpClockPortAssociateOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 1, 2, 11, 1, 11),
    _CPtpClockPortAssociateOutErrors_Type()
)
cPtpClockPortAssociateOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtpClockPortAssociateOutErrors.setStatus("current")
if mibBuilder.loadTexts:
    cPtpClockPortAssociateOutErrors.setUnits("packets")
_CiscoPtpMIBConformance_ObjectIdentity = ObjectIdentity
ciscoPtpMIBConformance = _CiscoPtpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 2)
)
_CiscoPtpMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoPtpMIBCompliances = _CiscoPtpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 2, 1)
)
_CiscoPtpMIBGroups_ObjectIdentity = ObjectIdentity
ciscoPtpMIBGroups = _CiscoPtpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 2, 2)
)

# Managed Objects groups

ciscoPtpMIBSystemInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 2, 2, 1)
)
ciscoPtpMIBSystemInfoGroup.setObjects(
      *(("CISCO-PTP-MIB", "cPtpSystemDomainTotals"),
        ("CISCO-PTP-MIB", "cPtpDomainClockPortsTotal"),
        ("CISCO-PTP-MIB", "cPtpDomainClockPortPhysicalInterfacesTotal"),
        ("CISCO-PTP-MIB", "cPtpClockInput1ppsEnabled"),
        ("CISCO-PTP-MIB", "cPtpClockOutput1ppsEnabled"),
        ("CISCO-PTP-MIB", "cPtpClockOutput1ppsOffsetEnabled"),
        ("CISCO-PTP-MIB", "cPtpClockInputFrequencyEnabled"),
        ("CISCO-PTP-MIB", "cPtpClockTODEnabled"),
        ("CISCO-PTP-MIB", "cPtpClockOutput1ppsOffsetValue"),
        ("CISCO-PTP-MIB", "cPtpClockOutput1ppsOffsetNegative"),
        ("CISCO-PTP-MIB", "cPtpSystemProfile"),
        ("CISCO-PTP-MIB", "cPtpClockInput1ppsInterface"),
        ("CISCO-PTP-MIB", "cPtpClockOutput1ppsInterface"),
        ("CISCO-PTP-MIB", "cPtpClockTODInterface"))
)
if mibBuilder.loadTexts:
    ciscoPtpMIBSystemInfoGroup.setStatus("current")

ciscoPtpMIBClockCurrentDSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 2, 2, 2)
)
ciscoPtpMIBClockCurrentDSGroup.setObjects(
      *(("CISCO-PTP-MIB", "cPtpClockCurrentDSStepsRemoved"),
        ("CISCO-PTP-MIB", "cPtpClockCurrentDSOffsetFromMaster"),
        ("CISCO-PTP-MIB", "cPtpClockCurrentDSMeanPathDelay"))
)
if mibBuilder.loadTexts:
    ciscoPtpMIBClockCurrentDSGroup.setStatus("current")

ciscoPtpMIBClockParentDSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 2, 2, 3)
)
ciscoPtpMIBClockParentDSGroup.setObjects(
      *(("CISCO-PTP-MIB", "cPtpClockParentDSParentPortIdentity"),
        ("CISCO-PTP-MIB", "cPtpClockParentDSParentStats"),
        ("CISCO-PTP-MIB", "cPtpClockParentDSOffset"),
        ("CISCO-PTP-MIB", "cPtpClockParentDSClockPhChRate"),
        ("CISCO-PTP-MIB", "cPtpClockParentDSGMClockIdentity"),
        ("CISCO-PTP-MIB", "cPtpClockParentDSGMClockPriority1"),
        ("CISCO-PTP-MIB", "cPtpClockParentDSGMClockPriority2"),
        ("CISCO-PTP-MIB", "cPtpClockParentDSGMClockQualityClass"),
        ("CISCO-PTP-MIB", "cPtpClockParentDSGMClockQualityAccuracy"),
        ("CISCO-PTP-MIB", "cPtpClockParentDSGMClockQualityOffset"))
)
if mibBuilder.loadTexts:
    ciscoPtpMIBClockParentDSGroup.setStatus("current")

ciscoPtpMIBClockDefaultDSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 2, 2, 4)
)
ciscoPtpMIBClockDefaultDSGroup.setObjects(
      *(("CISCO-PTP-MIB", "cPtpClockDefaultDSTwoStepFlag"),
        ("CISCO-PTP-MIB", "cPtpClockDefaultDSClockIdentity"),
        ("CISCO-PTP-MIB", "cPtpClockDefaultDSPriority1"),
        ("CISCO-PTP-MIB", "cPtpClockDefaultDSPriority2"),
        ("CISCO-PTP-MIB", "cPtpClockDefaultDSSlaveOnly"),
        ("CISCO-PTP-MIB", "cPtpClockDefaultDSQualityClass"),
        ("CISCO-PTP-MIB", "cPtpClockDefaultDSQualityAccuracy"),
        ("CISCO-PTP-MIB", "cPtpClockDefaultDSQualityOffset"))
)
if mibBuilder.loadTexts:
    ciscoPtpMIBClockDefaultDSGroup.setStatus("current")

ciscoPtpMIBClockRunningGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 2, 2, 5)
)
ciscoPtpMIBClockRunningGroup.setObjects(
      *(("CISCO-PTP-MIB", "cPtpClockRunningState"),
        ("CISCO-PTP-MIB", "cPtpClockRunningPacketsSent"),
        ("CISCO-PTP-MIB", "cPtpClockRunningPacketsReceived"))
)
if mibBuilder.loadTexts:
    ciscoPtpMIBClockRunningGroup.setStatus("current")

ciscoPtpMIBClockTimepropertiesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 2, 2, 6)
)
ciscoPtpMIBClockTimepropertiesGroup.setObjects(
      *(("CISCO-PTP-MIB", "cPtpClockTimePropertiesDSCurrentUTCOffsetValid"),
        ("CISCO-PTP-MIB", "cPtpClockTimePropertiesDSCurrentUTCOffset"),
        ("CISCO-PTP-MIB", "cPtpClockTimePropertiesDSLeap59"),
        ("CISCO-PTP-MIB", "cPtpClockTimePropertiesDSLeap61"),
        ("CISCO-PTP-MIB", "cPtpClockTimePropertiesDSTimeTraceable"),
        ("CISCO-PTP-MIB", "cPtpClockTimePropertiesDSFreqTraceable"),
        ("CISCO-PTP-MIB", "cPtpClockTimePropertiesDSPTPTimescale"),
        ("CISCO-PTP-MIB", "cPtpClockTimePropertiesDSSource"))
)
if mibBuilder.loadTexts:
    ciscoPtpMIBClockTimepropertiesGroup.setStatus("current")

ciscoPtpMIBClockTranparentDSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 2, 2, 7)
)
ciscoPtpMIBClockTranparentDSGroup.setObjects(
      *(("CISCO-PTP-MIB", "cPtpClockTransDefaultDSClockIdentity"),
        ("CISCO-PTP-MIB", "cPtpClockTransDefaultDSNumOfPorts"),
        ("CISCO-PTP-MIB", "cPtpClockTransDefaultDSDelay"),
        ("CISCO-PTP-MIB", "cPtpClockTransDefaultDSPrimaryDomain"))
)
if mibBuilder.loadTexts:
    ciscoPtpMIBClockTranparentDSGroup.setStatus("current")

ciscoPtpMIBClockPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 2, 2, 8)
)
ciscoPtpMIBClockPortGroup.setObjects(
      *(("CISCO-PTP-MIB", "cPtpClockPortName"),
        ("CISCO-PTP-MIB", "cPtpClockPortSyncOneStep"),
        ("CISCO-PTP-MIB", "cPtpClockPortCurrentPeerAddress"),
        ("CISCO-PTP-MIB", "cPtpClockPortNumOfAssociatedPorts"),
        ("CISCO-PTP-MIB", "cPtpClockPortCurrentPeerAddressType"),
        ("CISCO-PTP-MIB", "cPtpClockPortRole"))
)
if mibBuilder.loadTexts:
    ciscoPtpMIBClockPortGroup.setStatus("current")

ciscoPtpMIBClockPortDSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 2, 2, 9)
)
ciscoPtpMIBClockPortDSGroup.setObjects(
      *(("CISCO-PTP-MIB", "cPtpClockPortDSName"),
        ("CISCO-PTP-MIB", "cPtpClockPortDSPortIdentity"),
        ("CISCO-PTP-MIB", "cPtpClockPortDSAnnouncementInterval"),
        ("CISCO-PTP-MIB", "cPtpClockPortDSAnnounceRctTimeout"),
        ("CISCO-PTP-MIB", "cPtpClockPortDSSyncInterval"),
        ("CISCO-PTP-MIB", "cPtpClockPortDSMinDelayReqInterval"),
        ("CISCO-PTP-MIB", "cPtpClockPortDSPeerDelayReqInterval"),
        ("CISCO-PTP-MIB", "cPtpClockPortDSDelayMech"),
        ("CISCO-PTP-MIB", "cPtpClockPortDSPeerMeanPathDelay"),
        ("CISCO-PTP-MIB", "cPtpClockPortDSGrantDuration"),
        ("CISCO-PTP-MIB", "cPtpClockPortDSPTPVersion"))
)
if mibBuilder.loadTexts:
    ciscoPtpMIBClockPortDSGroup.setStatus("current")

ciscoPtpMIBClockPortRunningGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 2, 2, 10)
)
ciscoPtpMIBClockPortRunningGroup.setObjects(
      *(("CISCO-PTP-MIB", "cPtpClockPortRunningName"),
        ("CISCO-PTP-MIB", "cPtpClockPortRunningState"),
        ("CISCO-PTP-MIB", "cPtpClockPortRunningRole"),
        ("CISCO-PTP-MIB", "cPtpClockPortRunningInterfaceIndex"),
        ("CISCO-PTP-MIB", "cPtpClockPortRunningIPversion"),
        ("CISCO-PTP-MIB", "cPtpClockPortRunningEncapsulationType"),
        ("CISCO-PTP-MIB", "cPtpClockPortRunningTxMode"),
        ("CISCO-PTP-MIB", "cPtpClockPortRunningRxMode"),
        ("CISCO-PTP-MIB", "cPtpClockPortRunningPacketsReceived"),
        ("CISCO-PTP-MIB", "cPtpClockPortRunningPacketsSent"))
)
if mibBuilder.loadTexts:
    ciscoPtpMIBClockPortRunningGroup.setStatus("current")

ciscoPtpMIBClockPortTransDSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 2, 2, 11)
)
ciscoPtpMIBClockPortTransDSGroup.setObjects(
      *(("CISCO-PTP-MIB", "cPtpClockPortTransDSPortIdentity"),
        ("CISCO-PTP-MIB", "cPtpClockPortTransDSlogMinPdelayReqInt"),
        ("CISCO-PTP-MIB", "cPtpClockPortTransDSFaultyFlag"),
        ("CISCO-PTP-MIB", "cPtpClockPortTransDSPeerMeanPathDelay"))
)
if mibBuilder.loadTexts:
    ciscoPtpMIBClockPortTransDSGroup.setStatus("current")

ciscoPtpMIBClockPortAssociateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 2, 2, 12)
)
ciscoPtpMIBClockPortAssociateGroup.setObjects(
      *(("CISCO-PTP-MIB", "cPtpClockPortAssociatePacketsSent"),
        ("CISCO-PTP-MIB", "cPtpClockPortAssociatePacketsReceived"),
        ("CISCO-PTP-MIB", "cPtpClockPortAssociateAddress"),
        ("CISCO-PTP-MIB", "cPtpClockPortAssociateAddressType"),
        ("CISCO-PTP-MIB", "cPtpClockPortAssociateInErrors"),
        ("CISCO-PTP-MIB", "cPtpClockPortAssociateOutErrors"))
)
if mibBuilder.loadTexts:
    ciscoPtpMIBClockPortAssociateGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoPtpMIBCompliances1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoPtpMIBCompliances1.setStatus(
        "current"
    )

ciscoPtpMIBCompliances2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoPtpMIBCompliances2.setStatus(
        "current"
    )

ciscoPtpMIBCompliances3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoPtpMIBCompliances3.setStatus(
        "current"
    )

ciscoPtpMIBCompliances4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 760, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoPtpMIBCompliances4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PTP-MIB",
    **{"ClockDomainType": ClockDomainType,
       "ClockIdentity": ClockIdentity,
       "ClockIntervalBase2": ClockIntervalBase2,
       "ClockMechanismType": ClockMechanismType,
       "ClockInstanceType": ClockInstanceType,
       "ClockPortNumber": ClockPortNumber,
       "ClockPortState": ClockPortState,
       "ClockProfileType": ClockProfileType,
       "ClockQualityAccuracyType": ClockQualityAccuracyType,
       "ClockQualityClassType": ClockQualityClassType,
       "ClockRoleType": ClockRoleType,
       "ClockStateType": ClockStateType,
       "ClockTimeSourceType": ClockTimeSourceType,
       "ClockTimeInterval": ClockTimeInterval,
       "ClockTxModeType": ClockTxModeType,
       "ClockType": ClockType,
       "ciscoPtpMIB": ciscoPtpMIB,
       "ciscoPtpMIBNotifs": ciscoPtpMIBNotifs,
       "ciscoPtpMIBObjects": ciscoPtpMIBObjects,
       "ciscoPtpMIBSystemInfo": ciscoPtpMIBSystemInfo,
       "cPtpSystemTable": cPtpSystemTable,
       "cPtpSystemEntry": cPtpSystemEntry,
       "cPtpDomainIndex": cPtpDomainIndex,
       "cPtpInstanceIndex": cPtpInstanceIndex,
       "cPtpDomainClockPortsTotal": cPtpDomainClockPortsTotal,
       "cPtpDomainClockPortPhysicalInterfacesTotal": cPtpDomainClockPortPhysicalInterfacesTotal,
       "cPtpSystemDomainTable": cPtpSystemDomainTable,
       "cPtpSystemDomainEntry": cPtpSystemDomainEntry,
       "cPtpSystemDomainClockTypeIndex": cPtpSystemDomainClockTypeIndex,
       "cPtpSystemDomainTotals": cPtpSystemDomainTotals,
       "cPtpClockNodeTable": cPtpClockNodeTable,
       "cPtpClockNodeEntry": cPtpClockNodeEntry,
       "cPtpClockDomainIndex": cPtpClockDomainIndex,
       "cPtpClockTypeIndex": cPtpClockTypeIndex,
       "cPtpClockInstanceIndex": cPtpClockInstanceIndex,
       "cPtpClockInput1ppsEnabled": cPtpClockInput1ppsEnabled,
       "cPtpClockInputFrequencyEnabled": cPtpClockInputFrequencyEnabled,
       "cPtpClockTODEnabled": cPtpClockTODEnabled,
       "cPtpClockOutput1ppsEnabled": cPtpClockOutput1ppsEnabled,
       "cPtpClockOutput1ppsOffsetEnabled": cPtpClockOutput1ppsOffsetEnabled,
       "cPtpClockOutput1ppsOffsetValue": cPtpClockOutput1ppsOffsetValue,
       "cPtpClockOutput1ppsOffsetNegative": cPtpClockOutput1ppsOffsetNegative,
       "cPtpClockInput1ppsInterface": cPtpClockInput1ppsInterface,
       "cPtpClockOutput1ppsInterface": cPtpClockOutput1ppsInterface,
       "cPtpClockTODInterface": cPtpClockTODInterface,
       "cPtpSystemProfile": cPtpSystemProfile,
       "ciscoPtpMIBClockInfo": ciscoPtpMIBClockInfo,
       "cPtpClockCurrentDSTable": cPtpClockCurrentDSTable,
       "cPtpClockCurrentDSEntry": cPtpClockCurrentDSEntry,
       "cPtpClockCurrentDSDomainIndex": cPtpClockCurrentDSDomainIndex,
       "cPtpClockCurrentDSClockTypeIndex": cPtpClockCurrentDSClockTypeIndex,
       "cPtpClockCurrentDSInstanceIndex": cPtpClockCurrentDSInstanceIndex,
       "cPtpClockCurrentDSStepsRemoved": cPtpClockCurrentDSStepsRemoved,
       "cPtpClockCurrentDSOffsetFromMaster": cPtpClockCurrentDSOffsetFromMaster,
       "cPtpClockCurrentDSMeanPathDelay": cPtpClockCurrentDSMeanPathDelay,
       "cPtpClockParentDSTable": cPtpClockParentDSTable,
       "cPtpClockParentDSEntry": cPtpClockParentDSEntry,
       "cPtpClockParentDSDomainIndex": cPtpClockParentDSDomainIndex,
       "cPtpClockParentDSClockTypeIndex": cPtpClockParentDSClockTypeIndex,
       "cPtpClockParentDSInstanceIndex": cPtpClockParentDSInstanceIndex,
       "cPtpClockParentDSParentPortIdentity": cPtpClockParentDSParentPortIdentity,
       "cPtpClockParentDSParentStats": cPtpClockParentDSParentStats,
       "cPtpClockParentDSOffset": cPtpClockParentDSOffset,
       "cPtpClockParentDSClockPhChRate": cPtpClockParentDSClockPhChRate,
       "cPtpClockParentDSGMClockIdentity": cPtpClockParentDSGMClockIdentity,
       "cPtpClockParentDSGMClockPriority1": cPtpClockParentDSGMClockPriority1,
       "cPtpClockParentDSGMClockPriority2": cPtpClockParentDSGMClockPriority2,
       "cPtpClockParentDSGMClockQualityClass": cPtpClockParentDSGMClockQualityClass,
       "cPtpClockParentDSGMClockQualityAccuracy": cPtpClockParentDSGMClockQualityAccuracy,
       "cPtpClockParentDSGMClockQualityOffset": cPtpClockParentDSGMClockQualityOffset,
       "cPtpClockDefaultDSTable": cPtpClockDefaultDSTable,
       "cPtpClockDefaultDSEntry": cPtpClockDefaultDSEntry,
       "cPtpClockDefaultDSDomainIndex": cPtpClockDefaultDSDomainIndex,
       "cPtpClockDefaultDSClockTypeIndex": cPtpClockDefaultDSClockTypeIndex,
       "cPtpClockDefaultDSInstanceIndex": cPtpClockDefaultDSInstanceIndex,
       "cPtpClockDefaultDSTwoStepFlag": cPtpClockDefaultDSTwoStepFlag,
       "cPtpClockDefaultDSClockIdentity": cPtpClockDefaultDSClockIdentity,
       "cPtpClockDefaultDSPriority1": cPtpClockDefaultDSPriority1,
       "cPtpClockDefaultDSPriority2": cPtpClockDefaultDSPriority2,
       "cPtpClockDefaultDSSlaveOnly": cPtpClockDefaultDSSlaveOnly,
       "cPtpClockDefaultDSQualityClass": cPtpClockDefaultDSQualityClass,
       "cPtpClockDefaultDSQualityAccuracy": cPtpClockDefaultDSQualityAccuracy,
       "cPtpClockDefaultDSQualityOffset": cPtpClockDefaultDSQualityOffset,
       "cPtpClockRunningTable": cPtpClockRunningTable,
       "cPtpClockRunningEntry": cPtpClockRunningEntry,
       "cPtpClockRunningDomainIndex": cPtpClockRunningDomainIndex,
       "cPtpClockRunningClockTypeIndex": cPtpClockRunningClockTypeIndex,
       "cPtpClockRunningInstanceIndex": cPtpClockRunningInstanceIndex,
       "cPtpClockRunningState": cPtpClockRunningState,
       "cPtpClockRunningPacketsSent": cPtpClockRunningPacketsSent,
       "cPtpClockRunningPacketsReceived": cPtpClockRunningPacketsReceived,
       "cPtpClockTimePropertiesDSTable": cPtpClockTimePropertiesDSTable,
       "cPtpClockTimePropertiesDSEntry": cPtpClockTimePropertiesDSEntry,
       "cPtpClockTimePropertiesDSDomainIndex": cPtpClockTimePropertiesDSDomainIndex,
       "cPtpClockTimePropertiesDSClockTypeIndex": cPtpClockTimePropertiesDSClockTypeIndex,
       "cPtpClockTimePropertiesDSInstanceIndex": cPtpClockTimePropertiesDSInstanceIndex,
       "cPtpClockTimePropertiesDSCurrentUTCOffsetValid": cPtpClockTimePropertiesDSCurrentUTCOffsetValid,
       "cPtpClockTimePropertiesDSCurrentUTCOffset": cPtpClockTimePropertiesDSCurrentUTCOffset,
       "cPtpClockTimePropertiesDSLeap59": cPtpClockTimePropertiesDSLeap59,
       "cPtpClockTimePropertiesDSLeap61": cPtpClockTimePropertiesDSLeap61,
       "cPtpClockTimePropertiesDSTimeTraceable": cPtpClockTimePropertiesDSTimeTraceable,
       "cPtpClockTimePropertiesDSFreqTraceable": cPtpClockTimePropertiesDSFreqTraceable,
       "cPtpClockTimePropertiesDSPTPTimescale": cPtpClockTimePropertiesDSPTPTimescale,
       "cPtpClockTimePropertiesDSSource": cPtpClockTimePropertiesDSSource,
       "cPtpClockTransDefaultDSTable": cPtpClockTransDefaultDSTable,
       "cPtpClockTransDefaultDSEntry": cPtpClockTransDefaultDSEntry,
       "cPtpClockTransDefaultDSDomainIndex": cPtpClockTransDefaultDSDomainIndex,
       "cPtpClockTransDefaultDSInstanceIndex": cPtpClockTransDefaultDSInstanceIndex,
       "cPtpClockTransDefaultDSClockIdentity": cPtpClockTransDefaultDSClockIdentity,
       "cPtpClockTransDefaultDSNumOfPorts": cPtpClockTransDefaultDSNumOfPorts,
       "cPtpClockTransDefaultDSDelay": cPtpClockTransDefaultDSDelay,
       "cPtpClockTransDefaultDSPrimaryDomain": cPtpClockTransDefaultDSPrimaryDomain,
       "cPtpClockPortTable": cPtpClockPortTable,
       "cPtpClockPortEntry": cPtpClockPortEntry,
       "cPtpClockPortDomainIndex": cPtpClockPortDomainIndex,
       "cPtpClockPortClockTypeIndex": cPtpClockPortClockTypeIndex,
       "cPtpClockPortClockInstanceIndex": cPtpClockPortClockInstanceIndex,
       "cPtpClockPortTablePortNumberIndex": cPtpClockPortTablePortNumberIndex,
       "cPtpClockPortName": cPtpClockPortName,
       "cPtpClockPortRole": cPtpClockPortRole,
       "cPtpClockPortSyncOneStep": cPtpClockPortSyncOneStep,
       "cPtpClockPortCurrentPeerAddressType": cPtpClockPortCurrentPeerAddressType,
       "cPtpClockPortCurrentPeerAddress": cPtpClockPortCurrentPeerAddress,
       "cPtpClockPortNumOfAssociatedPorts": cPtpClockPortNumOfAssociatedPorts,
       "cPtpClockPortDSTable": cPtpClockPortDSTable,
       "cPtpClockPortDSEntry": cPtpClockPortDSEntry,
       "cPtpClockPortDSDomainIndex": cPtpClockPortDSDomainIndex,
       "cPtpClockPortDSClockTypeIndex": cPtpClockPortDSClockTypeIndex,
       "cPtpClockPortDSClockInstanceIndex": cPtpClockPortDSClockInstanceIndex,
       "cPtpClockPortDSPortNumberIndex": cPtpClockPortDSPortNumberIndex,
       "cPtpClockPortDSName": cPtpClockPortDSName,
       "cPtpClockPortDSPortIdentity": cPtpClockPortDSPortIdentity,
       "cPtpClockPortDSAnnouncementInterval": cPtpClockPortDSAnnouncementInterval,
       "cPtpClockPortDSAnnounceRctTimeout": cPtpClockPortDSAnnounceRctTimeout,
       "cPtpClockPortDSSyncInterval": cPtpClockPortDSSyncInterval,
       "cPtpClockPortDSMinDelayReqInterval": cPtpClockPortDSMinDelayReqInterval,
       "cPtpClockPortDSPeerDelayReqInterval": cPtpClockPortDSPeerDelayReqInterval,
       "cPtpClockPortDSDelayMech": cPtpClockPortDSDelayMech,
       "cPtpClockPortDSPeerMeanPathDelay": cPtpClockPortDSPeerMeanPathDelay,
       "cPtpClockPortDSGrantDuration": cPtpClockPortDSGrantDuration,
       "cPtpClockPortDSPTPVersion": cPtpClockPortDSPTPVersion,
       "cPtpClockPortRunningTable": cPtpClockPortRunningTable,
       "cPtpClockPortRunningEntry": cPtpClockPortRunningEntry,
       "cPtpClockPortRunningDomainIndex": cPtpClockPortRunningDomainIndex,
       "cPtpClockPortRunningClockTypeIndex": cPtpClockPortRunningClockTypeIndex,
       "cPtpClockPortRunningClockInstanceIndex": cPtpClockPortRunningClockInstanceIndex,
       "cPtpClockPortRunningPortNumberIndex": cPtpClockPortRunningPortNumberIndex,
       "cPtpClockPortRunningName": cPtpClockPortRunningName,
       "cPtpClockPortRunningState": cPtpClockPortRunningState,
       "cPtpClockPortRunningRole": cPtpClockPortRunningRole,
       "cPtpClockPortRunningInterfaceIndex": cPtpClockPortRunningInterfaceIndex,
       "cPtpClockPortRunningIPversion": cPtpClockPortRunningIPversion,
       "cPtpClockPortRunningEncapsulationType": cPtpClockPortRunningEncapsulationType,
       "cPtpClockPortRunningTxMode": cPtpClockPortRunningTxMode,
       "cPtpClockPortRunningRxMode": cPtpClockPortRunningRxMode,
       "cPtpClockPortRunningPacketsReceived": cPtpClockPortRunningPacketsReceived,
       "cPtpClockPortRunningPacketsSent": cPtpClockPortRunningPacketsSent,
       "cPtpClockPortTransDSTable": cPtpClockPortTransDSTable,
       "cPtpClockPortTransDSEntry": cPtpClockPortTransDSEntry,
       "cPtpClockPortTransDSDomainIndex": cPtpClockPortTransDSDomainIndex,
       "cPtpClockPortTransDSInstanceIndex": cPtpClockPortTransDSInstanceIndex,
       "cPtpClockPortTransDSPortNumberIndex": cPtpClockPortTransDSPortNumberIndex,
       "cPtpClockPortTransDSPortIdentity": cPtpClockPortTransDSPortIdentity,
       "cPtpClockPortTransDSlogMinPdelayReqInt": cPtpClockPortTransDSlogMinPdelayReqInt,
       "cPtpClockPortTransDSFaultyFlag": cPtpClockPortTransDSFaultyFlag,
       "cPtpClockPortTransDSPeerMeanPathDelay": cPtpClockPortTransDSPeerMeanPathDelay,
       "cPtpClockPortAssociateTable": cPtpClockPortAssociateTable,
       "cPtpClockPortAssociateEntry": cPtpClockPortAssociateEntry,
       "cPtpClockPortCurrentDomainIndex": cPtpClockPortCurrentDomainIndex,
       "cPtpClockPortCurrentClockTypeIndex": cPtpClockPortCurrentClockTypeIndex,
       "cPtpClockPortCurrentClockInstanceIndex": cPtpClockPortCurrentClockInstanceIndex,
       "cPtpClockPortCurrentPortNumberIndex": cPtpClockPortCurrentPortNumberIndex,
       "cPtpClockPortAssociatePortIndex": cPtpClockPortAssociatePortIndex,
       "cPtpClockPortAssociateAddressType": cPtpClockPortAssociateAddressType,
       "cPtpClockPortAssociateAddress": cPtpClockPortAssociateAddress,
       "cPtpClockPortAssociatePacketsSent": cPtpClockPortAssociatePacketsSent,
       "cPtpClockPortAssociatePacketsReceived": cPtpClockPortAssociatePacketsReceived,
       "cPtpClockPortAssociateInErrors": cPtpClockPortAssociateInErrors,
       "cPtpClockPortAssociateOutErrors": cPtpClockPortAssociateOutErrors,
       "ciscoPtpMIBConformance": ciscoPtpMIBConformance,
       "ciscoPtpMIBCompliances": ciscoPtpMIBCompliances,
       "ciscoPtpMIBCompliances1": ciscoPtpMIBCompliances1,
       "ciscoPtpMIBCompliances2": ciscoPtpMIBCompliances2,
       "ciscoPtpMIBCompliances3": ciscoPtpMIBCompliances3,
       "ciscoPtpMIBCompliances4": ciscoPtpMIBCompliances4,
       "ciscoPtpMIBGroups": ciscoPtpMIBGroups,
       "ciscoPtpMIBSystemInfoGroup": ciscoPtpMIBSystemInfoGroup,
       "ciscoPtpMIBClockCurrentDSGroup": ciscoPtpMIBClockCurrentDSGroup,
       "ciscoPtpMIBClockParentDSGroup": ciscoPtpMIBClockParentDSGroup,
       "ciscoPtpMIBClockDefaultDSGroup": ciscoPtpMIBClockDefaultDSGroup,
       "ciscoPtpMIBClockRunningGroup": ciscoPtpMIBClockRunningGroup,
       "ciscoPtpMIBClockTimepropertiesGroup": ciscoPtpMIBClockTimepropertiesGroup,
       "ciscoPtpMIBClockTranparentDSGroup": ciscoPtpMIBClockTranparentDSGroup,
       "ciscoPtpMIBClockPortGroup": ciscoPtpMIBClockPortGroup,
       "ciscoPtpMIBClockPortDSGroup": ciscoPtpMIBClockPortDSGroup,
       "ciscoPtpMIBClockPortRunningGroup": ciscoPtpMIBClockPortRunningGroup,
       "ciscoPtpMIBClockPortTransDSGroup": ciscoPtpMIBClockPortTransDSGroup,
       "ciscoPtpMIBClockPortAssociateGroup": ciscoPtpMIBClockPortAssociateGroup}
)
