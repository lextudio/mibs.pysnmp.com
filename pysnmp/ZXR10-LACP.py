# SNMP MIB module (ZXR10-LACP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXR10-LACP
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:55 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")

(zxr10,) = mibBuilder.importSymbols(
    "ZXR10-SMI",
    "zxr10")


# MODULE-IDENTITY

lacpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125)
)


# Types definitions



class UINT32(Unsigned32):
    """Custom type UINT32 based on Unsigned32"""




class Char(OctetString):
    """Custom type Char based on OctetString"""



# TEXTUAL-CONVENTIONS



class LACPMode(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bondMode8023AD", 1),
          ("bondModeOn", 0))
    )



class LACPLoadBalanceType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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
              50,
              51)
        )
    )
    namedValues = NamedValues(
        *(("dst-ip", 1),
          ("dst-ip-dst-port", 10),
          ("dst-mac", 2),
          ("dst-port", 8),
          ("per-packet", 16),
          ("perDestination", 50),
          ("perPacket", 51),
          ("pri-label", 14),
          ("pub-label", 13),
          ("pub-pri-label", 15),
          ("src-dst-ip", 3),
          ("src-dst-ip-src-dst-port", 12),
          ("src-dst-mac", 4),
          ("src-dst-port", 9),
          ("src-ip", 5),
          ("src-ip-src-port", 11),
          ("src-mac", 6),
          ("src-port", 7))
    )



class LACPPortType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("on", 2),
          ("passive", 1))
    )



class LACPPortTimeoutType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("long-time", 0),
          ("short-time", 1))
    )



# MIB Managed Objects in the order of their OIDs

_LacpMibObjects_ObjectIdentity = ObjectIdentity
lacpMibObjects = _LacpMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1)
)
_LacpAggregatingPara_ObjectIdentity = ObjectIdentity
lacpAggregatingPara = _LacpAggregatingPara_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1)
)
_LacpAggregatingTable_Object = MibTable
lacpAggregatingTable = _LacpAggregatingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lacpAggregatingTable.setStatus("current")
_LacpAggregatingEntry_Object = MibTableRow
lacpAggregatingEntry = _LacpAggregatingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1)
)
lacpAggregatingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lacpAggregatingEntry.setStatus("current")
_LacpAggSgIfName_Type = Char
_LacpAggSgIfName_Object = MibTableColumn
lacpAggSgIfName = _LacpAggSgIfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 1),
    _LacpAggSgIfName_Type()
)
lacpAggSgIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpAggSgIfName.setStatus("current")
_LacpAggMacAddress_Type = MacAddress
_LacpAggMacAddress_Object = MibTableColumn
lacpAggMacAddress = _LacpAggMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 2),
    _LacpAggMacAddress_Type()
)
lacpAggMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpAggMacAddress.setStatus("current")


class _LacpAggActorSystemPriority_Type(UINT32):
    """Custom type lacpAggActorSystemPriority based on UINT32"""
    subtypeSpec = UINT32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LacpAggActorSystemPriority_Type.__name__ = "UINT32"
