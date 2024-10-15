# SNMP MIB module (IPV4INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPV4INTERFACE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:23 2024
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

(apIpv4Interface,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "apIpv4Interface")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

apIpv4InterfaceMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApIpv4InterfaceTable_Object = MibTable
apIpv4InterfaceTable = _ApIpv4InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2)
)
if mibBuilder.loadTexts:
    apIpv4InterfaceTable.setStatus("current")
_ApIpv4InterfaceEntry_Object = MibTableRow
apIpv4InterfaceEntry = _ApIpv4InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1)
)
apIpv4InterfaceEntry.setIndexNames(
    (0, "IPV4INTERFACE-MIB", "apIpv4IfAddress"),
    (0, "IPV4INTERFACE-MIB", "apIpv4IfCircuitIfIndex"),
)
if mibBuilder.loadTexts:
    apIpv4InterfaceEntry.setStatus("current")
_ApIpv4IfAddress_Type = IpAddress
_ApIpv4IfAddress_Object = MibTableColumn
apIpv4IfAddress = _ApIpv4IfAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 1),
    _ApIpv4IfAddress_Type()
)
apIpv4IfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4IfAddress.setStatus("current")
_ApIpv4IfCircuitIfIndex_Type = Integer32
_ApIpv4IfCircuitIfIndex_Object = MibTableColumn
apIpv4IfCircuitIfIndex = _ApIpv4IfCircuitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 2),
    _ApIpv4IfCircuitIfIndex_Type()
)
apIpv4IfCircuitIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4IfCircuitIfIndex.setStatus("current")


class _ApIpv4IfNetPrefixLen_Type(Integer32):
    """Custom type apIpv4IfNetPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 31),
    )


_ApIpv4IfNetPrefixLen_Type.__name__ = "Integer32"
_ApIpv4IfNetPrefixLen_Object = MibTableColumn
apIpv4IfNetPrefixLen = _ApIpv4IfNetPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 3),
    _ApIpv4IfNetPrefixLen_Type()
)
apIpv4IfNetPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4IfNetPrefixLen.setStatus("current")


class _ApIpv4IfDisable_Type(Integer32):
    """Custom type apIpv4IfDisable based on Integer32"""
    defaultValue = 1

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


_ApIpv4IfDisable_Type.__name__ = "Integer32"
_ApIpv4IfDisable_Object = MibTableColumn
apIpv4IfDisable = _ApIpv4IfDisable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 4),
    _ApIpv4IfDisable_Type()
)
apIpv4IfDisable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4IfDisable.setStatus("current")


class _ApIpv4IfState_Type(Integer32):
    """Custom type apIpv4IfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("disabled", 2),
          ("noCircuit", 3))
    )


_ApIpv4IfState_Type.__name__ = "Integer32"
_ApIpv4IfState_Object = MibTableColumn
apIpv4IfState = _ApIpv4IfState_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 5),
    _ApIpv4IfState_Type()
)
apIpv4IfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4IfState.setStatus("current")


class _ApIpv4IfBroadcastIpAddress_Type(IpAddress):
    """Custom type apIpv4IfBroadcastIpAddress based on IpAddress"""
    defaultValue = 0


_ApIpv4IfBroadcastIpAddress_Object = MibTableColumn
apIpv4IfBroadcastIpAddress = _ApIpv4IfBroadcastIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 6),
    _ApIpv4IfBroadcastIpAddress_Type()
)
apIpv4IfBroadcastIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4IfBroadcastIpAddress.setStatus("current")


class _ApIpv4IfRedirects_Type(Integer32):
    """Custom type apIpv4IfRedirects based on Integer32"""
    defaultValue = 1

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


_ApIpv4IfRedirects_Type.__name__ = "Integer32"
_ApIpv4IfRedirects_Object = MibTableColumn
apIpv4IfRedirects = _ApIpv4IfRedirects_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 7),
    _ApIpv4IfRedirects_Type()
)
apIpv4IfRedirects.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4IfRedirects.setStatus("current")


class _ApIpv4IfUnreachables_Type(Integer32):
    """Custom type apIpv4IfUnreachables based on Integer32"""
    defaultValue = 1

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


_ApIpv4IfUnreachables_Type.__name__ = "Integer32"
_ApIpv4IfUnreachables_Object = MibTableColumn
apIpv4IfUnreachables = _ApIpv4IfUnreachables_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 8),
    _ApIpv4IfUnreachables_Type()
)
apIpv4IfUnreachables.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4IfUnreachables.setStatus("current")


class _ApIpv4IfIrdp_Type(Integer32):
    """Custom type apIpv4IfIrdp based on Integer32"""
    defaultValue = 2

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


