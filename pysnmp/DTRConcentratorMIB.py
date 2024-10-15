# SNMP MIB module (DTRConcentratorMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DTRConcentratorMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:47 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class Counter32(Counter32):
    """Custom type Counter32 based on Counter32"""




class Integer32(Integer32):
    """Custom type Integer32 based on Integer32"""




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





class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class InterfaceIndex(Integer32):
    """Custom type InterfaceIndex based on Integer32"""




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
          ("slip", 28),
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





class BridgeId(OctetString):
    """Custom type BridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class DynamicFdbStatus(Integer32):
    """Custom type DynamicFdbStatus based on Integer32"""
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
        *(("invalid", 2),
          ("learned", 3),
          ("mgmt", 5),
          ("other", 1),
          ("self", 4))
    )





class StaticFdbStatus(Integer32):
    """Custom type StaticFdbStatus based on Integer32"""
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
        *(("deleteOnReset", 4),
          ("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )





class PortId(OctetString):
    """Custom type PortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )





class RouteDescriptor(OctetString):
    """Custom type RouteDescriptor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )





class Timeout(Integer32):
    """Custom type Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_Ibm8272_ObjectIdentity = ObjectIdentity
ibm8272 = _Ibm8272_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 66)
)
_Ibm8272Ts_ObjectIdentity = ObjectIdentity
ibm8272Ts = _Ibm8272Ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1)
)
_Ibm8272TsExpMIBs_ObjectIdentity = ObjectIdentity
ibm8272TsExpMIBs = _Ibm8272TsExpMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3)
)
_DtrMIBs_ObjectIdentity = ObjectIdentity
dtrMIBs = _DtrMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1)
)
_DtrConcMIB_ObjectIdentity = ObjectIdentity
dtrConcMIB = _DtrConcMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1)
)
_DtrConcMIBObjects_ObjectIdentity = ObjectIdentity
dtrConcMIBObjects = _DtrConcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1)
)
_DtrConcMIBBase_ObjectIdentity = ObjectIdentity
dtrConcMIBBase = _DtrConcMIBBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 1)
)
_DtrConcentratorAddress_Type = MacAddress
_DtrConcentratorAddress_Object = MibScalar
dtrConcentratorAddress = _DtrConcentratorAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 1, 1),
    _DtrConcentratorAddress_Type()
)
dtrConcentratorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrConcentratorAddress.setStatus("mandatory")


class _DtrOperNumberOfCrfs_Type(Integer32):
    """Custom type dtrOperNumberOfCrfs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DtrOperNumberOfCrfs_Type.__name__ = "Integer32"
_DtrOperNumberOfCrfs_Object = MibScalar
dtrOperNumberOfCrfs = _DtrOperNumberOfCrfs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 1, 2),
    _DtrOperNumberOfCrfs_Type()
)
dtrOperNumberOfCrfs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrOperNumberOfCrfs.setStatus("mandatory")


class _DtrOperNumberOfBridgeRelays_Type(Integer32):
    """Custom type dtrOperNumberOfBridgeRelays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_DtrOperNumberOfBridgeRelays_Type.__name__ = "Integer32"
_DtrOperNumberOfBridgeRelays_Object = MibScalar
dtrOperNumberOfBridgeRelays = _DtrOperNumberOfBridgeRelays_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 1, 3),
    _DtrOperNumberOfBridgeRelays_Type()
)
dtrOperNumberOfBridgeRelays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrOperNumberOfBridgeRelays.setStatus("mandatory")
_DtrCRFTable_Object = MibTable
dtrCRFTable = _DtrCRFTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    dtrCRFTable.setStatus("mandatory")
_DtrCRFEntry_Object = MibTableRow
dtrCRFEntry = _DtrCRFEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 1, 6, 1)
)
dtrCRFEntry.setIndexNames(
    (0, "DTRConcentratorMIB", "dtrCRFIndex"),
)
if mibBuilder.loadTexts:
    dtrCRFEntry.setStatus("mandatory")


class _DtrCRFIndex_Type(Integer32):
    """Custom type dtrCRFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DtrCRFIndex_Type.__name__ = "Integer32"
_DtrCRFIndex_Object = MibTableColumn
dtrCRFIndex = _DtrCRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 1, 6, 1, 1),
    _DtrCRFIndex_Type()
)
dtrCRFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFIndex.setStatus("mandatory")


class _DtrCRFNumberOfPorts_Type(Integer32):
    """Custom type dtrCRFNumberOfPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DtrCRFNumberOfPorts_Type.__name__ = "Integer32"
_DtrCRFNumberOfPorts_Object = MibTableColumn
dtrCRFNumberOfPorts = _DtrCRFNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 1, 6, 1, 2),
    _DtrCRFNumberOfPorts_Type()
)
dtrCRFNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFNumberOfPorts.setStatus("mandatory")
_DtrCRFPortMask_Type = OctetString
_DtrCRFPortMask_Object = MibTableColumn
dtrCRFPortMask = _DtrCRFPortMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 1, 6, 1, 3),
    _DtrCRFPortMask_Type()
)
dtrCRFPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrCRFPortMask.setStatus("mandatory")
_DtrCRFName_Type = DisplayString
_DtrCRFName_Object = MibTableColumn
dtrCRFName = _DtrCRFName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 1, 6, 1, 4),
    _DtrCRFName_Type()
)
dtrCRFName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFName.setStatus("mandatory")


class _DtrCRFMaxInfo_Type(Integer32):
    """Custom type dtrCRFMaxInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 18200),
    )


_DtrCRFMaxInfo_Type.__name__ = "Integer32"
_DtrCRFMaxInfo_Object = MibTableColumn
dtrCRFMaxInfo = _DtrCRFMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 1, 6, 1, 5),
    _DtrCRFMaxInfo_Type()
)
dtrCRFMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFMaxInfo.setStatus("mandatory")
_DtrCRFMacAddress_Type = MacAddress
_DtrCRFMacAddress_Object = MibTableColumn
dtrCRFMacAddress = _DtrCRFMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 1, 6, 1, 6),
    _DtrCRFMacAddress_Type()
)
dtrCRFMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFMacAddress.setStatus("mandatory")


class _DtrCRFLocalLanId_Type(Integer32):
    """Custom type dtrCRFLocalLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DtrCRFLocalLanId_Type.__name__ = "Integer32"
_DtrCRFLocalLanId_Object = MibTableColumn
dtrCRFLocalLanId = _DtrCRFLocalLanId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 1, 6, 1, 7),
    _DtrCRFLocalLanId_Type()
)
dtrCRFLocalLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrCRFLocalLanId.setStatus("mandatory")


class _DtrCRFFdbAgingTime_Type(Integer32):
    """Custom type dtrCRFFdbAgingTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_DtrCRFFdbAgingTime_Type.__name__ = "Integer32"
_DtrCRFFdbAgingTime_Object = MibTableColumn
dtrCRFFdbAgingTime = _DtrCRFFdbAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 1, 6, 1, 8),
    _DtrCRFFdbAgingTime_Type()
)
dtrCRFFdbAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrCRFFdbAgingTime.setStatus("mandatory")


class _DtrCRFMRIEnable_Type(Integer32):
    """Custom type dtrCRFMRIEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_DtrCRFMRIEnable_Type.__name__ = "Integer32"
_DtrCRFMRIEnable_Object = MibTableColumn
dtrCRFMRIEnable = _DtrCRFMRIEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 1, 6, 1, 9),
    _DtrCRFMRIEnable_Type()
)
dtrCRFMRIEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrCRFMRIEnable.setStatus("mandatory")
_DtrCRFLearnedEntryDiscards_Type = Counter32
_DtrCRFLearnedEntryDiscards_Object = MibTableColumn
dtrCRFLearnedEntryDiscards = _DtrCRFLearnedEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 1, 6, 1, 10),
    _DtrCRFLearnedEntryDiscards_Type()
)
dtrCRFLearnedEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFLearnedEntryDiscards.setStatus("mandatory")
_DtrCRFPortTable_Object = MibTable
dtrCRFPortTable = _DtrCRFPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    dtrCRFPortTable.setStatus("mandatory")
_DtrCRFPortEntry_Object = MibTableRow
dtrCRFPortEntry = _DtrCRFPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 1, 7, 1)
)
dtrCRFPortEntry.setIndexNames(
    (0, "DTRConcentratorMIB", "dtrCRFPortCRFIndex"),
    (0, "DTRConcentratorMIB", "dtrCRFPortNumber"),
)
if mibBuilder.loadTexts:
    dtrCRFPortEntry.setStatus("mandatory")


class _DtrCRFPortCRFIndex_Type(Integer32):
    """Custom type dtrCRFPortCRFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DtrCRFPortCRFIndex_Type.__name__ = "Integer32"
_DtrCRFPortCRFIndex_Object = MibTableColumn
dtrCRFPortCRFIndex = _DtrCRFPortCRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 1, 7, 1, 1),
    _DtrCRFPortCRFIndex_Type()
)
dtrCRFPortCRFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFPortCRFIndex.setStatus("mandatory")


class _DtrCRFPortNumber_Type(Integer32):
    """Custom type dtrCRFPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DtrCRFPortNumber_Type.__name__ = "Integer32"
_DtrCRFPortNumber_Object = MibTableColumn
dtrCRFPortNumber = _DtrCRFPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 1, 7, 1, 2),
    _DtrCRFPortNumber_Type()
)
dtrCRFPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFPortNumber.setStatus("mandatory")
_DtrCRFPortifIndex_Type = InterfaceIndex
_DtrCRFPortifIndex_Object = MibTableColumn
dtrCRFPortifIndex = _DtrCRFPortifIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 1, 7, 1, 3),
    _DtrCRFPortifIndex_Type()
)
dtrCRFPortifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFPortifIndex.setStatus("mandatory")


