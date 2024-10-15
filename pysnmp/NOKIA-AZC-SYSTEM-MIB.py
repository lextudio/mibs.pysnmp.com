# SNMP MIB module (NOKIA-AZC-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOKIA-AZC-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:34 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nokia_ObjectIdentity = ObjectIdentity
nokia = _Nokia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94)
)
_NokiaProducts_ObjectIdentity = ObjectIdentity
nokiaProducts = _NokiaProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1)
)
_AzcProducts_ObjectIdentity = ObjectIdentity
azcProducts = _AzcProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 32)
)
_AzcSystem_ObjectIdentity = ObjectIdentity
azcSystem = _AzcSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2)
)
_AzcStatusGroup_ObjectIdentity = ObjectIdentity
azcStatusGroup = _AzcStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1)
)
_AzcVersion_Type = DisplayString
_AzcVersion_Object = MibScalar
azcVersion = _AzcVersion_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 1),
    _AzcVersion_Type()
)
azcVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcVersion.setStatus("mandatory")
_AzcRelease_Type = Integer32
_AzcRelease_Object = MibScalar
azcRelease = _AzcRelease_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 2),
    _AzcRelease_Type()
)
azcRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcRelease.setStatus("mandatory")
_AzcStarted_Type = DisplayString
_AzcStarted_Object = MibScalar
azcStarted = _AzcStarted_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 3),
    _AzcStarted_Type()
)
azcStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcStarted.setStatus("mandatory")
_AzcLoginsSuccess_Type = Counter32
_AzcLoginsSuccess_Object = MibScalar
azcLoginsSuccess = _AzcLoginsSuccess_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 4),
    _AzcLoginsSuccess_Type()
)
azcLoginsSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcLoginsSuccess.setStatus("mandatory")
_AzcLoginsAuthFailures_Type = Counter32
_AzcLoginsAuthFailures_Object = MibScalar
azcLoginsAuthFailures = _AzcLoginsAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 5),
    _AzcLoginsAuthFailures_Type()
)
azcLoginsAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcLoginsAuthFailures.setStatus("mandatory")
_AzcLoginsACLFailures_Type = Counter32
_AzcLoginsACLFailures_Object = MibScalar
azcLoginsACLFailures = _AzcLoginsACLFailures_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 6),
    _AzcLoginsACLFailures_Type()
)
azcLoginsACLFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcLoginsACLFailures.setStatus("mandatory")
_AzcLoginsDuplFailures_Type = Counter32
_AzcLoginsDuplFailures_Object = MibScalar
azcLoginsDuplFailures = _AzcLoginsDuplFailures_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 7),
    _AzcLoginsDuplFailures_Type()
)
azcLoginsDuplFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcLoginsDuplFailures.setStatus("mandatory")
_AzcLoginsSpaceFailures_Type = Counter32
_AzcLoginsSpaceFailures_Object = MibScalar
azcLoginsSpaceFailures = _AzcLoginsSpaceFailures_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 8),
    _AzcLoginsSpaceFailures_Type()
)
azcLoginsSpaceFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcLoginsSpaceFailures.setStatus("mandatory")
_AzcLoginsRADIUSFailures_Type = Counter32
_AzcLoginsRADIUSFailures_Object = MibScalar
azcLoginsRADIUSFailures = _AzcLoginsRADIUSFailures_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 9),
    _AzcLoginsRADIUSFailures_Type()
)
azcLoginsRADIUSFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcLoginsRADIUSFailures.setStatus("mandatory")
_AzcLoginsRADIUSACLFailures_Type = Counter32
_AzcLoginsRADIUSACLFailures_Object = MibScalar
azcLoginsRADIUSACLFailures = _AzcLoginsRADIUSACLFailures_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 10),
    _AzcLoginsRADIUSACLFailures_Type()
)
azcLoginsRADIUSACLFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcLoginsRADIUSACLFailures.setStatus("mandatory")
_AzcAutologoffsRADIUS_Type = Counter32
_AzcAutologoffsRADIUS_Object = MibScalar
azcAutologoffsRADIUS = _AzcAutologoffsRADIUS_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 11),
    _AzcAutologoffsRADIUS_Type()
)
azcAutologoffsRADIUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcAutologoffsRADIUS.setStatus("mandatory")
_AzcAutologoffsPing_Type = Counter32
_AzcAutologoffsPing_Object = MibScalar
azcAutologoffsPing = _AzcAutologoffsPing_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 12),
    _AzcAutologoffsPing_Type()
)
azcAutologoffsPing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcAutologoffsPing.setStatus("mandatory")
_AzcAutologoffsMAC_Type = Counter32
_AzcAutologoffsMAC_Object = MibScalar
azcAutologoffsMAC = _AzcAutologoffsMAC_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 13),
    _AzcAutologoffsMAC_Type()
)
azcAutologoffsMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcAutologoffsMAC.setStatus("mandatory")
_AzcAutologoffsACL_Type = Counter32
_AzcAutologoffsACL_Object = MibScalar
azcAutologoffsACL = _AzcAutologoffsACL_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 14),
    _AzcAutologoffsACL_Type()
)
azcAutologoffsACL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcAutologoffsACL.setStatus("mandatory")
_AzcAutologoffsQuota_Type = Counter32
_AzcAutologoffsQuota_Object = MibScalar
azcAutologoffsQuota = _AzcAutologoffsQuota_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 15),
    _AzcAutologoffsQuota_Type()
)
azcAutologoffsQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcAutologoffsQuota.setStatus("mandatory")
_AzcAutologoffsMaxTime_Type = Counter32
_AzcAutologoffsMaxTime_Object = MibScalar
azcAutologoffsMaxTime = _AzcAutologoffsMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 16),
    _AzcAutologoffsMaxTime_Type()
)
azcAutologoffsMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcAutologoffsMaxTime.setStatus("mandatory")
_AzcAutologoffsIdletimer_Type = Counter32
_AzcAutologoffsIdletimer_Object = MibScalar
azcAutologoffsIdletimer = _AzcAutologoffsIdletimer_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 17),
    _AzcAutologoffsIdletimer_Type()
)
azcAutologoffsIdletimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcAutologoffsIdletimer.setStatus("mandatory")
_AzcPktsIntIn_Type = Counter32
_AzcPktsIntIn_Object = MibScalar
azcPktsIntIn = _AzcPktsIntIn_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 18),
    _AzcPktsIntIn_Type()
)
azcPktsIntIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcPktsIntIn.setStatus("mandatory")
_AzcPktsIntOut_Type = Counter32
_AzcPktsIntOut_Object = MibScalar
azcPktsIntOut = _AzcPktsIntOut_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 19),
    _AzcPktsIntOut_Type()
)
azcPktsIntOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcPktsIntOut.setStatus("mandatory")
_AzcBytesIntIn_Type = Counter32
_AzcBytesIntIn_Object = MibScalar
azcBytesIntIn = _AzcBytesIntIn_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 20),
    _AzcBytesIntIn_Type()
)
azcBytesIntIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcBytesIntIn.setStatus("mandatory")
_AzcBytesIntOut_Type = Counter32
_AzcBytesIntOut_Object = MibScalar
azcBytesIntOut = _AzcBytesIntOut_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 21),
    _AzcBytesIntOut_Type()
)
azcBytesIntOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcBytesIntOut.setStatus("mandatory")
_AzcPktsExtIn_Type = Counter32
_AzcPktsExtIn_Object = MibScalar
azcPktsExtIn = _AzcPktsExtIn_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 22),
    _AzcPktsExtIn_Type()
)
azcPktsExtIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcPktsExtIn.setStatus("mandatory")
_AzcPktsExtOut_Type = Counter32
_AzcPktsExtOut_Object = MibScalar
azcPktsExtOut = _AzcPktsExtOut_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 23),
    _AzcPktsExtOut_Type()
)
azcPktsExtOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcPktsExtOut.setStatus("mandatory")
_AzcBytesExtIn_Type = Counter32
_AzcBytesExtIn_Object = MibScalar
azcBytesExtIn = _AzcBytesExtIn_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 24),
    _AzcBytesExtIn_Type()
)
azcBytesExtIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcBytesExtIn.setStatus("mandatory")
_AzcBytesExtOut_Type = Counter32
_AzcBytesExtOut_Object = MibScalar
azcBytesExtOut = _AzcBytesExtOut_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 25),
    _AzcBytesExtOut_Type()
)
azcBytesExtOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcBytesExtOut.setStatus("mandatory")
_AzcPktsNattedIn_Type = Counter32
_AzcPktsNattedIn_Object = MibScalar
azcPktsNattedIn = _AzcPktsNattedIn_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 26),
    _AzcPktsNattedIn_Type()
)
azcPktsNattedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcPktsNattedIn.setStatus("mandatory")
_AzcPktsNattedOut_Type = Counter32
_AzcPktsNattedOut_Object = MibScalar
azcPktsNattedOut = _AzcPktsNattedOut_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 27),
    _AzcPktsNattedOut_Type()
)
azcPktsNattedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcPktsNattedOut.setStatus("mandatory")
_AzcBytesNattedIn_Type = Counter32
_AzcBytesNattedIn_Object = MibScalar
azcBytesNattedIn = _AzcBytesNattedIn_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 28),
    _AzcBytesNattedIn_Type()
)
azcBytesNattedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcBytesNattedIn.setStatus("mandatory")
_AzcBytesNattedOut_Type = Counter32
_AzcBytesNattedOut_Object = MibScalar
azcBytesNattedOut = _AzcBytesNattedOut_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 29),
    _AzcBytesNattedOut_Type()
)
azcBytesNattedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcBytesNattedOut.setStatus("mandatory")
_AzcPktsNattedErrIn_Type = Counter32
_AzcPktsNattedErrIn_Object = MibScalar
azcPktsNattedErrIn = _AzcPktsNattedErrIn_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 30),
    _AzcPktsNattedErrIn_Type()
)
azcPktsNattedErrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcPktsNattedErrIn.setStatus("mandatory")
_AzcPktsNattedErrOut_Type = Counter32
_AzcPktsNattedErrOut_Object = MibScalar
azcPktsNattedErrOut = _AzcPktsNattedErrOut_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 31),
    _AzcPktsNattedErrOut_Type()
)
azcPktsNattedErrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcPktsNattedErrOut.setStatus("mandatory")
_AzcBytesNattedErrIn_Type = Counter32
_AzcBytesNattedErrIn_Object = MibScalar
azcBytesNattedErrIn = _AzcBytesNattedErrIn_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 32),
    _AzcBytesNattedErrIn_Type()
)
azcBytesNattedErrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcBytesNattedErrIn.setStatus("mandatory")
_AzcBytesNattedErrOut_Type = Counter32
_AzcBytesNattedErrOut_Object = MibScalar
azcBytesNattedErrOut = _AzcBytesNattedErrOut_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 33),
    _AzcBytesNattedErrOut_Type()
)
azcBytesNattedErrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcBytesNattedErrOut.setStatus("mandatory")
_AzcPktsRejInt_Type = Counter32
_AzcPktsRejInt_Object = MibScalar
azcPktsRejInt = _AzcPktsRejInt_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 34),
    _AzcPktsRejInt_Type()
)
azcPktsRejInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcPktsRejInt.setStatus("mandatory")
_AzcPktsRejExt_Type = Counter32
_AzcPktsRejExt_Object = MibScalar
azcPktsRejExt = _AzcPktsRejExt_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 35),
    _AzcPktsRejExt_Type()
)
azcPktsRejExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcPktsRejExt.setStatus("mandatory")
_AzcBytesRejInt_Type = Counter32
_AzcBytesRejInt_Object = MibScalar
azcBytesRejInt = _AzcBytesRejInt_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 36),
    _AzcBytesRejInt_Type()
)
azcBytesRejInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcBytesRejInt.setStatus("mandatory")
_AzcBytesRejExt_Type = Counter32
_AzcBytesRejExt_Object = MibScalar
azcBytesRejExt = _AzcBytesRejExt_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 37),
    _AzcBytesRejExt_Type()
)
azcBytesRejExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcBytesRejExt.setStatus("mandatory")
_AzcACLSelectErr_Type = Counter32
_AzcACLSelectErr_Object = MibScalar
azcACLSelectErr = _AzcACLSelectErr_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 38),
    _AzcACLSelectErr_Type()
)
azcACLSelectErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcACLSelectErr.setStatus("mandatory")
_AzcACLSendmsgErr_Type = Counter32
_AzcACLSendmsgErr_Object = MibScalar
azcACLSendmsgErr = _AzcACLSendmsgErr_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 39),
    _AzcACLSendmsgErr_Type()
)
azcACLSendmsgErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcACLSendmsgErr.setStatus("mandatory")
_AzcACLRevmsgErr_Type = Counter32
_AzcACLRevmsgErr_Object = MibScalar
azcACLRevmsgErr = _AzcACLRevmsgErr_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 40),
    _AzcACLRevmsgErr_Type()
)
azcACLRevmsgErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcACLRevmsgErr.setStatus("mandatory")
_AzcACLRevmsgOverflow_Type = Counter32
_AzcACLRevmsgOverflow_Object = MibScalar
azcACLRevmsgOverflow = _AzcACLRevmsgOverflow_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 41),
    _AzcACLRevmsgOverflow_Type()
)
azcACLRevmsgOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcACLRevmsgOverflow.setStatus("mandatory")
_AzcACLSendmsgLocErr_Type = Counter32
_AzcACLSendmsgLocErr_Object = MibScalar
azcACLSendmsgLocErr = _AzcACLSendmsgLocErr_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 42),
    _AzcACLSendmsgLocErr_Type()
)
azcACLSendmsgLocErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcACLSendmsgLocErr.setStatus("mandatory")
_AzcACLRevmsgLocErr_Type = Counter32
_AzcACLRevmsgLocErr_Object = MibScalar
azcACLRevmsgLocErr = _AzcACLRevmsgLocErr_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 43),
    _AzcACLRevmsgLocErr_Type()
)
azcACLRevmsgLocErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcACLRevmsgLocErr.setStatus("mandatory")
_AzcACLRevmsgLocOverflow_Type = Counter32
_AzcACLRevmsgLocOverflow_Object = MibScalar
azcACLRevmsgLocOverflow = _AzcACLRevmsgLocOverflow_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 44),
    _AzcACLRevmsgLocOverflow_Type()
)
azcACLRevmsgLocOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcACLRevmsgLocOverflow.setStatus("mandatory")
_AzcACLRevmsgCtlErr_Type = Counter32
_AzcACLRevmsgCtlErr_Object = MibScalar
azcACLRevmsgCtlErr = _AzcACLRevmsgCtlErr_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 45),
    _AzcACLRevmsgCtlErr_Type()
)
azcACLRevmsgCtlErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcACLRevmsgCtlErr.setStatus("mandatory")
_AzcACLRevmsgCtlOverflow_Type = Counter32
_AzcACLRevmsgCtlOverflow_Object = MibScalar
azcACLRevmsgCtlOverflow = _AzcACLRevmsgCtlOverflow_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 46),
    _AzcACLRevmsgCtlOverflow_Type()
)
azcACLRevmsgCtlOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcACLRevmsgCtlOverflow.setStatus("mandatory")
_AzcACLMemAllocs_Type = Gauge32
_AzcACLMemAllocs_Object = MibScalar
azcACLMemAllocs = _AzcACLMemAllocs_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 47),
    _AzcACLMemAllocs_Type()
)
azcACLMemAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcACLMemAllocs.setStatus("mandatory")
_AzcACLMemAllocErr_Type = Counter32
_AzcACLMemAllocErr_Object = MibScalar
azcACLMemAllocErr = _AzcACLMemAllocErr_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 48),
    _AzcACLMemAllocErr_Type()
)
azcACLMemAllocErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcACLMemAllocErr.setStatus("mandatory")
_AzcActivationKey_Type = DisplayString
_AzcActivationKey_Object = MibScalar
azcActivationKey = _AzcActivationKey_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 49),
    _AzcActivationKey_Type()
)
azcActivationKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcActivationKey.setStatus("mandatory")
_AzcHostID_Type = DisplayString
_AzcHostID_Object = MibScalar
azcHostID = _AzcHostID_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 50),
    _AzcHostID_Type()
)
azcHostID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcHostID.setStatus("mandatory")
_AzcIntIf_Type = DisplayString
_AzcIntIf_Object = MibScalar
azcIntIf = _AzcIntIf_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 51),
    _AzcIntIf_Type()
)
azcIntIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcIntIf.setStatus("mandatory")
_AzcExtIf_Type = DisplayString
_AzcExtIf_Object = MibScalar
azcExtIf = _AzcExtIf_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 52),
    _AzcExtIf_Type()
)
azcExtIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcExtIf.setStatus("mandatory")
_AzcMaxTimeout_Type = Integer32
_AzcMaxTimeout_Object = MibScalar
azcMaxTimeout = _AzcMaxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 53),
    _AzcMaxTimeout_Type()
)
azcMaxTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcMaxTimeout.setStatus("mandatory")
_AzcMaxIdleTimeout_Type = Integer32
_AzcMaxIdleTimeout_Object = MibScalar
azcMaxIdleTimeout = _AzcMaxIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 54),
    _AzcMaxIdleTimeout_Type()
)
azcMaxIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcMaxIdleTimeout.setStatus("mandatory")
_AzcPingPeriod_Type = Integer32
_AzcPingPeriod_Object = MibScalar
azcPingPeriod = _AzcPingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 55),
    _AzcPingPeriod_Type()
)
azcPingPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcPingPeriod.setStatus("mandatory")
_AzcLoginURL_Type = DisplayString
_AzcLoginURL_Object = MibScalar
azcLoginURL = _AzcLoginURL_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 56),
    _AzcLoginURL_Type()
)
azcLoginURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcLoginURL.setStatus("mandatory")
_AzcIPAddress_Type = DisplayString
_AzcIPAddress_Object = MibScalar
azcIPAddress = _AzcIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 57),
    _AzcIPAddress_Type()
)
azcIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcIPAddress.setStatus("mandatory")
_AzcExtIPAddress_Type = DisplayString
_AzcExtIPAddress_Object = MibScalar
azcExtIPAddress = _AzcExtIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 58),
    _AzcExtIPAddress_Type()
)
azcExtIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcExtIPAddress.setStatus("mandatory")
_AzcDNSIPAddress_Type = DisplayString
_AzcDNSIPAddress_Object = MibScalar
azcDNSIPAddress = _AzcDNSIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 59),
    _AzcDNSIPAddress_Type()
)
azcDNSIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcDNSIPAddress.setStatus("mandatory")
_AzcDHCPIPAddress_Type = DisplayString
_AzcDHCPIPAddress_Object = MibScalar
azcDHCPIPAddress = _AzcDHCPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 60),
    _AzcDHCPIPAddress_Type()
)
azcDHCPIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcDHCPIPAddress.setStatus("mandatory")
_AzcProxyHost_Type = DisplayString
_AzcProxyHost_Object = MibScalar
azcProxyHost = _AzcProxyHost_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 61),
    _AzcProxyHost_Type()
)
azcProxyHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcProxyHost.setStatus("mandatory")
_AzcProxyPorts_Type = DisplayString
_AzcProxyPorts_Object = MibScalar
azcProxyPorts = _AzcProxyPorts_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 62),
    _AzcProxyPorts_Type()
)
azcProxyPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcProxyPorts.setStatus("mandatory")
_AzcMailRelayHost_Type = DisplayString
_AzcMailRelayHost_Object = MibScalar
azcMailRelayHost = _AzcMailRelayHost_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 63),
    _AzcMailRelayHost_Type()
)
azcMailRelayHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcMailRelayHost.setStatus("mandatory")
_AzcRADIUSAlivePeriod_Type = Integer32
_AzcRADIUSAlivePeriod_Object = MibScalar
azcRADIUSAlivePeriod = _AzcRADIUSAlivePeriod_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 64),
    _AzcRADIUSAlivePeriod_Type()
)
azcRADIUSAlivePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcRADIUSAlivePeriod.setStatus("mandatory")
_AzcRADIUSAliveTrigger_Type = Integer32
_AzcRADIUSAliveTrigger_Object = MibScalar
azcRADIUSAliveTrigger = _AzcRADIUSAliveTrigger_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 65),
    _AzcRADIUSAliveTrigger_Type()
)
azcRADIUSAliveTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcRADIUSAliveTrigger.setStatus("mandatory")
_AzcWhitelist_Type = DisplayString
_AzcWhitelist_Object = MibScalar
azcWhitelist = _AzcWhitelist_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 66),
    _AzcWhitelist_Type()
)
azcWhitelist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcWhitelist.setStatus("mandatory")
_AzcBlackList_Type = DisplayString
_AzcBlackList_Object = MibScalar
azcBlackList = _AzcBlackList_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 67),
    _AzcBlackList_Type()
)
azcBlackList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcBlackList.setStatus("mandatory")
_AzcDemoAccounts_Type = DisplayString
_AzcDemoAccounts_Object = MibScalar
azcDemoAccounts = _AzcDemoAccounts_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 68),
    _AzcDemoAccounts_Type()
)
azcDemoAccounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcDemoAccounts.setStatus("mandatory")
_AzcUDPFilter_Type = Integer32
_AzcUDPFilter_Object = MibScalar
azcUDPFilter = _AzcUDPFilter_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 69),
    _AzcUDPFilter_Type()
)
azcUDPFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcUDPFilter.setStatus("mandatory")
_AzcCutTime_Type = DisplayString
_AzcCutTime_Object = MibScalar
azcCutTime = _AzcCutTime_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 70),
    _AzcCutTime_Type()
)
azcCutTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcCutTime.setStatus("mandatory")
_AzcCutSafetyTime_Type = Integer32
_AzcCutSafetyTime_Object = MibScalar
azcCutSafetyTime = _AzcCutSafetyTime_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 71),
    _AzcCutSafetyTime_Type()
)
azcCutSafetyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcCutSafetyTime.setStatus("mandatory")