_ApIpv4IfIrdp_Type.__name__ = "Integer32"
_ApIpv4IfIrdp_Object = MibTableColumn
apIpv4IfIrdp = _ApIpv4IfIrdp_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 9),
    _ApIpv4IfIrdp_Type()
)
apIpv4IfIrdp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4IfIrdp.setStatus("current")


class _ApIpv4IfIrdpUseMulticast_Type(Integer32):
    """Custom type apIpv4IfIrdpUseMulticast based on Integer32"""
    defaultValue = 2

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


_ApIpv4IfIrdpUseMulticast_Type.__name__ = "Integer32"
_ApIpv4IfIrdpUseMulticast_Object = MibTableColumn
apIpv4IfIrdpUseMulticast = _ApIpv4IfIrdpUseMulticast_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 10),
    _ApIpv4IfIrdpUseMulticast_Type()
)
apIpv4IfIrdpUseMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4IfIrdpUseMulticast.setStatus("obsolete")


class _ApIpv4IfIrdpMax_Type(Integer32):
    """Custom type apIpv4IfIrdpMax based on Integer32"""
    defaultValue = 600


_ApIpv4IfIrdpMax_Object = MibTableColumn
apIpv4IfIrdpMax = _ApIpv4IfIrdpMax_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 11),
    _ApIpv4IfIrdpMax_Type()
)
apIpv4IfIrdpMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4IfIrdpMax.setStatus("obsolete")


class _ApIpv4IfIrdpMin_Type(Integer32):
    """Custom type apIpv4IfIrdpMin based on Integer32"""
    defaultValue = 0


_ApIpv4IfIrdpMin_Object = MibTableColumn
apIpv4IfIrdpMin = _ApIpv4IfIrdpMin_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 12),
    _ApIpv4IfIrdpMin_Type()
)
apIpv4IfIrdpMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4IfIrdpMin.setStatus("obsolete")


class _ApIpv4IfIrdpPref_Type(Integer32):
    """Custom type apIpv4IfIrdpPref based on Integer32"""
    defaultValue = 0


_ApIpv4IfIrdpPref_Object = MibTableColumn
apIpv4IfIrdpPref = _ApIpv4IfIrdpPref_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 13),
    _ApIpv4IfIrdpPref_Type()
)
apIpv4IfIrdpPref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4IfIrdpPref.setStatus("current")
_ApIpv4IfStatus_Type = RowStatus
_ApIpv4IfStatus_Object = MibTableColumn
apIpv4IfStatus = _ApIpv4IfStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 14),
    _ApIpv4IfStatus_Type()
)
apIpv4IfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4IfStatus.setStatus("current")


class _ApIpv4IfRunRedundancyProto_Type(TruthValue):
    """Custom type apIpv4IfRunRedundancyProto based on TruthValue"""


_ApIpv4IfRunRedundancyProto_Object = MibTableColumn
apIpv4IfRunRedundancyProto = _ApIpv4IfRunRedundancyProto_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 2, 2, 1, 15),
    _ApIpv4IfRunRedundancyProto_Type()
)
apIpv4IfRunRedundancyProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4IfRunRedundancyProto.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPV4INTERFACE-MIB",
    **{"apIpv4InterfaceMib": apIpv4InterfaceMib,
       "apIpv4InterfaceTable": apIpv4InterfaceTable,
       "apIpv4InterfaceEntry": apIpv4InterfaceEntry,
       "apIpv4IfAddress": apIpv4IfAddress,
       "apIpv4IfCircuitIfIndex": apIpv4IfCircuitIfIndex,
       "apIpv4IfNetPrefixLen": apIpv4IfNetPrefixLen,
       "apIpv4IfDisable": apIpv4IfDisable,
       "apIpv4IfState": apIpv4IfState,
       "apIpv4IfBroadcastIpAddress": apIpv4IfBroadcastIpAddress,
       "apIpv4IfRedirects": apIpv4IfRedirects,
       "apIpv4IfUnreachables": apIpv4IfUnreachables,
       "apIpv4IfIrdp": apIpv4IfIrdp,
       "apIpv4IfIrdpUseMulticast": apIpv4IfIrdpUseMulticast,
       "apIpv4IfIrdpMax": apIpv4IfIrdpMax,
       "apIpv4IfIrdpMin": apIpv4IfIrdpMin,
       "apIpv4IfIrdpPref": apIpv4IfIrdpPref,
       "apIpv4IfStatus": apIpv4IfStatus,
       "apIpv4IfRunRedundancyProto": apIpv4IfRunRedundancyProto}
)
