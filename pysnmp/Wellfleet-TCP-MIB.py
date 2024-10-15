# SNMP MIB module (Wellfleet-TCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-TCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:16 2024
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

(wfTcpGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfTcpGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfTcp_ObjectIdentity = ObjectIdentity
wfTcp = _WfTcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1)
)


class _WfTcpDelete_Type(Integer32):
    """Custom type wfTcpDelete based on Integer32"""
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


_WfTcpDelete_Type.__name__ = "Integer32"
_WfTcpDelete_Object = MibScalar
wfTcpDelete = _WfTcpDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 1),
    _WfTcpDelete_Type()
)
wfTcpDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTcpDelete.setStatus("mandatory")


class _WfTcpDisable_Type(Integer32):
    """Custom type wfTcpDisable based on Integer32"""
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


_WfTcpDisable_Type.__name__ = "Integer32"
_WfTcpDisable_Object = MibScalar
wfTcpDisable = _WfTcpDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 2),
    _WfTcpDisable_Type()
)
wfTcpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTcpDisable.setStatus("mandatory")


class _WfTcpState_Type(Integer32):
    """Custom type wfTcpState based on Integer32"""
    defaultValue = 4

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


_WfTcpState_Type.__name__ = "Integer32"
_WfTcpState_Object = MibScalar
wfTcpState = _WfTcpState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 3),
    _WfTcpState_Type()
)
wfTcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTcpState.setStatus("mandatory")


class _WfTcpRtoAlgorithm_Type(Integer32):
    """Custom type wfTcpRtoAlgorithm based on Integer32"""
    defaultValue = 4

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
        *(("constant", 2),
          ("other", 1),
          ("rsre", 3),
          ("vanj", 4))
    )


_WfTcpRtoAlgorithm_Type.__name__ = "Integer32"
_WfTcpRtoAlgorithm_Object = MibScalar
wfTcpRtoAlgorithm = _WfTcpRtoAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 4),
    _WfTcpRtoAlgorithm_Type()
)
wfTcpRtoAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTcpRtoAlgorithm.setStatus("mandatory")


