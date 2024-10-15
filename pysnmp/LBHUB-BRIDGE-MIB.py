# SNMP MIB module (LBHUB-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LBHUB-BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:25 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mgmt")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""




class BridgeId(OctetString):
    """Custom type BridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mib_2_ObjectIdentity = ObjectIdentity
mib_2 = _Mib_2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1)
)
_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1)
)
_TerminalServer_ObjectIdentity = ObjectIdentity
terminalServer = _TerminalServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1)
)
_DedicatedBridgeServer_ObjectIdentity = ObjectIdentity
dedicatedBridgeServer = _DedicatedBridgeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 2)
)
_DedicatedRouteServer_ObjectIdentity = ObjectIdentity
dedicatedRouteServer = _DedicatedRouteServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 3)
)
_Brouter_ObjectIdentity = ObjectIdentity
brouter = _Brouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4)
)
_GenericMSWorkstation_ObjectIdentity = ObjectIdentity
genericMSWorkstation = _GenericMSWorkstation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 5)
)
_GenericMSServer_ObjectIdentity = ObjectIdentity
genericMSServer = _GenericMSServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 6)
)
_GenericUnixServer_ObjectIdentity = ObjectIdentity
genericUnixServer = _GenericUnixServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 7)
)
_Hub_ObjectIdentity = ObjectIdentity
hub = _Hub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8)
)
_LinkBuilder3GH_ObjectIdentity = ObjectIdentity
linkBuilder3GH = _LinkBuilder3GH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 1)
)
_LinkBuilder10BTi_ObjectIdentity = ObjectIdentity
linkBuilder10BTi = _LinkBuilder10BTi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 2)
)
_LinkBuilderECS_ObjectIdentity = ObjectIdentity
linkBuilderECS = _LinkBuilderECS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 3)
)
_LinkBuilderMSH_ObjectIdentity = ObjectIdentity
linkBuilderMSH = _LinkBuilderMSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4)
)
_LinkBuilderFMS_ObjectIdentity = ObjectIdentity
linkBuilderFMS = _LinkBuilderFMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 5)
)
_LinkBuilderFMSII_ObjectIdentity = ObjectIdentity
linkBuilderFMSII = _LinkBuilderFMSII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 7)
)
_LinkBuilderFMSLBridge_ObjectIdentity = ObjectIdentity
linkBuilderFMSLBridge = _LinkBuilderFMSLBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 10)
)
_Cards_ObjectIdentity = ObjectIdentity
cards = _Cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9)
)
_LinkBuilder3GH_cards_ObjectIdentity = ObjectIdentity
linkBuilder3GH_cards = _LinkBuilder3GH_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 1)
)
_LinkBuilder10BTi_cards_ObjectIdentity = ObjectIdentity
linkBuilder10BTi_cards = _LinkBuilder10BTi_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 2)
)
_LinkBuilder10BTi_cards_utp_ObjectIdentity = ObjectIdentity
linkBuilder10BTi_cards_utp = _LinkBuilder10BTi_cards_utp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 2, 1)
)
_LinkBuilder10BT_cards_utp_ObjectIdentity = ObjectIdentity
linkBuilder10BT_cards_utp = _LinkBuilder10BT_cards_utp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 2, 2)
)
_LinkBuilderECS_cards_ObjectIdentity = ObjectIdentity
linkBuilderECS_cards = _LinkBuilderECS_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 3)
)
_LinkBuilderMSH_cards_ObjectIdentity = ObjectIdentity
linkBuilderMSH_cards = _LinkBuilderMSH_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 4)
)
_LinkBuilderFMS_cards_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards = _LinkBuilderFMS_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5)
)
_LinkBuilderFMS_cards_utp_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_utp = _LinkBuilderFMS_cards_utp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 1)
)
_LinkBuilderFMS_cards_coax_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_coax = _LinkBuilderFMS_cards_coax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 2)
)
_LinkBuilderFMS_cards_fiber_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_fiber = _LinkBuilderFMS_cards_fiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 3)
)
_LinkBuilderFMS_cards_12fiber_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_12fiber = _LinkBuilderFMS_cards_12fiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 4)
)
_LinkBuilderFMS_cards_24utp_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_24utp = _LinkBuilderFMS_cards_24utp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 5)
)
_LinkBuilderFMSII_cards_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards = _LinkBuilderFMSII_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6)
)
_LinkBuilderFMSII_cards_12tp_rj45_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_12tp_rj45 = _LinkBuilderFMSII_cards_12tp_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 1)
)
_LinkBuilderFMSII_cards_10coax_bnc_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_10coax_bnc = _LinkBuilderFMSII_cards_10coax_bnc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 2)
)
_LinkBuilderFMSII_cards_6fiber_st_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_6fiber_st = _LinkBuilderFMSII_cards_6fiber_st_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 3)
)
_LinkBuilderFMSII_cards_12fiber_st_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_12fiber_st = _LinkBuilderFMSII_cards_12fiber_st_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 4)
)
_LinkBuilderFMSII_cards_24tp_rj45_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_24tp_rj45 = _LinkBuilderFMSII_cards_24tp_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 5)
)
_LinkBuilderFMSII_cards_24tp_telco_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_24tp_telco = _LinkBuilderFMSII_cards_24tp_telco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 6)
)
_Amp_mib_ObjectIdentity = ObjectIdentity
amp_mib = _Amp_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 3)
)
_GenericTrap_ObjectIdentity = ObjectIdentity
genericTrap = _GenericTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 4)
)
_ViewBuilderApps_ObjectIdentity = ObjectIdentity
viewBuilderApps = _ViewBuilderApps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 5)
)
_SpecificTrap_ObjectIdentity = ObjectIdentity
specificTrap = _SpecificTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 6)
)
_LinkBuilder3GH_mib_ObjectIdentity = ObjectIdentity
linkBuilder3GH_mib = _LinkBuilder3GH_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7)
)
_LinkBuilder10BTi_mib_ObjectIdentity = ObjectIdentity
linkBuilder10BTi_mib = _LinkBuilder10BTi_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 8)
)
_LinkBuilderECS_mib_ObjectIdentity = ObjectIdentity
linkBuilderECS_mib = _LinkBuilderECS_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 9)
)
_Generic_ObjectIdentity = ObjectIdentity
generic = _Generic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10)
)
_GenExperimental_ObjectIdentity = ObjectIdentity
genExperimental = _GenExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 1)
)
_TestData_ObjectIdentity = ObjectIdentity
testData = _TestData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 1)
)
_IfExtensions_ObjectIdentity = ObjectIdentity
ifExtensions = _IfExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 2)
)
_Setup_ObjectIdentity = ObjectIdentity
setup = _Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 2)
)
_SysLoader_ObjectIdentity = ObjectIdentity
sysLoader = _SysLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 3)
)
_Security_ObjectIdentity = ObjectIdentity
security = _Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 4)
)
_Gauges_ObjectIdentity = ObjectIdentity
gauges = _Gauges_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 5)
)
_AsciiAgent_ObjectIdentity = ObjectIdentity
asciiAgent = _AsciiAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 6)
)
_SerialIf_ObjectIdentity = ObjectIdentity
serialIf = _SerialIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 7)
)
_RepeaterMgmt_ObjectIdentity = ObjectIdentity
repeaterMgmt = _RepeaterMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 8)
)
_EndStation_ObjectIdentity = ObjectIdentity
endStation = _EndStation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 9)
)
_LocalSnmp_ObjectIdentity = ObjectIdentity
localSnmp = _LocalSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 10)
)
_Manager_ObjectIdentity = ObjectIdentity
manager = _Manager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 11)
)
_UnusedGeneric12_ObjectIdentity = ObjectIdentity
unusedGeneric12 = _UnusedGeneric12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 12)
)
_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 14)
)
_MrmResilience_ObjectIdentity = ObjectIdentity
mrmResilience = _MrmResilience_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 15)
)
_TokenRing_ObjectIdentity = ObjectIdentity
tokenRing = _TokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 16)
)
_MultiRepeater_ObjectIdentity = ObjectIdentity
multiRepeater = _MultiRepeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 17)
)
_BridgeMgmt_ObjectIdentity = ObjectIdentity
bridgeMgmt = _BridgeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 18)
)
_BrControlPackage_ObjectIdentity = ObjectIdentity
brControlPackage = _BrControlPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 1)
)


class _BrClearCounters_Type(Integer32):
    """Custom type brClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("no-action", 1))
    )


