# SNMP MIB module (NSC-TCP-EXCEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NSC-TCP-EXCEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:27 2024
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

(nscDx,) = mibBuilder.importSymbols(
    "NSC-MIB",
    "nscDx")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NscDxTcpXcel_ObjectIdentity = ObjectIdentity
nscDxTcpXcel = _NscDxTcpXcel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6)
)
_NscDxTcpXcelTcp_ObjectIdentity = ObjectIdentity
nscDxTcpXcelTcp = _NscDxTcpXcelTcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1)
)


class _NscDxTcpXcelTcpRtoAlgorithm_Type(Integer32):
    """Custom type nscDxTcpXcelTcpRtoAlgorithm based on Integer32"""
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


_NscDxTcpXcelTcpRtoAlgorithm_Type.__name__ = "Integer32"
_NscDxTcpXcelTcpRtoAlgorithm_Object = MibScalar
nscDxTcpXcelTcpRtoAlgorithm = _NscDxTcpXcelTcpRtoAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 1),
    _NscDxTcpXcelTcpRtoAlgorithm_Type()
)
nscDxTcpXcelTcpRtoAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpRtoAlgorithm.setStatus("mandatory")
_NscDxTcpXcelTcpRtoMin_Type = Integer32
_NscDxTcpXcelTcpRtoMin_Object = MibScalar
nscDxTcpXcelTcpRtoMin = _NscDxTcpXcelTcpRtoMin_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 2),
    _NscDxTcpXcelTcpRtoMin_Type()
)
nscDxTcpXcelTcpRtoMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpRtoMin.setStatus("mandatory")
_NscDxTcpXcelTcpRtoMax_Type = Integer32
_NscDxTcpXcelTcpRtoMax_Object = MibScalar
nscDxTcpXcelTcpRtoMax = _NscDxTcpXcelTcpRtoMax_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 3),
    _NscDxTcpXcelTcpRtoMax_Type()
)
nscDxTcpXcelTcpRtoMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpRtoMax.setStatus("mandatory")
_NscDxTcpXcelTcpMaxConn_Type = Integer32
_NscDxTcpXcelTcpMaxConn_Object = MibScalar
nscDxTcpXcelTcpMaxConn = _NscDxTcpXcelTcpMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 4),
    _NscDxTcpXcelTcpMaxConn_Type()
)
nscDxTcpXcelTcpMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpMaxConn.setStatus("mandatory")
_NscDxTcpXcelTcpActiveOpens_Type = Counter32
_NscDxTcpXcelTcpActiveOpens_Object = MibScalar
nscDxTcpXcelTcpActiveOpens = _NscDxTcpXcelTcpActiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 5),
    _NscDxTcpXcelTcpActiveOpens_Type()
)
nscDxTcpXcelTcpActiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpActiveOpens.setStatus("mandatory")
_NscDxTcpXcelTcpPassiveOpens_Type = Counter32
_NscDxTcpXcelTcpPassiveOpens_Object = MibScalar
nscDxTcpXcelTcpPassiveOpens = _NscDxTcpXcelTcpPassiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 6),
    _NscDxTcpXcelTcpPassiveOpens_Type()
)
nscDxTcpXcelTcpPassiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpPassiveOpens.setStatus("mandatory")
_NscDxTcpXcelTcpAttemptFails_Type = Counter32
_NscDxTcpXcelTcpAttemptFails_Object = MibScalar
nscDxTcpXcelTcpAttemptFails = _NscDxTcpXcelTcpAttemptFails_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 7),
    _NscDxTcpXcelTcpAttemptFails_Type()
)
nscDxTcpXcelTcpAttemptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpAttemptFails.setStatus("mandatory")
_NscDxTcpXcelTcpEstabResets_Type = Counter32
_NscDxTcpXcelTcpEstabResets_Object = MibScalar
nscDxTcpXcelTcpEstabResets = _NscDxTcpXcelTcpEstabResets_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 8),
    _NscDxTcpXcelTcpEstabResets_Type()
)
nscDxTcpXcelTcpEstabResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpEstabResets.setStatus("mandatory")
_NscDxTcpXcelTcpCurrEstab_Type = Gauge32
_NscDxTcpXcelTcpCurrEstab_Object = MibScalar
nscDxTcpXcelTcpCurrEstab = _NscDxTcpXcelTcpCurrEstab_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 9),
    _NscDxTcpXcelTcpCurrEstab_Type()
)
nscDxTcpXcelTcpCurrEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpCurrEstab.setStatus("mandatory")
_NscDxTcpXcelTcpInSegs_Type = Counter32
_NscDxTcpXcelTcpInSegs_Object = MibScalar
nscDxTcpXcelTcpInSegs = _NscDxTcpXcelTcpInSegs_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 10),
    _NscDxTcpXcelTcpInSegs_Type()
)
nscDxTcpXcelTcpInSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpInSegs.setStatus("mandatory")
_NscDxTcpXcelTcpOutSegs_Type = Counter32
_NscDxTcpXcelTcpOutSegs_Object = MibScalar
nscDxTcpXcelTcpOutSegs = _NscDxTcpXcelTcpOutSegs_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 11),
    _NscDxTcpXcelTcpOutSegs_Type()
)
nscDxTcpXcelTcpOutSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpOutSegs.setStatus("mandatory")
_NscDxTcpXcelTcpRetransSegs_Type = Counter32
_NscDxTcpXcelTcpRetransSegs_Object = MibScalar
nscDxTcpXcelTcpRetransSegs = _NscDxTcpXcelTcpRetransSegs_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 12),
    _NscDxTcpXcelTcpRetransSegs_Type()
)
nscDxTcpXcelTcpRetransSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpRetransSegs.setStatus("mandatory")
_NscDxTcpXcelTcpConnTable_Object = MibTable
nscDxTcpXcelTcpConnTable = _NscDxTcpXcelTcpConnTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 13)
)
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpConnTable.setStatus("mandatory")
_NscDxTcpXcelTcpConnEntry_Object = MibTableRow
nscDxTcpXcelTcpConnEntry = _NscDxTcpXcelTcpConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 13, 1)
)
nscDxTcpXcelTcpConnEntry.setIndexNames(
    (0, "NSC-TCP-EXCEL-MIB", "nscDxTcpXcelTcpSapId"),
)
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpConnEntry.setStatus("mandatory")


