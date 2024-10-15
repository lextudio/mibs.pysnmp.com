# SNMP MIB module (Wellfleet-BOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-BOT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:53 2024
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

(wfBotGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfBotGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfBot_ObjectIdentity = ObjectIdentity
wfBot = _WfBot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 1)
)


class _WfBotDelete_Type(Integer32):
    """Custom type wfBotDelete based on Integer32"""
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


_WfBotDelete_Type.__name__ = "Integer32"
_WfBotDelete_Object = MibScalar
wfBotDelete = _WfBotDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 1, 1),
    _WfBotDelete_Type()
)
wfBotDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBotDelete.setStatus("mandatory")


class _WfBotDisable_Type(Integer32):
    """Custom type wfBotDisable based on Integer32"""
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


_WfBotDisable_Type.__name__ = "Integer32"
_WfBotDisable_Object = MibScalar
wfBotDisable = _WfBotDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 1, 2),
    _WfBotDisable_Type()
)
wfBotDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBotDisable.setStatus("mandatory")


class _WfBotState_Type(Integer32):
    """Custom type wfBotState based on Integer32"""
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


_WfBotState_Type.__name__ = "Integer32"
_WfBotState_Object = MibScalar
wfBotState = _WfBotState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 1, 3),
    _WfBotState_Type()
)
wfBotState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBotState.setStatus("mandatory")
_WfBotInterfaceTable_Object = MibTable
wfBotInterfaceTable = _WfBotInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2)
)
if mibBuilder.loadTexts:
    wfBotInterfaceTable.setStatus("mandatory")
_WfBotInterfaceEntry_Object = MibTableRow
wfBotInterfaceEntry = _WfBotInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1)
)
wfBotInterfaceEntry.setIndexNames(
    (0, "Wellfleet-BOT-MIB", "wfBotInterfaceSlotNumber"),
    (0, "Wellfleet-BOT-MIB", "wfBotInterfaceCctNumber"),
)
if mibBuilder.loadTexts:
    wfBotInterfaceEntry.setStatus("mandatory")


class _WfBotInterfaceDelete_Type(Integer32):
    """Custom type wfBotInterfaceDelete based on Integer32"""
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


_WfBotInterfaceDelete_Type.__name__ = "Integer32"
_WfBotInterfaceDelete_Object = MibTableColumn
wfBotInterfaceDelete = _WfBotInterfaceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 1),
    _WfBotInterfaceDelete_Type()
)
wfBotInterfaceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBotInterfaceDelete.setStatus("mandatory")


class _WfBotInterfaceDisable_Type(Integer32):
    """Custom type wfBotInterfaceDisable based on Integer32"""
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


_WfBotInterfaceDisable_Type.__name__ = "Integer32"
_WfBotInterfaceDisable_Object = MibTableColumn
wfBotInterfaceDisable = _WfBotInterfaceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 2),
    _WfBotInterfaceDisable_Type()
)
wfBotInterfaceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBotInterfaceDisable.setStatus("mandatory")
_WfBotInterfaceCctNumber_Type = Integer32
_WfBotInterfaceCctNumber_Object = MibTableColumn
wfBotInterfaceCctNumber = _WfBotInterfaceCctNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 3),
    _WfBotInterfaceCctNumber_Type()
)
wfBotInterfaceCctNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBotInterfaceCctNumber.setStatus("mandatory")
_WfBotInterfaceSlotNumber_Type = Integer32
_WfBotInterfaceSlotNumber_Object = MibTableColumn
wfBotInterfaceSlotNumber = _WfBotInterfaceSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 4),
    _WfBotInterfaceSlotNumber_Type()
)
wfBotInterfaceSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBotInterfaceSlotNumber.setStatus("mandatory")


class _WfBotInterfaceState_Type(Integer32):
    """Custom type wfBotInterfaceState based on Integer32"""
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


_WfBotInterfaceState_Type.__name__ = "Integer32"
_WfBotInterfaceState_Object = MibTableColumn
wfBotInterfaceState = _WfBotInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 5),
    _WfBotInterfaceState_Type()
)
wfBotInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBotInterfaceState.setStatus("mandatory")