_BrClearCounters_Type.__name__ = "Integer32"
_BrClearCounters_Object = MibScalar
brClearCounters = _BrClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 1, 1),
    _BrClearCounters_Type()
)
brClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brClearCounters.setStatus("mandatory")


class _BrSTAPMode_Type(Integer32):
    """Custom type brSTAPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_BrSTAPMode_Type.__name__ = "Integer32"
_BrSTAPMode_Object = MibScalar
brSTAPMode = _BrSTAPMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 1, 2),
    _BrSTAPMode_Type()
)
brSTAPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSTAPMode.setStatus("mandatory")


class _BrLearnMode_Type(Integer32):
    """Custom type brLearnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_BrLearnMode_Type.__name__ = "Integer32"
_BrLearnMode_Object = MibScalar
brLearnMode = _BrLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 1, 3),
    _BrLearnMode_Type()
)
brLearnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLearnMode.setStatus("mandatory")


class _BrAgingMode_Type(Integer32):
    """Custom type brAgingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_BrAgingMode_Type.__name__ = "Integer32"
_BrAgingMode_Object = MibScalar
brAgingMode = _BrAgingMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 1, 7),
    _BrAgingMode_Type()
)
brAgingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brAgingMode.setStatus("mandatory")
_BrMonitorPackage_ObjectIdentity = ObjectIdentity
brMonitorPackage = _BrMonitorPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 2)
)
_BrMonPortTable_Object = MibTable
brMonPortTable = _BrMonPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 2, 1)
)
if mibBuilder.loadTexts:
    brMonPortTable.setStatus("mandatory")
_BrMonPortEntry_Object = MibTableRow
brMonPortEntry = _BrMonPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 2, 1, 1)
)
brMonPortEntry.setIndexNames(
    (0, "LBHUB-BRIDGE-MIB", "brMonPort"),
)
if mibBuilder.loadTexts:
    brMonPortEntry.setStatus("mandatory")
_BrMonPort_Type = Integer32
_BrMonPort_Object = MibTableColumn
brMonPort = _BrMonPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 2, 1, 1, 1),
    _BrMonPort_Type()
)
brMonPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMonPort.setStatus("mandatory")
_BrMonPortIfIndex_Type = Integer32
_BrMonPortIfIndex_Object = MibTableColumn
brMonPortIfIndex = _BrMonPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 2, 1, 1, 2),
    _BrMonPortIfIndex_Type()
)
brMonPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMonPortIfIndex.setStatus("mandatory")
_BrMonPortPercentTrafficForwarded_Type = Integer32
_BrMonPortPercentTrafficForwarded_Object = MibTableColumn
brMonPortPercentTrafficForwarded = _BrMonPortPercentTrafficForwarded_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 2, 1, 1, 3),
    _BrMonPortPercentTrafficForwarded_Type()
)
brMonPortPercentTrafficForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMonPortPercentTrafficForwarded.setStatus("mandatory")
_BrMonPortBandwidthUsed_Type = Integer32
_BrMonPortBandwidthUsed_Object = MibTableColumn
brMonPortBandwidthUsed = _BrMonPortBandwidthUsed_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 2, 1, 1, 4),
    _BrMonPortBandwidthUsed_Type()
)
brMonPortBandwidthUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMonPortBandwidthUsed.setStatus("mandatory")
_BrMonPortErrorsPer10000Packets_Type = Integer32
_BrMonPortErrorsPer10000Packets_Object = MibTableColumn
brMonPortErrorsPer10000Packets = _BrMonPortErrorsPer10000Packets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 2, 1, 1, 5),
    _BrMonPortErrorsPer10000Packets_Type()
)
brMonPortErrorsPer10000Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMonPortErrorsPer10000Packets.setStatus("mandatory")
_BrMonPortBroadcastBandwidth_Type = Integer32
_BrMonPortBroadcastBandwidth_Object = MibTableColumn
brMonPortBroadcastBandwidth = _BrMonPortBroadcastBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 2, 1, 1, 6),
    _BrMonPortBroadcastBandwidth_Type()
)
brMonPortBroadcastBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMonPortBroadcastBandwidth.setStatus("mandatory")
_BrDialoguePackage_ObjectIdentity = ObjectIdentity
brDialoguePackage = _BrDialoguePackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 3)
)
_BrDataBase_ObjectIdentity = ObjectIdentity
brDataBase = _BrDataBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 4)
)
_BrSizeOfFilteringDataBase_Type = Integer32
_BrSizeOfFilteringDataBase_Object = MibScalar
brSizeOfFilteringDataBase = _BrSizeOfFilteringDataBase_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 4, 1),
    _BrSizeOfFilteringDataBase_Type()
)
brSizeOfFilteringDataBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brSizeOfFilteringDataBase.setStatus("mandatory")
_BrPercentageOfNonageingFDBEntries_Type = Integer32
_BrPercentageOfNonageingFDBEntries_Object = MibScalar
brPercentageOfNonageingFDBEntries = _BrPercentageOfNonageingFDBEntries_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 4, 2),
    _BrPercentageOfNonageingFDBEntries_Type()
)
brPercentageOfNonageingFDBEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPercentageOfNonageingFDBEntries.setStatus("mandatory")
_BrPercentageOfAgeingFDBEntries_Type = Integer32
_BrPercentageOfAgeingFDBEntries_Object = MibScalar
brPercentageOfAgeingFDBEntries = _BrPercentageOfAgeingFDBEntries_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 4, 3),
    _BrPercentageOfAgeingFDBEntries_Type()
)
brPercentageOfAgeingFDBEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPercentageOfAgeingFDBEntries.setStatus("mandatory")
_BrPercentageOfPermanentFDBEntries_Type = Integer32
_BrPercentageOfPermanentFDBEntries_Object = MibScalar
brPercentageOfPermanentFDBEntries = _BrPercentageOfPermanentFDBEntries_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 4, 4),
    _BrPercentageOfPermanentFDBEntries_Type()
)
brPercentageOfPermanentFDBEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPercentageOfPermanentFDBEntries.setStatus("mandatory")


class _BrClearFilteringDataBase_Type(Integer32):
    """Custom type brClearFilteringDataBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noAction", 1))
    )