class _WfTcpRtoMin_Type(Integer32):
    """Custom type wfTcpRtoMin based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 15000),
    )


_WfTcpRtoMin_Type.__name__ = "Integer32"
_WfTcpRtoMin_Object = MibScalar
wfTcpRtoMin = _WfTcpRtoMin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 5),
    _WfTcpRtoMin_Type()
)
wfTcpRtoMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTcpRtoMin.setStatus("mandatory")


class _WfTcpRtoMax_Type(Integer32):
    """Custom type wfTcpRtoMax based on Integer32"""
    defaultValue = 240000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15000, 240000),
    )


_WfTcpRtoMax_Type.__name__ = "Integer32"
_WfTcpRtoMax_Object = MibScalar
wfTcpRtoMax = _WfTcpRtoMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 6),
    _WfTcpRtoMax_Type()
)
wfTcpRtoMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTcpRtoMax.setStatus("mandatory")
_WfTcpMaxConn_Type = Integer32
_WfTcpMaxConn_Object = MibScalar
wfTcpMaxConn = _WfTcpMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 7),
    _WfTcpMaxConn_Type()
)
wfTcpMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTcpMaxConn.setStatus("mandatory")
_WfTcpActiveOpens_Type = Counter32
_WfTcpActiveOpens_Object = MibScalar
wfTcpActiveOpens = _WfTcpActiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 8),
    _WfTcpActiveOpens_Type()
)
wfTcpActiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTcpActiveOpens.setStatus("mandatory")
_WfTcpPassiveOpens_Type = Counter32
_WfTcpPassiveOpens_Object = MibScalar
wfTcpPassiveOpens = _WfTcpPassiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 9),
    _WfTcpPassiveOpens_Type()
)
wfTcpPassiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTcpPassiveOpens.setStatus("mandatory")
_WfTcpAttemptFails_Type = Counter32
_WfTcpAttemptFails_Object = MibScalar
wfTcpAttemptFails = _WfTcpAttemptFails_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 10),
    _WfTcpAttemptFails_Type()
)
wfTcpAttemptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTcpAttemptFails.setStatus("mandatory")
_WfTcpEstabResets_Type = Gauge32
_WfTcpEstabResets_Object = MibScalar
wfTcpEstabResets = _WfTcpEstabResets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 11),
    _WfTcpEstabResets_Type()
)
wfTcpEstabResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTcpEstabResets.setStatus("mandatory")
_WfTcpCurrEstab_Type = Gauge32
_WfTcpCurrEstab_Object = MibScalar
wfTcpCurrEstab = _WfTcpCurrEstab_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 12),
    _WfTcpCurrEstab_Type()
)
wfTcpCurrEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTcpCurrEstab.setStatus("mandatory")
_WfTcpInSegs_Type = Counter32
_WfTcpInSegs_Object = MibScalar
wfTcpInSegs = _WfTcpInSegs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 13),
    _WfTcpInSegs_Type()
)
wfTcpInSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTcpInSegs.setStatus("mandatory")
_WfTcpOutSegs_Type = Counter32
_WfTcpOutSegs_Object = MibScalar
wfTcpOutSegs = _WfTcpOutSegs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 14),
    _WfTcpOutSegs_Type()
)
wfTcpOutSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTcpOutSegs.setStatus("mandatory")
_WfTcpRetransSegs_Type = Counter32
_WfTcpRetransSegs_Object = MibScalar
wfTcpRetransSegs = _WfTcpRetransSegs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 15),
    _WfTcpRetransSegs_Type()
)
wfTcpRetransSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTcpRetransSegs.setStatus("mandatory")
_WfTcpInErrs_Type = Counter32
_WfTcpInErrs_Object = MibScalar
wfTcpInErrs = _WfTcpInErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 16),
    _WfTcpInErrs_Type()
)
wfTcpInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTcpInErrs.setStatus("mandatory")
_WfTcpOutRsts_Type = Counter32
_WfTcpOutRsts_Object = MibScalar
wfTcpOutRsts = _WfTcpOutRsts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 17),
    _WfTcpOutRsts_Type()
)
wfTcpOutRsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTcpOutRsts.setStatus("mandatory")


class _WfTcpMaxWindow_Type(Integer32):
    """Custom type wfTcpMaxWindow based on Integer32"""
    defaultValue = 4096

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 65535),
    )


_WfTcpMaxWindow_Type.__name__ = "Integer32"
_WfTcpMaxWindow_Object = MibScalar
wfTcpMaxWindow = _WfTcpMaxWindow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 1, 18),
    _WfTcpMaxWindow_Type()
)
wfTcpMaxWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTcpMaxWindow.setStatus("mandatory")
_WfTcpConnTable_Object = MibTable
wfTcpConnTable = _WfTcpConnTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 2)
)
if mibBuilder.loadTexts:
    wfTcpConnTable.setStatus("mandatory")
_WfTcpConnEntry_Object = MibTableRow
wfTcpConnEntry = _WfTcpConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 2, 1)
)
wfTcpConnEntry.setIndexNames(
    (0, "Wellfleet-TCP-MIB", "wfTcpConnLocalAddress"),
    (0, "Wellfleet-TCP-MIB", "wfTcpConnLocalPort"),
    (0, "Wellfleet-TCP-MIB", "wfTcpConnRemAddress"),
    (0, "Wellfleet-TCP-MIB", "wfTcpConnRemPort"),
)
if mibBuilder.loadTexts:
    wfTcpConnEntry.setStatus("mandatory")


class _WfTcpConnDelete_Type(Integer32):
    """Custom type wfTcpConnDelete based on Integer32"""
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


_WfTcpConnDelete_Type.__name__ = "Integer32"
_WfTcpConnDelete_Object = MibTableColumn
wfTcpConnDelete = _WfTcpConnDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 2, 1, 1),
    _WfTcpConnDelete_Type()
)
wfTcpConnDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTcpConnDelete.setStatus("mandatory")


class _WfTcpConnState_Type(Integer32):
    """Custom type wfTcpConnState based on Integer32"""
    defaultValue = 1

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
              12)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("closewait", 8),
          ("closing", 10),
          ("deletetcb", 12),
          ("established", 5),
          ("finwait1", 6),
          ("finwait2", 7),
          ("lastack", 9),
          ("listen", 2),
          ("synreceived", 4),
          ("synsent", 3),
          ("timewait", 11))
    )


_WfTcpConnState_Type.__name__ = "Integer32"
_WfTcpConnState_Object = MibTableColumn
wfTcpConnState = _WfTcpConnState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 2, 1, 2),
    _WfTcpConnState_Type()
)
wfTcpConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTcpConnState.setStatus("mandatory")
_WfTcpConnLocalAddress_Type = IpAddress
_WfTcpConnLocalAddress_Object = MibTableColumn
wfTcpConnLocalAddress = _WfTcpConnLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 2, 1, 3),
    _WfTcpConnLocalAddress_Type()
)
wfTcpConnLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTcpConnLocalAddress.setStatus("mandatory")


class _WfTcpConnLocalPort_Type(Integer32):
    """Custom type wfTcpConnLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfTcpConnLocalPort_Type.__name__ = "Integer32"