class _WfBotInterfaceType_Type(Integer32):
    """Custom type wfBotInterfaceType based on Integer32"""
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


_WfBotInterfaceType_Type.__name__ = "Integer32"
_WfBotInterfaceType_Object = MibTableColumn
wfBotInterfaceType = _WfBotInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 6),
    _WfBotInterfaceType_Type()
)
wfBotInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBotInterfaceType.setStatus("mandatory")


class _WfBotInterfaceAttachedTo_Type(Integer32):
    """Custom type wfBotInterfaceAttachedTo based on Integer32"""
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


_WfBotInterfaceAttachedTo_Type.__name__ = "Integer32"
_WfBotInterfaceAttachedTo_Object = MibTableColumn
wfBotInterfaceAttachedTo = _WfBotInterfaceAttachedTo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 7),
    _WfBotInterfaceAttachedTo_Type()
)
wfBotInterfaceAttachedTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBotInterfaceAttachedTo.setStatus("mandatory")
_WfBotInterfacePktCnt_Type = Counter32
_WfBotInterfacePktCnt_Object = MibTableColumn
wfBotInterfacePktCnt = _WfBotInterfacePktCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 8),
    _WfBotInterfacePktCnt_Type()
)
wfBotInterfacePktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBotInterfacePktCnt.setStatus("mandatory")


class _WfBotKeepaliveInterval_Type(Integer32):
    """Custom type wfBotKeepaliveInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_WfBotKeepaliveInterval_Type.__name__ = "Integer32"
_WfBotKeepaliveInterval_Object = MibTableColumn
wfBotKeepaliveInterval = _WfBotKeepaliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 9),
    _WfBotKeepaliveInterval_Type()
)
wfBotKeepaliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBotKeepaliveInterval.setStatus("mandatory")


class _WfBotKeepaliveRto_Type(Integer32):
    """Custom type wfBotKeepaliveRto based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_WfBotKeepaliveRto_Type.__name__ = "Integer32"
_WfBotKeepaliveRto_Object = MibTableColumn
wfBotKeepaliveRto = _WfBotKeepaliveRto_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 10),
    _WfBotKeepaliveRto_Type()
)
wfBotKeepaliveRto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBotKeepaliveRto.setStatus("mandatory")


