# SNMP MIB module (HPN-ICF-DHCPR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-DHCPR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:41 2024
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

(hpnicfRhw,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfRhw")

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

hpnicfDHCPRelayMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1)
)
hpnicfDHCPRelayMib.setRevisions(
        ("2003-02-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfDHCPRelayMibObject_ObjectIdentity = ObjectIdentity
hpnicfDHCPRelayMibObject = _HpnicfDHCPRelayMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1)
)
_HpnicfDHCPRIPTable_Object = MibTable
hpnicfDHCPRIPTable = _HpnicfDHCPRIPTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfDHCPRIPTable.setStatus("current")
_HpnicfDHCPRIPEntry_Object = MibTableRow
hpnicfDHCPRIPEntry = _HpnicfDHCPRIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 1, 1)
)
hpnicfDHCPRIPEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-DHCPR-MIB", "hpnicfDHCPRIPAddr"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPRIPEntry.setStatus("current")
_HpnicfDHCPRIPAddr_Type = IpAddress
_HpnicfDHCPRIPAddr_Object = MibTableColumn
hpnicfDHCPRIPAddr = _HpnicfDHCPRIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 1, 1, 1),
    _HpnicfDHCPRIPAddr_Type()
)
hpnicfDHCPRIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPRIPAddr.setStatus("current")
_HpnicfDHCPRIPRowStatus_Type = RowStatus
_HpnicfDHCPRIPRowStatus_Object = MibTableColumn
hpnicfDHCPRIPRowStatus = _HpnicfDHCPRIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 1, 1, 2),
    _HpnicfDHCPRIPRowStatus_Type()
)
hpnicfDHCPRIPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPRIPRowStatus.setStatus("current")
_HpnicfDHCPRSeletAllocateModeTable_Object = MibTable
hpnicfDHCPRSeletAllocateModeTable = _HpnicfDHCPRSeletAllocateModeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfDHCPRSeletAllocateModeTable.setStatus("current")
_HpnicfDHCPRSeletAllocateModeEntry_Object = MibTableRow
hpnicfDHCPRSeletAllocateModeEntry = _HpnicfDHCPRSeletAllocateModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 2, 1)
)
hpnicfDHCPRSeletAllocateModeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPRSeletAllocateModeEntry.setStatus("current")


class _HpnicfDHCPRSelectAllocateMode_Type(Integer32):
    """Custom type hpnicfDHCPRSelectAllocateMode based on Integer32"""
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


_HpnicfDHCPRSelectAllocateMode_Type.__name__ = "Integer32"
_HpnicfDHCPRSelectAllocateMode_Object = MibTableColumn
hpnicfDHCPRSelectAllocateMode = _HpnicfDHCPRSelectAllocateMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 2, 1, 1),
    _HpnicfDHCPRSelectAllocateMode_Type()
)
hpnicfDHCPRSelectAllocateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPRSelectAllocateMode.setStatus("current")


class _HpnicfDHCPRelayCycleStatus_Type(Integer32):
    """Custom type hpnicfDHCPRelayCycleStatus based on Integer32"""
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