class _NscDxTcpXcelTcpSapId_Type(Integer32):
    """Custom type nscDxTcpXcelTcpSapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NscDxTcpXcelTcpSapId_Type.__name__ = "Integer32"
_NscDxTcpXcelTcpSapId_Object = MibTableColumn
nscDxTcpXcelTcpSapId = _NscDxTcpXcelTcpSapId_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 13, 1, 1),
    _NscDxTcpXcelTcpSapId_Type()
)
nscDxTcpXcelTcpSapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpSapId.setStatus("mandatory")


class _NscDxTcpXcelTcpHostIdx_Type(Integer32):
    """Custom type nscDxTcpXcelTcpHostIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_NscDxTcpXcelTcpHostIdx_Type.__name__ = "Integer32"
_NscDxTcpXcelTcpHostIdx_Object = MibTableColumn
nscDxTcpXcelTcpHostIdx = _NscDxTcpXcelTcpHostIdx_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 13, 1, 2),
    _NscDxTcpXcelTcpHostIdx_Type()
)
nscDxTcpXcelTcpHostIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpHostIdx.setStatus("mandatory")


class _NscDxTcpXcelTcpHostName_Type(DisplayString):
    """Custom type nscDxTcpXcelTcpHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NscDxTcpXcelTcpHostName_Type.__name__ = "DisplayString"
_NscDxTcpXcelTcpHostName_Object = MibTableColumn
nscDxTcpXcelTcpHostName = _NscDxTcpXcelTcpHostName_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 13, 1, 3),
    _NscDxTcpXcelTcpHostName_Type()
)
nscDxTcpXcelTcpHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpHostName.setStatus("mandatory")


class _NscDxTcpXcelTcpConnState_Type(Integer32):
    """Custom type nscDxTcpXcelTcpConnState based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("closeWait", 8),
          ("closed", 1),
          ("closing", 10),
          ("established", 5),
          ("finWait1", 6),
          ("finWait2", 7),
          ("lastAck", 9),
          ("listen", 2),
          ("synReceived", 4),
          ("synSent", 3),
          ("timeWait", 11))
    )


_NscDxTcpXcelTcpConnState_Type.__name__ = "Integer32"
_NscDxTcpXcelTcpConnState_Object = MibTableColumn
nscDxTcpXcelTcpConnState = _NscDxTcpXcelTcpConnState_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 13, 1, 4),
    _NscDxTcpXcelTcpConnState_Type()
)
nscDxTcpXcelTcpConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpConnState.setStatus("mandatory")
_NscDxTcpXcelTcpConnLocalAddress_Type = IpAddress
_NscDxTcpXcelTcpConnLocalAddress_Object = MibTableColumn
nscDxTcpXcelTcpConnLocalAddress = _NscDxTcpXcelTcpConnLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 13, 1, 5),
    _NscDxTcpXcelTcpConnLocalAddress_Type()
)
nscDxTcpXcelTcpConnLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpConnLocalAddress.setStatus("mandatory")


