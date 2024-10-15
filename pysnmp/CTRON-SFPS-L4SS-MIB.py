# SNMP MIB module (CTRON-SFPS-L4SS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SFPS-L4SS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:26 2024
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

(switchSFPS,) = mibBuilder.importSymbols(
    "CTRON-SFPS-INCLUDE-MIB",
    "switchSFPS")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class HexInteger(Integer32):
    """Custom type HexInteger based on Integer32"""




class SfpsAddress(OctetString):
    """Custom type SfpsAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SfpsL4SS_ObjectIdentity = ObjectIdentity
sfpsL4SS = _SfpsL4SS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6)
)
_SfpsL4CP_ObjectIdentity = ObjectIdentity
sfpsL4CP = _SfpsL4CP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1)
)
_L4cpStats_ObjectIdentity = ObjectIdentity
l4cpStats = _L4cpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1)
)
_L4cpConfig_ObjectIdentity = ObjectIdentity
l4cpConfig = _L4cpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2)
)


class _SfpsL4CPDisableTCPAckCheck_Type(Integer32):
    """Custom type sfpsL4CPDisableTCPAckCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SfpsL4CPDisableTCPAckCheck_Type.__name__ = "Integer32"
_SfpsL4CPDisableTCPAckCheck_Object = MibScalar
sfpsL4CPDisableTCPAckCheck = _SfpsL4CPDisableTCPAckCheck_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 1),
    _SfpsL4CPDisableTCPAckCheck_Type()
)
sfpsL4CPDisableTCPAckCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsL4CPDisableTCPAckCheck.setStatus("mandatory")
_L4cpActions_ObjectIdentity = ObjectIdentity
l4cpActions = _L4cpActions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 3)
)
_SfpsL4CPFlowTable_Object = MibTable
sfpsL4CPFlowTable = _SfpsL4CPFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 4)
)
if mibBuilder.loadTexts:
    sfpsL4CPFlowTable.setStatus("mandatory")
_SfpsL4CPFlowEntry_Object = MibTableRow
sfpsL4CPFlowEntry = _SfpsL4CPFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 4, 1)
)
sfpsL4CPFlowEntry.setIndexNames(
    (0, "CTRON-SFPS-L4SS-MIB", "sfpsL4CPFlowCnxIndex"),
    (0, "CTRON-SFPS-L4SS-MIB", "sfpsL4CPFlowSecL3Address"),
    (0, "CTRON-SFPS-L4SS-MIB", "sfpsL4CPFlowPrimL3Address"),
    (0, "CTRON-SFPS-L4SS-MIB", "sfpsL4CPFlowSubprotocol"),
    (0, "CTRON-SFPS-L4SS-MIB", "sfpsL4CPFlowSecMatchAnyDyn"),
    (0, "CTRON-SFPS-L4SS-MIB", "sfpsL4CPFlowPrimMatchAnyDyn"),
    (0, "CTRON-SFPS-L4SS-MIB", "sfpsL4CPFlowSecProtPort"),
    (0, "CTRON-SFPS-L4SS-MIB", "sfpsL4CPFlowPrimProtPort"),
)
if mibBuilder.loadTexts:
    sfpsL4CPFlowEntry.setStatus("mandatory")


class _SfpsL4CPFlowCnxIndex_Type(Integer32):
    """Custom type sfpsL4CPFlowCnxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SfpsL4CPFlowCnxIndex_Type.__name__ = "Integer32"
_SfpsL4CPFlowCnxIndex_Object = MibTableColumn
sfpsL4CPFlowCnxIndex = _SfpsL4CPFlowCnxIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 4, 1, 1),
    _SfpsL4CPFlowCnxIndex_Type()
)
sfpsL4CPFlowCnxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPFlowCnxIndex.setStatus("mandatory")
_SfpsL4CPFlowSecL3Address_Type = DisplayString
_SfpsL4CPFlowSecL3Address_Object = MibTableColumn
sfpsL4CPFlowSecL3Address = _SfpsL4CPFlowSecL3Address_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 4, 1, 2),
    _SfpsL4CPFlowSecL3Address_Type()
)
sfpsL4CPFlowSecL3Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPFlowSecL3Address.setStatus("mandatory")
_SfpsL4CPFlowPrimL3Address_Type = DisplayString
_SfpsL4CPFlowPrimL3Address_Object = MibTableColumn
sfpsL4CPFlowPrimL3Address = _SfpsL4CPFlowPrimL3Address_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 4, 1, 3),
    _SfpsL4CPFlowPrimL3Address_Type()
)
sfpsL4CPFlowPrimL3Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPFlowPrimL3Address.setStatus("mandatory")


class _SfpsL4CPFlowSubprotocol_Type(HexInteger):
    """Custom type sfpsL4CPFlowSubprotocol based on HexInteger"""
    subtypeSpec = HexInteger.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SfpsL4CPFlowSubprotocol_Type.__name__ = "HexInteger"
_SfpsL4CPFlowSubprotocol_Object = MibTableColumn
sfpsL4CPFlowSubprotocol = _SfpsL4CPFlowSubprotocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 4, 1, 4),
    _SfpsL4CPFlowSubprotocol_Type()
)
sfpsL4CPFlowSubprotocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPFlowSubprotocol.setStatus("mandatory")


class _SfpsL4CPFlowSecMatchAnyDyn_Type(Integer32):
    """Custom type sfpsL4CPFlowSecMatchAnyDyn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SfpsL4CPFlowSecMatchAnyDyn_Type.__name__ = "Integer32"
_SfpsL4CPFlowSecMatchAnyDyn_Object = MibTableColumn
sfpsL4CPFlowSecMatchAnyDyn = _SfpsL4CPFlowSecMatchAnyDyn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 4, 1, 5),
    _SfpsL4CPFlowSecMatchAnyDyn_Type()
)
sfpsL4CPFlowSecMatchAnyDyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPFlowSecMatchAnyDyn.setStatus("mandatory")


class _SfpsL4CPFlowPrimMatchAnyDyn_Type(Integer32):
    """Custom type sfpsL4CPFlowPrimMatchAnyDyn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SfpsL4CPFlowPrimMatchAnyDyn_Type.__name__ = "Integer32"
_SfpsL4CPFlowPrimMatchAnyDyn_Object = MibTableColumn
sfpsL4CPFlowPrimMatchAnyDyn = _SfpsL4CPFlowPrimMatchAnyDyn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 4, 1, 6),
    _SfpsL4CPFlowPrimMatchAnyDyn_Type()
)
sfpsL4CPFlowPrimMatchAnyDyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPFlowPrimMatchAnyDyn.setStatus("mandatory")


class _SfpsL4CPFlowSecProtPort_Type(Integer32):
    """Custom type sfpsL4CPFlowSecProtPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpsL4CPFlowSecProtPort_Type.__name__ = "Integer32"
_SfpsL4CPFlowSecProtPort_Object = MibTableColumn
sfpsL4CPFlowSecProtPort = _SfpsL4CPFlowSecProtPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 4, 1, 7),
    _SfpsL4CPFlowSecProtPort_Type()
)
sfpsL4CPFlowSecProtPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPFlowSecProtPort.setStatus("mandatory")


class _SfpsL4CPFlowPrimProtPort_Type(Integer32):
    """Custom type sfpsL4CPFlowPrimProtPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpsL4CPFlowPrimProtPort_Type.__name__ = "Integer32"
_SfpsL4CPFlowPrimProtPort_Object = MibTableColumn
sfpsL4CPFlowPrimProtPort = _SfpsL4CPFlowPrimProtPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 4, 1, 8),
    _SfpsL4CPFlowPrimProtPort_Type()
)
sfpsL4CPFlowPrimProtPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPFlowPrimProtPort.setStatus("mandatory")


class _SfpsL4CPFlowSecSubstApplies_Type(Integer32):
    """Custom type sfpsL4CPFlowSecSubstApplies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SfpsL4CPFlowSecSubstApplies_Type.__name__ = "Integer32"
_SfpsL4CPFlowSecSubstApplies_Object = MibTableColumn
sfpsL4CPFlowSecSubstApplies = _SfpsL4CPFlowSecSubstApplies_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 4, 1, 9),
    _SfpsL4CPFlowSecSubstApplies_Type()
)
sfpsL4CPFlowSecSubstApplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPFlowSecSubstApplies.setStatus("mandatory")