_HpnicfDHCPRelayCycleStatus_Type.__name__ = "Integer32"
_HpnicfDHCPRelayCycleStatus_Object = MibScalar
hpnicfDHCPRelayCycleStatus = _HpnicfDHCPRelayCycleStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 3),
    _HpnicfDHCPRelayCycleStatus_Type()
)
hpnicfDHCPRelayCycleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPRelayCycleStatus.setStatus("current")
_HpnicfDHCPRRxBadPktNum_Type = Integer32
_HpnicfDHCPRRxBadPktNum_Object = MibScalar
hpnicfDHCPRRxBadPktNum = _HpnicfDHCPRRxBadPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 4),
    _HpnicfDHCPRRxBadPktNum_Type()
)
hpnicfDHCPRRxBadPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPRRxBadPktNum.setStatus("current")
_HpnicfDHCPRRxServerPktNum_Type = Integer32
_HpnicfDHCPRRxServerPktNum_Object = MibScalar
hpnicfDHCPRRxServerPktNum = _HpnicfDHCPRRxServerPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 5),
    _HpnicfDHCPRRxServerPktNum_Type()
)
hpnicfDHCPRRxServerPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPRRxServerPktNum.setStatus("current")
_HpnicfDHCPRTxServerPktNum_Type = Integer32
_HpnicfDHCPRTxServerPktNum_Object = MibScalar
hpnicfDHCPRTxServerPktNum = _HpnicfDHCPRTxServerPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 6),
    _HpnicfDHCPRTxServerPktNum_Type()
)
hpnicfDHCPRTxServerPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPRTxServerPktNum.setStatus("current")
_HpnicfDHCPRRxClientPktNum_Type = Integer32
_HpnicfDHCPRRxClientPktNum_Object = MibScalar
hpnicfDHCPRRxClientPktNum = _HpnicfDHCPRRxClientPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 7),
    _HpnicfDHCPRRxClientPktNum_Type()
)
hpnicfDHCPRRxClientPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPRRxClientPktNum.setStatus("current")
_HpnicfDHCPRTxClientPktNum_Type = Integer32
_HpnicfDHCPRTxClientPktNum_Object = MibScalar
hpnicfDHCPRTxClientPktNum = _HpnicfDHCPRTxClientPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 8),
    _HpnicfDHCPRTxClientPktNum_Type()
)
hpnicfDHCPRTxClientPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPRTxClientPktNum.setStatus("current")
_HpnicfDHCPRTxClientUniPktNum_Type = Integer32
_HpnicfDHCPRTxClientUniPktNum_Object = MibScalar
hpnicfDHCPRTxClientUniPktNum = _HpnicfDHCPRTxClientUniPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 9),
    _HpnicfDHCPRTxClientUniPktNum_Type()
)
hpnicfDHCPRTxClientUniPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPRTxClientUniPktNum.setStatus("current")
_HpnicfDHCPRTxClientBroPktNum_Type = Integer32
_HpnicfDHCPRTxClientBroPktNum_Object = MibScalar
hpnicfDHCPRTxClientBroPktNum = _HpnicfDHCPRTxClientBroPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 10),
    _HpnicfDHCPRTxClientBroPktNum_Type()
)
hpnicfDHCPRTxClientBroPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPRTxClientBroPktNum.setStatus("current")
_HpnicfDHCPRelayDiscoverPktNum_Type = Integer32
_HpnicfDHCPRelayDiscoverPktNum_Object = MibScalar
hpnicfDHCPRelayDiscoverPktNum = _HpnicfDHCPRelayDiscoverPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 11),
    _HpnicfDHCPRelayDiscoverPktNum_Type()
)
hpnicfDHCPRelayDiscoverPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPRelayDiscoverPktNum.setStatus("current")
_HpnicfDHCPRelayRequestPktNum_Type = Integer32
_HpnicfDHCPRelayRequestPktNum_Object = MibScalar
hpnicfDHCPRelayRequestPktNum = _HpnicfDHCPRelayRequestPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 12),
    _HpnicfDHCPRelayRequestPktNum_Type()
)
hpnicfDHCPRelayRequestPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPRelayRequestPktNum.setStatus("current")
_HpnicfDHCPRelayDeclinePktNum_Type = Integer32
_HpnicfDHCPRelayDeclinePktNum_Object = MibScalar
hpnicfDHCPRelayDeclinePktNum = _HpnicfDHCPRelayDeclinePktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 13),
    _HpnicfDHCPRelayDeclinePktNum_Type()
)
hpnicfDHCPRelayDeclinePktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPRelayDeclinePktNum.setStatus("current")
_HpnicfDHCPRelayReleasePktNum_Type = Integer32
_HpnicfDHCPRelayReleasePktNum_Object = MibScalar
hpnicfDHCPRelayReleasePktNum = _HpnicfDHCPRelayReleasePktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 14),
    _HpnicfDHCPRelayReleasePktNum_Type()
)
hpnicfDHCPRelayReleasePktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPRelayReleasePktNum.setStatus("current")
_HpnicfDHCPRelayInformPktNum_Type = Integer32
_HpnicfDHCPRelayInformPktNum_Object = MibScalar
hpnicfDHCPRelayInformPktNum = _HpnicfDHCPRelayInformPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 15),
    _HpnicfDHCPRelayInformPktNum_Type()
)
hpnicfDHCPRelayInformPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPRelayInformPktNum.setStatus("current")
_HpnicfDHCPRelayOfferPktNum_Type = Integer32
_HpnicfDHCPRelayOfferPktNum_Object = MibScalar
hpnicfDHCPRelayOfferPktNum = _HpnicfDHCPRelayOfferPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 16),
    _HpnicfDHCPRelayOfferPktNum_Type()
)
hpnicfDHCPRelayOfferPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPRelayOfferPktNum.setStatus("current")
_HpnicfDHCPRelayAckPktNum_Type = Integer32
_HpnicfDHCPRelayAckPktNum_Object = MibScalar
hpnicfDHCPRelayAckPktNum = _HpnicfDHCPRelayAckPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 17),
    _HpnicfDHCPRelayAckPktNum_Type()
)
hpnicfDHCPRelayAckPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPRelayAckPktNum.setStatus("current")
_HpnicfDHCPRelayNakPktNum_Type = Integer32
_HpnicfDHCPRelayNakPktNum_Object = MibScalar
hpnicfDHCPRelayNakPktNum = _HpnicfDHCPRelayNakPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 18),
    _HpnicfDHCPRelayNakPktNum_Type()
)
hpnicfDHCPRelayNakPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPRelayNakPktNum.setStatus("current")


class _HpnicfDHCPRelayStatisticsReset_Type(Integer32):
    """Custom type hpnicfDHCPRelayStatisticsReset based on Integer32"""
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