class _AzcRADIUSActivated_Type(Integer32):
    """Custom type azcRADIUSActivated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AzcRADIUSActivated_Type.__name__ = "Integer32"
_AzcRADIUSActivated_Object = MibScalar
azcRADIUSActivated = _AzcRADIUSActivated_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 72),
    _AzcRADIUSActivated_Type()
)
azcRADIUSActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcRADIUSActivated.setStatus("mandatory")


class _AzcMACCheckMode_Type(Integer32):
    """Custom type azcMACCheckMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AzcMACCheckMode_Type.__name__ = "Integer32"
_AzcMACCheckMode_Object = MibScalar
azcMACCheckMode = _AzcMACCheckMode_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 73),
    _AzcMACCheckMode_Type()
)
azcMACCheckMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcMACCheckMode.setStatus("mandatory")


class _AzcNATState_Type(Integer32):
    """Custom type azcNATState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AzcNATState_Type.__name__ = "Integer32"
_AzcNATState_Object = MibScalar
azcNATState = _AzcNATState_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 74),
    _AzcNATState_Type()
)
azcNATState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcNATState.setStatus("mandatory")


class _AzcDHCPState_Type(Integer32):
    """Custom type azcDHCPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AzcDHCPState_Type.__name__ = "Integer32"
_AzcDHCPState_Object = MibScalar
azcDHCPState = _AzcDHCPState_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 75),
    _AzcDHCPState_Type()
)
azcDHCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcDHCPState.setStatus("mandatory")