class _SfpsL4CPFlowPrimSubstApplies_Type(Integer32):
    """Custom type sfpsL4CPFlowPrimSubstApplies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SfpsL4CPFlowPrimSubstApplies_Type.__name__ = "Integer32"
_SfpsL4CPFlowPrimSubstApplies_Object = MibTableColumn
sfpsL4CPFlowPrimSubstApplies = _SfpsL4CPFlowPrimSubstApplies_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 4, 1, 10),
    _SfpsL4CPFlowPrimSubstApplies_Type()
)
sfpsL4CPFlowPrimSubstApplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPFlowPrimSubstApplies.setStatus("mandatory")
_SfpsL4CPFlowSecInPkts_Type = Counter32
_SfpsL4CPFlowSecInPkts_Object = MibTableColumn
sfpsL4CPFlowSecInPkts = _SfpsL4CPFlowSecInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 4, 1, 11),
    _SfpsL4CPFlowSecInPkts_Type()
)
sfpsL4CPFlowSecInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPFlowSecInPkts.setStatus("mandatory")
_SfpsL4CPFlowSecInOctets_Type = Counter32
_SfpsL4CPFlowSecInOctets_Object = MibTableColumn
sfpsL4CPFlowSecInOctets = _SfpsL4CPFlowSecInOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 4, 1, 12),
    _SfpsL4CPFlowSecInOctets_Type()
)
sfpsL4CPFlowSecInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPFlowSecInOctets.setStatus("mandatory")
_SfpsL4CPFlowPrimInPkts_Type = Counter32
_SfpsL4CPFlowPrimInPkts_Object = MibTableColumn
sfpsL4CPFlowPrimInPkts = _SfpsL4CPFlowPrimInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 4, 1, 13),
    _SfpsL4CPFlowPrimInPkts_Type()
)
sfpsL4CPFlowPrimInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPFlowPrimInPkts.setStatus("mandatory")
_SfpsL4CPFlowPrimInOctets_Type = Counter32
_SfpsL4CPFlowPrimInOctets_Object = MibTableColumn
sfpsL4CPFlowPrimInOctets = _SfpsL4CPFlowPrimInOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 4, 1, 14),
    _SfpsL4CPFlowPrimInOctets_Type()
)
sfpsL4CPFlowPrimInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPFlowPrimInOctets.setStatus("mandatory")
_SfpsL4CPFlowFlowAge_Type = TimeTicks
_SfpsL4CPFlowFlowAge_Object = MibTableColumn
sfpsL4CPFlowFlowAge = _SfpsL4CPFlowFlowAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 4, 1, 15),
    _SfpsL4CPFlowFlowAge_Type()
)
sfpsL4CPFlowFlowAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPFlowFlowAge.setStatus("mandatory")
_SfpsL4CPFlowFlowLastUse_Type = TimeTicks
_SfpsL4CPFlowFlowLastUse_Object = MibTableColumn
sfpsL4CPFlowFlowLastUse = _SfpsL4CPFlowFlowLastUse_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 4, 1, 16),
    _SfpsL4CPFlowFlowLastUse_Type()
)
sfpsL4CPFlowFlowLastUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPFlowFlowLastUse.setStatus("mandatory")
_SfpsL4CPFlowID_Type = Integer32
_SfpsL4CPFlowID_Object = MibTableColumn
sfpsL4CPFlowID = _SfpsL4CPFlowID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 4, 1, 17),
    _SfpsL4CPFlowID_Type()
)
sfpsL4CPFlowID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPFlowID.setStatus("mandatory")
_SfpsL4CPMACAddrSubTable_Object = MibTable
sfpsL4CPMACAddrSubTable = _SfpsL4CPMACAddrSubTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 5)
)
if mibBuilder.loadTexts:
    sfpsL4CPMACAddrSubTable.setStatus("mandatory")
_SfpsL4CPMACAddrSubEntry_Object = MibTableRow
sfpsL4CPMACAddrSubEntry = _SfpsL4CPMACAddrSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 5, 1)
)
sfpsL4CPMACAddrSubEntry.setIndexNames(
    (0, "CTRON-SFPS-L4SS-MIB", "sfpsL4CPMACAddrSubDestIP"),
)
if mibBuilder.loadTexts:
    sfpsL4CPMACAddrSubEntry.setStatus("mandatory")
_SfpsL4CPMACAddrSubDestIP_Type = IpAddress
_SfpsL4CPMACAddrSubDestIP_Object = MibTableColumn
sfpsL4CPMACAddrSubDestIP = _SfpsL4CPMACAddrSubDestIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 5, 1, 1),
    _SfpsL4CPMACAddrSubDestIP_Type()
)
sfpsL4CPMACAddrSubDestIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPMACAddrSubDestIP.setStatus("mandatory")
_SfpsL4CPMACAddrSubNextHopMAC_Type = PhysAddress
_SfpsL4CPMACAddrSubNextHopMAC_Object = MibTableColumn
sfpsL4CPMACAddrSubNextHopMAC = _SfpsL4CPMACAddrSubNextHopMAC_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 5, 1, 2),
    _SfpsL4CPMACAddrSubNextHopMAC_Type()
)
sfpsL4CPMACAddrSubNextHopMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPMACAddrSubNextHopMAC.setStatus("mandatory")


class _SfpsL4CPMACAddrSubRefCount_Type(Integer32):
    """Custom type sfpsL4CPMACAddrSubRefCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SfpsL4CPMACAddrSubRefCount_Type.__name__ = "Integer32"
_SfpsL4CPMACAddrSubRefCount_Object = MibTableColumn
sfpsL4CPMACAddrSubRefCount = _SfpsL4CPMACAddrSubRefCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 5, 1, 3),
    _SfpsL4CPMACAddrSubRefCount_Type()
)
sfpsL4CPMACAddrSubRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPMACAddrSubRefCount.setStatus("mandatory")
_SfpsL4CPNetAddrUserTable_Object = MibTable
sfpsL4CPNetAddrUserTable = _SfpsL4CPNetAddrUserTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 7)
)
if mibBuilder.loadTexts:
    sfpsL4CPNetAddrUserTable.setStatus("mandatory")
_SfpsL4CPNetAddrUserEntry_Object = MibTableRow
sfpsL4CPNetAddrUserEntry = _SfpsL4CPNetAddrUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 7, 1)
)
sfpsL4CPNetAddrUserEntry.setIndexNames(
    (0, "CTRON-SFPS-L4SS-MIB", "sfpsL4CPNetAddrUserProtocol"),
    (0, "CTRON-SFPS-L4SS-MIB", "sfpsL4CPNetAddrUserNetAddr"),
)
if mibBuilder.loadTexts:
    sfpsL4CPNetAddrUserEntry.setStatus("mandatory")


class _SfpsL4CPNetAddrUserProtocol_Type(Integer32):
    """Custom type sfpsL4CPNetAddrUserProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SfpsL4CPNetAddrUserProtocol_Type.__name__ = "Integer32"
_SfpsL4CPNetAddrUserProtocol_Object = MibTableColumn
sfpsL4CPNetAddrUserProtocol = _SfpsL4CPNetAddrUserProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 7, 1, 1),
    _SfpsL4CPNetAddrUserProtocol_Type()
)
sfpsL4CPNetAddrUserProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPNetAddrUserProtocol.setStatus("mandatory")
_SfpsL4CPNetAddrUserNetAddr_Type = DisplayString
_SfpsL4CPNetAddrUserNetAddr_Object = MibTableColumn
sfpsL4CPNetAddrUserNetAddr = _SfpsL4CPNetAddrUserNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 7, 1, 2),
    _SfpsL4CPNetAddrUserNetAddr_Type()
)
sfpsL4CPNetAddrUserNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPNetAddrUserNetAddr.setStatus("mandatory")
_SfpsL4CPNetAddrUserLoginID_Type = Integer32
_SfpsL4CPNetAddrUserLoginID_Object = MibTableColumn
sfpsL4CPNetAddrUserLoginID = _SfpsL4CPNetAddrUserLoginID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 7, 1, 3),
    _SfpsL4CPNetAddrUserLoginID_Type()
)
sfpsL4CPNetAddrUserLoginID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPNetAddrUserLoginID.setStatus("mandatory")
_SfpsL4CPNetAddrUserUserID_Type = Integer32
_SfpsL4CPNetAddrUserUserID_Object = MibTableColumn
sfpsL4CPNetAddrUserUserID = _SfpsL4CPNetAddrUserUserID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 7, 1, 4),
    _SfpsL4CPNetAddrUserUserID_Type()
)
sfpsL4CPNetAddrUserUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPNetAddrUserUserID.setStatus("mandatory")
_SfpsL4CPNetAddrUserUserName_Type = DisplayString
_SfpsL4CPNetAddrUserUserName_Object = MibTableColumn
sfpsL4CPNetAddrUserUserName = _SfpsL4CPNetAddrUserUserName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 7, 1, 5),
    _SfpsL4CPNetAddrUserUserName_Type()
)
sfpsL4CPNetAddrUserUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPNetAddrUserUserName.setStatus("mandatory")
_SfpsL4CPIPRouteTable_Object = MibTable
sfpsL4CPIPRouteTable = _SfpsL4CPIPRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 8)
)
if mibBuilder.loadTexts:
    sfpsL4CPIPRouteTable.setStatus("mandatory")
_SfpsL4CPIPRouteEntry_Object = MibTableRow
sfpsL4CPIPRouteEntry = _SfpsL4CPIPRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 8, 1)
)
sfpsL4CPIPRouteEntry.setIndexNames(
    (0, "CTRON-SFPS-L4SS-MIB", "sfpsL4CPIPRouteSubnetMask"),
    (0, "CTRON-SFPS-L4SS-MIB", "sfpsL4CPIPRouteSubnet"),
)
if mibBuilder.loadTexts:
    sfpsL4CPIPRouteEntry.setStatus("mandatory")
_SfpsL4CPIPRouteSubnetMask_Type = IpAddress
_SfpsL4CPIPRouteSubnetMask_Object = MibTableColumn
sfpsL4CPIPRouteSubnetMask = _SfpsL4CPIPRouteSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 8, 1, 1),
    _SfpsL4CPIPRouteSubnetMask_Type()
)
sfpsL4CPIPRouteSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPIPRouteSubnetMask.setStatus("mandatory")
_SfpsL4CPIPRouteSubnet_Type = IpAddress
_SfpsL4CPIPRouteSubnet_Object = MibTableColumn
sfpsL4CPIPRouteSubnet = _SfpsL4CPIPRouteSubnet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 8, 1, 2),
    _SfpsL4CPIPRouteSubnet_Type()
)
sfpsL4CPIPRouteSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPIPRouteSubnet.setStatus("mandatory")
_SfpsL4CPIPRouteRouteID_Type = Integer32
_SfpsL4CPIPRouteRouteID_Object = MibTableColumn
sfpsL4CPIPRouteRouteID = _SfpsL4CPIPRouteRouteID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 8, 1, 3),
    _SfpsL4CPIPRouteRouteID_Type()
)
sfpsL4CPIPRouteRouteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPIPRouteRouteID.setStatus("mandatory")


class _SfpsL4CPIPRouteRouteSubsystem_Type(Integer32):
    """Custom type sfpsL4CPIPRouteRouteSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_SfpsL4CPIPRouteRouteSubsystem_Type.__name__ = "Integer32"