_WfTcpConnLocalPort_Object = MibTableColumn
wfTcpConnLocalPort = _WfTcpConnLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 2, 1, 4),
    _WfTcpConnLocalPort_Type()
)
wfTcpConnLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTcpConnLocalPort.setStatus("mandatory")
_WfTcpConnRemAddress_Type = IpAddress
_WfTcpConnRemAddress_Object = MibTableColumn
wfTcpConnRemAddress = _WfTcpConnRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 2, 1, 5),
    _WfTcpConnRemAddress_Type()
)
wfTcpConnRemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTcpConnRemAddress.setStatus("mandatory")


class _WfTcpConnRemPort_Type(Integer32):
    """Custom type wfTcpConnRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfTcpConnRemPort_Type.__name__ = "Integer32"
_WfTcpConnRemPort_Object = MibTableColumn
wfTcpConnRemPort = _WfTcpConnRemPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 2, 1, 6),
    _WfTcpConnRemPort_Type()
)
wfTcpConnRemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTcpConnRemPort.setStatus("mandatory")


class _WfTcpConnKeepAliveInterval_Type(Integer32):
    """Custom type wfTcpConnKeepAliveInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_WfTcpConnKeepAliveInterval_Type.__name__ = "Integer32"
_WfTcpConnKeepAliveInterval_Object = MibTableColumn
wfTcpConnKeepAliveInterval = _WfTcpConnKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 2, 1, 7),
    _WfTcpConnKeepAliveInterval_Type()
)
wfTcpConnKeepAliveInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTcpConnKeepAliveInterval.setStatus("mandatory")


class _WfTcpConnKeepAliveRto_Type(Integer32):
    """Custom type wfTcpConnKeepAliveRto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_WfTcpConnKeepAliveRto_Type.__name__ = "Integer32"
_WfTcpConnKeepAliveRto_Object = MibTableColumn
wfTcpConnKeepAliveRto = _WfTcpConnKeepAliveRto_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 2, 1, 8),
    _WfTcpConnKeepAliveRto_Type()
)
wfTcpConnKeepAliveRto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTcpConnKeepAliveRto.setStatus("mandatory")
_WfTcpConnKeepAliveCount_Type = Counter32
_WfTcpConnKeepAliveCount_Object = MibTableColumn
wfTcpConnKeepAliveCount = _WfTcpConnKeepAliveCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 2, 1, 9),
    _WfTcpConnKeepAliveCount_Type()
)
wfTcpConnKeepAliveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTcpConnKeepAliveCount.setStatus("mandatory")
_WfTcpConnMd5Errors_Type = Counter32
_WfTcpConnMd5Errors_Object = MibTableColumn
wfTcpConnMd5Errors = _WfTcpConnMd5Errors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 3, 2, 1, 10),
    _WfTcpConnMd5Errors_Type()
)
wfTcpConnMd5Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTcpConnMd5Errors.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-TCP-MIB",
    **{"wfTcp": wfTcp,
       "wfTcpDelete": wfTcpDelete,
       "wfTcpDisable": wfTcpDisable,
       "wfTcpState": wfTcpState,
       "wfTcpRtoAlgorithm": wfTcpRtoAlgorithm,
       "wfTcpRtoMin": wfTcpRtoMin,
       "wfTcpRtoMax": wfTcpRtoMax,
       "wfTcpMaxConn": wfTcpMaxConn,
       "wfTcpActiveOpens": wfTcpActiveOpens,
       "wfTcpPassiveOpens": wfTcpPassiveOpens,
       "wfTcpAttemptFails": wfTcpAttemptFails,
       "wfTcpEstabResets": wfTcpEstabResets,
       "wfTcpCurrEstab": wfTcpCurrEstab,
       "wfTcpInSegs": wfTcpInSegs,
       "wfTcpOutSegs": wfTcpOutSegs,
       "wfTcpRetransSegs": wfTcpRetransSegs,
       "wfTcpInErrs": wfTcpInErrs,
       "wfTcpOutRsts": wfTcpOutRsts,
       "wfTcpMaxWindow": wfTcpMaxWindow,
       "wfTcpConnTable": wfTcpConnTable,
       "wfTcpConnEntry": wfTcpConnEntry,
       "wfTcpConnDelete": wfTcpConnDelete,
       "wfTcpConnState": wfTcpConnState,
       "wfTcpConnLocalAddress": wfTcpConnLocalAddress,
       "wfTcpConnLocalPort": wfTcpConnLocalPort,
       "wfTcpConnRemAddress": wfTcpConnRemAddress,
       "wfTcpConnRemPort": wfTcpConnRemPort,
       "wfTcpConnKeepAliveInterval": wfTcpConnKeepAliveInterval,
       "wfTcpConnKeepAliveRto": wfTcpConnKeepAliveRto,
       "wfTcpConnKeepAliveCount": wfTcpConnKeepAliveCount,
       "wfTcpConnMd5Errors": wfTcpConnMd5Errors}
)
