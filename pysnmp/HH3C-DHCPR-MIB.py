# SNMP MIB module (HH3C-DHCPR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-DHCPR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:41 2024
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

(hh3cRhw,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cRhw")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hh3cDHCPRelayMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1)
)
hh3cDHCPRelayMib.setRevisions(
        ("2003-02-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cDHCPRelayMibObject_ObjectIdentity = ObjectIdentity
hh3cDHCPRelayMibObject = _Hh3cDHCPRelayMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 1)
)
_Hh3cDHCPRIPTable_Object = MibTable
hh3cDHCPRIPTable = _Hh3cDHCPRIPTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cDHCPRIPTable.setStatus("current")
_Hh3cDHCPRIPEntry_Object = MibTableRow
hh3cDHCPRIPEntry = _Hh3cDHCPRIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 1, 1)
)
hh3cDHCPRIPEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-DHCPR-MIB", "hh3cDHCPRIPAddr"),
)
if mibBuilder.loadTexts:
    hh3cDHCPRIPEntry.setStatus("current")
_Hh3cDHCPRIPAddr_Type = IpAddress
_Hh3cDHCPRIPAddr_Object = MibTableColumn
hh3cDHCPRIPAddr = _Hh3cDHCPRIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 1, 1, 1),
    _Hh3cDHCPRIPAddr_Type()
)
hh3cDHCPRIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPRIPAddr.setStatus("current")
_Hh3cDHCPRIPRowStatus_Type = RowStatus
_Hh3cDHCPRIPRowStatus_Object = MibTableColumn
hh3cDHCPRIPRowStatus = _Hh3cDHCPRIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 1, 1, 2),
    _Hh3cDHCPRIPRowStatus_Type()
)
hh3cDHCPRIPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPRIPRowStatus.setStatus("current")
_Hh3cDHCPRSeletAllocateModeTable_Object = MibTable
hh3cDHCPRSeletAllocateModeTable = _Hh3cDHCPRSeletAllocateModeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cDHCPRSeletAllocateModeTable.setStatus("current")
_Hh3cDHCPRSeletAllocateModeEntry_Object = MibTableRow
hh3cDHCPRSeletAllocateModeEntry = _Hh3cDHCPRSeletAllocateModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 2, 1)
)
hh3cDHCPRSeletAllocateModeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cDHCPRSeletAllocateModeEntry.setStatus("current")


class _Hh3cDHCPRSelectAllocateMode_Type(Integer32):
    """Custom type hh3cDHCPRSelectAllocateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("global", 0),
          ("interface", 1),
          ("relay", 2))
    )


_Hh3cDHCPRSelectAllocateMode_Type.__name__ = "Integer32"
_Hh3cDHCPRSelectAllocateMode_Object = MibTableColumn
hh3cDHCPRSelectAllocateMode = _Hh3cDHCPRSelectAllocateMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 2, 1, 1),
    _Hh3cDHCPRSelectAllocateMode_Type()
)
hh3cDHCPRSelectAllocateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPRSelectAllocateMode.setStatus("current")


class _Hh3cDHCPRelayCycleStatus_Type(Integer32):
    """Custom type hh3cDHCPRelayCycleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_Hh3cDHCPRelayCycleStatus_Type.__name__ = "Integer32"