class _DtrCRFPortEnable_Type(Integer32):
    """Custom type dtrCRFPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_DtrCRFPortEnable_Type.__name__ = "Integer32"
_DtrCRFPortEnable_Object = MibTableColumn
dtrCRFPortEnable = _DtrCRFPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 1, 7, 1, 4),
    _DtrCRFPortEnable_Type()
)
dtrCRFPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrCRFPortEnable.setStatus("mandatory")
_DtrCRFOperPortType_Type = IANAifType
_DtrCRFOperPortType_Object = MibTableColumn
dtrCRFOperPortType = _DtrCRFOperPortType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 1, 7, 1, 5),
    _DtrCRFOperPortType_Type()
)
dtrCRFOperPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFOperPortType.setStatus("mandatory")
_DtrCRFPortMtuExceededDiscards_Type = Counter32
_DtrCRFPortMtuExceededDiscards_Object = MibTableColumn
dtrCRFPortMtuExceededDiscards = _DtrCRFPortMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 1, 7, 1, 6),
    _DtrCRFPortMtuExceededDiscards_Type()
)
dtrCRFPortMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFPortMtuExceededDiscards.setStatus("mandatory")
_DtrCRFPortDelayExceededDiscards_Type = Counter32
_DtrCRFPortDelayExceededDiscards_Object = MibTableColumn
dtrCRFPortDelayExceededDiscards = _DtrCRFPortDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 1, 7, 1, 7),
    _DtrCRFPortDelayExceededDiscards_Type()
)
dtrCRFPortDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFPortDelayExceededDiscards.setStatus("mandatory")
_DtrConcMIBSpTree_ObjectIdentity = ObjectIdentity
dtrConcMIBSpTree = _DtrConcMIBSpTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2)
)
_DtrSpanningTreeHoldTime_Type = Integer32
_DtrSpanningTreeHoldTime_Object = MibScalar
dtrSpanningTreeHoldTime = _DtrSpanningTreeHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 1),
    _DtrSpanningTreeHoldTime_Type()
)
dtrSpanningTreeHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrSpanningTreeHoldTime.setStatus("mandatory")


class _DtrSpanningTreeProtocolSpecification_Type(Integer32):
    """Custom type dtrSpanningTreeProtocolSpecification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ieee8021d", 3),
          ("unknown", 1))
    )


_DtrSpanningTreeProtocolSpecification_Type.__name__ = "Integer32"
_DtrSpanningTreeProtocolSpecification_Object = MibScalar
dtrSpanningTreeProtocolSpecification = _DtrSpanningTreeProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 2),
    _DtrSpanningTreeProtocolSpecification_Type()
)
dtrSpanningTreeProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrSpanningTreeProtocolSpecification.setStatus("mandatory")
_DtrSpanningTreeTimeSinceTopoChange_Type = TimeTicks
_DtrSpanningTreeTimeSinceTopoChange_Object = MibScalar
dtrSpanningTreeTimeSinceTopoChange = _DtrSpanningTreeTimeSinceTopoChange_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 3),
    _DtrSpanningTreeTimeSinceTopoChange_Type()
)
dtrSpanningTreeTimeSinceTopoChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrSpanningTreeTimeSinceTopoChange.setStatus("mandatory")
_DtrSpanningTreeTopologyChanges_Type = Counter32
_DtrSpanningTreeTopologyChanges_Object = MibScalar
dtrSpanningTreeTopologyChanges = _DtrSpanningTreeTopologyChanges_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 4),
    _DtrSpanningTreeTopologyChanges_Type()
)
dtrSpanningTreeTopologyChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrSpanningTreeTopologyChanges.setStatus("mandatory")


class _DtrSpanningTreeBridgeForwardDelay_Type(Timeout):
    """Custom type dtrSpanningTreeBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_DtrSpanningTreeBridgeForwardDelay_Type.__name__ = "Timeout"
_DtrSpanningTreeBridgeForwardDelay_Object = MibScalar
dtrSpanningTreeBridgeForwardDelay = _DtrSpanningTreeBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 5),
    _DtrSpanningTreeBridgeForwardDelay_Type()
)
dtrSpanningTreeBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrSpanningTreeBridgeForwardDelay.setStatus("mandatory")


class _DtrSpanningTreeBridgeHelloTime_Type(Timeout):
    """Custom type dtrSpanningTreeBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_DtrSpanningTreeBridgeHelloTime_Type.__name__ = "Timeout"
_DtrSpanningTreeBridgeHelloTime_Object = MibScalar
dtrSpanningTreeBridgeHelloTime = _DtrSpanningTreeBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 6),
    _DtrSpanningTreeBridgeHelloTime_Type()
)
dtrSpanningTreeBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrSpanningTreeBridgeHelloTime.setStatus("mandatory")


class _DtrSpanningTreeTreeBridgeMaxAge_Type(Integer32):
    """Custom type dtrSpanningTreeTreeBridgeMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_DtrSpanningTreeTreeBridgeMaxAge_Type.__name__ = "Integer32"
_DtrSpanningTreeTreeBridgeMaxAge_Object = MibScalar
dtrSpanningTreeTreeBridgeMaxAge = _DtrSpanningTreeTreeBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 7),
    _DtrSpanningTreeTreeBridgeMaxAge_Type()
)
dtrSpanningTreeTreeBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrSpanningTreeTreeBridgeMaxAge.setStatus("mandatory")
_DtrCRFSpTreeTable_Object = MibTable
dtrCRFSpTreeTable = _DtrCRFSpTreeTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 9)
)
if mibBuilder.loadTexts:
    dtrCRFSpTreeTable.setStatus("mandatory")
_DtrCRFSpTreeEntry_Object = MibTableRow
dtrCRFSpTreeEntry = _DtrCRFSpTreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 9, 1)
)
dtrCRFSpTreeEntry.setIndexNames(
    (0, "DTRConcentratorMIB", "dtrCRFSpTreeCRFIndex"),
)
if mibBuilder.loadTexts:
    dtrCRFSpTreeEntry.setStatus("mandatory")


class _DtrCRFSpTreeCRFIndex_Type(Integer32):
    """Custom type dtrCRFSpTreeCRFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DtrCRFSpTreeCRFIndex_Type.__name__ = "Integer32"
_DtrCRFSpTreeCRFIndex_Object = MibTableColumn
dtrCRFSpTreeCRFIndex = _DtrCRFSpTreeCRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 9, 1, 1),
    _DtrCRFSpTreeCRFIndex_Type()
)
dtrCRFSpTreeCRFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFSpTreeCRFIndex.setStatus("mandatory")


class _DtrCRFSpTreePriority_Type(Integer32):
    """Custom type dtrCRFSpTreePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DtrCRFSpTreePriority_Type.__name__ = "Integer32"
_DtrCRFSpTreePriority_Object = MibTableColumn
dtrCRFSpTreePriority = _DtrCRFSpTreePriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 9, 1, 2),
    _DtrCRFSpTreePriority_Type()
)
dtrCRFSpTreePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrCRFSpTreePriority.setStatus("mandatory")
_DtrCRFSpTreeDesignatedRoot_Type = BridgeId
_DtrCRFSpTreeDesignatedRoot_Object = MibTableColumn
dtrCRFSpTreeDesignatedRoot = _DtrCRFSpTreeDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 9, 1, 3),
    _DtrCRFSpTreeDesignatedRoot_Type()
)
dtrCRFSpTreeDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFSpTreeDesignatedRoot.setStatus("mandatory")
_DtrCRFSpTreeRootCost_Type = Integer32
_DtrCRFSpTreeRootCost_Object = MibTableColumn
dtrCRFSpTreeRootCost = _DtrCRFSpTreeRootCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 9, 1, 4),
    _DtrCRFSpTreeRootCost_Type()
)
dtrCRFSpTreeRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFSpTreeRootCost.setStatus("mandatory")
_DtrCRFSpTreeRootPort_Type = Integer32
_DtrCRFSpTreeRootPort_Object = MibTableColumn
dtrCRFSpTreeRootPort = _DtrCRFSpTreeRootPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 9, 1, 5),
    _DtrCRFSpTreeRootPort_Type()
)
dtrCRFSpTreeRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFSpTreeRootPort.setStatus("mandatory")
_DtrCRFSpTreeMaxAge_Type = Timeout
_DtrCRFSpTreeMaxAge_Object = MibTableColumn
dtrCRFSpTreeMaxAge = _DtrCRFSpTreeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 9, 1, 6),
    _DtrCRFSpTreeMaxAge_Type()
)
dtrCRFSpTreeMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFSpTreeMaxAge.setStatus("mandatory")
_DtrCRFSpTreeHelloTime_Type = Timeout
_DtrCRFSpTreeHelloTime_Object = MibTableColumn
dtrCRFSpTreeHelloTime = _DtrCRFSpTreeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 9, 1, 7),
    _DtrCRFSpTreeHelloTime_Type()
)
dtrCRFSpTreeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFSpTreeHelloTime.setStatus("mandatory")
_DtrCRFSpTreeForwardDelay_Type = Timeout
_DtrCRFSpTreeForwardDelay_Object = MibTableColumn
dtrCRFSpTreeForwardDelay = _DtrCRFSpTreeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 9, 1, 8),
    _DtrCRFSpTreeForwardDelay_Type()
)
dtrCRFSpTreeForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFSpTreeForwardDelay.setStatus("mandatory")
_DtrCRFPortSpTreeTable_Object = MibTable
dtrCRFPortSpTreeTable = _DtrCRFPortSpTreeTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 10)
)
if mibBuilder.loadTexts:
    dtrCRFPortSpTreeTable.setStatus("mandatory")
_DtrCRFPortSpTreeEntry_Object = MibTableRow
dtrCRFPortSpTreeEntry = _DtrCRFPortSpTreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 10, 1)
)
dtrCRFPortSpTreeEntry.setIndexNames(
    (0, "DTRConcentratorMIB", "dtrCRFPortSpTreeCRFIndex"),
    (0, "DTRConcentratorMIB", "dtrCRFPortSpTreeNumber"),
)
if mibBuilder.loadTexts:
    dtrCRFPortSpTreeEntry.setStatus("mandatory")


class _DtrCRFPortSpTreeCRFIndex_Type(Integer32):
    """Custom type dtrCRFPortSpTreeCRFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DtrCRFPortSpTreeCRFIndex_Type.__name__ = "Integer32"