_BrClearFilteringDataBase_Type.__name__ = "Integer32"
_BrClearFilteringDataBase_Object = MibScalar
brClearFilteringDataBase = _BrClearFilteringDataBase_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 4, 5),
    _BrClearFilteringDataBase_Type()
)
brClearFilteringDataBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brClearFilteringDataBase.setStatus("mandatory")
_BrMaxNumberOfPermanentEntries_Type = Integer32
_BrMaxNumberOfPermanentEntries_Object = MibScalar
brMaxNumberOfPermanentEntries = _BrMaxNumberOfPermanentEntries_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 4, 6),
    _BrMaxNumberOfPermanentEntries_Type()
)
brMaxNumberOfPermanentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMaxNumberOfPermanentEntries.setStatus("mandatory")
_BrPercentageOfPermanentDatabaseUsed_Type = Integer32
_BrPercentageOfPermanentDatabaseUsed_Object = MibScalar
brPercentageOfPermanentDatabaseUsed = _BrPercentageOfPermanentDatabaseUsed_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 4, 7),
    _BrPercentageOfPermanentDatabaseUsed_Type()
)
brPercentageOfPermanentDatabaseUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPercentageOfPermanentDatabaseUsed.setStatus("mandatory")


class _BrClearPermanentEntries_Type(Integer32):
    """Custom type brClearPermanentEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noAction", 1))
    )


_BrClearPermanentEntries_Type.__name__ = "Integer32"
_BrClearPermanentEntries_Object = MibScalar
brClearPermanentEntries = _BrClearPermanentEntries_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 4, 8),
    _BrClearPermanentEntries_Type()
)
brClearPermanentEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brClearPermanentEntries.setStatus("mandatory")


class _BrSaveLearntAddresses_Type(Integer32):
    """Custom type brSaveLearntAddresses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("save", 2))
    )