class _WfBotKeepaliveMaxRetry_Type(Integer32):
    """Custom type wfBotKeepaliveMaxRetry based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_WfBotKeepaliveMaxRetry_Type.__name__ = "Integer32"
_WfBotKeepaliveMaxRetry_Object = MibTableColumn
wfBotKeepaliveMaxRetry = _WfBotKeepaliveMaxRetry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 2, 1, 11),
    _WfBotKeepaliveMaxRetry_Type()
)
wfBotKeepaliveMaxRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBotKeepaliveMaxRetry.setStatus("mandatory")
_WfBotPeerTable_Object = MibTable
wfBotPeerTable = _WfBotPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3)
)
if mibBuilder.loadTexts:
    wfBotPeerTable.setStatus("mandatory")
_WfBotPeerEntry_Object = MibTableRow
wfBotPeerEntry = _WfBotPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1)
)
wfBotPeerEntry.setIndexNames(
    (0, "Wellfleet-BOT-MIB", "wfBotPeerSlotNumber"),
    (0, "Wellfleet-BOT-MIB", "wfBotPeerCctNumber"),
    (0, "Wellfleet-BOT-MIB", "wfBotPeerRemoteIpAddr"),
    (0, "Wellfleet-BOT-MIB", "wfBotPeerLocalTcpListenPort"),
    (0, "Wellfleet-BOT-MIB", "wfBotPeerRemoteTcpListenPort"),
    (0, "Wellfleet-BOT-MIB", "wfBotConnOriginator"),
)
if mibBuilder.loadTexts:
    wfBotPeerEntry.setStatus("mandatory")


class _WfBotPeerEntryDelete_Type(Integer32):
    """Custom type wfBotPeerEntryDelete based on Integer32"""
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


_WfBotPeerEntryDelete_Type.__name__ = "Integer32"
_WfBotPeerEntryDelete_Object = MibTableColumn
wfBotPeerEntryDelete = _WfBotPeerEntryDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 1),
    _WfBotPeerEntryDelete_Type()
)
wfBotPeerEntryDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBotPeerEntryDelete.setStatus("mandatory")


class _WfBotPeerEntryDisable_Type(Integer32):
    """Custom type wfBotPeerEntryDisable based on Integer32"""
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


_WfBotPeerEntryDisable_Type.__name__ = "Integer32"
_WfBotPeerEntryDisable_Object = MibTableColumn
wfBotPeerEntryDisable = _WfBotPeerEntryDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 2),
    _WfBotPeerEntryDisable_Type()
)
wfBotPeerEntryDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBotPeerEntryDisable.setStatus("mandatory")
_WfBotPeerSlotNumber_Type = Integer32
_WfBotPeerSlotNumber_Object = MibTableColumn
wfBotPeerSlotNumber = _WfBotPeerSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 3),
    _WfBotPeerSlotNumber_Type()
)
wfBotPeerSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBotPeerSlotNumber.setStatus("mandatory")
_WfBotPeerCctNumber_Type = Integer32
_WfBotPeerCctNumber_Object = MibTableColumn
wfBotPeerCctNumber = _WfBotPeerCctNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 4),
    _WfBotPeerCctNumber_Type()
)
wfBotPeerCctNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBotPeerCctNumber.setStatus("mandatory")
_WfBotPeerRemoteIpAddr_Type = IpAddress
_WfBotPeerRemoteIpAddr_Object = MibTableColumn
wfBotPeerRemoteIpAddr = _WfBotPeerRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 5),
    _WfBotPeerRemoteIpAddr_Type()
)
wfBotPeerRemoteIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBotPeerRemoteIpAddr.setStatus("mandatory")


class _WfBotConnOriginator_Type(Integer32):
    """Custom type wfBotConnOriginator based on Integer32"""
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


_WfBotConnOriginator_Type.__name__ = "Integer32"
_WfBotConnOriginator_Object = MibTableColumn
wfBotConnOriginator = _WfBotConnOriginator_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 6),
    _WfBotConnOriginator_Type()
)
wfBotConnOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBotConnOriginator.setStatus("mandatory")


class _WfBotPeerLocalTcpListenPort_Type(Integer32):
    """Custom type wfBotPeerLocalTcpListenPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 9999),
    )


_WfBotPeerLocalTcpListenPort_Type.__name__ = "Integer32"
_WfBotPeerLocalTcpListenPort_Object = MibTableColumn
wfBotPeerLocalTcpListenPort = _WfBotPeerLocalTcpListenPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 7),
    _WfBotPeerLocalTcpListenPort_Type()
)
wfBotPeerLocalTcpListenPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBotPeerLocalTcpListenPort.setStatus("mandatory")


class _WfBotPeerRemoteTcpListenPort_Type(Integer32):
    """Custom type wfBotPeerRemoteTcpListenPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 9999),
    )


_WfBotPeerRemoteTcpListenPort_Type.__name__ = "Integer32"
_WfBotPeerRemoteTcpListenPort_Object = MibTableColumn
wfBotPeerRemoteTcpListenPort = _WfBotPeerRemoteTcpListenPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 8),
    _WfBotPeerRemoteTcpListenPort_Type()
)
wfBotPeerRemoteTcpListenPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBotPeerRemoteTcpListenPort.setStatus("mandatory")


class _WfBotPeerLocalTcpPort_Type(Integer32):
    """Custom type wfBotPeerLocalTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 9999),
    )


_WfBotPeerLocalTcpPort_Type.__name__ = "Integer32"
_WfBotPeerLocalTcpPort_Object = MibTableColumn
wfBotPeerLocalTcpPort = _WfBotPeerLocalTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 9),
    _WfBotPeerLocalTcpPort_Type()
)
wfBotPeerLocalTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBotPeerLocalTcpPort.setStatus("mandatory")