_DtrCRFPortSpTreeCRFIndex_Object = MibTableColumn
dtrCRFPortSpTreeCRFIndex = _DtrCRFPortSpTreeCRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 10, 1, 1),
    _DtrCRFPortSpTreeCRFIndex_Type()
)
dtrCRFPortSpTreeCRFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFPortSpTreeCRFIndex.setStatus("mandatory")


class _DtrCRFPortSpTreeNumber_Type(Integer32):
    """Custom type dtrCRFPortSpTreeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DtrCRFPortSpTreeNumber_Type.__name__ = "Integer32"
_DtrCRFPortSpTreeNumber_Object = MibTableColumn
dtrCRFPortSpTreeNumber = _DtrCRFPortSpTreeNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 10, 1, 2),
    _DtrCRFPortSpTreeNumber_Type()
)
dtrCRFPortSpTreeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFPortSpTreeNumber.setStatus("mandatory")


class _DtrCRFPortSpTreePriority_Type(Integer32):
    """Custom type dtrCRFPortSpTreePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DtrCRFPortSpTreePriority_Type.__name__ = "Integer32"
_DtrCRFPortSpTreePriority_Object = MibTableColumn
dtrCRFPortSpTreePriority = _DtrCRFPortSpTreePriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 10, 1, 3),
    _DtrCRFPortSpTreePriority_Type()
)
dtrCRFPortSpTreePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrCRFPortSpTreePriority.setStatus("mandatory")


class _DtrCRFPortSpTreeState_Type(Integer32):
    """Custom type dtrCRFPortSpTreeState based on Integer32"""
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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_DtrCRFPortSpTreeState_Type.__name__ = "Integer32"
_DtrCRFPortSpTreeState_Object = MibTableColumn
dtrCRFPortSpTreeState = _DtrCRFPortSpTreeState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 10, 1, 4),
    _DtrCRFPortSpTreeState_Type()
)
dtrCRFPortSpTreeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFPortSpTreeState.setStatus("mandatory")


class _DtrCRFPortSpTreePathCost_Type(Integer32):
    """Custom type dtrCRFPortSpTreePathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DtrCRFPortSpTreePathCost_Type.__name__ = "Integer32"
_DtrCRFPortSpTreePathCost_Object = MibTableColumn
dtrCRFPortSpTreePathCost = _DtrCRFPortSpTreePathCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 10, 1, 5),
    _DtrCRFPortSpTreePathCost_Type()
)
dtrCRFPortSpTreePathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrCRFPortSpTreePathCost.setStatus("mandatory")
_DtrCRFPortSpTreeDesignatedRoot_Type = BridgeId
_DtrCRFPortSpTreeDesignatedRoot_Object = MibTableColumn
dtrCRFPortSpTreeDesignatedRoot = _DtrCRFPortSpTreeDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 10, 1, 6),
    _DtrCRFPortSpTreeDesignatedRoot_Type()
)
dtrCRFPortSpTreeDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFPortSpTreeDesignatedRoot.setStatus("mandatory")
_DtrCRFPortSpTreeDesignatedCost_Type = Integer32
_DtrCRFPortSpTreeDesignatedCost_Object = MibTableColumn
dtrCRFPortSpTreeDesignatedCost = _DtrCRFPortSpTreeDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 10, 1, 7),
    _DtrCRFPortSpTreeDesignatedCost_Type()
)
dtrCRFPortSpTreeDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFPortSpTreeDesignatedCost.setStatus("mandatory")
_DtrCRFPortSpTreeDesignatedBridge_Type = BridgeId
_DtrCRFPortSpTreeDesignatedBridge_Object = MibTableColumn
dtrCRFPortSpTreeDesignatedBridge = _DtrCRFPortSpTreeDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 10, 1, 8),
    _DtrCRFPortSpTreeDesignatedBridge_Type()
)
dtrCRFPortSpTreeDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFPortSpTreeDesignatedBridge.setStatus("mandatory")


class _DtrCRFPortSpTreeDesignatedPort_Type(OctetString):
    """Custom type dtrCRFPortSpTreeDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_DtrCRFPortSpTreeDesignatedPort_Type.__name__ = "OctetString"
_DtrCRFPortSpTreeDesignatedPort_Object = MibTableColumn
dtrCRFPortSpTreeDesignatedPort = _DtrCRFPortSpTreeDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 10, 1, 9),
    _DtrCRFPortSpTreeDesignatedPort_Type()
)
dtrCRFPortSpTreeDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFPortSpTreeDesignatedPort.setStatus("mandatory")
_DtrCRFPortSpTreeForwardTransitions_Type = Counter32
_DtrCRFPortSpTreeForwardTransitions_Object = MibTableColumn
dtrCRFPortSpTreeForwardTransitions = _DtrCRFPortSpTreeForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 2, 10, 1, 10),
    _DtrCRFPortSpTreeForwardTransitions_Type()
)
dtrCRFPortSpTreeForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFPortSpTreeForwardTransitions.setStatus("mandatory")
_DtrConcMIBForwarding_ObjectIdentity = ObjectIdentity
dtrConcMIBForwarding = _DtrConcMIBForwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 3)
)
_DtrFdbDynamicAddrTable_Object = MibTable
dtrFdbDynamicAddrTable = _DtrFdbDynamicAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dtrFdbDynamicAddrTable.setStatus("mandatory")
_DtrFdbDynamicAddrEntry_Object = MibTableRow
dtrFdbDynamicAddrEntry = _DtrFdbDynamicAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 3, 1, 1)
)
dtrFdbDynamicAddrEntry.setIndexNames(
    (0, "DTRConcentratorMIB", "dtrFdbDynamicAddrCRFIndex"),
    (0, "DTRConcentratorMIB", "dtrFdbDynamicAddrStnAddress"),
)
if mibBuilder.loadTexts:
    dtrFdbDynamicAddrEntry.setStatus("mandatory")


class _DtrFdbDynamicAddrCRFIndex_Type(Integer32):
    """Custom type dtrFdbDynamicAddrCRFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DtrFdbDynamicAddrCRFIndex_Type.__name__ = "Integer32"
_DtrFdbDynamicAddrCRFIndex_Object = MibTableColumn
dtrFdbDynamicAddrCRFIndex = _DtrFdbDynamicAddrCRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 3, 1, 1, 1),
    _DtrFdbDynamicAddrCRFIndex_Type()
)
dtrFdbDynamicAddrCRFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrFdbDynamicAddrCRFIndex.setStatus("mandatory")
_DtrFdbDynamicAddrStnAddress_Type = MacAddress
_DtrFdbDynamicAddrStnAddress_Object = MibTableColumn
dtrFdbDynamicAddrStnAddress = _DtrFdbDynamicAddrStnAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 3, 1, 1, 2),
    _DtrFdbDynamicAddrStnAddress_Type()
)
dtrFdbDynamicAddrStnAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrFdbDynamicAddrStnAddress.setStatus("mandatory")


class _DtrFdbDynamicAddrPortNumber_Type(Integer32):
    """Custom type dtrFdbDynamicAddrPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DtrFdbDynamicAddrPortNumber_Type.__name__ = "Integer32"
_DtrFdbDynamicAddrPortNumber_Object = MibTableColumn
dtrFdbDynamicAddrPortNumber = _DtrFdbDynamicAddrPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 3, 1, 1, 3),
    _DtrFdbDynamicAddrPortNumber_Type()
)
dtrFdbDynamicAddrPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrFdbDynamicAddrPortNumber.setStatus("mandatory")
_DtrFdbDynamicAddrStatus_Type = DynamicFdbStatus
_DtrFdbDynamicAddrStatus_Object = MibTableColumn
dtrFdbDynamicAddrStatus = _DtrFdbDynamicAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 3, 1, 1, 4),
    _DtrFdbDynamicAddrStatus_Type()
)
dtrFdbDynamicAddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrFdbDynamicAddrStatus.setStatus("mandatory")
_DtrFdbStaticAddrTable_Object = MibTable
dtrFdbStaticAddrTable = _DtrFdbStaticAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dtrFdbStaticAddrTable.setStatus("mandatory")
_DtrFdbStaticAddrEntry_Object = MibTableRow
dtrFdbStaticAddrEntry = _DtrFdbStaticAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 3, 2, 1)
)
dtrFdbStaticAddrEntry.setIndexNames(
    (0, "DTRConcentratorMIB", "dtrFdbStaticAddrCRFIndex"),
    (0, "DTRConcentratorMIB", "dtrFdbStaticAddrStnAddress"),
)
if mibBuilder.loadTexts:
    dtrFdbStaticAddrEntry.setStatus("mandatory")