_SfpsL4CPIPRouteRouteSubsystem_Object = MibTableColumn
sfpsL4CPIPRouteRouteSubsystem = _SfpsL4CPIPRouteRouteSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 8, 1, 4),
    _SfpsL4CPIPRouteRouteSubsystem_Type()
)
sfpsL4CPIPRouteRouteSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPIPRouteRouteSubsystem.setStatus("mandatory")
_SfpsL4CPIPRouteDeviceID_Type = Integer32
_SfpsL4CPIPRouteDeviceID_Object = MibTableColumn
sfpsL4CPIPRouteDeviceID = _SfpsL4CPIPRouteDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 8, 1, 5),
    _SfpsL4CPIPRouteDeviceID_Type()
)
sfpsL4CPIPRouteDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPIPRouteDeviceID.setStatus("mandatory")
_SfpsL4CPIPRouteDeviceName_Type = DisplayString
_SfpsL4CPIPRouteDeviceName_Object = MibTableColumn
sfpsL4CPIPRouteDeviceName = _SfpsL4CPIPRouteDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 8, 1, 6),
    _SfpsL4CPIPRouteDeviceName_Type()
)
sfpsL4CPIPRouteDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPIPRouteDeviceName.setStatus("mandatory")
_SfpsL4CPIPRouteMACAddress_Type = SfpsAddress
_SfpsL4CPIPRouteMACAddress_Object = MibTableColumn
sfpsL4CPIPRouteMACAddress = _SfpsL4CPIPRouteMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 8, 1, 7),
    _SfpsL4CPIPRouteMACAddress_Type()
)
sfpsL4CPIPRouteMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPIPRouteMACAddress.setStatus("mandatory")
_SfpsL4CPIPRouteMetric_Type = Integer32
_SfpsL4CPIPRouteMetric_Object = MibTableColumn
sfpsL4CPIPRouteMetric = _SfpsL4CPIPRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 8, 1, 8),
    _SfpsL4CPIPRouteMetric_Type()
)
sfpsL4CPIPRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPIPRouteMetric.setStatus("mandatory")


class _SfpsL4CPIPRouteCallable_Type(Integer32):
    """Custom type sfpsL4CPIPRouteCallable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SfpsL4CPIPRouteCallable_Type.__name__ = "Integer32"
_SfpsL4CPIPRouteCallable_Object = MibTableColumn
sfpsL4CPIPRouteCallable = _SfpsL4CPIPRouteCallable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 8, 1, 9),
    _SfpsL4CPIPRouteCallable_Type()
)
sfpsL4CPIPRouteCallable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPIPRouteCallable.setStatus("mandatory")
_SfpsL4CPPortTable_Object = MibTable
sfpsL4CPPortTable = _SfpsL4CPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 9)
)
if mibBuilder.loadTexts:
    sfpsL4CPPortTable.setStatus("mandatory")
_SfpsL4CPPortEntry_Object = MibTableRow
sfpsL4CPPortEntry = _SfpsL4CPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 9, 1)
)
sfpsL4CPPortEntry.setIndexNames(
    (0, "CTRON-SFPS-L4SS-MIB", "sfpsL4CPPortNum"),
)
if mibBuilder.loadTexts:
    sfpsL4CPPortEntry.setStatus("mandatory")


class _SfpsL4CPPortNum_Type(Integer32):
    """Custom type sfpsL4CPPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SfpsL4CPPortNum_Type.__name__ = "Integer32"
_SfpsL4CPPortNum_Object = MibTableColumn
sfpsL4CPPortNum = _SfpsL4CPPortNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 9, 1, 1),
    _SfpsL4CPPortNum_Type()
)
sfpsL4CPPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPPortNum.setStatus("mandatory")
_SfpsL4CPPortID_Type = Integer32
_SfpsL4CPPortID_Object = MibTableColumn
sfpsL4CPPortID = _SfpsL4CPPortID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 9, 1, 2),
    _SfpsL4CPPortID_Type()
)
sfpsL4CPPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPPortID.setStatus("mandatory")


class _SfpsL4CPPortApplyPolicyIn_Type(Integer32):
    """Custom type sfpsL4CPPortApplyPolicyIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SfpsL4CPPortApplyPolicyIn_Type.__name__ = "Integer32"
_SfpsL4CPPortApplyPolicyIn_Object = MibTableColumn
sfpsL4CPPortApplyPolicyIn = _SfpsL4CPPortApplyPolicyIn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 9, 1, 3),
    _SfpsL4CPPortApplyPolicyIn_Type()
)
sfpsL4CPPortApplyPolicyIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPPortApplyPolicyIn.setStatus("mandatory")


class _SfpsL4CPPortApplyPolicyOut_Type(Integer32):
    """Custom type sfpsL4CPPortApplyPolicyOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SfpsL4CPPortApplyPolicyOut_Type.__name__ = "Integer32"
_SfpsL4CPPortApplyPolicyOut_Object = MibTableColumn
sfpsL4CPPortApplyPolicyOut = _SfpsL4CPPortApplyPolicyOut_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 9, 1, 4),
    _SfpsL4CPPortApplyPolicyOut_Type()
)
sfpsL4CPPortApplyPolicyOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPPortApplyPolicyOut.setStatus("mandatory")
_SfpsL4CPPortDefaultUserID_Type = Integer32
_SfpsL4CPPortDefaultUserID_Object = MibTableColumn
sfpsL4CPPortDefaultUserID = _SfpsL4CPPortDefaultUserID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 9, 1, 5),
    _SfpsL4CPPortDefaultUserID_Type()
)
sfpsL4CPPortDefaultUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPPortDefaultUserID.setStatus("mandatory")
_SfpsL4CPPortDefaultUserName_Type = DisplayString
_SfpsL4CPPortDefaultUserName_Object = MibTableColumn
sfpsL4CPPortDefaultUserName = _SfpsL4CPPortDefaultUserName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 9, 1, 6),
    _SfpsL4CPPortDefaultUserName_Type()
)
sfpsL4CPPortDefaultUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPPortDefaultUserName.setStatus("mandatory")
_SfpsL4CPCallableDeviceTable_Object = MibTable
sfpsL4CPCallableDeviceTable = _SfpsL4CPCallableDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 11)
)
if mibBuilder.loadTexts:
    sfpsL4CPCallableDeviceTable.setStatus("mandatory")
_SfpsL4CPCallableDeviceEntry_Object = MibTableRow
sfpsL4CPCallableDeviceEntry = _SfpsL4CPCallableDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 11, 1)
)
sfpsL4CPCallableDeviceEntry.setIndexNames(
    (0, "CTRON-SFPS-L4SS-MIB", "sfpsL4CPCallableDeviceDeviceID"),
)
if mibBuilder.loadTexts:
    sfpsL4CPCallableDeviceEntry.setStatus("mandatory")