class _WfBotPeerRemoteTcpPort_Type(Integer32):
    """Custom type wfBotPeerRemoteTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 9999),
    )


_WfBotPeerRemoteTcpPort_Type.__name__ = "Integer32"
_WfBotPeerRemoteTcpPort_Object = MibTableColumn
wfBotPeerRemoteTcpPort = _WfBotPeerRemoteTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 3, 1, 10),
    _WfBotPeerRemoteTcpPort_Type()
)
wfBotPeerRemoteTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBotPeerRemoteTcpPort.setStatus("mandatory")
_WfBotCUTable_Object = MibTable
wfBotCUTable = _WfBotCUTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4)
)
if mibBuilder.loadTexts:
    wfBotCUTable.setStatus("mandatory")
_WfBotCUEntry_Object = MibTableRow
wfBotCUEntry = _WfBotCUEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4, 1)
)
wfBotCUEntry.setIndexNames(
    (0, "Wellfleet-BOT-MIB", "wfBotCUSlotNumber"),
    (0, "Wellfleet-BOT-MIB", "wfBotCUCctNumber"),
    (0, "Wellfleet-BOT-MIB", "wfBotCURemoteIpAddr"),
    (0, "Wellfleet-BOT-MIB", "wfBotCULocalTcpListenPort"),
    (0, "Wellfleet-BOT-MIB", "wfBotCURemoteTcpListenPort"),
    (0, "Wellfleet-BOT-MIB", "wfBotCUAddrReachable"),
)
if mibBuilder.loadTexts:
    wfBotCUEntry.setStatus("mandatory")


class _WfBotCUEntryDelete_Type(Integer32):
    """Custom type wfBotCUEntryDelete based on Integer32"""
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


_WfBotCUEntryDelete_Type.__name__ = "Integer32"
_WfBotCUEntryDelete_Object = MibTableColumn
wfBotCUEntryDelete = _WfBotCUEntryDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4, 1, 1),
    _WfBotCUEntryDelete_Type()
)
wfBotCUEntryDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBotCUEntryDelete.setStatus("mandatory")


class _WfBotCUEntryDisable_Type(Integer32):
    """Custom type wfBotCUEntryDisable based on Integer32"""
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


_WfBotCUEntryDisable_Type.__name__ = "Integer32"
_WfBotCUEntryDisable_Object = MibTableColumn
wfBotCUEntryDisable = _WfBotCUEntryDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4, 1, 2),
    _WfBotCUEntryDisable_Type()
)
wfBotCUEntryDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBotCUEntryDisable.setStatus("mandatory")
_WfBotCUSlotNumber_Type = Integer32
_WfBotCUSlotNumber_Object = MibTableColumn
wfBotCUSlotNumber = _WfBotCUSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4, 1, 3),
    _WfBotCUSlotNumber_Type()
)
wfBotCUSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBotCUSlotNumber.setStatus("mandatory")
_WfBotCUCctNumber_Type = Integer32
_WfBotCUCctNumber_Object = MibTableColumn
wfBotCUCctNumber = _WfBotCUCctNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4, 1, 4),
    _WfBotCUCctNumber_Type()
)
wfBotCUCctNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBotCUCctNumber.setStatus("mandatory")
_WfBotCURemoteIpAddr_Type = IpAddress
_WfBotCURemoteIpAddr_Object = MibTableColumn
wfBotCURemoteIpAddr = _WfBotCURemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4, 1, 5),
    _WfBotCURemoteIpAddr_Type()
)
wfBotCURemoteIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBotCURemoteIpAddr.setStatus("mandatory")


class _WfBotCULocalTcpListenPort_Type(Integer32):
    """Custom type wfBotCULocalTcpListenPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 9999),
    )


_WfBotCULocalTcpListenPort_Type.__name__ = "Integer32"
_WfBotCULocalTcpListenPort_Object = MibTableColumn
wfBotCULocalTcpListenPort = _WfBotCULocalTcpListenPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4, 1, 6),
    _WfBotCULocalTcpListenPort_Type()
)
wfBotCULocalTcpListenPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBotCULocalTcpListenPort.setStatus("mandatory")