class _DtrFdbStaticAddrCRFIndex_Type(Integer32):
    """Custom type dtrFdbStaticAddrCRFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DtrFdbStaticAddrCRFIndex_Type.__name__ = "Integer32"
_DtrFdbStaticAddrCRFIndex_Object = MibTableColumn
dtrFdbStaticAddrCRFIndex = _DtrFdbStaticAddrCRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 3, 2, 1, 1),
    _DtrFdbStaticAddrCRFIndex_Type()
)
dtrFdbStaticAddrCRFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrFdbStaticAddrCRFIndex.setStatus("mandatory")
_DtrFdbStaticAddrStnAddress_Type = MacAddress
_DtrFdbStaticAddrStnAddress_Object = MibTableColumn
dtrFdbStaticAddrStnAddress = _DtrFdbStaticAddrStnAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 3, 2, 1, 2),
    _DtrFdbStaticAddrStnAddress_Type()
)
dtrFdbStaticAddrStnAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrFdbStaticAddrStnAddress.setStatus("mandatory")
_DtrFdbStaticAddrRowStatus_Type = RowStatus
_DtrFdbStaticAddrRowStatus_Object = MibTableColumn
dtrFdbStaticAddrRowStatus = _DtrFdbStaticAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 3, 2, 1, 3),
    _DtrFdbStaticAddrRowStatus_Type()
)
dtrFdbStaticAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrFdbStaticAddrRowStatus.setStatus("mandatory")
_DtrFdbStaticAddrInMask_Type = OctetString
_DtrFdbStaticAddrInMask_Object = MibTableColumn
dtrFdbStaticAddrInMask = _DtrFdbStaticAddrInMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 3, 2, 1, 4),
    _DtrFdbStaticAddrInMask_Type()
)
dtrFdbStaticAddrInMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrFdbStaticAddrInMask.setStatus("mandatory")
_DtrFdbStaticAddrOutMask_Type = OctetString
_DtrFdbStaticAddrOutMask_Object = MibTableColumn
dtrFdbStaticAddrOutMask = _DtrFdbStaticAddrOutMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 3, 2, 1, 5),
    _DtrFdbStaticAddrOutMask_Type()
)
dtrFdbStaticAddrOutMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrFdbStaticAddrOutMask.setStatus("mandatory")
_DtrFdbStaticAddrStatus_Type = StaticFdbStatus
_DtrFdbStaticAddrStatus_Object = MibTableColumn
dtrFdbStaticAddrStatus = _DtrFdbStaticAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 3, 2, 1, 6),
    _DtrFdbStaticAddrStatus_Type()
)
dtrFdbStaticAddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrFdbStaticAddrStatus.setStatus("mandatory")
_DtrFdbDynamicRDTable_Object = MibTable
dtrFdbDynamicRDTable = _DtrFdbDynamicRDTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    dtrFdbDynamicRDTable.setStatus("mandatory")
_DtrFdbDynamicRDEntry_Object = MibTableRow
dtrFdbDynamicRDEntry = _DtrFdbDynamicRDEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 3, 3, 1)
)
dtrFdbDynamicRDEntry.setIndexNames(
    (0, "DTRConcentratorMIB", "dtrFdbDynamicRDCRFIndex"),
    (0, "DTRConcentratorMIB", "dtrFdbDynamicRDRouteDesc"),
)
if mibBuilder.loadTexts:
    dtrFdbDynamicRDEntry.setStatus("mandatory")


class _DtrFdbDynamicRDCRFIndex_Type(Integer32):
    """Custom type dtrFdbDynamicRDCRFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DtrFdbDynamicRDCRFIndex_Type.__name__ = "Integer32"
_DtrFdbDynamicRDCRFIndex_Object = MibTableColumn
dtrFdbDynamicRDCRFIndex = _DtrFdbDynamicRDCRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 3, 3, 1, 1),
    _DtrFdbDynamicRDCRFIndex_Type()
)
dtrFdbDynamicRDCRFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrFdbDynamicRDCRFIndex.setStatus("mandatory")
_DtrFdbDynamicRDRouteDesc_Type = RouteDescriptor
_DtrFdbDynamicRDRouteDesc_Object = MibTableColumn
dtrFdbDynamicRDRouteDesc = _DtrFdbDynamicRDRouteDesc_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 3, 3, 1, 2),
    _DtrFdbDynamicRDRouteDesc_Type()
)
dtrFdbDynamicRDRouteDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrFdbDynamicRDRouteDesc.setStatus("mandatory")


class _DtrFdbDynamicRDPortNumber_Type(Integer32):
    """Custom type dtrFdbDynamicRDPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DtrFdbDynamicRDPortNumber_Type.__name__ = "Integer32"
_DtrFdbDynamicRDPortNumber_Object = MibTableColumn
dtrFdbDynamicRDPortNumber = _DtrFdbDynamicRDPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 3, 3, 1, 3),
    _DtrFdbDynamicRDPortNumber_Type()
)
dtrFdbDynamicRDPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrFdbDynamicRDPortNumber.setStatus("mandatory")
_DtrFdbDynamicRDStatus_Type = DynamicFdbStatus
_DtrFdbDynamicRDStatus_Object = MibTableColumn
dtrFdbDynamicRDStatus = _DtrFdbDynamicRDStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 3, 3, 1, 4),
    _DtrFdbDynamicRDStatus_Type()
)
dtrFdbDynamicRDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrFdbDynamicRDStatus.setStatus("mandatory")
_DtrFdbStaticRDTable_Object = MibTable
dtrFdbStaticRDTable = _DtrFdbStaticRDTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    dtrFdbStaticRDTable.setStatus("mandatory")
_DtrFdbStaticRDEntry_Object = MibTableRow
dtrFdbStaticRDEntry = _DtrFdbStaticRDEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 3, 5, 1)
)
dtrFdbStaticRDEntry.setIndexNames(
    (0, "DTRConcentratorMIB", "dtrFdbStaticRDCRFIndex"),
    (0, "DTRConcentratorMIB", "dtrFdbStaticRDRouteDesc"),
)
if mibBuilder.loadTexts:
    dtrFdbStaticRDEntry.setStatus("mandatory")


class _DtrFdbStaticRDCRFIndex_Type(Integer32):
    """Custom type dtrFdbStaticRDCRFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DtrFdbStaticRDCRFIndex_Type.__name__ = "Integer32"
_DtrFdbStaticRDCRFIndex_Object = MibTableColumn
dtrFdbStaticRDCRFIndex = _DtrFdbStaticRDCRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 3, 5, 1, 1),
    _DtrFdbStaticRDCRFIndex_Type()
)
dtrFdbStaticRDCRFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrFdbStaticRDCRFIndex.setStatus("mandatory")
_DtrFdbStaticRDRouteDesc_Type = RouteDescriptor
_DtrFdbStaticRDRouteDesc_Object = MibTableColumn
dtrFdbStaticRDRouteDesc = _DtrFdbStaticRDRouteDesc_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 3, 5, 1, 2),
    _DtrFdbStaticRDRouteDesc_Type()
)
dtrFdbStaticRDRouteDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrFdbStaticRDRouteDesc.setStatus("mandatory")
_DtrFdbStaticRDRowStatus_Type = RowStatus
_DtrFdbStaticRDRowStatus_Object = MibTableColumn
dtrFdbStaticRDRowStatus = _DtrFdbStaticRDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 3, 5, 1, 3),
    _DtrFdbStaticRDRowStatus_Type()
)
dtrFdbStaticRDRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrFdbStaticRDRowStatus.setStatus("mandatory")


class _DtrFdbStaticRDPortNumber_Type(Integer32):
    """Custom type dtrFdbStaticRDPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DtrFdbStaticRDPortNumber_Type.__name__ = "Integer32"
_DtrFdbStaticRDPortNumber_Object = MibTableColumn
dtrFdbStaticRDPortNumber = _DtrFdbStaticRDPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 3, 5, 1, 4),
    _DtrFdbStaticRDPortNumber_Type()
)
dtrFdbStaticRDPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrFdbStaticRDPortNumber.setStatus("mandatory")
_DtrFdbStaticRDStatus_Type = StaticFdbStatus
_DtrFdbStaticRDStatus_Object = MibTableColumn
dtrFdbStaticRDStatus = _DtrFdbStaticRDStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 3, 5, 1, 5),
    _DtrFdbStaticRDStatus_Type()
)
dtrFdbStaticRDStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrFdbStaticRDStatus.setStatus("mandatory")
_DtrConcMIBMRI_ObjectIdentity = ObjectIdentity
dtrConcMIBMRI = _DtrConcMIBMRI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 4)
)
_DtrMRITable_Object = MibTable
dtrMRITable = _DtrMRITable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dtrMRITable.setStatus("mandatory")
_DtrMRIEntry_Object = MibTableRow
dtrMRIEntry = _DtrMRIEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 4, 1, 1)
)
dtrMRIEntry.setIndexNames(
    (0, "DTRConcentratorMIB", "dtrMRICRFIndex"),
    (0, "DTRConcentratorMIB", "dtrMRIMgmtType"),
)
if mibBuilder.loadTexts:
    dtrMRIEntry.setStatus("mandatory")


class _DtrMRICRFIndex_Type(Integer32):
    """Custom type dtrMRICRFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DtrMRICRFIndex_Type.__name__ = "Integer32"