class _SfpsL4CPCallableDeviceDeviceID_Type(Integer32):
    """Custom type sfpsL4CPCallableDeviceDeviceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SfpsL4CPCallableDeviceDeviceID_Type.__name__ = "Integer32"
_SfpsL4CPCallableDeviceDeviceID_Object = MibTableColumn
sfpsL4CPCallableDeviceDeviceID = _SfpsL4CPCallableDeviceDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 11, 1, 1),
    _SfpsL4CPCallableDeviceDeviceID_Type()
)
sfpsL4CPCallableDeviceDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPCallableDeviceDeviceID.setStatus("mandatory")
_SfpsL4CPCallableDeviceDeviceName_Type = DisplayString
_SfpsL4CPCallableDeviceDeviceName_Object = MibTableColumn
sfpsL4CPCallableDeviceDeviceName = _SfpsL4CPCallableDeviceDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 11, 1, 2),
    _SfpsL4CPCallableDeviceDeviceName_Type()
)
sfpsL4CPCallableDeviceDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPCallableDeviceDeviceName.setStatus("mandatory")
_SfpsL4CPCallableDeviceDefaultUserName_Type = DisplayString
_SfpsL4CPCallableDeviceDefaultUserName_Object = MibTableColumn
sfpsL4CPCallableDeviceDefaultUserName = _SfpsL4CPCallableDeviceDefaultUserName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 11, 1, 3),
    _SfpsL4CPCallableDeviceDefaultUserName_Type()
)
sfpsL4CPCallableDeviceDefaultUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CPCallableDeviceDefaultUserName.setStatus("mandatory")
_SfpsL4CDR_ObjectIdentity = ObjectIdentity
sfpsL4CDR = _SfpsL4CDR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2)
)
_L4cdrStats_ObjectIdentity = ObjectIdentity
l4cdrStats = _L4cdrStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 1)
)
_L4cdrConfig_ObjectIdentity = ObjectIdentity
l4cdrConfig = _L4cdrConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 2)
)
_L4cdrActions_ObjectIdentity = ObjectIdentity
l4cdrActions = _L4cdrActions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 3)
)
_SfpsL4CDRActiveFlowTable_Object = MibTable
sfpsL4CDRActiveFlowTable = _SfpsL4CDRActiveFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 4)
)
if mibBuilder.loadTexts:
    sfpsL4CDRActiveFlowTable.setStatus("mandatory")
_SfpsL4CDRActiveFlowEntry_Object = MibTableRow
sfpsL4CDRActiveFlowEntry = _SfpsL4CDRActiveFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 4, 1)
)
sfpsL4CDRActiveFlowEntry.setIndexNames(
    (0, "CTRON-SFPS-L4SS-MIB", "sfpsL4CDRActiveFlowFlowID"),
)
if mibBuilder.loadTexts:
    sfpsL4CDRActiveFlowEntry.setStatus("mandatory")


class _SfpsL4CDRActiveFlowFlowID_Type(Integer32):
    """Custom type sfpsL4CDRActiveFlowFlowID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SfpsL4CDRActiveFlowFlowID_Type.__name__ = "Integer32"
_SfpsL4CDRActiveFlowFlowID_Object = MibTableColumn
sfpsL4CDRActiveFlowFlowID = _SfpsL4CDRActiveFlowFlowID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 4, 1, 1),
    _SfpsL4CDRActiveFlowFlowID_Type()
)
sfpsL4CDRActiveFlowFlowID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRActiveFlowFlowID.setStatus("mandatory")
_SfpsL4CDRActiveFlowSubProtocol_Type = Integer32
_SfpsL4CDRActiveFlowSubProtocol_Object = MibTableColumn
sfpsL4CDRActiveFlowSubProtocol = _SfpsL4CDRActiveFlowSubProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 4, 1, 2),
    _SfpsL4CDRActiveFlowSubProtocol_Type()
)
sfpsL4CDRActiveFlowSubProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRActiveFlowSubProtocol.setStatus("mandatory")
_SfpsL4CDRActiveFlowEtherType_Type = Integer32
_SfpsL4CDRActiveFlowEtherType_Object = MibTableColumn
sfpsL4CDRActiveFlowEtherType = _SfpsL4CDRActiveFlowEtherType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 4, 1, 3),
    _SfpsL4CDRActiveFlowEtherType_Type()
)
sfpsL4CDRActiveFlowEtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRActiveFlowEtherType.setStatus("mandatory")
_SfpsL4CDRActiveFlowSourceUser_Type = DisplayString
_SfpsL4CDRActiveFlowSourceUser_Object = MibTableColumn
sfpsL4CDRActiveFlowSourceUser = _SfpsL4CDRActiveFlowSourceUser_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 4, 1, 4),
    _SfpsL4CDRActiveFlowSourceUser_Type()
)
sfpsL4CDRActiveFlowSourceUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRActiveFlowSourceUser.setStatus("mandatory")
_SfpsL4CDRActiveFlowSourceMACAddr_Type = DisplayString
_SfpsL4CDRActiveFlowSourceMACAddr_Object = MibTableColumn
sfpsL4CDRActiveFlowSourceMACAddr = _SfpsL4CDRActiveFlowSourceMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 4, 1, 5),
    _SfpsL4CDRActiveFlowSourceMACAddr_Type()
)
sfpsL4CDRActiveFlowSourceMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRActiveFlowSourceMACAddr.setStatus("mandatory")
_SfpsL4CDRActiveFlowSourceNetAddr_Type = DisplayString
_SfpsL4CDRActiveFlowSourceNetAddr_Object = MibTableColumn
sfpsL4CDRActiveFlowSourceNetAddr = _SfpsL4CDRActiveFlowSourceNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 4, 1, 6),
    _SfpsL4CDRActiveFlowSourceNetAddr_Type()
)
sfpsL4CDRActiveFlowSourceNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRActiveFlowSourceNetAddr.setStatus("mandatory")
_SfpsL4CDRActiveFlowSourceProtocolPort_Type = Integer32
_SfpsL4CDRActiveFlowSourceProtocolPort_Object = MibTableColumn
sfpsL4CDRActiveFlowSourceProtocolPort = _SfpsL4CDRActiveFlowSourceProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 4, 1, 7),
    _SfpsL4CDRActiveFlowSourceProtocolPort_Type()
)
sfpsL4CDRActiveFlowSourceProtocolPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRActiveFlowSourceProtocolPort.setStatus("mandatory")


class _SfpsL4CDRActiveFlowSourcePPRangeEnabled_Type(Integer32):
    """Custom type sfpsL4CDRActiveFlowSourcePPRangeEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SfpsL4CDRActiveFlowSourcePPRangeEnabled_Type.__name__ = "Integer32"
_SfpsL4CDRActiveFlowSourcePPRangeEnabled_Object = MibTableColumn
sfpsL4CDRActiveFlowSourcePPRangeEnabled = _SfpsL4CDRActiveFlowSourcePPRangeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 4, 1, 8),
    _SfpsL4CDRActiveFlowSourcePPRangeEnabled_Type()
)
sfpsL4CDRActiveFlowSourcePPRangeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRActiveFlowSourcePPRangeEnabled.setStatus("mandatory")
_SfpsL4CDRActiveFlowSourceConnNumber_Type = Integer32
_SfpsL4CDRActiveFlowSourceConnNumber_Object = MibTableColumn
sfpsL4CDRActiveFlowSourceConnNumber = _SfpsL4CDRActiveFlowSourceConnNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 4, 1, 9),
    _SfpsL4CDRActiveFlowSourceConnNumber_Type()
)
sfpsL4CDRActiveFlowSourceConnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRActiveFlowSourceConnNumber.setStatus("mandatory")
_SfpsL4CDRActiveFlowDestUser_Type = DisplayString
_SfpsL4CDRActiveFlowDestUser_Object = MibTableColumn
sfpsL4CDRActiveFlowDestUser = _SfpsL4CDRActiveFlowDestUser_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 4, 1, 10),
    _SfpsL4CDRActiveFlowDestUser_Type()
)
sfpsL4CDRActiveFlowDestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRActiveFlowDestUser.setStatus("mandatory")
_SfpsL4CDRActiveFlowDestMACAddr_Type = DisplayString
_SfpsL4CDRActiveFlowDestMACAddr_Object = MibTableColumn
sfpsL4CDRActiveFlowDestMACAddr = _SfpsL4CDRActiveFlowDestMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 4, 1, 11),
    _SfpsL4CDRActiveFlowDestMACAddr_Type()
)
sfpsL4CDRActiveFlowDestMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRActiveFlowDestMACAddr.setStatus("mandatory")
_SfpsL4CDRActiveFlowDestNetAddr_Type = DisplayString
_SfpsL4CDRActiveFlowDestNetAddr_Object = MibTableColumn
sfpsL4CDRActiveFlowDestNetAddr = _SfpsL4CDRActiveFlowDestNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 4, 1, 12),
    _SfpsL4CDRActiveFlowDestNetAddr_Type()
)
sfpsL4CDRActiveFlowDestNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRActiveFlowDestNetAddr.setStatus("mandatory")
_SfpsL4CDRActiveFlowDestProtocolPort_Type = Integer32
_SfpsL4CDRActiveFlowDestProtocolPort_Object = MibTableColumn
sfpsL4CDRActiveFlowDestProtocolPort = _SfpsL4CDRActiveFlowDestProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 4, 1, 13),
    _SfpsL4CDRActiveFlowDestProtocolPort_Type()
)
sfpsL4CDRActiveFlowDestProtocolPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRActiveFlowDestProtocolPort.setStatus("mandatory")


class _SfpsL4CDRActiveFlowDestPPRangeEnabled_Type(Integer32):
    """Custom type sfpsL4CDRActiveFlowDestPPRangeEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SfpsL4CDRActiveFlowDestPPRangeEnabled_Type.__name__ = "Integer32"