class _NscDxTcpXcelTcpConnLocalPort_Type(Integer32):
    """Custom type nscDxTcpXcelTcpConnLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NscDxTcpXcelTcpConnLocalPort_Type.__name__ = "Integer32"
_NscDxTcpXcelTcpConnLocalPort_Object = MibTableColumn
nscDxTcpXcelTcpConnLocalPort = _NscDxTcpXcelTcpConnLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 13, 1, 6),
    _NscDxTcpXcelTcpConnLocalPort_Type()
)
nscDxTcpXcelTcpConnLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpConnLocalPort.setStatus("mandatory")
_NscDxTcpXcelTcpConnRemAddress_Type = IpAddress
_NscDxTcpXcelTcpConnRemAddress_Object = MibTableColumn
nscDxTcpXcelTcpConnRemAddress = _NscDxTcpXcelTcpConnRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 13, 1, 7),
    _NscDxTcpXcelTcpConnRemAddress_Type()
)
nscDxTcpXcelTcpConnRemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpConnRemAddress.setStatus("mandatory")


class _NscDxTcpXcelTcpConnRemPort_Type(Integer32):
    """Custom type nscDxTcpXcelTcpConnRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NscDxTcpXcelTcpConnRemPort_Type.__name__ = "Integer32"
_NscDxTcpXcelTcpConnRemPort_Object = MibTableColumn
nscDxTcpXcelTcpConnRemPort = _NscDxTcpXcelTcpConnRemPort_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 13, 1, 8),
    _NscDxTcpXcelTcpConnRemPort_Type()
)
nscDxTcpXcelTcpConnRemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpConnRemPort.setStatus("mandatory")
_NscDxTcpXcelTcpInErrs_Type = Counter32
_NscDxTcpXcelTcpInErrs_Object = MibScalar
nscDxTcpXcelTcpInErrs = _NscDxTcpXcelTcpInErrs_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 14),
    _NscDxTcpXcelTcpInErrs_Type()
)
nscDxTcpXcelTcpInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpInErrs.setStatus("mandatory")
_NscDxTcpXcelTcpOutRsts_Type = Counter32
_NscDxTcpXcelTcpOutRsts_Object = MibScalar
nscDxTcpXcelTcpOutRsts = _NscDxTcpXcelTcpOutRsts_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 15),
    _NscDxTcpXcelTcpOutRsts_Type()
)
nscDxTcpXcelTcpOutRsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpOutRsts.setStatus("mandatory")
_NscDxTcpXcelTcpConnAttempt_Type = Counter32
_NscDxTcpXcelTcpConnAttempt_Object = MibScalar
nscDxTcpXcelTcpConnAttempt = _NscDxTcpXcelTcpConnAttempt_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 16),
    _NscDxTcpXcelTcpConnAttempt_Type()
)
nscDxTcpXcelTcpConnAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpConnAttempt.setStatus("mandatory")
_NscDxTcpXcelTcpClosed_Type = Counter32
_NscDxTcpXcelTcpClosed_Object = MibScalar
nscDxTcpXcelTcpClosed = _NscDxTcpXcelTcpClosed_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 17),
    _NscDxTcpXcelTcpClosed_Type()
)
nscDxTcpXcelTcpClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpClosed.setStatus("mandatory")
_NscDxTcpXcelTcpSegsTimed_Type = Counter32
_NscDxTcpXcelTcpSegsTimed_Object = MibScalar
nscDxTcpXcelTcpSegsTimed = _NscDxTcpXcelTcpSegsTimed_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 18),
    _NscDxTcpXcelTcpSegsTimed_Type()
)
nscDxTcpXcelTcpSegsTimed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpSegsTimed.setStatus("mandatory")
_NscDxTcpXcelTcpRttUpdated_Type = Counter32
_NscDxTcpXcelTcpRttUpdated_Object = MibScalar
nscDxTcpXcelTcpRttUpdated = _NscDxTcpXcelTcpRttUpdated_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 19),
    _NscDxTcpXcelTcpRttUpdated_Type()
)
nscDxTcpXcelTcpRttUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpRttUpdated.setStatus("mandatory")
_NscDxTcpXcelTcpDelAck_Type = Counter32
_NscDxTcpXcelTcpDelAck_Object = MibScalar
nscDxTcpXcelTcpDelAck = _NscDxTcpXcelTcpDelAck_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 20),
    _NscDxTcpXcelTcpDelAck_Type()
)
nscDxTcpXcelTcpDelAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpDelAck.setStatus("mandatory")
_NscDxTcpXcelTcpTimeoutDrop_Type = Counter32
_NscDxTcpXcelTcpTimeoutDrop_Object = MibScalar
nscDxTcpXcelTcpTimeoutDrop = _NscDxTcpXcelTcpTimeoutDrop_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 21),
    _NscDxTcpXcelTcpTimeoutDrop_Type()
)
nscDxTcpXcelTcpTimeoutDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpTimeoutDrop.setStatus("mandatory")
_NscDxTcpXcelTcpRexmtTimeo_Type = Counter32
_NscDxTcpXcelTcpRexmtTimeo_Object = MibScalar
nscDxTcpXcelTcpRexmtTimeo = _NscDxTcpXcelTcpRexmtTimeo_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 22),
    _NscDxTcpXcelTcpRexmtTimeo_Type()
)
nscDxTcpXcelTcpRexmtTimeo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpRexmtTimeo.setStatus("mandatory")
_NscDxTcpXcelTcpPersistTimeo_Type = Counter32
_NscDxTcpXcelTcpPersistTimeo_Object = MibScalar
nscDxTcpXcelTcpPersistTimeo = _NscDxTcpXcelTcpPersistTimeo_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 23),
    _NscDxTcpXcelTcpPersistTimeo_Type()
)
nscDxTcpXcelTcpPersistTimeo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpPersistTimeo.setStatus("mandatory")
_NscDxTcpXcelTcpKeepTimeo_Type = Counter32
_NscDxTcpXcelTcpKeepTimeo_Object = MibScalar
nscDxTcpXcelTcpKeepTimeo = _NscDxTcpXcelTcpKeepTimeo_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 24),
    _NscDxTcpXcelTcpKeepTimeo_Type()
)
nscDxTcpXcelTcpKeepTimeo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpKeepTimeo.setStatus("mandatory")
_NscDxTcpXcelTcpKeepProbe_Type = Counter32
_NscDxTcpXcelTcpKeepProbe_Object = MibScalar
nscDxTcpXcelTcpKeepProbe = _NscDxTcpXcelTcpKeepProbe_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 25),
    _NscDxTcpXcelTcpKeepProbe_Type()
)
nscDxTcpXcelTcpKeepProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpKeepProbe.setStatus("mandatory")
_NscDxTcpXcelTcpKeepDrop_Type = Counter32
_NscDxTcpXcelTcpKeepDrop_Object = MibScalar
nscDxTcpXcelTcpKeepDrop = _NscDxTcpXcelTcpKeepDrop_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 26),
    _NscDxTcpXcelTcpKeepDrop_Type()
)
nscDxTcpXcelTcpKeepDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpKeepDrop.setStatus("mandatory")
_NscDxTcpXcelTcpSndPack_Type = Counter32
_NscDxTcpXcelTcpSndPack_Object = MibScalar
nscDxTcpXcelTcpSndPack = _NscDxTcpXcelTcpSndPack_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 27),
    _NscDxTcpXcelTcpSndPack_Type()
)
nscDxTcpXcelTcpSndPack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpSndPack.setStatus("mandatory")
_NscDxTcpXcelTcpSndByte_Type = Counter32
_NscDxTcpXcelTcpSndByte_Object = MibScalar
nscDxTcpXcelTcpSndByte = _NscDxTcpXcelTcpSndByte_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 28),
    _NscDxTcpXcelTcpSndByte_Type()
)
nscDxTcpXcelTcpSndByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpSndByte.setStatus("mandatory")
_NscDxTcpXcelTcpSndRexmitPack_Type = Counter32
_NscDxTcpXcelTcpSndRexmitPack_Object = MibScalar
nscDxTcpXcelTcpSndRexmitPack = _NscDxTcpXcelTcpSndRexmitPack_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 29),
    _NscDxTcpXcelTcpSndRexmitPack_Type()
)
nscDxTcpXcelTcpSndRexmitPack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpSndRexmitPack.setStatus("mandatory")
_NscDxTcpXcelTcpSndRexmitByte_Type = Counter32
_NscDxTcpXcelTcpSndRexmitByte_Object = MibScalar
nscDxTcpXcelTcpSndRexmitByte = _NscDxTcpXcelTcpSndRexmitByte_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 30),
    _NscDxTcpXcelTcpSndRexmitByte_Type()
)
nscDxTcpXcelTcpSndRexmitByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpSndRexmitByte.setStatus("mandatory")
_NscDxTcpXcelTcpSndAcks_Type = Counter32
_NscDxTcpXcelTcpSndAcks_Object = MibScalar
nscDxTcpXcelTcpSndAcks = _NscDxTcpXcelTcpSndAcks_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 31),
    _NscDxTcpXcelTcpSndAcks_Type()
)
nscDxTcpXcelTcpSndAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpSndAcks.setStatus("mandatory")
_NscDxTcpXcelTcpSndProbe_Type = Counter32
_NscDxTcpXcelTcpSndProbe_Object = MibScalar
nscDxTcpXcelTcpSndProbe = _NscDxTcpXcelTcpSndProbe_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 32),
    _NscDxTcpXcelTcpSndProbe_Type()
)
nscDxTcpXcelTcpSndProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpSndProbe.setStatus("mandatory")
_NscDxTcpXcelTcpSndUrg_Type = Counter32
_NscDxTcpXcelTcpSndUrg_Object = MibScalar
nscDxTcpXcelTcpSndUrg = _NscDxTcpXcelTcpSndUrg_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 33),
    _NscDxTcpXcelTcpSndUrg_Type()
)
nscDxTcpXcelTcpSndUrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpSndUrg.setStatus("mandatory")
_NscDxTcpXcelTcpSndWinUp_Type = Counter32
_NscDxTcpXcelTcpSndWinUp_Object = MibScalar
nscDxTcpXcelTcpSndWinUp = _NscDxTcpXcelTcpSndWinUp_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 34),
    _NscDxTcpXcelTcpSndWinUp_Type()
)
nscDxTcpXcelTcpSndWinUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpSndWinUp.setStatus("mandatory")
_NscDxTcpXcelTcpSndCtrl_Type = Counter32
_NscDxTcpXcelTcpSndCtrl_Object = MibScalar
nscDxTcpXcelTcpSndCtrl = _NscDxTcpXcelTcpSndCtrl_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 35),
    _NscDxTcpXcelTcpSndCtrl_Type()
)
nscDxTcpXcelTcpSndCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpSndCtrl.setStatus("mandatory")
_NscDxTcpXcelTcpPcbCacheMiss_Type = Counter32
_NscDxTcpXcelTcpPcbCacheMiss_Object = MibScalar
nscDxTcpXcelTcpPcbCacheMiss = _NscDxTcpXcelTcpPcbCacheMiss_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 36),
    _NscDxTcpXcelTcpPcbCacheMiss_Type()
)
nscDxTcpXcelTcpPcbCacheMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpPcbCacheMiss.setStatus("mandatory")
_NscDxTcpXcelTcpRcvPack_Type = Counter32
_NscDxTcpXcelTcpRcvPack_Object = MibScalar
nscDxTcpXcelTcpRcvPack = _NscDxTcpXcelTcpRcvPack_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 37),
    _NscDxTcpXcelTcpRcvPack_Type()
)
nscDxTcpXcelTcpRcvPack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpRcvPack.setStatus("mandatory")
_NscDxTcpXcelTcpRcvBytes_Type = Counter32
_NscDxTcpXcelTcpRcvBytes_Object = MibScalar
nscDxTcpXcelTcpRcvBytes = _NscDxTcpXcelTcpRcvBytes_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 38),
    _NscDxTcpXcelTcpRcvBytes_Type()
)
nscDxTcpXcelTcpRcvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpRcvBytes.setStatus("mandatory")
_NscDxTcpXcelTcpRcvByteAfterWin_Type = Counter32
_NscDxTcpXcelTcpRcvByteAfterWin_Object = MibScalar
nscDxTcpXcelTcpRcvByteAfterWin = _NscDxTcpXcelTcpRcvByteAfterWin_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 39),
    _NscDxTcpXcelTcpRcvByteAfterWin_Type()
)
nscDxTcpXcelTcpRcvByteAfterWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpRcvByteAfterWin.setStatus("mandatory")
_NscDxTcpXcelTcpRcvAfterClose_Type = Counter32
_NscDxTcpXcelTcpRcvAfterClose_Object = MibScalar
nscDxTcpXcelTcpRcvAfterClose = _NscDxTcpXcelTcpRcvAfterClose_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 40),
    _NscDxTcpXcelTcpRcvAfterClose_Type()
)
nscDxTcpXcelTcpRcvAfterClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpRcvAfterClose.setStatus("mandatory")
_NscDxTcpXcelTcpRcvWinProbe_Type = Counter32
_NscDxTcpXcelTcpRcvWinProbe_Object = MibScalar
nscDxTcpXcelTcpRcvWinProbe = _NscDxTcpXcelTcpRcvWinProbe_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 41),
    _NscDxTcpXcelTcpRcvWinProbe_Type()
)
nscDxTcpXcelTcpRcvWinProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpRcvWinProbe.setStatus("mandatory")
_NscDxTcpXcelTcpRcvdUpack_Type = Counter32
_NscDxTcpXcelTcpRcvdUpack_Object = MibScalar
nscDxTcpXcelTcpRcvdUpack = _NscDxTcpXcelTcpRcvdUpack_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 42),
    _NscDxTcpXcelTcpRcvdUpack_Type()
)
nscDxTcpXcelTcpRcvdUpack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpRcvdUpack.setStatus("mandatory")
_NscDxTcpXcelTcpRcvAckTooMuch_Type = Counter32
_NscDxTcpXcelTcpRcvAckTooMuch_Object = MibScalar
nscDxTcpXcelTcpRcvAckTooMuch = _NscDxTcpXcelTcpRcvAckTooMuch_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 43),
    _NscDxTcpXcelTcpRcvAckTooMuch_Type()
)
nscDxTcpXcelTcpRcvAckTooMuch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpRcvAckTooMuch.setStatus("mandatory")
_NscDxTcpXcelTcpRcvAckPack_Type = Counter32
_NscDxTcpXcelTcpRcvAckPack_Object = MibScalar
nscDxTcpXcelTcpRcvAckPack = _NscDxTcpXcelTcpRcvAckPack_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 44),
    _NscDxTcpXcelTcpRcvAckPack_Type()
)
nscDxTcpXcelTcpRcvAckPack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpRcvAckPack.setStatus("mandatory")
_NscDxTcpXcelTcpRcvAckByte_Type = Counter32
_NscDxTcpXcelTcpRcvAckByte_Object = MibScalar
nscDxTcpXcelTcpRcvAckByte = _NscDxTcpXcelTcpRcvAckByte_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 45),
    _NscDxTcpXcelTcpRcvAckByte_Type()
)
nscDxTcpXcelTcpRcvAckByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpRcvAckByte.setStatus("mandatory")
_NscDxTcpXcelTcpRcvWinUpd_Type = Counter32
_NscDxTcpXcelTcpRcvWinUpd_Object = MibScalar
nscDxTcpXcelTcpRcvWinUpd = _NscDxTcpXcelTcpRcvWinUpd_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 1, 46),
    _NscDxTcpXcelTcpRcvWinUpd_Type()
)
nscDxTcpXcelTcpRcvWinUpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelTcpRcvWinUpd.setStatus("mandatory")
_NscDxTcpXcelUdp_ObjectIdentity = ObjectIdentity
nscDxTcpXcelUdp = _NscDxTcpXcelUdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 2)
)
_NscDxTcpXcelUdpInDatagrams_Type = Counter32
_NscDxTcpXcelUdpInDatagrams_Object = MibScalar
nscDxTcpXcelUdpInDatagrams = _NscDxTcpXcelUdpInDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 2, 1),
    _NscDxTcpXcelUdpInDatagrams_Type()
)
nscDxTcpXcelUdpInDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelUdpInDatagrams.setStatus("mandatory")
_NscDxTcpXcelUdpNoPorts_Type = Counter32
_NscDxTcpXcelUdpNoPorts_Object = MibScalar
nscDxTcpXcelUdpNoPorts = _NscDxTcpXcelUdpNoPorts_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 2, 2),
    _NscDxTcpXcelUdpNoPorts_Type()
)
nscDxTcpXcelUdpNoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelUdpNoPorts.setStatus("mandatory")
_NscDxTcpXcelUdpInErrors_Type = Counter32
_NscDxTcpXcelUdpInErrors_Object = MibScalar
nscDxTcpXcelUdpInErrors = _NscDxTcpXcelUdpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 2, 3),
    _NscDxTcpXcelUdpInErrors_Type()
)
nscDxTcpXcelUdpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelUdpInErrors.setStatus("mandatory")
_NscDxTcpXcelUdpOutDatagrams_Type = Counter32
_NscDxTcpXcelUdpOutDatagrams_Object = MibScalar
nscDxTcpXcelUdpOutDatagrams = _NscDxTcpXcelUdpOutDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 2, 4),
    _NscDxTcpXcelUdpOutDatagrams_Type()
)
nscDxTcpXcelUdpOutDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelUdpOutDatagrams.setStatus("mandatory")
_NscDxTcpXcelUdpNoPortBcast_Type = Counter32
_NscDxTcpXcelUdpNoPortBcast_Object = MibScalar
nscDxTcpXcelUdpNoPortBcast = _NscDxTcpXcelUdpNoPortBcast_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 2, 5),
    _NscDxTcpXcelUdpNoPortBcast_Type()
)
nscDxTcpXcelUdpNoPortBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelUdpNoPortBcast.setStatus("mandatory")
_NscDxTcpXcelUdpPcbCacheMissing_Type = Counter32
_NscDxTcpXcelUdpPcbCacheMissing_Object = MibScalar
nscDxTcpXcelUdpPcbCacheMissing = _NscDxTcpXcelUdpPcbCacheMissing_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 2, 6),
    _NscDxTcpXcelUdpPcbCacheMissing_Type()
)
nscDxTcpXcelUdpPcbCacheMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelUdpPcbCacheMissing.setStatus("mandatory")
_NscDxTcpXcelUdpTable_Object = MibTable
nscDxTcpXcelUdpTable = _NscDxTcpXcelUdpTable_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 2, 7)
)
if mibBuilder.loadTexts:
    nscDxTcpXcelUdpTable.setStatus("mandatory")