_DtrMRICRFIndex_Object = MibTableColumn
dtrMRICRFIndex = _DtrMRICRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 4, 1, 1, 1),
    _DtrMRICRFIndex_Type()
)
dtrMRICRFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrMRICRFIndex.setStatus("mandatory")


class _DtrMRIMgmtType_Type(Integer32):
    """Custom type dtrMRIMgmtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DtrMRIMgmtType_Type.__name__ = "Integer32"
_DtrMRIMgmtType_Object = MibTableColumn
dtrMRIMgmtType = _DtrMRIMgmtType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 4, 1, 1, 2),
    _DtrMRIMgmtType_Type()
)
dtrMRIMgmtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrMRIMgmtType.setStatus("mandatory")
_DtrMRIOutMask_Type = OctetString
_DtrMRIOutMask_Object = MibTableColumn
dtrMRIOutMask = _DtrMRIOutMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 4, 1, 1, 3),
    _DtrMRIOutMask_Type()
)
dtrMRIOutMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrMRIOutMask.setStatus("mandatory")
_DtrConcMIBStats_ObjectIdentity = ObjectIdentity
dtrConcMIBStats = _DtrConcMIBStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 5)
)
_DtrCRFPortStatsTable_Object = MibTable
dtrCRFPortStatsTable = _DtrCRFPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    dtrCRFPortStatsTable.setStatus("mandatory")
_DtrCRFPortStatsEntry_Object = MibTableRow
dtrCRFPortStatsEntry = _DtrCRFPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 5, 1, 1)
)
dtrCRFPortStatsEntry.setIndexNames(
    (0, "DTRConcentratorMIB", "dtrCRFPortStatsCRFIndex"),
    (0, "DTRConcentratorMIB", "dtrCRFPortStatsPortNumber"),
)
if mibBuilder.loadTexts:
    dtrCRFPortStatsEntry.setStatus("mandatory")


class _DtrCRFPortStatsCRFIndex_Type(Integer32):
    """Custom type dtrCRFPortStatsCRFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DtrCRFPortStatsCRFIndex_Type.__name__ = "Integer32"
_DtrCRFPortStatsCRFIndex_Object = MibTableColumn
dtrCRFPortStatsCRFIndex = _DtrCRFPortStatsCRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 5, 1, 1, 1),
    _DtrCRFPortStatsCRFIndex_Type()
)
dtrCRFPortStatsCRFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFPortStatsCRFIndex.setStatus("mandatory")


class _DtrCRFPortStatsPortNumber_Type(Integer32):
    """Custom type dtrCRFPortStatsPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DtrCRFPortStatsPortNumber_Type.__name__ = "Integer32"
_DtrCRFPortStatsPortNumber_Object = MibTableColumn
dtrCRFPortStatsPortNumber = _DtrCRFPortStatsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 5, 1, 1, 2),
    _DtrCRFPortStatsPortNumber_Type()
)
dtrCRFPortStatsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFPortStatsPortNumber.setStatus("mandatory")
_DtrCRFPortStatsAreInFrames_Type = Counter32
_DtrCRFPortStatsAreInFrames_Object = MibTableColumn
dtrCRFPortStatsAreInFrames = _DtrCRFPortStatsAreInFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 5, 1, 1, 3),
    _DtrCRFPortStatsAreInFrames_Type()
)
dtrCRFPortStatsAreInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFPortStatsAreInFrames.setStatus("mandatory")
_DtrCRFPortStatsAreOutFrames_Type = Counter32
_DtrCRFPortStatsAreOutFrames_Object = MibTableColumn
dtrCRFPortStatsAreOutFrames = _DtrCRFPortStatsAreOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 5, 1, 1, 4),
    _DtrCRFPortStatsAreOutFrames_Type()
)
dtrCRFPortStatsAreOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFPortStatsAreOutFrames.setStatus("mandatory")
_DtrCRFPortStatsInFrames_Type = Counter32
_DtrCRFPortStatsInFrames_Object = MibTableColumn
dtrCRFPortStatsInFrames = _DtrCRFPortStatsInFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 5, 1, 1, 5),
    _DtrCRFPortStatsInFrames_Type()
)
dtrCRFPortStatsInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFPortStatsInFrames.setStatus("mandatory")
_DtrCRFPortStatsOutFrames_Type = Counter32
_DtrCRFPortStatsOutFrames_Object = MibTableColumn
dtrCRFPortStatsOutFrames = _DtrCRFPortStatsOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 5, 1, 1, 6),
    _DtrCRFPortStatsOutFrames_Type()
)
dtrCRFPortStatsOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFPortStatsOutFrames.setStatus("mandatory")
_DtrCRFPortStatsSrfInFrames_Type = Counter32
_DtrCRFPortStatsSrfInFrames_Object = MibTableColumn
dtrCRFPortStatsSrfInFrames = _DtrCRFPortStatsSrfInFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 5, 1, 1, 7),
    _DtrCRFPortStatsSrfInFrames_Type()
)
dtrCRFPortStatsSrfInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFPortStatsSrfInFrames.setStatus("mandatory")
_DtrCRFPortStatsSrfOutFrames_Type = Counter32
_DtrCRFPortStatsSrfOutFrames_Object = MibTableColumn
dtrCRFPortStatsSrfOutFrames = _DtrCRFPortStatsSrfOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 5, 1, 1, 8),
    _DtrCRFPortStatsSrfOutFrames_Type()
)
dtrCRFPortStatsSrfOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFPortStatsSrfOutFrames.setStatus("mandatory")
_DtrCRFPortStatsSteInFrames_Type = Counter32
_DtrCRFPortStatsSteInFrames_Object = MibTableColumn
dtrCRFPortStatsSteInFrames = _DtrCRFPortStatsSteInFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 5, 1, 1, 9),
    _DtrCRFPortStatsSteInFrames_Type()
)
dtrCRFPortStatsSteInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFPortStatsSteInFrames.setStatus("mandatory")
_DtrCRFPortStatsSteOutFrames_Type = Counter32
_DtrCRFPortStatsSteOutFrames_Object = MibTableColumn
dtrCRFPortStatsSteOutFrames = _DtrCRFPortStatsSteOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 5, 1, 1, 10),
    _DtrCRFPortStatsSteOutFrames_Type()
)
dtrCRFPortStatsSteOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFPortStatsSteOutFrames.setStatus("mandatory")
_DtrCRFPortStatsInvalidRI_Type = Counter32
_DtrCRFPortStatsInvalidRI_Object = MibTableColumn
dtrCRFPortStatsInvalidRI = _DtrCRFPortStatsInvalidRI_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 5, 1, 1, 11),
    _DtrCRFPortStatsInvalidRI_Type()
)
dtrCRFPortStatsInvalidRI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFPortStatsInvalidRI.setStatus("mandatory")
_DtrCRFPortStatsInMisdirected_Type = Counter32
_DtrCRFPortStatsInMisdirected_Object = MibTableColumn
dtrCRFPortStatsInMisdirected = _DtrCRFPortStatsInMisdirected_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 5, 1, 1, 12),
    _DtrCRFPortStatsInMisdirected_Type()
)
dtrCRFPortStatsInMisdirected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFPortStatsInMisdirected.setStatus("mandatory")
_DtrCRFPortStatsInDiscards_Type = Counter32
_DtrCRFPortStatsInDiscards_Object = MibTableColumn
dtrCRFPortStatsInDiscards = _DtrCRFPortStatsInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 1, 1, 5, 1, 1, 13),
    _DtrCRFPortStatsInDiscards_Type()
)
dtrCRFPortStatsInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrCRFPortStatsInDiscards.setStatus("mandatory")
_DtrMacMIB_ObjectIdentity = ObjectIdentity
dtrMacMIB = _DtrMacMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 2)
)
_DtrExt_ObjectIdentity = ObjectIdentity
dtrExt = _DtrExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3)
)
_DtrExSrbGlobal_ObjectIdentity = ObjectIdentity
dtrExSrbGlobal = _DtrExSrbGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 1)
)


class _DtrExSrbBridgeNumber_Type(Integer32):
    """Custom type dtrExSrbBridgeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DtrExSrbBridgeNumber_Type.__name__ = "Integer32"
_DtrExSrbBridgeNumber_Object = MibScalar
dtrExSrbBridgeNumber = _DtrExSrbBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 1, 1),
    _DtrExSrbBridgeNumber_Type()
)
dtrExSrbBridgeNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrExSrbBridgeNumber.setStatus("mandatory")


class _DtrExSrbBridgeNumberOfCrfs_Type(Integer32):
    """Custom type dtrExSrbBridgeNumberOfCrfs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_DtrExSrbBridgeNumberOfCrfs_Type.__name__ = "Integer32"
_DtrExSrbBridgeNumberOfCrfs_Object = MibScalar
dtrExSrbBridgeNumberOfCrfs = _DtrExSrbBridgeNumberOfCrfs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 1, 2),
    _DtrExSrbBridgeNumberOfCrfs_Type()
)
dtrExSrbBridgeNumberOfCrfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrExSrbBridgeNumberOfCrfs.setStatus("mandatory")
_DtrExSrbStp_ObjectIdentity = ObjectIdentity
dtrExSrbStp = _DtrExSrbStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 2)
)
_DtrExSrbStpGlobal_ObjectIdentity = ObjectIdentity
dtrExSrbStpGlobal = _DtrExSrbStpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 2, 1)
)


class _DtrExSrbStpPriority_Type(Integer32):
    """Custom type dtrExSrbStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DtrExSrbStpPriority_Type.__name__ = "Integer32"