_SfpsL4CDRActiveFlowDestPPRangeEnabled_Object = MibTableColumn
sfpsL4CDRActiveFlowDestPPRangeEnabled = _SfpsL4CDRActiveFlowDestPPRangeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 4, 1, 14),
    _SfpsL4CDRActiveFlowDestPPRangeEnabled_Type()
)
sfpsL4CDRActiveFlowDestPPRangeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRActiveFlowDestPPRangeEnabled.setStatus("mandatory")
_SfpsL4CDRActiveFlowDestConnNumber_Type = Integer32
_SfpsL4CDRActiveFlowDestConnNumber_Object = MibTableColumn
sfpsL4CDRActiveFlowDestConnNumber = _SfpsL4CDRActiveFlowDestConnNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 4, 1, 15),
    _SfpsL4CDRActiveFlowDestConnNumber_Type()
)
sfpsL4CDRActiveFlowDestConnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRActiveFlowDestConnNumber.setStatus("mandatory")
_SfpsL4CDRActiveFlowStartTime_Type = TimeTicks
_SfpsL4CDRActiveFlowStartTime_Object = MibTableColumn
sfpsL4CDRActiveFlowStartTime = _SfpsL4CDRActiveFlowStartTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 4, 1, 16),
    _SfpsL4CDRActiveFlowStartTime_Type()
)
sfpsL4CDRActiveFlowStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRActiveFlowStartTime.setStatus("mandatory")
_SfpsL4CDRActiveFlowLastPktTime_Type = TimeTicks
_SfpsL4CDRActiveFlowLastPktTime_Object = MibTableColumn
sfpsL4CDRActiveFlowLastPktTime = _SfpsL4CDRActiveFlowLastPktTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 4, 1, 17),
    _SfpsL4CDRActiveFlowLastPktTime_Type()
)
sfpsL4CDRActiveFlowLastPktTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRActiveFlowLastPktTime.setStatus("mandatory")
_SfpsL4CDRActiveFlowEndTime_Type = TimeTicks
_SfpsL4CDRActiveFlowEndTime_Object = MibTableColumn
sfpsL4CDRActiveFlowEndTime = _SfpsL4CDRActiveFlowEndTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 4, 1, 18),
    _SfpsL4CDRActiveFlowEndTime_Type()
)
sfpsL4CDRActiveFlowEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRActiveFlowEndTime.setStatus("mandatory")
_SfpsL4CDRActiveFlowInOctets_Type = Counter32
_SfpsL4CDRActiveFlowInOctets_Object = MibTableColumn
sfpsL4CDRActiveFlowInOctets = _SfpsL4CDRActiveFlowInOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 4, 1, 19),
    _SfpsL4CDRActiveFlowInOctets_Type()
)
sfpsL4CDRActiveFlowInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRActiveFlowInOctets.setStatus("mandatory")
_SfpsL4CDRActiveFlowOutOctets_Type = Counter32
_SfpsL4CDRActiveFlowOutOctets_Object = MibTableColumn
sfpsL4CDRActiveFlowOutOctets = _SfpsL4CDRActiveFlowOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 4, 1, 20),
    _SfpsL4CDRActiveFlowOutOctets_Type()
)
sfpsL4CDRActiveFlowOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRActiveFlowOutOctets.setStatus("mandatory")
_SfpsL4CDRActiveFlowInPkts_Type = Counter32
_SfpsL4CDRActiveFlowInPkts_Object = MibTableColumn
sfpsL4CDRActiveFlowInPkts = _SfpsL4CDRActiveFlowInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 4, 1, 21),
    _SfpsL4CDRActiveFlowInPkts_Type()
)
sfpsL4CDRActiveFlowInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRActiveFlowInPkts.setStatus("mandatory")
_SfpsL4CDRActiveFlowOutPkts_Type = Counter32
_SfpsL4CDRActiveFlowOutPkts_Object = MibTableColumn
sfpsL4CDRActiveFlowOutPkts = _SfpsL4CDRActiveFlowOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 4, 1, 22),
    _SfpsL4CDRActiveFlowOutPkts_Type()
)
sfpsL4CDRActiveFlowOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRActiveFlowOutPkts.setStatus("mandatory")


class _SfpsL4CDRActiveFlowDemandAccessConnMade_Type(Integer32):
    """Custom type sfpsL4CDRActiveFlowDemandAccessConnMade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SfpsL4CDRActiveFlowDemandAccessConnMade_Type.__name__ = "Integer32"
_SfpsL4CDRActiveFlowDemandAccessConnMade_Object = MibTableColumn
sfpsL4CDRActiveFlowDemandAccessConnMade = _SfpsL4CDRActiveFlowDemandAccessConnMade_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 4, 1, 23),
    _SfpsL4CDRActiveFlowDemandAccessConnMade_Type()
)
sfpsL4CDRActiveFlowDemandAccessConnMade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRActiveFlowDemandAccessConnMade.setStatus("mandatory")


class _SfpsL4CDRActiveFlowFlowRecordState_Type(Integer32):
    """Custom type sfpsL4CDRActiveFlowFlowRecordState based on Integer32"""
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
        *(("active", 2),
          ("initialized", 1),
          ("invalid", 4),
          ("terminated", 3))
    )


_SfpsL4CDRActiveFlowFlowRecordState_Type.__name__ = "Integer32"
_SfpsL4CDRActiveFlowFlowRecordState_Object = MibTableColumn
sfpsL4CDRActiveFlowFlowRecordState = _SfpsL4CDRActiveFlowFlowRecordState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 4, 1, 24),
    _SfpsL4CDRActiveFlowFlowRecordState_Type()
)
sfpsL4CDRActiveFlowFlowRecordState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRActiveFlowFlowRecordState.setStatus("mandatory")
_SfpsL4CDRTermedFlowTable_Object = MibTable
sfpsL4CDRTermedFlowTable = _SfpsL4CDRTermedFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 5)
)
if mibBuilder.loadTexts:
    sfpsL4CDRTermedFlowTable.setStatus("mandatory")
_SfpsL4CDRTermedFlowEntry_Object = MibTableRow
sfpsL4CDRTermedFlowEntry = _SfpsL4CDRTermedFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 5, 1)
)
sfpsL4CDRTermedFlowEntry.setIndexNames(
    (0, "CTRON-SFPS-L4SS-MIB", "sfpsL4CDRTermedFlowFlowID"),
)
if mibBuilder.loadTexts:
    sfpsL4CDRTermedFlowEntry.setStatus("mandatory")


class _SfpsL4CDRTermedFlowFlowID_Type(Integer32):
    """Custom type sfpsL4CDRTermedFlowFlowID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SfpsL4CDRTermedFlowFlowID_Type.__name__ = "Integer32"
_SfpsL4CDRTermedFlowFlowID_Object = MibTableColumn
sfpsL4CDRTermedFlowFlowID = _SfpsL4CDRTermedFlowFlowID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 5, 1, 1),
    _SfpsL4CDRTermedFlowFlowID_Type()
)
sfpsL4CDRTermedFlowFlowID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRTermedFlowFlowID.setStatus("mandatory")
_SfpsL4CDRTermedFlowSubProtocol_Type = Integer32
_SfpsL4CDRTermedFlowSubProtocol_Object = MibTableColumn
sfpsL4CDRTermedFlowSubProtocol = _SfpsL4CDRTermedFlowSubProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 5, 1, 2),
    _SfpsL4CDRTermedFlowSubProtocol_Type()
)
sfpsL4CDRTermedFlowSubProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRTermedFlowSubProtocol.setStatus("mandatory")
_SfpsL4CDRTermedFlowEtherType_Type = Integer32
_SfpsL4CDRTermedFlowEtherType_Object = MibTableColumn
sfpsL4CDRTermedFlowEtherType = _SfpsL4CDRTermedFlowEtherType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 5, 1, 3),
    _SfpsL4CDRTermedFlowEtherType_Type()
)
sfpsL4CDRTermedFlowEtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRTermedFlowEtherType.setStatus("mandatory")
_SfpsL4CDRTermedFlowSourceUser_Type = DisplayString
_SfpsL4CDRTermedFlowSourceUser_Object = MibTableColumn
sfpsL4CDRTermedFlowSourceUser = _SfpsL4CDRTermedFlowSourceUser_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 5, 1, 4),
    _SfpsL4CDRTermedFlowSourceUser_Type()
)
sfpsL4CDRTermedFlowSourceUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRTermedFlowSourceUser.setStatus("mandatory")
_SfpsL4CDRTermedFlowSourceMACAddr_Type = DisplayString
_SfpsL4CDRTermedFlowSourceMACAddr_Object = MibTableColumn
sfpsL4CDRTermedFlowSourceMACAddr = _SfpsL4CDRTermedFlowSourceMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 5, 1, 5),
    _SfpsL4CDRTermedFlowSourceMACAddr_Type()
)
sfpsL4CDRTermedFlowSourceMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRTermedFlowSourceMACAddr.setStatus("mandatory")
_SfpsL4CDRTermedFlowSourceNetAddr_Type = DisplayString
_SfpsL4CDRTermedFlowSourceNetAddr_Object = MibTableColumn
sfpsL4CDRTermedFlowSourceNetAddr = _SfpsL4CDRTermedFlowSourceNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 5, 1, 6),
    _SfpsL4CDRTermedFlowSourceNetAddr_Type()
)
sfpsL4CDRTermedFlowSourceNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRTermedFlowSourceNetAddr.setStatus("mandatory")
_SfpsL4CDRTermedFlowSourceProtocolPort_Type = Integer32
_SfpsL4CDRTermedFlowSourceProtocolPort_Object = MibTableColumn
sfpsL4CDRTermedFlowSourceProtocolPort = _SfpsL4CDRTermedFlowSourceProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 5, 1, 7),
    _SfpsL4CDRTermedFlowSourceProtocolPort_Type()
)
sfpsL4CDRTermedFlowSourceProtocolPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRTermedFlowSourceProtocolPort.setStatus("mandatory")


