# SNMP MIB module (Wellfleet-AOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-AOT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:44 2024
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

(wfAsyncOverTcpGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfAsyncOverTcpGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfAot_ObjectIdentity = ObjectIdentity
wfAot = _WfAot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 1)
)


class _WfAotDelete_Type(Integer32):
    """Custom type wfAotDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAotDelete_Type.__name__ = "Integer32"
_WfAotDelete_Object = MibScalar
wfAotDelete = _WfAotDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 1, 1),
    _WfAotDelete_Type()
)
wfAotDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAotDelete.setStatus("mandatory")


class _WfAotDisable_Type(Integer32):
    """Custom type wfAotDisable based on Integer32"""
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


_WfAotDisable_Type.__name__ = "Integer32"
_WfAotDisable_Object = MibScalar
wfAotDisable = _WfAotDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 1, 2),
    _WfAotDisable_Type()
)
wfAotDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAotDisable.setStatus("mandatory")


class _WfAotState_Type(Integer32):
    """Custom type wfAotState based on Integer32"""
    defaultValue = 2

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfAotState_Type.__name__ = "Integer32"
_WfAotState_Object = MibScalar
wfAotState = _WfAotState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 1, 3),
    _WfAotState_Type()
)
wfAotState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAotState.setStatus("mandatory")
_WfAotInterfaceTable_Object = MibTable
wfAotInterfaceTable = _WfAotInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 2)
)
if mibBuilder.loadTexts:
    wfAotInterfaceTable.setStatus("mandatory")
_WfAotInterfaceEntry_Object = MibTableRow
wfAotInterfaceEntry = _WfAotInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 2, 1)
)
wfAotInterfaceEntry.setIndexNames(
    (0, "Wellfleet-AOT-MIB", "wfAotInterfaceSlotNumber"),
    (0, "Wellfleet-AOT-MIB", "wfAotInterfaceCctNumber"),
)
if mibBuilder.loadTexts:
    wfAotInterfaceEntry.setStatus("mandatory")


class _WfAotInterfaceDelete_Type(Integer32):
    """Custom type wfAotInterfaceDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAotInterfaceDelete_Type.__name__ = "Integer32"
_WfAotInterfaceDelete_Object = MibTableColumn
wfAotInterfaceDelete = _WfAotInterfaceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 2, 1, 1),
    _WfAotInterfaceDelete_Type()
)
wfAotInterfaceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAotInterfaceDelete.setStatus("mandatory")


class _WfAotInterfaceDisable_Type(Integer32):
    """Custom type wfAotInterfaceDisable based on Integer32"""
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


_WfAotInterfaceDisable_Type.__name__ = "Integer32"
_WfAotInterfaceDisable_Object = MibTableColumn
wfAotInterfaceDisable = _WfAotInterfaceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 2, 1, 2),
    _WfAotInterfaceDisable_Type()
)
wfAotInterfaceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAotInterfaceDisable.setStatus("mandatory")
_WfAotInterfaceCctNumber_Type = Integer32
_WfAotInterfaceCctNumber_Object = MibTableColumn
wfAotInterfaceCctNumber = _WfAotInterfaceCctNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 2, 1, 3),
    _WfAotInterfaceCctNumber_Type()
)
wfAotInterfaceCctNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAotInterfaceCctNumber.setStatus("mandatory")
_WfAotInterfaceSlotNumber_Type = Integer32
_WfAotInterfaceSlotNumber_Object = MibTableColumn
wfAotInterfaceSlotNumber = _WfAotInterfaceSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 2, 1, 4),
    _WfAotInterfaceSlotNumber_Type()
)
wfAotInterfaceSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAotInterfaceSlotNumber.setStatus("mandatory")


class _WfAotInterfaceState_Type(Integer32):
    """Custom type wfAotInterfaceState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("init", 3),
          ("up", 1))
    )


_WfAotInterfaceState_Type.__name__ = "Integer32"
_WfAotInterfaceState_Object = MibTableColumn
wfAotInterfaceState = _WfAotInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 2, 1, 5),
    _WfAotInterfaceState_Type()
)
wfAotInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAotInterfaceState.setStatus("mandatory")


class _WfAotInterfaceType_Type(Integer32):
    """Custom type wfAotInterfaceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multidrop", 2),
          ("singledrop", 1))
    )


_WfAotInterfaceType_Type.__name__ = "Integer32"
_WfAotInterfaceType_Object = MibTableColumn
wfAotInterfaceType = _WfAotInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 2, 1, 6),
    _WfAotInterfaceType_Type()
)
wfAotInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAotInterfaceType.setStatus("mandatory")