class _AzcSSLState_Type(Integer32):
    """Custom type azcSSLState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AzcSSLState_Type.__name__ = "Integer32"
_AzcSSLState_Object = MibScalar
azcSSLState = _AzcSSLState_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 76),
    _AzcSSLState_Type()
)
azcSSLState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcSSLState.setStatus("mandatory")


class _AzcSNMPTrapState_Type(Integer32):
    """Custom type azcSNMPTrapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AzcSNMPTrapState_Type.__name__ = "Integer32"
_AzcSNMPTrapState_Object = MibScalar
azcSNMPTrapState = _AzcSNMPTrapState_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 77),
    _AzcSNMPTrapState_Type()
)
azcSNMPTrapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcSNMPTrapState.setStatus("mandatory")


class _AzcMACAuthState_Type(Integer32):
    """Custom type azcMACAuthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AzcMACAuthState_Type.__name__ = "Integer32"
_AzcMACAuthState_Object = MibScalar
azcMACAuthState = _AzcMACAuthState_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 78),
    _AzcMACAuthState_Type()
)
azcMACAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcMACAuthState.setStatus("mandatory")
_AzcMACRealm_Type = DisplayString
_AzcMACRealm_Object = MibScalar
azcMACRealm = _AzcMACRealm_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 79),
    _AzcMACRealm_Type()
)
azcMACRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcMACRealm.setStatus("mandatory")
_AzcMACPassword_Type = DisplayString
_AzcMACPassword_Object = MibScalar
azcMACPassword = _AzcMACPassword_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 80),
    _AzcMACPassword_Type()
)
azcMACPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcMACPassword.setStatus("mandatory")
_AzcNATDArgs_Type = DisplayString
_AzcNATDArgs_Object = MibScalar
azcNATDArgs = _AzcNATDArgs_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 81),
    _AzcNATDArgs_Type()
)
azcNATDArgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcNATDArgs.setStatus("mandatory")
_AzcSyslogFacility_Type = Integer32
_AzcSyslogFacility_Object = MibScalar
azcSyslogFacility = _AzcSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 82),
    _AzcSyslogFacility_Type()
)
azcSyslogFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcSyslogFacility.setStatus("mandatory")


class _AzcSyslogLevel_Type(Integer32):
    """Custom type azcSyslogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("alsoInfo", 6),
          ("alsoWarnings", 4),
          ("nothing", 0),
          ("onlyErrors", 1))
    )