_NscDxTcpXcelUdpEntry_Object = MibTableRow
nscDxTcpXcelUdpEntry = _NscDxTcpXcelUdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 2, 7, 1)
)
nscDxTcpXcelUdpEntry.setIndexNames(
    (0, "NSC-TCP-EXCEL-MIB", "nscDxTcpXcelUdpSapId"),
)
if mibBuilder.loadTexts:
    nscDxTcpXcelUdpEntry.setStatus("mandatory")


class _NscDxTcpXcelUdpSapId_Type(Integer32):
    """Custom type nscDxTcpXcelUdpSapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NscDxTcpXcelUdpSapId_Type.__name__ = "Integer32"
_NscDxTcpXcelUdpSapId_Object = MibTableColumn
nscDxTcpXcelUdpSapId = _NscDxTcpXcelUdpSapId_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 2, 7, 1, 1),
    _NscDxTcpXcelUdpSapId_Type()
)
nscDxTcpXcelUdpSapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelUdpSapId.setStatus("mandatory")


class _NscDxTcpXcelUdpHostIdx_Type(Integer32):
    """Custom type nscDxTcpXcelUdpHostIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_NscDxTcpXcelUdpHostIdx_Type.__name__ = "Integer32"
_NscDxTcpXcelUdpHostIdx_Object = MibTableColumn
nscDxTcpXcelUdpHostIdx = _NscDxTcpXcelUdpHostIdx_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 2, 7, 1, 2),
    _NscDxTcpXcelUdpHostIdx_Type()
)
nscDxTcpXcelUdpHostIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelUdpHostIdx.setStatus("mandatory")