class _WfAotInterfaceAttachedTo_Type(Integer32):
    """Custom type wfAotInterfaceAttachedTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_WfAotInterfaceAttachedTo_Type.__name__ = "Integer32"
_WfAotInterfaceAttachedTo_Object = MibTableColumn
wfAotInterfaceAttachedTo = _WfAotInterfaceAttachedTo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 2, 1, 7),
    _WfAotInterfaceAttachedTo_Type()
)
wfAotInterfaceAttachedTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAotInterfaceAttachedTo.setStatus("mandatory")
_WfAotInterfacePktCnt_Type = Counter32
_WfAotInterfacePktCnt_Object = MibTableColumn
wfAotInterfacePktCnt = _WfAotInterfacePktCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 2, 1, 8),
    _WfAotInterfacePktCnt_Type()
)
wfAotInterfacePktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAotInterfacePktCnt.setStatus("mandatory")


class _WfAotKeepaliveInterval_Type(Integer32):
    """Custom type wfAotKeepaliveInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_WfAotKeepaliveInterval_Type.__name__ = "Integer32"
_WfAotKeepaliveInterval_Object = MibTableColumn
wfAotKeepaliveInterval = _WfAotKeepaliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 2, 1, 9),
    _WfAotKeepaliveInterval_Type()
)
wfAotKeepaliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAotKeepaliveInterval.setStatus("mandatory")


class _WfAotKeepaliveRto_Type(Integer32):
    """Custom type wfAotKeepaliveRto based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_WfAotKeepaliveRto_Type.__name__ = "Integer32"
_WfAotKeepaliveRto_Object = MibTableColumn
wfAotKeepaliveRto = _WfAotKeepaliveRto_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 2, 1, 10),
    _WfAotKeepaliveRto_Type()
)
wfAotKeepaliveRto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAotKeepaliveRto.setStatus("mandatory")


class _WfAotKeepaliveMaxRetry_Type(Integer32):
    """Custom type wfAotKeepaliveMaxRetry based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_WfAotKeepaliveMaxRetry_Type.__name__ = "Integer32"
_WfAotKeepaliveMaxRetry_Object = MibTableColumn
wfAotKeepaliveMaxRetry = _WfAotKeepaliveMaxRetry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 2, 1, 11),
    _WfAotKeepaliveMaxRetry_Type()
)
wfAotKeepaliveMaxRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAotKeepaliveMaxRetry.setStatus("mandatory")
_WfAotPeerTable_Object = MibTable
wfAotPeerTable = _WfAotPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 3)
)
if mibBuilder.loadTexts:
    wfAotPeerTable.setStatus("mandatory")
_WfAotPeerEntry_Object = MibTableRow
wfAotPeerEntry = _WfAotPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 3, 1)
)
wfAotPeerEntry.setIndexNames(
    (0, "Wellfleet-AOT-MIB", "wfAotPeerSlotNumber"),
    (0, "Wellfleet-AOT-MIB", "wfAotPeerCctNumber"),
    (0, "Wellfleet-AOT-MIB", "wfAotPeerRemoteIpAddr"),
    (0, "Wellfleet-AOT-MIB", "wfAotPeerLocalTcpListenPort"),
    (0, "Wellfleet-AOT-MIB", "wfAotPeerRemoteTcpListenPort"),
    (0, "Wellfleet-AOT-MIB", "wfAotConnOriginator"),
)
if mibBuilder.loadTexts:
    wfAotPeerEntry.setStatus("mandatory")


class _WfAotPeerEntryDelete_Type(Integer32):
    """Custom type wfAotPeerEntryDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAotPeerEntryDelete_Type.__name__ = "Integer32"
_WfAotPeerEntryDelete_Object = MibTableColumn
wfAotPeerEntryDelete = _WfAotPeerEntryDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 3, 1, 1),
    _WfAotPeerEntryDelete_Type()
)
wfAotPeerEntryDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAotPeerEntryDelete.setStatus("mandatory")


class _WfAotPeerEntryDisable_Type(Integer32):
    """Custom type wfAotPeerEntryDisable based on Integer32"""
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


_WfAotPeerEntryDisable_Type.__name__ = "Integer32"
_WfAotPeerEntryDisable_Object = MibTableColumn
wfAotPeerEntryDisable = _WfAotPeerEntryDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 3, 1, 2),
    _WfAotPeerEntryDisable_Type()
)
wfAotPeerEntryDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAotPeerEntryDisable.setStatus("mandatory")
_WfAotPeerSlotNumber_Type = Integer32
_WfAotPeerSlotNumber_Object = MibTableColumn
wfAotPeerSlotNumber = _WfAotPeerSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 3, 1, 3),
    _WfAotPeerSlotNumber_Type()
)
wfAotPeerSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAotPeerSlotNumber.setStatus("mandatory")
_WfAotPeerCctNumber_Type = Integer32
_WfAotPeerCctNumber_Object = MibTableColumn
wfAotPeerCctNumber = _WfAotPeerCctNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 3, 1, 4),
    _WfAotPeerCctNumber_Type()
)
wfAotPeerCctNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAotPeerCctNumber.setStatus("mandatory")
_WfAotPeerRemoteIpAddr_Type = IpAddress
_WfAotPeerRemoteIpAddr_Object = MibTableColumn
wfAotPeerRemoteIpAddr = _WfAotPeerRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 3, 1, 5),
    _WfAotPeerRemoteIpAddr_Type()
)
wfAotPeerRemoteIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAotPeerRemoteIpAddr.setStatus("mandatory")


class _WfAotConnOriginator_Type(Integer32):
    """Custom type wfAotConnOriginator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("partner", 2),
          ("self", 1))
    )