_LacpAggActorSystemPriority_Object = MibTableColumn
lacpAggActorSystemPriority = _LacpAggActorSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 3),
    _LacpAggActorSystemPriority_Type()
)
lacpAggActorSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpAggActorSystemPriority.setStatus("current")
_LacpAggMode_Type = LACPMode
_LacpAggMode_Object = MibTableColumn
lacpAggMode = _LacpAggMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 4),
    _LacpAggMode_Type()
)
lacpAggMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpAggMode.setStatus("current")
_LacpAggLoadBalanceMode_Type = LACPLoadBalanceType
_LacpAggLoadBalanceMode_Object = MibTableColumn
lacpAggLoadBalanceMode = _LacpAggLoadBalanceMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 5),
    _LacpAggLoadBalanceMode_Type()
)
lacpAggLoadBalanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpAggLoadBalanceMode.setStatus("current")
_LacpAggJumboframe_Type = TruthValue
_LacpAggJumboframe_Object = MibTableColumn
lacpAggJumboframe = _LacpAggJumboframe_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 6),
    _LacpAggJumboframe_Type()
)
lacpAggJumboframe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpAggJumboframe.setStatus("current")
_LacpAggSubIfIndexName1_Type = Char
_LacpAggSubIfIndexName1_Object = MibTableColumn
lacpAggSubIfIndexName1 = _LacpAggSubIfIndexName1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 7),
    _LacpAggSubIfIndexName1_Type()
)
lacpAggSubIfIndexName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpAggSubIfIndexName1.setStatus("current")
_LacpAggSubIfIndexName2_Type = Char
_LacpAggSubIfIndexName2_Object = MibTableColumn
lacpAggSubIfIndexName2 = _LacpAggSubIfIndexName2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 8),
    _LacpAggSubIfIndexName2_Type()
)
lacpAggSubIfIndexName2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpAggSubIfIndexName2.setStatus("current")
_LacpAggSubIfIndexName3_Type = Char
_LacpAggSubIfIndexName3_Object = MibTableColumn
lacpAggSubIfIndexName3 = _LacpAggSubIfIndexName3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 9),
    _LacpAggSubIfIndexName3_Type()
)
lacpAggSubIfIndexName3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpAggSubIfIndexName3.setStatus("current")
_LacpAggSubIfIndexName4_Type = Char
_LacpAggSubIfIndexName4_Object = MibTableColumn
lacpAggSubIfIndexName4 = _LacpAggSubIfIndexName4_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 10),
    _LacpAggSubIfIndexName4_Type()
)
lacpAggSubIfIndexName4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpAggSubIfIndexName4.setStatus("current")
_LacpAggSubIfIndexName5_Type = Char
_LacpAggSubIfIndexName5_Object = MibTableColumn
lacpAggSubIfIndexName5 = _LacpAggSubIfIndexName5_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 11),
    _LacpAggSubIfIndexName5_Type()
)
lacpAggSubIfIndexName5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpAggSubIfIndexName5.setStatus("current")
_LacpAggSubIfIndexName6_Type = Char
_LacpAggSubIfIndexName6_Object = MibTableColumn
lacpAggSubIfIndexName6 = _LacpAggSubIfIndexName6_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 12),
    _LacpAggSubIfIndexName6_Type()
)
lacpAggSubIfIndexName6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpAggSubIfIndexName6.setStatus("current")
_LacpAggSubIfIndexName7_Type = Char
_LacpAggSubIfIndexName7_Object = MibTableColumn
lacpAggSubIfIndexName7 = _LacpAggSubIfIndexName7_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 13),
    _LacpAggSubIfIndexName7_Type()
)
lacpAggSubIfIndexName7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpAggSubIfIndexName7.setStatus("current")
_LacpAggSubIfIndexName8_Type = Char
_LacpAggSubIfIndexName8_Object = MibTableColumn
lacpAggSubIfIndexName8 = _LacpAggSubIfIndexName8_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 1, 1, 1, 14),
    _LacpAggSubIfIndexName8_Type()
)
lacpAggSubIfIndexName8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpAggSubIfIndexName8.setStatus("current")
_LacpAggregatedPara_ObjectIdentity = ObjectIdentity
lacpAggregatedPara = _LacpAggregatedPara_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2)
)
_LacpAggregatedTable_Object = MibTable
lacpAggregatedTable = _LacpAggregatedTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lacpAggregatedTable.setStatus("current")
_LacpAggregatedEntry_Object = MibTableRow
lacpAggregatedEntry = _LacpAggregatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1)
)
lacpAggregatedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lacpAggregatedEntry.setStatus("current")


class _LacpAggSgId_Type(UINT32):
    """Custom type lacpAggSgId based on UINT32"""
    subtypeSpec = UINT32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_LacpAggSgId_Type.__name__ = "UINT32"
_LacpAggSgId_Object = MibTableColumn
lacpAggSgId = _LacpAggSgId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1, 1),
    _LacpAggSgId_Type()
)
lacpAggSgId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpAggSgId.setStatus("current")
_LacpAggregatedIfName_Type = Char
_LacpAggregatedIfName_Object = MibTableColumn
lacpAggregatedIfName = _LacpAggregatedIfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1, 2),
    _LacpAggregatedIfName_Type()
)
lacpAggregatedIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpAggregatedIfName.setStatus("current")
_LacpAggPortMode_Type = LACPPortType
_LacpAggPortMode_Object = MibTableColumn
lacpAggPortMode = _LacpAggPortMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1, 3),
    _LacpAggPortMode_Type()
)
lacpAggPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpAggPortMode.setStatus("current")
_LacpAggPortTimeOut_Type = LACPPortTimeoutType
_LacpAggPortTimeOut_Object = MibTableColumn
lacpAggPortTimeOut = _LacpAggPortTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1, 4),
    _LacpAggPortTimeOut_Type()
)
lacpAggPortTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpAggPortTimeOut.setStatus("current")


