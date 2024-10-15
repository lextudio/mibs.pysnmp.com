# SNMP MIB module (AIIPVCTABLE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AIIPVCTABLE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:11 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

aiPVC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 16, 1)
)


# Types definitions



class UnsignedShort(Integer32):
    """Custom type UnsignedShort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class IfIndexType(Integer32):
    """Custom type IfIndexType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )




# TEXTUAL-CONVENTIONS



class IANAifType(Integer32, TextualConvention):
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



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)
_AiSLC2_ObjectIdentity = ObjectIdentity
aiSLC2 = _AiSLC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 16)
)
_AiPVCTable_Object = MibTable
aiPVCTable = _AiPVCTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 1, 1)
)
if mibBuilder.loadTexts:
    aiPVCTable.setStatus("current")
_AiPVCEntry_Object = MibTableRow
aiPVCEntry = _AiPVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 1, 1, 1)
)
aiPVCEntry.setIndexNames(
    (0, "AIIPVCTABLE-MIB", "aiPVCIfType"),
    (0, "AIIPVCTABLE-MIB", "aiPVCIfIndex"),
    (0, "AIIPVCTABLE-MIB", "aiPVCCircuit"),
)
if mibBuilder.loadTexts:
    aiPVCEntry.setStatus("current")
_AiPVCStatus_Type = RowStatus
_AiPVCStatus_Object = MibTableColumn
aiPVCStatus = _AiPVCStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 1, 1, 1, 1),
    _AiPVCStatus_Type()
)
aiPVCStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aiPVCStatus.setStatus("current")
_AiPVCIfType_Type = IANAifType
_AiPVCIfType_Object = MibTableColumn
aiPVCIfType = _AiPVCIfType_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 1, 1, 1, 2),
    _AiPVCIfType_Type()
)
aiPVCIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiPVCIfType.setStatus("current")
_AiPVCIfIndex_Type = IfIndexType
_AiPVCIfIndex_Object = MibTableColumn
aiPVCIfIndex = _AiPVCIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 1, 1, 1, 3),
    _AiPVCIfIndex_Type()
)
aiPVCIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiPVCIfIndex.setStatus("current")
_AiPVCCircuit_Type = PositiveInteger
_AiPVCCircuit_Object = MibTableColumn
aiPVCCircuit = _AiPVCCircuit_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 1, 1, 1, 4),
    _AiPVCCircuit_Type()
)
aiPVCCircuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiPVCCircuit.setStatus("current")
_AiPVCCallTimer_Type = UnsignedShort
_AiPVCCallTimer_Object = MibTableColumn
aiPVCCallTimer = _AiPVCCallTimer_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 1, 1, 1, 5),
    _AiPVCCallTimer_Type()
)
aiPVCCallTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiPVCCallTimer.setStatus("current")
_AiPVCInactivityTimer_Type = UnsignedShort
_AiPVCInactivityTimer_Object = MibTableColumn
aiPVCInactivityTimer = _AiPVCInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 539, 16, 1, 1, 1, 6),
    _AiPVCInactivityTimer_Type()
)
aiPVCInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiPVCInactivityTimer.setStatus("current")
_AiPVCConformance_ObjectIdentity = ObjectIdentity
aiPVCConformance = _AiPVCConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 16, 1, 2)
)
_AiPVCGroups_ObjectIdentity = ObjectIdentity
aiPVCGroups = _AiPVCGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 16, 1, 2, 1)
)
_AiPVCCompliances_ObjectIdentity = ObjectIdentity
aiPVCCompliances = _AiPVCCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 16, 1, 2, 2)
)

# Managed Objects groups

aiPVCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 539, 16, 1, 2, 1, 1)
)
aiPVCGroup.setObjects(
      *(("AIIPVCTABLE-MIB", "aiPVCStatus"),
        ("AIIPVCTABLE-MIB", "aiPVCIfIndex"),
        ("AIIPVCTABLE-MIB", "aiPVCIfType"),
        ("AIIPVCTABLE-MIB", "aiPVCCircuit"),
        ("AIIPVCTABLE-MIB", "aiPVCCallTimer"),
        ("AIIPVCTABLE-MIB", "aiPVCInactivityTimer"))
)
if mibBuilder.loadTexts:
    aiPVCGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aiPVCCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 539, 16, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    aiPVCCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AIIPVCTABLE-MIB",
    **{"UnsignedShort": UnsignedShort,
       "PositiveInteger": PositiveInteger,
       "IfIndexType": IfIndexType,
       "IANAifType": IANAifType,
       "aii": aii,
       "aiSLC2": aiSLC2,
       "aiPVC": aiPVC,
       "aiPVCTable": aiPVCTable,
       "aiPVCEntry": aiPVCEntry,
       "aiPVCStatus": aiPVCStatus,
       "aiPVCIfType": aiPVCIfType,
       "aiPVCIfIndex": aiPVCIfIndex,
       "aiPVCCircuit": aiPVCCircuit,
       "aiPVCCallTimer": aiPVCCallTimer,
       "aiPVCInactivityTimer": aiPVCInactivityTimer,
       "aiPVCConformance": aiPVCConformance,
       "aiPVCGroups": aiPVCGroups,
       "aiPVCGroup": aiPVCGroup,
       "aiPVCCompliances": aiPVCCompliances,
       "aiPVCCompliance": aiPVCCompliance}
)