_Hh3cDHCPRelayCycleStatus_Object = MibScalar
hh3cDHCPRelayCycleStatus = _Hh3cDHCPRelayCycleStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 3),
    _Hh3cDHCPRelayCycleStatus_Type()
)
hh3cDHCPRelayCycleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPRelayCycleStatus.setStatus("current")
_Hh3cDHCPRRxBadPktNum_Type = Integer32
_Hh3cDHCPRRxBadPktNum_Object = MibScalar
hh3cDHCPRRxBadPktNum = _Hh3cDHCPRRxBadPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 4),
    _Hh3cDHCPRRxBadPktNum_Type()
)
hh3cDHCPRRxBadPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPRRxBadPktNum.setStatus("current")
_Hh3cDHCPRRxServerPktNum_Type = Integer32
_Hh3cDHCPRRxServerPktNum_Object = MibScalar
hh3cDHCPRRxServerPktNum = _Hh3cDHCPRRxServerPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 5),
    _Hh3cDHCPRRxServerPktNum_Type()
)
hh3cDHCPRRxServerPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPRRxServerPktNum.setStatus("current")
_Hh3cDHCPRTxServerPktNum_Type = Integer32
_Hh3cDHCPRTxServerPktNum_Object = MibScalar
hh3cDHCPRTxServerPktNum = _Hh3cDHCPRTxServerPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 6),
    _Hh3cDHCPRTxServerPktNum_Type()
)
hh3cDHCPRTxServerPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPRTxServerPktNum.setStatus("current")
_Hh3cDHCPRRxClientPktNum_Type = Integer32
_Hh3cDHCPRRxClientPktNum_Object = MibScalar
hh3cDHCPRRxClientPktNum = _Hh3cDHCPRRxClientPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 7),
    _Hh3cDHCPRRxClientPktNum_Type()
)
hh3cDHCPRRxClientPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPRRxClientPktNum.setStatus("current")
_Hh3cDHCPRTxClientPktNum_Type = Integer32
_Hh3cDHCPRTxClientPktNum_Object = MibScalar
hh3cDHCPRTxClientPktNum = _Hh3cDHCPRTxClientPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 8),
    _Hh3cDHCPRTxClientPktNum_Type()
)
hh3cDHCPRTxClientPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPRTxClientPktNum.setStatus("current")
_Hh3cDHCPRTxClientUniPktNum_Type = Integer32
_Hh3cDHCPRTxClientUniPktNum_Object = MibScalar
hh3cDHCPRTxClientUniPktNum = _Hh3cDHCPRTxClientUniPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 9),
    _Hh3cDHCPRTxClientUniPktNum_Type()
)
hh3cDHCPRTxClientUniPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPRTxClientUniPktNum.setStatus("current")
_Hh3cDHCPRTxClientBroPktNum_Type = Integer32
_Hh3cDHCPRTxClientBroPktNum_Object = MibScalar
hh3cDHCPRTxClientBroPktNum = _Hh3cDHCPRTxClientBroPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 10),
    _Hh3cDHCPRTxClientBroPktNum_Type()
)
hh3cDHCPRTxClientBroPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPRTxClientBroPktNum.setStatus("current")
_Hh3cDHCPRelayDiscoverPktNum_Type = Integer32
_Hh3cDHCPRelayDiscoverPktNum_Object = MibScalar
hh3cDHCPRelayDiscoverPktNum = _Hh3cDHCPRelayDiscoverPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 11),
    _Hh3cDHCPRelayDiscoverPktNum_Type()
)
hh3cDHCPRelayDiscoverPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPRelayDiscoverPktNum.setStatus("current")
_Hh3cDHCPRelayRequestPktNum_Type = Integer32
_Hh3cDHCPRelayRequestPktNum_Object = MibScalar
hh3cDHCPRelayRequestPktNum = _Hh3cDHCPRelayRequestPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 12),
    _Hh3cDHCPRelayRequestPktNum_Type()
)
hh3cDHCPRelayRequestPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPRelayRequestPktNum.setStatus("current")
_Hh3cDHCPRelayDeclinePktNum_Type = Integer32
_Hh3cDHCPRelayDeclinePktNum_Object = MibScalar
hh3cDHCPRelayDeclinePktNum = _Hh3cDHCPRelayDeclinePktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 13),
    _Hh3cDHCPRelayDeclinePktNum_Type()
)
hh3cDHCPRelayDeclinePktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPRelayDeclinePktNum.setStatus("current")
_Hh3cDHCPRelayReleasePktNum_Type = Integer32
_Hh3cDHCPRelayReleasePktNum_Object = MibScalar
hh3cDHCPRelayReleasePktNum = _Hh3cDHCPRelayReleasePktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 14),
    _Hh3cDHCPRelayReleasePktNum_Type()
)
hh3cDHCPRelayReleasePktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPRelayReleasePktNum.setStatus("current")
_Hh3cDHCPRelayInformPktNum_Type = Integer32
_Hh3cDHCPRelayInformPktNum_Object = MibScalar
hh3cDHCPRelayInformPktNum = _Hh3cDHCPRelayInformPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 15),
    _Hh3cDHCPRelayInformPktNum_Type()
)
hh3cDHCPRelayInformPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPRelayInformPktNum.setStatus("current")
_Hh3cDHCPRelayOfferPktNum_Type = Integer32
_Hh3cDHCPRelayOfferPktNum_Object = MibScalar
hh3cDHCPRelayOfferPktNum = _Hh3cDHCPRelayOfferPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 16),
    _Hh3cDHCPRelayOfferPktNum_Type()
)
hh3cDHCPRelayOfferPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPRelayOfferPktNum.setStatus("current")
_Hh3cDHCPRelayAckPktNum_Type = Integer32
_Hh3cDHCPRelayAckPktNum_Object = MibScalar
hh3cDHCPRelayAckPktNum = _Hh3cDHCPRelayAckPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 17),
    _Hh3cDHCPRelayAckPktNum_Type()
)
hh3cDHCPRelayAckPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPRelayAckPktNum.setStatus("current")
_Hh3cDHCPRelayNakPktNum_Type = Integer32
_Hh3cDHCPRelayNakPktNum_Object = MibScalar
hh3cDHCPRelayNakPktNum = _Hh3cDHCPRelayNakPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 18),
    _Hh3cDHCPRelayNakPktNum_Type()
)
hh3cDHCPRelayNakPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPRelayNakPktNum.setStatus("current")