_WfAotConnOriginator_Type.__name__ = "Integer32"
_WfAotConnOriginator_Object = MibTableColumn
wfAotConnOriginator = _WfAotConnOriginator_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 3, 1, 6),
    _WfAotConnOriginator_Type()
)
wfAotConnOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAotConnOriginator.setStatus("mandatory")


class _WfAotPeerLocalTcpListenPort_Type(Integer32):
    """Custom type wfAotPeerLocalTcpListenPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 9999),
    )


_WfAotPeerLocalTcpListenPort_Type.__name__ = "Integer32"
_WfAotPeerLocalTcpListenPort_Object = MibTableColumn
wfAotPeerLocalTcpListenPort = _WfAotPeerLocalTcpListenPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 3, 1, 7),
    _WfAotPeerLocalTcpListenPort_Type()
)
wfAotPeerLocalTcpListenPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAotPeerLocalTcpListenPort.setStatus("mandatory")


class _WfAotPeerRemoteTcpListenPort_Type(Integer32):
    """Custom type wfAotPeerRemoteTcpListenPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 9999),
    )


_WfAotPeerRemoteTcpListenPort_Type.__name__ = "Integer32"
_WfAotPeerRemoteTcpListenPort_Object = MibTableColumn
wfAotPeerRemoteTcpListenPort = _WfAotPeerRemoteTcpListenPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 3, 1, 8),
    _WfAotPeerRemoteTcpListenPort_Type()
)
wfAotPeerRemoteTcpListenPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAotPeerRemoteTcpListenPort.setStatus("mandatory")


class _WfAotPeerLocalTcpPort_Type(Integer32):
    """Custom type wfAotPeerLocalTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 9999),
    )


_WfAotPeerLocalTcpPort_Type.__name__ = "Integer32"
_WfAotPeerLocalTcpPort_Object = MibTableColumn
wfAotPeerLocalTcpPort = _WfAotPeerLocalTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 3, 1, 9),
    _WfAotPeerLocalTcpPort_Type()
)
wfAotPeerLocalTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAotPeerLocalTcpPort.setStatus("mandatory")


class _WfAotPeerRemoteTcpPort_Type(Integer32):
    """Custom type wfAotPeerRemoteTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 9999),
    )


_WfAotPeerRemoteTcpPort_Type.__name__ = "Integer32"
_WfAotPeerRemoteTcpPort_Object = MibTableColumn
wfAotPeerRemoteTcpPort = _WfAotPeerRemoteTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 21, 3, 1, 10),
    _WfAotPeerRemoteTcpPort_Type()
)
wfAotPeerRemoteTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAotPeerRemoteTcpPort.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-AOT-MIB",
    **{"wfAot": wfAot,
       "wfAotDelete": wfAotDelete,
       "wfAotDisable": wfAotDisable,
       "wfAotState": wfAotState,
       "wfAotInterfaceTable": wfAotInterfaceTable,
       "wfAotInterfaceEntry": wfAotInterfaceEntry,
       "wfAotInterfaceDelete": wfAotInterfaceDelete,
       "wfAotInterfaceDisable": wfAotInterfaceDisable,
       "wfAotInterfaceCctNumber": wfAotInterfaceCctNumber,
       "wfAotInterfaceSlotNumber": wfAotInterfaceSlotNumber,
       "wfAotInterfaceState": wfAotInterfaceState,
       "wfAotInterfaceType": wfAotInterfaceType,
       "wfAotInterfaceAttachedTo": wfAotInterfaceAttachedTo,
       "wfAotInterfacePktCnt": wfAotInterfacePktCnt,
       "wfAotKeepaliveInterval": wfAotKeepaliveInterval,
       "wfAotKeepaliveRto": wfAotKeepaliveRto,
       "wfAotKeepaliveMaxRetry": wfAotKeepaliveMaxRetry,
       "wfAotPeerTable": wfAotPeerTable,
       "wfAotPeerEntry": wfAotPeerEntry,
       "wfAotPeerEntryDelete": wfAotPeerEntryDelete,
       "wfAotPeerEntryDisable": wfAotPeerEntryDisable,
       "wfAotPeerSlotNumber": wfAotPeerSlotNumber,
       "wfAotPeerCctNumber": wfAotPeerCctNumber,
       "wfAotPeerRemoteIpAddr": wfAotPeerRemoteIpAddr,
       "wfAotConnOriginator": wfAotConnOriginator,
       "wfAotPeerLocalTcpListenPort": wfAotPeerLocalTcpListenPort,
       "wfAotPeerRemoteTcpListenPort": wfAotPeerRemoteTcpListenPort,
       "wfAotPeerLocalTcpPort": wfAotPeerLocalTcpPort,
       "wfAotPeerRemoteTcpPort": wfAotPeerRemoteTcpPort}
)