class _LacpAggLacpPriority_Type(UINT32):
    """Custom type lacpAggLacpPriority based on UINT32"""
    subtypeSpec = UINT32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LacpAggLacpPriority_Type.__name__ = "UINT32"
_LacpAggLacpPriority_Object = MibTableColumn
lacpAggLacpPriority = _LacpAggLacpPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1, 5),
    _LacpAggLacpPriority_Type()
)
lacpAggLacpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpAggLacpPriority.setStatus("current")
_LacpAggPortActorOperKey_Type = UINT32
_LacpAggPortActorOperKey_Object = MibTableColumn
lacpAggPortActorOperKey = _LacpAggPortActorOperKey_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1, 6),
    _LacpAggPortActorOperKey_Type()
)
lacpAggPortActorOperKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpAggPortActorOperKey.setStatus("current")
_LacpAggPortActorOperState_Type = UINT32
_LacpAggPortActorOperState_Object = MibTableColumn
lacpAggPortActorOperState = _LacpAggPortActorOperState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1, 7),
    _LacpAggPortActorOperState_Type()
)
lacpAggPortActorOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpAggPortActorOperState.setStatus("current")
_LacpAggPortPartnerOperKey_Type = UINT32
_LacpAggPortPartnerOperKey_Object = MibTableColumn
lacpAggPortPartnerOperKey = _LacpAggPortPartnerOperKey_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1, 8),
    _LacpAggPortPartnerOperKey_Type()
)
lacpAggPortPartnerOperKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpAggPortPartnerOperKey.setStatus("current")
_LacpAggPortPartnerOperState_Type = UINT32
_LacpAggPortPartnerOperState_Object = MibTableColumn
lacpAggPortPartnerOperState = _LacpAggPortPartnerOperState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 125, 1, 2, 1, 1, 9),
    _LacpAggPortPartnerOperState_Type()
)
lacpAggPortPartnerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpAggPortPartnerOperState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXR10-LACP",
    **{"UINT32": UINT32,
       "Char": Char,
       "LACPMode": LACPMode,
       "LACPLoadBalanceType": LACPLoadBalanceType,
       "LACPPortType": LACPPortType,
       "LACPPortTimeoutType": LACPPortTimeoutType,
       "lacpMIB": lacpMIB,
       "lacpMibObjects": lacpMibObjects,
       "lacpAggregatingPara": lacpAggregatingPara,
       "lacpAggregatingTable": lacpAggregatingTable,
       "lacpAggregatingEntry": lacpAggregatingEntry,
       "lacpAggSgIfName": lacpAggSgIfName,
       "lacpAggMacAddress": lacpAggMacAddress,
       "lacpAggActorSystemPriority": lacpAggActorSystemPriority,
       "lacpAggMode": lacpAggMode,
       "lacpAggLoadBalanceMode": lacpAggLoadBalanceMode,
       "lacpAggJumboframe": lacpAggJumboframe,
       "lacpAggSubIfIndexName1": lacpAggSubIfIndexName1,
       "lacpAggSubIfIndexName2": lacpAggSubIfIndexName2,
       "lacpAggSubIfIndexName3": lacpAggSubIfIndexName3,
       "lacpAggSubIfIndexName4": lacpAggSubIfIndexName4,
       "lacpAggSubIfIndexName5": lacpAggSubIfIndexName5,
       "lacpAggSubIfIndexName6": lacpAggSubIfIndexName6,
       "lacpAggSubIfIndexName7": lacpAggSubIfIndexName7,
       "lacpAggSubIfIndexName8": lacpAggSubIfIndexName8,
       "lacpAggregatedPara": lacpAggregatedPara,
       "lacpAggregatedTable": lacpAggregatedTable,
       "lacpAggregatedEntry": lacpAggregatedEntry,
       "lacpAggSgId": lacpAggSgId,
       "lacpAggregatedIfName": lacpAggregatedIfName,
       "lacpAggPortMode": lacpAggPortMode,
       "lacpAggPortTimeOut": lacpAggPortTimeOut,
       "lacpAggLacpPriority": lacpAggLacpPriority,
       "lacpAggPortActorOperKey": lacpAggPortActorOperKey,
       "lacpAggPortActorOperState": lacpAggPortActorOperState,
       "lacpAggPortPartnerOperKey": lacpAggPortPartnerOperKey,
       "lacpAggPortPartnerOperState": lacpAggPortPartnerOperState}
)