_DtrExSrbStpPriority_Object = MibScalar
dtrExSrbStpPriority = _DtrExSrbStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 2, 1, 1),
    _DtrExSrbStpPriority_Type()
)
dtrExSrbStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrExSrbStpPriority.setStatus("mandatory")
_DtrExSrbStpAddress_Type = MacAddress
_DtrExSrbStpAddress_Object = MibScalar
dtrExSrbStpAddress = _DtrExSrbStpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 2, 1, 2),
    _DtrExSrbStpAddress_Type()
)
dtrExSrbStpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrExSrbStpAddress.setStatus("mandatory")


class _DtrExSrbStpBridgeMaxAge_Type(Timeout):
    """Custom type dtrExSrbStpBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_DtrExSrbStpBridgeMaxAge_Type.__name__ = "Timeout"
_DtrExSrbStpBridgeMaxAge_Object = MibScalar
dtrExSrbStpBridgeMaxAge = _DtrExSrbStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 2, 1, 3),
    _DtrExSrbStpBridgeMaxAge_Type()
)
dtrExSrbStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrExSrbStpBridgeMaxAge.setStatus("mandatory")


class _DtrExSrbStpBridgeHelloTime_Type(Timeout):
    """Custom type dtrExSrbStpBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_DtrExSrbStpBridgeHelloTime_Type.__name__ = "Timeout"
_DtrExSrbStpBridgeHelloTime_Object = MibScalar
dtrExSrbStpBridgeHelloTime = _DtrExSrbStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 2, 1, 4),
    _DtrExSrbStpBridgeHelloTime_Type()
)
dtrExSrbStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrExSrbStpBridgeHelloTime.setStatus("mandatory")


class _DtrExSrbStpBridgeForwardDelay_Type(Timeout):
    """Custom type dtrExSrbStpBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_DtrExSrbStpBridgeForwardDelay_Type.__name__ = "Timeout"
_DtrExSrbStpBridgeForwardDelay_Object = MibScalar
dtrExSrbStpBridgeForwardDelay = _DtrExSrbStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 2, 1, 5),
    _DtrExSrbStpBridgeForwardDelay_Type()
)
dtrExSrbStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrExSrbStpBridgeForwardDelay.setStatus("mandatory")
_DtrExSrbStpDesignatedRoot_Type = BridgeId
_DtrExSrbStpDesignatedRoot_Object = MibScalar
dtrExSrbStpDesignatedRoot = _DtrExSrbStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 2, 1, 6),
    _DtrExSrbStpDesignatedRoot_Type()
)
dtrExSrbStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrExSrbStpDesignatedRoot.setStatus("mandatory")
_DtrExSrbStpRootCost_Type = Integer32
_DtrExSrbStpRootCost_Object = MibScalar
dtrExSrbStpRootCost = _DtrExSrbStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 2, 1, 7),
    _DtrExSrbStpRootCost_Type()
)
dtrExSrbStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrExSrbStpRootCost.setStatus("mandatory")
_DtrExSrbStpRootPort_Type = PortId
_DtrExSrbStpRootPort_Object = MibScalar
dtrExSrbStpRootPort = _DtrExSrbStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 2, 1, 8),
    _DtrExSrbStpRootPort_Type()
)
dtrExSrbStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrExSrbStpRootPort.setStatus("mandatory")


class _DtrExSrbStpMaxAge_Type(Timeout):
    """Custom type dtrExSrbStpMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DtrExSrbStpMaxAge_Type.__name__ = "Timeout"
_DtrExSrbStpMaxAge_Object = MibScalar
dtrExSrbStpMaxAge = _DtrExSrbStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 2, 1, 9),
    _DtrExSrbStpMaxAge_Type()
)
dtrExSrbStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrExSrbStpMaxAge.setStatus("mandatory")


class _DtrExSrbStpHelloTime_Type(Timeout):
    """Custom type dtrExSrbStpHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DtrExSrbStpHelloTime_Type.__name__ = "Timeout"
_DtrExSrbStpHelloTime_Object = MibScalar
dtrExSrbStpHelloTime = _DtrExSrbStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 2, 1, 10),
    _DtrExSrbStpHelloTime_Type()
)
dtrExSrbStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrExSrbStpHelloTime.setStatus("mandatory")
_DtrExSrbStpHoldTime_Type = Integer32
_DtrExSrbStpHoldTime_Object = MibScalar
dtrExSrbStpHoldTime = _DtrExSrbStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 2, 1, 11),
    _DtrExSrbStpHoldTime_Type()
)
dtrExSrbStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrExSrbStpHoldTime.setStatus("mandatory")


class _DtrExSrbStpForwardDelay_Type(Timeout):
    """Custom type dtrExSrbStpForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DtrExSrbStpForwardDelay_Type.__name__ = "Timeout"
_DtrExSrbStpForwardDelay_Object = MibScalar
dtrExSrbStpForwardDelay = _DtrExSrbStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 2, 1, 12),
    _DtrExSrbStpForwardDelay_Type()
)
dtrExSrbStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrExSrbStpForwardDelay.setStatus("mandatory")


class _DtrExSrbStpMode_Type(Integer32):
    """Custom type dtrExSrbStpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 0))
    )


_DtrExSrbStpMode_Type.__name__ = "Integer32"
_DtrExSrbStpMode_Object = MibScalar
dtrExSrbStpMode = _DtrExSrbStpMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 2, 1, 13),
    _DtrExSrbStpMode_Type()
)
dtrExSrbStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrExSrbStpMode.setStatus("mandatory")
_DtrExSrbPortStpTable_Object = MibTable
dtrExSrbPortStpTable = _DtrExSrbPortStpTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    dtrExSrbPortStpTable.setStatus("mandatory")
_DtrExSrbPortStpEntry_Object = MibTableRow
dtrExSrbPortStpEntry = _DtrExSrbPortStpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 2, 2, 1)
)
dtrExSrbPortStpEntry.setIndexNames(
    (0, "DTRConcentratorMIB", "dtrExSrbPortStpCRFIndex"),
    (0, "DTRConcentratorMIB", "dtrExSrbPortStpPort"),
)
if mibBuilder.loadTexts:
    dtrExSrbPortStpEntry.setStatus("mandatory")


class _DtrExSrbPortStpCRFIndex_Type(Integer32):
    """Custom type dtrExSrbPortStpCRFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DtrExSrbPortStpCRFIndex_Type.__name__ = "Integer32"
_DtrExSrbPortStpCRFIndex_Object = MibTableColumn
dtrExSrbPortStpCRFIndex = _DtrExSrbPortStpCRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 2, 2, 1, 1),
    _DtrExSrbPortStpCRFIndex_Type()
)
dtrExSrbPortStpCRFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrExSrbPortStpCRFIndex.setStatus("mandatory")


class _DtrExSrbPortStpPort_Type(Integer32):
    """Custom type dtrExSrbPortStpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 563),
    )


_DtrExSrbPortStpPort_Type.__name__ = "Integer32"
_DtrExSrbPortStpPort_Object = MibTableColumn
dtrExSrbPortStpPort = _DtrExSrbPortStpPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 2, 2, 1, 2),
    _DtrExSrbPortStpPort_Type()
)
dtrExSrbPortStpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrExSrbPortStpPort.setStatus("mandatory")


class _DtrExSrbPortStpPriority_Type(Integer32):
    """Custom type dtrExSrbPortStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_DtrExSrbPortStpPriority_Type.__name__ = "Integer32"
_DtrExSrbPortStpPriority_Object = MibTableColumn
dtrExSrbPortStpPriority = _DtrExSrbPortStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 2, 2, 1, 3),
    _DtrExSrbPortStpPriority_Type()
)
dtrExSrbPortStpPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrExSrbPortStpPriority.setStatus("mandatory")


class _DtrExSrbPortStpState_Type(Integer32):
    """Custom type dtrExSrbPortStpState based on Integer32"""
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
        *(("blocking", 2),
          ("broken", 5),
          ("disabled", 1),
          ("forwarding", 4),
          ("listening", 3))
    )


_DtrExSrbPortStpState_Type.__name__ = "Integer32"
_DtrExSrbPortStpState_Object = MibTableColumn
dtrExSrbPortStpState = _DtrExSrbPortStpState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 2, 2, 1, 4),
    _DtrExSrbPortStpState_Type()
)
dtrExSrbPortStpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrExSrbPortStpState.setStatus("mandatory")