class _Hh3cDHCPRelayStatisticsReset_Type(Integer32):
    """Custom type hh3cDHCPRelayStatisticsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("reset", 1))
    )


_Hh3cDHCPRelayStatisticsReset_Type.__name__ = "Integer32"
_Hh3cDHCPRelayStatisticsReset_Object = MibScalar
hh3cDHCPRelayStatisticsReset = _Hh3cDHCPRelayStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 1, 19),
    _Hh3cDHCPRelayStatisticsReset_Type()
)
hh3cDHCPRelayStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPRelayStatisticsReset.setStatus("current")
_Hh3cDHCPRelayMIBConformance_ObjectIdentity = ObjectIdentity
hh3cDHCPRelayMIBConformance = _Hh3cDHCPRelayMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 2)
)
_Hh3cDHCPRelayMIBCompliances_ObjectIdentity = ObjectIdentity
hh3cDHCPRelayMIBCompliances = _Hh3cDHCPRelayMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 2, 1)
)
_Hh3cDHCPRelayMIBGroups_ObjectIdentity = ObjectIdentity
hh3cDHCPRelayMIBGroups = _Hh3cDHCPRelayMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 2, 2)
)

# Managed Objects groups

hh3cDHCPRelayMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1, 2, 2, 1)
)
hh3cDHCPRelayMIBGroup.setObjects(
      *(("HH3C-DHCPR-MIB", "hh3cDHCPRIPAddr"),
        ("HH3C-DHCPR-MIB", "hh3cDHCPRIPRowStatus"),
        ("HH3C-DHCPR-MIB", "hh3cDHCPRSelectAllocateMode"),
        ("HH3C-DHCPR-MIB", "hh3cDHCPRelayCycleStatus"),
        ("HH3C-DHCPR-MIB", "hh3cDHCPRRxBadPktNum"),
        ("HH3C-DHCPR-MIB", "hh3cDHCPRRxServerPktNum"),
        ("HH3C-DHCPR-MIB", "hh3cDHCPRTxServerPktNum"),
        ("HH3C-DHCPR-MIB", "hh3cDHCPRRxClientPktNum"),
        ("HH3C-DHCPR-MIB", "hh3cDHCPRTxClientPktNum"),
        ("HH3C-DHCPR-MIB", "hh3cDHCPRTxClientUniPktNum"),
        ("HH3C-DHCPR-MIB", "hh3cDHCPRTxClientBroPktNum"),
        ("HH3C-DHCPR-MIB", "hh3cDHCPRelayDiscoverPktNum"),
        ("HH3C-DHCPR-MIB", "hh3cDHCPRelayRequestPktNum"),
        ("HH3C-DHCPR-MIB", "hh3cDHCPRelayDeclinePktNum"),
        ("HH3C-DHCPR-MIB", "hh3cDHCPRelayReleasePktNum"),
        ("HH3C-DHCPR-MIB", "hh3cDHCPRelayInformPktNum"),
        ("HH3C-DHCPR-MIB", "hh3cDHCPRelayOfferPktNum"),
        ("HH3C-DHCPR-MIB", "hh3cDHCPRelayAckPktNum"),
        ("HH3C-DHCPR-MIB", "hh3cDHCPRelayNakPktNum"),
        ("HH3C-DHCPR-MIB", "hh3cDHCPRelayStatisticsReset"))
)
if mibBuilder.loadTexts:
    hh3cDHCPRelayMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DHCPR-MIB",
    **{"hh3cDHCPRelayMib": hh3cDHCPRelayMib,
       "hh3cDHCPRelayMibObject": hh3cDHCPRelayMibObject,
       "hh3cDHCPRIPTable": hh3cDHCPRIPTable,
       "hh3cDHCPRIPEntry": hh3cDHCPRIPEntry,
       "hh3cDHCPRIPAddr": hh3cDHCPRIPAddr,
       "hh3cDHCPRIPRowStatus": hh3cDHCPRIPRowStatus,
       "hh3cDHCPRSeletAllocateModeTable": hh3cDHCPRSeletAllocateModeTable,
       "hh3cDHCPRSeletAllocateModeEntry": hh3cDHCPRSeletAllocateModeEntry,
       "hh3cDHCPRSelectAllocateMode": hh3cDHCPRSelectAllocateMode,
       "hh3cDHCPRelayCycleStatus": hh3cDHCPRelayCycleStatus,
       "hh3cDHCPRRxBadPktNum": hh3cDHCPRRxBadPktNum,
       "hh3cDHCPRRxServerPktNum": hh3cDHCPRRxServerPktNum,
       "hh3cDHCPRTxServerPktNum": hh3cDHCPRTxServerPktNum,
       "hh3cDHCPRRxClientPktNum": hh3cDHCPRRxClientPktNum,
       "hh3cDHCPRTxClientPktNum": hh3cDHCPRTxClientPktNum,
       "hh3cDHCPRTxClientUniPktNum": hh3cDHCPRTxClientUniPktNum,
       "hh3cDHCPRTxClientBroPktNum": hh3cDHCPRTxClientBroPktNum,
       "hh3cDHCPRelayDiscoverPktNum": hh3cDHCPRelayDiscoverPktNum,
       "hh3cDHCPRelayRequestPktNum": hh3cDHCPRelayRequestPktNum,
       "hh3cDHCPRelayDeclinePktNum": hh3cDHCPRelayDeclinePktNum,
       "hh3cDHCPRelayReleasePktNum": hh3cDHCPRelayReleasePktNum,
       "hh3cDHCPRelayInformPktNum": hh3cDHCPRelayInformPktNum,
       "hh3cDHCPRelayOfferPktNum": hh3cDHCPRelayOfferPktNum,
       "hh3cDHCPRelayAckPktNum": hh3cDHCPRelayAckPktNum,
       "hh3cDHCPRelayNakPktNum": hh3cDHCPRelayNakPktNum,
       "hh3cDHCPRelayStatisticsReset": hh3cDHCPRelayStatisticsReset,
       "hh3cDHCPRelayMIBConformance": hh3cDHCPRelayMIBConformance,
       "hh3cDHCPRelayMIBCompliances": hh3cDHCPRelayMIBCompliances,
       "hh3cDHCPRelayMIBGroups": hh3cDHCPRelayMIBGroups,
       "hh3cDHCPRelayMIBGroup": hh3cDHCPRelayMIBGroup}
)