_BrSaveLearntAddresses_Type.__name__ = "Integer32"
_BrSaveLearntAddresses_Object = MibScalar
brSaveLearntAddresses = _BrSaveLearntAddresses_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 4, 9),
    _BrSaveLearntAddresses_Type()
)
brSaveLearntAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brSaveLearntAddresses.setStatus("mandatory")


class _BrDatabaseModified_Type(Integer32):
    """Custom type brDatabaseModified based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modified", 2),
          ("noChange", 1))
    )


_BrDatabaseModified_Type.__name__ = "Integer32"
_BrDatabaseModified_Object = MibScalar
brDatabaseModified = _BrDatabaseModified_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 4, 11),
    _BrDatabaseModified_Type()
)
brDatabaseModified.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brDatabaseModified.setStatus("mandatory")
_BrDummyPackage_ObjectIdentity = ObjectIdentity
brDummyPackage = _BrDummyPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 5)
)


class _BrDatabaseType_Type(Integer32):
    """Custom type brDatabaseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filtering", 1),
          ("permanent", 2))
    )


_BrDatabaseType_Type.__name__ = "Integer32"
_BrDatabaseType_Object = MibScalar
brDatabaseType = _BrDatabaseType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 5, 1),
    _BrDatabaseType_Type()
)
brDatabaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brDatabaseType.setStatus("mandatory")