class _DtrExSrbPortStpPathCost_Type(Integer32):
    """Custom type dtrExSrbPortStpPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DtrExSrbPortStpPathCost_Type.__name__ = "Integer32"
_DtrExSrbPortStpPathCost_Object = MibTableColumn
dtrExSrbPortStpPathCost = _DtrExSrbPortStpPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 2, 2, 1, 5),
    _DtrExSrbPortStpPathCost_Type()
)
dtrExSrbPortStpPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrExSrbPortStpPathCost.setStatus("mandatory")
_DtrExSrbPortStpDesignatedRoot_Type = BridgeId
_DtrExSrbPortStpDesignatedRoot_Object = MibTableColumn
dtrExSrbPortStpDesignatedRoot = _DtrExSrbPortStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 2, 2, 1, 6),
    _DtrExSrbPortStpDesignatedRoot_Type()
)
dtrExSrbPortStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrExSrbPortStpDesignatedRoot.setStatus("mandatory")
_DtrExSrbPortStpDesignatedCost_Type = Integer32
_DtrExSrbPortStpDesignatedCost_Object = MibTableColumn
dtrExSrbPortStpDesignatedCost = _DtrExSrbPortStpDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 2, 2, 1, 7),
    _DtrExSrbPortStpDesignatedCost_Type()
)
dtrExSrbPortStpDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrExSrbPortStpDesignatedCost.setStatus("mandatory")
_DtrExSrbPortStpDesignatedBridge_Type = BridgeId
_DtrExSrbPortStpDesignatedBridge_Object = MibTableColumn
dtrExSrbPortStpDesignatedBridge = _DtrExSrbPortStpDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 2, 2, 1, 8),
    _DtrExSrbPortStpDesignatedBridge_Type()
)
dtrExSrbPortStpDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrExSrbPortStpDesignatedBridge.setStatus("mandatory")
_DtrExSrbPortStpDesignatedPort_Type = PortId
_DtrExSrbPortStpDesignatedPort_Object = MibTableColumn
dtrExSrbPortStpDesignatedPort = _DtrExSrbPortStpDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 2, 2, 1, 9),
    _DtrExSrbPortStpDesignatedPort_Type()
)
dtrExSrbPortStpDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrExSrbPortStpDesignatedPort.setStatus("mandatory")
_DtrExSrbPortStpForwardTrans_Type = Counter32
_DtrExSrbPortStpForwardTrans_Object = MibTableColumn
dtrExSrbPortStpForwardTrans = _DtrExSrbPortStpForwardTrans_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 2, 2, 1, 10),
    _DtrExSrbPortStpForwardTrans_Type()
)
dtrExSrbPortStpForwardTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrExSrbPortStpForwardTrans.setStatus("mandatory")
_DtrExSrbPortHopTable_Object = MibTable
dtrExSrbPortHopTable = _DtrExSrbPortHopTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    dtrExSrbPortHopTable.setStatus("mandatory")
_DtrExSrbPortHopEntry_Object = MibTableRow
dtrExSrbPortHopEntry = _DtrExSrbPortHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 3, 1)
)
dtrExSrbPortHopEntry.setIndexNames(
    (0, "DTRConcentratorMIB", "dtrExSrbPortHopCRFIndex"),
    (0, "DTRConcentratorMIB", "dtrExSrbPortHopPort"),
)
if mibBuilder.loadTexts:
    dtrExSrbPortHopEntry.setStatus("mandatory")


class _DtrExSrbPortHopCRFIndex_Type(Integer32):
    """Custom type dtrExSrbPortHopCRFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DtrExSrbPortHopCRFIndex_Type.__name__ = "Integer32"
_DtrExSrbPortHopCRFIndex_Object = MibTableColumn
dtrExSrbPortHopCRFIndex = _DtrExSrbPortHopCRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 3, 1, 1),
    _DtrExSrbPortHopCRFIndex_Type()
)
dtrExSrbPortHopCRFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrExSrbPortHopCRFIndex.setStatus("mandatory")


class _DtrExSrbPortHopPort_Type(Integer32):
    """Custom type dtrExSrbPortHopPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 563),
    )


_DtrExSrbPortHopPort_Type.__name__ = "Integer32"
_DtrExSrbPortHopPort_Object = MibTableColumn
dtrExSrbPortHopPort = _DtrExSrbPortHopPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 3, 1, 2),
    _DtrExSrbPortHopPort_Type()
)
dtrExSrbPortHopPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtrExSrbPortHopPort.setStatus("mandatory")


class _DtrExSrbPortHopAreRcvMax_Type(Integer32):
    """Custom type dtrExSrbPortHopAreRcvMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_DtrExSrbPortHopAreRcvMax_Type.__name__ = "Integer32"
_DtrExSrbPortHopAreRcvMax_Object = MibTableColumn
dtrExSrbPortHopAreRcvMax = _DtrExSrbPortHopAreRcvMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 3, 1, 3),
    _DtrExSrbPortHopAreRcvMax_Type()
)
dtrExSrbPortHopAreRcvMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrExSrbPortHopAreRcvMax.setStatus("mandatory")


class _DtrExSrbPortHopAreXmtMax_Type(Integer32):
    """Custom type dtrExSrbPortHopAreXmtMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_DtrExSrbPortHopAreXmtMax_Type.__name__ = "Integer32"
_DtrExSrbPortHopAreXmtMax_Object = MibTableColumn
dtrExSrbPortHopAreXmtMax = _DtrExSrbPortHopAreXmtMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 3, 1, 4),
    _DtrExSrbPortHopAreXmtMax_Type()
)
dtrExSrbPortHopAreXmtMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrExSrbPortHopAreXmtMax.setStatus("mandatory")


class _DtrExSrbPortHopSteRcvMax_Type(Integer32):
    """Custom type dtrExSrbPortHopSteRcvMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_DtrExSrbPortHopSteRcvMax_Type.__name__ = "Integer32"
_DtrExSrbPortHopSteRcvMax_Object = MibTableColumn
dtrExSrbPortHopSteRcvMax = _DtrExSrbPortHopSteRcvMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 3, 1, 5),
    _DtrExSrbPortHopSteRcvMax_Type()
)
dtrExSrbPortHopSteRcvMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrExSrbPortHopSteRcvMax.setStatus("mandatory")


