# SNMP MIB module (BIANCA-BRICK-X25STAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-X25STAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:53 2024
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
 enterprises,
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
    "enterprises",
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

_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_X25_ObjectIdentity = ObjectIdentity
x25 = _X25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 6)
)
_X25statMIB_ObjectIdentity = ObjectIdentity
x25statMIB = _X25statMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16)
)
_X25SwStats_ObjectIdentity = ObjectIdentity
x25SwStats = _X25SwStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1)
)
_X25SwIncomingAttempts_Type = Counter32
_X25SwIncomingAttempts_Object = MibScalar
x25SwIncomingAttempts = _X25SwIncomingAttempts_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 1),
    _X25SwIncomingAttempts_Type()
)
x25SwIncomingAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SwIncomingAttempts.setStatus("mandatory")
_X25SwIncomingSucceeded_Type = Counter32
_X25SwIncomingSucceeded_Object = MibScalar
x25SwIncomingSucceeded = _X25SwIncomingSucceeded_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 2),
    _X25SwIncomingSucceeded_Type()
)
x25SwIncomingSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SwIncomingSucceeded.setStatus("mandatory")
_X25SwIncomingFailed_Type = Counter32
_X25SwIncomingFailed_Object = MibScalar
x25SwIncomingFailed = _X25SwIncomingFailed_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 3),
    _X25SwIncomingFailed_Type()
)
x25SwIncomingFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SwIncomingFailed.setStatus("mandatory")
_X25SwIncCurrentCalls_Type = Counter32
_X25SwIncCurrentCalls_Object = MibScalar
x25SwIncCurrentCalls = _X25SwIncCurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 4),
    _X25SwIncCurrentCalls_Type()
)
x25SwIncCurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SwIncCurrentCalls.setStatus("mandatory")
_X25SwIncMaxConcCalls_Type = Counter32
_X25SwIncMaxConcCalls_Object = MibScalar
x25SwIncMaxConcCalls = _X25SwIncMaxConcCalls_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 5),
    _X25SwIncMaxConcCalls_Type()
)
x25SwIncMaxConcCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SwIncMaxConcCalls.setStatus("mandatory")
_X25SwIncCurrentPending_Type = Counter32
_X25SwIncCurrentPending_Object = MibScalar
x25SwIncCurrentPending = _X25SwIncCurrentPending_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 6),
    _X25SwIncCurrentPending_Type()
)
x25SwIncCurrentPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SwIncCurrentPending.setStatus("mandatory")
_X25SwIncMaxConcPending_Type = Counter32
_X25SwIncMaxConcPending_Object = MibScalar
x25SwIncMaxConcPending = _X25SwIncMaxConcPending_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 7),
    _X25SwIncMaxConcPending_Type()
)
x25SwIncMaxConcPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SwIncMaxConcPending.setStatus("mandatory")
_X25SwIncFailedTimeout_Type = Counter32
_X25SwIncFailedTimeout_Object = MibScalar
x25SwIncFailedTimeout = _X25SwIncFailedTimeout_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 8),
    _X25SwIncFailedTimeout_Type()
)
x25SwIncFailedTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SwIncFailedTimeout.setStatus("mandatory")
_X25SwOutgoingAttempts_Type = Counter32
_X25SwOutgoingAttempts_Object = MibScalar
x25SwOutgoingAttempts = _X25SwOutgoingAttempts_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 15),
    _X25SwOutgoingAttempts_Type()
)
x25SwOutgoingAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SwOutgoingAttempts.setStatus("mandatory")
_X25SwOutgoingSucceeded_Type = Counter32
_X25SwOutgoingSucceeded_Object = MibScalar
x25SwOutgoingSucceeded = _X25SwOutgoingSucceeded_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 16),
    _X25SwOutgoingSucceeded_Type()
)
x25SwOutgoingSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SwOutgoingSucceeded.setStatus("mandatory")
_X25SwOutgoingFailed_Type = Counter32
_X25SwOutgoingFailed_Object = MibScalar
x25SwOutgoingFailed = _X25SwOutgoingFailed_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 17),
    _X25SwOutgoingFailed_Type()
)
x25SwOutgoingFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SwOutgoingFailed.setStatus("mandatory")
_X25SwOutCurrentCalls_Type = Counter32
_X25SwOutCurrentCalls_Object = MibScalar
x25SwOutCurrentCalls = _X25SwOutCurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 18),
    _X25SwOutCurrentCalls_Type()
)
x25SwOutCurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SwOutCurrentCalls.setStatus("mandatory")
_X25SwOutMaxConcCalls_Type = Counter32
_X25SwOutMaxConcCalls_Object = MibScalar
x25SwOutMaxConcCalls = _X25SwOutMaxConcCalls_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 19),
    _X25SwOutMaxConcCalls_Type()
)
x25SwOutMaxConcCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SwOutMaxConcCalls.setStatus("mandatory")
_X25SwOutCurrentPending_Type = Counter32
_X25SwOutCurrentPending_Object = MibScalar
x25SwOutCurrentPending = _X25SwOutCurrentPending_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 20),
    _X25SwOutCurrentPending_Type()
)
x25SwOutCurrentPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SwOutCurrentPending.setStatus("mandatory")
_X25SwOutMaxConcPending_Type = Counter32
_X25SwOutMaxConcPending_Object = MibScalar
x25SwOutMaxConcPending = _X25SwOutMaxConcPending_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 21),
    _X25SwOutMaxConcPending_Type()
)
x25SwOutMaxConcPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SwOutMaxConcPending.setStatus("mandatory")
_X25SwOutFailedTimeout_Type = Counter32
_X25SwOutFailedTimeout_Object = MibScalar
x25SwOutFailedTimeout = _X25SwOutFailedTimeout_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 22),
    _X25SwOutFailedTimeout_Type()
)
x25SwOutFailedTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SwOutFailedTimeout.setStatus("mandatory")
_X25SwCallCnt_Type = Counter32
_X25SwCallCnt_Object = MibScalar
x25SwCallCnt = _X25SwCallCnt_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 23),
    _X25SwCallCnt_Type()
)
x25SwCallCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25SwCallCnt.setStatus("mandatory")
_X25MuxStats_ObjectIdentity = ObjectIdentity
x25MuxStats = _X25MuxStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2)
)
_X25MuxIncomingAttempts_Type = Counter32
_X25MuxIncomingAttempts_Object = MibScalar
x25MuxIncomingAttempts = _X25MuxIncomingAttempts_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 1),
    _X25MuxIncomingAttempts_Type()
)
x25MuxIncomingAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25MuxIncomingAttempts.setStatus("mandatory")
_X25MuxIncomingSucceeded_Type = Counter32
_X25MuxIncomingSucceeded_Object = MibScalar
x25MuxIncomingSucceeded = _X25MuxIncomingSucceeded_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 2),
    _X25MuxIncomingSucceeded_Type()
)
x25MuxIncomingSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25MuxIncomingSucceeded.setStatus("mandatory")
_X25MuxIncomingFailed_Type = Counter32
_X25MuxIncomingFailed_Object = MibScalar
x25MuxIncomingFailed = _X25MuxIncomingFailed_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 3),
    _X25MuxIncomingFailed_Type()
)
x25MuxIncomingFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25MuxIncomingFailed.setStatus("mandatory")
_X25MuxIncCurrentCalls_Type = Counter32
_X25MuxIncCurrentCalls_Object = MibScalar
x25MuxIncCurrentCalls = _X25MuxIncCurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 4),
    _X25MuxIncCurrentCalls_Type()
)
x25MuxIncCurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25MuxIncCurrentCalls.setStatus("mandatory")
_X25MuxIncMaxConcCalls_Type = Counter32
_X25MuxIncMaxConcCalls_Object = MibScalar
x25MuxIncMaxConcCalls = _X25MuxIncMaxConcCalls_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 5),
    _X25MuxIncMaxConcCalls_Type()
)
x25MuxIncMaxConcCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25MuxIncMaxConcCalls.setStatus("mandatory")
_X25MuxIncCurrentPending_Type = Counter32
_X25MuxIncCurrentPending_Object = MibScalar
x25MuxIncCurrentPending = _X25MuxIncCurrentPending_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 6),
    _X25MuxIncCurrentPending_Type()
)
x25MuxIncCurrentPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25MuxIncCurrentPending.setStatus("mandatory")
_X25MuxIncMaxConcPending_Type = Counter32
_X25MuxIncMaxConcPending_Object = MibScalar
x25MuxIncMaxConcPending = _X25MuxIncMaxConcPending_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 7),
    _X25MuxIncMaxConcPending_Type()
)
x25MuxIncMaxConcPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25MuxIncMaxConcPending.setStatus("mandatory")
_X25MuxIncResets_Type = Counter32
_X25MuxIncResets_Object = MibScalar
x25MuxIncResets = _X25MuxIncResets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 8),
    _X25MuxIncResets_Type()
)
x25MuxIncResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25MuxIncResets.setStatus("mandatory")
_X25MuxOutgoingAttempts_Type = Counter32
_X25MuxOutgoingAttempts_Object = MibScalar
x25MuxOutgoingAttempts = _X25MuxOutgoingAttempts_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 15),
    _X25MuxOutgoingAttempts_Type()
)
x25MuxOutgoingAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25MuxOutgoingAttempts.setStatus("mandatory")
_X25MuxOutgoingSucceeded_Type = Counter32
_X25MuxOutgoingSucceeded_Object = MibScalar
x25MuxOutgoingSucceeded = _X25MuxOutgoingSucceeded_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 16),
    _X25MuxOutgoingSucceeded_Type()
)
x25MuxOutgoingSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25MuxOutgoingSucceeded.setStatus("mandatory")
_X25MuxOutgoingFailed_Type = Counter32
_X25MuxOutgoingFailed_Object = MibScalar
x25MuxOutgoingFailed = _X25MuxOutgoingFailed_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 17),
    _X25MuxOutgoingFailed_Type()
)
x25MuxOutgoingFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25MuxOutgoingFailed.setStatus("mandatory")
_X25MuxOutCurrentCalls_Type = Counter32
_X25MuxOutCurrentCalls_Object = MibScalar
x25MuxOutCurrentCalls = _X25MuxOutCurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 18),
    _X25MuxOutCurrentCalls_Type()
)
x25MuxOutCurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25MuxOutCurrentCalls.setStatus("mandatory")
_X25MuxOutMaxConcCalls_Type = Counter32
_X25MuxOutMaxConcCalls_Object = MibScalar
x25MuxOutMaxConcCalls = _X25MuxOutMaxConcCalls_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 19),
    _X25MuxOutMaxConcCalls_Type()
)
x25MuxOutMaxConcCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25MuxOutMaxConcCalls.setStatus("mandatory")
_X25MuxOutCurrentPending_Type = Counter32
_X25MuxOutCurrentPending_Object = MibScalar
x25MuxOutCurrentPending = _X25MuxOutCurrentPending_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 20),
    _X25MuxOutCurrentPending_Type()
)
x25MuxOutCurrentPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25MuxOutCurrentPending.setStatus("mandatory")
_X25MuxOutMaxConcPending_Type = Counter32
_X25MuxOutMaxConcPending_Object = MibScalar
x25MuxOutMaxConcPending = _X25MuxOutMaxConcPending_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 21),
    _X25MuxOutMaxConcPending_Type()
)
x25MuxOutMaxConcPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25MuxOutMaxConcPending.setStatus("mandatory")
_X25MuxOutResets_Type = Counter32
_X25MuxOutResets_Object = MibScalar
x25MuxOutResets = _X25MuxOutResets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 22),
    _X25MuxOutResets_Type()
)
x25MuxOutResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25MuxOutResets.setStatus("mandatory")
_X25MuxInstCnt_Type = Counter32
_X25MuxInstCnt_Object = MibScalar
x25MuxInstCnt = _X25MuxInstCnt_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 23),
    _X25MuxInstCnt_Type()
)
x25MuxInstCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25MuxInstCnt.setStatus("mandatory")
_X25ToTcpStats_ObjectIdentity = ObjectIdentity
x25ToTcpStats = _X25ToTcpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3)
)