class _WfBotCURemoteTcpListenPort_Type(Integer32):
    """Custom type wfBotCURemoteTcpListenPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 9999),
    )


_WfBotCURemoteTcpListenPort_Type.__name__ = "Integer32"
_WfBotCURemoteTcpListenPort_Object = MibTableColumn
wfBotCURemoteTcpListenPort = _WfBotCURemoteTcpListenPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4, 1, 7),
    _WfBotCURemoteTcpListenPort_Type()
)
wfBotCURemoteTcpListenPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBotCURemoteTcpListenPort.setStatus("mandatory")


class _WfBotCUAddrReachable_Type(Integer32):
    """Custom type wfBotCUAddrReachable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            254
        )
    )
    namedValues = NamedValues(
        ("address", 254)
    )


_WfBotCUAddrReachable_Type.__name__ = "Integer32"
_WfBotCUAddrReachable_Object = MibTableColumn
wfBotCUAddrReachable = _WfBotCUAddrReachable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 18, 4, 1, 8),
    _WfBotCUAddrReachable_Type()
)
wfBotCUAddrReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBotCUAddrReachable.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-BOT-MIB",
    **{"wfBot": wfBot,
       "wfBotDelete": wfBotDelete,
       "wfBotDisable": wfBotDisable,
       "wfBotState": wfBotState,
       "wfBotInterfaceTable": wfBotInterfaceTable,
       "wfBotInterfaceEntry": wfBotInterfaceEntry,
       "wfBotInterfaceDelete": wfBotInterfaceDelete,
       "wfBotInterfaceDisable": wfBotInterfaceDisable,
       "wfBotInterfaceCctNumber": wfBotInterfaceCctNumber,
       "wfBotInterfaceSlotNumber": wfBotInterfaceSlotNumber,
       "wfBotInterfaceState": wfBotInterfaceState,
       "wfBotInterfaceType": wfBotInterfaceType,
       "wfBotInterfaceAttachedTo": wfBotInterfaceAttachedTo,
       "wfBotInterfacePktCnt": wfBotInterfacePktCnt,
       "wfBotKeepaliveInterval": wfBotKeepaliveInterval,
       "wfBotKeepaliveRto": wfBotKeepaliveRto,
       "wfBotKeepaliveMaxRetry": wfBotKeepaliveMaxRetry,
       "wfBotPeerTable": wfBotPeerTable,
       "wfBotPeerEntry": wfBotPeerEntry,
       "wfBotPeerEntryDelete": wfBotPeerEntryDelete,
       "wfBotPeerEntryDisable": wfBotPeerEntryDisable,
       "wfBotPeerSlotNumber": wfBotPeerSlotNumber,
       "wfBotPeerCctNumber": wfBotPeerCctNumber,
       "wfBotPeerRemoteIpAddr": wfBotPeerRemoteIpAddr,
       "wfBotConnOriginator": wfBotConnOriginator,
       "wfBotPeerLocalTcpListenPort": wfBotPeerLocalTcpListenPort,
       "wfBotPeerRemoteTcpListenPort": wfBotPeerRemoteTcpListenPort,
       "wfBotPeerLocalTcpPort": wfBotPeerLocalTcpPort,
       "wfBotPeerRemoteTcpPort": wfBotPeerRemoteTcpPort,
       "wfBotCUTable": wfBotCUTable,
       "wfBotCUEntry": wfBotCUEntry,
       "wfBotCUEntryDelete": wfBotCUEntryDelete,
       "wfBotCUEntryDisable": wfBotCUEntryDisable,
       "wfBotCUSlotNumber": wfBotCUSlotNumber,
       "wfBotCUCctNumber": wfBotCUCctNumber,
       "wfBotCURemoteIpAddr": wfBotCURemoteIpAddr,
       "wfBotCULocalTcpListenPort": wfBotCULocalTcpListenPort,
       "wfBotCURemoteTcpListenPort": wfBotCURemoteTcpListenPort,
       "wfBotCUAddrReachable": wfBotCUAddrReachable}
)