class _SfpsL4CDRTermedFlowSourcePPRangeEnabled_Type(Integer32):
    """Custom type sfpsL4CDRTermedFlowSourcePPRangeEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SfpsL4CDRTermedFlowSourcePPRangeEnabled_Type.__name__ = "Integer32"
_SfpsL4CDRTermedFlowSourcePPRangeEnabled_Object = MibTableColumn
sfpsL4CDRTermedFlowSourcePPRangeEnabled = _SfpsL4CDRTermedFlowSourcePPRangeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 5, 1, 8),
    _SfpsL4CDRTermedFlowSourcePPRangeEnabled_Type()
)
sfpsL4CDRTermedFlowSourcePPRangeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRTermedFlowSourcePPRangeEnabled.setStatus("mandatory")
_SfpsL4CDRTermedFlowSourceConnNumber_Type = Integer32
_SfpsL4CDRTermedFlowSourceConnNumber_Object = MibTableColumn
sfpsL4CDRTermedFlowSourceConnNumber = _SfpsL4CDRTermedFlowSourceConnNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 5, 1, 9),
    _SfpsL4CDRTermedFlowSourceConnNumber_Type()
)
sfpsL4CDRTermedFlowSourceConnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRTermedFlowSourceConnNumber.setStatus("mandatory")
_SfpsL4CDRTermedFlowDestUser_Type = DisplayString
_SfpsL4CDRTermedFlowDestUser_Object = MibTableColumn
sfpsL4CDRTermedFlowDestUser = _SfpsL4CDRTermedFlowDestUser_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 5, 1, 10),
    _SfpsL4CDRTermedFlowDestUser_Type()
)
sfpsL4CDRTermedFlowDestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRTermedFlowDestUser.setStatus("mandatory")
_SfpsL4CDRTermedFlowDestMACAddr_Type = DisplayString
_SfpsL4CDRTermedFlowDestMACAddr_Object = MibTableColumn
sfpsL4CDRTermedFlowDestMACAddr = _SfpsL4CDRTermedFlowDestMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 5, 1, 11),
    _SfpsL4CDRTermedFlowDestMACAddr_Type()
)
sfpsL4CDRTermedFlowDestMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRTermedFlowDestMACAddr.setStatus("mandatory")
_SfpsL4CDRTermedFlowDestNetAddr_Type = DisplayString
_SfpsL4CDRTermedFlowDestNetAddr_Object = MibTableColumn
sfpsL4CDRTermedFlowDestNetAddr = _SfpsL4CDRTermedFlowDestNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 5, 1, 12),
    _SfpsL4CDRTermedFlowDestNetAddr_Type()
)
sfpsL4CDRTermedFlowDestNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRTermedFlowDestNetAddr.setStatus("mandatory")
_SfpsL4CDRTermedFlowDestProtocolPort_Type = Integer32
_SfpsL4CDRTermedFlowDestProtocolPort_Object = MibTableColumn
sfpsL4CDRTermedFlowDestProtocolPort = _SfpsL4CDRTermedFlowDestProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 5, 1, 13),
    _SfpsL4CDRTermedFlowDestProtocolPort_Type()
)
sfpsL4CDRTermedFlowDestProtocolPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRTermedFlowDestProtocolPort.setStatus("mandatory")


class _SfpsL4CDRTermedFlowDestPPRangeEnabled_Type(Integer32):
    """Custom type sfpsL4CDRTermedFlowDestPPRangeEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SfpsL4CDRTermedFlowDestPPRangeEnabled_Type.__name__ = "Integer32"
_SfpsL4CDRTermedFlowDestPPRangeEnabled_Object = MibTableColumn
sfpsL4CDRTermedFlowDestPPRangeEnabled = _SfpsL4CDRTermedFlowDestPPRangeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 5, 1, 14),
    _SfpsL4CDRTermedFlowDestPPRangeEnabled_Type()
)
sfpsL4CDRTermedFlowDestPPRangeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRTermedFlowDestPPRangeEnabled.setStatus("mandatory")
_SfpsL4CDRTermedFlowDestConnNumber_Type = Integer32
_SfpsL4CDRTermedFlowDestConnNumber_Object = MibTableColumn
sfpsL4CDRTermedFlowDestConnNumber = _SfpsL4CDRTermedFlowDestConnNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 5, 1, 15),
    _SfpsL4CDRTermedFlowDestConnNumber_Type()
)
sfpsL4CDRTermedFlowDestConnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRTermedFlowDestConnNumber.setStatus("mandatory")
_SfpsL4CDRTermedFlowStartTime_Type = TimeTicks
_SfpsL4CDRTermedFlowStartTime_Object = MibTableColumn
sfpsL4CDRTermedFlowStartTime = _SfpsL4CDRTermedFlowStartTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 5, 1, 16),
    _SfpsL4CDRTermedFlowStartTime_Type()
)
sfpsL4CDRTermedFlowStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRTermedFlowStartTime.setStatus("mandatory")
_SfpsL4CDRTermedFlowLastPktTime_Type = TimeTicks
_SfpsL4CDRTermedFlowLastPktTime_Object = MibTableColumn
sfpsL4CDRTermedFlowLastPktTime = _SfpsL4CDRTermedFlowLastPktTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 5, 1, 17),
    _SfpsL4CDRTermedFlowLastPktTime_Type()
)
sfpsL4CDRTermedFlowLastPktTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRTermedFlowLastPktTime.setStatus("mandatory")
_SfpsL4CDRTermedFlowEndTime_Type = TimeTicks
_SfpsL4CDRTermedFlowEndTime_Object = MibTableColumn
sfpsL4CDRTermedFlowEndTime = _SfpsL4CDRTermedFlowEndTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 5, 1, 18),
    _SfpsL4CDRTermedFlowEndTime_Type()
)
sfpsL4CDRTermedFlowEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRTermedFlowEndTime.setStatus("mandatory")
_SfpsL4CDRTermedFlowInOctets_Type = Counter32
_SfpsL4CDRTermedFlowInOctets_Object = MibTableColumn
sfpsL4CDRTermedFlowInOctets = _SfpsL4CDRTermedFlowInOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 5, 1, 19),
    _SfpsL4CDRTermedFlowInOctets_Type()
)
sfpsL4CDRTermedFlowInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRTermedFlowInOctets.setStatus("mandatory")
_SfpsL4CDRTermedFlowOutOctets_Type = Counter32
_SfpsL4CDRTermedFlowOutOctets_Object = MibTableColumn
sfpsL4CDRTermedFlowOutOctets = _SfpsL4CDRTermedFlowOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 5, 1, 20),
    _SfpsL4CDRTermedFlowOutOctets_Type()
)
sfpsL4CDRTermedFlowOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRTermedFlowOutOctets.setStatus("mandatory")
_SfpsL4CDRTermedFlowInPkts_Type = Counter32
_SfpsL4CDRTermedFlowInPkts_Object = MibTableColumn
sfpsL4CDRTermedFlowInPkts = _SfpsL4CDRTermedFlowInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 5, 1, 21),
    _SfpsL4CDRTermedFlowInPkts_Type()
)
sfpsL4CDRTermedFlowInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRTermedFlowInPkts.setStatus("mandatory")
_SfpsL4CDRTermedFlowOutPkts_Type = Counter32
_SfpsL4CDRTermedFlowOutPkts_Object = MibTableColumn
sfpsL4CDRTermedFlowOutPkts = _SfpsL4CDRTermedFlowOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 5, 1, 22),
    _SfpsL4CDRTermedFlowOutPkts_Type()
)
sfpsL4CDRTermedFlowOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRTermedFlowOutPkts.setStatus("mandatory")