class _X25ToTcpRestart_Type(Integer32):
    """Custom type x25ToTcpRestart based on Integer32"""
    defaultValue = 2

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


_X25ToTcpRestart_Type.__name__ = "Integer32"
_X25ToTcpRestart_Object = MibScalar
x25ToTcpRestart = _X25ToTcpRestart_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 1),
    _X25ToTcpRestart_Type()
)
x25ToTcpRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25ToTcpRestart.setStatus("mandatory")
_X25ToTcpCurrentRestart_Type = Counter32
_X25ToTcpCurrentRestart_Object = MibScalar
x25ToTcpCurrentRestart = _X25ToTcpCurrentRestart_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 2),
    _X25ToTcpCurrentRestart_Type()
)
x25ToTcpCurrentRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpCurrentRestart.setStatus("mandatory")
_X25ToTcpTotalRestart_Type = Counter32
_X25ToTcpTotalRestart_Object = MibScalar
x25ToTcpTotalRestart = _X25ToTcpTotalRestart_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 3),
    _X25ToTcpTotalRestart_Type()
)
x25ToTcpTotalRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpTotalRestart.setStatus("mandatory")
_X25ToTcpIncX25Attempts_Type = Counter32
_X25ToTcpIncX25Attempts_Object = MibScalar
x25ToTcpIncX25Attempts = _X25ToTcpIncX25Attempts_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 4),
    _X25ToTcpIncX25Attempts_Type()
)
x25ToTcpIncX25Attempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpIncX25Attempts.setStatus("mandatory")
_X25ToTcpIncX25Succeeded_Type = Counter32
_X25ToTcpIncX25Succeeded_Object = MibScalar
x25ToTcpIncX25Succeeded = _X25ToTcpIncX25Succeeded_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 5),
    _X25ToTcpIncX25Succeeded_Type()
)
x25ToTcpIncX25Succeeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpIncX25Succeeded.setStatus("mandatory")
_X25ToTcpIncX25Failed_Type = Counter32
_X25ToTcpIncX25Failed_Object = MibScalar
x25ToTcpIncX25Failed = _X25ToTcpIncX25Failed_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 6),
    _X25ToTcpIncX25Failed_Type()
)
x25ToTcpIncX25Failed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpIncX25Failed.setStatus("mandatory")
_X25ToTcpOutTcpAttempts_Type = Counter32
_X25ToTcpOutTcpAttempts_Object = MibScalar
x25ToTcpOutTcpAttempts = _X25ToTcpOutTcpAttempts_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 7),
    _X25ToTcpOutTcpAttempts_Type()
)
x25ToTcpOutTcpAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpOutTcpAttempts.setStatus("mandatory")
_X25ToTcpOutTcpSucceeded_Type = Counter32
_X25ToTcpOutTcpSucceeded_Object = MibScalar
x25ToTcpOutTcpSucceeded = _X25ToTcpOutTcpSucceeded_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 8),
    _X25ToTcpOutTcpSucceeded_Type()
)
x25ToTcpOutTcpSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpOutTcpSucceeded.setStatus("mandatory")
_X25ToTcpOutTcpFailed_Type = Counter32
_X25ToTcpOutTcpFailed_Object = MibScalar
x25ToTcpOutTcpFailed = _X25ToTcpOutTcpFailed_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 9),
    _X25ToTcpOutTcpFailed_Type()
)
x25ToTcpOutTcpFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpOutTcpFailed.setStatus("mandatory")
_X25ToTcpIncX25CurrentCalls_Type = Counter32
_X25ToTcpIncX25CurrentCalls_Object = MibScalar
x25ToTcpIncX25CurrentCalls = _X25ToTcpIncX25CurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 10),
    _X25ToTcpIncX25CurrentCalls_Type()
)
x25ToTcpIncX25CurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpIncX25CurrentCalls.setStatus("mandatory")
_X25ToTcpIncX25MaxConcCalls_Type = Counter32
_X25ToTcpIncX25MaxConcCalls_Object = MibScalar
x25ToTcpIncX25MaxConcCalls = _X25ToTcpIncX25MaxConcCalls_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 11),
    _X25ToTcpIncX25MaxConcCalls_Type()
)
x25ToTcpIncX25MaxConcCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpIncX25MaxConcCalls.setStatus("mandatory")
_X25ToTcpIncX25CurrentPending_Type = Counter32
_X25ToTcpIncX25CurrentPending_Object = MibScalar
x25ToTcpIncX25CurrentPending = _X25ToTcpIncX25CurrentPending_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 12),
    _X25ToTcpIncX25CurrentPending_Type()
)
x25ToTcpIncX25CurrentPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpIncX25CurrentPending.setStatus("mandatory")
_X25ToTcpIncX25MaxConcPending_Type = Counter32
_X25ToTcpIncX25MaxConcPending_Object = MibScalar
x25ToTcpIncX25MaxConcPending = _X25ToTcpIncX25MaxConcPending_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 13),
    _X25ToTcpIncX25MaxConcPending_Type()
)
x25ToTcpIncX25MaxConcPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpIncX25MaxConcPending.setStatus("mandatory")
_X25ToTcpIncTcpAttempts_Type = Counter32
_X25ToTcpIncTcpAttempts_Object = MibScalar
x25ToTcpIncTcpAttempts = _X25ToTcpIncTcpAttempts_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 14),
    _X25ToTcpIncTcpAttempts_Type()
)
x25ToTcpIncTcpAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpIncTcpAttempts.setStatus("mandatory")
_X25ToTcpIncTcpSucceeded_Type = Counter32
_X25ToTcpIncTcpSucceeded_Object = MibScalar
x25ToTcpIncTcpSucceeded = _X25ToTcpIncTcpSucceeded_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 15),
    _X25ToTcpIncTcpSucceeded_Type()
)
x25ToTcpIncTcpSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpIncTcpSucceeded.setStatus("mandatory")
_X25ToTcpIncTcpFailed_Type = Counter32
_X25ToTcpIncTcpFailed_Object = MibScalar
x25ToTcpIncTcpFailed = _X25ToTcpIncTcpFailed_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 16),
    _X25ToTcpIncTcpFailed_Type()
)
x25ToTcpIncTcpFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpIncTcpFailed.setStatus("mandatory")
_X25ToTcpOutX25Attempts_Type = Counter32
_X25ToTcpOutX25Attempts_Object = MibScalar
x25ToTcpOutX25Attempts = _X25ToTcpOutX25Attempts_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 17),
    _X25ToTcpOutX25Attempts_Type()
)
x25ToTcpOutX25Attempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpOutX25Attempts.setStatus("mandatory")
_X25ToTcpOutX25Succeeded_Type = Counter32
_X25ToTcpOutX25Succeeded_Object = MibScalar
x25ToTcpOutX25Succeeded = _X25ToTcpOutX25Succeeded_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 18),
    _X25ToTcpOutX25Succeeded_Type()
)
x25ToTcpOutX25Succeeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpOutX25Succeeded.setStatus("mandatory")
_X25ToTcpOutX25Failed_Type = Counter32
_X25ToTcpOutX25Failed_Object = MibScalar
x25ToTcpOutX25Failed = _X25ToTcpOutX25Failed_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 19),
    _X25ToTcpOutX25Failed_Type()
)
x25ToTcpOutX25Failed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpOutX25Failed.setStatus("mandatory")
_X25ToTcpIncTcpCurrentCalls_Type = Counter32
_X25ToTcpIncTcpCurrentCalls_Object = MibScalar
x25ToTcpIncTcpCurrentCalls = _X25ToTcpIncTcpCurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 20),
    _X25ToTcpIncTcpCurrentCalls_Type()
)
x25ToTcpIncTcpCurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpIncTcpCurrentCalls.setStatus("mandatory")
_X25ToTcpIncTcpMaxConcCalls_Type = Counter32
_X25ToTcpIncTcpMaxConcCalls_Object = MibScalar
x25ToTcpIncTcpMaxConcCalls = _X25ToTcpIncTcpMaxConcCalls_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 21),
    _X25ToTcpIncTcpMaxConcCalls_Type()
)
x25ToTcpIncTcpMaxConcCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpIncTcpMaxConcCalls.setStatus("mandatory")
_X25ToTcpIncTcpCurrentPending_Type = Counter32
_X25ToTcpIncTcpCurrentPending_Object = MibScalar
x25ToTcpIncTcpCurrentPending = _X25ToTcpIncTcpCurrentPending_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 22),
    _X25ToTcpIncTcpCurrentPending_Type()
)
x25ToTcpIncTcpCurrentPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpIncTcpCurrentPending.setStatus("mandatory")
_X25ToTcpIncTcpMaxConcPending_Type = Counter32
_X25ToTcpIncTcpMaxConcPending_Object = MibScalar
x25ToTcpIncTcpMaxConcPending = _X25ToTcpIncTcpMaxConcPending_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 23),
    _X25ToTcpIncTcpMaxConcPending_Type()
)
x25ToTcpIncTcpMaxConcPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpIncTcpMaxConcPending.setStatus("mandatory")
_X25ToTcpUEvTcpListen_Type = Counter32
_X25ToTcpUEvTcpListen_Object = MibScalar
x25ToTcpUEvTcpListen = _X25ToTcpUEvTcpListen_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 24),
    _X25ToTcpUEvTcpListen_Type()
)
x25ToTcpUEvTcpListen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpUEvTcpListen.setStatus("mandatory")
_X25ToTcpUEvTcpData_Type = Counter32
_X25ToTcpUEvTcpData_Object = MibScalar
x25ToTcpUEvTcpData = _X25ToTcpUEvTcpData_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 25),
    _X25ToTcpUEvTcpData_Type()
)
x25ToTcpUEvTcpData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpUEvTcpData.setStatus("mandatory")
_X25ToTcpUEvX25Listen_Type = Counter32
_X25ToTcpUEvX25Listen_Object = MibScalar
x25ToTcpUEvX25Listen = _X25ToTcpUEvX25Listen_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 26),
    _X25ToTcpUEvX25Listen_Type()
)
x25ToTcpUEvX25Listen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpUEvX25Listen.setStatus("mandatory")
_X25ToTcpUEvX25Data_Type = Counter32
_X25ToTcpUEvX25Data_Object = MibScalar
x25ToTcpUEvX25Data = _X25ToTcpUEvX25Data_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 27),
    _X25ToTcpUEvX25Data_Type()
)
x25ToTcpUEvX25Data.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpUEvX25Data.setStatus("mandatory")
_X25ToTcpX25CanPutEvDisc_Type = Counter32
_X25ToTcpX25CanPutEvDisc_Object = MibScalar
x25ToTcpX25CanPutEvDisc = _X25ToTcpX25CanPutEvDisc_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 28),
    _X25ToTcpX25CanPutEvDisc_Type()
)
x25ToTcpX25CanPutEvDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpX25CanPutEvDisc.setStatus("mandatory")
_X25ToTcpX25CanPutEvTok_Type = Counter32
_X25ToTcpX25CanPutEvTok_Object = MibScalar
x25ToTcpX25CanPutEvTok = _X25ToTcpX25CanPutEvTok_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 29),
    _X25ToTcpX25CanPutEvTok_Type()
)
x25ToTcpX25CanPutEvTok.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpX25CanPutEvTok.setStatus("mandatory")
_X25ToTcpX25CanPutEvReset_Type = Counter32
_X25ToTcpX25CanPutEvReset_Object = MibScalar
x25ToTcpX25CanPutEvReset = _X25ToTcpX25CanPutEvReset_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 30),
    _X25ToTcpX25CanPutEvReset_Type()
)
x25ToTcpX25CanPutEvReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpX25CanPutEvReset.setStatus("mandatory")
_X25ToTcpTcpCanPutEvDisc_Type = Counter32
_X25ToTcpTcpCanPutEvDisc_Object = MibScalar
x25ToTcpTcpCanPutEvDisc = _X25ToTcpTcpCanPutEvDisc_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 31),
    _X25ToTcpTcpCanPutEvDisc_Type()
)
x25ToTcpTcpCanPutEvDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpTcpCanPutEvDisc.setStatus("mandatory")
_X25ToTcpTcpCanPutEvTok_Type = Counter32
_X25ToTcpTcpCanPutEvTok_Object = MibScalar
x25ToTcpTcpCanPutEvTok = _X25ToTcpTcpCanPutEvTok_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 32),
    _X25ToTcpTcpCanPutEvTok_Type()
)
x25ToTcpTcpCanPutEvTok.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25ToTcpTcpCanPutEvTok.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-X25STAT-MIB",
    **{"bintec": bintec,
       "bibo": bibo,
       "x25": x25,
       "x25statMIB": x25statMIB,
       "x25SwStats": x25SwStats,
       "x25SwIncomingAttempts": x25SwIncomingAttempts,
       "x25SwIncomingSucceeded": x25SwIncomingSucceeded,
       "x25SwIncomingFailed": x25SwIncomingFailed,
       "x25SwIncCurrentCalls": x25SwIncCurrentCalls,
       "x25SwIncMaxConcCalls": x25SwIncMaxConcCalls,
       "x25SwIncCurrentPending": x25SwIncCurrentPending,
       "x25SwIncMaxConcPending": x25SwIncMaxConcPending,
       "x25SwIncFailedTimeout": x25SwIncFailedTimeout,
       "x25SwOutgoingAttempts": x25SwOutgoingAttempts,
       "x25SwOutgoingSucceeded": x25SwOutgoingSucceeded,
       "x25SwOutgoingFailed": x25SwOutgoingFailed,
       "x25SwOutCurrentCalls": x25SwOutCurrentCalls,
       "x25SwOutMaxConcCalls": x25SwOutMaxConcCalls,
       "x25SwOutCurrentPending": x25SwOutCurrentPending,
       "x25SwOutMaxConcPending": x25SwOutMaxConcPending,
       "x25SwOutFailedTimeout": x25SwOutFailedTimeout,
       "x25SwCallCnt": x25SwCallCnt,
       "x25MuxStats": x25MuxStats,
       "x25MuxIncomingAttempts": x25MuxIncomingAttempts,
       "x25MuxIncomingSucceeded": x25MuxIncomingSucceeded,
       "x25MuxIncomingFailed": x25MuxIncomingFailed,
       "x25MuxIncCurrentCalls": x25MuxIncCurrentCalls,
       "x25MuxIncMaxConcCalls": x25MuxIncMaxConcCalls,
       "x25MuxIncCurrentPending": x25MuxIncCurrentPending,
       "x25MuxIncMaxConcPending": x25MuxIncMaxConcPending,
       "x25MuxIncResets": x25MuxIncResets,
       "x25MuxOutgoingAttempts": x25MuxOutgoingAttempts,
       "x25MuxOutgoingSucceeded": x25MuxOutgoingSucceeded,
       "x25MuxOutgoingFailed": x25MuxOutgoingFailed,
       "x25MuxOutCurrentCalls": x25MuxOutCurrentCalls,
       "x25MuxOutMaxConcCalls": x25MuxOutMaxConcCalls,
       "x25MuxOutCurrentPending": x25MuxOutCurrentPending,
       "x25MuxOutMaxConcPending": x25MuxOutMaxConcPending,
       "x25MuxOutResets": x25MuxOutResets,
       "x25MuxInstCnt": x25MuxInstCnt,
       "x25ToTcpStats": x25ToTcpStats,
       "x25ToTcpRestart": x25ToTcpRestart,
       "x25ToTcpCurrentRestart": x25ToTcpCurrentRestart,
       "x25ToTcpTotalRestart": x25ToTcpTotalRestart,
       "x25ToTcpIncX25Attempts": x25ToTcpIncX25Attempts,
       "x25ToTcpIncX25Succeeded": x25ToTcpIncX25Succeeded,
       "x25ToTcpIncX25Failed": x25ToTcpIncX25Failed,
       "x25ToTcpOutTcpAttempts": x25ToTcpOutTcpAttempts,
       "x25ToTcpOutTcpSucceeded": x25ToTcpOutTcpSucceeded,
       "x25ToTcpOutTcpFailed": x25ToTcpOutTcpFailed,
       "x25ToTcpIncX25CurrentCalls": x25ToTcpIncX25CurrentCalls,
       "x25ToTcpIncX25MaxConcCalls": x25ToTcpIncX25MaxConcCalls,
       "x25ToTcpIncX25CurrentPending": x25ToTcpIncX25CurrentPending,
       "x25ToTcpIncX25MaxConcPending": x25ToTcpIncX25MaxConcPending,
       "x25ToTcpIncTcpAttempts": x25ToTcpIncTcpAttempts,
       "x25ToTcpIncTcpSucceeded": x25ToTcpIncTcpSucceeded,
       "x25ToTcpIncTcpFailed": x25ToTcpIncTcpFailed,
       "x25ToTcpOutX25Attempts": x25ToTcpOutX25Attempts,
       "x25ToTcpOutX25Succeeded": x25ToTcpOutX25Succeeded,
       "x25ToTcpOutX25Failed": x25ToTcpOutX25Failed,
       "x25ToTcpIncTcpCurrentCalls": x25ToTcpIncTcpCurrentCalls,
       "x25ToTcpIncTcpMaxConcCalls": x25ToTcpIncTcpMaxConcCalls,
       "x25ToTcpIncTcpCurrentPending": x25ToTcpIncTcpCurrentPending,
       "x25ToTcpIncTcpMaxConcPending": x25ToTcpIncTcpMaxConcPending,
       "x25ToTcpUEvTcpListen": x25ToTcpUEvTcpListen,
       "x25ToTcpUEvTcpData": x25ToTcpUEvTcpData,
       "x25ToTcpUEvX25Listen": x25ToTcpUEvX25Listen,
       "x25ToTcpUEvX25Data": x25ToTcpUEvX25Data,
       "x25ToTcpX25CanPutEvDisc": x25ToTcpX25CanPutEvDisc,
       "x25ToTcpX25CanPutEvTok": x25ToTcpX25CanPutEvTok,
       "x25ToTcpX25CanPutEvReset": x25ToTcpX25CanPutEvReset,
       "x25ToTcpTcpCanPutEvDisc": x25ToTcpTcpCanPutEvDisc,
       "x25ToTcpTcpCanPutEvTok": x25ToTcpTcpCanPutEvTok}
)