_HpnicfDHCPRelayStatisticsReset_Type.__name__ = "Integer32"
_HpnicfDHCPRelayStatisticsReset_Object = MibScalar
hpnicfDHCPRelayStatisticsReset = _HpnicfDHCPRelayStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 1, 19),
    _HpnicfDHCPRelayStatisticsReset_Type()
)
hpnicfDHCPRelayStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPRelayStatisticsReset.setStatus("current")
_HpnicfDHCPRelayMIBConformance_ObjectIdentity = ObjectIdentity
hpnicfDHCPRelayMIBConformance = _HpnicfDHCPRelayMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 2)
)
_HpnicfDHCPRelayMIBCompliances_ObjectIdentity = ObjectIdentity
hpnicfDHCPRelayMIBCompliances = _HpnicfDHCPRelayMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 2, 1)
)
_HpnicfDHCPRelayMIBGroups_ObjectIdentity = ObjectIdentity
hpnicfDHCPRelayMIBGroups = _HpnicfDHCPRelayMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 2, 2)
)

# Managed Objects groups

hpnicfDHCPRelayMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1, 2, 2, 1)
)
hpnicfDHCPRelayMIBGroup.setObjects(
      *(("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRIPAddr"),
        ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRIPRowStatus"),
        ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRSelectAllocateMode"),
        ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRelayCycleStatus"),
        ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRRxBadPktNum"),
        ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRRxServerPktNum"),
        ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRTxServerPktNum"),
        ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRRxClientPktNum"),
        ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRTxClientPktNum"),
        ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRTxClientUniPktNum"),
        ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRTxClientBroPktNum"),
        ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRelayDiscoverPktNum"),
        ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRelayRequestPktNum"),
        ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRelayDeclinePktNum"),
        ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRelayReleasePktNum"),
        ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRelayInformPktNum"),
        ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRelayOfferPktNum"),
        ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRelayAckPktNum"),
        ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRelayNakPktNum"),
        ("HPN-ICF-DHCPR-MIB", "hpnicfDHCPRelayStatisticsReset"))
)
if mibBuilder.loadTexts:
    hpnicfDHCPRelayMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-DHCPR-MIB",
    **{"hpnicfDHCPRelayMib": hpnicfDHCPRelayMib,
       "hpnicfDHCPRelayMibObject": hpnicfDHCPRelayMibObject,
       "hpnicfDHCPRIPTable": hpnicfDHCPRIPTable,
       "hpnicfDHCPRIPEntry": hpnicfDHCPRIPEntry,
       "hpnicfDHCPRIPAddr": hpnicfDHCPRIPAddr,
       "hpnicfDHCPRIPRowStatus": hpnicfDHCPRIPRowStatus,
       "hpnicfDHCPRSeletAllocateModeTable": hpnicfDHCPRSeletAllocateModeTable,
       "hpnicfDHCPRSeletAllocateModeEntry": hpnicfDHCPRSeletAllocateModeEntry,
       "hpnicfDHCPRSelectAllocateMode": hpnicfDHCPRSelectAllocateMode,
       "hpnicfDHCPRelayCycleStatus": hpnicfDHCPRelayCycleStatus,
       "hpnicfDHCPRRxBadPktNum": hpnicfDHCPRRxBadPktNum,
       "hpnicfDHCPRRxServerPktNum": hpnicfDHCPRRxServerPktNum,
       "hpnicfDHCPRTxServerPktNum": hpnicfDHCPRTxServerPktNum,
       "hpnicfDHCPRRxClientPktNum": hpnicfDHCPRRxClientPktNum,
       "hpnicfDHCPRTxClientPktNum": hpnicfDHCPRTxClientPktNum,
       "hpnicfDHCPRTxClientUniPktNum": hpnicfDHCPRTxClientUniPktNum,
       "hpnicfDHCPRTxClientBroPktNum": hpnicfDHCPRTxClientBroPktNum,
       "hpnicfDHCPRelayDiscoverPktNum": hpnicfDHCPRelayDiscoverPktNum,
       "hpnicfDHCPRelayRequestPktNum": hpnicfDHCPRelayRequestPktNum,
       "hpnicfDHCPRelayDeclinePktNum": hpnicfDHCPRelayDeclinePktNum,
       "hpnicfDHCPRelayReleasePktNum": hpnicfDHCPRelayReleasePktNum,
       "hpnicfDHCPRelayInformPktNum": hpnicfDHCPRelayInformPktNum,
       "hpnicfDHCPRelayOfferPktNum": hpnicfDHCPRelayOfferPktNum,
       "hpnicfDHCPRelayAckPktNum": hpnicfDHCPRelayAckPktNum,
       "hpnicfDHCPRelayNakPktNum": hpnicfDHCPRelayNakPktNum,
       "hpnicfDHCPRelayStatisticsReset": hpnicfDHCPRelayStatisticsReset,
       "hpnicfDHCPRelayMIBConformance": hpnicfDHCPRelayMIBConformance,
       "hpnicfDHCPRelayMIBCompliances": hpnicfDHCPRelayMIBCompliances,
       "hpnicfDHCPRelayMIBGroups": hpnicfDHCPRelayMIBGroups,
       "hpnicfDHCPRelayMIBGroup": hpnicfDHCPRelayMIBGroup}
)