class _SfpsL4CDRTermedFlowDemandAccessConnMade_Type(Integer32):
    """Custom type sfpsL4CDRTermedFlowDemandAccessConnMade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SfpsL4CDRTermedFlowDemandAccessConnMade_Type.__name__ = "Integer32"
_SfpsL4CDRTermedFlowDemandAccessConnMade_Object = MibTableColumn
sfpsL4CDRTermedFlowDemandAccessConnMade = _SfpsL4CDRTermedFlowDemandAccessConnMade_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 5, 1, 23),
    _SfpsL4CDRTermedFlowDemandAccessConnMade_Type()
)
sfpsL4CDRTermedFlowDemandAccessConnMade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRTermedFlowDemandAccessConnMade.setStatus("mandatory")


class _SfpsL4CDRTermedFlowFlowRecordState_Type(Integer32):
    """Custom type sfpsL4CDRTermedFlowFlowRecordState based on Integer32"""
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
        *(("active", 2),
          ("initialized", 1),
          ("invalid", 4),
          ("terminated", 3))
    )


_SfpsL4CDRTermedFlowFlowRecordState_Type.__name__ = "Integer32"
_SfpsL4CDRTermedFlowFlowRecordState_Object = MibTableColumn
sfpsL4CDRTermedFlowFlowRecordState = _SfpsL4CDRTermedFlowFlowRecordState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 5, 1, 24),
    _SfpsL4CDRTermedFlowFlowRecordState_Type()
)
sfpsL4CDRTermedFlowFlowRecordState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRTermedFlowFlowRecordState.setStatus("mandatory")
_SfpsL4CDRFlowIndexTable_Object = MibTable
sfpsL4CDRFlowIndexTable = _SfpsL4CDRFlowIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 6)
)
if mibBuilder.loadTexts:
    sfpsL4CDRFlowIndexTable.setStatus("mandatory")
_SfpsL4CDRFlowIndexEntry_Object = MibTableRow
sfpsL4CDRFlowIndexEntry = _SfpsL4CDRFlowIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 6, 1)
)
sfpsL4CDRFlowIndexEntry.setIndexNames(
    (0, "CTRON-SFPS-L4SS-MIB", "sfpsL4CDRFlowIndexFlowID"),
)
if mibBuilder.loadTexts:
    sfpsL4CDRFlowIndexEntry.setStatus("mandatory")


class _SfpsL4CDRFlowIndexFlowID_Type(Integer32):
    """Custom type sfpsL4CDRFlowIndexFlowID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SfpsL4CDRFlowIndexFlowID_Type.__name__ = "Integer32"
_SfpsL4CDRFlowIndexFlowID_Object = MibTableColumn
sfpsL4CDRFlowIndexFlowID = _SfpsL4CDRFlowIndexFlowID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 6, 1, 1),
    _SfpsL4CDRFlowIndexFlowID_Type()
)
sfpsL4CDRFlowIndexFlowID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRFlowIndexFlowID.setStatus("mandatory")
_SfpsL4CDRFlowIndexSFPSFlowTblIndex_Type = Integer32
_SfpsL4CDRFlowIndexSFPSFlowTblIndex_Object = MibTableColumn
sfpsL4CDRFlowIndexSFPSFlowTblIndex = _SfpsL4CDRFlowIndexSFPSFlowTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 6, 1, 2),
    _SfpsL4CDRFlowIndexSFPSFlowTblIndex_Type()
)
sfpsL4CDRFlowIndexSFPSFlowTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRFlowIndexSFPSFlowTblIndex.setStatus("mandatory")
_SfpsL4CDRFlowIndexSFlowStatsPtr_Type = Integer32
_SfpsL4CDRFlowIndexSFlowStatsPtr_Object = MibTableColumn
sfpsL4CDRFlowIndexSFlowStatsPtr = _SfpsL4CDRFlowIndexSFlowStatsPtr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 6, 1, 3),
    _SfpsL4CDRFlowIndexSFlowStatsPtr_Type()
)
sfpsL4CDRFlowIndexSFlowStatsPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRFlowIndexSFlowStatsPtr.setStatus("mandatory")
_SfpsL4CDRFlowIndexStaticFlowInfoPtr_Type = Integer32
_SfpsL4CDRFlowIndexStaticFlowInfoPtr_Object = MibTableColumn
sfpsL4CDRFlowIndexStaticFlowInfoPtr = _SfpsL4CDRFlowIndexStaticFlowInfoPtr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 6, 1, 4),
    _SfpsL4CDRFlowIndexStaticFlowInfoPtr_Type()
)
sfpsL4CDRFlowIndexStaticFlowInfoPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRFlowIndexStaticFlowInfoPtr.setStatus("mandatory")
_SfpsL4CDRFlowIndexFlowTblEntryPtr_Type = Integer32
_SfpsL4CDRFlowIndexFlowTblEntryPtr_Object = MibTableColumn
sfpsL4CDRFlowIndexFlowTblEntryPtr = _SfpsL4CDRFlowIndexFlowTblEntryPtr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 6, 1, 5),
    _SfpsL4CDRFlowIndexFlowTblEntryPtr_Type()
)
sfpsL4CDRFlowIndexFlowTblEntryPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRFlowIndexFlowTblEntryPtr.setStatus("mandatory")


class _SfpsL4CDRFlowIndexFlowState_Type(Integer32):
    """Custom type sfpsL4CDRFlowIndexFlowState based on Integer32"""
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
        *(("active", 2),
          ("initialized", 1),
          ("invalid", 4),
          ("terminated", 3))
    )