_AzcSyslogLevel_Type.__name__ = "Integer32"
_AzcSyslogLevel_Object = MibScalar
azcSyslogLevel = _AzcSyslogLevel_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 83),
    _AzcSyslogLevel_Type()
)
azcSyslogLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcSyslogLevel.setStatus("mandatory")
_AzcQOSClass1_Type = DisplayString
_AzcQOSClass1_Object = MibScalar
azcQOSClass1 = _AzcQOSClass1_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 84),
    _AzcQOSClass1_Type()
)
azcQOSClass1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcQOSClass1.setStatus("mandatory")
_AzcQOSClass2_Type = DisplayString
_AzcQOSClass2_Object = MibScalar
azcQOSClass2 = _AzcQOSClass2_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 85),
    _AzcQOSClass2_Type()
)
azcQOSClass2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcQOSClass2.setStatus("mandatory")
_AzcQOSClass3_Type = DisplayString
_AzcQOSClass3_Object = MibScalar
azcQOSClass3 = _AzcQOSClass3_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 86),
    _AzcQOSClass3_Type()
)
azcQOSClass3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcQOSClass3.setStatus("mandatory")
_AzcQOSClassDefault_Type = DisplayString
_AzcQOSClassDefault_Object = MibScalar
azcQOSClassDefault = _AzcQOSClassDefault_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 87),
    _AzcQOSClassDefault_Type()
)
azcQOSClassDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcQOSClassDefault.setStatus("mandatory")
_AzcLocation_Type = DisplayString
_AzcLocation_Object = MibScalar
azcLocation = _AzcLocation_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 88),
    _AzcLocation_Type()
)
azcLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcLocation.setStatus("mandatory")
_AzcUptime_Type = Integer32
_AzcUptime_Object = MibScalar
azcUptime = _AzcUptime_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 89),
    _AzcUptime_Type()
)
azcUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcUptime.setStatus("mandatory")
_AzcTrialTime_Type = Integer32
_AzcTrialTime_Object = MibScalar
azcTrialTime = _AzcTrialTime_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 90),
    _AzcTrialTime_Type()
)
azcTrialTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcTrialTime.setStatus("mandatory")
_AzcTrialLockime_Type = Integer32
_AzcTrialLockime_Object = MibScalar
azcTrialLockime = _AzcTrialLockime_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 91),
    _AzcTrialLockime_Type()
)
azcTrialLockime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcTrialLockime.setStatus("mandatory")
_AzcNokiaAuthMode_Type = Integer32
_AzcNokiaAuthMode_Object = MibScalar
azcNokiaAuthMode = _AzcNokiaAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 92),
    _AzcNokiaAuthMode_Type()
)
azcNokiaAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcNokiaAuthMode.setStatus("mandatory")
_AzcActiveLogins_Type = Integer32
_AzcActiveLogins_Object = MibScalar
azcActiveLogins = _AzcActiveLogins_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 93),
    _AzcActiveLogins_Type()
)
azcActiveLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcActiveLogins.setStatus("mandatory")
_AzcZoneName_Type = DisplayString
_AzcZoneName_Object = MibScalar
azcZoneName = _AzcZoneName_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 94),
    _AzcZoneName_Type()
)
azcZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcZoneName.setStatus("mandatory")
_AzcLoginTime_Type = Integer32
_AzcLoginTime_Object = MibScalar
azcLoginTime = _AzcLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 95),
    _AzcLoginTime_Type()
)
azcLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azcLoginTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOKIA-AZC-SYSTEM-MIB",
    **{"nokia": nokia,
       "nokiaProducts": nokiaProducts,
       "azcProducts": azcProducts,
       "azcSystem": azcSystem,
       "azcStatusGroup": azcStatusGroup,
       "azcVersion": azcVersion,
       "azcRelease": azcRelease,
       "azcStarted": azcStarted,
       "azcLoginsSuccess": azcLoginsSuccess,
       "azcLoginsAuthFailures": azcLoginsAuthFailures,
       "azcLoginsACLFailures": azcLoginsACLFailures,
       "azcLoginsDuplFailures": azcLoginsDuplFailures,
       "azcLoginsSpaceFailures": azcLoginsSpaceFailures,
       "azcLoginsRADIUSFailures": azcLoginsRADIUSFailures,
       "azcLoginsRADIUSACLFailures": azcLoginsRADIUSACLFailures,
       "azcAutologoffsRADIUS": azcAutologoffsRADIUS,
       "azcAutologoffsPing": azcAutologoffsPing,
       "azcAutologoffsMAC": azcAutologoffsMAC,
       "azcAutologoffsACL": azcAutologoffsACL,
       "azcAutologoffsQuota": azcAutologoffsQuota,
       "azcAutologoffsMaxTime": azcAutologoffsMaxTime,
       "azcAutologoffsIdletimer": azcAutologoffsIdletimer,
       "azcPktsIntIn": azcPktsIntIn,
       "azcPktsIntOut": azcPktsIntOut,
       "azcBytesIntIn": azcBytesIntIn,
       "azcBytesIntOut": azcBytesIntOut,
       "azcPktsExtIn": azcPktsExtIn,
       "azcPktsExtOut": azcPktsExtOut,
       "azcBytesExtIn": azcBytesExtIn,
       "azcBytesExtOut": azcBytesExtOut,
       "azcPktsNattedIn": azcPktsNattedIn,
       "azcPktsNattedOut": azcPktsNattedOut,
       "azcBytesNattedIn": azcBytesNattedIn,
       "azcBytesNattedOut": azcBytesNattedOut,
       "azcPktsNattedErrIn": azcPktsNattedErrIn,
       "azcPktsNattedErrOut": azcPktsNattedErrOut,
       "azcBytesNattedErrIn": azcBytesNattedErrIn,
       "azcBytesNattedErrOut": azcBytesNattedErrOut,
       "azcPktsRejInt": azcPktsRejInt,
       "azcPktsRejExt": azcPktsRejExt,
       "azcBytesRejInt": azcBytesRejInt,
       "azcBytesRejExt": azcBytesRejExt,
       "azcACLSelectErr": azcACLSelectErr,
       "azcACLSendmsgErr": azcACLSendmsgErr,
       "azcACLRevmsgErr": azcACLRevmsgErr,
       "azcACLRevmsgOverflow": azcACLRevmsgOverflow,
       "azcACLSendmsgLocErr": azcACLSendmsgLocErr,
       "azcACLRevmsgLocErr": azcACLRevmsgLocErr,
       "azcACLRevmsgLocOverflow": azcACLRevmsgLocOverflow,
       "azcACLRevmsgCtlErr": azcACLRevmsgCtlErr,
       "azcACLRevmsgCtlOverflow": azcACLRevmsgCtlOverflow,
       "azcACLMemAllocs": azcACLMemAllocs,
       "azcACLMemAllocErr": azcACLMemAllocErr,
       "azcActivationKey": azcActivationKey,
       "azcHostID": azcHostID,
       "azcIntIf": azcIntIf,
       "azcExtIf": azcExtIf,
       "azcMaxTimeout": azcMaxTimeout,
       "azcMaxIdleTimeout": azcMaxIdleTimeout,
       "azcPingPeriod": azcPingPeriod,
       "azcLoginURL": azcLoginURL,
       "azcIPAddress": azcIPAddress,
       "azcExtIPAddress": azcExtIPAddress,
       "azcDNSIPAddress": azcDNSIPAddress,
       "azcDHCPIPAddress": azcDHCPIPAddress,
       "azcProxyHost": azcProxyHost,
       "azcProxyPorts": azcProxyPorts,
       "azcMailRelayHost": azcMailRelayHost,
       "azcRADIUSAlivePeriod": azcRADIUSAlivePeriod,
       "azcRADIUSAliveTrigger": azcRADIUSAliveTrigger,
       "azcWhitelist": azcWhitelist,
       "azcBlackList": azcBlackList,
       "azcDemoAccounts": azcDemoAccounts,
       "azcUDPFilter": azcUDPFilter,
       "azcCutTime": azcCutTime,
       "azcCutSafetyTime": azcCutSafetyTime,
       "azcRADIUSActivated": azcRADIUSActivated,
       "azcMACCheckMode": azcMACCheckMode,
       "azcNATState": azcNATState,
       "azcDHCPState": azcDHCPState,
       "azcSSLState": azcSSLState,
       "azcSNMPTrapState": azcSNMPTrapState,
       "azcMACAuthState": azcMACAuthState,
       "azcMACRealm": azcMACRealm,
       "azcMACPassword": azcMACPassword,
       "azcNATDArgs": azcNATDArgs,
       "azcSyslogFacility": azcSyslogFacility,
       "azcSyslogLevel": azcSyslogLevel,
       "azcQOSClass1": azcQOSClass1,
       "azcQOSClass2": azcQOSClass2,
       "azcQOSClass3": azcQOSClass3,
       "azcQOSClassDefault": azcQOSClassDefault,
       "azcLocation": azcLocation,
       "azcUptime": azcUptime,
       "azcTrialTime": azcTrialTime,
       "azcTrialLockime": azcTrialLockime,
       "azcNokiaAuthMode": azcNokiaAuthMode,
       "azcActiveLogins": azcActiveLogins,
       "azcZoneName": azcZoneName,
       "azcLoginTime": azcLoginTime}
)