class _DtrExSrbPortHopSteXmtMax_Type(Integer32):
    """Custom type dtrExSrbPortHopSteXmtMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_DtrExSrbPortHopSteXmtMax_Type.__name__ = "Integer32"
_DtrExSrbPortHopSteXmtMax_Object = MibTableColumn
dtrExSrbPortHopSteXmtMax = _DtrExSrbPortHopSteXmtMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 66, 1, 3, 1, 3, 3, 1, 6),
    _DtrExSrbPortHopSteXmtMax_Type()
)
dtrExSrbPortHopSteXmtMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtrExSrbPortHopSteXmtMax.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DTRConcentratorMIB",
    **{"Counter32": Counter32,
       "Integer32": Integer32,
       "RowStatus": RowStatus,
       "MacAddress": MacAddress,
       "InterfaceIndex": InterfaceIndex,
       "IANAifType": IANAifType,
       "BridgeId": BridgeId,
       "DynamicFdbStatus": DynamicFdbStatus,
       "StaticFdbStatus": StaticFdbStatus,
       "PortId": PortId,
       "RouteDescriptor": RouteDescriptor,
       "Timeout": Timeout,
       "ibm": ibm,
       "ibmProd": ibmProd,
       "ibm8272": ibm8272,
       "ibm8272Ts": ibm8272Ts,
       "ibm8272TsExpMIBs": ibm8272TsExpMIBs,
       "dtrMIBs": dtrMIBs,
       "dtrConcMIB": dtrConcMIB,
       "dtrConcMIBObjects": dtrConcMIBObjects,
       "dtrConcMIBBase": dtrConcMIBBase,
       "dtrConcentratorAddress": dtrConcentratorAddress,
       "dtrOperNumberOfCrfs": dtrOperNumberOfCrfs,
       "dtrOperNumberOfBridgeRelays": dtrOperNumberOfBridgeRelays,
       "dtrCRFTable": dtrCRFTable,
       "dtrCRFEntry": dtrCRFEntry,
       "dtrCRFIndex": dtrCRFIndex,
       "dtrCRFNumberOfPorts": dtrCRFNumberOfPorts,
       "dtrCRFPortMask": dtrCRFPortMask,
       "dtrCRFName": dtrCRFName,
       "dtrCRFMaxInfo": dtrCRFMaxInfo,
       "dtrCRFMacAddress": dtrCRFMacAddress,
       "dtrCRFLocalLanId": dtrCRFLocalLanId,
       "dtrCRFFdbAgingTime": dtrCRFFdbAgingTime,
       "dtrCRFMRIEnable": dtrCRFMRIEnable,
       "dtrCRFLearnedEntryDiscards": dtrCRFLearnedEntryDiscards,
       "dtrCRFPortTable": dtrCRFPortTable,
       "dtrCRFPortEntry": dtrCRFPortEntry,
       "dtrCRFPortCRFIndex": dtrCRFPortCRFIndex,
       "dtrCRFPortNumber": dtrCRFPortNumber,
       "dtrCRFPortifIndex": dtrCRFPortifIndex,
       "dtrCRFPortEnable": dtrCRFPortEnable,
       "dtrCRFOperPortType": dtrCRFOperPortType,
       "dtrCRFPortMtuExceededDiscards": dtrCRFPortMtuExceededDiscards,
       "dtrCRFPortDelayExceededDiscards": dtrCRFPortDelayExceededDiscards,
       "dtrConcMIBSpTree": dtrConcMIBSpTree,
       "dtrSpanningTreeHoldTime": dtrSpanningTreeHoldTime,
       "dtrSpanningTreeProtocolSpecification": dtrSpanningTreeProtocolSpecification,
       "dtrSpanningTreeTimeSinceTopoChange": dtrSpanningTreeTimeSinceTopoChange,
       "dtrSpanningTreeTopologyChanges": dtrSpanningTreeTopologyChanges,
       "dtrSpanningTreeBridgeForwardDelay": dtrSpanningTreeBridgeForwardDelay,
       "dtrSpanningTreeBridgeHelloTime": dtrSpanningTreeBridgeHelloTime,
       "dtrSpanningTreeTreeBridgeMaxAge": dtrSpanningTreeTreeBridgeMaxAge,
       "dtrCRFSpTreeTable": dtrCRFSpTreeTable,
       "dtrCRFSpTreeEntry": dtrCRFSpTreeEntry,
       "dtrCRFSpTreeCRFIndex": dtrCRFSpTreeCRFIndex,
       "dtrCRFSpTreePriority": dtrCRFSpTreePriority,
       "dtrCRFSpTreeDesignatedRoot": dtrCRFSpTreeDesignatedRoot,
       "dtrCRFSpTreeRootCost": dtrCRFSpTreeRootCost,
       "dtrCRFSpTreeRootPort": dtrCRFSpTreeRootPort,
       "dtrCRFSpTreeMaxAge": dtrCRFSpTreeMaxAge,
       "dtrCRFSpTreeHelloTime": dtrCRFSpTreeHelloTime,
       "dtrCRFSpTreeForwardDelay": dtrCRFSpTreeForwardDelay,
       "dtrCRFPortSpTreeTable": dtrCRFPortSpTreeTable,
       "dtrCRFPortSpTreeEntry": dtrCRFPortSpTreeEntry,
       "dtrCRFPortSpTreeCRFIndex": dtrCRFPortSpTreeCRFIndex,
       "dtrCRFPortSpTreeNumber": dtrCRFPortSpTreeNumber,
       "dtrCRFPortSpTreePriority": dtrCRFPortSpTreePriority,
       "dtrCRFPortSpTreeState": dtrCRFPortSpTreeState,
       "dtrCRFPortSpTreePathCost": dtrCRFPortSpTreePathCost,
       "dtrCRFPortSpTreeDesignatedRoot": dtrCRFPortSpTreeDesignatedRoot,
       "dtrCRFPortSpTreeDesignatedCost": dtrCRFPortSpTreeDesignatedCost,
       "dtrCRFPortSpTreeDesignatedBridge": dtrCRFPortSpTreeDesignatedBridge,
       "dtrCRFPortSpTreeDesignatedPort": dtrCRFPortSpTreeDesignatedPort,
       "dtrCRFPortSpTreeForwardTransitions": dtrCRFPortSpTreeForwardTransitions,
       "dtrConcMIBForwarding": dtrConcMIBForwarding,
       "dtrFdbDynamicAddrTable": dtrFdbDynamicAddrTable,
       "dtrFdbDynamicAddrEntry": dtrFdbDynamicAddrEntry,
       "dtrFdbDynamicAddrCRFIndex": dtrFdbDynamicAddrCRFIndex,
       "dtrFdbDynamicAddrStnAddress": dtrFdbDynamicAddrStnAddress,
       "dtrFdbDynamicAddrPortNumber": dtrFdbDynamicAddrPortNumber,
       "dtrFdbDynamicAddrStatus": dtrFdbDynamicAddrStatus,
       "dtrFdbStaticAddrTable": dtrFdbStaticAddrTable,
       "dtrFdbStaticAddrEntry": dtrFdbStaticAddrEntry,
       "dtrFdbStaticAddrCRFIndex": dtrFdbStaticAddrCRFIndex,
       "dtrFdbStaticAddrStnAddress": dtrFdbStaticAddrStnAddress,
       "dtrFdbStaticAddrRowStatus": dtrFdbStaticAddrRowStatus,
       "dtrFdbStaticAddrInMask": dtrFdbStaticAddrInMask,
       "dtrFdbStaticAddrOutMask": dtrFdbStaticAddrOutMask,
       "dtrFdbStaticAddrStatus": dtrFdbStaticAddrStatus,
       "dtrFdbDynamicRDTable": dtrFdbDynamicRDTable,
       "dtrFdbDynamicRDEntry": dtrFdbDynamicRDEntry,
       "dtrFdbDynamicRDCRFIndex": dtrFdbDynamicRDCRFIndex,
       "dtrFdbDynamicRDRouteDesc": dtrFdbDynamicRDRouteDesc,
       "dtrFdbDynamicRDPortNumber": dtrFdbDynamicRDPortNumber,
       "dtrFdbDynamicRDStatus": dtrFdbDynamicRDStatus,
       "dtrFdbStaticRDTable": dtrFdbStaticRDTable,
       "dtrFdbStaticRDEntry": dtrFdbStaticRDEntry,
       "dtrFdbStaticRDCRFIndex": dtrFdbStaticRDCRFIndex,
       "dtrFdbStaticRDRouteDesc": dtrFdbStaticRDRouteDesc,
       "dtrFdbStaticRDRowStatus": dtrFdbStaticRDRowStatus,
       "dtrFdbStaticRDPortNumber": dtrFdbStaticRDPortNumber,
       "dtrFdbStaticRDStatus": dtrFdbStaticRDStatus,
       "dtrConcMIBMRI": dtrConcMIBMRI,
       "dtrMRITable": dtrMRITable,
       "dtrMRIEntry": dtrMRIEntry,
       "dtrMRICRFIndex": dtrMRICRFIndex,
       "dtrMRIMgmtType": dtrMRIMgmtType,
       "dtrMRIOutMask": dtrMRIOutMask,
       "dtrConcMIBStats": dtrConcMIBStats,
       "dtrCRFPortStatsTable": dtrCRFPortStatsTable,
       "dtrCRFPortStatsEntry": dtrCRFPortStatsEntry,
       "dtrCRFPortStatsCRFIndex": dtrCRFPortStatsCRFIndex,
       "dtrCRFPortStatsPortNumber": dtrCRFPortStatsPortNumber,
       "dtrCRFPortStatsAreInFrames": dtrCRFPortStatsAreInFrames,
       "dtrCRFPortStatsAreOutFrames": dtrCRFPortStatsAreOutFrames,
       "dtrCRFPortStatsInFrames": dtrCRFPortStatsInFrames,
       "dtrCRFPortStatsOutFrames": dtrCRFPortStatsOutFrames,
       "dtrCRFPortStatsSrfInFrames": dtrCRFPortStatsSrfInFrames,
       "dtrCRFPortStatsSrfOutFrames": dtrCRFPortStatsSrfOutFrames,
       "dtrCRFPortStatsSteInFrames": dtrCRFPortStatsSteInFrames,
       "dtrCRFPortStatsSteOutFrames": dtrCRFPortStatsSteOutFrames,
       "dtrCRFPortStatsInvalidRI": dtrCRFPortStatsInvalidRI,
       "dtrCRFPortStatsInMisdirected": dtrCRFPortStatsInMisdirected,
       "dtrCRFPortStatsInDiscards": dtrCRFPortStatsInDiscards,
       "dtrMacMIB": dtrMacMIB,
       "dtrExt": dtrExt,
       "dtrExSrbGlobal": dtrExSrbGlobal,
       "dtrExSrbBridgeNumber": dtrExSrbBridgeNumber,
       "dtrExSrbBridgeNumberOfCrfs": dtrExSrbBridgeNumberOfCrfs,
       "dtrExSrbStp": dtrExSrbStp,
       "dtrExSrbStpGlobal": dtrExSrbStpGlobal,
       "dtrExSrbStpPriority": dtrExSrbStpPriority,
       "dtrExSrbStpAddress": dtrExSrbStpAddress,
       "dtrExSrbStpBridgeMaxAge": dtrExSrbStpBridgeMaxAge,
       "dtrExSrbStpBridgeHelloTime": dtrExSrbStpBridgeHelloTime,
       "dtrExSrbStpBridgeForwardDelay": dtrExSrbStpBridgeForwardDelay,
       "dtrExSrbStpDesignatedRoot": dtrExSrbStpDesignatedRoot,
       "dtrExSrbStpRootCost": dtrExSrbStpRootCost,
       "dtrExSrbStpRootPort": dtrExSrbStpRootPort,
       "dtrExSrbStpMaxAge": dtrExSrbStpMaxAge,
       "dtrExSrbStpHelloTime": dtrExSrbStpHelloTime,
       "dtrExSrbStpHoldTime": dtrExSrbStpHoldTime,
       "dtrExSrbStpForwardDelay": dtrExSrbStpForwardDelay,
       "dtrExSrbStpMode": dtrExSrbStpMode,
       "dtrExSrbPortStpTable": dtrExSrbPortStpTable,
       "dtrExSrbPortStpEntry": dtrExSrbPortStpEntry,
       "dtrExSrbPortStpCRFIndex": dtrExSrbPortStpCRFIndex,
       "dtrExSrbPortStpPort": dtrExSrbPortStpPort,
       "dtrExSrbPortStpPriority": dtrExSrbPortStpPriority,
       "dtrExSrbPortStpState": dtrExSrbPortStpState,
       "dtrExSrbPortStpPathCost": dtrExSrbPortStpPathCost,
       "dtrExSrbPortStpDesignatedRoot": dtrExSrbPortStpDesignatedRoot,
       "dtrExSrbPortStpDesignatedCost": dtrExSrbPortStpDesignatedCost,
       "dtrExSrbPortStpDesignatedBridge": dtrExSrbPortStpDesignatedBridge,
       "dtrExSrbPortStpDesignatedPort": dtrExSrbPortStpDesignatedPort,
       "dtrExSrbPortStpForwardTrans": dtrExSrbPortStpForwardTrans,
       "dtrExSrbPortHopTable": dtrExSrbPortHopTable,
       "dtrExSrbPortHopEntry": dtrExSrbPortHopEntry,
       "dtrExSrbPortHopCRFIndex": dtrExSrbPortHopCRFIndex,
       "dtrExSrbPortHopPort": dtrExSrbPortHopPort,
       "dtrExSrbPortHopAreRcvMax": dtrExSrbPortHopAreRcvMax,
       "dtrExSrbPortHopAreXmtMax": dtrExSrbPortHopAreXmtMax,
       "dtrExSrbPortHopSteRcvMax": dtrExSrbPortHopSteRcvMax,
       "dtrExSrbPortHopSteXmtMax": dtrExSrbPortHopSteXmtMax}
)
