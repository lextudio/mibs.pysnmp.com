# SNMP MIB module (Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:43 2024
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

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscPassportMIBs")

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



class Gauge32(Gauge32):
    """Custom type Gauge32 based on Gauge32"""




class Counter32(Counter32):
    """Custom type Counter32 based on Counter32"""




class Unsigned32(Gauge32):
    """Custom type Unsigned32 based on Gauge32"""




class Integer32(Integer32):
    """Custom type Integer32 based on Integer32"""




class NsapAddress(OctetString):
    """Custom type NsapAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
        ValueSizeConstraint(4, 21),
    )





class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""




class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )





class TestAndIncr(Integer32):
    """Custom type TestAndIncr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class AutonomousType(ObjectIdentifier):
    """Custom type AutonomousType based on ObjectIdentifier"""




class VariablePointer(ObjectIdentifier):
    """Custom type VariablePointer based on ObjectIdentifier"""




class RowPointer(ObjectIdentifier):
    """Custom type RowPointer based on ObjectIdentifier"""




class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )





class TimeStamp(TimeTicks):
    """Custom type TimeStamp based on TimeTicks"""




class TimeInterval(Integer32):
    """Custom type TimeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class DateAndTime(OctetString):
    """Custom type DateAndTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )





class TAddress(OctetString):
    """Custom type TAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )





class StorageType(Integer32):
    """Custom type StorageType based on Integer32"""
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
        *(("nonVolatile", 3),
          ("other", 1),
          ("permanent", 4),
          ("readOnly", 5),
          ("volatile", 2))
    )





class IANAifType(Integer32):
    """Custom type IANAifType based on Integer32"""
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
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
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
              50,
              51,
              52,
              53,
              54)
        )
    )
    namedValues = NamedValues(
        *(("aal5", 49),
          ("arcnet", 35),
          ("arcnetPlus", 36),
          ("atm", 37),
          ("basicISDN", 20),
          ("ddnX25", 4),
          ("ds1", 18),
          ("ds3", 30),
          ("e1", 19),
          ("eon", 25),
          ("ethernet3Mbit", 26),
          ("ethernetCsmacd", 6),
          ("fddi", 15),
          ("frameRelay", 32),
          ("frameRelayService", 44),
          ("fslip", 28),
          ("hdh1822", 3),
          ("hippi", 47),
          ("hssi", 46),
          ("hyperchannel", 14),
          ("iso88022llc", 41),
          ("iso88023Csmacd", 7),
          ("iso88024TokenBus", 8),
          ("iso88025TokenRing", 9),
          ("iso88026Man", 10),
          ("lapb", 16),
          ("localTalk", 42),
          ("miox25", 38),
          ("modem", 48),
          ("nsip", 27),
          ("other", 1),
          ("para", 34),
          ("ppp", 23),
          ("primaryISDN", 21),
          ("propMultiplexor", 54),
          ("propPointToPointSerial", 22),
          ("propVirtual", 53),
          ("proteon10Mbit", 12),
          ("proteon80Mbit", 13),
          ("regular1822", 2),
          ("rfc877x25", 5),
          ("rs232", 33),
          ("sdlc", 17),
          ("sip", 31),
          ("smdsDxi", 43),
          ("smdsIcip", 52),
          ("softwareLoopback", 24),
          ("sonet", 39),
          ("sonetPath", 50),
          ("sonetVT", 51),
          ("starLan", 11),
          ("ultra", 29),
          ("v35", 45),
          ("x25ple", 40))
    )





class InterfaceIndex(Integer32):
    """Custom type InterfaceIndex based on Integer32"""




class FddiTimeNano(Integer32):
    """Custom type FddiTimeNano based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class FddiTimeMilli(Integer32):
    """Custom type FddiTimeMilli based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class FddiResourceId(Integer32):
    """Custom type FddiResourceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class FddiSMTStationIdType(OctetString):
    """Custom type FddiSMTStationIdType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class FddiMACLongAddressType(OctetString):
    """Custom type FddiMACLongAddressType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class BridgeId(OctetString):
    """Custom type BridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class Timeout(Integer32):
    """Custom type Timeout based on Integer32"""




class DLCI(Integer32):
    """Custom type DLCI based on Integer32"""




class AreaID(IpAddress):
    """Custom type AreaID based on IpAddress"""




class RouterID(IpAddress):
    """Custom type RouterID based on IpAddress"""




class Metric(Integer32):
    """Custom type Metric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )





class BigMetric(Integer32):
    """Custom type BigMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )





class Status(Integer32):
    """Custom type Status based on Integer32"""
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





class Validation(Integer32):
    """Custom type Validation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )





class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )





class HelloRange(Integer32):
    """Custom type HelloRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )





class UpToMaxAge(Integer32):
    """Custom type UpToMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )





class DesignatedRouterPriority(Integer32):
    """Custom type DesignatedRouterPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class TOSType(Integer32):
    """Custom type TOSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )





class X121Address(OctetString):
    """Custom type X121Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StandardTextualConventionsMIB_ObjectIdentity = ObjectIdentity
standardTextualConventionsMIB = _StandardTextualConventionsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 6)
)
_StandardTextualConventionsGroup_ObjectIdentity = ObjectIdentity
standardTextualConventionsGroup = _StandardTextualConventionsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 6, 1)
)
_StandardTextualConventionsGroupCA_ObjectIdentity = ObjectIdentity
standardTextualConventionsGroupCA = _StandardTextualConventionsGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 6, 1, 1)
)
_StandardTextualConventionsGroupCA01_ObjectIdentity = ObjectIdentity
standardTextualConventionsGroupCA01 = _StandardTextualConventionsGroupCA01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 6, 1, 1, 2)
)
_StandardTextualConventionsGroupCA01A_ObjectIdentity = ObjectIdentity
standardTextualConventionsGroupCA01A = _StandardTextualConventionsGroupCA01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 6, 1, 1, 2, 2)
)
_StandardTextualConventionsCapabilities_ObjectIdentity = ObjectIdentity
standardTextualConventionsCapabilities = _StandardTextualConventionsCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 6, 3)
)
_StandardTextualConventionsCapabilitiesCA_ObjectIdentity = ObjectIdentity
standardTextualConventionsCapabilitiesCA = _StandardTextualConventionsCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 6, 3, 1)
)
_StandardTextualConventionsCapabilitiesCA01_ObjectIdentity = ObjectIdentity
standardTextualConventionsCapabilitiesCA01 = _StandardTextualConventionsCapabilitiesCA01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 6, 3, 1, 2)
)
_StandardTextualConventionsCapabilitiesCA01A_ObjectIdentity = ObjectIdentity
standardTextualConventionsCapabilitiesCA01A = _StandardTextualConventionsCapabilitiesCA01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 6, 3, 1, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    **{"Gauge32": Gauge32,
       "Counter32": Counter32,
       "Unsigned32": Unsigned32,
       "Integer32": Integer32,
       "NsapAddress": NsapAddress,
       "DisplayString": DisplayString,
       "PhysAddress": PhysAddress,
       "MacAddress": MacAddress,
       "TruthValue": TruthValue,
       "TestAndIncr": TestAndIncr,
       "AutonomousType": AutonomousType,
       "VariablePointer": VariablePointer,
       "RowPointer": RowPointer,
       "RowStatus": RowStatus,
       "TimeStamp": TimeStamp,
       "TimeInterval": TimeInterval,
       "DateAndTime": DateAndTime,
       "TAddress": TAddress,
       "StorageType": StorageType,
       "IANAifType": IANAifType,
       "InterfaceIndex": InterfaceIndex,
       "FddiTimeNano": FddiTimeNano,
       "FddiTimeMilli": FddiTimeMilli,
       "FddiResourceId": FddiResourceId,
       "FddiSMTStationIdType": FddiSMTStationIdType,
       "FddiMACLongAddressType": FddiMACLongAddressType,
       "BridgeId": BridgeId,
       "Timeout": Timeout,
       "DLCI": DLCI,
       "AreaID": AreaID,
       "RouterID": RouterID,
       "Metric": Metric,
       "BigMetric": BigMetric,
       "Status": Status,
       "Validation": Validation,
       "PositiveInteger": PositiveInteger,
       "HelloRange": HelloRange,
       "UpToMaxAge": UpToMaxAge,
       "DesignatedRouterPriority": DesignatedRouterPriority,
       "TOSType": TOSType,
       "X121Address": X121Address,
       "standardTextualConventionsMIB": standardTextualConventionsMIB,
       "standardTextualConventionsGroup": standardTextualConventionsGroup,
       "standardTextualConventionsGroupCA": standardTextualConventionsGroupCA,
       "standardTextualConventionsGroupCA01": standardTextualConventionsGroupCA01,
       "standardTextualConventionsGroupCA01A": standardTextualConventionsGroupCA01A,
       "standardTextualConventionsCapabilities": standardTextualConventionsCapabilities,
       "standardTextualConventionsCapabilitiesCA": standardTextualConventionsCapabilitiesCA,
       "standardTextualConventionsCapabilitiesCA01": standardTextualConventionsCapabilitiesCA01,
       "standardTextualConventionsCapabilitiesCA01A": standardTextualConventionsCapabilitiesCA01A}
)