class _NscDxTcpXcelUdpHostName_Type(DisplayString):
    """Custom type nscDxTcpXcelUdpHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NscDxTcpXcelUdpHostName_Type.__name__ = "DisplayString"
_NscDxTcpXcelUdpHostName_Object = MibTableColumn
nscDxTcpXcelUdpHostName = _NscDxTcpXcelUdpHostName_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 2, 7, 1, 3),
    _NscDxTcpXcelUdpHostName_Type()
)
nscDxTcpXcelUdpHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelUdpHostName.setStatus("mandatory")
_NscDxTcpXcelUdpLocalAddress_Type = IpAddress
_NscDxTcpXcelUdpLocalAddress_Object = MibTableColumn
nscDxTcpXcelUdpLocalAddress = _NscDxTcpXcelUdpLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 2, 7, 1, 4),
    _NscDxTcpXcelUdpLocalAddress_Type()
)
nscDxTcpXcelUdpLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelUdpLocalAddress.setStatus("mandatory")


class _NscDxTcpXcelUdpLocalPort_Type(Integer32):
    """Custom type nscDxTcpXcelUdpLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NscDxTcpXcelUdpLocalPort_Type.__name__ = "Integer32"
_NscDxTcpXcelUdpLocalPort_Object = MibTableColumn
nscDxTcpXcelUdpLocalPort = _NscDxTcpXcelUdpLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3, 6, 2, 7, 1, 5),
    _NscDxTcpXcelUdpLocalPort_Type()
)
nscDxTcpXcelUdpLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscDxTcpXcelUdpLocalPort.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSC-TCP-EXCEL-MIB",
    **{"nscDxTcpXcel": nscDxTcpXcel,
       "nscDxTcpXcelTcp": nscDxTcpXcelTcp,
       "nscDxTcpXcelTcpRtoAlgorithm": nscDxTcpXcelTcpRtoAlgorithm,
       "nscDxTcpXcelTcpRtoMin": nscDxTcpXcelTcpRtoMin,
       "nscDxTcpXcelTcpRtoMax": nscDxTcpXcelTcpRtoMax,
       "nscDxTcpXcelTcpMaxConn": nscDxTcpXcelTcpMaxConn,
       "nscDxTcpXcelTcpActiveOpens": nscDxTcpXcelTcpActiveOpens,
       "nscDxTcpXcelTcpPassiveOpens": nscDxTcpXcelTcpPassiveOpens,
       "nscDxTcpXcelTcpAttemptFails": nscDxTcpXcelTcpAttemptFails,
       "nscDxTcpXcelTcpEstabResets": nscDxTcpXcelTcpEstabResets,
       "nscDxTcpXcelTcpCurrEstab": nscDxTcpXcelTcpCurrEstab,
       "nscDxTcpXcelTcpInSegs": nscDxTcpXcelTcpInSegs,
       "nscDxTcpXcelTcpOutSegs": nscDxTcpXcelTcpOutSegs,
       "nscDxTcpXcelTcpRetransSegs": nscDxTcpXcelTcpRetransSegs,
       "nscDxTcpXcelTcpConnTable": nscDxTcpXcelTcpConnTable,
       "nscDxTcpXcelTcpConnEntry": nscDxTcpXcelTcpConnEntry,
       "nscDxTcpXcelTcpSapId": nscDxTcpXcelTcpSapId,
       "nscDxTcpXcelTcpHostIdx": nscDxTcpXcelTcpHostIdx,
       "nscDxTcpXcelTcpHostName": nscDxTcpXcelTcpHostName,
       "nscDxTcpXcelTcpConnState": nscDxTcpXcelTcpConnState,
       "nscDxTcpXcelTcpConnLocalAddress": nscDxTcpXcelTcpConnLocalAddress,
       "nscDxTcpXcelTcpConnLocalPort": nscDxTcpXcelTcpConnLocalPort,
       "nscDxTcpXcelTcpConnRemAddress": nscDxTcpXcelTcpConnRemAddress,
       "nscDxTcpXcelTcpConnRemPort": nscDxTcpXcelTcpConnRemPort,
       "nscDxTcpXcelTcpInErrs": nscDxTcpXcelTcpInErrs,
       "nscDxTcpXcelTcpOutRsts": nscDxTcpXcelTcpOutRsts,
       "nscDxTcpXcelTcpConnAttempt": nscDxTcpXcelTcpConnAttempt,
       "nscDxTcpXcelTcpClosed": nscDxTcpXcelTcpClosed,
       "nscDxTcpXcelTcpSegsTimed": nscDxTcpXcelTcpSegsTimed,
       "nscDxTcpXcelTcpRttUpdated": nscDxTcpXcelTcpRttUpdated,
       "nscDxTcpXcelTcpDelAck": nscDxTcpXcelTcpDelAck,
       "nscDxTcpXcelTcpTimeoutDrop": nscDxTcpXcelTcpTimeoutDrop,
       "nscDxTcpXcelTcpRexmtTimeo": nscDxTcpXcelTcpRexmtTimeo,
       "nscDxTcpXcelTcpPersistTimeo": nscDxTcpXcelTcpPersistTimeo,
       "nscDxTcpXcelTcpKeepTimeo": nscDxTcpXcelTcpKeepTimeo,
       "nscDxTcpXcelTcpKeepProbe": nscDxTcpXcelTcpKeepProbe,
       "nscDxTcpXcelTcpKeepDrop": nscDxTcpXcelTcpKeepDrop,
       "nscDxTcpXcelTcpSndPack": nscDxTcpXcelTcpSndPack,
       "nscDxTcpXcelTcpSndByte": nscDxTcpXcelTcpSndByte,
       "nscDxTcpXcelTcpSndRexmitPack": nscDxTcpXcelTcpSndRexmitPack,
       "nscDxTcpXcelTcpSndRexmitByte": nscDxTcpXcelTcpSndRexmitByte,
       "nscDxTcpXcelTcpSndAcks": nscDxTcpXcelTcpSndAcks,
       "nscDxTcpXcelTcpSndProbe": nscDxTcpXcelTcpSndProbe,
       "nscDxTcpXcelTcpSndUrg": nscDxTcpXcelTcpSndUrg,
       "nscDxTcpXcelTcpSndWinUp": nscDxTcpXcelTcpSndWinUp,
       "nscDxTcpXcelTcpSndCtrl": nscDxTcpXcelTcpSndCtrl,
       "nscDxTcpXcelTcpPcbCacheMiss": nscDxTcpXcelTcpPcbCacheMiss,
       "nscDxTcpXcelTcpRcvPack": nscDxTcpXcelTcpRcvPack,
       "nscDxTcpXcelTcpRcvBytes": nscDxTcpXcelTcpRcvBytes,
       "nscDxTcpXcelTcpRcvByteAfterWin": nscDxTcpXcelTcpRcvByteAfterWin,
       "nscDxTcpXcelTcpRcvAfterClose": nscDxTcpXcelTcpRcvAfterClose,
       "nscDxTcpXcelTcpRcvWinProbe": nscDxTcpXcelTcpRcvWinProbe,
       "nscDxTcpXcelTcpRcvdUpack": nscDxTcpXcelTcpRcvdUpack,
       "nscDxTcpXcelTcpRcvAckTooMuch": nscDxTcpXcelTcpRcvAckTooMuch,
       "nscDxTcpXcelTcpRcvAckPack": nscDxTcpXcelTcpRcvAckPack,
       "nscDxTcpXcelTcpRcvAckByte": nscDxTcpXcelTcpRcvAckByte,
       "nscDxTcpXcelTcpRcvWinUpd": nscDxTcpXcelTcpRcvWinUpd,
       "nscDxTcpXcelUdp": nscDxTcpXcelUdp,
       "nscDxTcpXcelUdpInDatagrams": nscDxTcpXcelUdpInDatagrams,
       "nscDxTcpXcelUdpNoPorts": nscDxTcpXcelUdpNoPorts,
       "nscDxTcpXcelUdpInErrors": nscDxTcpXcelUdpInErrors,
       "nscDxTcpXcelUdpOutDatagrams": nscDxTcpXcelUdpOutDatagrams,
       "nscDxTcpXcelUdpNoPortBcast": nscDxTcpXcelUdpNoPortBcast,
       "nscDxTcpXcelUdpPcbCacheMissing": nscDxTcpXcelUdpPcbCacheMissing,
       "nscDxTcpXcelUdpTable": nscDxTcpXcelUdpTable,
       "nscDxTcpXcelUdpEntry": nscDxTcpXcelUdpEntry,
       "nscDxTcpXcelUdpSapId": nscDxTcpXcelUdpSapId,
       "nscDxTcpXcelUdpHostIdx": nscDxTcpXcelUdpHostIdx,
       "nscDxTcpXcelUdpHostName": nscDxTcpXcelUdpHostName,
       "nscDxTcpXcelUdpLocalAddress": nscDxTcpXcelUdpLocalAddress,
       "nscDxTcpXcelUdpLocalPort": nscDxTcpXcelUdpLocalPort}
)