class _BrDatabaseLevel_Type(Integer32):
    """Custom type brDatabaseLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(90,
              100)
        )
    )
    namedValues = NamedValues(
        *(("ninetyPercent", 90),
          ("oneHundredPercent", 100))
    )


_BrDatabaseLevel_Type.__name__ = "Integer32"
_BrDatabaseLevel_Object = MibScalar
brDatabaseLevel = _BrDatabaseLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 5, 2),
    _BrDatabaseLevel_Type()
)
brDatabaseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brDatabaseLevel.setStatus("mandatory")
_BrTrafficForwarded_Type = Counter32
_BrTrafficForwarded_Object = MibScalar
brTrafficForwarded = _BrTrafficForwarded_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 5, 3),
    _BrTrafficForwarded_Type()
)
brTrafficForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brTrafficForwarded.setStatus("mandatory")
_BrPortBandwidth_Type = Counter32
_BrPortBandwidth_Object = MibScalar
brPortBandwidth = _BrPortBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 5, 4),
    _BrPortBandwidth_Type()
)
brPortBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPortBandwidth.setStatus("mandatory")
_BrPortBroadcastBandwidth_Type = Counter32
_BrPortBroadcastBandwidth_Object = MibScalar
brPortBroadcastBandwidth = _BrPortBroadcastBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 5, 5),
    _BrPortBroadcastBandwidth_Type()
)
brPortBroadcastBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPortBroadcastBandwidth.setStatus("mandatory")
_BrPortErrors_Type = Counter32
_BrPortErrors_Object = MibScalar
brPortErrors = _BrPortErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 18, 5, 6),
    _BrPortErrors_Type()
)
brPortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brPortErrors.setStatus("mandatory")
_Fault_ObjectIdentity = ObjectIdentity
fault = _Fault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 19)
)
_Poll_ObjectIdentity = ObjectIdentity
poll = _Poll_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 20)
)
_PowerSupply_ObjectIdentity = ObjectIdentity
powerSupply = _PowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 21)
)
_NetBuilder_mib_ObjectIdentity = ObjectIdentity
netBuilder_mib = _NetBuilder_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 11)
)
_LBridgeECS_mib_ObjectIdentity = ObjectIdentity
lBridgeECS_mib = _LBridgeECS_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 12)
)
_DeskMan_mib_ObjectIdentity = ObjectIdentity
deskMan_mib = _DeskMan_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 13)
)
_LinkBuilderMSH_mib_ObjectIdentity = ObjectIdentity
linkBuilderMSH_mib = _LinkBuilderMSH_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 14)
)

# Managed Objects groups


# Notification objects

brDatabaseFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 65)
)
brDatabaseFull.setObjects(
      *(("LBHUB-BRIDGE-MIB", "brDatabaseType"),
        ("LBHUB-BRIDGE-MIB", "brDatabaseLevel"))
)
if mibBuilder.loadTexts:
    brDatabaseFull.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LBHUB-BRIDGE-MIB",
    **{"DisplayString": DisplayString,
       "PhysAddress": PhysAddress,
       "BridgeId": BridgeId,
       "MacAddress": MacAddress,
       "mib-2": mib_2,
       "a3Com": a3Com,
       "brDatabaseFull": brDatabaseFull,
       "products": products,
       "terminalServer": terminalServer,
       "dedicatedBridgeServer": dedicatedBridgeServer,
       "dedicatedRouteServer": dedicatedRouteServer,
       "brouter": brouter,
       "genericMSWorkstation": genericMSWorkstation,
       "genericMSServer": genericMSServer,
       "genericUnixServer": genericUnixServer,
       "hub": hub,
       "linkBuilder3GH": linkBuilder3GH,
       "linkBuilder10BTi": linkBuilder10BTi,
       "linkBuilderECS": linkBuilderECS,
       "linkBuilderMSH": linkBuilderMSH,
       "linkBuilderFMS": linkBuilderFMS,
       "linkBuilderFMSII": linkBuilderFMSII,
       "linkBuilderFMSLBridge": linkBuilderFMSLBridge,
       "cards": cards,
       "linkBuilder3GH-cards": linkBuilder3GH_cards,
       "linkBuilder10BTi-cards": linkBuilder10BTi_cards,
       "linkBuilder10BTi-cards-utp": linkBuilder10BTi_cards_utp,
       "linkBuilder10BT-cards-utp": linkBuilder10BT_cards_utp,
       "linkBuilderECS-cards": linkBuilderECS_cards,
       "linkBuilderMSH-cards": linkBuilderMSH_cards,
       "linkBuilderFMS-cards": linkBuilderFMS_cards,
       "linkBuilderFMS-cards-utp": linkBuilderFMS_cards_utp,
       "linkBuilderFMS-cards-coax": linkBuilderFMS_cards_coax,
       "linkBuilderFMS-cards-fiber": linkBuilderFMS_cards_fiber,
       "linkBuilderFMS-cards-12fiber": linkBuilderFMS_cards_12fiber,
       "linkBuilderFMS-cards-24utp": linkBuilderFMS_cards_24utp,
       "linkBuilderFMSII-cards": linkBuilderFMSII_cards,
       "linkBuilderFMSII-cards-12tp-rj45": linkBuilderFMSII_cards_12tp_rj45,
       "linkBuilderFMSII-cards-10coax-bnc": linkBuilderFMSII_cards_10coax_bnc,
       "linkBuilderFMSII-cards-6fiber-st": linkBuilderFMSII_cards_6fiber_st,
       "linkBuilderFMSII-cards-12fiber-st": linkBuilderFMSII_cards_12fiber_st,
       "linkBuilderFMSII-cards-24tp-rj45": linkBuilderFMSII_cards_24tp_rj45,
       "linkBuilderFMSII-cards-24tp-telco": linkBuilderFMSII_cards_24tp_telco,
       "amp-mib": amp_mib,
       "genericTrap": genericTrap,
       "viewBuilderApps": viewBuilderApps,
       "specificTrap": specificTrap,
       "linkBuilder3GH-mib": linkBuilder3GH_mib,
       "linkBuilder10BTi-mib": linkBuilder10BTi_mib,
       "linkBuilderECS-mib": linkBuilderECS_mib,
       "generic": generic,
       "genExperimental": genExperimental,
       "testData": testData,
       "ifExtensions": ifExtensions,
       "setup": setup,
       "sysLoader": sysLoader,
       "security": security,
       "gauges": gauges,
       "asciiAgent": asciiAgent,
       "serialIf": serialIf,
       "repeaterMgmt": repeaterMgmt,
       "endStation": endStation,
       "localSnmp": localSnmp,
       "manager": manager,
       "unusedGeneric12": unusedGeneric12,
       "chassis": chassis,
       "mrmResilience": mrmResilience,
       "tokenRing": tokenRing,
       "multiRepeater": multiRepeater,
       "bridgeMgmt": bridgeMgmt,
       "brControlPackage": brControlPackage,
       "brClearCounters": brClearCounters,
       "brSTAPMode": brSTAPMode,
       "brLearnMode": brLearnMode,
       "brAgingMode": brAgingMode,
       "brMonitorPackage": brMonitorPackage,
       "brMonPortTable": brMonPortTable,
       "brMonPortEntry": brMonPortEntry,
       "brMonPort": brMonPort,
       "brMonPortIfIndex": brMonPortIfIndex,
       "brMonPortPercentTrafficForwarded": brMonPortPercentTrafficForwarded,
       "brMonPortBandwidthUsed": brMonPortBandwidthUsed,
       "brMonPortErrorsPer10000Packets": brMonPortErrorsPer10000Packets,
       "brMonPortBroadcastBandwidth": brMonPortBroadcastBandwidth,
       "brDialoguePackage": brDialoguePackage,
       "brDataBase": brDataBase,
       "brSizeOfFilteringDataBase": brSizeOfFilteringDataBase,
       "brPercentageOfNonageingFDBEntries": brPercentageOfNonageingFDBEntries,
       "brPercentageOfAgeingFDBEntries": brPercentageOfAgeingFDBEntries,
       "brPercentageOfPermanentFDBEntries": brPercentageOfPermanentFDBEntries,
       "brClearFilteringDataBase": brClearFilteringDataBase,
       "brMaxNumberOfPermanentEntries": brMaxNumberOfPermanentEntries,
       "brPercentageOfPermanentDatabaseUsed": brPercentageOfPermanentDatabaseUsed,
       "brClearPermanentEntries": brClearPermanentEntries,
       "brSaveLearntAddresses": brSaveLearntAddresses,
       "brDatabaseModified": brDatabaseModified,
       "brDummyPackage": brDummyPackage,
       "brDatabaseType": brDatabaseType,
       "brDatabaseLevel": brDatabaseLevel,
       "brTrafficForwarded": brTrafficForwarded,
       "brPortBandwidth": brPortBandwidth,
       "brPortBroadcastBandwidth": brPortBroadcastBandwidth,
       "brPortErrors": brPortErrors,
       "fault": fault,
       "poll": poll,
       "powerSupply": powerSupply,
       "netBuilder-mib": netBuilder_mib,
       "lBridgeECS-mib": lBridgeECS_mib,
       "deskMan-mib": deskMan_mib,
       "linkBuilderMSH-mib": linkBuilderMSH_mib}
)