_SfpsL4CDRFlowIndexFlowState_Type.__name__ = "Integer32"
_SfpsL4CDRFlowIndexFlowState_Object = MibTableColumn
sfpsL4CDRFlowIndexFlowState = _SfpsL4CDRFlowIndexFlowState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 2, 6, 1, 6),
    _SfpsL4CDRFlowIndexFlowState_Type()
)
sfpsL4CDRFlowIndexFlowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsL4CDRFlowIndexFlowState.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFPS-L4SS-MIB",
    **{"HexInteger": HexInteger,
       "SfpsAddress": SfpsAddress,
       "sfpsL4SS": sfpsL4SS,
       "sfpsL4CP": sfpsL4CP,
       "l4cpStats": l4cpStats,
       "l4cpConfig": l4cpConfig,
       "sfpsL4CPDisableTCPAckCheck": sfpsL4CPDisableTCPAckCheck,
       "l4cpActions": l4cpActions,
       "sfpsL4CPFlowTable": sfpsL4CPFlowTable,
       "sfpsL4CPFlowEntry": sfpsL4CPFlowEntry,
       "sfpsL4CPFlowCnxIndex": sfpsL4CPFlowCnxIndex,
       "sfpsL4CPFlowSecL3Address": sfpsL4CPFlowSecL3Address,
       "sfpsL4CPFlowPrimL3Address": sfpsL4CPFlowPrimL3Address,
       "sfpsL4CPFlowSubprotocol": sfpsL4CPFlowSubprotocol,
       "sfpsL4CPFlowSecMatchAnyDyn": sfpsL4CPFlowSecMatchAnyDyn,
       "sfpsL4CPFlowPrimMatchAnyDyn": sfpsL4CPFlowPrimMatchAnyDyn,
       "sfpsL4CPFlowSecProtPort": sfpsL4CPFlowSecProtPort,
       "sfpsL4CPFlowPrimProtPort": sfpsL4CPFlowPrimProtPort,
       "sfpsL4CPFlowSecSubstApplies": sfpsL4CPFlowSecSubstApplies,
       "sfpsL4CPFlowPrimSubstApplies": sfpsL4CPFlowPrimSubstApplies,
       "sfpsL4CPFlowSecInPkts": sfpsL4CPFlowSecInPkts,
       "sfpsL4CPFlowSecInOctets": sfpsL4CPFlowSecInOctets,
       "sfpsL4CPFlowPrimInPkts": sfpsL4CPFlowPrimInPkts,
       "sfpsL4CPFlowPrimInOctets": sfpsL4CPFlowPrimInOctets,
       "sfpsL4CPFlowFlowAge": sfpsL4CPFlowFlowAge,
       "sfpsL4CPFlowFlowLastUse": sfpsL4CPFlowFlowLastUse,
       "sfpsL4CPFlowID": sfpsL4CPFlowID,
       "sfpsL4CPMACAddrSubTable": sfpsL4CPMACAddrSubTable,
       "sfpsL4CPMACAddrSubEntry": sfpsL4CPMACAddrSubEntry,
       "sfpsL4CPMACAddrSubDestIP": sfpsL4CPMACAddrSubDestIP,
       "sfpsL4CPMACAddrSubNextHopMAC": sfpsL4CPMACAddrSubNextHopMAC,
       "sfpsL4CPMACAddrSubRefCount": sfpsL4CPMACAddrSubRefCount,
       "sfpsL4CPNetAddrUserTable": sfpsL4CPNetAddrUserTable,
       "sfpsL4CPNetAddrUserEntry": sfpsL4CPNetAddrUserEntry,
       "sfpsL4CPNetAddrUserProtocol": sfpsL4CPNetAddrUserProtocol,
       "sfpsL4CPNetAddrUserNetAddr": sfpsL4CPNetAddrUserNetAddr,
       "sfpsL4CPNetAddrUserLoginID": sfpsL4CPNetAddrUserLoginID,
       "sfpsL4CPNetAddrUserUserID": sfpsL4CPNetAddrUserUserID,
       "sfpsL4CPNetAddrUserUserName": sfpsL4CPNetAddrUserUserName,
       "sfpsL4CPIPRouteTable": sfpsL4CPIPRouteTable,
       "sfpsL4CPIPRouteEntry": sfpsL4CPIPRouteEntry,
       "sfpsL4CPIPRouteSubnetMask": sfpsL4CPIPRouteSubnetMask,
       "sfpsL4CPIPRouteSubnet": sfpsL4CPIPRouteSubnet,
       "sfpsL4CPIPRouteRouteID": sfpsL4CPIPRouteRouteID,
       "sfpsL4CPIPRouteRouteSubsystem": sfpsL4CPIPRouteRouteSubsystem,
       "sfpsL4CPIPRouteDeviceID": sfpsL4CPIPRouteDeviceID,
       "sfpsL4CPIPRouteDeviceName": sfpsL4CPIPRouteDeviceName,
       "sfpsL4CPIPRouteMACAddress": sfpsL4CPIPRouteMACAddress,
       "sfpsL4CPIPRouteMetric": sfpsL4CPIPRouteMetric,
       "sfpsL4CPIPRouteCallable": sfpsL4CPIPRouteCallable,
       "sfpsL4CPPortTable": sfpsL4CPPortTable,
       "sfpsL4CPPortEntry": sfpsL4CPPortEntry,
       "sfpsL4CPPortNum": sfpsL4CPPortNum,
       "sfpsL4CPPortID": sfpsL4CPPortID,
       "sfpsL4CPPortApplyPolicyIn": sfpsL4CPPortApplyPolicyIn,
       "sfpsL4CPPortApplyPolicyOut": sfpsL4CPPortApplyPolicyOut,
       "sfpsL4CPPortDefaultUserID": sfpsL4CPPortDefaultUserID,
       "sfpsL4CPPortDefaultUserName": sfpsL4CPPortDefaultUserName,
       "sfpsL4CPCallableDeviceTable": sfpsL4CPCallableDeviceTable,
       "sfpsL4CPCallableDeviceEntry": sfpsL4CPCallableDeviceEntry,
       "sfpsL4CPCallableDeviceDeviceID": sfpsL4CPCallableDeviceDeviceID,
       "sfpsL4CPCallableDeviceDeviceName": sfpsL4CPCallableDeviceDeviceName,
       "sfpsL4CPCallableDeviceDefaultUserName": sfpsL4CPCallableDeviceDefaultUserName,
       "sfpsL4CDR": sfpsL4CDR,
       "l4cdrStats": l4cdrStats,
       "l4cdrConfig": l4cdrConfig,
       "l4cdrActions": l4cdrActions,
       "sfpsL4CDRActiveFlowTable": sfpsL4CDRActiveFlowTable,
       "sfpsL4CDRActiveFlowEntry": sfpsL4CDRActiveFlowEntry,
       "sfpsL4CDRActiveFlowFlowID": sfpsL4CDRActiveFlowFlowID,
       "sfpsL4CDRActiveFlowSubProtocol": sfpsL4CDRActiveFlowSubProtocol,
       "sfpsL4CDRActiveFlowEtherType": sfpsL4CDRActiveFlowEtherType,
       "sfpsL4CDRActiveFlowSourceUser": sfpsL4CDRActiveFlowSourceUser,
       "sfpsL4CDRActiveFlowSourceMACAddr": sfpsL4CDRActiveFlowSourceMACAddr,
       "sfpsL4CDRActiveFlowSourceNetAddr": sfpsL4CDRActiveFlowSourceNetAddr,
       "sfpsL4CDRActiveFlowSourceProtocolPort": sfpsL4CDRActiveFlowSourceProtocolPort,
       "sfpsL4CDRActiveFlowSourcePPRangeEnabled": sfpsL4CDRActiveFlowSourcePPRangeEnabled,
       "sfpsL4CDRActiveFlowSourceConnNumber": sfpsL4CDRActiveFlowSourceConnNumber,
       "sfpsL4CDRActiveFlowDestUser": sfpsL4CDRActiveFlowDestUser,
       "sfpsL4CDRActiveFlowDestMACAddr": sfpsL4CDRActiveFlowDestMACAddr,
       "sfpsL4CDRActiveFlowDestNetAddr": sfpsL4CDRActiveFlowDestNetAddr,
       "sfpsL4CDRActiveFlowDestProtocolPort": sfpsL4CDRActiveFlowDestProtocolPort,
       "sfpsL4CDRActiveFlowDestPPRangeEnabled": sfpsL4CDRActiveFlowDestPPRangeEnabled,
       "sfpsL4CDRActiveFlowDestConnNumber": sfpsL4CDRActiveFlowDestConnNumber,
       "sfpsL4CDRActiveFlowStartTime": sfpsL4CDRActiveFlowStartTime,
       "sfpsL4CDRActiveFlowLastPktTime": sfpsL4CDRActiveFlowLastPktTime,
       "sfpsL4CDRActiveFlowEndTime": sfpsL4CDRActiveFlowEndTime,
       "sfpsL4CDRActiveFlowInOctets": sfpsL4CDRActiveFlowInOctets,
       "sfpsL4CDRActiveFlowOutOctets": sfpsL4CDRActiveFlowOutOctets,
       "sfpsL4CDRActiveFlowInPkts": sfpsL4CDRActiveFlowInPkts,
       "sfpsL4CDRActiveFlowOutPkts": sfpsL4CDRActiveFlowOutPkts,
       "sfpsL4CDRActiveFlowDemandAccessConnMade": sfpsL4CDRActiveFlowDemandAccessConnMade,
       "sfpsL4CDRActiveFlowFlowRecordState": sfpsL4CDRActiveFlowFlowRecordState,
       "sfpsL4CDRTermedFlowTable": sfpsL4CDRTermedFlowTable,
       "sfpsL4CDRTermedFlowEntry": sfpsL4CDRTermedFlowEntry,
       "sfpsL4CDRTermedFlowFlowID": sfpsL4CDRTermedFlowFlowID,
       "sfpsL4CDRTermedFlowSubProtocol": sfpsL4CDRTermedFlowSubProtocol,
       "sfpsL4CDRTermedFlowEtherType": sfpsL4CDRTermedFlowEtherType,
       "sfpsL4CDRTermedFlowSourceUser": sfpsL4CDRTermedFlowSourceUser,
       "sfpsL4CDRTermedFlowSourceMACAddr": sfpsL4CDRTermedFlowSourceMACAddr,
       "sfpsL4CDRTermedFlowSourceNetAddr": sfpsL4CDRTermedFlowSourceNetAddr,
       "sfpsL4CDRTermedFlowSourceProtocolPort": sfpsL4CDRTermedFlowSourceProtocolPort,
       "sfpsL4CDRTermedFlowSourcePPRangeEnabled": sfpsL4CDRTermedFlowSourcePPRangeEnabled,
       "sfpsL4CDRTermedFlowSourceConnNumber": sfpsL4CDRTermedFlowSourceConnNumber,
       "sfpsL4CDRTermedFlowDestUser": sfpsL4CDRTermedFlowDestUser,
       "sfpsL4CDRTermedFlowDestMACAddr": sfpsL4CDRTermedFlowDestMACAddr,
       "sfpsL4CDRTermedFlowDestNetAddr": sfpsL4CDRTermedFlowDestNetAddr,
       "sfpsL4CDRTermedFlowDestProtocolPort": sfpsL4CDRTermedFlowDestProtocolPort,
       "sfpsL4CDRTermedFlowDestPPRangeEnabled": sfpsL4CDRTermedFlowDestPPRangeEnabled,
       "sfpsL4CDRTermedFlowDestConnNumber": sfpsL4CDRTermedFlowDestConnNumber,
       "sfpsL4CDRTermedFlowStartTime": sfpsL4CDRTermedFlowStartTime,
       "sfpsL4CDRTermedFlowLastPktTime": sfpsL4CDRTermedFlowLastPktTime,
       "sfpsL4CDRTermedFlowEndTime": sfpsL4CDRTermedFlowEndTime,
       "sfpsL4CDRTermedFlowInOctets": sfpsL4CDRTermedFlowInOctets,
       "sfpsL4CDRTermedFlowOutOctets": sfpsL4CDRTermedFlowOutOctets,
       "sfpsL4CDRTermedFlowInPkts": sfpsL4CDRTermedFlowInPkts,
       "sfpsL4CDRTermedFlowOutPkts": sfpsL4CDRTermedFlowOutPkts,
       "sfpsL4CDRTermedFlowDemandAccessConnMade": sfpsL4CDRTermedFlowDemandAccessConnMade,
       "sfpsL4CDRTermedFlowFlowRecordState": sfpsL4CDRTermedFlowFlowRecordState,
       "sfpsL4CDRFlowIndexTable": sfpsL4CDRFlowIndexTable,
       "sfpsL4CDRFlowIndexEntry": sfpsL4CDRFlowIndexEntry,
       "sfpsL4CDRFlowIndexFlowID": sfpsL4CDRFlowIndexFlowID,
       "sfpsL4CDRFlowIndexSFPSFlowTblIndex": sfpsL4CDRFlowIndexSFPSFlowTblIndex,
       "sfpsL4CDRFlowIndexSFlowStatsPtr": sfpsL4CDRFlowIndexSFlowStatsPtr,
       "sfpsL4CDRFlowIndexStaticFlowInfoPtr": sfpsL4CDRFlowIndexStaticFlowInfoPtr,
       "sfpsL4CDRFlowIndexFlowTblEntryPtr": sfpsL4CDRFlowIndexFlowTblEntryPtr,
       "sfpsL4CDRFlowIndexFlowState": sfpsL4CDRFlowIndexFlowState}
)
